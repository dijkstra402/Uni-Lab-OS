from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAgilent8722es(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent8722ES.py', 'class_name': 'Agilent8722ES', 'import_roots': [], 'candidate_methods': ['set_fixed_frequency', 'parameter', 'scan_points', 'set_IF_bandwidth', 'set_averaging', 'disable_averaging', 'enable_averaging', 'is_averaging', 'restart_averaging', 'scan', 'scan_single', 'scan_continuous', 'frequencies', 'data_complex', 'data_log_magnitude', 'data_magnitude', 'data_phase', 'data', 'log_magnitude', 'magnitude', 'phase', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/agilent/agilent8722ES.py', 'confidence': 0.95, 'quality_score': 1.17, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def set_fixed_frequency(self, **kwargs):
        return self.call('set_fixed_frequency', kwargs=kwargs)

    def parameter(self, **kwargs):
        return self.call('parameter', kwargs=kwargs)

    def scan_points(self, **kwargs):
        return self.call('scan_points', kwargs=kwargs)

    def set_IF_bandwidth(self, **kwargs):
        return self.call('set_IF_bandwidth', kwargs=kwargs)

    def set_averaging(self, **kwargs):
        return self.call('set_averaging', kwargs=kwargs)

    def disable_averaging(self, **kwargs):
        return self.call('disable_averaging', kwargs=kwargs)

    def enable_averaging(self, **kwargs):
        return self.call('enable_averaging', kwargs=kwargs)

    def is_averaging(self, **kwargs):
        return self.call('is_averaging', kwargs=kwargs)

    def restart_averaging(self, **kwargs):
        return self.call('restart_averaging', kwargs=kwargs)

    def scan(self, **kwargs):
        return self.call('scan', kwargs=kwargs)

    def scan_single(self, **kwargs):
        return self.call('scan_single', kwargs=kwargs)

    def scan_continuous(self, **kwargs):
        return self.call('scan_continuous', kwargs=kwargs)

    def frequencies(self, **kwargs):
        return self.call('frequencies', kwargs=kwargs)

    def data_complex(self, **kwargs):
        return self.call('data_complex', kwargs=kwargs)

    def data_log_magnitude(self, **kwargs):
        return self.call('data_log_magnitude', kwargs=kwargs)

    def data_magnitude(self, **kwargs):
        return self.call('data_magnitude', kwargs=kwargs)

    def data_phase(self, **kwargs):
        return self.call('data_phase', kwargs=kwargs)

    def data(self, **kwargs):
        return self.call('data', kwargs=kwargs)

    def log_magnitude(self, **kwargs):
        return self.call('log_magnitude', kwargs=kwargs)

    def magnitude(self, **kwargs):
        return self.call('magnitude', kwargs=kwargs)

    def phase(self, **kwargs):
        return self.call('phase', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

