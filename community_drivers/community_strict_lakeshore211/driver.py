from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictLakeshore211(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/lakeshore/lakeshore211.py', 'class_name': 'LakeShore211', 'import_roots': [], 'candidate_methods': ['get_relay_mode', 'configure_relay', 'get_alarm_status', 'configure_alarm', 'reset_alarm', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/lakeshore/lakeshore211.py', 'confidence': 0.8, 'quality_score': 0.94, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_relay_mode(self, **kwargs):
        return self.call('get_relay_mode', kwargs=kwargs)

    def configure_relay(self, **kwargs):
        return self.call('configure_relay', kwargs=kwargs)

    def get_alarm_status(self, **kwargs):
        return self.call('get_alarm_status', kwargs=kwargs)

    def configure_alarm(self, **kwargs):
        return self.call('configure_alarm', kwargs=kwargs)

    def reset_alarm(self, **kwargs):
        return self.call('reset_alarm', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

