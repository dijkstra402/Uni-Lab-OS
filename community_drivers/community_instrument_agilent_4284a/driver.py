from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilent4284a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent4284A.py', 'class_name': 'Agilent4284ASpot', 'import_roots': [], 'candidate_methods': ['measure_open', 'measure_short', 'measure_load', 'measure_open', 'measure_short', 'measure_load', 'high_power_enabled', 'high_power_enabled', 'sweep_measurement', 'trigger', 'trigger_immediate', 'trigger_initiate'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilent4284A.py', 'class_name': 'Agilent4284ASpot', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def measure_open(self, **kwargs):
            return self.call('measure_open', kwargs=kwargs)

        def measure_short(self, **kwargs):
            return self.call('measure_short', kwargs=kwargs)

        def measure_load(self, **kwargs):
            return self.call('measure_load', kwargs=kwargs)

        def measure_open(self, **kwargs):
            return self.call('measure_open', kwargs=kwargs)

        def measure_short(self, **kwargs):
            return self.call('measure_short', kwargs=kwargs)

        def measure_load(self, **kwargs):
            return self.call('measure_load', kwargs=kwargs)

        def high_power_enabled(self, **kwargs):
            return self.call('high_power_enabled', kwargs=kwargs)

        def high_power_enabled(self, **kwargs):
            return self.call('high_power_enabled', kwargs=kwargs)

        def sweep_measurement(self, **kwargs):
            return self.call('sweep_measurement', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def trigger_immediate(self, **kwargs):
            return self.call('trigger_immediate', kwargs=kwargs)

        def trigger_initiate(self, **kwargs):
            return self.call('trigger_initiate', kwargs=kwargs)

