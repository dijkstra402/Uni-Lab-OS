from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictLakeshore425(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/lakeshore/lakeshore425.py', 'class_name': 'LakeShore425', 'import_roots': [], 'candidate_methods': ['auto_range', 'dc_mode', 'ac_mode', 'mode', 'zero_probe', 'measure', 'next_error', 'write_binary_values', 'read_binary_values', 'check_errors'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/lakeshore/lakeshore425.py', 'confidence': 0.75, 'quality_score': 0.89, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def auto_range(self, **kwargs):
        return self.call('auto_range', kwargs=kwargs)

    def dc_mode(self, **kwargs):
        return self.call('dc_mode', kwargs=kwargs)

    def ac_mode(self, **kwargs):
        return self.call('ac_mode', kwargs=kwargs)

    def mode(self, **kwargs):
        return self.call('mode', kwargs=kwargs)

    def zero_probe(self, **kwargs):
        return self.call('zero_probe', kwargs=kwargs)

    def measure(self, **kwargs):
        return self.call('measure', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

