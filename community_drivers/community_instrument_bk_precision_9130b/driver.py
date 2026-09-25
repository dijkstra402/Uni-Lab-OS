from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBkPrecision9130b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/bkprecision/bkprecision9130b.py', 'class_name': 'BKPrecision9130B', 'import_roots': [], 'candidate_methods': ['voltage', 'voltage'], 'metadata': {'source_file': 'pymeasure/instruments/bkprecision/bkprecision9130b.py', 'class_name': 'BKPrecision9130B', 'candidate_score': 0.941, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def voltage(self, **kwargs):
            return self.call('voltage', kwargs=kwargs)

        def voltage(self, **kwargs):
            return self.call('voltage', kwargs=kwargs)

