from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAjaDcxs(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/aja/dcxs.py', 'class_name': 'DCXS', 'import_roots': [], 'candidate_methods': ['ask', 'read'], 'metadata': {'source_file': 'pymeasure/instruments/aja/dcxs.py', 'class_name': 'DCXS', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def ask(self, **kwargs):
            return self.call('ask', kwargs=kwargs)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

