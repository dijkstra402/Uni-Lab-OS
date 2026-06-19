#!/usr/bin/env python3

import logging
import re
import serial
import time

try:
    from odoo.addons.iot_drivers.driver import Driver
    from odoo.addons.iot_drivers.event_manager import event_manager
except ImportError:
    from tests import Driver, EventManager
    event_manager = EventManager()

logger = logging.getLogger(__name__)


class KernPCBScaleDriver(Driver):
    """
    Driver for KERN PCB series precision scales using KCP protocol
    Supports models like PCB 6000-0 via RS-232/USB serial
    """

    connection_type = "serial"

    def __init__(self, identifier, device):
        super().__init__(identifier, device)
        self.device_manufacturer = "KERN"
        self.device_type = "scale"
        self.device_connection = "serial"
        self.device_name = "KERN PCB Scale"
        self._is_reading = False

        # Serial port configuration for KERN PCB (from manual section 9.1)
        self._serial_config = {
            "baudrate": 9600,  # Configurable: 1200, 2400, 4800, 9600
            "bytesize": serial.EIGHTBITS,
            "parity": serial.PARITY_NONE,
            "stopbits": serial.STOPBITS_ONE,
            "timeout": 1.0,
        }

    @classmethod
    def supported(cls, device):
        """
        Check if device is a KERN scale
        Can be enhanced with actual device detection
        """
        protocol = device.get("protocol", "")
        return protocol == "kern_kcp" or "KERN" in device.get("name", "")

    def _connect(self):
        """Establish serial connection to scale"""
        try:
            self.dev = serial.Serial(port=self.device_identifier, **self._serial_config)
            logger.info(f"Connected to KERN scale on {self.device_identifier}")
            return True

        except Exception as e:
            logger.error(f"Failed to connect to KERN scale: {e}")
            return False

    def _send_command(self, command):
        """
        Send KCP command to scale
        Commands must end with CR LF as per manual section 1.4
        """
        if not self.dev or not self.dev.is_open:
            return None

        try:
            cmd = f"{command}\r\n".encode("ascii")
            self.dev.write(cmd)
            time.sleep(0.1)  # Brief delay for scale to process

            # Read response
            response = self.dev.readline().decode("ascii").strip()
            return response

        except Exception as e:
            logger.error(f"Error sending command {command}: {e}")
            return None

    WEIGHT_RE = re.compile(
        r"""
            ^                         # start of string
            (                         # group 1: Optional prefix
                (                     # group 2: Status with whitespace
                    (?P<status>[DS])  # named group: D or S
                    \s                # whitespace after status
                )?                    # status is optional
                .*                    # any characters
                \s+                   # one or more whitespace
            )?                        # entire prefix is optional
            (?P<value>-?[0-9.]+)      # named group: number (optional minus, digits/dots)
            \s+                       # one or more whitespace
            (?P<unit>[a-z]+)          # named group: unit (lowercase letters)
            $                         # end of string
        """,
        re.VERBOSE,
    )

    def _parse_weight(self, response):
        """
        Parse weight response from scale
        Example: "S S    123.4 g"
        """
        try:
            # Remove extra spaces and extract values
            match = self.WEIGHT_RE.search(response.strip())
            if match:
                result = match.groupdict()
                result["status"] = "stable" if result["status"] == "S" else "unstable"
                result["value"] = float(result["value"])
                return result

        except Exception as e:
            logger.warning(f"Failed to parse weight: {response}, error: {e}")
            return None

    def get_weight(self):
        """
        Get current weight from scale
        Uses KCP command 'S' for stable weight or 'SI' for immediate weight
        """
        # 'S' = stable weight, 'SI' = immediate weight (manual section 1.4)
        response = self._send_command("S")

        if response:
            weight_data = self._parse_weight(response)
            if weight_data:
                event_manager.device_changed(self)
                return weight_data

        return {"value": 0, "unit": "g", "status": "error"}

    def tare(self):
        """
        Tare the scale (zero with container)
        Uses KCP command 'T'
        """
        response = self._send_command("T")
        logger.info(f"Tare command sent, response: {response}")
        return response is not None

    def zero(self):
        """
        Zero the scale
        Uses KCP command 'Z'
        """
        response = self._send_command("Z")
        logger.info(f"Zero command sent, response: {response}")
        return response is not None

    def action(self, data):
        """
        Handle actions from Odoo (called by IoT box)
        """
        if data.get("action") == "read_weight":
            return self.get_weight()

        elif data.get("action") == "tare":
            return self.tare()

        elif data.get("action") == "zero":
            return self.zero()

        return {"error": "Unknown action"}

    def disconnect(self):
        """Close serial connection"""
        if self.dev and self.dev.is_open:
            self.dev.close()
            logger.info("Disconnected from KERN scale")
