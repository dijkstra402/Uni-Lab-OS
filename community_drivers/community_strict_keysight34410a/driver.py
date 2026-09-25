from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictKeysight34410a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/Keysight/Keysight_34410A_submodules.py', 'class_name': 'Keysight34410A', 'import_roots': ['src'], 'candidate_methods': ['init_measurement', 'abort_measurement', 'fetch', 'autorange_once', 'increase_range', 'decrease_range', 'get_sense_function', 'set_sense_function', 'get_line_frequency', 'set_line_frequency', 'get_nplc', 'set_nplc', 'get_range', 'set_range', 'get_resolution', 'set_resolution', 'get_autorange', 'set_autorange', 'get_autozero', 'set_autozero', 'get_volt', 'get_curr', 'get_ac_volt', 'get_ac_curr', 'get_res', 'get_four_wire_res', 'get_time_axis', 'get_timetrace', 'get_aperture_mode', 'set_aperture_mode', 'get_aperture_time', 'set_aperture_time', 'error', 'flush_error_queue', 'address', 'resource_manager', 'visa_handle', 'visabackend', 'visalib', 'set_address', 'device_clear', 'set_terminator', 'close', 'write_raw', 'ask_raw', 'snapshot_base', 'get_timeout', 'set_timeout', 'get_idn', 'connect_message', 'close_all', 'record_instance', 'instances', 'remove_instance', 'find_instrument', 'exist', 'is_valid', 'label', 'add_parameter', 'remove_parameter', 'add_function', 'add_submodule', 'get_component', 'print_readable_snapshot', 'invalidate_cache', 'parent', 'ancestors', 'root_instrument', 'name_parts', 'full_name', 'name', 'short_name', 'set', 'get', 'call', 'validate_status', 'load_metadata', 'snapshot'], 'action_targets': {'get_sense_function': '__qcodes_param_get__sense_function', 'set_sense_function': '__qcodes_param_set__sense_function', 'get_line_frequency': '__qcodes_param_get__line_frequency', 'set_line_frequency': '__qcodes_param_set__line_frequency', 'get_nplc': '__qcodes_param_get__nplc', 'set_nplc': '__qcodes_param_set__nplc', 'get_range': '__qcodes_param_get__range', 'set_range': '__qcodes_param_set__range', 'get_resolution': '__qcodes_param_get__resolution', 'set_resolution': '__qcodes_param_set__resolution', 'get_autorange': '__qcodes_param_get__autorange', 'set_autorange': '__qcodes_param_set__autorange', 'get_autozero': '__qcodes_param_get__autozero', 'set_autozero': '__qcodes_param_set__autozero', 'get_volt': '__qcodes_param_get__volt', 'get_curr': '__qcodes_param_get__curr', 'get_ac_volt': '__qcodes_param_get__ac_volt', 'get_ac_curr': '__qcodes_param_get__ac_curr', 'get_res': '__qcodes_param_get__res', 'get_four_wire_res': '__qcodes_param_get__four_wire_res', 'get_time_axis': '__qcodes_param_get__time_axis', 'get_timetrace': '__qcodes_param_get__timetrace', 'get_aperture_mode': '__qcodes_param_get__aperture_mode', 'set_aperture_mode': '__qcodes_param_set__aperture_mode', 'get_aperture_time': '__qcodes_param_get__aperture_time', 'set_aperture_time': '__qcodes_param_set__aperture_time', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}, 'metadata': {'repo': 'QCoDeS/Qcodes', 'repo_url': 'https://github.com/QCoDeS/Qcodes', 'source_url': 'https://github.com/QCoDeS/Qcodes/blob/main/src/qcodes/instrument_drivers/Keysight/Keysight_34410A_submodules.py', 'confidence': 0.95, 'quality_score': 1.17, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_sense_function': '__qcodes_param_get__sense_function', 'set_sense_function': '__qcodes_param_set__sense_function', 'get_line_frequency': '__qcodes_param_get__line_frequency', 'set_line_frequency': '__qcodes_param_set__line_frequency', 'get_nplc': '__qcodes_param_get__nplc', 'set_nplc': '__qcodes_param_set__nplc', 'get_range': '__qcodes_param_get__range', 'set_range': '__qcodes_param_set__range', 'get_resolution': '__qcodes_param_get__resolution', 'set_resolution': '__qcodes_param_set__resolution', 'get_autorange': '__qcodes_param_get__autorange', 'set_autorange': '__qcodes_param_set__autorange', 'get_autozero': '__qcodes_param_get__autozero', 'set_autozero': '__qcodes_param_set__autozero', 'get_volt': '__qcodes_param_get__volt', 'get_curr': '__qcodes_param_get__curr', 'get_ac_volt': '__qcodes_param_get__ac_volt', 'get_ac_curr': '__qcodes_param_get__ac_curr', 'get_res': '__qcodes_param_get__res', 'get_four_wire_res': '__qcodes_param_get__four_wire_res', 'get_time_axis': '__qcodes_param_get__time_axis', 'get_timetrace': '__qcodes_param_get__timetrace', 'get_aperture_mode': '__qcodes_param_get__aperture_mode', 'set_aperture_mode': '__qcodes_param_set__aperture_mode', 'get_aperture_time': '__qcodes_param_get__aperture_time', 'set_aperture_time': '__qcodes_param_set__aperture_time', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def init_measurement(self, **kwargs):
        return self.call('init_measurement', kwargs=kwargs)

    def abort_measurement(self, **kwargs):
        return self.call('abort_measurement', kwargs=kwargs)

    def fetch(self, **kwargs):
        return self.call('fetch', kwargs=kwargs)

    def autorange_once(self, **kwargs):
        return self.call('autorange_once', kwargs=kwargs)

    def increase_range(self, **kwargs):
        return self.call('increase_range', kwargs=kwargs)

    def decrease_range(self, **kwargs):
        return self.call('decrease_range', kwargs=kwargs)

    def get_sense_function(self, **kwargs):
        return self.call('get_sense_function', kwargs=kwargs)

    def set_sense_function(self, **kwargs):
        return self.call('set_sense_function', kwargs=kwargs)

    def get_line_frequency(self, **kwargs):
        return self.call('get_line_frequency', kwargs=kwargs)

    def set_line_frequency(self, **kwargs):
        return self.call('set_line_frequency', kwargs=kwargs)

    def get_nplc(self, **kwargs):
        return self.call('get_nplc', kwargs=kwargs)

    def set_nplc(self, **kwargs):
        return self.call('set_nplc', kwargs=kwargs)

    def get_range(self, **kwargs):
        return self.call('get_range', kwargs=kwargs)

    def set_range(self, **kwargs):
        return self.call('set_range', kwargs=kwargs)

    def get_resolution(self, **kwargs):
        return self.call('get_resolution', kwargs=kwargs)

    def set_resolution(self, **kwargs):
        return self.call('set_resolution', kwargs=kwargs)

    def get_autorange(self, **kwargs):
        return self.call('get_autorange', kwargs=kwargs)

    def set_autorange(self, **kwargs):
        return self.call('set_autorange', kwargs=kwargs)

    def get_autozero(self, **kwargs):
        return self.call('get_autozero', kwargs=kwargs)

    def set_autozero(self, **kwargs):
        return self.call('set_autozero', kwargs=kwargs)

    def get_volt(self, **kwargs):
        return self.call('get_volt', kwargs=kwargs)

    def get_curr(self, **kwargs):
        return self.call('get_curr', kwargs=kwargs)

    def get_ac_volt(self, **kwargs):
        return self.call('get_ac_volt', kwargs=kwargs)

    def get_ac_curr(self, **kwargs):
        return self.call('get_ac_curr', kwargs=kwargs)

    def get_res(self, **kwargs):
        return self.call('get_res', kwargs=kwargs)

    def get_four_wire_res(self, **kwargs):
        return self.call('get_four_wire_res', kwargs=kwargs)

    def get_time_axis(self, **kwargs):
        return self.call('get_time_axis', kwargs=kwargs)

    def get_timetrace(self, **kwargs):
        return self.call('get_timetrace', kwargs=kwargs)

    def get_aperture_mode(self, **kwargs):
        return self.call('get_aperture_mode', kwargs=kwargs)

    def set_aperture_mode(self, **kwargs):
        return self.call('set_aperture_mode', kwargs=kwargs)

    def get_aperture_time(self, **kwargs):
        return self.call('get_aperture_time', kwargs=kwargs)

    def set_aperture_time(self, **kwargs):
        return self.call('set_aperture_time', kwargs=kwargs)

    def error(self, **kwargs):
        return self.call('error', kwargs=kwargs)

    def flush_error_queue(self, **kwargs):
        return self.call('flush_error_queue', kwargs=kwargs)

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

