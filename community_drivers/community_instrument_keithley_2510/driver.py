from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley2510(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithley2510.py', 'class_name': 'Keithley2510', 'import_roots': [], 'candidate_methods': ['temperature_protection_range', 'temperature_protection_range', 'temperature_pid', 'temperature_pid', 'enable_source', 'disable_source', 'enable_temperature_protection', 'disable_temperature_protection', 'check_temperature_stability'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithley2510.py', 'class_name': 'Keithley2510', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def temperature_protection_range(self, **kwargs):
            return self.call('temperature_protection_range', kwargs=kwargs)

        def temperature_protection_range(self, **kwargs):
            return self.call('temperature_protection_range', kwargs=kwargs)

        def temperature_pid(self, **kwargs):
            return self.call('temperature_pid', kwargs=kwargs)

        def temperature_pid(self, **kwargs):
            return self.call('temperature_pid', kwargs=kwargs)

        def enable_source(self, **kwargs):
            return self.call('enable_source', kwargs=kwargs)

        def disable_source(self, **kwargs):
            return self.call('disable_source', kwargs=kwargs)

        def enable_temperature_protection(self, **kwargs):
            return self.call('enable_temperature_protection', kwargs=kwargs)

        def disable_temperature_protection(self, **kwargs):
            return self.call('disable_temperature_protection', kwargs=kwargs)

        def check_temperature_stability(self, **kwargs):
            return self.call('check_temperature_stability', kwargs=kwargs)

