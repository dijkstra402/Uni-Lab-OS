from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley2450(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithley2450.py', 'class_name': 'Keithley2450', 'import_roots': [], 'candidate_methods': ['enable_source', 'disable_source', 'measure_resistance', 'measure_voltage', 'measure_current', 'auto_range_source', 'apply_current', 'apply_voltage', 'beep', 'triad', 'error', 'reset', 'ramp_to_current', 'ramp_to_voltage', 'trigger', 'mean_voltage', 'max_voltage', 'min_voltage', 'std_voltage', 'mean_current'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithley2450.py', 'class_name': 'Keithley2450', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def enable_source(self, **kwargs):
            return self.call('enable_source', kwargs=kwargs)

        def disable_source(self, **kwargs):
            return self.call('disable_source', kwargs=kwargs)

        def measure_resistance(self, **kwargs):
            return self.call('measure_resistance', kwargs=kwargs)

        def measure_voltage(self, **kwargs):
            return self.call('measure_voltage', kwargs=kwargs)

        def measure_current(self, **kwargs):
            return self.call('measure_current', kwargs=kwargs)

        def auto_range_source(self, **kwargs):
            return self.call('auto_range_source', kwargs=kwargs)

        def apply_current(self, **kwargs):
            return self.call('apply_current', kwargs=kwargs)

        def apply_voltage(self, **kwargs):
            return self.call('apply_voltage', kwargs=kwargs)

        def beep(self, **kwargs):
            return self.call('beep', kwargs=kwargs)

        def triad(self, **kwargs):
            return self.call('triad', kwargs=kwargs)

        def error(self, **kwargs):
            return self.call('error', kwargs=kwargs)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

        def ramp_to_current(self, **kwargs):
            return self.call('ramp_to_current', kwargs=kwargs)

        def ramp_to_voltage(self, **kwargs):
            return self.call('ramp_to_voltage', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def mean_voltage(self, **kwargs):
            return self.call('mean_voltage', kwargs=kwargs)

        def max_voltage(self, **kwargs):
            return self.call('max_voltage', kwargs=kwargs)

        def min_voltage(self, **kwargs):
            return self.call('min_voltage', kwargs=kwargs)

        def std_voltage(self, **kwargs):
            return self.call('std_voltage', kwargs=kwargs)

        def mean_current(self, **kwargs):
            return self.call('mean_current', kwargs=kwargs)

