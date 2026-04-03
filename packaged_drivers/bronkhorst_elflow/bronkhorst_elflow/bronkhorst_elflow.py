"""Bronkhorst EL-FLOW mass flow controller driver.

Communicates via RS232 serial interface using the Bronkhorst protocol.
Manual: https://www.bronkhorst.com/getmedia/77a1438f-e547-4a79-95ad-53e81fd38a97/917027-Manual-RS232-interface.pdf
"""

import logging
import struct
import time

import serial

logger = logging.getLogger(__name__)

CMDS = {
    "get_measure_flow": ":06800401210120",
    "get_capacity": ":068004014D014D",
    "get_control_mode": ":06800401040104",
    "set_control_mode": ":0580010104",
    "set_setpoint": ":0680010121",
    "get_setpoint": ":06800401210121",
    "get_valve": ":06800472417241",
}


class BronkhorstELFLOW:
    """Bronkhorst EL-FLOW mass flow controller.

    Config keys:
        port (str): Serial port, e.g. "/dev/ttyUSB0" or "COM3".
        baudrate (int): Baud rate, default 38400.
        node (str): Instrument node address, default "80".
    """

    def __init__(self, device_id=None, config=None, **kwargs):
        self.device_id = device_id or "bronkhorst_elflow"
        self.config = config or {}
        self._port = self.config.get("port")
        self._baudrate = int(self.config.get("baudrate", 38400))
        self._node = self.config.get("node", "80")
        self._serial = None
        self._pre_time = 0.0

    def _write(self, cmd):
        if not self._serial or not self._serial.is_open:
            raise RuntimeError("Serial port not connected")
        elapsed = time.time() - self._pre_time
        if elapsed < 1.0:
            time.sleep(1.0 - elapsed)
        self._serial.write((cmd + "\r\n").encode())
        self._pre_time = time.time()

    def _read(self):
        if not self._serial or not self._serial.is_open:
            raise RuntimeError("Serial port not connected")
        ret = self._serial.readline().decode(errors="replace")
        if len(ret) < 2 or ret[-2:] != "\r\n":
            logger.warning("read() termination error: %r", ret)
        return ret.strip()

    def connect(self):
        """连接串口并初始化设备"""
        if not self._port:
            return {"success": False, "error": "No serial port configured"}
        try:
            self._serial = serial.Serial(
                port=self._port,
                baudrate=self._baudrate,
                timeout=2,
            )
            return {"success": True, "port": self._port}
        except serial.SerialException as e:
            return {"success": False, "error": str(e)}

    def disconnect(self):
        """断开串口连接"""
        if self._serial and self._serial.is_open:
            self._serial.close()
        return {"success": True}

    def get_valve_output(self):
        """读取当前阀门输出百分比"""
        self._write(CMDS["get_valve"])
        ret = self._read()
        raw = int(ret[11:], 16)
        return raw * 61.7 / 10345949

    def set_setpoint(self, value):
        """设置流量设定值 (0-32000)"""
        if not isinstance(value, int):
            raise ValueError(f"value must be int, got {type(value)}")
        value = max(0, min(value, 32000))
        hex_val = hex(value)[2:].zfill(4)
        self._write(f"{CMDS['set_setpoint']}{hex_val}")
        return self._read()

    def get_setpoint(self):
        """读取当前流量设定值"""
        self._write(CMDS["get_setpoint"])
        ret = self._read()
        return int(ret[11:], 16)

    def set_mode(self, value):
        """设置控制模式 (0=RS232, 3=关阀, 4=冻结, 8=全开, 20=阀门转向)"""
        hex_val = hex(value)[2:].zfill(2)
        self._write(f"{CMDS['set_control_mode']}{hex_val}")
        return self._read()

    def get_mode(self):
        """读取当前控制模式"""
        self._write(CMDS["get_control_mode"])
        ret = self._read()
        return int(ret[11:], 16)

    def get_flow(self):
        """读取当前流量 (容量单位, l/min)"""
        self._write(CMDS["get_capacity"])
        ret = self._read()
        cap_100 = struct.unpack("!f", bytes.fromhex(ret[11:]))[0]

        self._write(CMDS["get_measure_flow"])
        ret1 = self._read()
        raw = int(ret1[11:], 16)
        return raw / 32000 * cap_100


__all__ = ["BronkhorstELFLOW"]
