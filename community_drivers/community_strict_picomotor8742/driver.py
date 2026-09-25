from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictPicomotor8742(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/AlexShkarin__pyLabLib', 'source_file': 'pylablib/devices/Newport/picomotor.py', 'class_name': 'Picomotor8742', 'import_roots': [], 'candidate_methods': ['query', 'get_id', 'get_device_info', 'reset', 'save_parameters', 'restore_parameters', 'scan_devices', 'get_addr_map', 'wait_for_scan', 'get_addr', 'set_addr', 'get_ethernet_parameters', 'setup_ethernet', 'autodetect_motors', 'get_motor_type', 'set_motor_type', 'move_to', 'move_by', 'get_position', 'set_position_reference', 'jog', 'is_moving', 'wait_move', 'stop', 'get_velocity_parameters', 'setup_velocity', 'open', 'close', 'is_opened', 'lock', 'unlock', 'locking', 'get_settings', 'get_full_status', 'get_full_info', 'apply_settings', 'get_device_variable', 'set_device_variable', 'get_all_axes', 'remap_axes'], 'action_targets': {}, 'metadata': {'repo': 'AlexShkarin/pyLabLib', 'repo_url': 'https://github.com/AlexShkarin/pyLabLib', 'source_url': 'https://github.com/AlexShkarin/pyLabLib/blob/main/pylablib/devices/Newport/picomotor.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def get_id(self, **kwargs):
        return self.call('get_id', kwargs=kwargs)

    def get_device_info(self, **kwargs):
        return self.call('get_device_info', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def save_parameters(self, **kwargs):
        return self.call('save_parameters', kwargs=kwargs)

    def restore_parameters(self, **kwargs):
        return self.call('restore_parameters', kwargs=kwargs)

    def scan_devices(self, **kwargs):
        return self.call('scan_devices', kwargs=kwargs)

    def get_addr_map(self, **kwargs):
        return self.call('get_addr_map', kwargs=kwargs)

    def wait_for_scan(self, **kwargs):
        return self.call('wait_for_scan', kwargs=kwargs)

    def get_addr(self, **kwargs):
        return self.call('get_addr', kwargs=kwargs)

    def set_addr(self, **kwargs):
        return self.call('set_addr', kwargs=kwargs)

    def get_ethernet_parameters(self, **kwargs):
        return self.call('get_ethernet_parameters', kwargs=kwargs)

    def setup_ethernet(self, **kwargs):
        return self.call('setup_ethernet', kwargs=kwargs)

    def autodetect_motors(self, **kwargs):
        return self.call('autodetect_motors', kwargs=kwargs)

    def get_motor_type(self, **kwargs):
        return self.call('get_motor_type', kwargs=kwargs)

    def set_motor_type(self, **kwargs):
        return self.call('set_motor_type', kwargs=kwargs)

    def move_to(self, **kwargs):
        return self.call('move_to', kwargs=kwargs)

    def move_by(self, **kwargs):
        return self.call('move_by', kwargs=kwargs)

    def get_position(self, **kwargs):
        return self.call('get_position', kwargs=kwargs)

    def set_position_reference(self, **kwargs):
        return self.call('set_position_reference', kwargs=kwargs)

    def jog(self, **kwargs):
        return self.call('jog', kwargs=kwargs)

    def is_moving(self, **kwargs):
        return self.call('is_moving', kwargs=kwargs)

    def wait_move(self, **kwargs):
        return self.call('wait_move', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def get_velocity_parameters(self, **kwargs):
        return self.call('get_velocity_parameters', kwargs=kwargs)

    def setup_velocity(self, **kwargs):
        return self.call('setup_velocity', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def is_opened(self, **kwargs):
        return self.call('is_opened', kwargs=kwargs)

    def lock(self, **kwargs):
        return self.call('lock', kwargs=kwargs)

    def unlock(self, **kwargs):
        return self.call('unlock', kwargs=kwargs)

    def locking(self, **kwargs):
        return self.call('locking', kwargs=kwargs)

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

    def get_all_axes(self, **kwargs):
        return self.call('get_all_axes', kwargs=kwargs)

    def remap_axes(self, **kwargs):
        return self.call('remap_axes', kwargs=kwargs)

