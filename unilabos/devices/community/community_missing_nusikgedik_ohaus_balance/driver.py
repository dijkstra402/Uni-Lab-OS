import serial
import time


# Balance is a subclass of the Serial class which is defined in serial library
class Balance(serial.Serial):
    def __init__(self, port='COM4', baudrate=9600, bytesize=serial.EIGHTBITS,
                 parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, timeout = 1):
        """
        Initialize the Balance class. See __init__ of the parent class serial.Serial for
        more information.

        Args:
            port (str): Which port the balance is connected to
            baudrate (int): The serial connection baudrate to use
            bytesize (int): Communication byte size
            parity: Communication parity
            stopbits: Communication stop bits
            timeout (float): Communication timeout.
        """
        # Initialize the superclass Serial
        super(Balance, self).__init__(port = port, baudrate = baudrate, bytesize = bytesize,
                                      parity = parity, stopbits = stopbits, timeout = timeout)

    def write_utf8_with_nr(self, command):
        print(f"Sent: {commands[command]}")
        command += "\r\n" # in manual says use rn
        self.reset_input_buffer()
        self.write(command.encode("UTF-8"))

    def on(self):
        self.write_utf8_with_nr("ON")

    def off(self):
        self.write_utf8_with_nr("OFF")

    def set_unit(self, unit="g"):
        self.write_utf8_with_nr(unit + "U")

    def tare(self):
        self.write_utf8_with_nr("T")

    def zero(self):
        self.write_utf8_with_nr("Z")

    def read_weigh(self, command = "SP"):
        self.reset_input_buffer()
        try:
            self.write_utf8_with_nr(command)
            line = self.readline()  # attempts to read until \n or timeout
            if line:
                weight_str = line.strip()
            else:
                print("Partial data or timeout.")
                weight_str = None
            weight_value = float(weight_str.decode())
        except ValueError:
            print("Failed to convert to float, trying again...")
        return weight_value

    def open_door(self, door="left"):
        if door == "left":
            command = "WI 1 0"
        elif door == "right":
            command = "WI 0 1"
        elif door == "both":
            command = "WI 1 1"
        else:
            raise ValueError("Variable 'door' must be one of [left, right, both]")
        self.write_utf8_with_nr(command)
        time.sleep(2)

    def close_doors(self):
        self.write_utf8_with_nr("WI 0 0")
        time.sleep(2)

