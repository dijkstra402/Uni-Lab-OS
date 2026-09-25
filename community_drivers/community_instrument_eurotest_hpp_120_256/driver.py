from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentEurotestHpp120256(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/eurotest/eurotestHPP120256.py', 'class_name': 'EurotestHPP120256', 'import_roots': [], 'candidate_methods': ['emergency_off', 'shutdown', 'ramp_to_zero', 'wait_for_output_voltage_reached', 'write', 'ask'], 'metadata': {'source_file': 'pymeasure/instruments/eurotest/eurotestHPP120256.py', 'class_name': 'EurotestHPP120256', 'candidate_score': 0.919, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def emergency_off(self, **kwargs):
            return self.call('emergency_off', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

        def ramp_to_zero(self, **kwargs):
            return self.call('ramp_to_zero', kwargs=kwargs)

        def wait_for_output_voltage_reached(self, **kwargs):
            return self.call('wait_for_output_voltage_reached', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def ask(self, **kwargs):
            return self.call('ask', kwargs=kwargs)

