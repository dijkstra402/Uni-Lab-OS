#!/usr/bin/env python3
"""/** [AI] Model: Claude Opus 4.8 | 2026-06-20 | 仿真配对覆盖基线报告（Chunk 8 CI） */

仿真配对覆盖基线：遍历设备广场各包，汇总 real drivers / virtual drivers /
active pairs / coverage(K/N) / missing policy 分布，输出纯文本或 JSON。

复用后端公开接口（无需鉴权、无需 DB 凭据）：
  GET {base}/api/v1/lab/square/packages
  GET {base}/api/v1/lab/square/packages/{name}/simulation-coverage

ponytail：最小可用——仅依赖标准库 urllib/json，不引 requests；不接入流水线 YAML。
可在 CI 中以 `--fail-under` 作为覆盖率门禁（低于阈值返回非 0）。
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any, Dict, List

DEFAULT_BASE_URL = os.environ.get("UNILAB_BACKEND_URL", "http://127.0.0.1:48197")
API_PREFIX = "/api/v1/lab/square"


def _get_json(url: str, timeout: float) -> Any:
    """GET 并解析 JSON；非 200 或网络错误抛 RuntimeError。"""
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 受控内网地址
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"无法连接后端 {url}: {exc.reason}") from exc


def _unwrap(envelope: Any) -> Any:
    """剥离 {code,msg,data} 信封；非信封原样返回。"""
    if isinstance(envelope, dict) and "data" in envelope and "code" in envelope:
        return envelope["data"]
    return envelope


def list_package_names(base_url: str, timeout: float) -> List[str]:
    data = _unwrap(_get_json(f"{base_url}{API_PREFIX}/packages", timeout))
    # PackageListResp 为对象包装 {data:[...]}；公开列表禁裸数组，故再剥一层。
    items = data.get("data", data) if isinstance(data, dict) else data
    if not isinstance(items, list):
        return []
    return [str(it.get("name")) for it in items if isinstance(it, dict) and it.get("name")]


def package_coverage(base_url: str, name: str, timeout: float) -> Dict[str, Any]:
    url = f"{base_url}{API_PREFIX}/packages/{urllib.request.quote(name)}/simulation-coverage"
    result = _unwrap(_get_json(url, timeout))
    return result if isinstance(result, dict) else {}


def aggregate_baseline(coverages: List[Dict[str, Any]]) -> Dict[str, Any]:
    """纯聚合：把各包 coverage 汇总成全局基线指标。"""
    total_real = total_virtual = total_active = total_covered = 0
    policy_dist: Dict[str, int] = {}
    packages: List[Dict[str, Any]] = []
    for cov in coverages:
        real = int(cov.get("real_driver_count", 0))
        virtual = int(cov.get("virtual_driver_count", 0))
        active = int(cov.get("active_pair_count", 0))
        covered = int(cov.get("covered_real_driver_count", 0))
        total_real += real
        total_virtual += virtual
        total_active += active
        total_covered += covered
        for policy, count in (cov.get("policy_distribution") or {}).items():
            policy_dist[policy] = policy_dist.get(policy, 0) + int(count)
        packages.append(
            {
                "package_name": cov.get("package_name"),
                "real_driver_count": real,
                "virtual_driver_count": virtual,
                "active_pair_count": active,
                "covered_real_driver_count": covered,
                "coverage_ratio": round(covered / real, 4) if real else 0.0,
                "missing_real_classes": cov.get("missing_real_classes") or [],
            }
        )
    coverage_ratio = round(total_covered / total_real, 4) if total_real else 0.0
    return {
        "package_count": len(coverages),
        "real_driver_count": total_real,
        "virtual_driver_count": total_virtual,
        "active_pair_count": total_active,
        "covered_real_driver_count": total_covered,
        "coverage": f"{total_covered}/{total_real}",
        "coverage_ratio": coverage_ratio,
        "policy_distribution": policy_dist,
        "packages": packages,
    }


def format_text(baseline: Dict[str, Any]) -> str:
    lines = [
        "=== 仿真配对覆盖基线 ===",
        f"packages       : {baseline['package_count']}",
        f"real drivers   : {baseline['real_driver_count']}",
        f"virtual drivers: {baseline['virtual_driver_count']}",
        f"active pairs   : {baseline['active_pair_count']}",
        f"coverage       : {baseline['coverage']} ({baseline['coverage_ratio']:.2%})",
        f"missing policy : {baseline['policy_distribution']}",
        "--- per package ---",
    ]
    for pkg in sorted(baseline["packages"], key=lambda p: p["coverage_ratio"]):
        lines.append(
            f"{pkg['package_name']}: "
            f"real={pkg['real_driver_count']} virtual={pkg['virtual_driver_count']} "
            f"active={pkg['active_pair_count']} "
            f"coverage={pkg['covered_real_driver_count']}/{pkg['real_driver_count']} "
            f"({pkg['coverage_ratio']:.2%})"
        )
    return "\n".join(lines)


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="后端基础地址")
    parser.add_argument("--package", action="append", default=[], help="仅统计指定包名（可重复）")
    parser.add_argument("--json", action="store_true", help="输出 JSON 而非文本")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--fail-under", type=float, default=None, help="覆盖率低于该阈值返回非 0（CI 门禁）")
    args = parser.parse_args(argv)

    base_url = args.base_url.rstrip("/")
    try:
        names = args.package or list_package_names(base_url, args.timeout)
        coverages = [package_coverage(base_url, n, args.timeout) for n in names]
    except RuntimeError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    baseline = aggregate_baseline([c for c in coverages if c])
    print(json.dumps(baseline, ensure_ascii=False, indent=2) if args.json else format_text(baseline))

    if args.fail_under is not None and baseline["coverage_ratio"] < args.fail_under:
        print(
            f"[FAIL] coverage_ratio {baseline['coverage_ratio']:.2%} < fail-under {args.fail_under:.2%}",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
