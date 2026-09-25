from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTopticaIbeamSmart2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/toptica/ibeamsmart.py', 'class_name': 'IBeamSmart', 'import_roots': [], 'candidate_methods': ['read', 'check_set_errors', 'enable_continous', 'enable_pulsing', 'disable', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/toptica/ibeamsmart.py', 'class_name': 'IBeamSmart', 'candidate_score': 0.8, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def check_set_errors(self, **kwargs):
            return self.call('check_set_errors', kwargs=kwargs)

        def enable_continous(self, **kwargs):
            return self.call('enable_continous', kwargs=kwargs)

        def enable_pulsing(self, **kwargs):
            return self.call('enable_pulsing', kwargs=kwargs)

        def disable(self, **kwargs):
            return self.call('disable', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

