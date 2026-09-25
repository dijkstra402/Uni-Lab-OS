from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAnritsuMg3692c(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/anritsu/anritsuMG3692C.py', 'class_name': 'AnritsuMG3692C', 'import_roots': [], 'candidate_methods': ['output', 'output', 'enable', 'disable', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/anritsu/anritsuMG3692C.py', 'class_name': 'AnritsuMG3692C', 'candidate_score': 0.966, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def output(self, **kwargs):
            return self.call('output', kwargs=kwargs)

        def output(self, **kwargs):
            return self.call('output', kwargs=kwargs)

        def enable(self, **kwargs):
            return self.call('enable', kwargs=kwargs)

        def disable(self, **kwargs):
            return self.call('disable', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

