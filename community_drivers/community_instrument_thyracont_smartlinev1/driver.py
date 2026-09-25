from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThyracontSmartlinev1(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/thyracont/smartline_v1.py', 'class_name': 'SmartlineV1', 'import_roots': [], 'candidate_methods': ['read', 'write', 'check_set_errors'], 'metadata': {'source_file': 'pymeasure/instruments/thyracont/smartline_v1.py', 'class_name': 'SmartlineV1', 'candidate_score': 0.974, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def check_set_errors(self, **kwargs):
            return self.call('check_set_errors', kwargs=kwargs)

