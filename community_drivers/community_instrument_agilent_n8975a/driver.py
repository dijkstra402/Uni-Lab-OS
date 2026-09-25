from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilentN8975a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilentN8975A.py', 'class_name': 'AgilentN8975AFrequency', 'import_roots': [], 'candidate_methods': ['abort', 'calibrate', 'initiate', 'single', 'gain', 'noise_figure'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilentN8975A.py', 'class_name': 'AgilentN8975AFrequency', 'candidate_score': 0.963, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def abort(self, **kwargs):
            return self.call('abort', kwargs=kwargs)

        def calibrate(self, **kwargs):
            return self.call('calibrate', kwargs=kwargs)

        def initiate(self, **kwargs):
            return self.call('initiate', kwargs=kwargs)

        def single(self, **kwargs):
            return self.call('single', kwargs=kwargs)

        def gain(self, **kwargs):
            return self.call('gain', kwargs=kwargs)

        def noise_figure(self, **kwargs):
            return self.call('noise_figure', kwargs=kwargs)

