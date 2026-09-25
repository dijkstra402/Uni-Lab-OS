from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilentB2983(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilentB298x.py', 'class_name': 'AgilentB2981', 'import_roots': [], 'candidate_methods': ['abort', 'arm', 'init', 'abort_acquisition', 'arm_acquisition', 'init_acquisition', 'abort_transient', 'arm_transient', 'init_transient'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilentB298x.py', 'class_name': 'AgilentB2981', 'candidate_score': 0.88, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def abort(self, **kwargs):
            return self.call('abort', kwargs=kwargs)

        def arm(self, **kwargs):
            return self.call('arm', kwargs=kwargs)

        def init(self, **kwargs):
            return self.call('init', kwargs=kwargs)

        def abort_acquisition(self, **kwargs):
            return self.call('abort_acquisition', kwargs=kwargs)

        def arm_acquisition(self, **kwargs):
            return self.call('arm_acquisition', kwargs=kwargs)

        def init_acquisition(self, **kwargs):
            return self.call('init_acquisition', kwargs=kwargs)

        def abort_transient(self, **kwargs):
            return self.call('abort_transient', kwargs=kwargs)

        def arm_transient(self, **kwargs):
            return self.call('arm_transient', kwargs=kwargs)

        def init_transient(self, **kwargs):
            return self.call('init_transient', kwargs=kwargs)

