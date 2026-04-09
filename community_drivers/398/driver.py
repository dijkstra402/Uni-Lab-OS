"""
自动生成的驱动存根
设备: Princeton Instruments PIXIS背照式CCD相机
厂商: Princeton Instruments
GitHub来源: https://github.com/ScopeFoundry/HW_picam

"""
from typing import Dict, Any


class PrincetonDriver:
    """驱动: Princeton Instruments PIXIS背照式CCD相机"""
    def __init__(self, address: str = "", **kwargs):
        self.address = address
        self._connected = False

    def connect(self):
        self._connected = True

    def disconnect(self):
        self._connected = False

    def get_id(self) -> str:
        return "Princeton Instruments PIXIS背照式CCD相机"

    def get_status(self) -> Dict[str, Any]:
        return {"connected": self._connected, "device": "Princeton Instruments PIXIS背照式CCD相机"}
