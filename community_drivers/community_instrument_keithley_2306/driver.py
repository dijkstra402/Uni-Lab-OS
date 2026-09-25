from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley2306(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithley2306.py', 'class_name': 'Step', 'import_roots': [], 'candidate_methods': ['pulse_current_time_auto', 'long_integration_time_auto', 'pulse_current_step', 'ch', 'relay'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithley2306.py', 'class_name': 'Step', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def pulse_current_time_auto(self, **kwargs):
            return self.call('pulse_current_time_auto', kwargs=kwargs)

        def long_integration_time_auto(self, **kwargs):
            return self.call('long_integration_time_auto', kwargs=kwargs)

        def pulse_current_step(self, **kwargs):
            return self.call('pulse_current_step', kwargs=kwargs)

        def ch(self, **kwargs):
            return self.call('ch', kwargs=kwargs)

        def relay(self, **kwargs):
            return self.call('relay', kwargs=kwargs)

