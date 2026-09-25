from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictDanfysik8500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/danfysik/danfysik8500.py', 'class_name': 'Danfysik8500', 'import_roots': [], 'candidate_methods': ['read', 'local', 'remote', 'polarity', 'reset_interlocks', 'enable', 'disable', 'is_enabled', 'status_hex', 'current', 'current_ppm', 'current_setpoint', 'slew_rate', 'wait_for_current', 'is_current_stable', 'is_ready', 'wait_for_ready', 'status', 'clear_ramp_set', 'set_ramp_delay', 'start_ramp', 'add_ramp_step', 'stop_ramp', 'set_ramp_to_current', 'ramp_to_current', 'set_sequence', 'clear_sequence', 'sync_sequence', 'start_sequence', 'stop_sequence', 'is_sequence_running', 'next_error', 'write_binary_values', 'read_binary_values', 'check_errors'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/danfysik/danfysik8500.py', 'confidence': 0.75, 'quality_score': 0.89, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def local(self, **kwargs):
        return self.call('local', kwargs=kwargs)

    def remote(self, **kwargs):
        return self.call('remote', kwargs=kwargs)

    def polarity(self, **kwargs):
        return self.call('polarity', kwargs=kwargs)

    def reset_interlocks(self, **kwargs):
        return self.call('reset_interlocks', kwargs=kwargs)

    def enable(self, **kwargs):
        return self.call('enable', kwargs=kwargs)

    def disable(self, **kwargs):
        return self.call('disable', kwargs=kwargs)

    def is_enabled(self, **kwargs):
        return self.call('is_enabled', kwargs=kwargs)

    def status_hex(self, **kwargs):
        return self.call('status_hex', kwargs=kwargs)

    def current(self, **kwargs):
        return self.call('current', kwargs=kwargs)

    def current_ppm(self, **kwargs):
        return self.call('current_ppm', kwargs=kwargs)

    def current_setpoint(self, **kwargs):
        return self.call('current_setpoint', kwargs=kwargs)

    def slew_rate(self, **kwargs):
        return self.call('slew_rate', kwargs=kwargs)

    def wait_for_current(self, **kwargs):
        return self.call('wait_for_current', kwargs=kwargs)

    def is_current_stable(self, **kwargs):
        return self.call('is_current_stable', kwargs=kwargs)

    def is_ready(self, **kwargs):
        return self.call('is_ready', kwargs=kwargs)

    def wait_for_ready(self, **kwargs):
        return self.call('wait_for_ready', kwargs=kwargs)

    def status(self, **kwargs):
        return self.call('status', kwargs=kwargs)

    def clear_ramp_set(self, **kwargs):
        return self.call('clear_ramp_set', kwargs=kwargs)

    def set_ramp_delay(self, **kwargs):
        return self.call('set_ramp_delay', kwargs=kwargs)

    def start_ramp(self, **kwargs):
        return self.call('start_ramp', kwargs=kwargs)

    def add_ramp_step(self, **kwargs):
        return self.call('add_ramp_step', kwargs=kwargs)

    def stop_ramp(self, **kwargs):
        return self.call('stop_ramp', kwargs=kwargs)

    def set_ramp_to_current(self, **kwargs):
        return self.call('set_ramp_to_current', kwargs=kwargs)

    def ramp_to_current(self, **kwargs):
        return self.call('ramp_to_current', kwargs=kwargs)

    def set_sequence(self, **kwargs):
        return self.call('set_sequence', kwargs=kwargs)

    def clear_sequence(self, **kwargs):
        return self.call('clear_sequence', kwargs=kwargs)

    def sync_sequence(self, **kwargs):
        return self.call('sync_sequence', kwargs=kwargs)

    def start_sequence(self, **kwargs):
        return self.call('start_sequence', kwargs=kwargs)

    def stop_sequence(self, **kwargs):
        return self.call('stop_sequence', kwargs=kwargs)

    def is_sequence_running(self, **kwargs):
        return self.call('is_sequence_running', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

