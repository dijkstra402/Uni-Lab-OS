from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAts525(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/temptronic/temptronic_ats525.py', 'class_name': 'ATS525', 'import_roots': [], 'candidate_methods': ['enter_cycle', 'enter_ramp', 'next_setpoint', 'configure', 'set_temperature', 'wait_for_settling', 'start', 'error_status', 'cycling_stopped', 'end_of_all_cycles', 'end_of_one_cycle', 'end_of_test', 'not_at_temperature', 'at_temperature', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/temptronic/temptronic_ats525.py', 'confidence': 0.95, 'quality_score': 1.17, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def enter_cycle(self, **kwargs):
        return self.call('enter_cycle', kwargs=kwargs)

    def enter_ramp(self, **kwargs):
        return self.call('enter_ramp', kwargs=kwargs)

    def next_setpoint(self, **kwargs):
        return self.call('next_setpoint', kwargs=kwargs)

    def configure(self, **kwargs):
        return self.call('configure', kwargs=kwargs)

    def set_temperature(self, **kwargs):
        return self.call('set_temperature', kwargs=kwargs)

    def wait_for_settling(self, **kwargs):
        return self.call('wait_for_settling', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def error_status(self, **kwargs):
        return self.call('error_status', kwargs=kwargs)

    def cycling_stopped(self, **kwargs):
        return self.call('cycling_stopped', kwargs=kwargs)

    def end_of_all_cycles(self, **kwargs):
        return self.call('end_of_all_cycles', kwargs=kwargs)

    def end_of_one_cycle(self, **kwargs):
        return self.call('end_of_one_cycle', kwargs=kwargs)

    def end_of_test(self, **kwargs):
        return self.call('end_of_test', kwargs=kwargs)

    def not_at_temperature(self, **kwargs):
        return self.call('not_at_temperature', kwargs=kwargs)

    def at_temperature(self, **kwargs):
        return self.call('at_temperature', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

