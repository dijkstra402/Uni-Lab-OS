from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAnapicoApsin12g(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/anapico/apsin12G.py', 'class_name': 'APSIN12G', 'import_roots': [], 'candidate_methods': ['enable_rf', 'disable_rf'], 'metadata': {'source_file': 'pymeasure/instruments/anapico/apsin12G.py', 'class_name': 'APSIN12G', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def enable_rf(self, **kwargs):
            return self.call('enable_rf', kwargs=kwargs)

        def disable_rf(self, **kwargs):
            return self.call('disable_rf', kwargs=kwargs)

