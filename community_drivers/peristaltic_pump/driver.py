"""
Masterflex L/S 蠕动泵 — 继承蠕动泵标准接口的真实品牌实现

把「蠕动泵标准动作」映射到 Masterflex L/S 串口私有命令（P-S/G/H/V/I/C 等），
使一套工作流可跨品牌控制整类蠕动泵。

与自动生成的 auto-* 注册表的区别：
  - 动作名是语义化的 initialize/set_speed/start/stop/...，不是 auto-setMotorSpeed/auto-go
  - status 用 @topic_config 广播设备真实状态（运行状态/转速/累计转数），不是加载器状态

上游源码: https://github.com/Wyss/masterflex  (masterflex/masterflex.py, 类 MasterflexSerial)
串口: 7 数据位 / 奇校验 / 4800 baud (8N1 ❌, 见 SERIAL_CONFIG)
"""

from typing import Any, Dict, Optional

from unilabos.registry.decorators import device, action, topic_config

from .peristaltic_pump import PeristalticPump


class _MockMasterflex:
    """无硬件时的内存模拟，覆盖本驱动用到的最小命令集，便于闭环演示与 CI。"""

    STX = "\x02"
    CR = "\x0d"
    ACK = "\x06"

    def __init__(self, pump_addr: int = 1, ser_port: str = "VIRTUAL", configs=None):
        self.pump_addr = pump_addr
        self.ser_port = ser_port
        self._rpm = 0.0
        self._revs = 0.0
        self._running = False
        self._cumulative = 0.0

    def enableRemote(self):
        return self.ACK

    def setMotorSpeed(self, rpm):
        self._rpm = float(rpm)
        return self.ACK

    def setRevolutions(self, revolutions):
        self._revs = float(revolutions)
        return self.ACK

    def go(self):
        self._running = abs(self._rpm) > 0.1
        if self._running:
            self._cumulative += self._revs
        return self.ACK

    def halt(self):
        self._running = False
        return self.ACK

    def requestMotorSpeed(self):
        return f"P{self.pump_addr:02d}S{self._rpm:+06.1f}{self.CR}"

    def requestStatus(self):
        return f"P{self.pump_addr:02d}I{'R' if self._running else 'H'}{self.CR}"

    def requestCumulative(self):
        return f"P{self.pump_addr:02d}C{self._cumulative}{self.CR}"


@device(
    id="peristaltic_pump_masterflex_ls",
    category=["蠕动泵"],
    description="Masterflex L/S 蠕动泵，继承蠕动泵标准接口（串口 7O1 / 4800 baud）。",
    display_name="Masterflex L/S 蠕动泵",
)
class MasterflexLSPump(PeristalticPump):
    """Masterflex L/S 品牌蠕动泵，把标准动作映射到 Masterflex 私有命令。"""

    def __init__(self, device_id: Optional[str] = None, config: Optional[Dict[str, Any]] = None, **kwargs):
        """
        初始化设备。

        Args:
            device_id[设备ID]: 设备实例 ID。
            config[设备配置]: 启动配置 (port/pump_addr 等)。
        """
        super().__init__(device_id or "peristaltic_pump_masterflex_ls", config, **kwargs)
        self._pump = None  # 上游 MasterflexSerial 对象，惰性创建
        # 方向缓存：+1 正转 / -1 反转，set_speed 只给大小，由 rotate_* 决定方向
        self.data.setdefault("direction", 1)

    def _ensure_pump(self):
        """惰性建立串口连接（避免无硬件时导入即失败）；无上游 SDK 时退化为内存模拟。"""
        if self._pump is None:
            try:
                from masterflex import MasterflexSerial  # 上游真实 SDK
            except ModuleNotFoundError:
                MasterflexSerial = _MockMasterflex  # 无 SDK / 无硬件 → 内存模拟
            self._pump = MasterflexSerial(
                self.config.get("pump_addr", 1),
                self.config.get("port", "/dev/ttyUSB0"),
            )
        return self._pump

    @action(description="初始化")
    def initialize(self) -> Dict[str, Any]:
        """打开串口并切到远程控制模式。"""
        pump = self._ensure_pump()
        pump.enableRemote()
        self.data["status"] = "idle"
        return {"success": True}

    @action(description="设置转动速度")
    def set_speed(self, speed: float = 0.0) -> Dict[str, Any]:
        """
        设置转速大小 (rpm, 0~100)。方向由正转/反转动作决定。

        Args:
            speed[转动速度]: 目标转速 rpm，取值 0~100。
        """
        pump = self._ensure_pump()
        rpm = max(0.0, min(100.0, abs(float(speed)))) * self.data.get("direction", 1)
        pump.setMotorSpeed(f"{rpm:+06.1f}")
        self.data["set_speed"] = abs(float(speed))
        return {"success": True}

    @action(description="设置转动圈数")
    def set_revolutions(self, revolutions: float = 0.0) -> Dict[str, Any]:
        """
        设置本次运行圈数 (<99999.99)。0 表示连续运行直到停止。

        Args:
            revolutions[转动圈数]: 目标圈数。
        """
        pump = self._ensure_pump()
        pump.setRevolutions(revolutions)
        self.data["set_revolutions"] = float(revolutions)
        return {"success": True}

    @action(description="正转")
    def rotate_forward(self) -> Dict[str, Any]:
        """正转 (CW) 并启动。"""
        self.data["direction"] = 1
        return self._start()

    @action(description="反转")
    def rotate_reverse(self) -> Dict[str, Any]:
        """反转 (CCW) 并启动。"""
        self.data["direction"] = -1
        return self._start()

    def _start(self) -> Dict[str, Any]:
        pump = self._ensure_pump()
        # 重新下发带方向的速度，再启动
        rpm = self.data.get("set_speed", 0.0) * self.data.get("direction", 1)
        pump.setMotorSpeed(f"{rpm:+06.1f}")
        pump.go()
        self.data["status"] = "running"
        return {"success": True}

    @action(description="停止")
    def stop(self) -> Dict[str, Any]:
        """停止泵。"""
        pump = self._ensure_pump()
        pump.halt()
        self.data["status"] = "idle"
        return {"success": True}

    @property
    @topic_config()
    def status(self) -> str:
        """设备运行状态 (idle/running)。"""
        if self._pump is None:
            return self.data.get("status", "idle")
        try:
            # 响应帧前缀 "P<2位地址><命令字母>"，载荷从第 4 个字符起
            resp = str(self._pump.requestStatus() or "")
            return "running" if "R" in resp[4:] else "idle"
        except Exception:
            return self.data.get("status", "idle")

    @property
    @topic_config()
    def motor_speed(self) -> float:
        """当前转速 rpm（含方向，正转为正）。"""
        if self._pump is None:
            return 0.0
        try:
            resp = str(self._pump.requestMotorSpeed())
            return float(resp[4:].rstrip("\r\n"))
        except Exception:
            return 0.0

    @property
    @topic_config()
    def cumulative_revolutions(self) -> float:
        """累计转数计数。"""
        if self._pump is None:
            return 0.0
        try:
            resp = str(self._pump.requestCumulative())
            return float(resp[4:].rstrip("\r\n"))
        except Exception:
            return 0.0
