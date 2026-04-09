"""
自动生成的驱动存根
设备: M Squared SolsTiS超窄线宽可调谐Ti:Sapphire激光器
厂商: M2
GitHub来源: https://github.com/QCoDeS/Qcodes_contrib_drivers

"""
from typing import Dict, Any


class M2Driver:
    """驱动: M Squared SolsTiS超窄线宽可调谐Ti:Sapphire激光器"""
    def __init__(self, address: str = "", **kwargs):
        self.address = address
        self._connected = False

    def connect(self):
        self._connected = True

    def disconnect(self):
        self._connected = False

    def get_id(self) -> str:
        return "M Squared SolsTiS超窄线宽可调谐Ti:Sapphire激光器"

    def get_status(self) -> Dict[str, Any]:
        return {"connected": self._connected, "device": "M Squared SolsTiS超窄线宽可调谐Ti:Sapphire激光器"}
