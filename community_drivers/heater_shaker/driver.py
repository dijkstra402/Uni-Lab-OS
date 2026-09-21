"""
加热振荡器 — 生物设备「统一指令集」第一个样板 (Unified Instruction Set, sample #1)

要点（对应会议「以现有成果为样板，为生物仪器制定统一指令集」「整体类为入口、注册表指明
不同机型对应不同 backend」）：

  - 对外只暴露一套**语义统一指令**：initialize / set_temperature / start_shaking /
    stop_shaking / deactivate_temperature / stop —— 不直接把 PyLabRobot backend 的函数抛出去。
  - 一个类统管整类设备：内部按注册表 config 选择不同品牌 backend（BioShake / Inheco
    Thermoshake / Hamilton HS …），它们共享 PyLabRobot 的 HeaterShakerBackend 接口
    （set_temperature/get_current_temperature/deactivate + start_shaking/stop_shaking + setup/stop）。
  - 自带仿真：无硬件 / config.simulate=True 时退化为内存仿真，指令集完全一致，可虚实切换
    （对应会议「仿真驱动与真机驱动对应、指令一致」的雏形）。

真机 backend 为异步（async），这里用一个常驻事件循环把统一指令同步化转发到 backend。
"""

from __future__ import annotations

import asyncio
import importlib
import sys
from typing import Any, Dict, Optional

from unilabos.registry.decorators import device, action, topic_config


class _MockHeaterShaker:
    """无硬件时的内存仿真，实现与 PyLabRobot HeaterShakerBackend 相同的异步接口。

    ponytail: 仿真不建温度动力学模型，get_current_temperature 直接回读目标温度；
    若以后要接仿真引擎做温升曲线，在此类替换即可，统一指令层无需改动。"""

    def __init__(self, **_kwargs):
        self._target_temp = 0.0
        self._speed = 0.0
        self._shaking = False
        self._on = False

    async def setup(self):
        self._on = True

    async def stop(self):
        self._shaking = False
        self._on = False

    async def set_temperature(self, temperature: float):
        self._target_temp = float(temperature)

    async def get_current_temperature(self) -> float:
        return self._target_temp

    async def deactivate(self):
        self._target_temp = 0.0

    async def start_shaking(self, speed: float):
        self._speed = float(speed)
        self._shaking = True

    async def stop_shaking(self):
        self._shaking = False


