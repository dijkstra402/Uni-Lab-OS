from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictSr570(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/StanfordResearchSystems/SR570.py', 'class_name': 'SR570', 'import_roots': ['src'], 'candidate_methods': ['reset', 'get_idn', 'set_sensitivity', 'set_sensitivity_uncalibrated_mode', 'set_sensitivity_uncalibrated_vernier', 'set_input_offset_current_status', 'set_input_offset_current_level', 'set_input_offset_current_sign', 'set_input_offset_uncalibrated_mode', 'set_input_offset_uncalibrated_vernier', 'set_bias_voltage_status', 'set_bias_voltage', 'set_filter_type', 'set_filter_lowpass_frequency', 'set_filter_highpass_frequency', 'set_gain_mode', 'set_invert', 'set_blank'], 'action_targets': {'set_sensitivity': '__qcodes_param_set__sensitivity', 'set_sensitivity_uncalibrated_mode': '__qcodes_param_set__sensitivity_uncalibrated_mode', 'set_sensitivity_uncalibrated_vernier': '__qcodes_param_set__sensitivity_uncalibrated_vernier', 'set_input_offset_current_status': '__qcodes_param_set__input_offset_current_status', 'set_input_offset_current_level': '__qcodes_param_set__input_offset_current_level', 'set_input_offset_current_sign': '__qcodes_param_set__input_offset_current_sign', 'set_input_offset_uncalibrated_mode': '__qcodes_param_set__input_offset_uncalibrated_mode', 'set_input_offset_uncalibrated_vernier': '__qcodes_param_set__input_offset_uncalibrated_vernier', 'set_bias_voltage_status': '__qcodes_param_set__bias_voltage_status', 'set_bias_voltage': '__qcodes_param_set__bias_voltage', 'set_filter_type': '__qcodes_param_set__filter_type', 'set_filter_lowpass_frequency': '__qcodes_param_set__filter_lowpass_frequency', 'set_filter_highpass_frequency': '__qcodes_param_set__filter_highpass_frequency', 'set_gain_mode': '__qcodes_param_set__gain_mode', 'set_invert': '__qcodes_param_set__invert', 'set_blank': '__qcodes_param_set__blank'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/StanfordResearchSystems/SR570.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'set_sensitivity': '__qcodes_param_set__sensitivity', 'set_sensitivity_uncalibrated_mode': '__qcodes_param_set__sensitivity_uncalibrated_mode', 'set_sensitivity_uncalibrated_vernier': '__qcodes_param_set__sensitivity_uncalibrated_vernier', 'set_input_offset_current_status': '__qcodes_param_set__input_offset_current_status', 'set_input_offset_current_level': '__qcodes_param_set__input_offset_current_level', 'set_input_offset_current_sign': '__qcodes_param_set__input_offset_current_sign', 'set_input_offset_uncalibrated_mode': '__qcodes_param_set__input_offset_uncalibrated_mode', 'set_input_offset_uncalibrated_vernier': '__qcodes_param_set__input_offset_uncalibrated_vernier', 'set_bias_voltage_status': '__qcodes_param_set__bias_voltage_status', 'set_bias_voltage': '__qcodes_param_set__bias_voltage', 'set_filter_type': '__qcodes_param_set__filter_type', 'set_filter_lowpass_frequency': '__qcodes_param_set__filter_lowpass_frequency', 'set_filter_highpass_frequency': '__qcodes_param_set__filter_highpass_frequency', 'set_gain_mode': '__qcodes_param_set__gain_mode', 'set_invert': '__qcodes_param_set__invert', 'set_blank': '__qcodes_param_set__blank'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def set_sensitivity(self, **kwargs):
        return self.call('set_sensitivity', kwargs=kwargs)

    def set_sensitivity_uncalibrated_mode(self, **kwargs):
        return self.call('set_sensitivity_uncalibrated_mode', kwargs=kwargs)

    def set_sensitivity_uncalibrated_vernier(self, **kwargs):
        return self.call('set_sensitivity_uncalibrated_vernier', kwargs=kwargs)

    def set_input_offset_current_status(self, **kwargs):
        return self.call('set_input_offset_current_status', kwargs=kwargs)

    def set_input_offset_current_level(self, **kwargs):
        return self.call('set_input_offset_current_level', kwargs=kwargs)

    def set_input_offset_current_sign(self, **kwargs):
        return self.call('set_input_offset_current_sign', kwargs=kwargs)

    def set_input_offset_uncalibrated_mode(self, **kwargs):
        return self.call('set_input_offset_uncalibrated_mode', kwargs=kwargs)

    def set_input_offset_uncalibrated_vernier(self, **kwargs):
        return self.call('set_input_offset_uncalibrated_vernier', kwargs=kwargs)

    def set_bias_voltage_status(self, **kwargs):
        return self.call('set_bias_voltage_status', kwargs=kwargs)

    def set_bias_voltage(self, **kwargs):
        return self.call('set_bias_voltage', kwargs=kwargs)

    def set_filter_type(self, **kwargs):
        return self.call('set_filter_type', kwargs=kwargs)

    def set_filter_lowpass_frequency(self, **kwargs):
        return self.call('set_filter_lowpass_frequency', kwargs=kwargs)

    def set_filter_highpass_frequency(self, **kwargs):
        return self.call('set_filter_highpass_frequency', kwargs=kwargs)

    def set_gain_mode(self, **kwargs):
        return self.call('set_gain_mode', kwargs=kwargs)

    def set_invert(self, **kwargs):
        return self.call('set_invert', kwargs=kwargs)

    def set_blank(self, **kwargs):
        return self.call('set_blank', kwargs=kwargs)

