from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilent33500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent33500.py', 'class_name': 'Agilent33500', 'import_roots': [], 'candidate_methods': ['data_volatile_clear', 'data_arb', 'beep', 'data_volatile_clear', 'phase_sync', 'data_arb', 'clear_display', 'trigger', 'wait_for_trigger'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilent33500.py', 'class_name': 'Agilent33500', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def data_volatile_clear(self, **kwargs):
            return self.call('data_volatile_clear', kwargs=kwargs)

        def data_arb(self, **kwargs):
            return self.call('data_arb', kwargs=kwargs)

        def beep(self, **kwargs):
            return self.call('beep', kwargs=kwargs)

        def data_volatile_clear(self, **kwargs):
            return self.call('data_volatile_clear', kwargs=kwargs)

        def phase_sync(self, **kwargs):
            return self.call('phase_sync', kwargs=kwargs)

        def data_arb(self, **kwargs):
            return self.call('data_arb', kwargs=kwargs)

        def clear_display(self, **kwargs):
            return self.call('clear_display', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def wait_for_trigger(self, **kwargs):
            return self.call('wait_for_trigger', kwargs=kwargs)

