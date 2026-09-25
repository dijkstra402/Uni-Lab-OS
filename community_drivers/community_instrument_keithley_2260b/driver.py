from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley2260b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithley2260B.py', 'class_name': 'Keithley2260B', 'import_roots': [], 'candidate_methods': ['error', 'enabled', 'enabled', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithley2260B.py', 'class_name': 'Keithley2260B', 'candidate_score': 0.963, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def error(self, **kwargs):
            return self.call('error', kwargs=kwargs)

        def enabled(self, **kwargs):
            return self.call('enabled', kwargs=kwargs)

        def enabled(self, **kwargs):
            return self.call('enabled', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

