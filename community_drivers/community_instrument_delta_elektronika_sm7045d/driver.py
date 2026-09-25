from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentDeltaElektronikaSm7045d(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/deltaelektronika/sm7045d.py', 'class_name': 'SM7045D', 'import_roots': [], 'candidate_methods': ['enable', 'disable', 'ramp_to_current', 'ramp_to_zero', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/deltaelektronika/sm7045d.py', 'class_name': 'SM7045D', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def enable(self, **kwargs):
            return self.call('enable', kwargs=kwargs)

        def disable(self, **kwargs):
            return self.call('disable', kwargs=kwargs)

        def ramp_to_current(self, **kwargs):
            return self.call('ramp_to_current', kwargs=kwargs)

        def ramp_to_zero(self, **kwargs):
            return self.call('ramp_to_zero', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

