from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentSignalRecoveryDsp7265(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/signalrecovery/dsp7265.py', 'class_name': 'DSP7265', 'import_roots': [], 'candidate_methods': ['adc3', 'adc3_time', 'adc3_time'], 'metadata': {'source_file': 'pymeasure/instruments/signalrecovery/dsp7265.py', 'class_name': 'DSP7265', 'candidate_score': 0.727, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def adc3(self, **kwargs):
            return self.call('adc3', kwargs=kwargs)

        def adc3_time(self, **kwargs):
            return self.call('adc3_time', kwargs=kwargs)

        def adc3_time(self, **kwargs):
            return self.call('adc3_time', kwargs=kwargs)

