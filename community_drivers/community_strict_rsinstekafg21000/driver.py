from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictRsinstekafg21000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/AlexShkarin__pyLabLib', 'source_file': 'pylablib/devices/AWG/specific.py', 'class_name': 'RSInstekAFG21000', 'import_roots': [], 'candidate_methods': ['get_offset', 'get_amplitude', 'set_offset', 'set_amplitude', 'get_channels_number', 'get_current_channel', 'select_current_channel', 'is_output_enabled', 'enable_output', 'get_output_polarity', 'set_output_polarity', 'is_sync_output_enabled', 'enable_sync_output', 'get_load', 'set_load', 'get_function', 'set_function', 'get_output_range', 'set_output_range', 'get_frequency', 'set_frequency', 'get_phase', 'set_phase', 'sync_phase', 'get_duty_cycle', 'set_duty_cycle', 'get_ramp_symmetry', 'set_ramp_symmetry', 'get_pulse_width', 'set_pulse_width', 'is_burst_enabled', 'enable_burst', 'get_burst_mode', 'set_burst_mode', 'get_burst_ncycles', 'set_burst_ncycles', 'get_gate_polarity', 'set_gate_polarity', 'get_trigger_source', 'set_trigger_source', 'get_trigger_slope', 'set_trigger_slope', 'is_trigger_output_enabled', 'enable_trigger_output', 'get_output_trigger_slope', 'set_output_trigger_slope', 'reconnect', 'sleep', 'using_write_buffer', 'get_id', 'get_esr', 'wait_sync', 'wait_dev', 'wait', 'get_arg_type', 'flush', 'read_binary_array_data', 'parse_array_data', 'apply_settings', 'open', 'close', 'is_opened', 'lock', 'unlock', 'locking', 'get_settings', 'get_full_status', 'get_full_info', 'get_device_variable', 'set_device_variable'], 'action_targets': {}, 'metadata': {'repo': 'AlexShkarin/pyLabLib', 'repo_url': 'https://github.com/AlexShkarin/pyLabLib', 'source_url': 'https://github.com/AlexShkarin/pyLabLib/blob/main/pylablib/devices/AWG/specific.py', 'confidence': 0.9, 'quality_score': 1.06, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_offset(self, **kwargs):
        return self.call('get_offset', kwargs=kwargs)

    def get_amplitude(self, **kwargs):
        return self.call('get_amplitude', kwargs=kwargs)

    def set_offset(self, **kwargs):
        return self.call('set_offset', kwargs=kwargs)

    def set_amplitude(self, **kwargs):
        return self.call('set_amplitude', kwargs=kwargs)

    def get_channels_number(self, **kwargs):
        return self.call('get_channels_number', kwargs=kwargs)

    def get_current_channel(self, **kwargs):
        return self.call('get_current_channel', kwargs=kwargs)

    def select_current_channel(self, **kwargs):
        return self.call('select_current_channel', kwargs=kwargs)

    def is_output_enabled(self, **kwargs):
        return self.call('is_output_enabled', kwargs=kwargs)

    def enable_output(self, **kwargs):
        return self.call('enable_output', kwargs=kwargs)

    def get_output_polarity(self, **kwargs):
        return self.call('get_output_polarity', kwargs=kwargs)

    def set_output_polarity(self, **kwargs):
        return self.call('set_output_polarity', kwargs=kwargs)

    def is_sync_output_enabled(self, **kwargs):
        return self.call('is_sync_output_enabled', kwargs=kwargs)

    def enable_sync_output(self, **kwargs):
        return self.call('enable_sync_output', kwargs=kwargs)

    def get_load(self, **kwargs):
        return self.call('get_load', kwargs=kwargs)

    def set_load(self, **kwargs):
        return self.call('set_load', kwargs=kwargs)

    def get_function(self, **kwargs):
        return self.call('get_function', kwargs=kwargs)

    def set_function(self, **kwargs):
        return self.call('set_function', kwargs=kwargs)

    def get_output_range(self, **kwargs):
        return self.call('get_output_range', kwargs=kwargs)

    def set_output_range(self, **kwargs):
        return self.call('set_output_range', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def get_phase(self, **kwargs):
        return self.call('get_phase', kwargs=kwargs)

    def set_phase(self, **kwargs):
        return self.call('set_phase', kwargs=kwargs)

    def sync_phase(self, **kwargs):
        return self.call('sync_phase', kwargs=kwargs)

    def get_duty_cycle(self, **kwargs):
        return self.call('get_duty_cycle', kwargs=kwargs)

    def set_duty_cycle(self, **kwargs):
        return self.call('set_duty_cycle', kwargs=kwargs)

    def get_ramp_symmetry(self, **kwargs):
        return self.call('get_ramp_symmetry', kwargs=kwargs)

    def set_ramp_symmetry(self, **kwargs):
        return self.call('set_ramp_symmetry', kwargs=kwargs)

    def get_pulse_width(self, **kwargs):
        return self.call('get_pulse_width', kwargs=kwargs)

    def set_pulse_width(self, **kwargs):
        return self.call('set_pulse_width', kwargs=kwargs)

    def is_burst_enabled(self, **kwargs):
        return self.call('is_burst_enabled', kwargs=kwargs)

    def enable_burst(self, **kwargs):
        return self.call('enable_burst', kwargs=kwargs)

    def get_burst_mode(self, **kwargs):
        return self.call('get_burst_mode', kwargs=kwargs)

    def set_burst_mode(self, **kwargs):
        return self.call('set_burst_mode', kwargs=kwargs)

    def get_burst_ncycles(self, **kwargs):
        return self.call('get_burst_ncycles', kwargs=kwargs)

    def set_burst_ncycles(self, **kwargs):
        return self.call('set_burst_ncycles', kwargs=kwargs)

    def get_gate_polarity(self, **kwargs):
        return self.call('get_gate_polarity', kwargs=kwargs)

    def set_gate_polarity(self, **kwargs):
        return self.call('set_gate_polarity', kwargs=kwargs)

    def get_trigger_source(self, **kwargs):
        return self.call('get_trigger_source', kwargs=kwargs)

    def set_trigger_source(self, **kwargs):
        return self.call('set_trigger_source', kwargs=kwargs)

    def get_trigger_slope(self, **kwargs):
        return self.call('get_trigger_slope', kwargs=kwargs)

    def set_trigger_slope(self, **kwargs):
        return self.call('set_trigger_slope', kwargs=kwargs)

    def is_trigger_output_enabled(self, **kwargs):
        return self.call('is_trigger_output_enabled', kwargs=kwargs)

    def enable_trigger_output(self, **kwargs):
        return self.call('enable_trigger_output', kwargs=kwargs)

    def get_output_trigger_slope(self, **kwargs):
        return self.call('get_output_trigger_slope', kwargs=kwargs)

    def set_output_trigger_slope(self, **kwargs):
        return self.call('set_output_trigger_slope', kwargs=kwargs)

    def reconnect(self, **kwargs):
        return self.call('reconnect', kwargs=kwargs)

    def sleep(self, **kwargs):
        return self.call('sleep', kwargs=kwargs)

    def using_write_buffer(self, **kwargs):
        return self.call('using_write_buffer', kwargs=kwargs)

    def get_id(self, **kwargs):
        return self.call('get_id', kwargs=kwargs)

    def get_esr(self, **kwargs):
        return self.call('get_esr', kwargs=kwargs)

    def wait_sync(self, **kwargs):
        return self.call('wait_sync', kwargs=kwargs)

    def wait_dev(self, **kwargs):
        return self.call('wait_dev', kwargs=kwargs)

    def wait(self, **kwargs):
        return self.call('wait', kwargs=kwargs)

    def get_arg_type(self, **kwargs):
        return self.call('get_arg_type', kwargs=kwargs)

    def flush(self, **kwargs):
        return self.call('flush', kwargs=kwargs)

    def read_binary_array_data(self, **kwargs):
        return self.call('read_binary_array_data', kwargs=kwargs)

    def parse_array_data(self, **kwargs):
        return self.call('parse_array_data', kwargs=kwargs)

    def apply_settings(self, **kwargs):
        return self.call('apply_settings', kwargs=kwargs)

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

    def get_device_variable(self, **kwargs):
        return self.call('get_device_variable', kwargs=kwargs)

    def set_device_variable(self, **kwargs):
        return self.call('set_device_variable', kwargs=kwargs)

