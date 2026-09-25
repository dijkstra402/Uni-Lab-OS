from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLakeShore224(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/lakeshore/lakeshore224.py', 'class_name': 'LakeShore224', 'import_roots': [], 'candidate_methods': [], 'metadata': {'source_file': 'pymeasure/instruments/lakeshore/lakeshore224.py', 'class_name': 'LakeShore224', 'candidate_score': 0.923, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


