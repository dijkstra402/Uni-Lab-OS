from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTektronixAfg3152c(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/tektronix/afg3152c.py', 'class_name': 'AFG3152C', 'import_roots': [], 'candidate_methods': ['insert_id', 'enable', 'disable', 'beep', 'opc'], 'metadata': {'source_file': 'pymeasure/instruments/tektronix/afg3152c.py', 'class_name': 'AFG3152C', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def insert_id(self, **kwargs):
            return self.call('insert_id', kwargs=kwargs)

        def enable(self, **kwargs):
            return self.call('enable', kwargs=kwargs)

        def disable(self, **kwargs):
            return self.call('disable', kwargs=kwargs)

        def beep(self, **kwargs):
            return self.call('beep', kwargs=kwargs)

        def opc(self, **kwargs):
            return self.call('opc', kwargs=kwargs)

