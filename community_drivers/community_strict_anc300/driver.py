from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAnc300(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/AlexShkarin__pyLabLib', 'source_file': 'pylablib/devices/Attocube/anc300.py', 'class_name': 'ANC300', 'import_roots': [], 'candidate_methods': ['open', 'query', 'update_available_axes', 'get_device_info', 'get_axis_serial', 'set_mode', 'get_mode', 'is_enabled', 'enable_axis', 'disable_axis', 'measure_capacitance', 'get_voltage', 'set_voltage', 'get_offset', 'set_offset', 'get_output', 'get_frequency', 'set_frequency', 'get_capacitance', 'get_voltage_pattern', 'set_voltage_pattern', 'get_trigger_input', 'set_trigger_input', 'get_external_input_modes', 'set_external_input_modes', 'get_axis_correction', 'set_axis_correction', 'jog', 'move_by', 'wait_move', 'is_moving', 'stop', 'close', 'is_opened', 'lock', 'unlock', 'locking', 'get_settings', 'get_full_status', 'get_full_info', 'apply_settings', 'get_device_variable', 'set_device_variable', 'get_all_axes', 'remap_axes'], 'action_targets': {}, 'metadata': {'repo': 'AlexShkarin/pyLabLib', 'repo_url': 'https://github.com/AlexShkarin/pyLabLib', 'source_url': 'https://github.com/AlexShkarin/pyLabLib/blob/main/pylablib/devices/Attocube/anc300.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def update_available_axes(self, **kwargs):
        return self.call('update_available_axes', kwargs=kwargs)

    def get_device_info(self, **kwargs):
        return self.call('get_device_info', kwargs=kwargs)

    def get_axis_serial(self, **kwargs):
        return self.call('get_axis_serial', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def get_mode(self, **kwargs):
        return self.call('get_mode', kwargs=kwargs)

    def is_enabled(self, **kwargs):
        return self.call('is_enabled', kwargs=kwargs)

    def enable_axis(self, **kwargs):
        return self.call('enable_axis', kwargs=kwargs)

    def disable_axis(self, **kwargs):
        return self.call('disable_axis', kwargs=kwargs)

    def measure_capacitance(self, **kwargs):
        return self.call('measure_capacitance', kwargs=kwargs)

    def get_voltage(self, **kwargs):
        return self.call('get_voltage', kwargs=kwargs)

    def set_voltage(self, **kwargs):
        return self.call('set_voltage', kwargs=kwargs)

    def get_offset(self, **kwargs):
        return self.call('get_offset', kwargs=kwargs)

    def set_offset(self, **kwargs):
        return self.call('set_offset', kwargs=kwargs)

    def get_output(self, **kwargs):
        return self.call('get_output', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def get_capacitance(self, **kwargs):
        return self.call('get_capacitance', kwargs=kwargs)

    def get_voltage_pattern(self, **kwargs):
        return self.call('get_voltage_pattern', kwargs=kwargs)

    def set_voltage_pattern(self, **kwargs):
        return self.call('set_voltage_pattern', kwargs=kwargs)

    def get_trigger_input(self, **kwargs):
        return self.call('get_trigger_input', kwargs=kwargs)

    def set_trigger_input(self, **kwargs):
        return self.call('set_trigger_input', kwargs=kwargs)

    def get_external_input_modes(self, **kwargs):
        return self.call('get_external_input_modes', kwargs=kwargs)

    def set_external_input_modes(self, **kwargs):
        return self.call('set_external_input_modes', kwargs=kwargs)

    def get_axis_correction(self, **kwargs):
        return self.call('get_axis_correction', kwargs=kwargs)

    def set_axis_correction(self, **kwargs):
        return self.call('set_axis_correction', kwargs=kwargs)

    def jog(self, **kwargs):
        return self.call('jog', kwargs=kwargs)

    def move_by(self, **kwargs):
        return self.call('move_by', kwargs=kwargs)

    def wait_move(self, **kwargs):
        return self.call('wait_move', kwargs=kwargs)

    def is_moving(self, **kwargs):
        return self.call('is_moving', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

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

