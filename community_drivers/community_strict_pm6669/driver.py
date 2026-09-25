from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictPm6669(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/philips/PM6669.py', 'class_name': 'PM6669', 'import_roots': [], 'candidate_methods': ['spoll', 'trigger', 'read_measurement', 'read', 'reset_to_defaults', 'next_error', 'write_binary_values', 'read_binary_values', 'check_errors'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/philips/PM6669.py', 'confidence': 0.75, 'quality_score': 0.89, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def spoll(self, **kwargs):
        return self.call('spoll', kwargs=kwargs)

    def trigger(self, **kwargs):
        return self.call('trigger', kwargs=kwargs)

    def read_measurement(self, **kwargs):
        return self.call('read_measurement', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def reset_to_defaults(self, **kwargs):
        return self.call('reset_to_defaults', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

