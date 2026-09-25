from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHewlettPackard8560a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/srs/sr860.py', 'class_name': 'SR860', 'import_roots': [], 'candidate_methods': ['sensitvity', 'filer_synchronous', 'snap', 'snap_all', 'screenshot'], 'metadata': {'source_file': 'pymeasure/instruments/srs/sr860.py', 'class_name': 'SR860', 'candidate_score': 0.6, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def sensitvity(self, **kwargs):
            return self.call('sensitvity', kwargs=kwargs)

        def filer_synchronous(self, **kwargs):
            return self.call('filer_synchronous', kwargs=kwargs)

        def snap(self, **kwargs):
            return self.call('snap', kwargs=kwargs)

        def snap_all(self, **kwargs):
            return self.call('snap_all', kwargs=kwargs)

        def screenshot(self, **kwargs):
            return self.call('screenshot', kwargs=kwargs)

