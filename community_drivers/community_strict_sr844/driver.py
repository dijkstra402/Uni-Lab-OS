from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictSr844(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/StanfordResearchSystems/SR844.py', 'class_name': 'SR844', 'import_roots': ['src'], 'candidate_methods': ['snap', 'increment_sensitivity', 'decrement_sensitivity', 'update_ch_unit', 'get_display_value', 'set_sweep_parameters', 'get_phase_offset', 'set_phase_offset', 'get_reference_source', 'set_reference_source', 'get_frequency', 'set_frequency', 'get_harmonic', 'set_harmonic', 'get_input_impedance', 'set_input_impedance', 'get_sensitivity', 'set_sensitivity', 'get_reserve', 'set_reserve', 'get_time_constant', 'set_time_constant', 'get_filter_slope', 'set_filter_slope', 'get_x_offset', 'set_x_offset', 'get_r_v_offset', 'set_r_v_offset', 'get_r_dbm_offset', 'set_r_dbm_offset', 'get_y_offset', 'set_y_offset', 'get_complex_voltage', 'get_output_interface', 'set_output_interface', 'get_ratio_mode', 'set_ratio_mode', 'get_buffer_sr', 'set_buffer_sr', 'get_buffer_acq_mode', 'set_buffer_acq_mode', 'get_buffer_trig_mode', 'set_buffer_trig_mode', 'get_buffer_npts', 'get_sweep_setpoints', 'get_x', 'get_y', 'get_r_v', 'get_r_dbm', 'get_phase', 'get_ch1', 'get_ch2'], 'action_targets': {'get_phase_offset': '__qcodes_param_get__phase_offset', 'set_phase_offset': '__qcodes_param_set__phase_offset', 'get_reference_source': '__qcodes_param_get__reference_source', 'set_reference_source': '__qcodes_param_set__reference_source', 'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_harmonic': '__qcodes_param_get__harmonic', 'set_harmonic': '__qcodes_param_set__harmonic', 'get_input_impedance': '__qcodes_param_get__input_impedance', 'set_input_impedance': '__qcodes_param_set__input_impedance', 'get_sensitivity': '__qcodes_param_get__sensitivity', 'set_sensitivity': '__qcodes_param_set__sensitivity', 'get_reserve': '__qcodes_param_get__reserve', 'set_reserve': '__qcodes_param_set__reserve', 'get_time_constant': '__qcodes_param_get__time_constant', 'set_time_constant': '__qcodes_param_set__time_constant', 'get_filter_slope': '__qcodes_param_get__filter_slope', 'set_filter_slope': '__qcodes_param_set__filter_slope', 'get_x_offset': '__qcodes_param_get__x_offset', 'set_x_offset': '__qcodes_param_set__x_offset', 'get_r_v_offset': '__qcodes_param_get__r_v_offset', 'set_r_v_offset': '__qcodes_param_set__r_v_offset', 'get_r_dbm_offset': '__qcodes_param_get__r_dbm_offset', 'set_r_dbm_offset': '__qcodes_param_set__r_dbm_offset', 'get_y_offset': '__qcodes_param_get__y_offset', 'set_y_offset': '__qcodes_param_set__y_offset', 'get_complex_voltage': '__qcodes_param_get__complex_voltage', 'get_output_interface': '__qcodes_param_get__output_interface', 'set_output_interface': '__qcodes_param_set__output_interface', 'get_ratio_mode': '__qcodes_param_get__ratio_mode', 'set_ratio_mode': '__qcodes_param_set__ratio_mode', 'get_buffer_sr': '__qcodes_param_get__buffer_sr', 'set_buffer_sr': '__qcodes_param_set__buffer_sr', 'get_buffer_acq_mode': '__qcodes_param_get__buffer_acq_mode', 'set_buffer_acq_mode': '__qcodes_param_set__buffer_acq_mode', 'get_buffer_trig_mode': '__qcodes_param_get__buffer_trig_mode', 'set_buffer_trig_mode': '__qcodes_param_set__buffer_trig_mode', 'get_buffer_npts': '__qcodes_param_get__buffer_npts', 'get_sweep_setpoints': '__qcodes_param_get__sweep_setpoints', 'get_x': '__qcodes_param_get__x', 'get_y': '__qcodes_param_get__y', 'get_r_v': '__qcodes_param_get__r_v', 'get_r_dbm': '__qcodes_param_get__r_dbm', 'get_phase': '__qcodes_param_get__phase', 'get_ch1': '__qcodes_param_get__ch1', 'get_ch2': '__qcodes_param_get__ch2'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/StanfordResearchSystems/SR844.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_phase_offset': '__qcodes_param_get__phase_offset', 'set_phase_offset': '__qcodes_param_set__phase_offset', 'get_reference_source': '__qcodes_param_get__reference_source', 'set_reference_source': '__qcodes_param_set__reference_source', 'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_harmonic': '__qcodes_param_get__harmonic', 'set_harmonic': '__qcodes_param_set__harmonic', 'get_input_impedance': '__qcodes_param_get__input_impedance', 'set_input_impedance': '__qcodes_param_set__input_impedance', 'get_sensitivity': '__qcodes_param_get__sensitivity', 'set_sensitivity': '__qcodes_param_set__sensitivity', 'get_reserve': '__qcodes_param_get__reserve', 'set_reserve': '__qcodes_param_set__reserve', 'get_time_constant': '__qcodes_param_get__time_constant', 'set_time_constant': '__qcodes_param_set__time_constant', 'get_filter_slope': '__qcodes_param_get__filter_slope', 'set_filter_slope': '__qcodes_param_set__filter_slope', 'get_x_offset': '__qcodes_param_get__x_offset', 'set_x_offset': '__qcodes_param_set__x_offset', 'get_r_v_offset': '__qcodes_param_get__r_v_offset', 'set_r_v_offset': '__qcodes_param_set__r_v_offset', 'get_r_dbm_offset': '__qcodes_param_get__r_dbm_offset', 'set_r_dbm_offset': '__qcodes_param_set__r_dbm_offset', 'get_y_offset': '__qcodes_param_get__y_offset', 'set_y_offset': '__qcodes_param_set__y_offset', 'get_complex_voltage': '__qcodes_param_get__complex_voltage', 'get_output_interface': '__qcodes_param_get__output_interface', 'set_output_interface': '__qcodes_param_set__output_interface', 'get_ratio_mode': '__qcodes_param_get__ratio_mode', 'set_ratio_mode': '__qcodes_param_set__ratio_mode', 'get_buffer_sr': '__qcodes_param_get__buffer_sr', 'set_buffer_sr': '__qcodes_param_set__buffer_sr', 'get_buffer_acq_mode': '__qcodes_param_get__buffer_acq_mode', 'set_buffer_acq_mode': '__qcodes_param_set__buffer_acq_mode', 'get_buffer_trig_mode': '__qcodes_param_get__buffer_trig_mode', 'set_buffer_trig_mode': '__qcodes_param_set__buffer_trig_mode', 'get_buffer_npts': '__qcodes_param_get__buffer_npts', 'get_sweep_setpoints': '__qcodes_param_get__sweep_setpoints', 'get_x': '__qcodes_param_get__x', 'get_y': '__qcodes_param_get__y', 'get_r_v': '__qcodes_param_get__r_v', 'get_r_dbm': '__qcodes_param_get__r_dbm', 'get_phase': '__qcodes_param_get__phase', 'get_ch1': '__qcodes_param_get__ch1', 'get_ch2': '__qcodes_param_get__ch2'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def snap(self, **kwargs):
        return self.call('snap', kwargs=kwargs)

    def increment_sensitivity(self, **kwargs):
        return self.call('increment_sensitivity', kwargs=kwargs)

    def decrement_sensitivity(self, **kwargs):
        return self.call('decrement_sensitivity', kwargs=kwargs)

    def update_ch_unit(self, **kwargs):
        return self.call('update_ch_unit', kwargs=kwargs)

    def get_display_value(self, **kwargs):
        return self.call('get_display_value', kwargs=kwargs)

    def set_sweep_parameters(self, **kwargs):
        return self.call('set_sweep_parameters', kwargs=kwargs)

    def get_phase_offset(self, **kwargs):
        return self.call('get_phase_offset', kwargs=kwargs)

    def set_phase_offset(self, **kwargs):
        return self.call('set_phase_offset', kwargs=kwargs)

    def get_reference_source(self, **kwargs):
        return self.call('get_reference_source', kwargs=kwargs)

    def set_reference_source(self, **kwargs):
        return self.call('set_reference_source', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def get_harmonic(self, **kwargs):
        return self.call('get_harmonic', kwargs=kwargs)

    def set_harmonic(self, **kwargs):
        return self.call('set_harmonic', kwargs=kwargs)

    def get_input_impedance(self, **kwargs):
        return self.call('get_input_impedance', kwargs=kwargs)

    def set_input_impedance(self, **kwargs):
        return self.call('set_input_impedance', kwargs=kwargs)

    def get_sensitivity(self, **kwargs):
        return self.call('get_sensitivity', kwargs=kwargs)

    def set_sensitivity(self, **kwargs):
        return self.call('set_sensitivity', kwargs=kwargs)

    def get_reserve(self, **kwargs):
        return self.call('get_reserve', kwargs=kwargs)

    def set_reserve(self, **kwargs):
        return self.call('set_reserve', kwargs=kwargs)

    def get_time_constant(self, **kwargs):
        return self.call('get_time_constant', kwargs=kwargs)

    def set_time_constant(self, **kwargs):
        return self.call('set_time_constant', kwargs=kwargs)

    def get_filter_slope(self, **kwargs):
        return self.call('get_filter_slope', kwargs=kwargs)

    def set_filter_slope(self, **kwargs):
        return self.call('set_filter_slope', kwargs=kwargs)

    def get_x_offset(self, **kwargs):
        return self.call('get_x_offset', kwargs=kwargs)

    def set_x_offset(self, **kwargs):
        return self.call('set_x_offset', kwargs=kwargs)

    def get_r_v_offset(self, **kwargs):
        return self.call('get_r_v_offset', kwargs=kwargs)

    def set_r_v_offset(self, **kwargs):
        return self.call('set_r_v_offset', kwargs=kwargs)

    def get_r_dbm_offset(self, **kwargs):
        return self.call('get_r_dbm_offset', kwargs=kwargs)

    def set_r_dbm_offset(self, **kwargs):
        return self.call('set_r_dbm_offset', kwargs=kwargs)

    def get_y_offset(self, **kwargs):
        return self.call('get_y_offset', kwargs=kwargs)

    def set_y_offset(self, **kwargs):
        return self.call('set_y_offset', kwargs=kwargs)

    def get_complex_voltage(self, **kwargs):
        return self.call('get_complex_voltage', kwargs=kwargs)

    def get_output_interface(self, **kwargs):
        return self.call('get_output_interface', kwargs=kwargs)

    def set_output_interface(self, **kwargs):
        return self.call('set_output_interface', kwargs=kwargs)

    def get_ratio_mode(self, **kwargs):
        return self.call('get_ratio_mode', kwargs=kwargs)

    def set_ratio_mode(self, **kwargs):
        return self.call('set_ratio_mode', kwargs=kwargs)

    def get_buffer_sr(self, **kwargs):
        return self.call('get_buffer_sr', kwargs=kwargs)

    def set_buffer_sr(self, **kwargs):
        return self.call('set_buffer_sr', kwargs=kwargs)

    def get_buffer_acq_mode(self, **kwargs):
        return self.call('get_buffer_acq_mode', kwargs=kwargs)

    def set_buffer_acq_mode(self, **kwargs):
        return self.call('set_buffer_acq_mode', kwargs=kwargs)

    def get_buffer_trig_mode(self, **kwargs):
        return self.call('get_buffer_trig_mode', kwargs=kwargs)

    def set_buffer_trig_mode(self, **kwargs):
        return self.call('set_buffer_trig_mode', kwargs=kwargs)

    def get_buffer_npts(self, **kwargs):
        return self.call('get_buffer_npts', kwargs=kwargs)

    def get_sweep_setpoints(self, **kwargs):
        return self.call('get_sweep_setpoints', kwargs=kwargs)

    def get_x(self, **kwargs):
        return self.call('get_x', kwargs=kwargs)

    def get_y(self, **kwargs):
        return self.call('get_y', kwargs=kwargs)

    def get_r_v(self, **kwargs):
        return self.call('get_r_v', kwargs=kwargs)

    def get_r_dbm(self, **kwargs):
        return self.call('get_r_dbm', kwargs=kwargs)

    def get_phase(self, **kwargs):
        return self.call('get_phase', kwargs=kwargs)

    def get_ch1(self, **kwargs):
        return self.call('get_ch1', kwargs=kwargs)

    def get_ch2(self, **kwargs):
        return self.call('get_ch2', kwargs=kwargs)

