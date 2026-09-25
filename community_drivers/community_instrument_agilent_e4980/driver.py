from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilentE4980(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilentE4980.py', 'class_name': 'AgilentE4980', 'import_roots': [], 'candidate_methods': ['freq_sweep', 'aperture'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilentE4980.py', 'class_name': 'AgilentE4980', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def freq_sweep(self, **kwargs):
            return self.call('freq_sweep', kwargs=kwargs)

        def aperture(self, **kwargs):
            return self.call('aperture', kwargs=kwargs)

