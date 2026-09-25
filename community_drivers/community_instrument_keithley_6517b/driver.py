from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley6517b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithley6517b.py', 'class_name': 'Keithley6517B', 'import_roots': [], 'candidate_methods': ['enable_source', 'disable_source', 'measure_resistance', 'measure_voltage', 'measure_current', 'auto_range_source', 'apply_voltage', 'error', 'reset', 'ramp_to_voltage', 'trigger', 'trigger_immediately', 'trigger_on_bus', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithley6517b.py', 'class_name': 'Keithley6517B', 'candidate_score': 0.963, 'fix_note': 'reselected from tests->instruments'}}

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

        def apply_voltage(self, **kwargs):
            return self.call('apply_voltage', kwargs=kwargs)

        def error(self, **kwargs):
            return self.call('error', kwargs=kwargs)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

        def ramp_to_voltage(self, **kwargs):
            return self.call('ramp_to_voltage', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def trigger_immediately(self, **kwargs):
            return self.call('trigger_immediately', kwargs=kwargs)

        def trigger_on_bus(self, **kwargs):
            return self.call('trigger_on_bus', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

