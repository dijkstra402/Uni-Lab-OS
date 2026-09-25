from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictKeysightb2201(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/Keysight/keysight_b220x.py', 'class_name': 'KeysightB220X', 'import_roots': ['src'], 'candidate_methods': ['connect', 'connect_paths', 'disconnect_paths', 'disconnect', 'disconnect_all', 'bias_disable_all_outputs', 'bias_enable_all_outputs', 'bias_enable_output', 'bias_disable_output', 'gnd_enable_output', 'gnd_disable_output', 'gnd_enable_all_outputs', 'gnd_disable_all_outputs', 'couple_port_autodetect', 'clear_status', 'reset', 'parse_channel_list', 'to_channel_list', 'get_get_status', 'get_get_error', 'get_connections', 'get_connection_rule', 'set_connection_rule', 'get_connection_sequence', 'set_connection_sequence', 'get_bias_input_port', 'set_bias_input_port', 'get_bias_mode', 'set_bias_mode', 'get_gnd_input_port', 'set_gnd_input_port', 'get_gnd_mode', 'set_gnd_mode', 'get_unused_inputs', 'set_unused_inputs', 'get_couple_ports', 'set_couple_ports', 'get_couple_mode', 'set_couple_mode', 'address', 'resource_manager', 'visa_handle', 'visabackend', 'visalib', 'set_address', 'device_clear', 'set_terminator', 'close', 'write_raw', 'ask_raw', 'snapshot_base', 'get_timeout', 'set_timeout', 'get_idn', 'connect_message', 'close_all', 'record_instance', 'instances', 'remove_instance', 'find_instrument', 'exist', 'is_valid', 'label', 'add_parameter', 'remove_parameter', 'add_function', 'add_submodule', 'get_component', 'print_readable_snapshot', 'invalidate_cache', 'parent', 'ancestors', 'root_instrument', 'name_parts', 'full_name', 'name', 'short_name', 'set', 'get', 'call', 'validate_status', 'load_metadata', 'snapshot'], 'action_targets': {'get_get_status': '__qcodes_param_get__get_status', 'get_get_error': '__qcodes_param_get__get_error', 'get_connections': '__qcodes_param_get__connections', 'get_connection_rule': '__qcodes_param_get__connection_rule', 'set_connection_rule': '__qcodes_param_set__connection_rule', 'get_connection_sequence': '__qcodes_param_get__connection_sequence', 'set_connection_sequence': '__qcodes_param_set__connection_sequence', 'get_bias_input_port': '__qcodes_param_get__bias_input_port', 'set_bias_input_port': '__qcodes_param_set__bias_input_port', 'get_bias_mode': '__qcodes_param_get__bias_mode', 'set_bias_mode': '__qcodes_param_set__bias_mode', 'get_gnd_input_port': '__qcodes_param_get__gnd_input_port', 'set_gnd_input_port': '__qcodes_param_set__gnd_input_port', 'get_gnd_mode': '__qcodes_param_get__gnd_mode', 'set_gnd_mode': '__qcodes_param_set__gnd_mode', 'get_unused_inputs': '__qcodes_param_get__unused_inputs', 'set_unused_inputs': '__qcodes_param_set__unused_inputs', 'get_couple_ports': '__qcodes_param_get__couple_ports', 'set_couple_ports': '__qcodes_param_set__couple_ports', 'get_couple_mode': '__qcodes_param_get__couple_mode', 'set_couple_mode': '__qcodes_param_set__couple_mode', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}, 'metadata': {'repo': 'QCoDeS/Qcodes', 'repo_url': 'https://github.com/QCoDeS/Qcodes', 'source_url': 'https://github.com/QCoDeS/Qcodes/blob/main/src/qcodes/instrument_drivers/Keysight/keysight_b220x.py', 'confidence': 0.95, 'quality_score': 1.17, 'parse_status': 'class_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_get_status': '__qcodes_param_get__get_status', 'get_get_error': '__qcodes_param_get__get_error', 'get_connections': '__qcodes_param_get__connections', 'get_connection_rule': '__qcodes_param_get__connection_rule', 'set_connection_rule': '__qcodes_param_set__connection_rule', 'get_connection_sequence': '__qcodes_param_get__connection_sequence', 'set_connection_sequence': '__qcodes_param_set__connection_sequence', 'get_bias_input_port': '__qcodes_param_get__bias_input_port', 'set_bias_input_port': '__qcodes_param_set__bias_input_port', 'get_bias_mode': '__qcodes_param_get__bias_mode', 'set_bias_mode': '__qcodes_param_set__bias_mode', 'get_gnd_input_port': '__qcodes_param_get__gnd_input_port', 'set_gnd_input_port': '__qcodes_param_set__gnd_input_port', 'get_gnd_mode': '__qcodes_param_get__gnd_mode', 'set_gnd_mode': '__qcodes_param_set__gnd_mode', 'get_unused_inputs': '__qcodes_param_get__unused_inputs', 'set_unused_inputs': '__qcodes_param_set__unused_inputs', 'get_couple_ports': '__qcodes_param_get__couple_ports', 'set_couple_ports': '__qcodes_param_set__couple_ports', 'get_couple_mode': '__qcodes_param_get__couple_mode', 'set_couple_mode': '__qcodes_param_set__couple_mode', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def connect_paths(self, **kwargs):
        return self.call('connect_paths', kwargs=kwargs)

    def disconnect_paths(self, **kwargs):
        return self.call('disconnect_paths', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def disconnect_all(self, **kwargs):
        return self.call('disconnect_all', kwargs=kwargs)

    def bias_disable_all_outputs(self, **kwargs):
        return self.call('bias_disable_all_outputs', kwargs=kwargs)

    def bias_enable_all_outputs(self, **kwargs):
        return self.call('bias_enable_all_outputs', kwargs=kwargs)

    def bias_enable_output(self, **kwargs):
        return self.call('bias_enable_output', kwargs=kwargs)

    def bias_disable_output(self, **kwargs):
        return self.call('bias_disable_output', kwargs=kwargs)

    def gnd_enable_output(self, **kwargs):
        return self.call('gnd_enable_output', kwargs=kwargs)

    def gnd_disable_output(self, **kwargs):
        return self.call('gnd_disable_output', kwargs=kwargs)

    def gnd_enable_all_outputs(self, **kwargs):
        return self.call('gnd_enable_all_outputs', kwargs=kwargs)

    def gnd_disable_all_outputs(self, **kwargs):
        return self.call('gnd_disable_all_outputs', kwargs=kwargs)

    def couple_port_autodetect(self, **kwargs):
        return self.call('couple_port_autodetect', kwargs=kwargs)

    def clear_status(self, **kwargs):
        return self.call('clear_status', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def parse_channel_list(self, **kwargs):
        return self.call('parse_channel_list', kwargs=kwargs)

    def to_channel_list(self, **kwargs):
        return self.call('to_channel_list', kwargs=kwargs)

    def get_get_status(self, **kwargs):
        return self.call('get_get_status', kwargs=kwargs)

    def get_get_error(self, **kwargs):
        return self.call('get_get_error', kwargs=kwargs)

    def get_connections(self, **kwargs):
        return self.call('get_connections', kwargs=kwargs)

    def get_connection_rule(self, **kwargs):
        return self.call('get_connection_rule', kwargs=kwargs)

    def set_connection_rule(self, **kwargs):
        return self.call('set_connection_rule', kwargs=kwargs)

    def get_connection_sequence(self, **kwargs):
        return self.call('get_connection_sequence', kwargs=kwargs)

    def set_connection_sequence(self, **kwargs):
        return self.call('set_connection_sequence', kwargs=kwargs)

    def get_bias_input_port(self, **kwargs):
        return self.call('get_bias_input_port', kwargs=kwargs)

    def set_bias_input_port(self, **kwargs):
        return self.call('set_bias_input_port', kwargs=kwargs)

    def get_bias_mode(self, **kwargs):
        return self.call('get_bias_mode', kwargs=kwargs)

    def set_bias_mode(self, **kwargs):
        return self.call('set_bias_mode', kwargs=kwargs)

    def get_gnd_input_port(self, **kwargs):
        return self.call('get_gnd_input_port', kwargs=kwargs)

    def set_gnd_input_port(self, **kwargs):
        return self.call('set_gnd_input_port', kwargs=kwargs)

    def get_gnd_mode(self, **kwargs):
        return self.call('get_gnd_mode', kwargs=kwargs)

    def set_gnd_mode(self, **kwargs):
        return self.call('set_gnd_mode', kwargs=kwargs)

    def get_unused_inputs(self, **kwargs):
        return self.call('get_unused_inputs', kwargs=kwargs)

    def set_unused_inputs(self, **kwargs):
        return self.call('set_unused_inputs', kwargs=kwargs)

    def get_couple_ports(self, **kwargs):
        return self.call('get_couple_ports', kwargs=kwargs)

    def set_couple_ports(self, **kwargs):
        return self.call('set_couple_ports', kwargs=kwargs)

    def get_couple_mode(self, **kwargs):
        return self.call('get_couple_mode', kwargs=kwargs)

    def set_couple_mode(self, **kwargs):
        return self.call('set_couple_mode', kwargs=kwargs)

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

