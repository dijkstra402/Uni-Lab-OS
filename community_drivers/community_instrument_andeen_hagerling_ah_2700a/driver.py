from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAndeenHagerlingAh2700a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/andeenhagerling/ah2700a.py', 'class_name': 'AH2700A', 'import_roots': [], 'candidate_methods': ['reset', 'trigger'], 'metadata': {'source_file': 'pymeasure/instruments/andeenhagerling/ah2700a.py', 'class_name': 'AH2700A', 'candidate_score': 0.833, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

