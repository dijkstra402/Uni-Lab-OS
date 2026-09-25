from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeysightN5767a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keysight/keysightN5767A.py', 'class_name': 'KeysightN5767A', 'import_roots': [], 'candidate_methods': ['enable', 'disable', 'is_enabled'], 'metadata': {'source_file': 'pymeasure/instruments/keysight/keysightN5767A.py', 'class_name': 'KeysightN5767A', 'candidate_score': 0.966, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def enable(self, **kwargs):
            return self.call('enable', kwargs=kwargs)

        def disable(self, **kwargs):
            return self.call('disable', kwargs=kwargs)

        def is_enabled(self, **kwargs):
            return self.call('is_enabled', kwargs=kwargs)

