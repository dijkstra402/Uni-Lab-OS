from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictDataformattingfmt21(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilentB1500.py', 'class_name': 'AgilentB1500', 'import_roots': [], 'candidate_methods': ['smu_references', 'smu_names', 'query_learn', 'query_learn_header', 'query_modules', 'initialize_smu', 'initialize_all_smus', 'initialize_all_spgus', 'initialize_cmu', 'pause', 'abort', 'force_gnd', 'restore_settings', 'set_port_connection', 'check_errors', 'check_idle', 'clear_buffer', 'clear_timer', 'send_trigger', 'auto_calibration', 'data_format', 'parallel_meas', 'query_meas_settings', 'query_meas_mode', 'meas_mode', 'query_adc_setup', 'adc_setup', 'adc_averaging', 'adc_auto_zero', 'time_stamp', 'query_time_stamp_setting', 'wait_time', 'query_staircase_sweep_settings', 'sweep_timing', 'sweep_auto_abort', 'query_sampling_settings', 'sampling_mode', 'sampling_timing', 'sampling_auto_abort', 'read_data', 'read_channels', 'query_series_resistor', 'query_meas_range_current_auto', 'query_meas_op_mode', 'query_meas_ranges', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/agilent/agilentB1500.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'class_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def smu_references(self, **kwargs):
        return self.call('smu_references', kwargs=kwargs)

    def smu_names(self, **kwargs):
        return self.call('smu_names', kwargs=kwargs)

    def query_learn(self, **kwargs):
        return self.call('query_learn', kwargs=kwargs)

    def query_learn_header(self, **kwargs):
        return self.call('query_learn_header', kwargs=kwargs)

    def query_modules(self, **kwargs):
        return self.call('query_modules', kwargs=kwargs)

    def initialize_smu(self, **kwargs):
        return self.call('initialize_smu', kwargs=kwargs)

    def initialize_all_smus(self, **kwargs):
        return self.call('initialize_all_smus', kwargs=kwargs)

    def initialize_all_spgus(self, **kwargs):
        return self.call('initialize_all_spgus', kwargs=kwargs)

    def initialize_cmu(self, **kwargs):
        return self.call('initialize_cmu', kwargs=kwargs)

    def pause(self, **kwargs):
        return self.call('pause', kwargs=kwargs)

    def abort(self, **kwargs):
        return self.call('abort', kwargs=kwargs)

    def force_gnd(self, **kwargs):
        return self.call('force_gnd', kwargs=kwargs)

    def restore_settings(self, **kwargs):
        return self.call('restore_settings', kwargs=kwargs)

    def set_port_connection(self, **kwargs):
        return self.call('set_port_connection', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def check_idle(self, **kwargs):
        return self.call('check_idle', kwargs=kwargs)

    def clear_buffer(self, **kwargs):
        return self.call('clear_buffer', kwargs=kwargs)

    def clear_timer(self, **kwargs):
        return self.call('clear_timer', kwargs=kwargs)

    def send_trigger(self, **kwargs):
        return self.call('send_trigger', kwargs=kwargs)

    def auto_calibration(self, **kwargs):
        return self.call('auto_calibration', kwargs=kwargs)

    def data_format(self, **kwargs):
        return self.call('data_format', kwargs=kwargs)

    def parallel_meas(self, **kwargs):
        return self.call('parallel_meas', kwargs=kwargs)

    def query_meas_settings(self, **kwargs):
        return self.call('query_meas_settings', kwargs=kwargs)

    def query_meas_mode(self, **kwargs):
        return self.call('query_meas_mode', kwargs=kwargs)

    def meas_mode(self, **kwargs):
        return self.call('meas_mode', kwargs=kwargs)

    def query_adc_setup(self, **kwargs):
        return self.call('query_adc_setup', kwargs=kwargs)

    def adc_setup(self, **kwargs):
        return self.call('adc_setup', kwargs=kwargs)

    def adc_averaging(self, **kwargs):
        return self.call('adc_averaging', kwargs=kwargs)

    def adc_auto_zero(self, **kwargs):
        return self.call('adc_auto_zero', kwargs=kwargs)

    def time_stamp(self, **kwargs):
        return self.call('time_stamp', kwargs=kwargs)

    def query_time_stamp_setting(self, **kwargs):
        return self.call('query_time_stamp_setting', kwargs=kwargs)

    def wait_time(self, **kwargs):
        return self.call('wait_time', kwargs=kwargs)

    def query_staircase_sweep_settings(self, **kwargs):
        return self.call('query_staircase_sweep_settings', kwargs=kwargs)

    def sweep_timing(self, **kwargs):
        return self.call('sweep_timing', kwargs=kwargs)

    def sweep_auto_abort(self, **kwargs):
        return self.call('sweep_auto_abort', kwargs=kwargs)

    def query_sampling_settings(self, **kwargs):
        return self.call('query_sampling_settings', kwargs=kwargs)

    def sampling_mode(self, **kwargs):
        return self.call('sampling_mode', kwargs=kwargs)

    def sampling_timing(self, **kwargs):
        return self.call('sampling_timing', kwargs=kwargs)

    def sampling_auto_abort(self, **kwargs):
        return self.call('sampling_auto_abort', kwargs=kwargs)

    def read_data(self, **kwargs):
        return self.call('read_data', kwargs=kwargs)

    def read_channels(self, **kwargs):
        return self.call('read_channels', kwargs=kwargs)

    def query_series_resistor(self, **kwargs):
        return self.call('query_series_resistor', kwargs=kwargs)

    def query_meas_range_current_auto(self, **kwargs):
        return self.call('query_meas_range_current_auto', kwargs=kwargs)

    def query_meas_op_mode(self, **kwargs):
        return self.call('query_meas_op_mode', kwargs=kwargs)

    def query_meas_ranges(self, **kwargs):
        return self.call('query_meas_ranges', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

