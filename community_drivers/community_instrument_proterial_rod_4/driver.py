from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentProterialRod4(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/proterial/rod4.py', 'class_name': 'ROD4', 'import_roots': [], 'candidate_methods': ['check_set_errors'], 'metadata': {'source_file': 'pymeasure/instruments/proterial/rod4.py', 'class_name': 'ROD4', 'candidate_score': 0.914, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def check_set_errors(self, **kwargs):
            return self.call('check_set_errors', kwargs=kwargs)

