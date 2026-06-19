"""
Masterflex L/S 蠕动泵驱动（自包含，无外部依赖）

真纳管：驱动代码内置完整串口协议，module 指向本文件，UniLab 包内即可加载，
不依赖任何包外 repo_root。无硬件时串口打开失败会软回退到内存模拟，保证导入/自检不崩。

协议来源: https://github.com/Wyss/masterflex (MasterflexSerial)
串口: 7 数据位 / 奇校验 / 4800 baud
"""

import glob
import sys
from typing import Optional

import serial


def list_serial_ports():
    """列出当前平台可用串口。"""
    if sys.platform.startswith("win"):
        candidates = ["COM%d" % (i + 1) for i in range(256)]
    elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
        candidates = glob.glob("/dev/tty[A-Za-z]*")
    elif sys.platform.startswith("darwin"):
        candidates = glob.glob("/dev/tty.*")
    else:
        raise EnvironmentError("Unsupported platform")
    result = []
    for port in candidates:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class _MockLink:
    """无硬件时的内存模拟串口链路，闭环维护转速/转数/运行状态。"""

    def __init__(self):
        self.rpm = 0.0
        self.revs = 0.0
        self.running = False
        self.cumulative = 0.0

    def exec_command(self, cmd_char, *params):
        if cmd_char == "S" and params:
            try:
                self.rpm = float(params[0])
            except ValueError:
                pass
            return ""
        if cmd_char == "V" and params:
            self.revs = float(params[0])
            return ""
        if cmd_char == "G":
            self.running = abs(self.rpm) > 0.1
            if self.running:
                self.cumulative += self.revs
            return "\x06"
        if cmd_char == "H":
            self.running = False
            return "\x06"
        if cmd_char == "I":
            return "R" if self.running else "H"
        if cmd_char == "S":
            return f"{self.rpm:+06.1f}"
        if cmd_char == "C":
            return str(self.cumulative)
        return ""


class MasterflexLSPump:
    """Masterflex L/S 蠕动泵。语义动作映射到 Masterflex 串口私有命令。"""

    SERIAL_CONFIG = {
        "bytesize": serial.SEVENBITS,
        "baudrate": 4800,
        "parity": serial.PARITY_ODD,
        "timeout": 1,
    }
    STX = "\x02"
    CR = "\x0d"

    def __init__(self, port: str, pump_addr: int = 1):
        """
        Args:
            port: 串口设备路径，如 /dev/ttyUSB0；无硬件时自动软回退到模拟。
            pump_addr: 泵地址 (satellite number)。
        """
        self.port = port
        self.pump_addr = int(pump_addr)
        self._status = "idle"
        self._direction = 1  # +1 正转 / -1 反转
        self._set_speed = 0.0
        try:
            self.ser = serial.Serial(port=port, **self.SERIAL_CONFIG)
            self._mock = None
        except (OSError, serial.SerialException):
            self.ser = None
            self._mock = _MockLink()

    # ---------------- 底层通讯 ----------------

    def _command(self, cmd_char, *params):
        if self._mock is not None:
            return self._mock.exec_command(cmd_char, *params)
        cmd = "P%02d" % self.pump_addr + cmd_char
        for p in params:
            cmd += "%s" % p
        frame = (self.STX + cmd + self.CR).encode("ascii")
        self.ser.write(frame)
        return self.ser.read_until(self.CR.encode()).decode(errors="ignore")

    # ---------------- 语义动作 ----------------

    def initialize(self):
        """切到远程控制模式并就绪。"""
        self._command("R")
        self._status = "idle"
        return {"success": True}

    def set_speed(self, speed: float = 0.0):
        """设置转速大小 rpm (0~100)；方向由正转/反转决定。"""
        self._set_speed = max(0.0, min(100.0, abs(float(speed))))
        self._command("S", f"{self._set_speed * self._direction:+06.1f}")
        return {"success": True}

    def set_revolutions(self, revolutions: float = 0.0):
        """设置本次运行圈数 (<99999.99)；0 表示连续运行。"""
        self._command("V", revolutions)
        return {"success": True}

    def rotate_forward(self):
        """正转 (CW) 并启动。"""
        self._direction = 1
        return self._start()

    def rotate_reverse(self):
        """反转 (CCW) 并启动。"""
        self._direction = -1
        return self._start()

    def _start(self):
        self._command("S", f"{self._set_speed * self._direction:+06.1f}")
        self._command("G")
        self._status = "running"
        return {"success": True}

    def stop(self):
        """停止泵。"""
        self._command("H")
        self._status = "idle"
        return {"success": True}

    # ---------------- 状态 ----------------

    @property
    def status(self) -> str:
        """运行状态 idle/running。"""
        try:
            resp = str(self._command("I"))
            return "running" if "R" in resp[-3:] else "idle"
        except Exception:
            return self._status

    @property
    def motor_speed(self) -> float:
        """当前转速 rpm（含方向）。"""
        try:
            resp = str(self._command("S"))
            return float(resp.strip().lstrip("S").rstrip("\r\n"))
        except Exception:
            return 0.0

    @property
    def cumulative_revolutions(self) -> float:
        """累计转数。"""
        try:
            resp = str(self._command("C"))
            return float(resp.strip().lstrip("C").rstrip("\r\n"))
        except Exception:
            return 0.0


if __name__ == "__main__":
    # 自包含自检（无硬件，走内存模拟）
    p = MasterflexLSPump(port="VIRTUAL", pump_addr=1)
    assert p.initialize()["success"]
    assert p.set_speed(50)["success"]
    assert p.set_revolutions(10)["success"]
    assert p.rotate_forward()["success"]
    assert p.status == "running", p.status
    assert abs(p.motor_speed - 50.0) < 0.01, p.motor_speed
    assert p.cumulative_revolutions == 10.0, p.cumulative_revolutions
    assert p.rotate_reverse()["success"]
    assert p.motor_speed < 0, p.motor_speed
    assert p.stop()["success"]
    assert p.status == "idle"
    print("MasterflexLSPump 自检: PASS")
