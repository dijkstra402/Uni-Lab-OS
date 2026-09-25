from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIlxLightwaveLdp3811(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/ilxlightwave/ldp3811.py', 'class_name': 'LDP3811Mode', 'import_roots': [], 'candidate_methods': ['check_errors', 'current_setpoint', 'current_setpoint', 'duty_cycle_setpoint', 'duty_cycle_setpoint', 'set_to_min_duty_cycle', 'set_to_max_duty_cycle', 'pulse_repetition_interval_setpoint', 'pulse_repetition_interval_setpoint', 'pulse_width_setpoint', 'pulse_width_setpoint'], 'metadata': {'source_file': 'pymeasure/instruments/ilxlightwave/ldp3811.py', 'class_name': 'LDP3811Mode', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def check_errors(self, **kwargs):
            return self.call('check_errors', kwargs=kwargs)

        def current_setpoint(self, **kwargs):
            return self.call('current_setpoint', kwargs=kwargs)

        def current_setpoint(self, **kwargs):
            return self.call('current_setpoint', kwargs=kwargs)

        def duty_cycle_setpoint(self, **kwargs):
            return self.call('duty_cycle_setpoint', kwargs=kwargs)

        def duty_cycle_setpoint(self, **kwargs):
            return self.call('duty_cycle_setpoint', kwargs=kwargs)

        def set_to_min_duty_cycle(self, **kwargs):
            return self.call('set_to_min_duty_cycle', kwargs=kwargs)

        def set_to_max_duty_cycle(self, **kwargs):
            return self.call('set_to_max_duty_cycle', kwargs=kwargs)

        def pulse_repetition_interval_setpoint(self, **kwargs):
            return self.call('pulse_repetition_interval_setpoint', kwargs=kwargs)

        def pulse_repetition_interval_setpoint(self, **kwargs):
            return self.call('pulse_repetition_interval_setpoint', kwargs=kwargs)

        def pulse_width_setpoint(self, **kwargs):
            return self.call('pulse_width_setpoint', kwargs=kwargs)

        def pulse_width_setpoint(self, **kwargs):
            return self.call('pulse_width_setpoint', kwargs=kwargs)

