from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeysightN7776c(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keysight/keysightN7776C.py', 'class_name': 'KeysightN7776C', 'import_roots': [], 'candidate_methods': ['output_power_mW', 'output_power_mW', 'output_power_dBm', 'output_power_dBm', 'valid_sweep_params', 'next_step', 'previous_step', 'get_wl_data', 'close'], 'metadata': {'source_file': 'pymeasure/instruments/keysight/keysightN7776C.py', 'class_name': 'KeysightN7776C', 'candidate_score': 0.966, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def output_power_mW(self, **kwargs):
            return self.call('output_power_mW', kwargs=kwargs)

        def output_power_mW(self, **kwargs):
            return self.call('output_power_mW', kwargs=kwargs)

        def output_power_dBm(self, **kwargs):
            return self.call('output_power_dBm', kwargs=kwargs)

        def output_power_dBm(self, **kwargs):
            return self.call('output_power_dBm', kwargs=kwargs)

        def valid_sweep_params(self, **kwargs):
            return self.call('valid_sweep_params', kwargs=kwargs)

        def next_step(self, **kwargs):
            return self.call('next_step', kwargs=kwargs)

        def previous_step(self, **kwargs):
            return self.call('previous_step', kwargs=kwargs)

        def get_wl_data(self, **kwargs):
            return self.call('get_wl_data', kwargs=kwargs)

        def close(self, **kwargs):
            return self.call('close', kwargs=kwargs)

