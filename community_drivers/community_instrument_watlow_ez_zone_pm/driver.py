from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentWatlowEzZonePm(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/numat__watlow', 'source_file': 'watlow/util.py', 'class_name': 'AsyncioModbusClient', 'import_roots': [], 'candidate_methods': ['read_coils', 'read_registers', 'read_holding_registers', 'write_coil', 'write_coils', 'write_register', 'write_registers'], 'action_targets': {}, 'metadata': {'repo': 'numat/watlow', 'repo_url': 'https://github.com/numat/watlow', 'brand': 'Watlow', 'model': 'EZ-Zone PM', 'device_type_cn': '箱式电阻炉', 'device_type_en': 'Box Resistance Furnace', 'source_framework': 'numat', 'tag_id': '4438', 'tag_name': '箱式电阻炉', 'tag_name_en': 'Box Resistance Furnace', 'candidate_score': 94, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def read_coils(self, **kwargs):
        return self.call('read_coils', kwargs=kwargs)

    def read_registers(self, **kwargs):
        return self.call('read_registers', kwargs=kwargs)

    def read_holding_registers(self, **kwargs):
        return self.call('read_holding_registers', kwargs=kwargs)

    def write_coil(self, **kwargs):
        return self.call('write_coil', kwargs=kwargs)

    def write_coils(self, **kwargs):
        return self.call('write_coils', kwargs=kwargs)

    def write_register(self, **kwargs):
        return self.call('write_register', kwargs=kwargs)

    def write_registers(self, **kwargs):
        return self.call('write_registers', kwargs=kwargs)

