from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentFWBell5080(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/fwbell/fwbell5080.py', 'class_name': 'FWBell5080', 'import_roots': [], 'candidate_methods': ['read', 'reset', 'fields', 'auto_range'], 'metadata': {'source_file': 'pymeasure/instruments/fwbell/fwbell5080.py', 'class_name': 'FWBell5080', 'candidate_score': 0.87, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

        def fields(self, **kwargs):
            return self.call('fields', kwargs=kwargs)

        def auto_range(self, **kwargs):
            return self.call('auto_range', kwargs=kwargs)

