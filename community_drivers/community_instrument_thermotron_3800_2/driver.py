from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThermotron38002(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/thermotron/thermotron3800.py', 'class_name': 'Thermotron3800', 'import_roots': [], 'candidate_methods': ['write', 'run', 'stop', 'initalize_oven'], 'metadata': {'source_file': 'pymeasure/instruments/thermotron/thermotron3800.py', 'class_name': 'Thermotron3800', 'candidate_score': 0.903, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def run(self, **kwargs):
            return self.call('run', kwargs=kwargs)

        def stop(self, **kwargs):
            return self.call('stop', kwargs=kwargs)

        def initalize_oven(self, **kwargs):
            return self.call('initalize_oven', kwargs=kwargs)

