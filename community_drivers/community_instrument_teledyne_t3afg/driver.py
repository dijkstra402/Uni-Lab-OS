from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTeledyneT3afg(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/teledyne/teledyneT3AFG.py', 'class_name': 'TeledyneT3AFG', 'import_roots': [], 'candidate_methods': [], 'metadata': {'source_file': 'pymeasure/instruments/teledyne/teledyneT3AFG.py', 'class_name': 'TeledyneT3AFG', 'candidate_score': 0.963, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


