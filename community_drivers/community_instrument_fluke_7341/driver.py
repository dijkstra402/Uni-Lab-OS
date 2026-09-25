from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentFluke7341(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/fluke/fluke7341.py', 'class_name': 'Fluke7341', 'import_roots': [], 'candidate_methods': ['read'], 'metadata': {'source_file': 'pymeasure/instruments/fluke/fluke7341.py', 'class_name': 'Fluke7341', 'candidate_score': 0.947, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

