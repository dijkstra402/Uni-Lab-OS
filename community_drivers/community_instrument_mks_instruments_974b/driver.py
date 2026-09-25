from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMksInstruments974b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/mksinst/mks974b.py', 'class_name': 'Unit', 'import_roots': [], 'candidate_methods': ['id'], 'metadata': {'source_file': 'pymeasure/instruments/mksinst/mks974b.py', 'class_name': 'Unit', 'candidate_score': 0.727, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def id(self, **kwargs):
            return self.call('id', kwargs=kwargs)

