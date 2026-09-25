from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictLd400p(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/aimtti/ld400p.py', 'class_name': 'LD400P', 'import_roots': [], 'candidate_methods': ['remove_unit_suffix', 'options', 'next_error', 'check_errors', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/aimtti/ld400p.py', 'confidence': 0.75, 'quality_score': 0.89, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def remove_unit_suffix(self, **kwargs):
        return self.call('remove_unit_suffix', kwargs=kwargs)

    def options(self, **kwargs):
        return self.call('options', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

