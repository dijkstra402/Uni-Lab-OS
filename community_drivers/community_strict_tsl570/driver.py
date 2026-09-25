from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictTsl570(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/santec/tsl570.py', 'class_name': 'TSL570', 'import_roots': [], 'candidate_methods': ['start_sweep', 'start_repeat', 'stop_sweep', 'sweep_pattern', 'sweep_routing', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/santec/tsl570.py', 'confidence': 0.75, 'quality_score': 0.89, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def start_sweep(self, **kwargs):
        return self.call('start_sweep', kwargs=kwargs)

    def start_repeat(self, **kwargs):
        return self.call('start_repeat', kwargs=kwargs)

    def stop_sweep(self, **kwargs):
        return self.call('stop_sweep', kwargs=kwargs)

    def sweep_pattern(self, **kwargs):
        return self.call('sweep_pattern', kwargs=kwargs)

    def sweep_routing(self, **kwargs):
        return self.call('sweep_routing', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

