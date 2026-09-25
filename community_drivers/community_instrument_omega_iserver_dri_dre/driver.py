from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOmegaIserverDriDre(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/yaq-project__yaqd-omega', 'source_file': 'yaqd_omega/_omega_iseries_modbus.py', 'class_name': 'OmegaIseriesModbus', 'import_roots': [], 'candidate_methods': ['direct_serial_write', 'update_state'], 'action_targets': {}, 'metadata': {'repo': 'yaq-project/yaqd-omega', 'repo_url': 'https://github.com/yaq-project/yaqd-omega', 'brand': 'Omega', 'model': 'iServer DRi/DRE', 'device_type_cn': '温度控制器', 'device_type_en': 'Temperature Controller', 'source_framework': 'yaq', 'tag_id': '4369', 'tag_name': '冷热水机', 'tag_name_en': 'Chiller / Heater Unit', 'candidate_score': 82, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def direct_serial_write(self, **kwargs):
        return self.call('direct_serial_write', kwargs=kwargs)

    def update_state(self, **kwargs):
        return self.call('update_state', kwargs=kwargs)

