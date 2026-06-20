"""Registry for real/virtual device pairs."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, Literal

import yaml

MissingSimPolicy = Literal["stub", "skip", "fail"]


def _parse_twin(item: dict) -> tuple[list[str], float]:
    """解析孪生观测字段，兼容两种 YAML 格式：

    - 新版 Edge bundle：嵌套 ``twin_capability: {enabled, observed, throttle_hz}``；
      ``enabled`` 为假时视为无孪生（observed 置空），即使误填 observed 也不启用。
    - Phase 1A / 仓库默认：扁平 ``twin_observed`` + ``twin_throttle_hz``。
    """
    cap = item.get("twin_capability")
    if isinstance(cap, dict):
        if not cap.get("enabled"):
            return [], float(cap.get("throttle_hz", 10.0))
        return list(cap.get("observed") or []), float(cap.get("throttle_hz", 10.0))
    return list(item.get("twin_observed") or []), float(item.get("twin_throttle_hz", 10.0))


@dataclass(frozen=True)
class PairEntry:
    real: str
    virtual: str | None = None
    missing_sim_policy: MissingSimPolicy = "stub"
    engine: str = "none"
    twin_observed: list[str] = field(default_factory=list)
    twin_throttle_hz: float = 10.0
    explicit: bool = True


class PairRegistry:
    def __init__(self, path: str | Path | None = None, default_policy: MissingSimPolicy = "stub"):
        self.path = Path(path) if path else Path(__file__).with_name("device_pair.yaml")
        self.default_policy = default_policy
        self._pairs = self._load()

    def _load(self) -> dict[str, PairEntry]:
        if not self.path.exists():
            return {}
        raw = yaml.safe_load(self.path.read_text(encoding="utf-8")) or {}
        pairs = {}
        for item in raw.get("pairs", []):
            policy = item.get("missing_sim_policy", self.default_policy)
            if policy not in ("stub", "skip", "fail"):
                raise ValueError(f"invalid missing_sim_policy for {item.get('real')}: {policy}")
            real = item["real"]
            observed, throttle = _parse_twin(item)
            pairs[real] = PairEntry(
                real=real,
                virtual=item.get("virtual"),
                missing_sim_policy=policy,
                engine=item.get("engine") or "none",
                twin_observed=observed,
                twin_throttle_hz=throttle,
            )
        return pairs

    def lookup(self, real_class_name: str) -> PairEntry:
        return self._pairs.get(
            real_class_name,
            PairEntry(real=real_class_name, virtual=None, missing_sim_policy=self.default_policy, explicit=False),
        )

    def iter_stub_devices(self) -> Iterator[PairEntry]:
        for entry in self._pairs.values():
            if entry.virtual is None and entry.missing_sim_policy == "stub":
                yield entry


_default_registry: PairRegistry | None = None


def get_pair_registry() -> PairRegistry:
    global _default_registry
    if _default_registry is None:
        _default_registry = PairRegistry()
    return _default_registry


def lookup(real_class_name: str) -> PairEntry:
    return get_pair_registry().lookup(real_class_name)


def resolve_pair_registry_path(
    explicit_path: str | Path | None = None,
    generated_path: str | Path | None = None,
) -> Path:
    """选择 PairRegistry 数据源：显式配置 > Edge 生成 bundle > 仓库默认 device_pair.yaml。"""
    for candidate in (explicit_path, generated_path):
        if candidate and Path(candidate).exists():
            return Path(candidate)
    return Path(__file__).with_name("device_pair.yaml")


def set_pair_registry_path(path: str | Path) -> PairRegistry:
    """用给定 yaml 重建模块级单例，使 lookup() 立即读取该路径（如 Edge 生成的 bundle）。"""
    global _default_registry
    _default_registry = PairRegistry(path)
    return _default_registry


def init_pair_registry(
    explicit_path: str | Path | None = None,
    generated_path: str | Path | None = None,
) -> PairRegistry:
    """按优先级解析数据源并重建单例。"""
    return set_pair_registry_path(resolve_pair_registry_path(explicit_path, generated_path))
