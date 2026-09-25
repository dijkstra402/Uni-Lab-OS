from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley2200(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithley2200.py', 'class_name': 'Keithley2200', 'import_roots': [], 'candidate_methods': ['insert_id'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithley2200.py', 'class_name': 'Keithley2200', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def insert_id(self, **kwargs):
            return self.call('insert_id', kwargs=kwargs)

