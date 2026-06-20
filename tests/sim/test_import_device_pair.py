"""/** [AI] Model: Claude Opus 4.8 | 2026-06-20 | device_pair.yaml 导入脚本纯函数单测 */

只测纯映射/解析逻辑（class→uuid、字段映射、计划生成），用假模板列表，不连后端。
scripts/ 非 package，按文件路径加载脚本模块，避免触发 HTTPClient 重型导入。
"""

import importlib.util
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "import_device_pair_yaml_to_backend.py"
_spec = importlib.util.spec_from_file_location("import_device_pair_yaml_to_backend", _SCRIPT)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def test_device_class_namespace_rule():
    assert mod.device_class("virtual_heatchill", "") == "virtual_heatchill"
    assert mod.device_class("foo", "community.bar") == "community.bar.foo"
    assert mod.device_class("  x  ", "  ns ") == "ns.x"


def test_extract_record_prefers_effective_device_id():
    detail = {
        "name": "叠加显示名",  # 顶层 name 被 overlay 污染，不应采用
        "package_info": {"class_namespace": "community.acme"},
        "effective_template": {"device": {"id": "raw_class", "name": "也是显示名"}},
    }
    rec = mod.extract_record("uuid-1", detail)
    assert rec == {"uuid": "uuid-1", "name": "raw_class", "class_namespace": "community.acme"}


def test_extract_record_falls_back_to_top_name():
    detail = {"name": "fallback_class", "package_info": None, "effective_template": {}}
    rec = mod.extract_record("uuid-2", detail)
    assert rec == {"uuid": "uuid-2", "name": "fallback_class", "class_namespace": ""}


def test_build_class_index_namespace_and_dup_warning():
    templates = [
        {"uuid": "u-real", "name": "heaterstirrer.dalong", "class_namespace": ""},
        {"uuid": "u-comm", "name": "widget", "class_namespace": "community.acme"},
        {"uuid": "u-dup", "name": "heaterstirrer.dalong", "class_namespace": ""},
    ]
    index, warnings = mod.build_class_index(templates)
    assert index["heaterstirrer.dalong"] == "u-real"  # 取首个
    assert index["community.acme.widget"] == "u-comm"
    assert len(warnings) == 1 and "heaterstirrer.dalong" in warnings[0]


def test_build_create_payload_stub_no_virtual():
    pair = {"real": "Qone_nmr", "virtual": None, "missing_sim_policy": "fail"}
    payload = mod.build_create_payload(pair, "real-uuid", None, active=False)
    assert payload["pair_type"] == "stub"
    assert "virtual_resource_template_uuid" not in payload
    assert payload["supported_modes"] == ["sim"]
    assert payload["missing_sim_policy"] == "fail"
    assert payload["is_default"] is False
    assert payload["notes"] == mod.MIGRATION_NOTES
    assert "twin_config" not in payload


def test_build_create_payload_mock_with_twin_and_active():
    pair = {
        "real": "heaterstirrer.dalong",
        "virtual": "virtual_heatchill",
        "twin_observed": ["temperature", "rpm", "status"],
        "twin_throttle_hz": 2,
    }
    payload = mod.build_create_payload(pair, "real-uuid", "virtual-uuid", active=True)
    assert payload["pair_type"] == "mock"
    assert payload["virtual_resource_template_uuid"] == "virtual-uuid"
    assert payload["supported_modes"] == ["sim", "twin"]
    assert payload["missing_sim_policy"] == "stub"  # 未给则默认 stub
    assert payload["is_default"] is True
    assert payload["twin_config"] == {"observed": ["temperature", "rpm", "status"], "throttle_hz": 2}


def test_plan_pairs_matched_and_diagnostics():
    templates = [
        {"uuid": "u-h", "name": "heaterstirrer.dalong", "class_namespace": ""},
        {"uuid": "u-v", "name": "virtual_heatchill", "class_namespace": ""},
        {"uuid": "u-c", "name": "virtual_centrifuge", "class_namespace": ""},
    ]
    index, _ = mod.build_class_index(templates)
    pairs = [
        {"real": "heaterstirrer.dalong", "virtual": "virtual_heatchill", "twin_observed": ["temperature"]},
        {"real": "virtual_centrifuge", "virtual": "virtual_centrifuge"},  # 恒等对
        {"real": "Qone_nmr", "virtual": None, "missing_sim_policy": "fail"},  # real 未匹配
        {"real": "heaterstirrer.dalong", "virtual": "missing_sim"},  # virtual 未匹配
    ]
    plans, diagnostics = mod.plan_pairs(pairs, index, active=False)

    assert len(plans) == 2
    assert plans[0]["payload"]["real_resource_template_uuid"] == "u-h"
    assert plans[0]["payload"]["virtual_resource_template_uuid"] == "u-v"
    assert plans[1]["payload"]["real_resource_template_uuid"] == "u-c"

    reasons = " ".join(d["reason"] for d in diagnostics)
    assert "real class 未匹配模板: Qone_nmr" in reasons
    assert "virtual class 未匹配模板: missing_sim" in reasons


def test_load_pairs_reads_repo_yaml():
    pairs = mod.load_pairs(mod.DEFAULT_YAML)
    reals = {p["real"] for p in pairs}
    assert "heaterstirrer.dalong" in reals
    assert "Qone_nmr" in reals
