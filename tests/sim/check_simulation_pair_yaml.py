#!/usr/bin/env python3
"""/** [AI] Model: Claude Opus 4.8 | 2026-06-20 | 生成 device_pair.generated.yaml 的免框架自检（Chunk 8） */

无框架可直接运行的自检：`python tests/sim/check_simulation_pair_yaml.py`。

之所以不用 pytest：本环境 pytest==5.4.3 与 Python 3.11 的 AST 不兼容
（assertion-rewrite 报 `TypeError: required field "lineno" missing from alias`），
连 `pytest --version` 都跑不起来。按任务降级条款改为 import-light 的 assert 自检，
覆盖 test_simulation_pairs.py 未覆盖的缺口（missing_sim_policy 缺省兜底）。

断言点：
- 生成 YAML 与 Phase 1A PairRegistry schema 兼容（可被 PairRegistry 直接加载）。
- real→virtual 映射正确，twin_observed / twin_throttle_hz 透传。
- 缺失走 missing policy：显式 skip 保留；条目缺 missing_sim_policy 时兜底 stub；
  YAML 未声明的 real_class 走 registry 默认策略且 explicit=False。
- prepare_simulation_pairs 在线产出 generated yaml + manifest（real_classes 排序）。
"""

import tempfile
from pathlib import Path

from unilabos.app.simulation_pairs import compile_bundle_to_yaml, prepare_simulation_pairs
from unilabos.registry.pair_registry import PairRegistry

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
        {"real": "no_policy_dev", "virtual": None},  # 缺 missing_sim_policy → 编译默认 stub
    ],
    "warnings": [],
}

GRAPH = {"nodes": [{"class": "dalong_heaterstirrer"}, {"class": "cam"}, {"class": "no_policy_dev"}]}


class _FakeClient:
    """模拟 UniLabClient.resolve_simulation_pairs，返回本地 bundle dict。"""

    def __init__(self, bundle):
        self._bundle = bundle

    def resolve_simulation_pairs(self, real_classes, **kwargs):
        return self._bundle


def check_compile_schema_and_mapping() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        pair_file = Path(tmp) / "device_pair.generated.yaml"
        pair_file.write_text(compile_bundle_to_yaml(BUNDLE["pairs"]), encoding="utf-8")

        # Phase 1A schema 兼容：PairRegistry 能直接加载该 YAML。
        reg = PairRegistry(pair_file)

        heater = reg.lookup("dalong_heaterstirrer")
        assert heater.virtual == "community.dalong.virtual_x", heater.virtual
        assert heater.twin_observed == ["temperature", "rpm"], heater.twin_observed
        assert heater.twin_throttle_hz == 20, heater.twin_throttle_hz

        cam = reg.lookup("cam")
        assert cam.virtual is None, cam.virtual
        assert cam.missing_sim_policy == "skip", cam.missing_sim_policy

        # 缺 missing_sim_policy 的条目兜底为 stub。
        no_policy = reg.lookup("no_policy_dev")
        assert no_policy.virtual is None, no_policy.virtual
        assert no_policy.missing_sim_policy == "stub", no_policy.missing_sim_policy

        # YAML 未声明的 real_class → registry 默认策略 + explicit=False。
        unknown = reg.lookup("never_declared")
        assert unknown.explicit is False, unknown.explicit
        assert unknown.missing_sim_policy == "stub", unknown.missing_sim_policy


def check_prepare_generates_yaml_and_manifest() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        result = prepare_simulation_pairs(
            GRAPH, working_dir=tmp, mode="sim", http_client=_FakeClient(BUNDLE)
        )
        assert result.generated_yaml is not None
        assert result.bundle_version == "2026-06-20T00:00:00Z", result.bundle_version

        reg = PairRegistry(Path(result.generated_yaml))
        assert reg.lookup("dalong_heaterstirrer").virtual == "community.dalong.virtual_x"
        assert reg.lookup("cam").missing_sim_policy == "skip"

        import json

        manifest = json.loads(
            (Path(tmp) / "simulation_pairs" / "manifest.json").read_text(encoding="utf-8")
        )
        assert manifest["real_classes"] == ["cam", "dalong_heaterstirrer", "no_policy_dev"], manifest[
            "real_classes"
        ]
        assert manifest["generated_yaml"] == "device_pair.generated.yaml"


def main() -> None:
    checks = [
        ("compile schema + mapping + missing policy", check_compile_schema_and_mapping),
        ("prepare generates yaml + manifest", check_prepare_generates_yaml_and_manifest),
    ]
    for name, fn in checks:
        fn()
        print(f"[OK] {name}")
    print(f"device_pair.generated.yaml 自检全部通过：{len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
