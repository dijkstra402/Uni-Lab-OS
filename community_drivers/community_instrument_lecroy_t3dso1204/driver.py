from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLecroyT3dso1204(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/lecroy/lecroyT3DSO1204.py', 'class_name': 'LeCroyT3DSO1204', 'import_roots': [], 'candidate_methods': ['timebase', 'timebase_setup', 'acquisition_sample_size', 'waveform_preamble'], 'metadata': {'source_file': 'pymeasure/instruments/lecroy/lecroyT3DSO1204.py', 'class_name': 'LeCroyT3DSO1204', 'candidate_score': 0.968, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def timebase(self, **kwargs):
            return self.call('timebase', kwargs=kwargs)

        def timebase_setup(self, **kwargs):
            return self.call('timebase_setup', kwargs=kwargs)

        def acquisition_sample_size(self, **kwargs):
            return self.call('acquisition_sample_size', kwargs=kwargs)

        def waveform_preamble(self, **kwargs):
            return self.call('waveform_preamble', kwargs=kwargs)

