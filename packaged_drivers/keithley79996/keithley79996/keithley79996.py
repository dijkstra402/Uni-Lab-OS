from labtoolkit.Instrument import Instrument
from labtoolkit.SCPI import SCPI

class Keithley79996(Instrument, SCPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    pass
    # https://download.tek.com/manual/7999_6_901_01A.pdf

__all__ = ["Keithley79996"]
