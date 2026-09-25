from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentActiveTechnologiesAwg401x(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/activetechnologies/AWG401x.py', 'class_name': 'ChannelAFG', 'import_roots': [], 'candidate_methods': ['calculate_voltage_range', 'beep', 'save', 'load', 'wait_last', 'trigger', 'save_file', 'remove_file', 'list_files', 'reset', 'resize', 'insert_id', 'insert_id', 'calculate_voltage_range'], 'metadata': {'source_file': 'pymeasure/instruments/activetechnologies/AWG401x.py', 'class_name': 'ChannelAFG', 'candidate_score': 0.756, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def calculate_voltage_range(self, **kwargs):
            return self.call('calculate_voltage_range', kwargs=kwargs)

        def beep(self, **kwargs):
            return self.call('beep', kwargs=kwargs)

        def save(self, **kwargs):
            return self.call('save', kwargs=kwargs)

        def load(self, **kwargs):
            return self.call('load', kwargs=kwargs)

        def wait_last(self, **kwargs):
            return self.call('wait_last', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def save_file(self, **kwargs):
            return self.call('save_file', kwargs=kwargs)

        def remove_file(self, **kwargs):
            return self.call('remove_file', kwargs=kwargs)

        def list_files(self, **kwargs):
            return self.call('list_files', kwargs=kwargs)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

        def resize(self, **kwargs):
            return self.call('resize', kwargs=kwargs)

        def insert_id(self, **kwargs):
            return self.call('insert_id', kwargs=kwargs)

        def insert_id(self, **kwargs):
            return self.call('insert_id', kwargs=kwargs)

        def calculate_voltage_range(self, **kwargs):
            return self.call('calculate_voltage_range', kwargs=kwargs)

