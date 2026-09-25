from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeysight81160a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keysight/keysight81160A.py', 'class_name': 'Keysight81160A', 'import_roots': [], 'candidate_methods': ['waveform_volatile', 'waveform_volatile', 'save_waveform', 'delete_waveform', 'apply_dc', 'apply_noise', 'apply_pulse', 'apply_sin', 'apply_square', 'apply_user_waveform'], 'metadata': {'source_file': 'pymeasure/instruments/keysight/keysight81160A.py', 'class_name': 'Keysight81160A', 'candidate_score': 0.966, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def waveform_volatile(self, **kwargs):
            return self.call('waveform_volatile', kwargs=kwargs)

        def waveform_volatile(self, **kwargs):
            return self.call('waveform_volatile', kwargs=kwargs)

        def save_waveform(self, **kwargs):
            return self.call('save_waveform', kwargs=kwargs)

        def delete_waveform(self, **kwargs):
            return self.call('delete_waveform', kwargs=kwargs)

        def apply_dc(self, **kwargs):
            return self.call('apply_dc', kwargs=kwargs)

        def apply_noise(self, **kwargs):
            return self.call('apply_noise', kwargs=kwargs)

        def apply_pulse(self, **kwargs):
            return self.call('apply_pulse', kwargs=kwargs)

        def apply_sin(self, **kwargs):
            return self.call('apply_sin', kwargs=kwargs)

        def apply_square(self, **kwargs):
            return self.call('apply_square', kwargs=kwargs)

        def apply_user_waveform(self, **kwargs):
            return self.call('apply_user_waveform', kwargs=kwargs)

