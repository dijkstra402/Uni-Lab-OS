from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley4200(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithley4200.py', 'class_name': 'StatusCode', 'import_roots': [], 'candidate_methods': ['disable', 'add_smu', 'check_set_errors', 'clear'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithley4200.py', 'class_name': 'StatusCode', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def disable(self, **kwargs):
            return self.call('disable', kwargs=kwargs)

        def add_smu(self, **kwargs):
            return self.call('add_smu', kwargs=kwargs)

        def check_set_errors(self, **kwargs):
            return self.call('check_set_errors', kwargs=kwargs)

        def clear(self, **kwargs):
            return self.call('clear', kwargs=kwargs)

