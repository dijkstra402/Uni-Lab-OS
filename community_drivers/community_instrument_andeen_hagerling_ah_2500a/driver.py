from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAndeenHagerlingAh2500a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/andeenhagerling/ah2500a.py', 'class_name': 'AH2500A', 'import_roots': [], 'candidate_methods': ['trigger', 'triggered_caplossvolt'], 'metadata': {'source_file': 'pymeasure/instruments/andeenhagerling/ah2500a.py', 'class_name': 'AH2500A', 'candidate_score': 0.833, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def triggered_caplossvolt(self, **kwargs):
            return self.call('triggered_caplossvolt', kwargs=kwargs)

