from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictKeysighte8267d(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Keysight/Keysight_E8267D.py', 'class_name': 'Keysight_E8267D', 'import_roots': ['src'], 'candidate_methods': ['on', 'off', 'deg_to_rad', 'rad_to_deg', 'get_frequency', 'set_frequency', 'get_freq_offset', 'set_freq_offset', 'get_freq_mode', 'set_freq_mode', 'get_phase', 'set_phase', 'get_power', 'set_power', 'get_output_rf', 'set_output_rf', 'get_modulation_rf', 'set_modulation_rf', 'get_alc_enabled', 'set_alc_enabled', 'get_attenuator_hold_enabled', 'set_attenuator_hold_enabled', 'get_attenuator_level', 'set_attenuator_level', 'get_iqmodulator_enabled', 'set_iqmodulator_enabled', 'get_iqsource1', 'set_iqsource1', 'get_iqsource2', 'set_iqsource2', 'get_iqadjustments_enabled', 'set_iqadjustments_enabled', 'get_i_offset', 'set_i_offset', 'get_q_offset', 'set_q_offset', 'get_iq_quadrature', 'set_iq_quadrature', 'get_pulse_modulation_enabled', 'set_pulse_modulation_enabled', 'get_pulse_modulation_source', 'set_pulse_modulation_source', 'get_wideband_amplitude_modulation_enabled', 'set_wideband_amplitude_modulation_enabled', 'get_wideband_iq_enabled', 'set_wideband_iq_enabled', 'get_wideband_iq_adjustments_enabled', 'set_wideband_iq_adjustments_enabled', 'get_wideband_i_offset', 'set_wideband_i_offset', 'get_wideband_q_offset', 'set_wideband_q_offset', 'get_wideband_iq_quadrature', 'set_wideband_iq_quadrature'], 'action_targets': {'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_freq_offset': '__qcodes_param_get__freq_offset', 'set_freq_offset': '__qcodes_param_set__freq_offset', 'get_freq_mode': '__qcodes_param_get__freq_mode', 'set_freq_mode': '__qcodes_param_set__freq_mode', 'get_phase': '__qcodes_param_get__phase', 'set_phase': '__qcodes_param_set__phase', 'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power', 'get_output_rf': '__qcodes_param_get__output_rf', 'set_output_rf': '__qcodes_param_set__output_rf', 'get_modulation_rf': '__qcodes_param_get__modulation_rf', 'set_modulation_rf': '__qcodes_param_set__modulation_rf', 'get_alc_enabled': '__qcodes_param_get__alc_enabled', 'set_alc_enabled': '__qcodes_param_set__alc_enabled', 'get_attenuator_hold_enabled': '__qcodes_param_get__attenuator_hold_enabled', 'set_attenuator_hold_enabled': '__qcodes_param_set__attenuator_hold_enabled', 'get_attenuator_level': '__qcodes_param_get__attenuator_level', 'set_attenuator_level': '__qcodes_param_set__attenuator_level', 'get_iqmodulator_enabled': '__qcodes_param_get__iqmodulator_enabled', 'set_iqmodulator_enabled': '__qcodes_param_set__iqmodulator_enabled', 'get_iqsource1': '__qcodes_param_get__iqsource1', 'set_iqsource1': '__qcodes_param_set__iqsource1', 'get_iqsource2': '__qcodes_param_get__iqsource2', 'set_iqsource2': '__qcodes_param_set__iqsource2', 'get_iqadjustments_enabled': '__qcodes_param_get__iqadjustments_enabled', 'set_iqadjustments_enabled': '__qcodes_param_set__iqadjustments_enabled', 'get_i_offset': '__qcodes_param_get__i_offset', 'set_i_offset': '__qcodes_param_set__i_offset', 'get_q_offset': '__qcodes_param_get__q_offset', 'set_q_offset': '__qcodes_param_set__q_offset', 'get_iq_quadrature': '__qcodes_param_get__iq_quadrature', 'set_iq_quadrature': '__qcodes_param_set__iq_quadrature', 'get_pulse_modulation_enabled': '__qcodes_param_get__pulse_modulation_enabled', 'set_pulse_modulation_enabled': '__qcodes_param_set__pulse_modulation_enabled', 'get_pulse_modulation_source': '__qcodes_param_get__pulse_modulation_source', 'set_pulse_modulation_source': '__qcodes_param_set__pulse_modulation_source', 'get_wideband_amplitude_modulation_enabled': '__qcodes_param_get__wideband_amplitude_modulation_enabled', 'set_wideband_amplitude_modulation_enabled': '__qcodes_param_set__wideband_amplitude_modulation_enabled', 'get_wideband_iq_enabled': '__qcodes_param_get__wideband_iq_enabled', 'set_wideband_iq_enabled': '__qcodes_param_set__wideband_iq_enabled', 'get_wideband_iq_adjustments_enabled': '__qcodes_param_get__wideband_iq_adjustments_enabled', 'set_wideband_iq_adjustments_enabled': '__qcodes_param_set__wideband_iq_adjustments_enabled', 'get_wideband_i_offset': '__qcodes_param_get__wideband_i_offset', 'set_wideband_i_offset': '__qcodes_param_set__wideband_i_offset', 'get_wideband_q_offset': '__qcodes_param_get__wideband_q_offset', 'set_wideband_q_offset': '__qcodes_param_set__wideband_q_offset', 'get_wideband_iq_quadrature': '__qcodes_param_get__wideband_iq_quadrature', 'set_wideband_iq_quadrature': '__qcodes_param_set__wideband_iq_quadrature'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Keysight/Keysight_E8267D.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_freq_offset': '__qcodes_param_get__freq_offset', 'set_freq_offset': '__qcodes_param_set__freq_offset', 'get_freq_mode': '__qcodes_param_get__freq_mode', 'set_freq_mode': '__qcodes_param_set__freq_mode', 'get_phase': '__qcodes_param_get__phase', 'set_phase': '__qcodes_param_set__phase', 'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power', 'get_output_rf': '__qcodes_param_get__output_rf', 'set_output_rf': '__qcodes_param_set__output_rf', 'get_modulation_rf': '__qcodes_param_get__modulation_rf', 'set_modulation_rf': '__qcodes_param_set__modulation_rf', 'get_alc_enabled': '__qcodes_param_get__alc_enabled', 'set_alc_enabled': '__qcodes_param_set__alc_enabled', 'get_attenuator_hold_enabled': '__qcodes_param_get__attenuator_hold_enabled', 'set_attenuator_hold_enabled': '__qcodes_param_set__attenuator_hold_enabled', 'get_attenuator_level': '__qcodes_param_get__attenuator_level', 'set_attenuator_level': '__qcodes_param_set__attenuator_level', 'get_iqmodulator_enabled': '__qcodes_param_get__iqmodulator_enabled', 'set_iqmodulator_enabled': '__qcodes_param_set__iqmodulator_enabled', 'get_iqsource1': '__qcodes_param_get__iqsource1', 'set_iqsource1': '__qcodes_param_set__iqsource1', 'get_iqsource2': '__qcodes_param_get__iqsource2', 'set_iqsource2': '__qcodes_param_set__iqsource2', 'get_iqadjustments_enabled': '__qcodes_param_get__iqadjustments_enabled', 'set_iqadjustments_enabled': '__qcodes_param_set__iqadjustments_enabled', 'get_i_offset': '__qcodes_param_get__i_offset', 'set_i_offset': '__qcodes_param_set__i_offset', 'get_q_offset': '__qcodes_param_get__q_offset', 'set_q_offset': '__qcodes_param_set__q_offset', 'get_iq_quadrature': '__qcodes_param_get__iq_quadrature', 'set_iq_quadrature': '__qcodes_param_set__iq_quadrature', 'get_pulse_modulation_enabled': '__qcodes_param_get__pulse_modulation_enabled', 'set_pulse_modulation_enabled': '__qcodes_param_set__pulse_modulation_enabled', 'get_pulse_modulation_source': '__qcodes_param_get__pulse_modulation_source', 'set_pulse_modulation_source': '__qcodes_param_set__pulse_modulation_source', 'get_wideband_amplitude_modulation_enabled': '__qcodes_param_get__wideband_amplitude_modulation_enabled', 'set_wideband_amplitude_modulation_enabled': '__qcodes_param_set__wideband_amplitude_modulation_enabled', 'get_wideband_iq_enabled': '__qcodes_param_get__wideband_iq_enabled', 'set_wideband_iq_enabled': '__qcodes_param_set__wideband_iq_enabled', 'get_wideband_iq_adjustments_enabled': '__qcodes_param_get__wideband_iq_adjustments_enabled', 'set_wideband_iq_adjustments_enabled': '__qcodes_param_set__wideband_iq_adjustments_enabled', 'get_wideband_i_offset': '__qcodes_param_get__wideband_i_offset', 'set_wideband_i_offset': '__qcodes_param_set__wideband_i_offset', 'get_wideband_q_offset': '__qcodes_param_get__wideband_q_offset', 'set_wideband_q_offset': '__qcodes_param_set__wideband_q_offset', 'get_wideband_iq_quadrature': '__qcodes_param_get__wideband_iq_quadrature', 'set_wideband_iq_quadrature': '__qcodes_param_set__wideband_iq_quadrature'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def on(self, **kwargs):
        return self.call('on', kwargs=kwargs)

    def off(self, **kwargs):
        return self.call('off', kwargs=kwargs)

    def deg_to_rad(self, **kwargs):
        return self.call('deg_to_rad', kwargs=kwargs)

    def rad_to_deg(self, **kwargs):
        return self.call('rad_to_deg', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def get_freq_offset(self, **kwargs):
        return self.call('get_freq_offset', kwargs=kwargs)

    def set_freq_offset(self, **kwargs):
        return self.call('set_freq_offset', kwargs=kwargs)

    def get_freq_mode(self, **kwargs):
        return self.call('get_freq_mode', kwargs=kwargs)

    def set_freq_mode(self, **kwargs):
        return self.call('set_freq_mode', kwargs=kwargs)

    def get_phase(self, **kwargs):
        return self.call('get_phase', kwargs=kwargs)

    def set_phase(self, **kwargs):
        return self.call('set_phase', kwargs=kwargs)

    def get_power(self, **kwargs):
        return self.call('get_power', kwargs=kwargs)

    def set_power(self, **kwargs):
        return self.call('set_power', kwargs=kwargs)

    def get_output_rf(self, **kwargs):
        return self.call('get_output_rf', kwargs=kwargs)

    def set_output_rf(self, **kwargs):
        return self.call('set_output_rf', kwargs=kwargs)

    def get_modulation_rf(self, **kwargs):
        return self.call('get_modulation_rf', kwargs=kwargs)

    def set_modulation_rf(self, **kwargs):
        return self.call('set_modulation_rf', kwargs=kwargs)

    def get_alc_enabled(self, **kwargs):
        return self.call('get_alc_enabled', kwargs=kwargs)

    def set_alc_enabled(self, **kwargs):
        return self.call('set_alc_enabled', kwargs=kwargs)

    def get_attenuator_hold_enabled(self, **kwargs):
        return self.call('get_attenuator_hold_enabled', kwargs=kwargs)

    def set_attenuator_hold_enabled(self, **kwargs):
        return self.call('set_attenuator_hold_enabled', kwargs=kwargs)

    def get_attenuator_level(self, **kwargs):
        return self.call('get_attenuator_level', kwargs=kwargs)

    def set_attenuator_level(self, **kwargs):
        return self.call('set_attenuator_level', kwargs=kwargs)

    def get_iqmodulator_enabled(self, **kwargs):
        return self.call('get_iqmodulator_enabled', kwargs=kwargs)

    def set_iqmodulator_enabled(self, **kwargs):
        return self.call('set_iqmodulator_enabled', kwargs=kwargs)

    def get_iqsource1(self, **kwargs):
        return self.call('get_iqsource1', kwargs=kwargs)

    def set_iqsource1(self, **kwargs):
        return self.call('set_iqsource1', kwargs=kwargs)

    def get_iqsource2(self, **kwargs):
        return self.call('get_iqsource2', kwargs=kwargs)

    def set_iqsource2(self, **kwargs):
        return self.call('set_iqsource2', kwargs=kwargs)

    def get_iqadjustments_enabled(self, **kwargs):
        return self.call('get_iqadjustments_enabled', kwargs=kwargs)

    def set_iqadjustments_enabled(self, **kwargs):
        return self.call('set_iqadjustments_enabled', kwargs=kwargs)

    def get_i_offset(self, **kwargs):
        return self.call('get_i_offset', kwargs=kwargs)

    def set_i_offset(self, **kwargs):
        return self.call('set_i_offset', kwargs=kwargs)

    def get_q_offset(self, **kwargs):
        return self.call('get_q_offset', kwargs=kwargs)

    def set_q_offset(self, **kwargs):
        return self.call('set_q_offset', kwargs=kwargs)

    def get_iq_quadrature(self, **kwargs):
        return self.call('get_iq_quadrature', kwargs=kwargs)

    def set_iq_quadrature(self, **kwargs):
        return self.call('set_iq_quadrature', kwargs=kwargs)

    def get_pulse_modulation_enabled(self, **kwargs):
        return self.call('get_pulse_modulation_enabled', kwargs=kwargs)

    def set_pulse_modulation_enabled(self, **kwargs):
        return self.call('set_pulse_modulation_enabled', kwargs=kwargs)

    def get_pulse_modulation_source(self, **kwargs):
        return self.call('get_pulse_modulation_source', kwargs=kwargs)

    def set_pulse_modulation_source(self, **kwargs):
        return self.call('set_pulse_modulation_source', kwargs=kwargs)

    def get_wideband_amplitude_modulation_enabled(self, **kwargs):
        return self.call('get_wideband_amplitude_modulation_enabled', kwargs=kwargs)

    def set_wideband_amplitude_modulation_enabled(self, **kwargs):
        return self.call('set_wideband_amplitude_modulation_enabled', kwargs=kwargs)

    def get_wideband_iq_enabled(self, **kwargs):
        return self.call('get_wideband_iq_enabled', kwargs=kwargs)

    def set_wideband_iq_enabled(self, **kwargs):
        return self.call('set_wideband_iq_enabled', kwargs=kwargs)

    def get_wideband_iq_adjustments_enabled(self, **kwargs):
        return self.call('get_wideband_iq_adjustments_enabled', kwargs=kwargs)

    def set_wideband_iq_adjustments_enabled(self, **kwargs):
        return self.call('set_wideband_iq_adjustments_enabled', kwargs=kwargs)

    def get_wideband_i_offset(self, **kwargs):
        return self.call('get_wideband_i_offset', kwargs=kwargs)

    def set_wideband_i_offset(self, **kwargs):
        return self.call('set_wideband_i_offset', kwargs=kwargs)

    def get_wideband_q_offset(self, **kwargs):
        return self.call('get_wideband_q_offset', kwargs=kwargs)

    def set_wideband_q_offset(self, **kwargs):
        return self.call('set_wideband_q_offset', kwargs=kwargs)

    def get_wideband_iq_quadrature(self, **kwargs):
        return self.call('get_wideband_iq_quadrature', kwargs=kwargs)

    def set_wideband_iq_quadrature(self, **kwargs):
        return self.call('set_wideband_iq_quadrature', kwargs=kwargs)

