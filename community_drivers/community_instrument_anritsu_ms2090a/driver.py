from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAnritsuMs2090a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/anritsu/anritsuMS2090A.py', 'class_name': 'AnritsuMS2090A', 'import_roots': [], 'candidate_methods': ['init_sweep', 'init_all_sweep', 'abort'], 'metadata': {'source_file': 'pymeasure/instruments/anritsu/anritsuMS2090A.py', 'class_name': 'AnritsuMS2090A', 'candidate_score': 0.966, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def init_sweep(self, **kwargs):
            return self.call('init_sweep', kwargs=kwargs)

        def init_all_sweep(self, **kwargs):
            return self.call('init_all_sweep', kwargs=kwargs)

        def abort(self, **kwargs):
            return self.call('abort', kwargs=kwargs)

