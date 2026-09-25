from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley2400(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithley2400.py', 'class_name': 'Keithley2400', 'import_roots': [], 'candidate_methods': ['reset_data_format', 'enable_source', 'disable_source', 'auto_zero_once', 'auto_range_source', 'measure_all', 'measure_current', 'ramp_to_current', 'apply_current', 'measure_voltage', 'ramp_to_voltage', 'apply_voltage', 'measure_resistance', 'mean_voltage', 'max_voltage', 'min_voltage', 'std_voltage', 'mean_current', 'max_current', 'min_current'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithley2400.py', 'class_name': 'Keithley2400', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def reset_data_format(self, **kwargs):
            return self.call('reset_data_format', kwargs=kwargs)

        def enable_source(self, **kwargs):
            return self.call('enable_source', kwargs=kwargs)

        def disable_source(self, **kwargs):
            return self.call('disable_source', kwargs=kwargs)

        def auto_zero_once(self, **kwargs):
            return self.call('auto_zero_once', kwargs=kwargs)

        def auto_range_source(self, **kwargs):
            return self.call('auto_range_source', kwargs=kwargs)

        def measure_all(self, **kwargs):
            return self.call('measure_all', kwargs=kwargs)

        def measure_current(self, **kwargs):
            return self.call('measure_current', kwargs=kwargs)

        def ramp_to_current(self, **kwargs):
            return self.call('ramp_to_current', kwargs=kwargs)

        def apply_current(self, **kwargs):
            return self.call('apply_current', kwargs=kwargs)

        def measure_voltage(self, **kwargs):
            return self.call('measure_voltage', kwargs=kwargs)

        def ramp_to_voltage(self, **kwargs):
            return self.call('ramp_to_voltage', kwargs=kwargs)

        def apply_voltage(self, **kwargs):
            return self.call('apply_voltage', kwargs=kwargs)

        def measure_resistance(self, **kwargs):
            return self.call('measure_resistance', kwargs=kwargs)

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

        def max_current(self, **kwargs):
            return self.call('max_current', kwargs=kwargs)

        def min_current(self, **kwargs):
            return self.call('min_current', kwargs=kwargs)

