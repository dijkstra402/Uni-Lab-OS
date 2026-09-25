from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOxfordInstrumentsItc503(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/oxfordinstruments/itc503.py', 'class_name': 'ITC503', 'import_roots': [], 'candidate_methods': ['wait_for_temperature', 'program_sweep', 'wipe_sweep_table'], 'metadata': {'source_file': 'pymeasure/instruments/oxfordinstruments/itc503.py', 'class_name': 'ITC503', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def wait_for_temperature(self, **kwargs):
            return self.call('wait_for_temperature', kwargs=kwargs)

        def program_sweep(self, **kwargs):
            return self.call('program_sweep', kwargs=kwargs)

        def wipe_sweep_table(self, **kwargs):
            return self.call('wipe_sweep_table', kwargs=kwargs)

