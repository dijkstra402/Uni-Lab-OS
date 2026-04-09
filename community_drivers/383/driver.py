"""
自动生成的驱动存根
设备: QSI 600系列科学级CCD相机
厂商: QSI
GitHub来源: https://github.com/ScopeFoundry/HW_ascom_camera

"""
from typing import Dict, Any


class QSIDriver:
    """驱动: QSI 600系列科学级CCD相机"""
    def __init__(self, address: str = "", **kwargs):
        self.address = address
        self._connected = False

    def connect(self):
        self._connected = True

    def disconnect(self):
        self._connected = False

    def get_id(self) -> str:
        return "QSI 600系列科学级CCD相机"

    def get_status(self) -> Dict[str, Any]:
        return {"connected": self._connected, "device": "QSI 600系列科学级CCD相机"}
