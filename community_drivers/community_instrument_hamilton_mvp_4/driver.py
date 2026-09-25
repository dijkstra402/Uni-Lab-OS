from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHamiltonMvp4(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/fuzikt__psd_mvp_control', 'source_file': 'hw_classes/psd_pump.py', 'class_name': 'PSDpump', 'import_roots': [], 'candidate_methods': ['load_pump_parameters', 'run_command', 'steps_to_volume', 'volume_to_steps', 'initialize', 'set_step_position', 'reset_syringe_counter_position', 'move_down_steps', 'move_up_steps', 'set_return_steps', 'set_backoff_steps', 'valve_input', 'valve_output', 'valve_bypass', 'valve_extra', 'insert_loop_start', 'insert_loop_end', 'delay', 'halt', 'setHiRes', 'setLoRes', 'set_acceleration', 'set_start_velocity', 'set_max_velocity', 'set_syringe_speed', 'set_stop_velocity', 'terminate', 'empty_syringe', 'fill_syringe', 'move_syringe_up', 'move_syringe_down', 'get_command_buffer_status', 'get_firmware_version', 'get_status', 'get_absolute_syringe_position', 'get_start_velocity', 'get_max_velocity', 'get_stop_velocity', 'get_actual_syringe_position', 'get_nr_return_steps', 'get_aux1_status', 'get_aux2_status', 'get_back_off_steps'], 'action_targets': {}, 'metadata': {'repo': 'fuzikt/psd_mvp_control', 'repo_url': 'https://github.com/fuzikt/psd_mvp_control', 'brand': 'Hamilton', 'model': 'MVP/4', 'device_type_cn': '多位阀', 'device_type_en': 'Multi-Position Valve', 'source_framework': '泵阀/液体处理', 'tag_id': '4382', 'tag_name': '多通阀', 'tag_name_en': 'Multi-Port Valve', 'candidate_score': 402, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def load_pump_parameters(self, **kwargs):
        return self.call('load_pump_parameters', kwargs=kwargs)

    def run_command(self, **kwargs):
        return self.call('run_command', kwargs=kwargs)

    def steps_to_volume(self, **kwargs):
        return self.call('steps_to_volume', kwargs=kwargs)

    def volume_to_steps(self, **kwargs):
        return self.call('volume_to_steps', kwargs=kwargs)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def set_step_position(self, **kwargs):
        return self.call('set_step_position', kwargs=kwargs)

    def reset_syringe_counter_position(self, **kwargs):
        return self.call('reset_syringe_counter_position', kwargs=kwargs)

    def move_down_steps(self, **kwargs):
        return self.call('move_down_steps', kwargs=kwargs)

    def move_up_steps(self, **kwargs):
        return self.call('move_up_steps', kwargs=kwargs)

    def set_return_steps(self, **kwargs):
        return self.call('set_return_steps', kwargs=kwargs)

    def set_backoff_steps(self, **kwargs):
        return self.call('set_backoff_steps', kwargs=kwargs)

    def valve_input(self, **kwargs):
        return self.call('valve_input', kwargs=kwargs)

    def valve_output(self, **kwargs):
        return self.call('valve_output', kwargs=kwargs)

    def valve_bypass(self, **kwargs):
        return self.call('valve_bypass', kwargs=kwargs)

    def valve_extra(self, **kwargs):
        return self.call('valve_extra', kwargs=kwargs)

    def insert_loop_start(self, **kwargs):
        return self.call('insert_loop_start', kwargs=kwargs)

    def insert_loop_end(self, **kwargs):
        return self.call('insert_loop_end', kwargs=kwargs)

    def delay(self, **kwargs):
        return self.call('delay', kwargs=kwargs)

    def halt(self, **kwargs):
        return self.call('halt', kwargs=kwargs)

    def setHiRes(self, **kwargs):
        return self.call('setHiRes', kwargs=kwargs)

    def setLoRes(self, **kwargs):
        return self.call('setLoRes', kwargs=kwargs)

    def set_acceleration(self, **kwargs):
        return self.call('set_acceleration', kwargs=kwargs)

    def set_start_velocity(self, **kwargs):
        return self.call('set_start_velocity', kwargs=kwargs)

    def set_max_velocity(self, **kwargs):
        return self.call('set_max_velocity', kwargs=kwargs)

    def set_syringe_speed(self, **kwargs):
        return self.call('set_syringe_speed', kwargs=kwargs)

    def set_stop_velocity(self, **kwargs):
        return self.call('set_stop_velocity', kwargs=kwargs)

    def terminate(self, **kwargs):
        return self.call('terminate', kwargs=kwargs)

    def empty_syringe(self, **kwargs):
        return self.call('empty_syringe', kwargs=kwargs)

    def fill_syringe(self, **kwargs):
        return self.call('fill_syringe', kwargs=kwargs)

    def move_syringe_up(self, **kwargs):
        return self.call('move_syringe_up', kwargs=kwargs)

    def move_syringe_down(self, **kwargs):
        return self.call('move_syringe_down', kwargs=kwargs)

    def get_command_buffer_status(self, **kwargs):
        return self.call('get_command_buffer_status', kwargs=kwargs)

    def get_firmware_version(self, **kwargs):
        return self.call('get_firmware_version', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def get_absolute_syringe_position(self, **kwargs):
        return self.call('get_absolute_syringe_position', kwargs=kwargs)

    def get_start_velocity(self, **kwargs):
        return self.call('get_start_velocity', kwargs=kwargs)

    def get_max_velocity(self, **kwargs):
        return self.call('get_max_velocity', kwargs=kwargs)

    def get_stop_velocity(self, **kwargs):
        return self.call('get_stop_velocity', kwargs=kwargs)

    def get_actual_syringe_position(self, **kwargs):
        return self.call('get_actual_syringe_position', kwargs=kwargs)

    def get_nr_return_steps(self, **kwargs):
        return self.call('get_nr_return_steps', kwargs=kwargs)

    def get_aux1_status(self, **kwargs):
        return self.call('get_aux1_status', kwargs=kwargs)

    def get_aux2_status(self, **kwargs):
        return self.call('get_aux2_status', kwargs=kwargs)

    def get_back_off_steps(self, **kwargs):
        return self.call('get_back_off_steps', kwargs=kwargs)