# Commands, for full description refer to the manual
commands = {
    "IP" : "Immediate Print of displayed weight (stable or unstable)",
    "P" : "Print displayed weight",
    "CP" : "Continuous Print. If LFT ON, CP could not work",
    "SP" : "Print on Stability",
    "SLP" : "Auto Print stable non-zero displayed weight.",
    "SLZP" : "Auto Print stable non-zero weight and stable zero reading.",
    "xP" : "Interval Print x = Print Interval (1-3600 sec)",
    "0P" : "Ends interval Print.",
    "H" : "Enter or get Print Header Lines.",
    "Z" : "Zero",
    "T" : "Tare",
    "xT" : "Establish a preset Tare value in displayed unit. X = preset tare value. Sending 0T clears tare (if allowed).",
    "PT" : "Prints Tare weight stored in memory.",
    "PM" : "Print current application mode (weighing mode).",
    "xM" : "Set current application mode to x.Use application list.",
    "M" : "Scroll to the next enabled mode.",
    "PU" : "Print Current weighing unit: g, Kg, lb, oz, etc….",
    "gU" : "Set balance to unit g.",
    "kgU" : "Set balance to unit kg.",
    "U" : "Scroll to the next enabled unit.",
    "ON" : "Brings out of Standby.",
    "OFF" : "Goes to Standby.",
    "C" : "Begin Span Calibration, same as trigger from calibration menu.",
    "IC" : "Begin internal Calibration, same as trigger from calibration menu.",
    "UC" : "User Calibration (uses default weight), same as trigger from calibration menu.",
    "AC" : "Abort Calibration.",
    "xUC" : "Set user defined weight and trigger one user calibration.",
    "WI 1 0" : "Left door open, right door closed.",
    "WI 0 1" : "Left door closed, right door open.",
    "WI 1 1" : "Both doors open.",
    "WI 0 0" : "Both doors closed.",
    "PSN" : "Print Serial Number.",
    "PV" : "Print terminal software version, base software version and LFT ON (if LFT is set ON).",
    "x#" : "Set Counting APW (x) in grams. (must have APW stored).",
    "P#" : "Print Counting application APW.",
    "x%" : "Set Percent application reference weight (x) in grams. (must have reference weight stored)",
    "P%" : "Print Percent application reference weight.",
    "xAW" : "Set Dynamic Weigh Level or Mode. (x = 1 - 99 seconds) or x = A (Automatic), S (Semi-Automatic), M (Manual).",
    "PAW" : "Print Dynamic Weigh Level.",
    "BAW" : "Start Dynamic Weigh cycle. (Manual Mode)",
    "CW" : "Clear locked weight (weight < threshold) in Dynamic Weigh (same as button “Reset”) & Display Hold (same as button “End Peak Hold”).",
    "xCO" : "Set Checkweighing Over Limit in grams x.",
    "xCU" : "Set Checkweighing Under Limit in grams x.",
    "PCO" : "Print Checkweighing Over Limit.",
    "PCU" : "Print Checkweighing Under Limit.",
    "xCM" : "Set Checkweigh mode (1=over/under, 2=Target/weight tolerance, 3=target/% tolerance",
    "xCT%" : "Set Checkweighing target in grams x for percent tolerance mode.",
    "PCT%" : "Print Checkweighing Target for percent tolerance mode.",
    "xCTW" : "Set Checkweighing target in grams x for weight tolerance mode.",
    "PCTW" : "Print Checkweighing Target for weight tolerance mode.",
    "xC%" : "Set Checkweighing % tolerance x. Attention: when x is a positive value, it is used to set the +tolerance value; vice versa.",
    "PC%" : "Print Checkweighing % tolerance.",
    "xCW" : "Set Checkweighing weight tolerance x.",
    "PCW" : "Print Checkweighing weight tolerance.",
    "xDH" : "Set Display Hold mode (Peak Hold). x = A (Automatic), S (Semi-Automatic), M (Manual).",
    "xD" : "Set 1 second print delay (set x = 0 for OFF, or x = 1 for ON).",
    "xFL" : "Set filter level to x (1 = low, 2 = med, 3 = high).",
    "xAL" : "Set Auto-zero to x (x = 1 for 0d, x = 2 for 0.5d, x = 3 for 1d, x = 4 for 3d).",
    "Esc R" : "Resets all Balance menus to factory defaults. Attention: The binary code of this commands is “1B 20 52 0D 0A” or “1B 52 0D 0A”.",
    "PID" : "Print current user Name.",
    "xID" : "Program user Name. Attention: only allowed numeric input.",
    "xTL" : "Set Totalize Mode. x = A (Automatic), M (Manual).",
    "PTIME" : "Print current time.",
    "PDATE" : "Print current date.",
    "xTIME" : "Set Time, x format: hh:mm:ss.",
    "xDATE"	: "Set Date, x format: mm/dd/yyyy.",
    "CA" : "Continuous weight, same as CP.",
    "SA" : "Stable load, same as SLP.",
    "xA" : "Interval Print x = interval in sec (1-3600) 0 = off, same as xP.",
    "0A" : "Set AutoPrint off, same as 0P.",
    "SC" : "Begin Span Cal, same as C.",
    "xAM" : "Set Animal Mode to Auto, Semi-Auto, Manual. Same as xAW(A/S/M)",
    "?" : "Prints current mode, same as PM.",
    "xS" : "0 = print unstable data, same as IP; 1 = print stable only1), same as SP.",
    "xRL" : "0 = disable response; 1 = enable response. This command only controls the “OK!” response."
}


if __name__ == "__main__":
    # Example
    with Balance() as ohaus:
        assert isinstance(ohaus, Balance)
        ohaus.close()
        ohaus.open()
        time.sleep(2)
        ohaus.on()
        #ohaus.set_unit(unit="g")
        ohaus.tare()
        time.sleep(2)
        ohaus.open_door("right")
        time.sleep(5)
        ohaus.close_doors()
        time.sleep(5)
        ohaus.read_weigh()
        ohaus.off()
        ohaus.close()
