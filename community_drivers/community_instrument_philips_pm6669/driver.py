from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPhilipsPm6669(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/philips/PM6669.py', 'class_name': 'Functions', 'import_roots': [], 'candidate_methods': ['spoll', 'trigger', 'read_measurement', 'read', 'reset_to_defaults'], 'metadata': {'source_file': 'pymeasure/instruments/philips/PM6669.py', 'class_name': 'Functions', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def spoll(self, **kwargs):
            return self.call('spoll', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def read_measurement(self, **kwargs):
            return self.call('read_measurement', kwargs=kwargs)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def reset_to_defaults(self, **kwargs):
            return self.call('reset_to_defaults', kwargs=kwargs)

