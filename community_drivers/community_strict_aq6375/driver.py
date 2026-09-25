from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAq6375(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/yokogawa/aq6370series.py', 'class_name': 'AQ6370Series', 'import_roots': [], 'candidate_methods': ['authenticate_ethernet', 'trigger', 'abort', 'initiate_sweep', 'wait_for_sweep_complete', 'set_level_position_to_max', 'copy_trace', 'delete_trace', 'get_xdata', 'get_ydata', 'execute_analysis', 'get_analysis', 'get_binary_data', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/yokogawa/aq6370series.py', 'confidence': 0.95, 'quality_score': 1.17, 'parse_status': 'class_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def authenticate_ethernet(self, **kwargs):
        return self.call('authenticate_ethernet', kwargs=kwargs)

    def trigger(self, **kwargs):
        return self.call('trigger', kwargs=kwargs)

    def abort(self, **kwargs):
        return self.call('abort', kwargs=kwargs)

    def initiate_sweep(self, **kwargs):
        return self.call('initiate_sweep', kwargs=kwargs)

    def wait_for_sweep_complete(self, **kwargs):
        return self.call('wait_for_sweep_complete', kwargs=kwargs)

    def set_level_position_to_max(self, **kwargs):
        return self.call('set_level_position_to_max', kwargs=kwargs)

    def copy_trace(self, **kwargs):
        return self.call('copy_trace', kwargs=kwargs)

    def delete_trace(self, **kwargs):
        return self.call('delete_trace', kwargs=kwargs)

    def get_xdata(self, **kwargs):
        return self.call('get_xdata', kwargs=kwargs)

    def get_ydata(self, **kwargs):
        return self.call('get_ydata', kwargs=kwargs)

    def execute_analysis(self, **kwargs):
        return self.call('execute_analysis', kwargs=kwargs)

    def get_analysis(self, **kwargs):
        return self.call('get_analysis', kwargs=kwargs)

    def get_binary_data(self, **kwargs):
        return self.call('get_binary_data', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

