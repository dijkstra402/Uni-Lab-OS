from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAzentaA4sRollHeatSealer(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AD-SDL__a4s_sealer_module', 'source_file': 'src/a4s_sealer_driver.py', 'class_name': 'A4S_SEALER_DRIVER', 'import_roots': ['src'], 'candidate_methods': ['connect_sealer', 'get_status', 'send_command', 'reset', 'open_gate', 'close_gate', 'set_temp', 'set_time', 'seal', 'config_robot'], 'action_targets': {}, 'metadata': {'repo': 'AD-SDL/a4s_sealer_module', 'repo_url': 'https://github.com/AD-SDL/a4s_sealer_module', 'brand': 'Azenta', 'model': 'A4S Roll Heat Sealer', 'device_type_cn': '封膜仪', 'device_type_en': 'Plate Sealer', 'source_framework': 'AD-SDL', 'tag_id': '4384', 'tag_name': '封膜仪', 'tag_name_en': 'Plate Sealer', 'candidate_score': 158, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect_sealer(self, **kwargs):
        return self.call('connect_sealer', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def open_gate(self, **kwargs):
        return self.call('open_gate', kwargs=kwargs)

    def close_gate(self, **kwargs):
        return self.call('close_gate', kwargs=kwargs)

    def set_temp(self, **kwargs):
        return self.call('set_temp', kwargs=kwargs)

    def set_time(self, **kwargs):
        return self.call('set_time', kwargs=kwargs)

    def seal(self, **kwargs):
        return self.call('seal', kwargs=kwargs)

    def config_robot(self, **kwargs):
        return self.call('config_robot', kwargs=kwargs)

