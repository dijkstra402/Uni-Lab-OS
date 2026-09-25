from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHewlettPackard11713a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/hp/hp11713a.py', 'class_name': 'HP11713A', 'import_roots': [], 'candidate_methods': ['attenuation_x', 'attenuation_y', 'deactivate_all'], 'metadata': {'source_file': 'pymeasure/instruments/hp/hp11713a.py', 'class_name': 'HP11713A', 'candidate_score': 0.857, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def attenuation_x(self, **kwargs):
            return self.call('attenuation_x', kwargs=kwargs)

        def attenuation_y(self, **kwargs):
            return self.call('attenuation_y', kwargs=kwargs)

        def deactivate_all(self, **kwargs):
            return self.call('deactivate_all', kwargs=kwargs)

