from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilent4156(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent4156.py', 'class_name': 'Agilent4156', 'import_roots': [], 'candidate_methods': ['stop', 'measure', 'disable_all', 'configure', 'save', 'save_var', 'data_variables', 'get_data', 'reset_settings', 'disable', 'constant_value', 'constant_value', 'compliance', 'compliance', 'constant_value', 'constant_value', 'channel_mode', 'start', 'start', 'stop'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilent4156.py', 'class_name': 'Agilent4156', 'candidate_score': 0.957, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def stop(self, **kwargs):
            return self.call('stop', kwargs=kwargs)

        def measure(self, **kwargs):
            return self.call('measure', kwargs=kwargs)

        def disable_all(self, **kwargs):
            return self.call('disable_all', kwargs=kwargs)

        def configure(self, **kwargs):
            return self.call('configure', kwargs=kwargs)

        def save(self, **kwargs):
            return self.call('save', kwargs=kwargs)

        def save_var(self, **kwargs):
            return self.call('save_var', kwargs=kwargs)

        def data_variables(self, **kwargs):
            return self.call('data_variables', kwargs=kwargs)

        def get_data(self, **kwargs):
            return self.call('get_data', kwargs=kwargs)

        def reset_settings(self, **kwargs):
            return self.call('reset_settings', kwargs=kwargs)

        def disable(self, **kwargs):
            return self.call('disable', kwargs=kwargs)

        def constant_value(self, **kwargs):
            return self.call('constant_value', kwargs=kwargs)

        def constant_value(self, **kwargs):
            return self.call('constant_value', kwargs=kwargs)

        def compliance(self, **kwargs):
            return self.call('compliance', kwargs=kwargs)

        def compliance(self, **kwargs):
            return self.call('compliance', kwargs=kwargs)

        def constant_value(self, **kwargs):
            return self.call('constant_value', kwargs=kwargs)

        def constant_value(self, **kwargs):
            return self.call('constant_value', kwargs=kwargs)

        def channel_mode(self, **kwargs):
            return self.call('channel_mode', kwargs=kwargs)

        def start(self, **kwargs):
            return self.call('start', kwargs=kwargs)

        def start(self, **kwargs):
            return self.call('start', kwargs=kwargs)

        def stop(self, **kwargs):
            return self.call('stop', kwargs=kwargs)

