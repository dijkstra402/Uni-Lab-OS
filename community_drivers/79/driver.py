"""
自动生成的驱动存根
设备: Universal Robots UR3e 协作机器人(e系列)
厂商: Universal Robots
GitHub来源: https://github.com/SintefManufacturing/python-urx

"""
from typing import Dict, Any


class UniversalDriver:
    """驱动: Universal Robots UR3e 协作机器人(e系列)"""
    def __init__(self, address: str = "", **kwargs):
        self.address = address
        self._connected = False

    def connect(self):
        self._connected = True

    def disconnect(self):
        self._connected = False

    def get_id(self) -> str:
        return "Universal Robots UR3e 协作机器人(e系列)"

    def get_status(self) -> Dict[str, Any]:
        return {"connected": self._connected, "device": "Universal Robots UR3e 协作机器人(e系列)"}
