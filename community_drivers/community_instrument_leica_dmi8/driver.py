from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLeicaDmi8(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/zplab__rpc-scope', 'source_file': 'scope/device/leica/stage.py', 'class_name': 'Stage', 'import_roots': [], 'candidate_methods': ['set_position', 'set_x', 'set_y', 'set_z', 'z_from_offset', 'get_position', 'get_x', 'get_y', 'get_z', 'set_x_low_soft_limit', 'set_x_high_soft_limit', 'set_y_low_soft_limit', 'set_y_high_soft_limit', 'set_z_low_soft_limit', 'set_z_high_soft_limit', 'get_x_low_soft_limit', 'get_x_high_soft_limit', 'get_y_low_soft_limit', 'get_y_high_soft_limit', 'get_z_low_soft_limit', 'get_z_high_soft_limit', 'reset_x_high_soft_limit', 'reset_y_high_soft_limit', 'reset_z_high_soft_limit', 'stop_x', 'stop_y', 'stop_z', 'set_x_speed', 'set_y_speed', 'set_z_speed', 'get_x_speed', 'get_y_speed', 'get_z_speed', 'move_along_x', 'move_along_y', 'move_along_z', 'get_x_min_speed', 'get_y_min_speed', 'get_z_min_speed', 'get_x_max_speed', 'get_y_max_speed', 'get_z_max_speed', 'get_x_speed_range', 'get_y_speed_range', 'get_z_speed_range', 'reinit', 'reinit_x', 'reinit_y', 'reinit_z', 'set_xy_fine_control', 'set_z_fine_control', 'get_xy_fine_control', 'get_z_fine_control', 'get_z_ramp_range', 'get_z_ramp', 'set_z_ramp', 'calculate_z_movement_time', 'calculate_required_z_speed', 'calculate_z_movement_position', 'push_state', 'pop_state', 'send_message', 'wait', 'has_pending', 'set_async_', 'get_async_', 'in_state'], 'action_targets': {}, 'metadata': {'repo': 'zplab/rpc-scope', 'repo_url': 'https://github.com/zplab/rpc-scope', 'brand': 'Leica', 'model': 'DMi8', 'device_type_cn': '倒置显微镜', 'device_type_en': 'Inverted Microscope', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 518, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def set_position(self, **kwargs):
        return self.call('set_position', kwargs=kwargs)

    def set_x(self, **kwargs):
        return self.call('set_x', kwargs=kwargs)

    def set_y(self, **kwargs):
        return self.call('set_y', kwargs=kwargs)

    def set_z(self, **kwargs):
        return self.call('set_z', kwargs=kwargs)

    def z_from_offset(self, **kwargs):
        return self.call('z_from_offset', kwargs=kwargs)

    def get_position(self, **kwargs):
        return self.call('get_position', kwargs=kwargs)

    def get_x(self, **kwargs):
        return self.call('get_x', kwargs=kwargs)

    def get_y(self, **kwargs):
        return self.call('get_y', kwargs=kwargs)

    def get_z(self, **kwargs):
        return self.call('get_z', kwargs=kwargs)

    def set_x_low_soft_limit(self, **kwargs):
        return self.call('set_x_low_soft_limit', kwargs=kwargs)

    def set_x_high_soft_limit(self, **kwargs):
        return self.call('set_x_high_soft_limit', kwargs=kwargs)

    def set_y_low_soft_limit(self, **kwargs):
        return self.call('set_y_low_soft_limit', kwargs=kwargs)

    def set_y_high_soft_limit(self, **kwargs):
        return self.call('set_y_high_soft_limit', kwargs=kwargs)

    def set_z_low_soft_limit(self, **kwargs):
        return self.call('set_z_low_soft_limit', kwargs=kwargs)

    def set_z_high_soft_limit(self, **kwargs):
        return self.call('set_z_high_soft_limit', kwargs=kwargs)

    def get_x_low_soft_limit(self, **kwargs):
        return self.call('get_x_low_soft_limit', kwargs=kwargs)

    def get_x_high_soft_limit(self, **kwargs):
        return self.call('get_x_high_soft_limit', kwargs=kwargs)

    def get_y_low_soft_limit(self, **kwargs):
        return self.call('get_y_low_soft_limit', kwargs=kwargs)

    def get_y_high_soft_limit(self, **kwargs):
        return self.call('get_y_high_soft_limit', kwargs=kwargs)

    def get_z_low_soft_limit(self, **kwargs):
        return self.call('get_z_low_soft_limit', kwargs=kwargs)

    def get_z_high_soft_limit(self, **kwargs):
        return self.call('get_z_high_soft_limit', kwargs=kwargs)

    def reset_x_high_soft_limit(self, **kwargs):
        return self.call('reset_x_high_soft_limit', kwargs=kwargs)

    def reset_y_high_soft_limit(self, **kwargs):
        return self.call('reset_y_high_soft_limit', kwargs=kwargs)

    def reset_z_high_soft_limit(self, **kwargs):
        return self.call('reset_z_high_soft_limit', kwargs=kwargs)

    def stop_x(self, **kwargs):
        return self.call('stop_x', kwargs=kwargs)

    def stop_y(self, **kwargs):
        return self.call('stop_y', kwargs=kwargs)

    def stop_z(self, **kwargs):
        return self.call('stop_z', kwargs=kwargs)

    def set_x_speed(self, **kwargs):
        return self.call('set_x_speed', kwargs=kwargs)

    def set_y_speed(self, **kwargs):
        return self.call('set_y_speed', kwargs=kwargs)

    def set_z_speed(self, **kwargs):
        return self.call('set_z_speed', kwargs=kwargs)

    def get_x_speed(self, **kwargs):
        return self.call('get_x_speed', kwargs=kwargs)

    def get_y_speed(self, **kwargs):
        return self.call('get_y_speed', kwargs=kwargs)

    def get_z_speed(self, **kwargs):
        return self.call('get_z_speed', kwargs=kwargs)

    def move_along_x(self, **kwargs):
        return self.call('move_along_x', kwargs=kwargs)

    def move_along_y(self, **kwargs):
        return self.call('move_along_y', kwargs=kwargs)

    def move_along_z(self, **kwargs):
        return self.call('move_along_z', kwargs=kwargs)

    def get_x_min_speed(self, **kwargs):
        return self.call('get_x_min_speed', kwargs=kwargs)

    def get_y_min_speed(self, **kwargs):
        return self.call('get_y_min_speed', kwargs=kwargs)

    def get_z_min_speed(self, **kwargs):
        return self.call('get_z_min_speed', kwargs=kwargs)

    def get_x_max_speed(self, **kwargs):
        return self.call('get_x_max_speed', kwargs=kwargs)

    def get_y_max_speed(self, **kwargs):
        return self.call('get_y_max_speed', kwargs=kwargs)

    def get_z_max_speed(self, **kwargs):
        return self.call('get_z_max_speed', kwargs=kwargs)

    def get_x_speed_range(self, **kwargs):
        return self.call('get_x_speed_range', kwargs=kwargs)

    def get_y_speed_range(self, **kwargs):
        return self.call('get_y_speed_range', kwargs=kwargs)

    def get_z_speed_range(self, **kwargs):
        return self.call('get_z_speed_range', kwargs=kwargs)

    def reinit(self, **kwargs):
        return self.call('reinit', kwargs=kwargs)

    def reinit_x(self, **kwargs):
        return self.call('reinit_x', kwargs=kwargs)

    def reinit_y(self, **kwargs):
        return self.call('reinit_y', kwargs=kwargs)

    def reinit_z(self, **kwargs):
        return self.call('reinit_z', kwargs=kwargs)

    def set_xy_fine_control(self, **kwargs):
        return self.call('set_xy_fine_control', kwargs=kwargs)

    def set_z_fine_control(self, **kwargs):
        return self.call('set_z_fine_control', kwargs=kwargs)

    def get_xy_fine_control(self, **kwargs):
        return self.call('get_xy_fine_control', kwargs=kwargs)

    def get_z_fine_control(self, **kwargs):
        return self.call('get_z_fine_control', kwargs=kwargs)

    def get_z_ramp_range(self, **kwargs):
        return self.call('get_z_ramp_range', kwargs=kwargs)

    def get_z_ramp(self, **kwargs):
        return self.call('get_z_ramp', kwargs=kwargs)

    def set_z_ramp(self, **kwargs):
        return self.call('set_z_ramp', kwargs=kwargs)

    def calculate_z_movement_time(self, **kwargs):
        return self.call('calculate_z_movement_time', kwargs=kwargs)

    def calculate_required_z_speed(self, **kwargs):
        return self.call('calculate_required_z_speed', kwargs=kwargs)

    def calculate_z_movement_position(self, **kwargs):
        return self.call('calculate_z_movement_position', kwargs=kwargs)

    def push_state(self, **kwargs):
        return self.call('push_state', kwargs=kwargs)

    def pop_state(self, **kwargs):
        return self.call('pop_state', kwargs=kwargs)

    def send_message(self, **kwargs):
        return self.call('send_message', kwargs=kwargs)

    def wait(self, **kwargs):
        return self.call('wait', kwargs=kwargs)

    def has_pending(self, **kwargs):
        return self.call('has_pending', kwargs=kwargs)

    def set_async(self, **kwargs):
        return self.call('set_async_', kwargs=kwargs)

    def get_async(self, **kwargs):
        return self.call('get_async_', kwargs=kwargs)

    def in_state(self, **kwargs):
        return self.call('in_state', kwargs=kwargs)

