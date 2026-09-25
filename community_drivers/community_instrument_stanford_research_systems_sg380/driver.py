from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentStanfordResearchSystemsSg380(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/srs/sg380.py', 'class_name': 'SG380', 'import_roots': [], 'candidate_methods': ['has_doubler', 'has_IQ', 'frequency', 'frequency', 'mod_type', 'mod_type', 'mod_function', 'mod_func'], 'metadata': {'source_file': 'pymeasure/instruments/srs/sg380.py', 'class_name': 'SG380', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def has_doubler(self, **kwargs):
            return self.call('has_doubler', kwargs=kwargs)

        def has_IQ(self, **kwargs):
            return self.call('has_IQ', kwargs=kwargs)

        def frequency(self, **kwargs):
            return self.call('frequency', kwargs=kwargs)

        def frequency(self, **kwargs):
            return self.call('frequency', kwargs=kwargs)

        def mod_type(self, **kwargs):
            return self.call('mod_type', kwargs=kwargs)

        def mod_type(self, **kwargs):
            return self.call('mod_type', kwargs=kwargs)

        def mod_function(self, **kwargs):
            return self.call('mod_function', kwargs=kwargs)

        def mod_func(self, **kwargs):
            return self.call('mod_func', kwargs=kwargs)

