from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAwg70002a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/tektronix/AWG70002A.py', 'class_name': 'TektronixAWG70002A', 'import_roots': ['src'], 'candidate_methods': ['set_event_jump', 'force_triggerA', 'force_triggerB', 'wait_for_operation_to_complete', 'play', 'stop', 'sequenceList', 'waveformList', 'delete_sequence_from_list', 'clearSequenceList', 'clearWaveformList', 'makeWFMXFile', 'sendSEQXFile', 'sendWFMXFile', 'loadWFMXFile', 'loadSEQXFile', 'make_SEQX_from_forged_sequence', 'makeSEQXFile', 'get_current_directory', 'set_current_directory', 'get_mode', 'set_mode', 'get_sample_rate', 'set_sample_rate', 'get_clock_source', 'set_clock_source', 'get_clock_external_frequency', 'set_clock_external_frequency', 'get_run_state', 'get_all_output_off', 'set_all_output_off', 'get_force_jump', 'set_force_jump', 'address', 'resource_manager', 'visa_handle', 'visabackend', 'visalib', 'set_address', 'device_clear', 'set_terminator', 'close', 'write_raw', 'ask_raw', 'snapshot_base', 'get_timeout', 'set_timeout', 'get_idn', 'connect_message', 'close_all', 'record_instance', 'instances', 'remove_instance', 'find_instrument', 'exist', 'is_valid', 'label', 'add_parameter', 'remove_parameter', 'add_function', 'add_submodule', 'get_component', 'print_readable_snapshot', 'invalidate_cache', 'parent', 'ancestors', 'root_instrument', 'name_parts', 'full_name', 'name', 'short_name', 'set', 'get', 'call', 'validate_status', 'load_metadata', 'snapshot'], 'action_targets': {'get_current_directory': '__qcodes_param_get__current_directory', 'set_current_directory': '__qcodes_param_set__current_directory', 'get_mode': '__qcodes_param_get__mode', 'set_mode': '__qcodes_param_set__mode', 'get_sample_rate': '__qcodes_param_get__sample_rate', 'set_sample_rate': '__qcodes_param_set__sample_rate', 'get_clock_source': '__qcodes_param_get__clock_source', 'set_clock_source': '__qcodes_param_set__clock_source', 'get_clock_external_frequency': '__qcodes_param_get__clock_external_frequency', 'set_clock_external_frequency': '__qcodes_param_set__clock_external_frequency', 'get_run_state': '__qcodes_param_get__run_state', 'get_all_output_off': '__qcodes_param_get__all_output_off', 'set_all_output_off': '__qcodes_param_set__all_output_off', 'get_force_jump': '__qcodes_param_get__force_jump', 'set_force_jump': '__qcodes_param_set__force_jump', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}, 'metadata': {'repo': 'QCoDeS/Qcodes', 'repo_url': 'https://github.com/QCoDeS/Qcodes', 'source_url': 'https://github.com/QCoDeS/Qcodes/blob/main/src/qcodes/instrument_drivers/tektronix/AWG70002A.py', 'confidence': 0.95, 'quality_score': 1.17, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_current_directory': '__qcodes_param_get__current_directory', 'set_current_directory': '__qcodes_param_set__current_directory', 'get_mode': '__qcodes_param_get__mode', 'set_mode': '__qcodes_param_set__mode', 'get_sample_rate': '__qcodes_param_get__sample_rate', 'set_sample_rate': '__qcodes_param_set__sample_rate', 'get_clock_source': '__qcodes_param_get__clock_source', 'set_clock_source': '__qcodes_param_set__clock_source', 'get_clock_external_frequency': '__qcodes_param_get__clock_external_frequency', 'set_clock_external_frequency': '__qcodes_param_set__clock_external_frequency', 'get_run_state': '__qcodes_param_get__run_state', 'get_all_output_off': '__qcodes_param_get__all_output_off', 'set_all_output_off': '__qcodes_param_set__all_output_off', 'get_force_jump': '__qcodes_param_get__force_jump', 'set_force_jump': '__qcodes_param_set__force_jump', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def set_event_jump(self, **kwargs):
        return self.call('set_event_jump', kwargs=kwargs)

    def force_triggerA(self, **kwargs):
        return self.call('force_triggerA', kwargs=kwargs)

    def force_triggerB(self, **kwargs):
        return self.call('force_triggerB', kwargs=kwargs)

    def wait_for_operation_to_complete(self, **kwargs):
        return self.call('wait_for_operation_to_complete', kwargs=kwargs)

    def play(self, **kwargs):
        return self.call('play', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def sequenceList(self, **kwargs):
        return self.call('sequenceList', kwargs=kwargs)

    def waveformList(self, **kwargs):
        return self.call('waveformList', kwargs=kwargs)

    def delete_sequence_from_list(self, **kwargs):
        return self.call('delete_sequence_from_list', kwargs=kwargs)

    def clearSequenceList(self, **kwargs):
        return self.call('clearSequenceList', kwargs=kwargs)

    def clearWaveformList(self, **kwargs):
        return self.call('clearWaveformList', kwargs=kwargs)

    def makeWFMXFile(self, **kwargs):
        return self.call('makeWFMXFile', kwargs=kwargs)

    def sendSEQXFile(self, **kwargs):
        return self.call('sendSEQXFile', kwargs=kwargs)

    def sendWFMXFile(self, **kwargs):
        return self.call('sendWFMXFile', kwargs=kwargs)

    def loadWFMXFile(self, **kwargs):
        return self.call('loadWFMXFile', kwargs=kwargs)

    def loadSEQXFile(self, **kwargs):
        return self.call('loadSEQXFile', kwargs=kwargs)

    def make_SEQX_from_forged_sequence(self, **kwargs):
        return self.call('make_SEQX_from_forged_sequence', kwargs=kwargs)

    def makeSEQXFile(self, **kwargs):
        return self.call('makeSEQXFile', kwargs=kwargs)

    def get_current_directory(self, **kwargs):
        return self.call('get_current_directory', kwargs=kwargs)

    def set_current_directory(self, **kwargs):
        return self.call('set_current_directory', kwargs=kwargs)

    def get_mode(self, **kwargs):
        return self.call('get_mode', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def get_sample_rate(self, **kwargs):
        return self.call('get_sample_rate', kwargs=kwargs)

    def set_sample_rate(self, **kwargs):
        return self.call('set_sample_rate', kwargs=kwargs)

    def get_clock_source(self, **kwargs):
        return self.call('get_clock_source', kwargs=kwargs)

    def set_clock_source(self, **kwargs):
        return self.call('set_clock_source', kwargs=kwargs)

    def get_clock_external_frequency(self, **kwargs):
        return self.call('get_clock_external_frequency', kwargs=kwargs)

    def set_clock_external_frequency(self, **kwargs):
        return self.call('set_clock_external_frequency', kwargs=kwargs)

    def get_run_state(self, **kwargs):
        return self.call('get_run_state', kwargs=kwargs)

    def get_all_output_off(self, **kwargs):
        return self.call('get_all_output_off', kwargs=kwargs)

    def set_all_output_off(self, **kwargs):
        return self.call('set_all_output_off', kwargs=kwargs)

    def get_force_jump(self, **kwargs):
        return self.call('get_force_jump', kwargs=kwargs)

    def set_force_jump(self, **kwargs):
        return self.call('set_force_jump', kwargs=kwargs)

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

