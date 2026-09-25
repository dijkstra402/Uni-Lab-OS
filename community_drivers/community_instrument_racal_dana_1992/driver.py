from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentRacalDana1992(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/racal/racal1992.py', 'class_name': 'Racal1992', 'import_roots': [], 'candidate_methods': ['read', 'write', 'read_and_decode', 'channel_settings', 'preset', 'reset_measurement', 'wait_for_measurement', 'measured_value'], 'metadata': {'source_file': 'pymeasure/instruments/racal/racal1992.py', 'class_name': 'Racal1992', 'candidate_score': 0.829, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def read_and_decode(self, **kwargs):
            return self.call('read_and_decode', kwargs=kwargs)

        def channel_settings(self, **kwargs):
            return self.call('channel_settings', kwargs=kwargs)

        def preset(self, **kwargs):
            return self.call('preset', kwargs=kwargs)

        def reset_measurement(self, **kwargs):
            return self.call('reset_measurement', kwargs=kwargs)

        def wait_for_measurement(self, **kwargs):
            return self.call('wait_for_measurement', kwargs=kwargs)

        def measured_value(self, **kwargs):
            return self.call('measured_value', kwargs=kwargs)

