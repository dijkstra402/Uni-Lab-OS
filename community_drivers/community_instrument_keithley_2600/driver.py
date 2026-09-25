from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley2600(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithley2600.py', 'class_name': 'Keithley2600', 'import_roots': [], 'candidate_methods': ['next_error', 'error', 'ask', 'write', 'values', 'binary_values', 'check_errors', 'measure_voltage', 'measure_current', 'auto_range_source', 'apply_current', 'apply_voltage', 'ramp_to_voltage', 'ramp_to_current', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithley2600.py', 'class_name': 'Keithley2600', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def next_error(self, **kwargs):
            return self.call('next_error', kwargs=kwargs)

        def error(self, **kwargs):
            return self.call('error', kwargs=kwargs)

        def ask(self, **kwargs):
            return self.call('ask', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def values(self, **kwargs):
            return self.call('values', kwargs=kwargs)

        def binary_values(self, **kwargs):
            return self.call('binary_values', kwargs=kwargs)

        def check_errors(self, **kwargs):
            return self.call('check_errors', kwargs=kwargs)

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

        def ramp_to_voltage(self, **kwargs):
            return self.call('ramp_to_voltage', kwargs=kwargs)

        def ramp_to_current(self, **kwargs):
            return self.call('ramp_to_current', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

