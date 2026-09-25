from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictPerformax4exstage(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/AlexShkarin__pyLabLib', 'source_file': 'pylablib/devices/Arcus/performax.py', 'class_name': 'Performax4EXStage', 'import_roots': [], 'candidate_methods': ['get_baudrate', 'set_baudrate', 'enable_absolute_mode', 'enable_limit_errors', 'limit_errors_enabled', 'is_enabled', 'enable_axis', 'get_position', 'set_position_reference', 'get_encoder', 'set_encoder_reference', 'move_to', 'move_by', 'jog', 'stop', 'home', 'get_global_speed', 'get_axis_speed', 'set_global_speed', 'set_axis_speed', 'get_current_axis_speed', 'get_status_n', 'get_status', 'is_moving', 'wait_move', 'check_limit_error', 'clear_limit_error', 'get_analog_input', 'get_digital_input', 'get_digital_input_register', 'get_digital_output', 'get_digital_output_register', 'set_digital_output', 'set_digital_output_register', 'open', 'close', 'is_opened', 'get_device_info', 'query', 'get_device_number', 'set_device_number', 'store_defaults', 'get_all_axes', 'remap_axes', 'get_settings', 'get_full_status', 'get_full_info', 'apply_settings', 'get_device_variable', 'set_device_variable'], 'action_targets': {}, 'metadata': {'repo': 'AlexShkarin/pyLabLib', 'repo_url': 'https://github.com/AlexShkarin/pyLabLib', 'source_url': 'https://github.com/AlexShkarin/pyLabLib/blob/main/pylablib/devices/Arcus/performax.py', 'confidence': 0.8, 'quality_score': 0.88, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_baudrate(self, **kwargs):
        return self.call('get_baudrate', kwargs=kwargs)

    def set_baudrate(self, **kwargs):
        return self.call('set_baudrate', kwargs=kwargs)

    def enable_absolute_mode(self, **kwargs):
        return self.call('enable_absolute_mode', kwargs=kwargs)

    def enable_limit_errors(self, **kwargs):
        return self.call('enable_limit_errors', kwargs=kwargs)

    def limit_errors_enabled(self, **kwargs):
        return self.call('limit_errors_enabled', kwargs=kwargs)

    def is_enabled(self, **kwargs):
        return self.call('is_enabled', kwargs=kwargs)

    def enable_axis(self, **kwargs):
        return self.call('enable_axis', kwargs=kwargs)

    def get_position(self, **kwargs):
        return self.call('get_position', kwargs=kwargs)

    def set_position_reference(self, **kwargs):
        return self.call('set_position_reference', kwargs=kwargs)

    def get_encoder(self, **kwargs):
        return self.call('get_encoder', kwargs=kwargs)

    def set_encoder_reference(self, **kwargs):
        return self.call('set_encoder_reference', kwargs=kwargs)

    def move_to(self, **kwargs):
        return self.call('move_to', kwargs=kwargs)

    def move_by(self, **kwargs):
        return self.call('move_by', kwargs=kwargs)

    def jog(self, **kwargs):
        return self.call('jog', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def home(self, **kwargs):
        return self.call('home', kwargs=kwargs)

    def get_global_speed(self, **kwargs):
        return self.call('get_global_speed', kwargs=kwargs)

    def get_axis_speed(self, **kwargs):
        return self.call('get_axis_speed', kwargs=kwargs)

    def set_global_speed(self, **kwargs):
        return self.call('set_global_speed', kwargs=kwargs)

    def set_axis_speed(self, **kwargs):
        return self.call('set_axis_speed', kwargs=kwargs)

    def get_current_axis_speed(self, **kwargs):
        return self.call('get_current_axis_speed', kwargs=kwargs)

    def get_status_n(self, **kwargs):
        return self.call('get_status_n', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def is_moving(self, **kwargs):
        return self.call('is_moving', kwargs=kwargs)

    def wait_move(self, **kwargs):
        return self.call('wait_move', kwargs=kwargs)

    def check_limit_error(self, **kwargs):
        return self.call('check_limit_error', kwargs=kwargs)

    def clear_limit_error(self, **kwargs):
        return self.call('clear_limit_error', kwargs=kwargs)

    def get_analog_input(self, **kwargs):
        return self.call('get_analog_input', kwargs=kwargs)

    def get_digital_input(self, **kwargs):
        return self.call('get_digital_input', kwargs=kwargs)

    def get_digital_input_register(self, **kwargs):
        return self.call('get_digital_input_register', kwargs=kwargs)

    def get_digital_output(self, **kwargs):
        return self.call('get_digital_output', kwargs=kwargs)

    def get_digital_output_register(self, **kwargs):
        return self.call('get_digital_output_register', kwargs=kwargs)

    def set_digital_output(self, **kwargs):
        return self.call('set_digital_output', kwargs=kwargs)

    def set_digital_output_register(self, **kwargs):
        return self.call('set_digital_output_register', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def is_opened(self, **kwargs):
        return self.call('is_opened', kwargs=kwargs)

    def get_device_info(self, **kwargs):
        return self.call('get_device_info', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def get_device_number(self, **kwargs):
        return self.call('get_device_number', kwargs=kwargs)

    def set_device_number(self, **kwargs):
        return self.call('set_device_number', kwargs=kwargs)

    def store_defaults(self, **kwargs):
        return self.call('store_defaults', kwargs=kwargs)

    def get_all_axes(self, **kwargs):
        return self.call('get_all_axes', kwargs=kwargs)

    def remap_axes(self, **kwargs):
        return self.call('remap_axes', kwargs=kwargs)

    def get_settings(self, **kwargs):
        return self.call('get_settings', kwargs=kwargs)

    def get_full_status(self, **kwargs):
        return self.call('get_full_status', kwargs=kwargs)

    def get_full_info(self, **kwargs):
        return self.call('get_full_info', kwargs=kwargs)

    def apply_settings(self, **kwargs):
        return self.call('apply_settings', kwargs=kwargs)

    def get_device_variable(self, **kwargs):
        return self.call('get_device_variable', kwargs=kwargs)

    def set_device_variable(self, **kwargs):
        return self.call('set_device_variable', kwargs=kwargs)

