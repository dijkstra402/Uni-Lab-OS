from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOxfordInstrumentsPs12010(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/oxfordinstruments/ps120_10.py', 'class_name': 'PS120_10', 'import_roots': [], 'candidate_methods': [], 'metadata': {'source_file': 'pymeasure/instruments/oxfordinstruments/ps120_10.py', 'class_name': 'PS120_10', 'candidate_score': 0.776, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


