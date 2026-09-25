from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTexioPsw360l30(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/texio/texioPSW360L30.py', 'class_name': 'TexioPSW360L30', 'import_roots': [], 'candidate_methods': ['check_errors'], 'metadata': {'source_file': 'pymeasure/instruments/texio/texioPSW360L30.py', 'class_name': 'TexioPSW360L30', 'candidate_score': 0.933, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def check_errors(self, **kwargs):
            return self.call('check_errors', kwargs=kwargs)

