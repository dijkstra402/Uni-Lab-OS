from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThyracontVsp(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/thyracont/smartline_v2.py', 'class_name': 'Sources', 'import_roots': [], 'candidate_methods': ['write', 'write_composition', 'ask', 'ask_manually', 'read', 'check_set_errors', 'set_high', 'set_low', 'get_sensor_transition', 'set_default_sensor_transition', 'set_continuous_sensor_transition', 'set_direct_sensor_transition'], 'metadata': {'source_file': 'pymeasure/instruments/thyracont/smartline_v2.py', 'class_name': 'Sources', 'candidate_score': 0.514, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def write_composition(self, **kwargs):
            return self.call('write_composition', kwargs=kwargs)

        def ask(self, **kwargs):
            return self.call('ask', kwargs=kwargs)

        def ask_manually(self, **kwargs):
            return self.call('ask_manually', kwargs=kwargs)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def check_set_errors(self, **kwargs):
            return self.call('check_set_errors', kwargs=kwargs)

        def set_high(self, **kwargs):
            return self.call('set_high', kwargs=kwargs)

        def set_low(self, **kwargs):
            return self.call('set_low', kwargs=kwargs)

        def get_sensor_transition(self, **kwargs):
            return self.call('get_sensor_transition', kwargs=kwargs)

        def set_default_sensor_transition(self, **kwargs):
            return self.call('set_default_sensor_transition', kwargs=kwargs)

        def set_continuous_sensor_transition(self, **kwargs):
            return self.call('set_continuous_sensor_transition', kwargs=kwargs)

        def set_direct_sensor_transition(self, **kwargs):
            return self.call('set_direct_sensor_transition', kwargs=kwargs)

