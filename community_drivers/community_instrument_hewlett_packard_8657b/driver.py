from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHewlettPackard8657b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/hp/hp8657b.py', 'class_name': 'HP8657B', 'import_roots': [], 'candidate_methods': ['check_errors', 'clear', 'reset', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/hp/hp8657b.py', 'class_name': 'HP8657B', 'candidate_score': 0.833, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def check_errors(self, **kwargs):
            return self.call('check_errors', kwargs=kwargs)

        def clear(self, **kwargs):
            return self.call('clear', kwargs=kwargs)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

