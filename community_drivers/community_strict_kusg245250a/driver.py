from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictKusg245250a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/kuhneelectronic/kusg245_250a.py', 'class_name': 'Kusg245_250A', 'import_roots': [], 'candidate_methods': ['voltage_5v', 'voltage_32v', 'power_forward', 'power_reverse', 'external_enabled', 'bias_enabled', 'rf_enabled', 'pulse_mode_enabled', 'freq_steps_fine_enabled', 'phase_shift', 'reflection_limit', 'tune', 'clear_VSWR_error', 'store_settings', 'turn_off', 'turn_on', 'write', 'next_error', 'write_binary_values', 'read_binary_values', 'check_errors'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/kuhneelectronic/kusg245_250a.py', 'confidence': 0.8, 'quality_score': 0.94, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def voltage_5v(self, **kwargs):
        return self.call('voltage_5v', kwargs=kwargs)

    def voltage_32v(self, **kwargs):
        return self.call('voltage_32v', kwargs=kwargs)

    def power_forward(self, **kwargs):
        return self.call('power_forward', kwargs=kwargs)

    def power_reverse(self, **kwargs):
        return self.call('power_reverse', kwargs=kwargs)

    def external_enabled(self, **kwargs):
        return self.call('external_enabled', kwargs=kwargs)

    def bias_enabled(self, **kwargs):
        return self.call('bias_enabled', kwargs=kwargs)

    def rf_enabled(self, **kwargs):
        return self.call('rf_enabled', kwargs=kwargs)

    def pulse_mode_enabled(self, **kwargs):
        return self.call('pulse_mode_enabled', kwargs=kwargs)

    def freq_steps_fine_enabled(self, **kwargs):
        return self.call('freq_steps_fine_enabled', kwargs=kwargs)

    def phase_shift(self, **kwargs):
        return self.call('phase_shift', kwargs=kwargs)

    def reflection_limit(self, **kwargs):
        return self.call('reflection_limit', kwargs=kwargs)

    def tune(self, **kwargs):
        return self.call('tune', kwargs=kwargs)

    def clear_VSWR_error(self, **kwargs):
        return self.call('clear_VSWR_error', kwargs=kwargs)

    def store_settings(self, **kwargs):
        return self.call('store_settings', kwargs=kwargs)

    def turn_off(self, **kwargs):
        return self.call('turn_off', kwargs=kwargs)

    def turn_on(self, **kwargs):
        return self.call('turn_on', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

