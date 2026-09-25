from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeysightDsox1102g(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keysight/keysightDSOX1102G.py', 'class_name': 'KeysightDSOX1102G', 'import_roots': [], 'candidate_methods': ['values', 'ask', 'write', 'setup', 'current_configuration', 'autoscale', 'timebase', 'run', 'stop', 'single', 'digitize', 'waveform_preamble', 'waveform_data', 'system_setup', 'system_setup', 'ch', 'clear_status', 'factory_reset', 'default_setup', 'timebase_setup'], 'metadata': {'source_file': 'pymeasure/instruments/keysight/keysightDSOX1102G.py', 'class_name': 'KeysightDSOX1102G', 'candidate_score': 0.971, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def values(self, **kwargs):
            return self.call('values', kwargs=kwargs)

        def ask(self, **kwargs):
            return self.call('ask', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def setup(self, **kwargs):
            return self.call('setup', kwargs=kwargs)

        def current_configuration(self, **kwargs):
            return self.call('current_configuration', kwargs=kwargs)

        def autoscale(self, **kwargs):
            return self.call('autoscale', kwargs=kwargs)

        def timebase(self, **kwargs):
            return self.call('timebase', kwargs=kwargs)

        def run(self, **kwargs):
            return self.call('run', kwargs=kwargs)

        def stop(self, **kwargs):
            return self.call('stop', kwargs=kwargs)

        def single(self, **kwargs):
            return self.call('single', kwargs=kwargs)

        def digitize(self, **kwargs):
            return self.call('digitize', kwargs=kwargs)

        def waveform_preamble(self, **kwargs):
            return self.call('waveform_preamble', kwargs=kwargs)

        def waveform_data(self, **kwargs):
            return self.call('waveform_data', kwargs=kwargs)

        def system_setup(self, **kwargs):
            return self.call('system_setup', kwargs=kwargs)

        def system_setup(self, **kwargs):
            return self.call('system_setup', kwargs=kwargs)

        def ch(self, **kwargs):
            return self.call('ch', kwargs=kwargs)

        def clear_status(self, **kwargs):
            return self.call('clear_status', kwargs=kwargs)

        def factory_reset(self, **kwargs):
            return self.call('factory_reset', kwargs=kwargs)

        def default_setup(self, **kwargs):
            return self.call('default_setup', kwargs=kwargs)

        def timebase_setup(self, **kwargs):
            return self.call('timebase_setup', kwargs=kwargs)

