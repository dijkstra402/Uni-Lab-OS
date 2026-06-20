"""Edge 仿真配对编排与 PairRegistry fallback 优先级的最小单测（不连真实后端）。"""

import json
from pathlib import Path

import pytest

from unilabos.app.simulation_pairs import (
    SimulationPairError,
    compile_bundle_to_yaml,
    prepare_simulation_pairs,
)
from unilabos.registry.pair_registry import (
    PairRegistry,
    init_pair_registry,
    resolve_pair_registry_path,
)

GRAPH = {"nodes": [{"class": "dalong_heaterstirrer"}, {"class": "cam"}]}

BUNDLE = {
    "bundle_version": "2026-06-20T00:00:00Z",
    "pairs": [
        {
            "real": "dalong_heaterstirrer",
            "virtual": "community.dalong.virtual_x",
            "missing_sim_policy": "stub",
            "twin_observed": ["temperature", "rpm"],
            "twin_throttle_hz": 20,
        },
        {"real": "cam", "virtual": None, "missing_sim_policy": "skip"},
    ],
    "warnings": [],
}


class _FakeClient:
    """模拟 UniLabClient.resolve_simulation_pairs，返回本地 bundle dict。"""

    def __init__(self, bundle=None, raise_exc=False):
        self._bundle = bundle
        self._raise = raise_exc

    def resolve_simulation_pairs(self, real_classes, **kwargs):
        if self._raise:
            raise ConnectionError("backend unreachable")
        return self._bundle


class _FakeResponse:
    def __init__(self, status_code=200, payload=None):
        self.status_code = status_code
        self.text = json.dumps(payload or {})
        self._payload = payload or {}

    def json(self):
        return self._payload


def test_resolve_simulation_pairs_builds_snake_case_payload(monkeypatch):
    """HTTPClient.resolve_simulation_pairs 契约：snake_case 请求体 + 返回 {code,data}。"""
    from unilabos.app.web.client import HTTPClient

    client = HTTPClient(remote_addr="http://backend", auth="tok")
    captured = {}

    def fake_post(url, json=None, headers=None, timeout=None):
        captured["url"] = url
        captured["json"] = json
        return _FakeResponse(200, {"code": 0, "data": {"bundle_version": "v1", "pairs": []}})

    monkeypatch.setattr(client._session, "post", fake_post)

    resp = client.resolve_simulation_pairs(
        ["dalong_heaterstirrer"], mode="sim", lab_uuid="L", edge_uuid="E"
    )
    assert resp == {"code": 0, "data": {"bundle_version": "v1", "pairs": []}}
    assert captured["url"].endswith("/lab/square/edge/simulation-pairs/resolve")
    assert captured["json"] == {
        "mode": "sim",
        "real_classes": ["dalong_heaterstirrer"],
        "lab_uuid": "L",
        "edge_uuid": "E",
        "package_locks": [],
        "unilabos_version": "",
    }


def test_resolve_simulation_pairs_non_200_returns_code_message(monkeypatch):
    from unilabos.app.web.client import HTTPClient

    client = HTTPClient(remote_addr="http://backend", auth="tok")

    def fake_post(url, json=None, headers=None, timeout=None):
        resp = _FakeResponse(503)
        resp.text = "unavailable"
        return resp

    monkeypatch.setattr(client._session, "post", fake_post)
    resp = client.resolve_simulation_pairs([], mode="twin")
    assert resp == {"code": 503, "message": "unavailable"}


def test_compile_bundle_to_yaml_compatible_with_pair_registry(tmp_path: Path):
    text = compile_bundle_to_yaml(BUNDLE["pairs"])
    pair_file = tmp_path / "device_pair.generated.yaml"
    pair_file.write_text(text, encoding="utf-8")
    reg = PairRegistry(pair_file)
    assert reg.lookup("dalong_heaterstirrer").virtual == "community.dalong.virtual_x"
    assert reg.lookup("dalong_heaterstirrer").twin_throttle_hz == 20
    assert reg.lookup("cam").missing_sim_policy == "skip"


