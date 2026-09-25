from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTaInstrumentsSdt650TgaDsc(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/hp/hplegacyinstrument.py', 'class_name': 'HPLegacyInstrument', 'import_roots': [], 'candidate_methods': ['fields', 'write', 'values', 'status', 'GPIB_trigger', 'reset', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/hp/hplegacyinstrument.py', 'class_name': 'HPLegacyInstrument', 'candidate_score': 0.69, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def fields(self, **kwargs):
            return self.call('fields', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def values(self, **kwargs):
            return self.call('values', kwargs=kwargs)

        def status(self, **kwargs):
            return self.call('status', kwargs=kwargs)

        def GPIB_trigger(self, **kwargs):
            return self.call('GPIB_trigger', kwargs=kwargs)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

