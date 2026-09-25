from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAmetek7270(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/ametek/ametek7270.py', 'class_name': 'Ametek7270', 'import_roots': [], 'candidate_methods': ['check_set_errors', 'ask', 'set_reference_mode', 'set_voltage_mode', 'set_differential_mode', 'set_current_mode', 'set_channel_A_mode', 'id', 'auto_gain', 'shutdown', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/ametek/ametek7270.py', 'confidence': 0.75, 'quality_score': 0.89, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def check_set_errors(self, **kwargs):
        return self.call('check_set_errors', kwargs=kwargs)

    def ask(self, **kwargs):
        return self.call('ask', kwargs=kwargs)

    def set_reference_mode(self, **kwargs):
        return self.call('set_reference_mode', kwargs=kwargs)

    def set_voltage_mode(self, **kwargs):
        return self.call('set_voltage_mode', kwargs=kwargs)

    def set_differential_mode(self, **kwargs):
        return self.call('set_differential_mode', kwargs=kwargs)

    def set_current_mode(self, **kwargs):
        return self.call('set_current_mode', kwargs=kwargs)

    def set_channel_A_mode(self, **kwargs):
        return self.call('set_channel_A_mode', kwargs=kwargs)

    def id(self, **kwargs):
        return self.call('id', kwargs=kwargs)

    def auto_gain(self, **kwargs):
        return self.call('auto_gain', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

