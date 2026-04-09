"""
自动生成的驱动存根
设备: Gilson Minipuls 3 蠕动泵
厂商: Gilson
GitHub来源: https://github.com/qiyaolin/Minipuls3

"""
from typing import Dict, Any


class GilsonDriver:
    """驱动: Gilson Minipuls 3 蠕动泵"""
    def __init__(self, address: str = "", **kwargs):
        self.address = address
        self._connected = False

    def connect(self):
        self._connected = True

    def disconnect(self):
        self._connected = False

    def get_id(self) -> str:
        return "Gilson Minipuls 3 蠕动泵"

    def get_status(self) -> Dict[str, Any]:
        return {"connected": self._connected, "device": "Gilson Minipuls 3 蠕动泵"}
