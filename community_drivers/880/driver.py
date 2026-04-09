"""
自动生成的驱动存根
设备: SG380系列射频信号发生器
厂商: Stanford Research Systems
GitHub来源: https://github.com/pymeasure/pymeasure

"""
from typing import Dict, Any


class StanfordDriver:
    """驱动: SG380系列射频信号发生器"""
    def __init__(self, address: str = "", **kwargs):
        self.address = address
        self._connected = False

    def connect(self):
        self._connected = True

    def disconnect(self):
        self._connected = False

    def get_id(self) -> str:
        return "SG380系列射频信号发生器"

    def get_status(self) -> Dict[str, Any]:
        return {"connected": self._connected, "device": "SG380系列射频信号发生器"}
