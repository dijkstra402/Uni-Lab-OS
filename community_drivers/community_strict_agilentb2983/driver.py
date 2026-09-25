from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAgilentb2983(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilentB298x.py', 'class_name': 'AgilentB2981', 'import_roots': [], 'candidate_methods': ['abort', 'arm', 'init', 'abort_acquisition', 'arm_acquisition', 'init_acquisition', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/agilent/agilentB298x.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'class_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def abort(self, **kwargs):
        return self.call('abort', kwargs=kwargs)

    def arm(self, **kwargs):
        return self.call('arm', kwargs=kwargs)

    def init(self, **kwargs):
        return self.call('init', kwargs=kwargs)

    def abort_acquisition(self, **kwargs):
        return self.call('abort_acquisition', kwargs=kwargs)

    def arm_acquisition(self, **kwargs):
        return self.call('arm_acquisition', kwargs=kwargs)

    def init_acquisition(self, **kwargs):
        return self.call('init_acquisition', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

