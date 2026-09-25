from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAntonPaarMcr302(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/ipgphotonics/yar.py', 'class_name': 'YAR', 'import_roots': [], 'candidate_methods': ['read', 'check_set_errors', 'id', 'status', 'power_range', 'clear'], 'metadata': {'source_file': 'pymeasure/instruments/ipgphotonics/yar.py', 'class_name': 'YAR', 'candidate_score': 0.571, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def check_set_errors(self, **kwargs):
            return self.call('check_set_errors', kwargs=kwargs)

        def id(self, **kwargs):
            return self.call('id', kwargs=kwargs)

        def status(self, **kwargs):
            return self.call('status', kwargs=kwargs)

        def power_range(self, **kwargs):
            return self.call('power_range', kwargs=kwargs)

        def clear(self, **kwargs):
            return self.call('clear', kwargs=kwargs)

