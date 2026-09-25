from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOxfordInstrumentsIps12010(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/oxfordinstruments/ips120_10.py', 'class_name': 'IPS120_10', 'import_roots': [], 'candidate_methods': ['switch_heater_enabled', 'switch_heater_enabled', 'field', 'enable_control', 'disable_control', 'enable_persistent_mode', 'disable_persistent_mode', 'wait_for_idle', 'set_field', 'train_magnet'], 'metadata': {'source_file': 'pymeasure/instruments/oxfordinstruments/ips120_10.py', 'class_name': 'IPS120_10', 'candidate_score': 0.8, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def switch_heater_enabled(self, **kwargs):
            return self.call('switch_heater_enabled', kwargs=kwargs)

        def switch_heater_enabled(self, **kwargs):
            return self.call('switch_heater_enabled', kwargs=kwargs)

        def field(self, **kwargs):
            return self.call('field', kwargs=kwargs)

        def enable_control(self, **kwargs):
            return self.call('enable_control', kwargs=kwargs)

        def disable_control(self, **kwargs):
            return self.call('disable_control', kwargs=kwargs)

        def enable_persistent_mode(self, **kwargs):
            return self.call('enable_persistent_mode', kwargs=kwargs)

        def disable_persistent_mode(self, **kwargs):
            return self.call('disable_persistent_mode', kwargs=kwargs)

        def wait_for_idle(self, **kwargs):
            return self.call('wait_for_idle', kwargs=kwargs)

        def set_field(self, **kwargs):
            return self.call('set_field', kwargs=kwargs)

        def train_magnet(self, **kwargs):
            return self.call('train_magnet', kwargs=kwargs)

