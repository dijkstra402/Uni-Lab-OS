from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentCincinnatiSubZeroEzt570i(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/johnstile__chamber_EZT570i', 'source_file': 'chamber_communication.py', 'class_name': 'ChamberCommunication', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'write_register', 'read_registers', 'read_response', 'print_profile', 'load_profile', 'write_profile_to_modbus', 'write_profile_lines', 'read_profile_lines', 'profile_to_modbus_packets', 'create_com_network', 'create_com_serial', 'create_com_dummy', 'disconnect_com_network', 'disconnect_com_serial', 'disconnect_com_dummy', 'write_com_serial', 'write_com_network', 'write_com_dummy', 'read_com_serial', 'read_com_network', 'read_com_dummy'], 'action_targets': {}, 'metadata': {'repo': 'johnstile/chamber_EZT570i', 'repo_url': 'https://github.com/johnstile/chamber_EZT570i', 'brand': 'Cincinnati Sub-Zero', 'model': 'EZT-570i', 'device_type_cn': '环境试验箱', 'device_type_en': 'Environmental Test Chamber', 'source_framework': '环境控制/传感器', 'tag_id': '4387', 'tag_name': '微生物培养箱', 'tag_name_en': 'Microbial Incubator', 'candidate_score': 234, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def write_register(self, **kwargs):
        return self.call('write_register', kwargs=kwargs)

    def read_registers(self, **kwargs):
        return self.call('read_registers', kwargs=kwargs)

    def read_response(self, **kwargs):
        return self.call('read_response', kwargs=kwargs)

    def print_profile(self, **kwargs):
        return self.call('print_profile', kwargs=kwargs)

    def load_profile(self, **kwargs):
        return self.call('load_profile', kwargs=kwargs)

    def write_profile_to_modbus(self, **kwargs):
        return self.call('write_profile_to_modbus', kwargs=kwargs)

    def write_profile_lines(self, **kwargs):
        return self.call('write_profile_lines', kwargs=kwargs)

    def read_profile_lines(self, **kwargs):
        return self.call('read_profile_lines', kwargs=kwargs)

    def profile_to_modbus_packets(self, **kwargs):
        return self.call('profile_to_modbus_packets', kwargs=kwargs)

    def create_com_network(self, **kwargs):
        return self.call('create_com_network', kwargs=kwargs)

    def create_com_serial(self, **kwargs):
        return self.call('create_com_serial', kwargs=kwargs)

    def create_com_dummy(self, **kwargs):
        return self.call('create_com_dummy', kwargs=kwargs)

    def disconnect_com_network(self, **kwargs):
        return self.call('disconnect_com_network', kwargs=kwargs)

    def disconnect_com_serial(self, **kwargs):
        return self.call('disconnect_com_serial', kwargs=kwargs)

    def disconnect_com_dummy(self, **kwargs):
        return self.call('disconnect_com_dummy', kwargs=kwargs)

    def write_com_serial(self, **kwargs):
        return self.call('write_com_serial', kwargs=kwargs)

    def write_com_network(self, **kwargs):
        return self.call('write_com_network', kwargs=kwargs)

    def write_com_dummy(self, **kwargs):
        return self.call('write_com_dummy', kwargs=kwargs)

    def read_com_serial(self, **kwargs):
        return self.call('read_com_serial', kwargs=kwargs)

    def read_com_network(self, **kwargs):
        return self.call('read_com_network', kwargs=kwargs)

    def read_com_dummy(self, **kwargs):
        return self.call('read_com_dummy', kwargs=kwargs)

