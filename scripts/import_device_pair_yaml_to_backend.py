#!/usr/bin/env python3
"""
============================================================
AI-GENERATED CODE METADATA
============================================================
Model: Claude Opus 4.8
Generation Date: 2026-06-20 14:45:00
Prompt Summary: 一次性迁移脚本：把 device_pair.yaml 导入后端 simulation_driver_pair
Context: 设计文档 08 §12.1；后端 create API 已就绪，本脚本只读 YAML + 调 API，不改后端
Human Review Status: [ ] Pending [ ] Reviewed [ ] Approved
============================================================

把仓库内 `unilabos/registry/device_pair.yaml` 一次性导入设备广场后端的
`simulation_driver_pair`：

1. 读 YAML pairs。
2. 通过 real/virtual class 反查 `resource_node_template` 的模板 UUID。
3. 调后端 admin API `POST /lab/square/admin/simulation-pairs` 建配对。
4. 未匹配项输出 diagnostics；保留原 YAML，不删除。

class → 模板 UUID 解析说明（重要，已调研后端 handler）：
  后端 deviceClass(tpl) 规则：社区包（package_info.class_namespace 非空）为
  "<class_namespace>.<name>"，否则即模板 name。
  现有列表接口都拿不到「原始 name + class_namespace + uuid」三件套：
    - GET /lab/square/list   ：无 class_namespace，且 name 叠加 ui_overlay.display_name；
    - GET /square/agent-devices：display name 且无 class_namespace（不可用）。
  因此本脚本采用替代方案（不连后端时无法实现，故离线测试用 --templates-file）：
    用 list 仅枚举 uuid，再对每个 uuid 调 GET /lab/square/detail/:uuid，从
    package_info.class_namespace + effective_template.device.id（契约字段，overlay
    不可改）还原原始 class，按 deviceClass 规则建 class → uuid 映射。

安全：默认 dry-run，仅打印计划与 diagnostics；--apply 才真正 POST。

用法示例：
  # 离线 dry-run（喂入假模板列表，验证解析/映射，不连后端）
  python scripts/import_device_pair_yaml_to_backend.py --templates-file /tmp/tpls.json
  # 连本机后端 dry-run
  python scripts/import_device_pair_yaml_to_backend.py --remote-addr http://127.0.0.1:48198/api/v1 --auth <base64>
  # 真正写入，并让配对立即在公开页可见（is_default=true → active）
  python scripts/import_device_pair_yaml_to_backend.py --remote-addr ... --auth ... --apply --active
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

# 默认 YAML 路径：脚本位于 <repo>/scripts/，registry 在 <repo>/unilabos/registry/
DEFAULT_YAML = Path(__file__).resolve().parent.parent / "unilabos" / "registry" / "device_pair.yaml"
MIGRATION_NOTES = "migrated from device_pair.yaml"


# ──────────────────── 纯函数：可单测、不连后端 ────────────────────


def load_pairs(yaml_path: str | Path) -> list[dict[str, Any]]:
    """读取 device_pair.yaml，返回 pairs 列表（缺失则空列表）。"""
    raw = yaml.safe_load(Path(yaml_path).read_text(encoding="utf-8")) or {}
    return list(raw.get("pairs", []) or [])


def device_class(name: str | None, class_namespace: str | None) -> str:
    """复刻后端 deviceClass：社区包为 ns.name，否则即 name。"""
    name = (name or "").strip()
    namespace = (class_namespace or "").strip()
    return f"{namespace}.{name}" if namespace else name


def extract_record(template_uuid: str, detail: dict[str, Any]) -> dict[str, Any]:
    """从 detail 响应还原 {uuid, name(原始 class id), class_namespace}。

    name 优先取 effective_template.device.id（契约字段，overlay 不可改），
    回退顶层 name；class_namespace 取 package_info.class_namespace。
    """
    pkg = detail.get("package_info")
    class_namespace = pkg.get("class_namespace", "") if isinstance(pkg, dict) else ""

    name = ""
    effective = detail.get("effective_template")
    if isinstance(effective, dict):
        device = effective.get("device")
        if isinstance(device, dict):
            name = device.get("id") or device.get("name") or ""
    if not name:
        name = detail.get("name", "")
    return {"uuid": template_uuid, "name": name, "class_namespace": class_namespace}


def build_class_index(templates: list[dict[str, Any]]) -> tuple[dict[str, str], list[str]]:
    """据 deviceClass 规则建 class → uuid 映射；同名多模板记 warning 并取首个。"""
    index: dict[str, str] = {}
    warnings: list[str] = []
    for tpl in templates:
        cls = device_class(tpl.get("name"), tpl.get("class_namespace"))
        template_uuid = tpl.get("uuid")
        if not cls or not template_uuid:
            continue
        if cls in index and index[cls] != template_uuid:
            warnings.append(f"class '{cls}' 命中多个模板，取首个 {index[cls]}，忽略 {template_uuid}")
            continue
        index.setdefault(cls, template_uuid)
    return index, warnings


def build_create_payload(
    pair: dict[str, Any],
    real_uuid: str,
    virtual_uuid: str | None,
    active: bool,
) -> dict[str, Any]:
    """把单条 YAML pair 映射为后端 create 请求体（snake_case）。

    映射规则（设计文档 §12.1 + 任务约定）：
      - virtual=null → pair_type=stub，不传 virtual uuid；
      - virtual 非空 → pair_type=mock（保守）；
      - missing_sim_policy：YAML 值或默认 stub；
      - supported_modes：["sim"]，twin_observed 非空再加 "twin"；
      - twin_config：twin_observed/twin_throttle_hz 任一存在则带 {observed, throttle_hz}；
      - priority=0，notes 固定迁移标记。
    """
    is_stub = pair.get("virtual") is None
    twin_observed = pair.get("twin_observed") or []
    twin_throttle = pair.get("twin_throttle_hz")
    supported_modes = ["sim"] + (["twin"] if twin_observed else [])

    payload: dict[str, Any] = {
        "real_resource_template_uuid": real_uuid,
        "pair_type": "stub" if is_stub else "mock",
        "supported_modes": supported_modes,
        "missing_sim_policy": pair.get("missing_sim_policy") or "stub",
        "priority": 0,
        "is_default": bool(active),
        "compatibility": None,
        "runtime_config": None,
        "notes": MIGRATION_NOTES,
    }
    if not is_stub:
        payload["virtual_resource_template_uuid"] = virtual_uuid

    twin_config: dict[str, Any] = {}
    if twin_observed:
        twin_config["observed"] = twin_observed
    if twin_throttle is not None:
        twin_config["throttle_hz"] = twin_throttle
    if twin_config:
        payload["twin_config"] = twin_config
    return payload


def plan_pairs(
    pairs: list[dict[str, Any]],
    class_index: dict[str, str],
    active: bool,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """逐条解析 class→uuid 并生成 create 计划；未匹配项进 diagnostics。"""
    plans: list[dict[str, Any]] = []
    diagnostics: list[dict[str, Any]] = []
    for pair in pairs:
        real = pair.get("real")
        virtual = pair.get("virtual")
        real_uuid = class_index.get(real)
        if not real_uuid:
            diagnostics.append({"real": real, "virtual": virtual, "reason": f"real class 未匹配模板: {real}"})
            continue
        virtual_uuid = None
        if virtual is not None:
            virtual_uuid = class_index.get(virtual)
            if not virtual_uuid:
                diagnostics.append(
                    {"real": real, "virtual": virtual, "reason": f"virtual class 未匹配模板: {virtual}"}
                )
                continue
        plans.append(
            {
                "real": real,
                "virtual": virtual,
                "payload": build_create_payload(pair, real_uuid, virtual_uuid, active),
            }
        )
    return plans, diagnostics


# ──────────────────── 网络侧：连后端（不进单测） ────────────────────


def fetch_template_records(client: Any) -> list[dict[str, Any]]:
    """list 枚举 uuid + 逐个 detail 还原原始 class，组装模板记录。"""
    records: list[dict[str, Any]] = []
    for item in client.list_square_devices():
        template_uuid = item.get("uuid")
        if not template_uuid:
            continue
        detail = client.get_square_device_detail(template_uuid)
        records.append(extract_record(template_uuid, detail))
    return records


def _build_client(remote_addr: str | None, auth: str | None, config_path: str | None) -> Any:
    """复用 HTTPClient（remote_addr/auth 沿用其既有配置；不硬编码 token）。"""
    from unilabos.config.config import load_config

    if config_path:
        load_config(config_path)
    from unilabos.app.web.client import HTTPClient

    return HTTPClient(remote_addr=remote_addr or None, auth=auth or None)


def _print_plan(plans: list[dict[str, Any]], diagnostics: list[dict[str, Any]], warnings: list[str]) -> None:
    print(f"== 计划创建配对 {len(plans)} 条 ==")
    for plan in plans:
        payload = plan["payload"]
        print(
            f"  + real={plan['real']} virtual={plan['virtual']} "
            f"type={payload['pair_type']} modes={payload['supported_modes']} "
            f"policy={payload['missing_sim_policy']} is_default={payload['is_default']}"
        )
    if warnings:
        print(f"\n== class→uuid 映射 warning {len(warnings)} 条 ==")
        for w in warnings:
            print(f"  ! {w}")
    if diagnostics:
        print(f"\n== 未匹配 diagnostics {len(diagnostics)} 条 ==")
        for d in diagnostics:
            print(f"  - {d['reason']}")


def _apply(client: Any, plans: list[dict[str, Any]]) -> tuple[int, int, list[str]]:
    """逐条 POST；code==0 计成功，其余/异常计跳过并记录，不中断。"""
    success = 0
    skipped = 0
    notes: list[str] = []
    for plan in plans:
        label = f"real={plan['real']} virtual={plan['virtual']}"
        try:
            res = client.create_simulation_pair(plan["payload"])
        except Exception as exc:  # noqa: BLE001 一次性脚本：单条失败不应中断整体迁移
            skipped += 1
            notes.append(f"{label} 请求异常: {exc}")
            continue
        if res.get("code", 0) == 0:
            success += 1
            print(f"  OK {label} -> {res.get('data', {}).get('uuid', '')}")
        else:
            skipped += 1
            notes.append(f"{label} 后端拒绝: code={res.get('code')} msg={res.get('message')}")
    return success, skipped, notes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="导入 device_pair.yaml 到后端 simulation_driver_pair")
    parser.add_argument("--yaml", type=Path, default=DEFAULT_YAML, help="device_pair.yaml 路径")
    parser.add_argument("--remote-addr", default=None, help="后端地址（含 /api/v1）；缺省走 HTTPConfig")
    parser.add_argument("--auth", default=None, help="Authorization: Lab <auth> 的 auth；缺省走 ak/sk")
    parser.add_argument("--config", default=None, help="unilabos 配置文件路径（可选）")
    parser.add_argument(
        "--templates-file",
        type=Path,
        default=None,
        help="离线模板列表 JSON（[{uuid,name,class_namespace}]），提供则不连后端解析 class→uuid",
    )
    parser.add_argument("--apply", action="store_true", help="真正调用 create API（默认 dry-run）")
    parser.add_argument("--active", action="store_true", help="以 is_default=true(→active) 创建，立即公开可见")
    args = parser.parse_args(argv)

    pairs = load_pairs(args.yaml)
    print(f"== 读取 YAML pairs {len(pairs)} 条：{args.yaml} ==")

    client = None
    if args.templates_file is not None:
        records = json.loads(Path(args.templates_file).read_text(encoding="utf-8"))
        print(f"== 离线模板列表 {len(records)} 条：{args.templates_file} ==")
    else:
        client = _build_client(args.remote_addr, args.auth, args.config)
        records = fetch_template_records(client)
        print(f"== 后端模板 {len(records)} 条 ==")

    class_index, warnings = build_class_index(records)
    plans, diagnostics = plan_pairs(pairs, class_index, args.active)
    _print_plan(plans, diagnostics, warnings)

    if not args.apply:
        print("\n== dry-run：未发送任何 POST，加 --apply 才真正写入 ==")
        return 0

    if client is None:
        client = _build_client(args.remote_addr, args.auth, args.config)

    print("\n== 开始写入后端 ==")
    success, skipped, notes = _apply(client, plans)
    print("\n== 迁移汇总 ==")
    print(f"  成功 {success} | 跳过/冲突 {skipped} | 未匹配 {len(diagnostics)}")
    for note in notes:
        print(f"  ~ {note}")
    for d in diagnostics:
        print(f"  - 未匹配: {d['reason']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
