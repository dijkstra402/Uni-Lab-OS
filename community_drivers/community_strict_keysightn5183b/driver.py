from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictKeysightn5183b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/Keysight/Keysight_N5183B.py', 'class_name': 'KeysightN5183B', 'import_roots': ['src'], 'candidate_methods': ['get_idn', 'get_power', 'set_power', 'get_frequency', 'set_frequency', 'get_phase_offset', 'set_phase_offset', 'get_auto_freq_ref', 'set_auto_freq_ref', 'get_rf_output', 'set_rf_output', 'get_pulse_modulation', 'set_pulse_modulation', 'get_pulse_modulation_source', 'set_pulse_modulation_source', 'address', 'resource_manager', 'visa_handle', 'visabackend', 'visalib', 'set_address', 'device_clear', 'set_terminator', 'close', 'write_raw', 'ask_raw', 'snapshot_base', 'get_timeout', 'set_timeout', 'connect_message', 'close_all', 'record_instance', 'instances', 'remove_instance', 'find_instrument', 'exist', 'is_valid', 'label', 'add_parameter', 'remove_parameter', 'add_function', 'add_submodule', 'get_component', 'print_readable_snapshot', 'invalidate_cache', 'parent', 'ancestors', 'root_instrument', 'name_parts', 'full_name', 'name', 'short_name', 'set', 'get', 'call', 'validate_status', 'load_metadata', 'snapshot'], 'action_targets': {'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power', 'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_phase_offset': '__qcodes_param_get__phase_offset', 'set_phase_offset': '__qcodes_param_set__phase_offset', 'get_auto_freq_ref': '__qcodes_param_get__auto_freq_ref', 'set_auto_freq_ref': '__qcodes_param_set__auto_freq_ref', 'get_rf_output': '__qcodes_param_get__rf_output', 'set_rf_output': '__qcodes_param_set__rf_output', 'get_pulse_modulation': '__qcodes_param_get__pulse_modulation', 'set_pulse_modulation': '__qcodes_param_set__pulse_modulation', 'get_pulse_modulation_source': '__qcodes_param_get__pulse_modulation_source', 'set_pulse_modulation_source': '__qcodes_param_set__pulse_modulation_source', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout'}, 'metadata': {'repo': 'QCoDeS/Qcodes', 'repo_url': 'https://github.com/QCoDeS/Qcodes', 'source_url': 'https://github.com/QCoDeS/Qcodes/blob/main/src/qcodes/instrument_drivers/Keysight/Keysight_N5183B.py', 'confidence': 0.95, 'quality_score': 1.17, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power', 'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_phase_offset': '__qcodes_param_get__phase_offset', 'set_phase_offset': '__qcodes_param_set__phase_offset', 'get_auto_freq_ref': '__qcodes_param_get__auto_freq_ref', 'set_auto_freq_ref': '__qcodes_param_set__auto_freq_ref', 'get_rf_output': '__qcodes_param_get__rf_output', 'set_rf_output': '__qcodes_param_set__rf_output', 'get_pulse_modulation': '__qcodes_param_get__pulse_modulation', 'set_pulse_modulation': '__qcodes_param_set__pulse_modulation', 'get_pulse_modulation_source': '__qcodes_param_get__pulse_modulation_source', 'set_pulse_modulation_source': '__qcodes_param_set__pulse_modulation_source', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def get_power(self, **kwargs):
        return self.call('get_power', kwargs=kwargs)

    def set_power(self, **kwargs):
        return self.call('set_power', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def get_phase_offset(self, **kwargs):
        return self.call('get_phase_offset', kwargs=kwargs)

    def set_phase_offset(self, **kwargs):
        return self.call('set_phase_offset', kwargs=kwargs)

    def get_auto_freq_ref(self, **kwargs):
        return self.call('get_auto_freq_ref', kwargs=kwargs)

    def set_auto_freq_ref(self, **kwargs):
        return self.call('set_auto_freq_ref', kwargs=kwargs)

    def get_rf_output(self, **kwargs):
        return self.call('get_rf_output', kwargs=kwargs)

    def set_rf_output(self, **kwargs):
        return self.call('set_rf_output', kwargs=kwargs)

    def get_pulse_modulation(self, **kwargs):
        return self.call('get_pulse_modulation', kwargs=kwargs)

    def set_pulse_modulation(self, **kwargs):
        return self.call('set_pulse_modulation', kwargs=kwargs)

    def get_pulse_modulation_source(self, **kwargs):
        return self.call('get_pulse_modulation_source', kwargs=kwargs)

    def set_pulse_modulation_source(self, **kwargs):
        return self.call('set_pulse_modulation_source', kwargs=kwargs)

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

