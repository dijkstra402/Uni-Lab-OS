from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeysightE36312a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keysight/keysightE36312A.py', 'class_name': 'KeysightE36312A', 'import_roots': [], 'candidate_methods': [], 'metadata': {'source_file': 'pymeasure/instruments/keysight/keysightE36312A.py', 'class_name': 'KeysightE36312A', 'candidate_score': 0.968, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


