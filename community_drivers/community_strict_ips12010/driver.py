from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictIps12010(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/oxfordinstruments/ips120_10.py', 'class_name': 'IPS120_10', 'import_roots': [], 'candidate_methods': ['switch_heater_enabled', 'field', 'enable_control', 'disable_control', 'enable_persistent_mode', 'disable_persistent_mode', 'wait_for_idle', 'set_field', 'train_magnet', 'is_valid_response', 'next_error', 'write_binary_values', 'read_binary_values', 'check_errors'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/oxfordinstruments/ips120_10.py', 'confidence': 0.8, 'quality_score': 0.94, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def switch_heater_enabled(self, **kwargs):
        return self.call('switch_heater_enabled', kwargs=kwargs)

    def field(self, **kwargs):
        return self.call('field', kwargs=kwargs)

    def enable_control(self, **kwargs):
        return self.call('enable_control', kwargs=kwargs)

    def disable_control(self, **kwargs):
        return self.call('disable_control', kwargs=kwargs)

    def enable_persistent_mode(self, **kwargs):
        return self.call('enable_persistent_mode', kwargs=kwargs)

    def disable_persistent_mode(self, **kwargs):
        return self.call('disable_persistent_mode', kwargs=kwargs)

    def wait_for_idle(self, **kwargs):
        return self.call('wait_for_idle', kwargs=kwargs)

    def set_field(self, **kwargs):
        return self.call('set_field', kwargs=kwargs)

    def train_magnet(self, **kwargs):
        return self.call('train_magnet', kwargs=kwargs)

    def is_valid_response(self, **kwargs):
        return self.call('is_valid_response', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

