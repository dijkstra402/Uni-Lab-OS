from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentWatersAcquityUplc(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/aculight/argos.py', 'class_name': 'State', 'import_roots': [], 'candidate_methods': ['wait_for', 'check_set_errors', 'state'], 'metadata': {'source_file': 'pymeasure/instruments/aculight/argos.py', 'class_name': 'State', 'candidate_score': 0.545, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def wait_for(self, **kwargs):
            return self.call('wait_for', kwargs=kwargs)

        def check_set_errors(self, **kwargs):
            return self.call('check_set_errors', kwargs=kwargs)

        def state(self, **kwargs):
            return self.call('state', kwargs=kwargs)

