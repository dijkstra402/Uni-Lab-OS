# Quality Drivers — A 桶 (真实可用)

> 来自 `selected_quality_drivers_REVIEW.md` 评级 A 的 10 台驱动: 代码自包含或仅依赖标准库, 无 import-fail / 名义错绑 / 不是设备控制 等问题.

## 目录结构

```
quality_drivers_A/
  <id>/
    driver.py            # 主驱动
    <伴生模块>.py        # 如 53/de5000.py (主驱动)
    registry.yaml        # 含 quality_review 字段
    __init__.py          # 直接 import 用
  quality_drivers_A.csv  # 一览, 列对齐 all_instruments_merged.csv 并追加驱动元信息
  README.md
```

## 10 台一览

| id | 名称 | 厂商 | 主类 | 行数 | Action 数 | 通信 | 来源仓库 |
|---|---|---|---|---|---|---|---|
| 53 | DER EE DE-5000 手持式LCR表 | DER EE | `` | 4 | 6 | - | (自研/未标注) |
| 63 | Lauda LOOP L250 帕尔贴循环恒温器 | Lauda | `未识别` | 339 | 13 | Serial | gh:turbocasino/LOOP-L250-Chiller |
| 65 | Masterflex L/S 蠕动泵系统 | Masterflex | `MasterflexSerial` | 267 | 10 | Serial | gh:Wyss/masterflex |
| 75 | IKA RV 10 旋转蒸发仪 | IKA | `RV10Rotovap` | 308 | 10 | Serial | gh:croningp/pylabware |
| 76 | Universal Robots UR3 协作机器人 | Universal Robots | `SecondaryMonitor` | 477 | 10 | Socket/TCP | gh:SintefManufacturing/python-urx |
| 77 | Universal Robots UR5 协作机器人 | Universal Robots | `SecondaryMonitor` | 477 | 10 | Socket/TCP | gh:SintefManufacturing/python-urx |
| 78 | Universal Robots UR10 协作机器人 | Universal Robots | `SecondaryMonitor` | 477 | 10 | Socket/TCP | gh:SintefManufacturing/python-urx |
| 80 | Universal Robots UR5e 协作机器人 | Universal Robots | `SecondaryMonitor` | 477 | 10 | Socket/TCP | gh:SintefManufacturing/python-urx |
| 220 | Red Pitaya STEMlab 125-14 多功能测量平台 | RedPitaya | `scpi` | 136 | 10 | Socket/TCP | (自研/未标注) |
| 1011 | Universal Robots UR10e协作机器人 | Universal Robots | `SecondaryMonitor` | 477 | 10 | Socket/TCP | gh:SintefManufacturing/python-urx |

## 使用注意 (顶层副作用)

- **63**: driver.py 是脚本风格: 模块顶层直接打开 config.json 并 open() 串口, import 时会触发副作用. 实际使用前需要把顶层代码包成类或在导入前 mock. 命令实现 (write_cmd / temperature / power / status 等) 本身正确.

## 直接 import 用法

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path("quality_drivers_A").resolve()))
# 比如取 65 (Masterflex L/S):
from importlib import import_module
m = import_module("65.driver")
pump = m.MasterflexSerial(pump_addr=1, ser_port='/dev/tty.usbserial')
pump.go()
```

注意: UR3/5/10/5e/10e (76/77/78/80/1011) 共享同一份 `SecondaryMonitor`, 实际只是不同型号的标识, 代码完全相同, 见 registry 里的 `duplicate_of`.
