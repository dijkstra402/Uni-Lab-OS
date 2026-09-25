from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictCm10(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Lakeshore/modules/cm10.py', 'class_name': 'cm10', 'import_roots': ['src'], 'candidate_methods': ['get_current_range', 'set_current_range', 'get_current_autorange_enabled', 'set_current_autorange_enabled', 'get_bias_voltage_enabled', 'set_bias_voltage_enabled', 'get_bias_voltage', 'set_bias_voltage', 'get_frequency_range_threshold', 'set_frequency_range_threshold', 'read_DC', 'read_DC_relative', 'read_RMS', 'read_RMS_relative', 'read_r', 'read_theta', 'read_x', 'read_y', 'read_LIA_DC', 'read_frequency', 'read_npeak', 'read_ppeak', 'read_ptpeak', 'calculated_resistance', 'get_mode', 'set_mode', 'get_input_filter_enabled', 'set_input_filter_enabled', 'get_input_filter_highpass_rolloff', 'set_input_filter_highpass_rolloff', 'get_input_filter_highpass_cutoff', 'set_input_filter_highpass_cutoff', 'get_input_filter_lowpass_rolloff', 'set_input_filter_lowpass_rolloff', 'get_input_filter_lowpass_cutoff', 'set_input_filter_lowpass_cutoff', 'get_input_filter_optimization', 'set_input_filter_optimization', 'get_calculated_resistance_source', 'set_calculated_resistance_source', 'get_nplc', 'set_nplc', 'get_harmonic', 'set_harmonic', 'get_phase', 'set_phase', 'get_averaging_filter_enabled', 'set_averaging_filter_enabled', 'get_averaging_filter_cycles', 'set_averaging_filter_cycles', 'get_traditional_lowpass_enabled', 'set_traditional_lowpass_enabled', 'get_output_filter_rolloff', 'set_output_filter_rolloff', 'get_reference_source', 'set_reference_source', 'get_time_constant', 'set_time_constant', 'get_digital_highpass_enabled', 'set_digital_highpass_enabled', 'get_reference_frequency', 'get_settling_time', 'get_enbw', 'reset_to_default', 'get_model', 'get_serial'], 'action_targets': {'get_current_range': '__qcodes_param_get__current_range', 'set_current_range': '__qcodes_param_set__current_range', 'get_current_autorange_enabled': '__qcodes_param_get__current_autorange_enabled', 'set_current_autorange_enabled': '__qcodes_param_set__current_autorange_enabled', 'get_bias_voltage_enabled': '__qcodes_param_get__bias_voltage_enabled', 'set_bias_voltage_enabled': '__qcodes_param_set__bias_voltage_enabled', 'get_bias_voltage': '__qcodes_param_get__bias_voltage', 'set_bias_voltage': '__qcodes_param_set__bias_voltage', 'get_frequency_range_threshold': '__qcodes_param_get__frequency_range_threshold', 'set_frequency_range_threshold': '__qcodes_param_set__frequency_range_threshold', 'get_mode': '__qcodes_param_get__mode', 'set_mode': '__qcodes_param_set__mode', 'get_input_filter_enabled': '__qcodes_param_get__input_filter_enabled', 'set_input_filter_enabled': '__qcodes_param_set__input_filter_enabled', 'get_input_filter_highpass_rolloff': '__qcodes_param_get__input_filter_highpass_rolloff', 'set_input_filter_highpass_rolloff': '__qcodes_param_set__input_filter_highpass_rolloff', 'get_input_filter_highpass_cutoff': '__qcodes_param_get__input_filter_highpass_cutoff', 'set_input_filter_highpass_cutoff': '__qcodes_param_set__input_filter_highpass_cutoff', 'get_input_filter_lowpass_rolloff': '__qcodes_param_get__input_filter_lowpass_rolloff', 'set_input_filter_lowpass_rolloff': '__qcodes_param_set__input_filter_lowpass_rolloff', 'get_input_filter_lowpass_cutoff': '__qcodes_param_get__input_filter_lowpass_cutoff', 'set_input_filter_lowpass_cutoff': '__qcodes_param_set__input_filter_lowpass_cutoff', 'get_input_filter_optimization': '__qcodes_param_get__input_filter_optimization', 'set_input_filter_optimization': '__qcodes_param_set__input_filter_optimization', 'get_calculated_resistance_source': '__qcodes_param_get__calculated_resistance_source', 'set_calculated_resistance_source': '__qcodes_param_set__calculated_resistance_source', 'get_nplc': '__qcodes_param_get__nplc', 'set_nplc': '__qcodes_param_set__nplc', 'get_harmonic': '__qcodes_param_get__harmonic', 'set_harmonic': '__qcodes_param_set__harmonic', 'get_phase': '__qcodes_param_get__phase', 'set_phase': '__qcodes_param_set__phase', 'get_averaging_filter_enabled': '__qcodes_param_get__averaging_filter_enabled', 'set_averaging_filter_enabled': '__qcodes_param_set__averaging_filter_enabled', 'get_averaging_filter_cycles': '__qcodes_param_get__averaging_filter_cycles', 'set_averaging_filter_cycles': '__qcodes_param_set__averaging_filter_cycles', 'get_traditional_lowpass_enabled': '__qcodes_param_get__traditional_lowpass_enabled', 'set_traditional_lowpass_enabled': '__qcodes_param_set__traditional_lowpass_enabled', 'get_output_filter_rolloff': '__qcodes_param_get__output_filter_rolloff', 'set_output_filter_rolloff': '__qcodes_param_set__output_filter_rolloff', 'get_reference_source': '__qcodes_param_get__reference_source', 'set_reference_source': '__qcodes_param_set__reference_source', 'get_time_constant': '__qcodes_param_get__time_constant', 'set_time_constant': '__qcodes_param_set__time_constant', 'get_digital_highpass_enabled': '__qcodes_param_get__digital_highpass_enabled', 'set_digital_highpass_enabled': '__qcodes_param_set__digital_highpass_enabled', 'get_reference_frequency': '__qcodes_param_get__reference_frequency', 'get_settling_time': '__qcodes_param_get__settling_time', 'get_enbw': '__qcodes_param_get__enbw', 'get_model': '__qcodes_param_get__model', 'get_serial': '__qcodes_param_get__serial'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Lakeshore/modules/cm10.py', 'confidence': 0.75, 'quality_score': 0.83, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_current_range': '__qcodes_param_get__current_range', 'set_current_range': '__qcodes_param_set__current_range', 'get_current_autorange_enabled': '__qcodes_param_get__current_autorange_enabled', 'set_current_autorange_enabled': '__qcodes_param_set__current_autorange_enabled', 'get_bias_voltage_enabled': '__qcodes_param_get__bias_voltage_enabled', 'set_bias_voltage_enabled': '__qcodes_param_set__bias_voltage_enabled', 'get_bias_voltage': '__qcodes_param_get__bias_voltage', 'set_bias_voltage': '__qcodes_param_set__bias_voltage', 'get_frequency_range_threshold': '__qcodes_param_get__frequency_range_threshold', 'set_frequency_range_threshold': '__qcodes_param_set__frequency_range_threshold', 'get_mode': '__qcodes_param_get__mode', 'set_mode': '__qcodes_param_set__mode', 'get_input_filter_enabled': '__qcodes_param_get__input_filter_enabled', 'set_input_filter_enabled': '__qcodes_param_set__input_filter_enabled', 'get_input_filter_highpass_rolloff': '__qcodes_param_get__input_filter_highpass_rolloff', 'set_input_filter_highpass_rolloff': '__qcodes_param_set__input_filter_highpass_rolloff', 'get_input_filter_highpass_cutoff': '__qcodes_param_get__input_filter_highpass_cutoff', 'set_input_filter_highpass_cutoff': '__qcodes_param_set__input_filter_highpass_cutoff', 'get_input_filter_lowpass_rolloff': '__qcodes_param_get__input_filter_lowpass_rolloff', 'set_input_filter_lowpass_rolloff': '__qcodes_param_set__input_filter_lowpass_rolloff', 'get_input_filter_lowpass_cutoff': '__qcodes_param_get__input_filter_lowpass_cutoff', 'set_input_filter_lowpass_cutoff': '__qcodes_param_set__input_filter_lowpass_cutoff', 'get_input_filter_optimization': '__qcodes_param_get__input_filter_optimization', 'set_input_filter_optimization': '__qcodes_param_set__input_filter_optimization', 'get_calculated_resistance_source': '__qcodes_param_get__calculated_resistance_source', 'set_calculated_resistance_source': '__qcodes_param_set__calculated_resistance_source', 'get_nplc': '__qcodes_param_get__nplc', 'set_nplc': '__qcodes_param_set__nplc', 'get_harmonic': '__qcodes_param_get__harmonic', 'set_harmonic': '__qcodes_param_set__harmonic', 'get_phase': '__qcodes_param_get__phase', 'set_phase': '__qcodes_param_set__phase', 'get_averaging_filter_enabled': '__qcodes_param_get__averaging_filter_enabled', 'set_averaging_filter_enabled': '__qcodes_param_set__averaging_filter_enabled', 'get_averaging_filter_cycles': '__qcodes_param_get__averaging_filter_cycles', 'set_averaging_filter_cycles': '__qcodes_param_set__averaging_filter_cycles', 'get_traditional_lowpass_enabled': '__qcodes_param_get__traditional_lowpass_enabled', 'set_traditional_lowpass_enabled': '__qcodes_param_set__traditional_lowpass_enabled', 'get_output_filter_rolloff': '__qcodes_param_get__output_filter_rolloff', 'set_output_filter_rolloff': '__qcodes_param_set__output_filter_rolloff', 'get_reference_source': '__qcodes_param_get__reference_source', 'set_reference_source': '__qcodes_param_set__reference_source', 'get_time_constant': '__qcodes_param_get__time_constant', 'set_time_constant': '__qcodes_param_set__time_constant', 'get_digital_highpass_enabled': '__qcodes_param_get__digital_highpass_enabled', 'set_digital_highpass_enabled': '__qcodes_param_set__digital_highpass_enabled', 'get_reference_frequency': '__qcodes_param_get__reference_frequency', 'get_settling_time': '__qcodes_param_get__settling_time', 'get_enbw': '__qcodes_param_get__enbw', 'get_model': '__qcodes_param_get__model', 'get_serial': '__qcodes_param_get__serial'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_current_range(self, **kwargs):
        return self.call('get_current_range', kwargs=kwargs)

    def set_current_range(self, **kwargs):
        return self.call('set_current_range', kwargs=kwargs)

    def get_current_autorange_enabled(self, **kwargs):
        return self.call('get_current_autorange_enabled', kwargs=kwargs)

    def set_current_autorange_enabled(self, **kwargs):
        return self.call('set_current_autorange_enabled', kwargs=kwargs)

    def get_bias_voltage_enabled(self, **kwargs):
        return self.call('get_bias_voltage_enabled', kwargs=kwargs)

    def set_bias_voltage_enabled(self, **kwargs):
        return self.call('set_bias_voltage_enabled', kwargs=kwargs)

    def get_bias_voltage(self, **kwargs):
        return self.call('get_bias_voltage', kwargs=kwargs)

    def set_bias_voltage(self, **kwargs):
        return self.call('set_bias_voltage', kwargs=kwargs)

    def get_frequency_range_threshold(self, **kwargs):
        return self.call('get_frequency_range_threshold', kwargs=kwargs)

    def set_frequency_range_threshold(self, **kwargs):
        return self.call('set_frequency_range_threshold', kwargs=kwargs)

    def read_DC(self, **kwargs):
        return self.call('read_DC', kwargs=kwargs)

    def read_DC_relative(self, **kwargs):
        return self.call('read_DC_relative', kwargs=kwargs)

    def read_RMS(self, **kwargs):
        return self.call('read_RMS', kwargs=kwargs)

    def read_RMS_relative(self, **kwargs):
        return self.call('read_RMS_relative', kwargs=kwargs)

    def read_r(self, **kwargs):
        return self.call('read_r', kwargs=kwargs)

    def read_theta(self, **kwargs):
        return self.call('read_theta', kwargs=kwargs)

    def read_x(self, **kwargs):
        return self.call('read_x', kwargs=kwargs)

    def read_y(self, **kwargs):
        return self.call('read_y', kwargs=kwargs)

    def read_LIA_DC(self, **kwargs):
        return self.call('read_LIA_DC', kwargs=kwargs)

    def read_frequency(self, **kwargs):
        return self.call('read_frequency', kwargs=kwargs)

    def read_npeak(self, **kwargs):
        return self.call('read_npeak', kwargs=kwargs)

    def read_ppeak(self, **kwargs):
        return self.call('read_ppeak', kwargs=kwargs)

    def read_ptpeak(self, **kwargs):
        return self.call('read_ptpeak', kwargs=kwargs)

    def calculated_resistance(self, **kwargs):
        return self.call('calculated_resistance', kwargs=kwargs)

    def get_mode(self, **kwargs):
        return self.call('get_mode', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def get_input_filter_enabled(self, **kwargs):
        return self.call('get_input_filter_enabled', kwargs=kwargs)

    def set_input_filter_enabled(self, **kwargs):
        return self.call('set_input_filter_enabled', kwargs=kwargs)

    def get_input_filter_highpass_rolloff(self, **kwargs):
        return self.call('get_input_filter_highpass_rolloff', kwargs=kwargs)

    def set_input_filter_highpass_rolloff(self, **kwargs):
        return self.call('set_input_filter_highpass_rolloff', kwargs=kwargs)

    def get_input_filter_highpass_cutoff(self, **kwargs):
        return self.call('get_input_filter_highpass_cutoff', kwargs=kwargs)

    def set_input_filter_highpass_cutoff(self, **kwargs):
        return self.call('set_input_filter_highpass_cutoff', kwargs=kwargs)

    def get_input_filter_lowpass_rolloff(self, **kwargs):
        return self.call('get_input_filter_lowpass_rolloff', kwargs=kwargs)

    def set_input_filter_lowpass_rolloff(self, **kwargs):
        return self.call('set_input_filter_lowpass_rolloff', kwargs=kwargs)

    def get_input_filter_lowpass_cutoff(self, **kwargs):
        return self.call('get_input_filter_lowpass_cutoff', kwargs=kwargs)

    def set_input_filter_lowpass_cutoff(self, **kwargs):
        return self.call('set_input_filter_lowpass_cutoff', kwargs=kwargs)

    def get_input_filter_optimization(self, **kwargs):
        return self.call('get_input_filter_optimization', kwargs=kwargs)

    def set_input_filter_optimization(self, **kwargs):
        return self.call('set_input_filter_optimization', kwargs=kwargs)

    def get_calculated_resistance_source(self, **kwargs):
        return self.call('get_calculated_resistance_source', kwargs=kwargs)

    def set_calculated_resistance_source(self, **kwargs):
        return self.call('set_calculated_resistance_source', kwargs=kwargs)

    def get_nplc(self, **kwargs):
        return self.call('get_nplc', kwargs=kwargs)

    def set_nplc(self, **kwargs):
        return self.call('set_nplc', kwargs=kwargs)

    def get_harmonic(self, **kwargs):
        return self.call('get_harmonic', kwargs=kwargs)

    def set_harmonic(self, **kwargs):
        return self.call('set_harmonic', kwargs=kwargs)

    def get_phase(self, **kwargs):
        return self.call('get_phase', kwargs=kwargs)

    def set_phase(self, **kwargs):
        return self.call('set_phase', kwargs=kwargs)

    def get_averaging_filter_enabled(self, **kwargs):
        return self.call('get_averaging_filter_enabled', kwargs=kwargs)

    def set_averaging_filter_enabled(self, **kwargs):
        return self.call('set_averaging_filter_enabled', kwargs=kwargs)

    def get_averaging_filter_cycles(self, **kwargs):
        return self.call('get_averaging_filter_cycles', kwargs=kwargs)

    def set_averaging_filter_cycles(self, **kwargs):
        return self.call('set_averaging_filter_cycles', kwargs=kwargs)

    def get_traditional_lowpass_enabled(self, **kwargs):
        return self.call('get_traditional_lowpass_enabled', kwargs=kwargs)

    def set_traditional_lowpass_enabled(self, **kwargs):
        return self.call('set_traditional_lowpass_enabled', kwargs=kwargs)

    def get_output_filter_rolloff(self, **kwargs):
        return self.call('get_output_filter_rolloff', kwargs=kwargs)

    def set_output_filter_rolloff(self, **kwargs):
        return self.call('set_output_filter_rolloff', kwargs=kwargs)

    def get_reference_source(self, **kwargs):
        return self.call('get_reference_source', kwargs=kwargs)

    def set_reference_source(self, **kwargs):
        return self.call('set_reference_source', kwargs=kwargs)

    def get_time_constant(self, **kwargs):
        return self.call('get_time_constant', kwargs=kwargs)

    def set_time_constant(self, **kwargs):
        return self.call('set_time_constant', kwargs=kwargs)

    def get_digital_highpass_enabled(self, **kwargs):
        return self.call('get_digital_highpass_enabled', kwargs=kwargs)

    def set_digital_highpass_enabled(self, **kwargs):
        return self.call('set_digital_highpass_enabled', kwargs=kwargs)

    def get_reference_frequency(self, **kwargs):
        return self.call('get_reference_frequency', kwargs=kwargs)

    def get_settling_time(self, **kwargs):
        return self.call('get_settling_time', kwargs=kwargs)

    def get_enbw(self, **kwargs):
        return self.call('get_enbw', kwargs=kwargs)

    def reset_to_default(self, **kwargs):
        return self.call('reset_to_default', kwargs=kwargs)

    def get_model(self, **kwargs):
        return self.call('get_model', kwargs=kwargs)

    def get_serial(self, **kwargs):
        return self.call('get_serial', kwargs=kwargs)

