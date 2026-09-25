from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentRohdeSchwarzSfm(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/rohdeschwarz/sfm.py', 'class_name': 'SFM', 'import_roots': [], 'candidate_methods': ['values', 'ask', 'write', 'read', 'calibration', 'channel_up_relative', 'channel_down_relative', 'coder_adjust', 'status_preset'], 'metadata': {'source_file': 'pymeasure/instruments/rohdeschwarz/sfm.py', 'class_name': 'SFM', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

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

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def calibration(self, **kwargs):
            return self.call('calibration', kwargs=kwargs)

        def channel_up_relative(self, **kwargs):
            return self.call('channel_up_relative', kwargs=kwargs)

        def channel_down_relative(self, **kwargs):
            return self.call('channel_down_relative', kwargs=kwargs)

        def coder_adjust(self, **kwargs):
            return self.call('coder_adjust', kwargs=kwargs)

        def status_preset(self, **kwargs):
            return self.call('status_preset', kwargs=kwargs)

