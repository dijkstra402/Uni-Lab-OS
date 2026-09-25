from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPcoPcoEdge4255(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/kepco/kepcobop.py', 'class_name': 'KepcoBOP3612', 'import_roots': [], 'candidate_methods': ['beep', 'wait_to_continue'], 'metadata': {'source_file': 'pymeasure/instruments/kepco/kepcobop.py', 'class_name': 'KepcoBOP3612', 'candidate_score': 0.627, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def beep(self, **kwargs):
            return self.call('beep', kwargs=kwargs)

        def wait_to_continue(self, **kwargs):
            return self.call('wait_to_continue', kwargs=kwargs)

