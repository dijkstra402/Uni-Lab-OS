from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThorlabsPm100usb(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/instrumentkit__InstrumentKit', 'source_file': 'src/instruments/newport/newportesp301.py', 'class_name': 'NewportESP301', 'import_roots': ['src'], 'candidate_methods': ['axis', 'search_for_home', 'reset', 'define_program', 'execute_bulk_command', 'run_program', 'sendcmd', 'query', 'read_raw', 'timeout', 'address', 'terminator', 'prompt', 'binblockread', 'open_from_uri', 'open_tcpip', 'open_serial', 'open_gpibusb', 'open_gpibethernet', 'open_visa', 'open_test', 'open_usbtmc', 'open_vxi11', 'open_usb', 'open_file'], 'action_targets': {}, 'metadata': {'repo': 'instrumentkit/InstrumentKit', 'repo_url': 'https://github.com/instrumentkit/InstrumentKit', 'brand': 'Thorlabs', 'model': 'PM100USB', 'device_type_cn': '光功率计', 'device_type_en': 'Optical Power Meter', 'source_framework': 'InstrumentKit', 'tag_id': '4439', 'tag_name': '紫外-可见分光光谱仪', 'tag_name_en': 'UV-Vis Spectrophotometer', 'candidate_score': 391, 'parse_status': 'class_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def axis(self, **kwargs):
        return self.call('axis', kwargs=kwargs)

    def search_for_home(self, **kwargs):
        return self.call('search_for_home', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def define_program(self, **kwargs):
        return self.call('define_program', kwargs=kwargs)

    def execute_bulk_command(self, **kwargs):
        return self.call('execute_bulk_command', kwargs=kwargs)

    def run_program(self, **kwargs):
        return self.call('run_program', kwargs=kwargs)

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

