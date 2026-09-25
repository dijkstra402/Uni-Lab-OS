from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentSiglentSds1072cml(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/siglenttechnologies/siglent_sds1072cml.py', 'class_name': 'SDS1072CML', 'import_roots': [], 'candidate_methods': ['get_waveform', 'get_descriptor', 'get_trigger_config', 'set_trigger_config', 'wait', 'arm'], 'metadata': {'source_file': 'pymeasure/instruments/siglenttechnologies/siglent_sds1072cml.py', 'class_name': 'SDS1072CML', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def get_waveform(self, **kwargs):
            return self.call('get_waveform', kwargs=kwargs)

        def get_descriptor(self, **kwargs):
            return self.call('get_descriptor', kwargs=kwargs)

        def get_trigger_config(self, **kwargs):
            return self.call('get_trigger_config', kwargs=kwargs)

        def set_trigger_config(self, **kwargs):
            return self.call('set_trigger_config', kwargs=kwargs)

        def wait(self, **kwargs):
            return self.call('wait', kwargs=kwargs)

        def arm(self, **kwargs):
            return self.call('arm', kwargs=kwargs)

