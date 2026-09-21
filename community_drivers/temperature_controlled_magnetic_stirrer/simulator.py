"""控温磁力搅拌器的无硬件内存模拟驱动。"""

from __future__ import annotations

import math
import time as time_module
from collections.abc import Callable
from threading import RLock
from typing import Any, Dict, Optional

from unilabos.registry.decorators import action, device, topic_config


@device(
    id="temperature_controlled_magnetic_stirrer",
    category=["控温磁力搅拌器"],
    description="用于本地联调的控温磁力搅拌器内存模拟驱动，不连接真实硬件。",
    display_name="控温磁力搅拌器（内存模拟）",
)
class TemperatureControlledMagneticStirrerSimulator:
    """以单调时钟推进状态的确定性模拟器，不创建后台线程。"""

    def __init__(
        self,
        device_id: Optional[str] = None,
        config: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ):
        self.device_id = device_id or "temperature_controlled_magnetic_stirrer"
        self.config = dict(config or {})
        clock = kwargs.pop("_clock", None)
        self._clock: Callable[[], float] = (
            clock if callable(clock) else time_module.monotonic
        )
        self._state_lock = RLock()
        self._ambient_temperature = self._positive_config(
            "ambient_temperature", 25.0, allow_zero=True
        )
        self._temperature_rate = self._positive_config(
            "temperature_rate", 10.0
        )
        self._speed_rate = self._positive_config("speed_rate", 300.0)
        self._last_update_at = float(self._clock())
        self.data: Dict[str, Any] = {}
        self._reset_locked()

    def _positive_config(
        self, key: str, default: float, *, allow_zero: bool = False
    ) -> float:
        raw = self.config.get(key, default)
        try:
            value = float(raw)
        except (TypeError, ValueError):
            return default
        if not math.isfinite(value) or value < 0 or (value == 0 and not allow_zero):
            return default
        return value

    @staticmethod
    def _number(value: Any, label: str, *, non_negative: bool = False) -> float:
        if isinstance(value, bool):
            raise ValueError(f"{label}必须是有限数字")
        try:
            number = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{label}必须是有限数字") from exc
        if not math.isfinite(number):
            raise ValueError(f"{label}必须是有限数字")
        if non_negative and number < 0:
            raise ValueError(f"{label}不能小于 0")
        return number

    @staticmethod
    def _move_towards(current: float, target: float, step: float) -> float:
        if current < target:
            return min(current + step, target)
        if current > target:
            return max(current - step, target)
        return current

    def _reset_locked(self) -> None:
        self._last_update_at = float(self._clock())
        self.data = {
            "status": "idle",
            "fault": False,
            "idle": True,
            "fault_code": 0,
            "current_speed": 0.0,
            "current_temperature": self._ambient_temperature,
            "current_time": 0.0,
            "target_stir_speed": 0.0,
            "target_heating_temperature": self._ambient_temperature,
            "target_time": 0.0,
            "safety_temperature": 0.0,
            "temperature_unit": 0.0,
            "heating_mode": "",
            "work_mode": "",
        }

    def _advance_locked(self) -> None:
        now = float(self._clock())
        elapsed = max(0.0, now - self._last_update_at)
        self._last_update_at = now
        if elapsed == 0:
            return

        if self.data["status"] != "running" or self.data["fault"]:
            return

        target_time = float(self.data["target_time"])
        current_time = float(self.data["current_time"])
        active_elapsed = elapsed
        if target_time > 0:
            active_elapsed = min(elapsed, max(0.0, target_time - current_time))

        self.data["current_time"] = current_time + active_elapsed
        self.data["current_speed"] = self._move_towards(
            float(self.data["current_speed"]),
            float(self.data["target_stir_speed"]),
            self._speed_rate * active_elapsed,
        )
        self.data["current_temperature"] = self._move_towards(
            float(self.data["current_temperature"]),
            float(self.data["target_heating_temperature"]),
            self._temperature_rate * active_elapsed,
        )

        if target_time > 0 and self.data["current_time"] >= target_time:
            self.data["current_time"] = target_time
            self.data["current_speed"] = 0.0
            self.data["status"] = "idle"
            self.data["idle"] = True

    def _mark_ready_locked(self) -> None:
        if self.data["status"] == "idle":
            self.data["status"] = "ready"

    @action(description="初始化")
    def initialize(self) -> Dict[str, Any]:
        """恢复模拟设备的初始状态。"""
        with self._state_lock:
            self._reset_locked()
        return {}

    @action(description="设置搅拌速度")
    def set_stir_speed(self, stir_speed: float = 0.0) -> Dict[str, Any]:
        """设置目标搅拌速度。"""
        value = self._number(stir_speed, "搅拌速度", non_negative=True)
        with self._state_lock:
            self._advance_locked()
            self.data["target_stir_speed"] = value
            self._mark_ready_locked()
        return {}

    @action(description="设置加热温度")
    def set_heating_temperature(
        self, heating_temperature: float = 0.0
    ) -> Dict[str, Any]:
        """设置目标加热温度。"""
        value = self._number(heating_temperature, "加热温度")
        with self._state_lock:
            self._advance_locked()
            safety_temperature = float(self.data["safety_temperature"])
            if safety_temperature > 0 and value > safety_temperature:
                raise ValueError("加热温度不能高于安全温度")
            self.data["target_heating_temperature"] = value
            self._mark_ready_locked()
        return {}

    @action(description="设置时间")
    def set_time(self, time: float = 0.0) -> Dict[str, Any]:
        """设置目标运行时间；0 表示持续运行。"""
        value = self._number(time, "运行时间", non_negative=True)
        with self._state_lock:
            self._advance_locked()
            self.data["target_time"] = value
            self.data["current_time"] = 0.0
            self._mark_ready_locked()
        return {}

    @action(description="设置工作模式")
    def set_work_mode(self, work_mode: str = "") -> Dict[str, Any]:
        """保存模拟工作模式。"""
        with self._state_lock:
            self._advance_locked()
            self.data["work_mode"] = str(work_mode)
            self._mark_ready_locked()
        return {}

    @action(description="设置加热模式")
    def set_heating_mode(self, heating_mode: str = "") -> Dict[str, Any]:
        """保存模拟加热模式。"""
        with self._state_lock:
            self._advance_locked()
            self.data["heating_mode"] = str(heating_mode)
            self._mark_ready_locked()
        return {}

    @action(description="设置温度单位")
    def set_temperature_unit(
        self, temperature_unit: float = 0.0
    ) -> Dict[str, Any]:
        """保存设备定义的温度单位代码。"""
        value = self._number(temperature_unit, "温度单位代码")
        with self._state_lock:
            self._advance_locked()
            self.data["temperature_unit"] = value
            self._mark_ready_locked()
        return {}

    @action(description="设置安全温度")
    def set_safety_temperature(
        self, safety_temperature: float = 0.0
    ) -> Dict[str, Any]:
        """设置安全温度；0 表示不限制。"""
        value = self._number(safety_temperature, "安全温度", non_negative=True)
        with self._state_lock:
            self._advance_locked()
            target_temperature = float(self.data["target_heating_temperature"])
            if value > 0 and target_temperature > value:
                raise ValueError("安全温度不能低于当前目标加热温度")
            self.data["safety_temperature"] = value
            self._mark_ready_locked()
        return {}

    @action(description="搅拌")
    def stir(self) -> Dict[str, Any]:
        """开始按已设置的目标参数运行模拟设备。"""
        with self._state_lock:
            self._advance_locked()
            if self.data["fault"]:
                raise RuntimeError("设备处于故障状态，不能开始搅拌")
            self.data["status"] = "running"
            self.data["idle"] = False
            self.data["current_time"] = 0.0
            self._last_update_at = float(self._clock())
        return {}

    @property
    @topic_config(period=1.0)
    def status(self) -> str:
        with self._state_lock:
            self._advance_locked()
            return str(self.data["status"])

    @property
    @topic_config(period=1.0)
    def fault(self) -> bool:
        with self._state_lock:
            self._advance_locked()
            return bool(self.data["fault"])

    @property
    @topic_config(period=1.0)
    def idle(self) -> bool:
        with self._state_lock:
            self._advance_locked()
            return bool(self.data["idle"])

    @property
    @topic_config(period=1.0)
    def fault_code(self) -> int:
        with self._state_lock:
            self._advance_locked()
            return int(self.data["fault_code"])

    @property
    @topic_config(period=1.0)
    def current_speed(self) -> float:
        with self._state_lock:
            self._advance_locked()
            return float(self.data["current_speed"])

    @property
    @topic_config(period=1.0)
    def current_temperature(self) -> float:
        with self._state_lock:
            self._advance_locked()
            return float(self.data["current_temperature"])

    @property
    @topic_config(period=1.0)
    def current_time(self) -> float:
        with self._state_lock:
            self._advance_locked()
            return float(self.data["current_time"])

    @property
    @topic_config(period=1.0)
    def target_stir_speed(self) -> float:
        with self._state_lock:
            self._advance_locked()
            return float(self.data["target_stir_speed"])

    @property
    @topic_config(period=1.0)
    def target_heating_temperature(self) -> float:
        with self._state_lock:
            self._advance_locked()
            return float(self.data["target_heating_temperature"])

    @property
    @topic_config(period=1.0)
    def target_time(self) -> float:
        with self._state_lock:
            self._advance_locked()
            return float(self.data["target_time"])

    @property
    @topic_config(period=1.0)
    def safety_temperature(self) -> float:
        with self._state_lock:
            self._advance_locked()
            return float(self.data["safety_temperature"])

    @property
    @topic_config(period=1.0)
    def temperature_unit(self) -> float:
        with self._state_lock:
            self._advance_locked()
            return float(self.data["temperature_unit"])

    @property
    @topic_config(period=1.0)
    def heating_mode(self) -> str:
        with self._state_lock:
            self._advance_locked()
            return str(self.data["heating_mode"])

    @property
    @topic_config(period=1.0)
    def work_mode(self) -> str:
        with self._state_lock:
            self._advance_locked()
            return str(self.data["work_mode"])
