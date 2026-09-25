from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilentE4408b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilentE4408B.py', 'class_name': 'AgilentE4408B', 'import_roots': [], 'candidate_methods': ['frequencies', 'trace', 'trace_df'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilentE4408B.py', 'class_name': 'AgilentE4408B', 'candidate_score': 0.963, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def frequencies(self, **kwargs):
            return self.call('frequencies', kwargs=kwargs)

        def trace(self, **kwargs):
            return self.call('trace', kwargs=kwargs)

        def trace_df(self, **kwargs):
            return self.call('trace_df', kwargs=kwargs)