@device(
    id="heater_shaker",
    category=["加热振荡器"],
    description="加热振荡器标准接口：温控 + 振荡的统一语义指令，跨品牌/型号共用，按注册表选 backend。",
    display_name="加热振荡器",
)
class HeaterShaker:
    """加热振荡器统一设备类。

    config 关键字段：
      backend_module / backend_class : 选定品牌 backend（不同机型在注册表里指不同值）
      backend_init                   : 传给 backend 构造函数的参数（如 {"port": "/dev/ttyUSB0"}）
      repo_root                      : 可选；PyLabRobot 源码根（未 pip 安装时加入 sys.path）
      simulate                       : True 时强制走内存仿真（虚实切换）
    """

    def __init__(self, device_id: Optional[str] = None, config: Optional[Dict[str, Any]] = None, **kwargs):
        """
        初始化设备。

        Args:
            device_id[设备ID]: 设备实例 ID。
            config[设备配置]: 启动配置（backend 选择 / 连接参数 / 是否仿真）。
        """
        self.device_id = device_id or "heater_shaker"
        self.config = config or {}
        self.data: Dict[str, Any] = {
            "status": "idle", "target_temperature": 0.0, "shaking_speed": 0.0,
        }
        self._backend: Any = None
        self._loop: Optional[asyncio.AbstractEventLoop] = None

    # ---- 内部：事件循环 + 惰性 backend ----
    def _run(self, coro):
        if self._loop is None:
            self._loop = asyncio.new_event_loop()
        return self._loop.run_until_complete(coro)

    def _load_backend_class(self):
        mod_path = self.config["backend_module"]
        cls_name = self.config["backend_class"]
        try:
            mod = importlib.import_module(mod_path)
        except ModuleNotFoundError:
            repo_root = self.config.get("repo_root")
            if repo_root and repo_root not in sys.path:
                sys.path.insert(0, repo_root)
            mod = importlib.import_module(mod_path)
        return getattr(mod, cls_name)

    def _ensure_backend(self):
        if self._backend is not None:
            return self._backend
        if self.config.get("simulate") or not self.config.get("backend_class"):
            self._backend = _MockHeaterShaker()
        else:
            try:
                cls = self._load_backend_class()
                self._backend = cls(**dict(self.config.get("backend_init", {})))
            except Exception:  # noqa: BLE001 - 无硬件/无依赖/接口对象缺失 → 退化为仿真
                self._backend = _MockHeaterShaker()
        return self._backend

    # ---- 统一指令集（语义动作，非 backend 原函数）----
    @action(description="初始化")
    def initialize(self) -> Dict[str, Any]:
        """连接并初始化设备。真机连不上（无硬件/被占用）则回退内存仿真，实现虚实切换。"""
        backend = self._ensure_backend()
        try:
            self._run(backend.setup())
        except Exception:  # noqa: BLE001 - 连接失败 → 切到仿真，保证指令集仍可跑
            if not isinstance(backend, _MockHeaterShaker):
                self._backend = _MockHeaterShaker()
                self._run(self._backend.setup())
            else:
                raise
        self.data["status"] = "idle"
        return {"success": True}

    @action(description="设置目标温度")
    def set_temperature(self, temperature: float = 0.0) -> Dict[str, Any]:
        """
        设置目标温度并开始控温。

        Args:
            temperature[目标温度]: 目标温度，单位 ℃。
        """
        self._run(self._ensure_backend().set_temperature(float(temperature)))
        self.data["target_temperature"] = float(temperature)
        return {"success": True}

    @action(description="停止控温")
    def deactivate_temperature(self) -> Dict[str, Any]:
        """关闭主动控温。"""
        self._run(self._ensure_backend().deactivate())
        self.data["target_temperature"] = 0.0
        return {"success": True}

    @action(description="开始振荡")
    def start_shaking(self, speed: float = 0.0) -> Dict[str, Any]:
        """
        以指定转速开始振荡。

        Args:
            speed[振荡转速]: 目标转速，单位 rpm。
        """
        self._run(self._ensure_backend().start_shaking(float(speed)))
        self.data["shaking_speed"] = float(speed)
        self.data["status"] = "running"
        return {"success": True}

    @action(description="停止振荡")
    def stop_shaking(self) -> Dict[str, Any]:
        """停止振荡。"""
        self._run(self._ensure_backend().stop_shaking())
        self.data["shaking_speed"] = 0.0
        self.data["status"] = "idle"
        return {"success": True}

    @action(description="停止")
    def stop(self) -> Dict[str, Any]:
        """停止设备（停振荡 + 断开）。"""
        self._run(self._ensure_backend().stop())
        self.data["shaking_speed"] = 0.0
        self.data["status"] = "idle"
        return {"success": True}

    # ---- 状态属性 ----
    @property
    @topic_config()
    def status(self) -> str:
        """运行状态 (idle/running)。"""
        return self.data.get("status", "idle")

    @property
    @topic_config()
    def current_temperature(self) -> float:
        """当前温度 ℃（读自 backend）。"""
        try:
            return float(self._run(self._ensure_backend().get_current_temperature()))
        except Exception:  # noqa: BLE001
            return self.data.get("target_temperature", 0.0)

    @property
    @topic_config()
    def target_temperature(self) -> float:
        """目标温度 ℃。"""
        return self.data.get("target_temperature", 0.0)

    @property
    @topic_config()
    def shaking_speed(self) -> float:
        """当前振荡转速 rpm。"""
        return self.data.get("shaking_speed", 0.0)


if __name__ == "__main__":
    # 自检：无硬件 → 内存仿真，跑一遍统一指令集，断言状态正确。
    hs = HeaterShaker(config={"simulate": True})
    assert hs.initialize()["success"]
    assert hs.set_temperature(37.0)["success"]
    assert hs.start_shaking(500.0)["success"]
    assert hs.status == "running"
    assert hs.target_temperature == 37.0
    assert hs.shaking_speed == 500.0
    assert hs.current_temperature == 37.0
    assert hs.stop_shaking()["success"]
    assert hs.status == "idle" and hs.shaking_speed == 0.0
    assert hs.deactivate_temperature()["success"] and hs.target_temperature == 0.0
    assert hs.stop()["success"]
    print("HeaterShaker 统一指令集自检通过 (simulate)")
