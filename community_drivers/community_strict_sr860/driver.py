from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictSr860(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/stanford_research/SR860.py', 'class_name': 'SR860', 'import_roots': ['src'], 'candidate_methods': ['get_values', 'get_data_channels_values', 'get_data_channels_parameters', 'get_data_channels_dict', 'get_frequency', 'set_frequency', 'get_sine_outdc', 'set_sine_outdc', 'get_amplitude', 'set_amplitude', 'get_harmonic', 'set_harmonic', 'get_phase', 'set_phase', 'get_sensitivity', 'set_sensitivity', 'get_filter_slope', 'set_filter_slope', 'get_sync_filter', 'set_sync_filter', 'get_noise_bandwidth', 'get_signal_strength', 'get_signal_input', 'set_signal_input', 'get_input_range', 'set_input_range', 'get_input_config', 'set_input_config', 'get_input_shield', 'set_input_shield', 'get_input_gain', 'set_input_gain', 'get_adv_filter', 'set_adv_filter', 'get_input_coupling', 'set_input_coupling', 'get_time_constant', 'set_time_constant', 'get_external_reference_trigger', 'set_external_reference_trigger', 'get_reference_source', 'set_reference_source', 'get_external_reference_trigger_input_resistance', 'set_external_reference_trigger_input_resistance', 'get_x', 'get_y', 'get_r', 'get_p', 'get_complex_voltage', 'get_x_offset', 'set_x_offset', 'get_y_offset', 'set_y_offset', 'get_r_offset', 'set_r_offset', 'get_x_expand', 'set_x_expand', 'get_y_expand', 'set_y_expand', 'get_r_expand', 'set_r_expand', 'address', 'resource_manager', 'visa_handle', 'visabackend', 'visalib', 'set_address', 'device_clear', 'set_terminator', 'close', 'write_raw', 'ask_raw', 'snapshot_base', 'get_timeout', 'set_timeout', 'get_idn', 'connect_message', 'close_all', 'record_instance', 'instances', 'remove_instance', 'find_instrument', 'exist', 'is_valid', 'label', 'add_parameter', 'remove_parameter', 'add_function', 'add_submodule', 'get_component', 'print_readable_snapshot', 'invalidate_cache', 'parent', 'ancestors', 'root_instrument', 'name_parts', 'full_name', 'name', 'short_name', 'set', 'get', 'call', 'validate_status', 'load_metadata', 'snapshot'], 'action_targets': {'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_sine_outdc': '__qcodes_param_get__sine_outdc', 'set_sine_outdc': '__qcodes_param_set__sine_outdc', 'get_amplitude': '__qcodes_param_get__amplitude', 'set_amplitude': '__qcodes_param_set__amplitude', 'get_harmonic': '__qcodes_param_get__harmonic', 'set_harmonic': '__qcodes_param_set__harmonic', 'get_phase': '__qcodes_param_get__phase', 'set_phase': '__qcodes_param_set__phase', 'get_sensitivity': '__qcodes_param_get__sensitivity', 'set_sensitivity': '__qcodes_param_set__sensitivity', 'get_filter_slope': '__qcodes_param_get__filter_slope', 'set_filter_slope': '__qcodes_param_set__filter_slope', 'get_sync_filter': '__qcodes_param_get__sync_filter', 'set_sync_filter': '__qcodes_param_set__sync_filter', 'get_noise_bandwidth': '__qcodes_param_get__noise_bandwidth', 'get_signal_strength': '__qcodes_param_get__signal_strength', 'get_signal_input': '__qcodes_param_get__signal_input', 'set_signal_input': '__qcodes_param_set__signal_input', 'get_input_range': '__qcodes_param_get__input_range', 'set_input_range': '__qcodes_param_set__input_range', 'get_input_config': '__qcodes_param_get__input_config', 'set_input_config': '__qcodes_param_set__input_config', 'get_input_shield': '__qcodes_param_get__input_shield', 'set_input_shield': '__qcodes_param_set__input_shield', 'get_input_gain': '__qcodes_param_get__input_gain', 'set_input_gain': '__qcodes_param_set__input_gain', 'get_adv_filter': '__qcodes_param_get__adv_filter', 'set_adv_filter': '__qcodes_param_set__adv_filter', 'get_input_coupling': '__qcodes_param_get__input_coupling', 'set_input_coupling': '__qcodes_param_set__input_coupling', 'get_time_constant': '__qcodes_param_get__time_constant', 'set_time_constant': '__qcodes_param_set__time_constant', 'get_external_reference_trigger': '__qcodes_param_get__external_reference_trigger', 'set_external_reference_trigger': '__qcodes_param_set__external_reference_trigger', 'get_reference_source': '__qcodes_param_get__reference_source', 'set_reference_source': '__qcodes_param_set__reference_source', 'get_external_reference_trigger_input_resistance': '__qcodes_param_get__external_reference_trigger_input_resistance', 'set_external_reference_trigger_input_resistance': '__qcodes_param_set__external_reference_trigger_input_resistance', 'get_x': '__qcodes_param_get__x', 'get_y': '__qcodes_param_get__y', 'get_r': '__qcodes_param_get__r', 'get_p': '__qcodes_param_get__p', 'get_complex_voltage': '__qcodes_param_get__complex_voltage', 'get_x_offset': '__qcodes_param_get__x_offset', 'set_x_offset': '__qcodes_param_set__x_offset', 'get_y_offset': '__qcodes_param_get__y_offset', 'set_y_offset': '__qcodes_param_set__y_offset', 'get_r_offset': '__qcodes_param_get__r_offset', 'set_r_offset': '__qcodes_param_set__r_offset', 'get_x_expand': '__qcodes_param_get__x_expand', 'set_x_expand': '__qcodes_param_set__x_expand', 'get_y_expand': '__qcodes_param_get__y_expand', 'set_y_expand': '__qcodes_param_set__y_expand', 'get_r_expand': '__qcodes_param_get__r_expand', 'set_r_expand': '__qcodes_param_set__r_expand', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}, 'metadata': {'repo': 'QCoDeS/Qcodes', 'repo_url': 'https://github.com/QCoDeS/Qcodes', 'source_url': 'https://github.com/QCoDeS/Qcodes/blob/main/src/qcodes/instrument_drivers/stanford_research/SR860.py', 'confidence': 0.95, 'quality_score': 1.17, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_sine_outdc': '__qcodes_param_get__sine_outdc', 'set_sine_outdc': '__qcodes_param_set__sine_outdc', 'get_amplitude': '__qcodes_param_get__amplitude', 'set_amplitude': '__qcodes_param_set__amplitude', 'get_harmonic': '__qcodes_param_get__harmonic', 'set_harmonic': '__qcodes_param_set__harmonic', 'get_phase': '__qcodes_param_get__phase', 'set_phase': '__qcodes_param_set__phase', 'get_sensitivity': '__qcodes_param_get__sensitivity', 'set_sensitivity': '__qcodes_param_set__sensitivity', 'get_filter_slope': '__qcodes_param_get__filter_slope', 'set_filter_slope': '__qcodes_param_set__filter_slope', 'get_sync_filter': '__qcodes_param_get__sync_filter', 'set_sync_filter': '__qcodes_param_set__sync_filter', 'get_noise_bandwidth': '__qcodes_param_get__noise_bandwidth', 'get_signal_strength': '__qcodes_param_get__signal_strength', 'get_signal_input': '__qcodes_param_get__signal_input', 'set_signal_input': '__qcodes_param_set__signal_input', 'get_input_range': '__qcodes_param_get__input_range', 'set_input_range': '__qcodes_param_set__input_range', 'get_input_config': '__qcodes_param_get__input_config', 'set_input_config': '__qcodes_param_set__input_config', 'get_input_shield': '__qcodes_param_get__input_shield', 'set_input_shield': '__qcodes_param_set__input_shield', 'get_input_gain': '__qcodes_param_get__input_gain', 'set_input_gain': '__qcodes_param_set__input_gain', 'get_adv_filter': '__qcodes_param_get__adv_filter', 'set_adv_filter': '__qcodes_param_set__adv_filter', 'get_input_coupling': '__qcodes_param_get__input_coupling', 'set_input_coupling': '__qcodes_param_set__input_coupling', 'get_time_constant': '__qcodes_param_get__time_constant', 'set_time_constant': '__qcodes_param_set__time_constant', 'get_external_reference_trigger': '__qcodes_param_get__external_reference_trigger', 'set_external_reference_trigger': '__qcodes_param_set__external_reference_trigger', 'get_reference_source': '__qcodes_param_get__reference_source', 'set_reference_source': '__qcodes_param_set__reference_source', 'get_external_reference_trigger_input_resistance': '__qcodes_param_get__external_reference_trigger_input_resistance', 'set_external_reference_trigger_input_resistance': '__qcodes_param_set__external_reference_trigger_input_resistance', 'get_x': '__qcodes_param_get__x', 'get_y': '__qcodes_param_get__y', 'get_r': '__qcodes_param_get__r', 'get_p': '__qcodes_param_get__p', 'get_complex_voltage': '__qcodes_param_get__complex_voltage', 'get_x_offset': '__qcodes_param_get__x_offset', 'set_x_offset': '__qcodes_param_set__x_offset', 'get_y_offset': '__qcodes_param_get__y_offset', 'set_y_offset': '__qcodes_param_set__y_offset', 'get_r_offset': '__qcodes_param_get__r_offset', 'set_r_offset': '__qcodes_param_set__r_offset', 'get_x_expand': '__qcodes_param_get__x_expand', 'set_x_expand': '__qcodes_param_set__x_expand', 'get_y_expand': '__qcodes_param_get__y_expand', 'set_y_expand': '__qcodes_param_set__y_expand', 'get_r_expand': '__qcodes_param_get__r_expand', 'set_r_expand': '__qcodes_param_set__r_expand', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_values(self, **kwargs):
        return self.call('get_values', kwargs=kwargs)

    def get_data_channels_values(self, **kwargs):
        return self.call('get_data_channels_values', kwargs=kwargs)

    def get_data_channels_parameters(self, **kwargs):
        return self.call('get_data_channels_parameters', kwargs=kwargs)

    def get_data_channels_dict(self, **kwargs):
        return self.call('get_data_channels_dict', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def get_sine_outdc(self, **kwargs):
        return self.call('get_sine_outdc', kwargs=kwargs)

    def set_sine_outdc(self, **kwargs):
        return self.call('set_sine_outdc', kwargs=kwargs)

    def get_amplitude(self, **kwargs):
        return self.call('get_amplitude', kwargs=kwargs)

    def set_amplitude(self, **kwargs):
        return self.call('set_amplitude', kwargs=kwargs)

    def get_harmonic(self, **kwargs):
        return self.call('get_harmonic', kwargs=kwargs)

    def set_harmonic(self, **kwargs):
        return self.call('set_harmonic', kwargs=kwargs)

    def get_phase(self, **kwargs):
        return self.call('get_phase', kwargs=kwargs)

    def set_phase(self, **kwargs):
        return self.call('set_phase', kwargs=kwargs)

    def get_sensitivity(self, **kwargs):
        return self.call('get_sensitivity', kwargs=kwargs)

    def set_sensitivity(self, **kwargs):
        return self.call('set_sensitivity', kwargs=kwargs)

    def get_filter_slope(self, **kwargs):
        return self.call('get_filter_slope', kwargs=kwargs)

    def set_filter_slope(self, **kwargs):
        return self.call('set_filter_slope', kwargs=kwargs)

    def get_sync_filter(self, **kwargs):
        return self.call('get_sync_filter', kwargs=kwargs)

    def set_sync_filter(self, **kwargs):
        return self.call('set_sync_filter', kwargs=kwargs)

    def get_noise_bandwidth(self, **kwargs):
        return self.call('get_noise_bandwidth', kwargs=kwargs)

    def get_signal_strength(self, **kwargs):
        return self.call('get_signal_strength', kwargs=kwargs)

    def get_signal_input(self, **kwargs):
        return self.call('get_signal_input', kwargs=kwargs)

    def set_signal_input(self, **kwargs):
        return self.call('set_signal_input', kwargs=kwargs)

    def get_input_range(self, **kwargs):
        return self.call('get_input_range', kwargs=kwargs)

    def set_input_range(self, **kwargs):
        return self.call('set_input_range', kwargs=kwargs)

    def get_input_config(self, **kwargs):
        return self.call('get_input_config', kwargs=kwargs)

    def set_input_config(self, **kwargs):
        return self.call('set_input_config', kwargs=kwargs)

    def get_input_shield(self, **kwargs):
        return self.call('get_input_shield', kwargs=kwargs)

    def set_input_shield(self, **kwargs):
        return self.call('set_input_shield', kwargs=kwargs)

    def get_input_gain(self, **kwargs):
        return self.call('get_input_gain', kwargs=kwargs)

    def set_input_gain(self, **kwargs):
        return self.call('set_input_gain', kwargs=kwargs)

    def get_adv_filter(self, **kwargs):
        return self.call('get_adv_filter', kwargs=kwargs)

    def set_adv_filter(self, **kwargs):
        return self.call('set_adv_filter', kwargs=kwargs)

    def get_input_coupling(self, **kwargs):
        return self.call('get_input_coupling', kwargs=kwargs)

    def set_input_coupling(self, **kwargs):
        return self.call('set_input_coupling', kwargs=kwargs)

    def get_time_constant(self, **kwargs):
        return self.call('get_time_constant', kwargs=kwargs)

    def set_time_constant(self, **kwargs):
        return self.call('set_time_constant', kwargs=kwargs)

    def get_external_reference_trigger(self, **kwargs):
        return self.call('get_external_reference_trigger', kwargs=kwargs)

    def set_external_reference_trigger(self, **kwargs):
        return self.call('set_external_reference_trigger', kwargs=kwargs)

    def get_reference_source(self, **kwargs):
        return self.call('get_reference_source', kwargs=kwargs)

    def set_reference_source(self, **kwargs):
        return self.call('set_reference_source', kwargs=kwargs)

    def get_external_reference_trigger_input_resistance(self, **kwargs):
        return self.call('get_external_reference_trigger_input_resistance', kwargs=kwargs)

    def set_external_reference_trigger_input_resistance(self, **kwargs):
        return self.call('set_external_reference_trigger_input_resistance', kwargs=kwargs)

    def get_x(self, **kwargs):
        return self.call('get_x', kwargs=kwargs)

    def get_y(self, **kwargs):
        return self.call('get_y', kwargs=kwargs)

    def get_r(self, **kwargs):
        return self.call('get_r', kwargs=kwargs)

    def get_p(self, **kwargs):
        return self.call('get_p', kwargs=kwargs)

    def get_complex_voltage(self, **kwargs):
        return self.call('get_complex_voltage', kwargs=kwargs)

    def get_x_offset(self, **kwargs):
        return self.call('get_x_offset', kwargs=kwargs)

    def set_x_offset(self, **kwargs):
        return self.call('set_x_offset', kwargs=kwargs)

    def get_y_offset(self, **kwargs):
        return self.call('get_y_offset', kwargs=kwargs)

    def set_y_offset(self, **kwargs):
        return self.call('set_y_offset', kwargs=kwargs)

    def get_r_offset(self, **kwargs):
        return self.call('get_r_offset', kwargs=kwargs)

    def set_r_offset(self, **kwargs):
        return self.call('set_r_offset', kwargs=kwargs)

    def get_x_expand(self, **kwargs):
        return self.call('get_x_expand', kwargs=kwargs)

    def set_x_expand(self, **kwargs):
        return self.call('set_x_expand', kwargs=kwargs)

    def get_y_expand(self, **kwargs):
        return self.call('get_y_expand', kwargs=kwargs)

    def set_y_expand(self, **kwargs):
        return self.call('set_y_expand', kwargs=kwargs)

    def get_r_expand(self, **kwargs):
        return self.call('get_r_expand', kwargs=kwargs)

    def set_r_expand(self, **kwargs):
        return self.call('set_r_expand', kwargs=kwargs)

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

