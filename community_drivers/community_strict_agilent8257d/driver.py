from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAgilent8257d(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent8257D.py', 'class_name': 'Agilent8257D', 'import_roots': [], 'candidate_methods': ['enable_low_freq_out', 'disable_low_freq_out', 'config_low_freq_out', 'enable', 'disable', 'enable_modulation', 'disable_modulation', 'config_amplitude_modulation', 'enable_amplitude_modulation', 'disable_amplitude_modulation', 'config_pulse_modulation', 'enable_pulse_modulation', 'disable_pulse_modulation', 'config_step_sweep', 'enable_retrace', 'disable_retrace', 'single_sweep', 'start_step_sweep', 'stop_step_sweep', 'shutdown', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/agilent/agilent8257D.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def enable_low_freq_out(self, **kwargs):
        return self.call('enable_low_freq_out', kwargs=kwargs)

    def disable_low_freq_out(self, **kwargs):
        return self.call('disable_low_freq_out', kwargs=kwargs)

    def config_low_freq_out(self, **kwargs):
        return self.call('config_low_freq_out', kwargs=kwargs)

    def enable(self, **kwargs):
        return self.call('enable', kwargs=kwargs)

    def disable(self, **kwargs):
        return self.call('disable', kwargs=kwargs)

    def enable_modulation(self, **kwargs):
        return self.call('enable_modulation', kwargs=kwargs)

    def disable_modulation(self, **kwargs):
        return self.call('disable_modulation', kwargs=kwargs)

    def config_amplitude_modulation(self, **kwargs):
        return self.call('config_amplitude_modulation', kwargs=kwargs)

    def enable_amplitude_modulation(self, **kwargs):
        return self.call('enable_amplitude_modulation', kwargs=kwargs)

    def disable_amplitude_modulation(self, **kwargs):
        return self.call('disable_amplitude_modulation', kwargs=kwargs)

    def config_pulse_modulation(self, **kwargs):
        return self.call('config_pulse_modulation', kwargs=kwargs)

    def enable_pulse_modulation(self, **kwargs):
        return self.call('enable_pulse_modulation', kwargs=kwargs)

    def disable_pulse_modulation(self, **kwargs):
        return self.call('disable_pulse_modulation', kwargs=kwargs)

    def config_step_sweep(self, **kwargs):
        return self.call('config_step_sweep', kwargs=kwargs)

    def enable_retrace(self, **kwargs):
        return self.call('enable_retrace', kwargs=kwargs)

    def disable_retrace(self, **kwargs):
        return self.call('disable_retrace', kwargs=kwargs)

    def single_sweep(self, **kwargs):
        return self.call('single_sweep', kwargs=kwargs)

    def start_step_sweep(self, **kwargs):
        return self.call('start_step_sweep', kwargs=kwargs)

    def stop_step_sweep(self, **kwargs):
        return self.call('stop_step_sweep', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

