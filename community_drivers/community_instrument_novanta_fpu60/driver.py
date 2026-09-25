from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentNovantaFpu60(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/novanta/fpu60.py', 'class_name': 'Fpu60', 'import_roots': [], 'candidate_methods': ['get_operation_times', 'disable_emission', 'check_set_errors'], 'metadata': {'source_file': 'pymeasure/instruments/novanta/fpu60.py', 'class_name': 'Fpu60', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def get_operation_times(self, **kwargs):
            return self.call('get_operation_times', kwargs=kwargs)

        def disable_emission(self, **kwargs):
            return self.call('disable_emission', kwargs=kwargs)

        def check_set_errors(self, **kwargs):
            return self.call('check_set_errors', kwargs=kwargs)

