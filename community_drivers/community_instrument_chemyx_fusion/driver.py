from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentChemyxFusion(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/yaq-project__yaqd-chemyx', 'source_file': 'yaqd_chemyx/_chemyx_fusion.py', 'class_name': 'ChemyxFusion', 'import_roots': [], 'candidate_methods': ['close', 'direct_serial_write', 'get_rate', 'prime', 'purge', 'set_rate', 'update_state'], 'action_targets': {}, 'metadata': {'repo': 'yaq-project/yaqd-chemyx', 'repo_url': 'https://github.com/yaq-project/yaqd-chemyx', 'brand': 'Chemyx', 'model': 'Fusion', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': 'yaq', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 172, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def direct_serial_write(self, **kwargs):
        return self.call('direct_serial_write', kwargs=kwargs)

    def get_rate(self, **kwargs):
        return self.call('get_rate', kwargs=kwargs)

    def prime(self, **kwargs):
        return self.call('prime', kwargs=kwargs)

    def purge(self, **kwargs):
        return self.call('purge', kwargs=kwargs)

    def set_rate(self, **kwargs):
        return self.call('set_rate', kwargs=kwargs)

    def update_state(self, **kwargs):
        return self.call('update_state', kwargs=kwargs)

