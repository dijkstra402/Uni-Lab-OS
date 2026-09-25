from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilent8257d(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent8257D.py', 'class_name': 'Agilent8257D', 'import_roots': [], 'candidate_methods': ['enable_low_freq_out', 'disable_low_freq_out', 'config_low_freq_out', 'enable', 'disable', 'enable_modulation', 'disable_modulation', 'config_amplitude_modulation', 'enable_amplitude_modulation', 'disable_amplitude_modulation', 'config_pulse_modulation', 'enable_pulse_modulation', 'disable_pulse_modulation', 'config_step_sweep', 'enable_retrace', 'disable_retrace', 'single_sweep', 'start_step_sweep', 'stop_step_sweep', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilent8257D.py', 'class_name': 'Agilent8257D', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

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

