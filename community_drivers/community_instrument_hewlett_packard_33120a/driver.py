from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHewlettPackard33120a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/hp/hp33120A.py', 'class_name': 'HP33120A', 'import_roots': [], 'candidate_methods': ['beep'], 'metadata': {'source_file': 'pymeasure/instruments/hp/hp33120A.py', 'class_name': 'HP33120A', 'candidate_score': 0.857, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def beep(self, **kwargs):
            return self.call('beep', kwargs=kwargs)

