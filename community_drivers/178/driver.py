"""
自动生成的驱动存根
设备: Teledyne SSI Next Generation系列HPLC泵
厂商: Teledyne SSI
GitHub来源: https://github.com/biocatiit/beamline-control-user

"""
from typing import Dict, Any


class TeledyneDriver:
    """驱动: Teledyne SSI Next Generation系列HPLC泵"""
    def __init__(self, address: str = "", **kwargs):
        self.address = address
        self._connected = False

    def connect(self):
        self._connected = True

    def disconnect(self):
        self._connected = False

    def get_id(self) -> str:
        return "Teledyne SSI Next Generation系列HPLC泵"

    def get_status(self) -> Dict[str, Any]:
        return {"connected": self._connected, "device": "Teledyne SSI Next Generation系列HPLC泵"}
