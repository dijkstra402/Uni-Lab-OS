from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictTdkgen4038(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/tdk/tdk_gen40_38.py', 'class_name': 'TDK_Gen40_38', 'import_roots': [], 'candidate_methods': ['foldback_reset', 'save', 'recall', 'set_max_over_voltage', 'ramp_to_current', 'next_error', 'write_binary_values', 'read_binary_values', 'check_errors'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/tdk/tdk_gen40_38.py', 'confidence': 0.8, 'quality_score': 0.94, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def foldback_reset(self, **kwargs):
        return self.call('foldback_reset', kwargs=kwargs)

    def save(self, **kwargs):
        return self.call('save', kwargs=kwargs)

    def recall(self, **kwargs):
        return self.call('recall', kwargs=kwargs)

    def set_max_over_voltage(self, **kwargs):
        return self.call('set_max_over_voltage', kwargs=kwargs)

    def ramp_to_current(self, **kwargs):
        return self.call('ramp_to_current', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

