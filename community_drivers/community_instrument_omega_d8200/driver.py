from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOmegaD8200(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/yaq-project__yaqd-omega', 'source_file': 'yaqd_omega/_omega_d8200.py', 'class_name': 'OmegaD8200', 'import_roots': [], 'candidate_methods': ['direct_serial_write'], 'action_targets': {}, 'metadata': {'repo': 'yaq-project/yaqd-omega', 'repo_url': 'https://github.com/yaq-project/yaqd-omega', 'brand': 'Omega', 'model': 'D8200', 'device_type_cn': '温度传感器', 'device_type_en': 'Temperature Sensor', 'source_framework': 'yaq', 'tag_id': '4438', 'tag_name': '箱式电阻炉', 'tag_name_en': 'Box Resistance Furnace', 'candidate_score': 124, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def direct_serial_write(self, **kwargs):
        return self.call('direct_serial_write', kwargs=kwargs)

