from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHewlettPackard34401a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/hp/hp34401A.py', 'class_name': 'HP34401A', 'import_roots': [], 'candidate_methods': ['trigger_single_autozero', 'init_trigger', 'beep', 'write'], 'metadata': {'source_file': 'pymeasure/instruments/hp/hp34401A.py', 'class_name': 'HP34401A', 'candidate_score': 0.857, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def trigger_single_autozero(self, **kwargs):
            return self.call('trigger_single_autozero', kwargs=kwargs)

        def init_trigger(self, **kwargs):
            return self.call('init_trigger', kwargs=kwargs)

        def beep(self, **kwargs):
            return self.call('beep', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

