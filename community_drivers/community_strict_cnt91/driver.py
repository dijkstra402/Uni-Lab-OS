from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictCnt91(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/pendulum/cnt91.py', 'class_name': 'CNT91', 'import_roots': [], 'candidate_methods': ['batch_size', 'measurement_time', 'read_buffer', 'configure_frequency_array_measurement', 'buffer_frequency_time_series', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/pendulum/cnt91.py', 'confidence': 0.75, 'quality_score': 0.89, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def batch_size(self, **kwargs):
        return self.call('batch_size', kwargs=kwargs)

    def measurement_time(self, **kwargs):
        return self.call('measurement_time', kwargs=kwargs)

    def read_buffer(self, **kwargs):
        return self.call('read_buffer', kwargs=kwargs)

    def configure_frequency_array_measurement(self, **kwargs):
        return self.call('configure_frequency_array_measurement', kwargs=kwargs)

    def buffer_frequency_time_series(self, **kwargs):
        return self.call('buffer_frequency_time_series', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

