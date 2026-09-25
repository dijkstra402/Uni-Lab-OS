from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLakeShore425(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/lakeshore/lakeshore425.py', 'class_name': 'LakeShore425', 'import_roots': [], 'candidate_methods': ['auto_range', 'dc_mode', 'ac_mode', 'mode', 'mode', 'zero_probe', 'measure'], 'metadata': {'source_file': 'pymeasure/instruments/lakeshore/lakeshore425.py', 'class_name': 'LakeShore425', 'candidate_score': 0.923, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def auto_range(self, **kwargs):
            return self.call('auto_range', kwargs=kwargs)

        def dc_mode(self, **kwargs):
            return self.call('dc_mode', kwargs=kwargs)

        def ac_mode(self, **kwargs):
            return self.call('ac_mode', kwargs=kwargs)

        def mode(self, **kwargs):
            return self.call('mode', kwargs=kwargs)

        def mode(self, **kwargs):
            return self.call('mode', kwargs=kwargs)

        def zero_probe(self, **kwargs):
            return self.call('zero_probe', kwargs=kwargs)

        def measure(self, **kwargs):
            return self.call('measure', kwargs=kwargs)

