from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentWatersEmpowerHplc(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/rohdeschwarz/hmp.py', 'class_name': 'HMP4040', 'import_roots': [], 'candidate_methods': ['beep', 'voltage_to_min', 'voltage_to_max', 'step_voltage_up', 'step_voltage_down', 'current_to_min', 'current_to_max', 'step_current_up', 'step_current_down', 'set_channel_state', 'clear_sequence', 'load_sequence', 'save_sequence', 'start_sequence', 'stop_sequence', 'transfer_sequence'], 'metadata': {'source_file': 'pymeasure/instruments/rohdeschwarz/hmp.py', 'class_name': 'HMP4040', 'candidate_score': 0.571, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def beep(self, **kwargs):
            return self.call('beep', kwargs=kwargs)

        def voltage_to_min(self, **kwargs):
            return self.call('voltage_to_min', kwargs=kwargs)

        def voltage_to_max(self, **kwargs):
            return self.call('voltage_to_max', kwargs=kwargs)

        def step_voltage_up(self, **kwargs):
            return self.call('step_voltage_up', kwargs=kwargs)

        def step_voltage_down(self, **kwargs):
            return self.call('step_voltage_down', kwargs=kwargs)

        def current_to_min(self, **kwargs):
            return self.call('current_to_min', kwargs=kwargs)

        def current_to_max(self, **kwargs):
            return self.call('current_to_max', kwargs=kwargs)

        def step_current_up(self, **kwargs):
            return self.call('step_current_up', kwargs=kwargs)

        def step_current_down(self, **kwargs):
            return self.call('step_current_down', kwargs=kwargs)

        def set_channel_state(self, **kwargs):
            return self.call('set_channel_state', kwargs=kwargs)

        def clear_sequence(self, **kwargs):
            return self.call('clear_sequence', kwargs=kwargs)

        def load_sequence(self, **kwargs):
            return self.call('load_sequence', kwargs=kwargs)

        def save_sequence(self, **kwargs):
            return self.call('save_sequence', kwargs=kwargs)

        def start_sequence(self, **kwargs):
            return self.call('start_sequence', kwargs=kwargs)

        def stop_sequence(self, **kwargs):
            return self.call('stop_sequence', kwargs=kwargs)

        def transfer_sequence(self, **kwargs):
            return self.call('transfer_sequence', kwargs=kwargs)

