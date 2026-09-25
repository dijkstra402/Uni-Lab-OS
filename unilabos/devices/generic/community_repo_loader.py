from __future__ import annotations

import hashlib
import importlib
import importlib.util
import inspect
import sys
from pathlib import Path
from typing import Any


def _json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_safe(v) for v in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return repr(value)


class CommunityRepoLoader:
    """
    轻量纳管驱动：
    - 启动时只保存外部仓库元数据，不立即 import 上游驱动，避免依赖缺失导致 Unilab 启动失败
    - 需要时通过 `probe_import` / `instantiate` / `call` 惰性加载上游类
    """

    def __init__(
        self,
        repo_root: str,
        source_file: str | None = None,
        class_name: str | None = None,
        import_roots: list[str] | None = None,
        init_kwargs: dict[str, Any] | None = None,
        candidate_methods: list[str] | None = None,
        action_targets: dict[str, str] | None = None,
        metadata: dict[str, Any] | None = None,
        auto_instantiate: bool = False,
    ) -> None:
        self.repo_root = Path(repo_root).expanduser().resolve()
        self.source_file = source_file or ""
        self.class_name = class_name or ""
        self.import_roots = list(import_roots or [])
        self.init_kwargs = dict(init_kwargs or {})
        self.candidate_methods = list(candidate_methods or [])
        self.action_targets = dict(action_targets or {})
        self.metadata = dict(metadata or {})
        if not self.action_targets:
            self.action_targets = dict(self.metadata.get("action_targets") or {})

        self.loaded = False
        self.ready = False
        self.load_error = ""
        self.instance: Any | None = None
        self._target_class: type[Any] | None = None
        self._target_module: Any | None = None
        self._module_name = self.metadata.get("module_name") or ""

        if auto_instantiate:
            self.instantiate()

    def _source_path(self) -> Path:
        if not self.source_file:
            raise ValueError("source_file is empty")
        return (self.repo_root / self.source_file).resolve()

    def _resolved_import_roots(self) -> list[Path]:
        roots = [self.repo_root]
        for rel in self.import_roots:
            p = (self.repo_root / rel).resolve()
            if p.exists():
                roots.append(p)
        for name in ("src", "python", "lib"):
            p = (self.repo_root / name).resolve()
            if p.exists():
                roots.append(p)
        dedup: list[Path] = []
        seen: set[str] = set()
        for root in roots:
            key = str(root)
            if key not in seen:
                dedup.append(root)
                seen.add(key)
        return dedup

    def _ensure_paths(self) -> None:
        for root in reversed(self._resolved_import_roots()):
            root_str = str(root)
            if root_str not in sys.path:
                sys.path.insert(0, root_str)

    def _build_module_name(self) -> str:
        if self._module_name:
            return self._module_name
        digest = hashlib.sha1(f"{self.repo_root}|{self.source_file}|{self.class_name}".encode("utf-8")).hexdigest()[:12]
        self._module_name = f"community_repo_{digest}"
        return self._module_name

    def _module_name_candidates(self) -> list[str]:
        source_path = self._source_path()
        names: list[str] = []
        for root in self._resolved_import_roots():
            try:
                rel = source_path.relative_to(root)
            except Exception:
                continue
            if rel.suffix != ".py":
                continue
            parts = list(rel.with_suffix("").parts)
            if parts and parts[-1] == "__init__":
                parts = parts[:-1]
            if not parts:
                continue
            name = ".".join(parts)
            if name and name not in names:
                names.append(name)
        return names

    def _load_target_module(self) -> Any:
        if self._target_module is not None:
            return self._target_module
        self._ensure_paths()
        source_path = self._source_path()
        if not source_path.exists():
            raise FileNotFoundError(f"source file not found: {source_path}")

        module_errors: list[str] = []
        for candidate in self._module_name_candidates():
            try:
                module = importlib.import_module(candidate)
                self._module_name = candidate
                self._target_module = module
                self.loaded = True
                self.load_error = ""
                return module
            except Exception as exc:
                module_errors.append(f"{candidate}: {exc}")

        module_name = self._build_module_name()
        spec = importlib.util.spec_from_file_location(module_name, source_path)
        if spec is None or spec.loader is None:
            if module_errors:
                raise ImportError(f"cannot build import spec for: {source_path}; import errors: {module_errors[:3]}")
            raise ImportError(f"cannot build import spec for: {source_path}")

        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        self._target_module = module
        self.loaded = True
        self.load_error = ""
        return module

    def _load_target_class(self) -> type[Any]:
        if self._target_class is not None:
            return self._target_class
        if not self.class_name:
            raise ValueError("class_name is empty")

        module = self._load_target_module()
        target = getattr(module, self.class_name)
        self._target_class = target
        return target

    def get_metadata(self) -> dict[str, Any]:
        return {
            "repo_root": str(self.repo_root),
            "source_file": self.source_file,
            "class_name": self.class_name,
            "import_roots": self.import_roots,
            "candidate_methods": list(self.candidate_methods),
            "action_targets": _json_safe(self.action_targets),
            "loaded": self.loaded,
            "ready": self.ready,
            "load_error": self.load_error,
            "metadata": _json_safe(self.metadata),
        }

    def list_methods(self) -> list[str]:
        if self.candidate_methods:
            return list(self.candidate_methods)
        try:
            if self.class_name:
                target = self._load_target_class()
                members = inspect.getmembers(target)
            else:
                target = self._load_target_module()
                members = inspect.getmembers(target)
        except Exception:
            return []
        methods: list[str] = []
        for name, value in members:
            if name.startswith("_"):
                continue
            if callable(value):
                methods.append(name)
        self.candidate_methods = methods
        return methods

    def probe_import(self) -> dict[str, Any]:
        try:
            if self.class_name:
                target = self._load_target_class()
                methods = self.list_methods()
                return {
                    "success": True,
                    "class_name": getattr(target, "__name__", self.class_name),
                    "module_name": getattr(target, "__module__", self._module_name),
                    "methods": methods,
                }
            module = self._load_target_module()
            methods = self.list_methods()
            return {
                "success": True,
                "class_name": "",
                "module_name": getattr(module, "__name__", self._module_name),
                "methods": methods,
            }
        except Exception as exc:
            self.loaded = False
            self.load_error = str(exc)
            return {
                "success": False,
                "error": str(exc),
                "class_name": self.class_name,
                "source_file": self.source_file,
            }

    def instantiate(self, init_kwargs: dict[str, Any] | None = None, force: bool = False) -> dict[str, Any]:
        if not self.class_name:
            try:
                module = self._load_target_module()
                self.ready = True
                return {
                    "success": True,
                    "module_mode": True,
                    "module_name": getattr(module, "__name__", self._module_name),
                }
            except Exception as exc:
                self.ready = False
                self.load_error = str(exc)
                return {"success": False, "error": str(exc), "class_name": self.class_name}
        if self.instance is not None and not force:
            self.ready = True
            return {"success": True, "reused": True, "class_name": self.class_name}
        try:
            target = self._load_target_class()
            kwargs = dict(self.init_kwargs)
            if init_kwargs:
                kwargs.update(init_kwargs)
            self.instance = target(**kwargs)
            self.ready = True
            return {
                "success": True,
                "class_name": self.class_name,
                "module_name": getattr(target, "__module__", self._module_name),
            }
        except Exception as exc:
            self.ready = False
            self.load_error = str(exc)
            return {"success": False, "error": str(exc), "class_name": self.class_name}

    def call(
        self,
        method: str,
        kwargs: dict[str, Any] | None = None,
        auto_instantiate: bool = True,
    ) -> dict[str, Any]:
        resolved_method = self.action_targets.get(method, method)
        if not self.class_name:
            try:
                module = self._load_target_module()
                if not hasattr(module, resolved_method):
                    return {"success": False, "error": f"method not found: {method}"}
                target = getattr(module, resolved_method)
                if callable(target):
                    result = target(**(kwargs or {}))
                else:
                    if kwargs:
                        return {
                            "success": False,
                            "error": f"attribute '{method}' is not callable; kwargs are not supported",
                        }
                    result = target
                self.ready = True
                return {"success": True, "result": _json_safe(result)}
            except Exception as exc:
                return {"success": False, "error": str(exc)}
        if auto_instantiate and self.instance is None:
            created = self.instantiate()
            if not created.get("success"):
                return created
        if self.instance is None:
            return {"success": False, "error": "instance is not ready"}
        if resolved_method.startswith("__qcodes_param_get__"):
            param_name = resolved_method.replace("__qcodes_param_get__", "", 1)
            try:
                params = getattr(self.instance, "parameters", None)
                if isinstance(params, dict) and param_name in params:
                    result = params[param_name].get()
                elif hasattr(self.instance, param_name):
                    result = getattr(self.instance, param_name).get()
                else:
                    return {"success": False, "error": f"qcodes parameter not found: {param_name}"}
                return {"success": True, "result": _json_safe(result)}
            except Exception as exc:
                return {"success": False, "error": str(exc)}
        if resolved_method.startswith("__qcodes_param_set__"):
            param_name = resolved_method.replace("__qcodes_param_set__", "", 1)
            value = None
            if kwargs:
                if "value" in kwargs:
                    value = kwargs["value"]
                elif len(kwargs) == 1:
                    value = next(iter(kwargs.values()))
            if value is None:
                return {"success": False, "error": f"missing value for qcodes parameter: {param_name}"}
            try:
                params = getattr(self.instance, "parameters", None)
                if isinstance(params, dict) and param_name in params:
                    result = params[param_name].set(value)
                elif hasattr(self.instance, param_name):
                    result = getattr(self.instance, param_name).set(value)
                else:
                    return {"success": False, "error": f"qcodes parameter not found: {param_name}"}
                return {"success": True, "result": _json_safe(result)}
            except Exception as exc:
                return {"success": False, "error": str(exc)}
        if not hasattr(self.instance, resolved_method):
            return {"success": False, "error": f"method not found: {method}"}
        try:
            target = getattr(self.instance, resolved_method)
            if callable(target):
                result = target(**(kwargs or {}))
            else:
                if kwargs:
                    return {
                        "success": False,
                        "error": f"attribute '{method}' is not callable; kwargs are not supported",
                    }
                result = target
            return {"success": True, "result": _json_safe(result)}
        except Exception as exc:
            return {"success": False, "error": str(exc)}
