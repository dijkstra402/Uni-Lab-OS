from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHcpTc0382(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/hcp/tc038.py', 'class_name': 'TC038', 'import_roots': [], 'candidate_methods': ['write', 'read', 'check_set_errors', 'set_monitored_quantity'], 'metadata': {'source_file': 'pymeasure/instruments/hcp/tc038.py', 'class_name': 'TC038', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def check_set_errors(self, **kwargs):
            return self.call('check_set_errors', kwargs=kwargs)

        def set_monitored_quantity(self, **kwargs):
            return self.call('set_monitored_quantity', kwargs=kwargs)

