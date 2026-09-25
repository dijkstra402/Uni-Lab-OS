from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAnritsuMs9740a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/anritsu/anritsuMS9740A.py', 'class_name': 'AnritsuMS9740A', 'import_roots': [], 'candidate_methods': ['repeat_sweep'], 'metadata': {'source_file': 'pymeasure/instruments/anritsu/anritsuMS9740A.py', 'class_name': 'AnritsuMS9740A', 'candidate_score': 0.966, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def repeat_sweep(self, **kwargs):
            return self.call('repeat_sweep', kwargs=kwargs)

