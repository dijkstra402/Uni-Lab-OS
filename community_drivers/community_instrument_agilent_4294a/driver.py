from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilent4294a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent4294A.py', 'class_name': 'Agilent4294A', 'import_roots': [], 'candidate_methods': ['save_graphics', 'get_data'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilent4294A.py', 'class_name': 'Agilent4294A', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def save_graphics(self, **kwargs):
            return self.call('save_graphics', kwargs=kwargs)

        def get_data(self, **kwargs):
            return self.call('get_data', kwargs=kwargs)

