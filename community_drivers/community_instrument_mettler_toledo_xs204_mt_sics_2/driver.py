from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMettlerToledoXs204MtSics2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/janelia-python__mettler_toledo_device_python', 'source_file': 'mettler_toledo_device/mettler_toledo_device.py', 'class_name': 'MettlerToledoDevice', 'import_roots': [], 'candidate_methods': ['close', 'get_port', 'get_commands', 'get_mtsics_level', 'get_balance_data', 'get_software_version', 'get_serial_number', 'get_software_id', 'get_weight_stable', 'get_weight', 'zero_stable', 'zero', 'reset'], 'action_targets': {}, 'metadata': {'repo': 'janelia-python/mettler_toledo_device_python', 'repo_url': 'https://github.com/janelia-python/mettler_toledo_device_python', 'brand': 'Mettler Toledo', 'model': 'XS204 (MT-SICS)', 'device_type_cn': '固体称量工作站', 'device_type_en': 'Solid Weighing Workstation', 'source_framework': 'janelia-python', 'tag_id': '4378', 'tag_name': '固体称量工作站', 'tag_name_en': 'Solid Weighing Workstation', 'candidate_score': 202, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def get_port(self, **kwargs):
        return self.call('get_port', kwargs=kwargs)

    def get_commands(self, **kwargs):
        return self.call('get_commands', kwargs=kwargs)

    def get_mtsics_level(self, **kwargs):
        return self.call('get_mtsics_level', kwargs=kwargs)

    def get_balance_data(self, **kwargs):
        return self.call('get_balance_data', kwargs=kwargs)

    def get_software_version(self, **kwargs):
        return self.call('get_software_version', kwargs=kwargs)

    def get_serial_number(self, **kwargs):
        return self.call('get_serial_number', kwargs=kwargs)

    def get_software_id(self, **kwargs):
        return self.call('get_software_id', kwargs=kwargs)

    def get_weight_stable(self, **kwargs):
        return self.call('get_weight_stable', kwargs=kwargs)

    def get_weight(self, **kwargs):
        return self.call('get_weight', kwargs=kwargs)

    def zero_stable(self, **kwargs):
        return self.call('zero_stable', kwargs=kwargs)

    def zero(self, **kwargs):
        return self.call('zero', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

