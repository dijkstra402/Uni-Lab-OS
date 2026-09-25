from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictSg384(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/stanford_research/SG384.py', 'class_name': 'SG384', 'import_roots': ['src'], 'candidate_methods': ['get_frequency', 'set_frequency', 'get_phase', 'set_phase', 'get_amplitude_lf', 'set_amplitude_lf', 'get_amplitude_rf', 'set_amplitude_rf', 'get_amplitude_hf', 'set_amplitude_hf', 'get_amplitude_clock', 'set_amplitude_clock', 'get_noise_mode', 'set_noise_mode', 'get_enable_rf', 'set_enable_rf', 'get_enable_lf', 'set_enable_lf', 'get_enable_hf', 'set_enable_hf', 'get_enable_clock', 'set_enable_clock', 'get_offset_clock', 'set_offset_clock', 'get_offset_reardc', 'set_offset_reardc', 'get_offset_bnc', 'set_offset_bnc', 'get_modulation_coupling', 'set_modulation_coupling', 'get_fm_deviation', 'set_fm_deviation', 'get_modulation_function', 'set_modulation_function', 'get_enable_modulation', 'set_enable_modulation', 'get_modulation_rate', 'set_modulation_rate', 'get_modulation_type', 'set_modulation_type', 'address', 'resource_manager', 'visa_handle', 'visabackend', 'visalib', 'set_address', 'device_clear', 'set_terminator', 'close', 'write_raw', 'ask_raw', 'snapshot_base', 'get_timeout', 'set_timeout', 'get_idn', 'connect_message', 'close_all', 'record_instance', 'instances', 'remove_instance', 'find_instrument', 'exist', 'is_valid', 'label', 'add_parameter', 'remove_parameter', 'add_function', 'add_submodule', 'get_component', 'print_readable_snapshot', 'invalidate_cache', 'parent', 'ancestors', 'root_instrument', 'name_parts', 'full_name', 'name', 'short_name', 'set', 'get', 'call', 'validate_status', 'load_metadata', 'snapshot'], 'action_targets': {'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_phase': '__qcodes_param_get__phase', 'set_phase': '__qcodes_param_set__phase', 'get_amplitude_lf': '__qcodes_param_get__amplitude_lf', 'set_amplitude_lf': '__qcodes_param_set__amplitude_lf', 'get_amplitude_rf': '__qcodes_param_get__amplitude_rf', 'set_amplitude_rf': '__qcodes_param_set__amplitude_rf', 'get_amplitude_hf': '__qcodes_param_get__amplitude_hf', 'set_amplitude_hf': '__qcodes_param_set__amplitude_hf', 'get_amplitude_clock': '__qcodes_param_get__amplitude_clock', 'set_amplitude_clock': '__qcodes_param_set__amplitude_clock', 'get_noise_mode': '__qcodes_param_get__noise_mode', 'set_noise_mode': '__qcodes_param_set__noise_mode', 'get_enable_rf': '__qcodes_param_get__enable_rf', 'set_enable_rf': '__qcodes_param_set__enable_rf', 'get_enable_lf': '__qcodes_param_get__enable_lf', 'set_enable_lf': '__qcodes_param_set__enable_lf', 'get_enable_hf': '__qcodes_param_get__enable_hf', 'set_enable_hf': '__qcodes_param_set__enable_hf', 'get_enable_clock': '__qcodes_param_get__enable_clock', 'set_enable_clock': '__qcodes_param_set__enable_clock', 'get_offset_clock': '__qcodes_param_get__offset_clock', 'set_offset_clock': '__qcodes_param_set__offset_clock', 'get_offset_reardc': '__qcodes_param_get__offset_reardc', 'set_offset_reardc': '__qcodes_param_set__offset_reardc', 'get_offset_bnc': '__qcodes_param_get__offset_bnc', 'set_offset_bnc': '__qcodes_param_set__offset_bnc', 'get_modulation_coupling': '__qcodes_param_get__modulation_coupling', 'set_modulation_coupling': '__qcodes_param_set__modulation_coupling', 'get_fm_deviation': '__qcodes_param_get__fm_deviation', 'set_fm_deviation': '__qcodes_param_set__fm_deviation', 'get_modulation_function': '__qcodes_param_get__modulation_function', 'set_modulation_function': '__qcodes_param_set__modulation_function', 'get_enable_modulation': '__qcodes_param_get__enable_modulation', 'set_enable_modulation': '__qcodes_param_set__enable_modulation', 'get_modulation_rate': '__qcodes_param_get__modulation_rate', 'set_modulation_rate': '__qcodes_param_set__modulation_rate', 'get_modulation_type': '__qcodes_param_get__modulation_type', 'set_modulation_type': '__qcodes_param_set__modulation_type', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}, 'metadata': {'repo': 'QCoDeS/Qcodes', 'repo_url': 'https://github.com/QCoDeS/Qcodes', 'source_url': 'https://github.com/QCoDeS/Qcodes/blob/main/src/qcodes/instrument_drivers/stanford_research/SG384.py', 'confidence': 0.95, 'quality_score': 1.17, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_phase': '__qcodes_param_get__phase', 'set_phase': '__qcodes_param_set__phase', 'get_amplitude_lf': '__qcodes_param_get__amplitude_lf', 'set_amplitude_lf': '__qcodes_param_set__amplitude_lf', 'get_amplitude_rf': '__qcodes_param_get__amplitude_rf', 'set_amplitude_rf': '__qcodes_param_set__amplitude_rf', 'get_amplitude_hf': '__qcodes_param_get__amplitude_hf', 'set_amplitude_hf': '__qcodes_param_set__amplitude_hf', 'get_amplitude_clock': '__qcodes_param_get__amplitude_clock', 'set_amplitude_clock': '__qcodes_param_set__amplitude_clock', 'get_noise_mode': '__qcodes_param_get__noise_mode', 'set_noise_mode': '__qcodes_param_set__noise_mode', 'get_enable_rf': '__qcodes_param_get__enable_rf', 'set_enable_rf': '__qcodes_param_set__enable_rf', 'get_enable_lf': '__qcodes_param_get__enable_lf', 'set_enable_lf': '__qcodes_param_set__enable_lf', 'get_enable_hf': '__qcodes_param_get__enable_hf', 'set_enable_hf': '__qcodes_param_set__enable_hf', 'get_enable_clock': '__qcodes_param_get__enable_clock', 'set_enable_clock': '__qcodes_param_set__enable_clock', 'get_offset_clock': '__qcodes_param_get__offset_clock', 'set_offset_clock': '__qcodes_param_set__offset_clock', 'get_offset_reardc': '__qcodes_param_get__offset_reardc', 'set_offset_reardc': '__qcodes_param_set__offset_reardc', 'get_offset_bnc': '__qcodes_param_get__offset_bnc', 'set_offset_bnc': '__qcodes_param_set__offset_bnc', 'get_modulation_coupling': '__qcodes_param_get__modulation_coupling', 'set_modulation_coupling': '__qcodes_param_set__modulation_coupling', 'get_fm_deviation': '__qcodes_param_get__fm_deviation', 'set_fm_deviation': '__qcodes_param_set__fm_deviation', 'get_modulation_function': '__qcodes_param_get__modulation_function', 'set_modulation_function': '__qcodes_param_set__modulation_function', 'get_enable_modulation': '__qcodes_param_get__enable_modulation', 'set_enable_modulation': '__qcodes_param_set__enable_modulation', 'get_modulation_rate': '__qcodes_param_get__modulation_rate', 'set_modulation_rate': '__qcodes_param_set__modulation_rate', 'get_modulation_type': '__qcodes_param_get__modulation_type', 'set_modulation_type': '__qcodes_param_set__modulation_type', 'get_timeout': '__qcodes_param_get__timeout', 'set_timeout': '__qcodes_param_set__timeout', 'get_idn': '__qcodes_param_get__idn'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def get_phase(self, **kwargs):
        return self.call('get_phase', kwargs=kwargs)

    def set_phase(self, **kwargs):
        return self.call('set_phase', kwargs=kwargs)

    def get_amplitude_lf(self, **kwargs):
        return self.call('get_amplitude_lf', kwargs=kwargs)

    def set_amplitude_lf(self, **kwargs):
        return self.call('set_amplitude_lf', kwargs=kwargs)

    def get_amplitude_rf(self, **kwargs):
        return self.call('get_amplitude_rf', kwargs=kwargs)

    def set_amplitude_rf(self, **kwargs):
        return self.call('set_amplitude_rf', kwargs=kwargs)

    def get_amplitude_hf(self, **kwargs):
        return self.call('get_amplitude_hf', kwargs=kwargs)

    def set_amplitude_hf(self, **kwargs):
        return self.call('set_amplitude_hf', kwargs=kwargs)

    def get_amplitude_clock(self, **kwargs):
        return self.call('get_amplitude_clock', kwargs=kwargs)

    def set_amplitude_clock(self, **kwargs):
        return self.call('set_amplitude_clock', kwargs=kwargs)

    def get_noise_mode(self, **kwargs):
        return self.call('get_noise_mode', kwargs=kwargs)

    def set_noise_mode(self, **kwargs):
        return self.call('set_noise_mode', kwargs=kwargs)

    def get_enable_rf(self, **kwargs):
        return self.call('get_enable_rf', kwargs=kwargs)

    def set_enable_rf(self, **kwargs):
        return self.call('set_enable_rf', kwargs=kwargs)

    def get_enable_lf(self, **kwargs):
        return self.call('get_enable_lf', kwargs=kwargs)

    def set_enable_lf(self, **kwargs):
        return self.call('set_enable_lf', kwargs=kwargs)

    def get_enable_hf(self, **kwargs):
        return self.call('get_enable_hf', kwargs=kwargs)

    def set_enable_hf(self, **kwargs):
        return self.call('set_enable_hf', kwargs=kwargs)

    def get_enable_clock(self, **kwargs):
        return self.call('get_enable_clock', kwargs=kwargs)

    def set_enable_clock(self, **kwargs):
        return self.call('set_enable_clock', kwargs=kwargs)

    def get_offset_clock(self, **kwargs):
        return self.call('get_offset_clock', kwargs=kwargs)

    def set_offset_clock(self, **kwargs):
        return self.call('set_offset_clock', kwargs=kwargs)

    def get_offset_reardc(self, **kwargs):
        return self.call('get_offset_reardc', kwargs=kwargs)

    def set_offset_reardc(self, **kwargs):
        return self.call('set_offset_reardc', kwargs=kwargs)

    def get_offset_bnc(self, **kwargs):
        return self.call('get_offset_bnc', kwargs=kwargs)

    def set_offset_bnc(self, **kwargs):
        return self.call('set_offset_bnc', kwargs=kwargs)

    def get_modulation_coupling(self, **kwargs):
        return self.call('get_modulation_coupling', kwargs=kwargs)

    def set_modulation_coupling(self, **kwargs):
        return self.call('set_modulation_coupling', kwargs=kwargs)

    def get_fm_deviation(self, **kwargs):
        return self.call('get_fm_deviation', kwargs=kwargs)

    def set_fm_deviation(self, **kwargs):
        return self.call('set_fm_deviation', kwargs=kwargs)

    def get_modulation_function(self, **kwargs):
        return self.call('get_modulation_function', kwargs=kwargs)

    def set_modulation_function(self, **kwargs):
        return self.call('set_modulation_function', kwargs=kwargs)

    def get_enable_modulation(self, **kwargs):
        return self.call('get_enable_modulation', kwargs=kwargs)

    def set_enable_modulation(self, **kwargs):
        return self.call('set_enable_modulation', kwargs=kwargs)

    def get_modulation_rate(self, **kwargs):
        return self.call('get_modulation_rate', kwargs=kwargs)

    def set_modulation_rate(self, **kwargs):
        return self.call('set_modulation_rate', kwargs=kwargs)

    def get_modulation_type(self, **kwargs):
        return self.call('get_modulation_type', kwargs=kwargs)

    def set_modulation_type(self, **kwargs):
        return self.call('set_modulation_type', kwargs=kwargs)

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

