from devices.keithley_devices import KeithleyDevice


class ke2410(KeithleyDevice):
    """
    Keithley 2410 source meter.

    Example:
    -------------
    dev = ke2410(address=24)
    dev.print_idn()
    dev.set_source('voltage')
    dev.set_voltage(10)
    dev.set_sense('current')
    dev.set_current_limit(0.00005)
    dev.set_output_on()
    print dev.read_current()
    print dev.read_voltage()
    print dev.read_resistance()
    dev.set_output_off()
    dev.reset()
    """

    def __init__(self, address: int = 24):
        super().__init__(address=address)

    def set_nplc(self, value: float):
        self.ctrl.write(":SENSE:CURR:NPLC %f" % value)
        #self.ctrl.write(":SENSE:VOLT:NPLC %f" % val)

    # Read attribute functions
    # ---------------------------------

    def read_voltage(self):
        # self.ctrl.write(":SENS:FUNC VOLT")
        self.ctrl.write(":FORM:ELEM:SENS VOLT")
        val = self.ctrl.query(":MEAS:VOLT?")
        return float(val)

    def read_current(self):
        # self.ctrl.write(":SENS:FUNC CURR")
        self.ctrl.write(":FORM:ELEM:SENS CURR")
        val = self.ctrl.query(":MEAS:CURR?")
        return float(val)

    def read_resistance(self):
        # self.ctrl.write(":SENS:FUNC RES")
        self.ctrl.write(":FORM:ELEM:SENS RES")
        val = self.ctrl.query(":MEAS:RES?")
        return float(val)