def test_prepare_generates_yaml_and_manifest(tmp_path: Path):
    result = prepare_simulation_pairs(
        GRAPH, working_dir=tmp_path, mode="sim", http_client=_FakeClient(BUNDLE)
    )
    assert result.generated_yaml is not None
    assert result.bundle_version == "2026-06-20T00:00:00Z"

    reg = PairRegistry(Path(result.generated_yaml))
    assert reg.lookup("dalong_heaterstirrer").virtual == "community.dalong.virtual_x"

    manifest = json.loads((tmp_path / "simulation_pairs" / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["real_classes"] == ["cam", "dalong_heaterstirrer"]
    assert manifest["bundle_version"] == "2026-06-20T00:00:00Z"
    assert manifest["generated_yaml"] == "device_pair.generated.yaml"


def test_prepare_real_mode_is_noop(tmp_path: Path):
    result = prepare_simulation_pairs(GRAPH, working_dir=tmp_path, mode="real", http_client=_FakeClient(BUNDLE))
    assert result.generated_yaml is None
    assert not (tmp_path / "simulation_pairs").exists()


def test_prepare_fail_policy_without_virtual_raises(tmp_path: Path):
    bundle = {
        "bundle_version": "v1",
        "pairs": [{"real": "dalong_heaterstirrer", "virtual": None, "missing_sim_policy": "fail"}],
    }
    graph = {"nodes": [{"class": "dalong_heaterstirrer"}]}
    with pytest.raises(SimulationPairError, match="fail"):
        prepare_simulation_pairs(graph, working_dir=tmp_path, mode="sim", http_client=_FakeClient(bundle))


def test_offline_uses_compatible_cache(tmp_path: Path):
    # 先在线生成一次缓存
    prepare_simulation_pairs(GRAPH, working_dir=tmp_path, mode="sim", http_client=_FakeClient(BUNDLE))
    # 后端不可达：graph class 子集兼容 → 使用缓存 + offline 标记
    result = prepare_simulation_pairs(
        GRAPH, working_dir=tmp_path, mode="sim", http_client=_FakeClient(raise_exc=True)
    )
    assert result.offline is True
    assert result.generated_yaml is not None
    assert Path(result.generated_yaml).exists()


def test_offline_incompatible_cache_falls_back(tmp_path: Path):
    prepare_simulation_pairs(GRAPH, working_dir=tmp_path, mode="sim", http_client=_FakeClient(BUNDLE))
    # 新 graph 引入缓存未覆盖的 class → 不可用缓存，交还仓库默认（generated_yaml=None）
    new_graph = {"nodes": [{"class": "brand_new_device"}]}
    result = prepare_simulation_pairs(
        new_graph, working_dir=tmp_path, mode="sim", http_client=_FakeClient(raise_exc=True)
    )
    assert result.offline is True
    assert result.generated_yaml is None


def test_pair_registry_fallback_priority(tmp_path: Path):
    explicit = tmp_path / "explicit.yaml"
    explicit.write_text("pairs:\n- real: r\n  virtual: explicit_v\n", encoding="utf-8")
    generated = tmp_path / "generated.yaml"
    generated.write_text("pairs:\n- real: r\n  virtual: generated_v\n", encoding="utf-8")

    # explicit 最高优先
    assert resolve_pair_registry_path(explicit, generated) == explicit
    # 无 explicit 时用 generated
    assert resolve_pair_registry_path(None, generated) == generated
    # 都没有 → 回退仓库默认 device_pair.yaml
    repo_default = Path(resolve_pair_registry_path(None, None))
    assert repo_default.name == "device_pair.yaml"
    assert repo_default.exists()


def test_init_pair_registry_uses_generated_then_explicit(tmp_path: Path):
    explicit = tmp_path / "explicit.yaml"
    explicit.write_text("pairs:\n- real: r\n  virtual: explicit_v\n", encoding="utf-8")
    generated = tmp_path / "generated.yaml"
    generated.write_text("pairs:\n- real: r\n  virtual: generated_v\n", encoding="utf-8")

    reg = init_pair_registry(generated_path=generated)
    assert reg.lookup("r").virtual == "generated_v"

    reg = init_pair_registry(explicit_path=explicit, generated_path=generated)
    assert reg.lookup("r").virtual == "explicit_v"
