from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLiconicStx88(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AD-SDL__liconic_module', 'source_file': 'src/liconic_interface/liconic_interface.py', 'class_name': 'LICONIC', 'import_roots': ['src'], 'candidate_methods': ['connect', 'disconnect', 'activate', 'deactivate', 'reset', 'soft_reset', 'read_actual_climate', 'write_set_climate', 'read_set_climate', 'activate_shaker', 'deactivate_shaker', 'read_set_shaker_speed', 'set_shaker_speed', 'load_plate', 'unload_plate', 'read_transfer_station_detector', 'beeper_off', 'get_system_status', 'read_error_code', 'is_busy'], 'action_targets': {}, 'metadata': {'repo': 'AD-SDL/liconic_module', 'repo_url': 'https://github.com/AD-SDL/liconic_module', 'brand': 'Liconic', 'model': 'STX88', 'device_type_cn': '自动化耗材堆栈', 'device_type_en': 'Automated Consumable Stack', 'source_framework': 'AD-SDL', 'tag_id': '4446', 'tag_name': '自动化耗材堆栈', 'tag_name_en': 'Automated Consumable Stack', 'candidate_score': 210, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def activate(self, **kwargs):
        return self.call('activate', kwargs=kwargs)

    def deactivate(self, **kwargs):
        return self.call('deactivate', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def soft_reset(self, **kwargs):
        return self.call('soft_reset', kwargs=kwargs)

    def read_actual_climate(self, **kwargs):
        return self.call('read_actual_climate', kwargs=kwargs)

    def write_set_climate(self, **kwargs):
        return self.call('write_set_climate', kwargs=kwargs)

    def read_set_climate(self, **kwargs):
        return self.call('read_set_climate', kwargs=kwargs)

    def activate_shaker(self, **kwargs):
        return self.call('activate_shaker', kwargs=kwargs)

    def deactivate_shaker(self, **kwargs):
        return self.call('deactivate_shaker', kwargs=kwargs)

    def read_set_shaker_speed(self, **kwargs):
        return self.call('read_set_shaker_speed', kwargs=kwargs)

    def set_shaker_speed(self, **kwargs):
        return self.call('set_shaker_speed', kwargs=kwargs)

    def load_plate(self, **kwargs):
        return self.call('load_plate', kwargs=kwargs)

    def unload_plate(self, **kwargs):
        return self.call('unload_plate', kwargs=kwargs)

    def read_transfer_station_detector(self, **kwargs):
        return self.call('read_transfer_station_detector', kwargs=kwargs)

    def beeper_off(self, **kwargs):
        return self.call('beeper_off', kwargs=kwargs)

    def get_system_status(self, **kwargs):
        return self.call('get_system_status', kwargs=kwargs)

    def read_error_code(self, **kwargs):
        return self.call('read_error_code', kwargs=kwargs)

    def is_busy(self, **kwargs):
        return self.call('is_busy', kwargs=kwargs)

