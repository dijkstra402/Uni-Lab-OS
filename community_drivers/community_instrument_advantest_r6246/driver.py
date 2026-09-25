from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAdvantestR6246(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/advantest/advantestR624X.py', 'class_name': 'SampleHold', 'import_roots': [], 'candidate_methods': ['write', 'check_errors', 'enable_source', 'standby', 'clear_status_register', 'trigger', 'stop', 'set_digital_output', 'append_sequence_command', 'init_sequence', 'start_sequence', 'end_sequence', 'sequence_wait', 'start_sequence_program', 'store_sequence_command', 'interrupt_sequence_command', 'sequence_program_listing', 'trigger_output_signal', 'set_output_format', 'set_lo_common_connection_relay'], 'metadata': {'source_file': 'pymeasure/instruments/advantest/advantestR624X.py', 'class_name': 'SampleHold', 'candidate_score': 0.897, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def check_errors(self, **kwargs):
            return self.call('check_errors', kwargs=kwargs)

        def enable_source(self, **kwargs):
            return self.call('enable_source', kwargs=kwargs)

        def standby(self, **kwargs):
            return self.call('standby', kwargs=kwargs)

        def clear_status_register(self, **kwargs):
            return self.call('clear_status_register', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def stop(self, **kwargs):
            return self.call('stop', kwargs=kwargs)

        def set_digital_output(self, **kwargs):
            return self.call('set_digital_output', kwargs=kwargs)

        def append_sequence_command(self, **kwargs):
            return self.call('append_sequence_command', kwargs=kwargs)

        def init_sequence(self, **kwargs):
            return self.call('init_sequence', kwargs=kwargs)

        def start_sequence(self, **kwargs):
            return self.call('start_sequence', kwargs=kwargs)

        def end_sequence(self, **kwargs):
            return self.call('end_sequence', kwargs=kwargs)

        def sequence_wait(self, **kwargs):
            return self.call('sequence_wait', kwargs=kwargs)

        def start_sequence_program(self, **kwargs):
            return self.call('start_sequence_program', kwargs=kwargs)

        def store_sequence_command(self, **kwargs):
            return self.call('store_sequence_command', kwargs=kwargs)

        def interrupt_sequence_command(self, **kwargs):
            return self.call('interrupt_sequence_command', kwargs=kwargs)

        def sequence_program_listing(self, **kwargs):
            return self.call('sequence_program_listing', kwargs=kwargs)

        def trigger_output_signal(self, **kwargs):
            return self.call('trigger_output_signal', kwargs=kwargs)

        def set_output_format(self, **kwargs):
            return self.call('set_output_format', kwargs=kwargs)

        def set_lo_common_connection_relay(self, **kwargs):
            return self.call('set_lo_common_connection_relay', kwargs=kwargs)

