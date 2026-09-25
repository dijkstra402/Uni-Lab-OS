from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilentE5270b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilentE5270B.py', 'class_name': 'Display', 'import_roots': [], 'candidate_methods': ['clear', 'get_error_message', 'check_errors'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilentE5270B.py', 'class_name': 'Display', 'candidate_score': 0.963, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def clear(self, **kwargs):
            return self.call('clear', kwargs=kwargs)

        def get_error_message(self, **kwargs):
            return self.call('get_error_message', kwargs=kwargs)

        def check_errors(self, **kwargs):
            return self.call('check_errors', kwargs=kwargs)

