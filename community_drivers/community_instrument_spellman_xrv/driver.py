from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentSpellmanXrv(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/spellmanhv/spellmanXRV.py', 'class_name': 'StatusCode', 'import_roots': [], 'candidate_methods': ['write', 'wait_for', 'read', 'check_set_errors', 'set_scaling', 'reset_hv_on_timer', 'reset_errors'], 'metadata': {'source_file': 'pymeasure/instruments/spellmanhv/spellmanXRV.py', 'class_name': 'StatusCode', 'candidate_score': 0.957, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def wait_for(self, **kwargs):
            return self.call('wait_for', kwargs=kwargs)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def check_set_errors(self, **kwargs):
            return self.call('check_set_errors', kwargs=kwargs)

        def set_scaling(self, **kwargs):
            return self.call('set_scaling', kwargs=kwargs)

        def reset_hv_on_timer(self, **kwargs):
            return self.call('reset_hv_on_timer', kwargs=kwargs)

        def reset_errors(self, **kwargs):
            return self.call('reset_errors', kwargs=kwargs)

