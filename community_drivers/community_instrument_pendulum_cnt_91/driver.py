from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPendulumCnt91(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/pendulum/cnt91.py', 'class_name': 'CNT91', 'import_roots': [], 'candidate_methods': ['batch_size', 'measurement_time', 'measurement_time', 'read_buffer', 'configure_frequency_array_measurement'], 'metadata': {'source_file': 'pymeasure/instruments/pendulum/cnt91.py', 'class_name': 'CNT91', 'candidate_score': 0.85, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def batch_size(self, **kwargs):
            return self.call('batch_size', kwargs=kwargs)

        def measurement_time(self, **kwargs):
            return self.call('measurement_time', kwargs=kwargs)

        def measurement_time(self, **kwargs):
            return self.call('measurement_time', kwargs=kwargs)

        def read_buffer(self, **kwargs):
            return self.call('read_buffer', kwargs=kwargs)

        def configure_frequency_array_measurement(self, **kwargs):
            return self.call('configure_frequency_array_measurement', kwargs=kwargs)

