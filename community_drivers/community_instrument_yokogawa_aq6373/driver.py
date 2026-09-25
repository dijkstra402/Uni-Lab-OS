from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentYokogawaAq6373(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/yokogawa/yokogawa7651.py', 'class_name': 'Yokogawa7651', 'import_roots': [], 'candidate_methods': ['id', 'source_enabled', 'enable_source', 'disable_source', 'apply_current', 'apply_voltage', 'ramp_to_current', 'ramp_to_voltage', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/yokogawa/yokogawa7651.py', 'class_name': 'Yokogawa7651', 'candidate_score': 0.88, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def id(self, **kwargs):
            return self.call('id', kwargs=kwargs)

        def source_enabled(self, **kwargs):
            return self.call('source_enabled', kwargs=kwargs)

        def enable_source(self, **kwargs):
            return self.call('enable_source', kwargs=kwargs)

        def disable_source(self, **kwargs):
            return self.call('disable_source', kwargs=kwargs)

        def apply_current(self, **kwargs):
            return self.call('apply_current', kwargs=kwargs)

        def apply_voltage(self, **kwargs):
            return self.call('apply_voltage', kwargs=kwargs)

        def ramp_to_current(self, **kwargs):
            return self.call('ramp_to_current', kwargs=kwargs)

        def ramp_to_voltage(self, **kwargs):
            return self.call('ramp_to_voltage', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

