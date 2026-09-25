from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictKeysightn5222b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/Keysight/Keysight_N5222B.py', 'class_name': 'KeysightN5222B', 'import_roots': ['src'], 'candidate_methods': ['traces', 'get_options', 'add_trace', 'enable_trace', 'get_trace_catalog', 'select_trace_by_name', 'reset_averages', 'averages_on', 'averages_off', 'get_output', 'set_output', 'get_power', 'set_power', 'get_if_bandwidth', 'set_if_bandwidth', 'get_averages_enabled', 'set_averages_enabled', 'get_averages', 'set_averages', 'get_start', 'set_start', 'get_stop', 'set_stop', 'get_center', 'set_center', 'get_span', 'set_span', 'get_cw', 'set_cw', 'get_points', 'set_points', 'get_electrical_delay', 'set_electrical_delay', 'get_sweep_time', 'get_sweep_mode', 'set_sweep_mode', 'get_sweep_type', 'set_sweep_type', 'get_group_trigger_count', 'set_group_trigger_count', 'get_trigger_source', 'set_trigger_source', 'get_frequency_axis', 'get_frequency_log_axis', 'get_time_axis', 'get_active_trace', 'set_active_trace', 'address', 'resource_manager', 'visa_handle', 'visabackend', 'visalib', 'set_address', 'device_clear', 'set_terminator', 'close', 'write_raw', 'ask_raw', 'snapshot_base', 'get_timeout', 'set_timeout', 'get_idn', 'connect_message', 'close_all', 'record_instance', 'instances', 'remove_instance', 'find_instrument', 'exist', 'is_valid', 'label', 'add_parameter', 'remove_parameter', 'add_function', 'add_submodule', 'get_component', 'print_readable_snapshot', 'invalidate_cache', 'parent', 'ancestors', 'root_instrument', 'name_parts', 'full_name', 'name', 'short_name', 'set', 'get', 'call', 'validate_status', 'load_metadata', 'snapshot'], 'action_targets': {'get_output': '__qcodes_param_get__output', 'set_output': '__qcodes_param_set__output', 'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power', 'get_if_bandwidth': '__qcodes_param_get__if_bandwidth', 'set_if_bandwidth': '__qcodes_param_set__if_bandwidth', 'get_averages_enabled': '__qcodes_param_get__averages_enabled', 'set_averages_enabled': '__qcodes_param_set__averages_enabled', 'get_averages': '__qcodes_param_get__averages', 'set_averages': '__qcodes_param_set__averages', 'get_start': '__qcodes_param_get__start', 'set_start': '__qcodes_param_set__start', 'get_stop': '__qcodes_param_get__stop', 'set_stop': '__qcodes_param_set__stop', 'get_center': '__qcodes_param_get__center', 'set_center': '__qcodes_param_set__center', 'get_span': '__qcodes_param_get__span', 'set_span': '__qcodes_param_set__span', 'get_cw': '__qcodes_param_get__cw', 'set_cw': '__qcodes_param_set__cw', 'get_points': '__qcodes_param_get__points', 'set_points': '__qcodes_param_set__points', 'get_electrical_delay': '__qcodes_param_get__electrical_delay', 'set_electrical_delay': '__qcodes_param_set__electrical_delay', 'get_sweep_time': '__qcodes_param_get__sweep_time', 'get_sweep_mode': '__qcodes_param_get__sweep_mode', 'set_sweep_mode': '__qcodes_param_set__sweep_mode', 'get_sweep_type': '__qcodes_param_get__sweep_type', 'set_sweep_type': '__qcodes_param_set__sweep_type', 'get_group_trigger_count': '__qcodes_param_get__group_trigger_count', 'set_group_trigger_count': '__qcodes_param_set__group_trigger_count', 'get_trigger_source': '__qcodes_param_get__trigger_source', 'set_trigger_source': '__qcodes_param_set__trigger_source', 'get_frequency_axis': '__qcodes_param_get__frequency_axis', 'get_frequency_log_axis': '__qcodes_param_get__frequency_log_axis', 'get_time_axis': '__qcodes_param_get__time_axis', 'get_active_trace': '__qcodes_param_get__active_trace', 'set_active_trace': '__qcodes_param_set__active_trace', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}, 'metadata': {'repo': 'QCoDeS/Qcodes', 'repo_url': 'https://github.com/QCoDeS/Qcodes', 'source_url': 'https://github.com/QCoDeS/Qcodes/blob/main/src/qcodes/instrument_drivers/Keysight/Keysight_N5222B.py', 'confidence': 0.95, 'quality_score': 1.17, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_output': '__qcodes_param_get__output', 'set_output': '__qcodes_param_set__output', 'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power', 'get_if_bandwidth': '__qcodes_param_get__if_bandwidth', 'set_if_bandwidth': '__qcodes_param_set__if_bandwidth', 'get_averages_enabled': '__qcodes_param_get__averages_enabled', 'set_averages_enabled': '__qcodes_param_set__averages_enabled', 'get_averages': '__qcodes_param_get__averages', 'set_averages': '__qcodes_param_set__averages', 'get_start': '__qcodes_param_get__start', 'set_start': '__qcodes_param_set__start', 'get_stop': '__qcodes_param_get__stop', 'set_stop': '__qcodes_param_set__stop', 'get_center': '__qcodes_param_get__center', 'set_center': '__qcodes_param_set__center', 'get_span': '__qcodes_param_get__span', 'set_span': '__qcodes_param_set__span', 'get_cw': '__qcodes_param_get__cw', 'set_cw': '__qcodes_param_set__cw', 'get_points': '__qcodes_param_get__points', 'set_points': '__qcodes_param_set__points', 'get_electrical_delay': '__qcodes_param_get__electrical_delay', 'set_electrical_delay': '__qcodes_param_set__electrical_delay', 'get_sweep_time': '__qcodes_param_get__sweep_time', 'get_sweep_mode': '__qcodes_param_get__sweep_mode', 'set_sweep_mode': '__qcodes_param_set__sweep_mode', 'get_sweep_type': '__qcodes_param_get__sweep_type', 'set_sweep_type': '__qcodes_param_set__sweep_type', 'get_group_trigger_count': '__qcodes_param_get__group_trigger_count', 'set_group_trigger_count': '__qcodes_param_set__group_trigger_count', 'get_trigger_source': '__qcodes_param_get__trigger_source', 'set_trigger_source': '__qcodes_param_set__trigger_source', 'get_frequency_axis': '__qcodes_param_get__frequency_axis', 'get_frequency_log_axis': '__qcodes_param_get__frequency_log_axis', 'get_time_axis': '__qcodes_param_get__time_axis', 'get_active_trace': '__qcodes_param_get__active_trace', 'set_active_trace': '__qcodes_param_set__active_trace', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def traces(self, **kwargs):
        return self.call('traces', kwargs=kwargs)

    def get_options(self, **kwargs):
        return self.call('get_options', kwargs=kwargs)

    def add_trace(self, **kwargs):
        return self.call('add_trace', kwargs=kwargs)

    def enable_trace(self, **kwargs):
        return self.call('enable_trace', kwargs=kwargs)

    def get_trace_catalog(self, **kwargs):
        return self.call('get_trace_catalog', kwargs=kwargs)

    def select_trace_by_name(self, **kwargs):
        return self.call('select_trace_by_name', kwargs=kwargs)

    def reset_averages(self, **kwargs):
        return self.call('reset_averages', kwargs=kwargs)

    def averages_on(self, **kwargs):
        return self.call('averages_on', kwargs=kwargs)

    def averages_off(self, **kwargs):
        return self.call('averages_off', kwargs=kwargs)

    def get_output(self, **kwargs):
        return self.call('get_output', kwargs=kwargs)

    def set_output(self, **kwargs):
        return self.call('set_output', kwargs=kwargs)

    def get_power(self, **kwargs):
        return self.call('get_power', kwargs=kwargs)

    def set_power(self, **kwargs):
        return self.call('set_power', kwargs=kwargs)

    def get_if_bandwidth(self, **kwargs):
        return self.call('get_if_bandwidth', kwargs=kwargs)

    def set_if_bandwidth(self, **kwargs):
        return self.call('set_if_bandwidth', kwargs=kwargs)

    def get_averages_enabled(self, **kwargs):
        return self.call('get_averages_enabled', kwargs=kwargs)

    def set_averages_enabled(self, **kwargs):
        return self.call('set_averages_enabled', kwargs=kwargs)

    def get_averages(self, **kwargs):
        return self.call('get_averages', kwargs=kwargs)

    def set_averages(self, **kwargs):
        return self.call('set_averages', kwargs=kwargs)

    def get_start(self, **kwargs):
        return self.call('get_start', kwargs=kwargs)

    def set_start(self, **kwargs):
        return self.call('set_start', kwargs=kwargs)

    def get_stop(self, **kwargs):
        return self.call('get_stop', kwargs=kwargs)

    def set_stop(self, **kwargs):
        return self.call('set_stop', kwargs=kwargs)

    def get_center(self, **kwargs):
        return self.call('get_center', kwargs=kwargs)

    def set_center(self, **kwargs):
        return self.call('set_center', kwargs=kwargs)

    def get_span(self, **kwargs):
        return self.call('get_span', kwargs=kwargs)

    def set_span(self, **kwargs):
        return self.call('set_span', kwargs=kwargs)

    def get_cw(self, **kwargs):
        return self.call('get_cw', kwargs=kwargs)

    def set_cw(self, **kwargs):
        return self.call('set_cw', kwargs=kwargs)

    def get_points(self, **kwargs):
        return self.call('get_points', kwargs=kwargs)

    def set_points(self, **kwargs):
        return self.call('set_points', kwargs=kwargs)

    def get_electrical_delay(self, **kwargs):
        return self.call('get_electrical_delay', kwargs=kwargs)

    def set_electrical_delay(self, **kwargs):
        return self.call('set_electrical_delay', kwargs=kwargs)

    def get_sweep_time(self, **kwargs):
        return self.call('get_sweep_time', kwargs=kwargs)

    def get_sweep_mode(self, **kwargs):
        return self.call('get_sweep_mode', kwargs=kwargs)

    def set_sweep_mode(self, **kwargs):
        return self.call('set_sweep_mode', kwargs=kwargs)

    def get_sweep_type(self, **kwargs):
        return self.call('get_sweep_type', kwargs=kwargs)

    def set_sweep_type(self, **kwargs):
        return self.call('set_sweep_type', kwargs=kwargs)

    def get_group_trigger_count(self, **kwargs):
        return self.call('get_group_trigger_count', kwargs=kwargs)

    def set_group_trigger_count(self, **kwargs):
        return self.call('set_group_trigger_count', kwargs=kwargs)

    def get_trigger_source(self, **kwargs):
        return self.call('get_trigger_source', kwargs=kwargs)

    def set_trigger_source(self, **kwargs):
        return self.call('set_trigger_source', kwargs=kwargs)

    def get_frequency_axis(self, **kwargs):
        return self.call('get_frequency_axis', kwargs=kwargs)

    def get_frequency_log_axis(self, **kwargs):
        return self.call('get_frequency_log_axis', kwargs=kwargs)

    def get_time_axis(self, **kwargs):
        return self.call('get_time_axis', kwargs=kwargs)

    def get_active_trace(self, **kwargs):
        return self.call('get_active_trace', kwargs=kwargs)

    def set_active_trace(self, **kwargs):
        return self.call('set_active_trace', kwargs=kwargs)

    def address(self, **kwargs):
        return self.call('address', kwargs=kwargs)

    def resource_manager(self, **kwargs):
        return self.call('resource_manager', kwargs=kwargs)

    def visa_handle(self, **kwargs):
        return self.call('visa_handle', kwargs=kwargs)

    def visabackend(self, **kwargs):
        return self.call('visabackend', kwargs=kwargs)

    def visalib(self, **kwargs):
        return self.call('visalib', kwargs=kwargs)

    def set_address(self, **kwargs):
        return self.call('set_address', kwargs=kwargs)

    def device_clear(self, **kwargs):
        return self.call('device_clear', kwargs=kwargs)

    def set_terminator(self, **kwargs):
        return self.call('set_terminator', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def write_raw(self, **kwargs):
        return self.call('write_raw', kwargs=kwargs)

    def ask_raw(self, **kwargs):
        return self.call('ask_raw', kwargs=kwargs)

    def snapshot_base(self, **kwargs):
        return self.call('snapshot_base', kwargs=kwargs)

    def get_timeout(self, **kwargs):
        return self.call('get_timeout', kwargs=kwargs)

    def set_timeout(self, **kwargs):
        return self.call('set_timeout', kwargs=kwargs)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def connect_message(self, **kwargs):
        return self.call('connect_message', kwargs=kwargs)

    def close_all(self, **kwargs):
        return self.call('close_all', kwargs=kwargs)

    def record_instance(self, **kwargs):
        return self.call('record_instance', kwargs=kwargs)

    def instances(self, **kwargs):
        return self.call('instances', kwargs=kwargs)

    def remove_instance(self, **kwargs):
        return self.call('remove_instance', kwargs=kwargs)

    def find_instrument(self, **kwargs):
        return self.call('find_instrument', kwargs=kwargs)

    def exist(self, **kwargs):
        return self.call('exist', kwargs=kwargs)

    def is_valid(self, **kwargs):
        return self.call('is_valid', kwargs=kwargs)

    def label(self, **kwargs):
        return self.call('label', kwargs=kwargs)

    def add_parameter(self, **kwargs):
        return self.call('add_parameter', kwargs=kwargs)

    def remove_parameter(self, **kwargs):
        return self.call('remove_parameter', kwargs=kwargs)

    def add_function(self, **kwargs):
        return self.call('add_function', kwargs=kwargs)

    def add_submodule(self, **kwargs):
        return self.call('add_submodule', kwargs=kwargs)

    def get_component(self, **kwargs):
        return self.call('get_component', kwargs=kwargs)

    def print_readable_snapshot(self, **kwargs):
        return self.call('print_readable_snapshot', kwargs=kwargs)

    def invalidate_cache(self, **kwargs):
        return self.call('invalidate_cache', kwargs=kwargs)

    def parent(self, **kwargs):
        return self.call('parent', kwargs=kwargs)

    def ancestors(self, **kwargs):
        return self.call('ancestors', kwargs=kwargs)

    def root_instrument(self, **kwargs):
        return self.call('root_instrument', kwargs=kwargs)

    def name_parts(self, **kwargs):
        return self.call('name_parts', kwargs=kwargs)

    def full_name(self, **kwargs):
        return self.call('full_name', kwargs=kwargs)

    def name(self, **kwargs):
        return self.call('name', kwargs=kwargs)

    def short_name(self, **kwargs):
        return self.call('short_name', kwargs=kwargs)

    def set(self, **kwargs):
        return self.call('set', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def call(self, **kwargs):
        return self.call('call', kwargs=kwargs)

    def validate_status(self, **kwargs):
        return self.call('validate_status', kwargs=kwargs)

    def load_metadata(self, **kwargs):
        return self.call('load_metadata', kwargs=kwargs)

    def snapshot(self, **kwargs):
        return self.call('snapshot', kwargs=kwargs)

