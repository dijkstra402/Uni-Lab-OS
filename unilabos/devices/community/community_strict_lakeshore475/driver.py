from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictLakeshore475(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/instrumentkit__InstrumentKit', 'source_file': 'src/instruments/lakeshore/lakeshore475.py', 'class_name': 'Lakeshore475', 'import_roots': ['src'], 'candidate_methods': ['field', 'field_units', 'temp_units', 'field_setpoint', 'field_control_params', 'p_value', 'i_value', 'ramp_rate', 'control_slope_limit', 'change_measurement_mode', 'name', 'scpi_version', 'op_complete', 'power_on_status', 'self_test_ok', 'trigger', 'wait_to_continue', 'line_frequency', 'check_error_queue', 'display_brightness', 'display_contrast', 'sendcmd', 'query', 'read_raw', 'timeout', 'address', 'terminator', 'prompt', 'binblockread', 'open_from_uri', 'open_tcpip', 'open_serial', 'open_gpibusb', 'open_gpibethernet', 'open_visa', 'open_test', 'open_usbtmc', 'open_vxi11', 'open_usb', 'open_file'], 'action_targets': {}, 'metadata': {'repo': 'instrumentkit/InstrumentKit', 'repo_url': 'https://github.com/instrumentkit/InstrumentKit', 'source_url': 'https://github.com/instrumentkit/InstrumentKit/blob/main/src/instruments/lakeshore/lakeshore475.py', 'confidence': 0.75, 'quality_score': 0.89, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def field(self, **kwargs):
        return self.call('field', kwargs=kwargs)

    def field_units(self, **kwargs):
        return self.call('field_units', kwargs=kwargs)

    def temp_units(self, **kwargs):
        return self.call('temp_units', kwargs=kwargs)

    def field_setpoint(self, **kwargs):
        return self.call('field_setpoint', kwargs=kwargs)

    def field_control_params(self, **kwargs):
        return self.call('field_control_params', kwargs=kwargs)

    def p_value(self, **kwargs):
        return self.call('p_value', kwargs=kwargs)

    def i_value(self, **kwargs):
        return self.call('i_value', kwargs=kwargs)

    def ramp_rate(self, **kwargs):
        return self.call('ramp_rate', kwargs=kwargs)

    def control_slope_limit(self, **kwargs):
        return self.call('control_slope_limit', kwargs=kwargs)

    def change_measurement_mode(self, **kwargs):
        return self.call('change_measurement_mode', kwargs=kwargs)

    def name(self, **kwargs):
        return self.call('name', kwargs=kwargs)

    def scpi_version(self, **kwargs):
        return self.call('scpi_version', kwargs=kwargs)

    def op_complete(self, **kwargs):
        return self.call('op_complete', kwargs=kwargs)

    def power_on_status(self, **kwargs):
        return self.call('power_on_status', kwargs=kwargs)

    def self_test_ok(self, **kwargs):
        return self.call('self_test_ok', kwargs=kwargs)

    def trigger(self, **kwargs):
        return self.call('trigger', kwargs=kwargs)

    def wait_to_continue(self, **kwargs):
        return self.call('wait_to_continue', kwargs=kwargs)

    def line_frequency(self, **kwargs):
        return self.call('line_frequency', kwargs=kwargs)

    def check_error_queue(self, **kwargs):
        return self.call('check_error_queue', kwargs=kwargs)

    def display_brightness(self, **kwargs):
        return self.call('display_brightness', kwargs=kwargs)

    def display_contrast(self, **kwargs):
        return self.call('display_contrast', kwargs=kwargs)

    def sendcmd(self, **kwargs):
        return self.call('sendcmd', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def read_raw(self, **kwargs):
        return self.call('read_raw', kwargs=kwargs)

    def timeout(self, **kwargs):
        return self.call('timeout', kwargs=kwargs)

    def address(self, **kwargs):
        return self.call('address', kwargs=kwargs)

    def terminator(self, **kwargs):
        return self.call('terminator', kwargs=kwargs)

    def prompt(self, **kwargs):
        return self.call('prompt', kwargs=kwargs)

    def binblockread(self, **kwargs):
        return self.call('binblockread', kwargs=kwargs)

    def open_from_uri(self, **kwargs):
        return self.call('open_from_uri', kwargs=kwargs)

    def open_tcpip(self, **kwargs):
        return self.call('open_tcpip', kwargs=kwargs)

    def open_serial(self, **kwargs):
        return self.call('open_serial', kwargs=kwargs)

    def open_gpibusb(self, **kwargs):
        return self.call('open_gpibusb', kwargs=kwargs)

    def open_gpibethernet(self, **kwargs):
        return self.call('open_gpibethernet', kwargs=kwargs)

    def open_visa(self, **kwargs):
        return self.call('open_visa', kwargs=kwargs)

    def open_test(self, **kwargs):
        return self.call('open_test', kwargs=kwargs)

    def open_usbtmc(self, **kwargs):
        return self.call('open_usbtmc', kwargs=kwargs)

    def open_vxi11(self, **kwargs):
        return self.call('open_vxi11', kwargs=kwargs)

    def open_usb(self, **kwargs):
        return self.call('open_usb', kwargs=kwargs)

    def open_file(self, **kwargs):
        return self.call('open_file', kwargs=kwargs)

