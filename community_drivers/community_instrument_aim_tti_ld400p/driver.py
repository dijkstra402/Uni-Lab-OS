from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAimTtiLd400p(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/aimtti/ld400p.py', 'class_name': 'LD400P', 'import_roots': [], 'candidate_methods': ['options', 'next_error', 'check_errors'], 'metadata': {'source_file': 'pymeasure/instruments/aimtti/ld400p.py', 'class_name': 'LD400P', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def options(self, **kwargs):
            return self.call('options', kwargs=kwargs)

        def next_error(self, **kwargs):
            return self.call('next_error', kwargs=kwargs)

        def check_errors(self, **kwargs):
            return self.call('check_errors', kwargs=kwargs)

