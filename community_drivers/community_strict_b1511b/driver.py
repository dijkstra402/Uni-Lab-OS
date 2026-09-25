from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictB1511b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/Keysight/keysightb1500/KeysightB1511B.py', 'class_name': 'KeysightB1511B', 'import_roots': ['src'], 'candidate_methods': ['asu_present', 'source_config', 'v_measure_range_config', 'i_measure_range_config', 'timing_parameters', 'use_high_speed_adc', 'use_high_resolution_adc', 'set_average_samples_for_high_speed_adc', 'setup_staircase_sweep', 'set_measurement_mode', 'get_measurement_operation_mode', 'set_measurement_operation_mode', 'get_voltage', 'get_current', 'get_time_axis', 'get_sampling_measurement_trace', 'get_current_measurement_range', 'set_current_measurement_range', 'set_enable_filter', 'enable_outputs', 'disable_outputs', 'is_enabled', 'clear_timer_count', 'write_raw', 'ask_raw', 'parent', 'root_instrument', 'name_parts', 'label', 'add_parameter', 'remove_parameter', 'add_function', 'add_submodule', 'get_component', 'snapshot_base', 'print_readable_snapshot', 'invalidate_cache', 'ancestors', 'full_name', 'name', 'short_name', 'set', 'get', 'call', 'validate_status', 'load_metadata', 'snapshot'], 'action_targets': {'set_measurement_mode': '__qcodes_param_set__measurement_mode', 'get_measurement_operation_mode': '__qcodes_param_get__measurement_operation_mode', 'set_measurement_operation_mode': '__qcodes_param_set__measurement_operation_mode', 'get_voltage': '__qcodes_param_get__voltage', 'get_current': '__qcodes_param_get__current', 'get_time_axis': '__qcodes_param_get__time_axis', 'get_sampling_measurement_trace': '__qcodes_param_get__sampling_measurement_trace', 'get_current_measurement_range': '__qcodes_param_get__current_measurement_range', 'set_current_measurement_range': '__qcodes_param_set__current_measurement_range', 'set_enable_filter': '__qcodes_param_set__enable_filter'}, 'metadata': {'repo': 'QCoDeS/Qcodes', 'repo_url': 'https://github.com/QCoDeS/Qcodes', 'source_url': 'https://github.com/QCoDeS/Qcodes/blob/main/src/qcodes/instrument_drivers/Keysight/keysightb1500/KeysightB1511B.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'set_measurement_mode': '__qcodes_param_set__measurement_mode', 'get_measurement_operation_mode': '__qcodes_param_get__measurement_operation_mode', 'set_measurement_operation_mode': '__qcodes_param_set__measurement_operation_mode', 'get_voltage': '__qcodes_param_get__voltage', 'get_current': '__qcodes_param_get__current', 'get_time_axis': '__qcodes_param_get__time_axis', 'get_sampling_measurement_trace': '__qcodes_param_get__sampling_measurement_trace', 'get_current_measurement_range': '__qcodes_param_get__current_measurement_range', 'set_current_measurement_range': '__qcodes_param_set__current_measurement_range', 'set_enable_filter': '__qcodes_param_set__enable_filter'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def asu_present(self, **kwargs):
        return self.call('asu_present', kwargs=kwargs)

    def source_config(self, **kwargs):
        return self.call('source_config', kwargs=kwargs)

    def v_measure_range_config(self, **kwargs):
        return self.call('v_measure_range_config', kwargs=kwargs)

    def i_measure_range_config(self, **kwargs):
        return self.call('i_measure_range_config', kwargs=kwargs)

    def timing_parameters(self, **kwargs):
        return self.call('timing_parameters', kwargs=kwargs)

    def use_high_speed_adc(self, **kwargs):
        return self.call('use_high_speed_adc', kwargs=kwargs)

    def use_high_resolution_adc(self, **kwargs):
        return self.call('use_high_resolution_adc', kwargs=kwargs)

    def set_average_samples_for_high_speed_adc(self, **kwargs):
        return self.call('set_average_samples_for_high_speed_adc', kwargs=kwargs)

    def setup_staircase_sweep(self, **kwargs):
        return self.call('setup_staircase_sweep', kwargs=kwargs)

    def set_measurement_mode(self, **kwargs):
        return self.call('set_measurement_mode', kwargs=kwargs)

    def get_measurement_operation_mode(self, **kwargs):
        return self.call('get_measurement_operation_mode', kwargs=kwargs)

    def set_measurement_operation_mode(self, **kwargs):
        return self.call('set_measurement_operation_mode', kwargs=kwargs)

    def get_voltage(self, **kwargs):
        return self.call('get_voltage', kwargs=kwargs)

    def get_current(self, **kwargs):
        return self.call('get_current', kwargs=kwargs)

    def get_time_axis(self, **kwargs):
        return self.call('get_time_axis', kwargs=kwargs)

    def get_sampling_measurement_trace(self, **kwargs):
        return self.call('get_sampling_measurement_trace', kwargs=kwargs)

    def get_current_measurement_range(self, **kwargs):
        return self.call('get_current_measurement_range', kwargs=kwargs)

    def set_current_measurement_range(self, **kwargs):
        return self.call('set_current_measurement_range', kwargs=kwargs)

    def set_enable_filter(self, **kwargs):
        return self.call('set_enable_filter', kwargs=kwargs)

    def enable_outputs(self, **kwargs):
        return self.call('enable_outputs', kwargs=kwargs)

    def disable_outputs(self, **kwargs):
        return self.call('disable_outputs', kwargs=kwargs)

    def is_enabled(self, **kwargs):
        return self.call('is_enabled', kwargs=kwargs)

    def clear_timer_count(self, **kwargs):
        return self.call('clear_timer_count', kwargs=kwargs)

    def write_raw(self, **kwargs):
        return self.call('write_raw', kwargs=kwargs)

    def ask_raw(self, **kwargs):
        return self.call('ask_raw', kwargs=kwargs)

    def parent(self, **kwargs):
        return self.call('parent', kwargs=kwargs)

    def root_instrument(self, **kwargs):
        return self.call('root_instrument', kwargs=kwargs)

    def name_parts(self, **kwargs):
        return self.call('name_parts', kwargs=kwargs)

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

    def snapshot_base(self, **kwargs):
        return self.call('snapshot_base', kwargs=kwargs)

    def print_readable_snapshot(self, **kwargs):
        return self.call('print_readable_snapshot', kwargs=kwargs)

    def invalidate_cache(self, **kwargs):
        return self.call('invalidate_cache', kwargs=kwargs)

    def ancestors(self, **kwargs):
        return self.call('ancestors', kwargs=kwargs)

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

