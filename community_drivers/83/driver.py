"""
自动生成的驱动存根
设备: UR16e重载协作机械臂
厂商: Universal Robots
GitHub来源: https://github.com/UniversalRobots/RTDE_Python_Client_Library

"""
from typing import Dict, Any


class UniversalDriver:
    """驱动: UR16e重载协作机械臂"""
    def __init__(self, address: str = "", **kwargs):
        self.address = address
        self._connected = False

    def connect(self):
        self._connected = True

    def disconnect(self):
        self._connected = False

    def get_id(self) -> str:
        return "UR16e重载协作机械臂"

    def get_status(self) -> Dict[str, Any]:
        return {"connected": self._connected, "device": "UR16e重载协作机械臂"}
