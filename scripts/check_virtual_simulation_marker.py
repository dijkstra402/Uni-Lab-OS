#!/usr/bin/env python3
"""校验 virtual_device.yaml 中各 virtual 驱动条目带有仿真标记。

设备广场仿真配对依赖后端 isVirtualDriver(t) 读取
device_params._simulation.driver_runtime_kind == "virtual"。
本脚本确保核心 virtual 驱动模板都带上该标记，避免前端「仿真设备反查」块缺失。
"""

from pathlib import Path

import yaml

EXPECTED_DRIVERS = [
    "virtual_centrifuge",
    "virtual_column",
    "virtual_filter",
    "virtual_gas_source",
    "virtual_heatchill",
    "virtual_multiway_valve",
    "virtual_rotavap",
    "virtual_sample_demo",
    "virtual_separator",
    "virtual_solenoid_valve",
    "virtual_solid_dispenser",
    "virtual_stirrer",
    "virtual_transfer_pump",
    "virtual_vacuum_pump",
]

YAML_PATH = (
    Path(__file__).resolve().parent.parent
    / "unilabos"
    / "registry"
    / "devices"
    / "virtual_device.yaml"
)


def main() -> None:
    with YAML_PATH.open("r", encoding="utf-8") as fh:
        registry = yaml.safe_load(fh)

    for driver in EXPECTED_DRIVERS:
        assert driver in registry, f"缺少条目: {driver}"
        simulation = (
            registry[driver].get("device_params", {}).get("_simulation", {})
        )
        kind = simulation.get("driver_runtime_kind")
        assert kind == "virtual", (
            f"{driver} 的 driver_runtime_kind 应为 'virtual'，实际为 {kind!r}"
        )

    print(f"virtual_device.yaml 仿真标记校验通过：{len(EXPECTED_DRIVERS)}/14")


if __name__ == "__main__":
    main()
