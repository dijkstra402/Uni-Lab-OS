from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictCoppermountainm5065(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/CopperMountain/_M5065.py', 'class_name': 'CopperMountainM5065', 'import_roots': ['src'], 'candidate_methods': ['get_s_parameters', 'update_lin_traces', 'reset_averages', 'get_output', 'set_output', 'get_power', 'set_power', 'get_if_bandwidth', 'set_if_bandwidth', 'get_averages_enabled', 'set_averages_enabled', 'get_averages_trigger_enabled', 'set_averages_trigger_enabled', 'get_averages', 'set_averages', 'get_electrical_delay', 'set_electrical_delay', 'get_electrical_distance', 'set_electrical_distance', 'get_electrical_distance_units', 'set_electrical_distance_units', 'get_clock_source', 'set_clock_source', 'get_start', 'set_start', 'get_stop', 'set_stop', 'get_center', 'set_center', 'get_span', 'set_span', 'get_number_of_points', 'set_number_of_points', 'get_number_of_traces', 'set_number_of_traces', 'get_trigger_source', 'set_trigger_source', 'get_data_transfer_format', 'set_data_transfer_format', 'get_s11', 'get_s12', 'get_s21', 'get_s22', 'get_point_s11', 'get_point_s12', 'get_point_s21', 'get_point_s22', 'get_point_s11_iq', 'get_point_s12_iq', 'get_point_s21_iq', 'get_point_s22_iq', 'get_point_check_sweep_first', 'address', 'resource_manager', 'visa_handle', 'visabackend', 'visalib', 'set_address', 'device_clear', 'set_terminator', 'close', 'write_raw', 'ask_raw', 'snapshot_base', 'get_timeout', 'set_timeout', 'get_idn', 'connect_message', 'close_all', 'record_instance', 'instances', 'remove_instance', 'find_instrument', 'exist', 'is_valid', 'label', 'add_parameter', 'remove_parameter', 'add_function', 'add_submodule', 'get_component', 'print_readable_snapshot', 'invalidate_cache', 'parent', 'ancestors', 'root_instrument', 'name_parts', 'full_name', 'name', 'short_name', 'set', 'get', 'call', 'validate_status', 'load_metadata', 'snapshot'], 'action_targets': {'get_output': '__qcodes_param_get__output', 'set_output': '__qcodes_param_set__output', 'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power', 'get_if_bandwidth': '__qcodes_param_get__if_bandwidth', 'set_if_bandwidth': '__qcodes_param_set__if_bandwidth', 'get_averages_enabled': '__qcodes_param_get__averages_enabled', 'set_averages_enabled': '__qcodes_param_set__averages_enabled', 'get_averages_trigger_enabled': '__qcodes_param_get__averages_trigger_enabled', 'set_averages_trigger_enabled': '__qcodes_param_set__averages_trigger_enabled', 'get_averages': '__qcodes_param_get__averages', 'set_averages': '__qcodes_param_set__averages', 'get_electrical_delay': '__qcodes_param_get__electrical_delay', 'set_electrical_delay': '__qcodes_param_set__electrical_delay', 'get_electrical_distance': '__qcodes_param_get__electrical_distance', 'set_electrical_distance': '__qcodes_param_set__electrical_distance', 'get_electrical_distance_units': '__qcodes_param_get__electrical_distance_units', 'set_electrical_distance_units': '__qcodes_param_set__electrical_distance_units', 'get_clock_source': '__qcodes_param_get__clock_source', 'set_clock_source': '__qcodes_param_set__clock_source', 'get_start': '__qcodes_param_get__start', 'set_start': '__qcodes_param_set__start', 'get_stop': '__qcodes_param_get__stop', 'set_stop': '__qcodes_param_set__stop', 'get_center': '__qcodes_param_get__center', 'set_center': '__qcodes_param_set__center', 'get_span': '__qcodes_param_get__span', 'set_span': '__qcodes_param_set__span', 'get_number_of_points': '__qcodes_param_get__number_of_points', 'set_number_of_points': '__qcodes_param_set__number_of_points', 'get_number_of_traces': '__qcodes_param_get__number_of_traces', 'set_number_of_traces': '__qcodes_param_set__number_of_traces', 'get_trigger_source': '__qcodes_param_get__trigger_source', 'set_trigger_source': '__qcodes_param_set__trigger_source', 'get_data_transfer_format': '__qcodes_param_get__data_transfer_format', 'set_data_transfer_format': '__qcodes_param_set__data_transfer_format', 'get_s11': '__qcodes_param_get__s11', 'get_s12': '__qcodes_param_get__s12', 'get_s21': '__qcodes_param_get__s21', 'get_s22': '__qcodes_param_get__s22', 'get_point_s11': '__qcodes_param_get__point_s11', 'get_point_s12': '__qcodes_param_get__point_s12', 'get_point_s21': '__qcodes_param_get__point_s21', 'get_point_s22': '__qcodes_param_get__point_s22', 'get_point_s11_iq': '__qcodes_param_get__point_s11_iq', 'get_point_s12_iq': '__qcodes_param_get__point_s12_iq', 'get_point_s21_iq': '__qcodes_param_get__point_s21_iq', 'get_point_s22_iq': '__qcodes_param_get__point_s22_iq', 'get_point_check_sweep_first': '__qcodes_param_get__point_check_sweep_first', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}, 'metadata': {'repo': 'QCoDeS/Qcodes', 'repo_url': 'https://github.com/QCoDeS/Qcodes', 'source_url': 'https://github.com/QCoDeS/Qcodes/blob/main/src/qcodes/instrument_drivers/CopperMountain/_M5065.py', 'confidence': 0.8, 'quality_score': 0.94, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_output': '__qcodes_param_get__output', 'set_output': '__qcodes_param_set__output', 'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power', 'get_if_bandwidth': '__qcodes_param_get__if_bandwidth', 'set_if_bandwidth': '__qcodes_param_set__if_bandwidth', 'get_averages_enabled': '__qcodes_param_get__averages_enabled', 'set_averages_enabled': '__qcodes_param_set__averages_enabled', 'get_averages_trigger_enabled': '__qcodes_param_get__averages_trigger_enabled', 'set_averages_trigger_enabled': '__qcodes_param_set__averages_trigger_enabled', 'get_averages': '__qcodes_param_get__averages', 'set_averages': '__qcodes_param_set__averages', 'get_electrical_delay': '__qcodes_param_get__electrical_delay', 'set_electrical_delay': '__qcodes_param_set__electrical_delay', 'get_electrical_distance': '__qcodes_param_get__electrical_distance', 'set_electrical_distance': '__qcodes_param_set__electrical_distance', 'get_electrical_distance_units': '__qcodes_param_get__electrical_distance_units', 'set_electrical_distance_units': '__qcodes_param_set__electrical_distance_units', 'get_clock_source': '__qcodes_param_get__clock_source', 'set_clock_source': '__qcodes_param_set__clock_source', 'get_start': '__qcodes_param_get__start', 'set_start': '__qcodes_param_set__start', 'get_stop': '__qcodes_param_get__stop', 'set_stop': '__qcodes_param_set__stop', 'get_center': '__qcodes_param_get__center', 'set_center': '__qcodes_param_set__center', 'get_span': '__qcodes_param_get__span', 'set_span': '__qcodes_param_set__span', 'get_number_of_points': '__qcodes_param_get__number_of_points', 'set_number_of_points': '__qcodes_param_set__number_of_points', 'get_number_of_traces': '__qcodes_param_get__number_of_traces', 'set_number_of_traces': '__qcodes_param_set__number_of_traces', 'get_trigger_source': '__qcodes_param_get__trigger_source', 'set_trigger_source': '__qcodes_param_set__trigger_source', 'get_data_transfer_format': '__qcodes_param_get__data_transfer_format', 'set_data_transfer_format': '__qcodes_param_set__data_transfer_format', 'get_s11': '__qcodes_param_get__s11', 'get_s12': '__qcodes_param_get__s12', 'get_s21': '__qcodes_param_get__s21', 'get_s22': '__qcodes_param_get__s22', 'get_point_s11': '__qcodes_param_get__point_s11', 'get_point_s12': '__qcodes_param_get__point_s12', 'get_point_s21': '__qcodes_param_get__point_s21', 'get_point_s22': '__qcodes_param_get__point_s22', 'get_point_s11_iq': '__qcodes_param_get__point_s11_iq', 'get_point_s12_iq': '__qcodes_param_get__point_s12_iq', 'get_point_s21_iq': '__qcodes_param_get__point_s21_iq', 'get_point_s22_iq': '__qcodes_param_get__point_s22_iq', 'get_point_check_sweep_first': '__qcodes_param_get__point_check_sweep_first', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_s_parameters(self, **kwargs):
        return self.call('get_s_parameters', kwargs=kwargs)

    def update_lin_traces(self, **kwargs):
        return self.call('update_lin_traces', kwargs=kwargs)

    def reset_averages(self, **kwargs):
        return self.call('reset_averages', kwargs=kwargs)

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

    def get_averages_trigger_enabled(self, **kwargs):
        return self.call('get_averages_trigger_enabled', kwargs=kwargs)

    def set_averages_trigger_enabled(self, **kwargs):
        return self.call('set_averages_trigger_enabled', kwargs=kwargs)

    def get_averages(self, **kwargs):
        return self.call('get_averages', kwargs=kwargs)

    def set_averages(self, **kwargs):
        return self.call('set_averages', kwargs=kwargs)

    def get_electrical_delay(self, **kwargs):
        return self.call('get_electrical_delay', kwargs=kwargs)

    def set_electrical_delay(self, **kwargs):
        return self.call('set_electrical_delay', kwargs=kwargs)

    def get_electrical_distance(self, **kwargs):
        return self.call('get_electrical_distance', kwargs=kwargs)

    def set_electrical_distance(self, **kwargs):
        return self.call('set_electrical_distance', kwargs=kwargs)

    def get_electrical_distance_units(self, **kwargs):
        return self.call('get_electrical_distance_units', kwargs=kwargs)

    def set_electrical_distance_units(self, **kwargs):
        return self.call('set_electrical_distance_units', kwargs=kwargs)

    def get_clock_source(self, **kwargs):
        return self.call('get_clock_source', kwargs=kwargs)

    def set_clock_source(self, **kwargs):
        return self.call('set_clock_source', kwargs=kwargs)

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

    def get_number_of_points(self, **kwargs):
        return self.call('get_number_of_points', kwargs=kwargs)

    def set_number_of_points(self, **kwargs):
        return self.call('set_number_of_points', kwargs=kwargs)

    def get_number_of_traces(self, **kwargs):
        return self.call('get_number_of_traces', kwargs=kwargs)

    def set_number_of_traces(self, **kwargs):
        return self.call('set_number_of_traces', kwargs=kwargs)

    def get_trigger_source(self, **kwargs):
        return self.call('get_trigger_source', kwargs=kwargs)

    def set_trigger_source(self, **kwargs):
        return self.call('set_trigger_source', kwargs=kwargs)

    def get_data_transfer_format(self, **kwargs):
        return self.call('get_data_transfer_format', kwargs=kwargs)

    def set_data_transfer_format(self, **kwargs):
        return self.call('set_data_transfer_format', kwargs=kwargs)

    def get_s11(self, **kwargs):
        return self.call('get_s11', kwargs=kwargs)

    def get_s12(self, **kwargs):
        return self.call('get_s12', kwargs=kwargs)

    def get_s21(self, **kwargs):
        return self.call('get_s21', kwargs=kwargs)

    def get_s22(self, **kwargs):
        return self.call('get_s22', kwargs=kwargs)

    def get_point_s11(self, **kwargs):
        return self.call('get_point_s11', kwargs=kwargs)

    def get_point_s12(self, **kwargs):
        return self.call('get_point_s12', kwargs=kwargs)

    def get_point_s21(self, **kwargs):
        return self.call('get_point_s21', kwargs=kwargs)

    def get_point_s22(self, **kwargs):
        return self.call('get_point_s22', kwargs=kwargs)

    def get_point_s11_iq(self, **kwargs):
        return self.call('get_point_s11_iq', kwargs=kwargs)

    def get_point_s12_iq(self, **kwargs):
        return self.call('get_point_s12_iq', kwargs=kwargs)

    def get_point_s21_iq(self, **kwargs):
        return self.call('get_point_s21_iq', kwargs=kwargs)

    def get_point_s22_iq(self, **kwargs):
        return self.call('get_point_s22_iq', kwargs=kwargs)

    def get_point_check_sweep_first(self, **kwargs):
        return self.call('get_point_check_sweep_first', kwargs=kwargs)

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

