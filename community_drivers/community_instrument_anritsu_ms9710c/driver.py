from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAnritsuMs9710c(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/anritsu/anritsuMS9710C.py', 'class_name': 'AnritsuMS9710C', 'import_roots': [], 'candidate_methods': ['wavelengths', 'read_memory', 'wait', 'wait_for_sweep', 'single_sweep', 'center_at_peak', 'measure_peak'], 'metadata': {'source_file': 'pymeasure/instruments/anritsu/anritsuMS9710C.py', 'class_name': 'AnritsuMS9710C', 'candidate_score': 0.966, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def wavelengths(self, **kwargs):
            return self.call('wavelengths', kwargs=kwargs)

        def read_memory(self, **kwargs):
            return self.call('read_memory', kwargs=kwargs)

        def wait(self, **kwargs):
            return self.call('wait', kwargs=kwargs)

        def wait_for_sweep(self, **kwargs):
            return self.call('wait_for_sweep', kwargs=kwargs)

        def single_sweep(self, **kwargs):
            return self.call('single_sweep', kwargs=kwargs)

        def center_at_peak(self, **kwargs):
            return self.call('center_at_peak', kwargs=kwargs)

        def measure_peak(self, **kwargs):
            return self.call('measure_peak', kwargs=kwargs)

