from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAgilent33521a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent33521A.py', 'class_name': 'Agilent33521A', 'import_roots': [], 'candidate_methods': ['beep', 'data_volatile_clear', 'phase_sync', 'data_arb', 'clear_display', 'trigger', 'wait_for_trigger', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/agilent/agilent33521A.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def beep(self, **kwargs):
        return self.call('beep', kwargs=kwargs)

    def data_volatile_clear(self, **kwargs):
        return self.call('data_volatile_clear', kwargs=kwargs)

    def phase_sync(self, **kwargs):
        return self.call('phase_sync', kwargs=kwargs)

    def data_arb(self, **kwargs):
        return self.call('data_arb', kwargs=kwargs)

    def clear_display(self, **kwargs):
        return self.call('clear_display', kwargs=kwargs)

    def trigger(self, **kwargs):
        return self.call('trigger', kwargs=kwargs)

    def wait_for_trigger(self, **kwargs):
        return self.call('wait_for_trigger', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

