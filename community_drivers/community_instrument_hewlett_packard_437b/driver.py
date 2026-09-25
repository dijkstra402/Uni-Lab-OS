from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHewlettPackard437b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/hp/hp437b.py', 'class_name': 'MeasurementUnit', 'import_roots': [], 'candidate_methods': ['check_errors', 'activate_auto_range', 'calibrate', 'calibration_factor', 'calibration_factor', 'duty_cycle', 'duty_cycle', 'frequency', 'frequency', 'limit_high', 'limit_high', 'limit_low', 'limit_low', 'offset', 'offset', 'reset', 'clear_status_registers', 'preset', 'resolution', 'resolution'], 'metadata': {'source_file': 'pymeasure/instruments/hp/hp437b.py', 'class_name': 'MeasurementUnit', 'candidate_score': 0.8, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def check_errors(self, **kwargs):
            return self.call('check_errors', kwargs=kwargs)

        def activate_auto_range(self, **kwargs):
            return self.call('activate_auto_range', kwargs=kwargs)

        def calibrate(self, **kwargs):
            return self.call('calibrate', kwargs=kwargs)

        def calibration_factor(self, **kwargs):
            return self.call('calibration_factor', kwargs=kwargs)

        def calibration_factor(self, **kwargs):
            return self.call('calibration_factor', kwargs=kwargs)

        def duty_cycle(self, **kwargs):
            return self.call('duty_cycle', kwargs=kwargs)

        def duty_cycle(self, **kwargs):
            return self.call('duty_cycle', kwargs=kwargs)

        def frequency(self, **kwargs):
            return self.call('frequency', kwargs=kwargs)

        def frequency(self, **kwargs):
            return self.call('frequency', kwargs=kwargs)

        def limit_high(self, **kwargs):
            return self.call('limit_high', kwargs=kwargs)

        def limit_high(self, **kwargs):
            return self.call('limit_high', kwargs=kwargs)

        def limit_low(self, **kwargs):
            return self.call('limit_low', kwargs=kwargs)

        def limit_low(self, **kwargs):
            return self.call('limit_low', kwargs=kwargs)

        def offset(self, **kwargs):
            return self.call('offset', kwargs=kwargs)

        def offset(self, **kwargs):
            return self.call('offset', kwargs=kwargs)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

        def clear_status_registers(self, **kwargs):
            return self.call('clear_status_registers', kwargs=kwargs)

        def preset(self, **kwargs):
            return self.call('preset', kwargs=kwargs)

        def resolution(self, **kwargs):
            return self.call('resolution', kwargs=kwargs)

        def resolution(self, **kwargs):
            return self.call('resolution', kwargs=kwargs)

