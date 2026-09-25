from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKdScientificLegato100(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/yaq-project__yaqd-kds', 'source_file': 'yaqd_kds/_kds_legato100.py', 'class_name': 'KdsLegato100', 'import_roots': [], 'candidate_methods': ['run', 'direct_serial_write', 'purge', 'prime', 'stop', 'get_rate', 'set_infuse_rate', 'get_force', 'set_force', 'get_diameter', 'set_diameter', 'set_brightness', 'update_state'], 'action_targets': {}, 'metadata': {'repo': 'yaq-project/yaqd-kds', 'repo_url': 'https://github.com/yaq-project/yaqd-kds', 'brand': 'KD Scientific', 'model': 'Legato 100', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': 'yaq', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 210, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

    def direct_serial_write(self, **kwargs):
        return self.call('direct_serial_write', kwargs=kwargs)

    def purge(self, **kwargs):
        return self.call('purge', kwargs=kwargs)

    def prime(self, **kwargs):
        return self.call('prime', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def get_rate(self, **kwargs):
        return self.call('get_rate', kwargs=kwargs)

    def set_infuse_rate(self, **kwargs):
        return self.call('set_infuse_rate', kwargs=kwargs)

    def get_force(self, **kwargs):
        return self.call('get_force', kwargs=kwargs)

    def set_force(self, **kwargs):
        return self.call('set_force', kwargs=kwargs)

    def get_diameter(self, **kwargs):
        return self.call('get_diameter', kwargs=kwargs)

    def set_diameter(self, **kwargs):
        return self.call('set_diameter', kwargs=kwargs)

    def set_brightness(self, **kwargs):
        return self.call('set_brightness', kwargs=kwargs)

    def update_state(self, **kwargs):
        return self.call('update_state', kwargs=kwargs)

