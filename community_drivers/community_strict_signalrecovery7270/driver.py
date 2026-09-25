from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictSignalrecovery7270(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Ametek/SR_7270.py', 'class_name': 'Signalrecovery7270', 'import_roots': ['src'], 'candidate_methods': ['ask_raw', 'write_raw', 'get_idn', 'get_x', 'get_y', 'get_xy', 'get_r', 'get_phase', 'get_frequency', 'get_osc_amplitude', 'set_osc_amplitude', 'get_osc_frequency', 'set_osc_frequency', 'get_reference', 'set_reference', 'get_noise_mode', 'set_noise_mode', 'get_i_mode', 'set_i_mode', 'get_v_mode', 'set_v_mode', 'get_osc_sync', 'set_osc_sync', 'get_sensitivity', 'set_sensitivity', 'get_timeconstant', 'set_timeconstant'], 'action_targets': {'get_x': '__qcodes_param_get__x', 'get_y': '__qcodes_param_get__y', 'get_xy': '__qcodes_param_get__xy', 'get_r': '__qcodes_param_get__r', 'get_phase': '__qcodes_param_get__phase', 'get_frequency': '__qcodes_param_get__frequency', 'get_osc_amplitude': '__qcodes_param_get__osc_amplitude', 'set_osc_amplitude': '__qcodes_param_set__osc_amplitude', 'get_osc_frequency': '__qcodes_param_get__osc_frequency', 'set_osc_frequency': '__qcodes_param_set__osc_frequency', 'get_reference': '__qcodes_param_get__reference', 'set_reference': '__qcodes_param_set__reference', 'get_noise_mode': '__qcodes_param_get__noise_mode', 'set_noise_mode': '__qcodes_param_set__noise_mode', 'get_i_mode': '__qcodes_param_get__i_mode', 'set_i_mode': '__qcodes_param_set__i_mode', 'get_v_mode': '__qcodes_param_get__v_mode', 'set_v_mode': '__qcodes_param_set__v_mode', 'get_osc_sync': '__qcodes_param_get__osc_sync', 'set_osc_sync': '__qcodes_param_set__osc_sync', 'get_sensitivity': '__qcodes_param_get__sensitivity', 'set_sensitivity': '__qcodes_param_set__sensitivity', 'get_timeconstant': '__qcodes_param_get__timeconstant', 'set_timeconstant': '__qcodes_param_set__timeconstant'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Ametek/SR_7270.py', 'confidence': 0.8, 'quality_score': 0.88, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_x': '__qcodes_param_get__x', 'get_y': '__qcodes_param_get__y', 'get_xy': '__qcodes_param_get__xy', 'get_r': '__qcodes_param_get__r', 'get_phase': '__qcodes_param_get__phase', 'get_frequency': '__qcodes_param_get__frequency', 'get_osc_amplitude': '__qcodes_param_get__osc_amplitude', 'set_osc_amplitude': '__qcodes_param_set__osc_amplitude', 'get_osc_frequency': '__qcodes_param_get__osc_frequency', 'set_osc_frequency': '__qcodes_param_set__osc_frequency', 'get_reference': '__qcodes_param_get__reference', 'set_reference': '__qcodes_param_set__reference', 'get_noise_mode': '__qcodes_param_get__noise_mode', 'set_noise_mode': '__qcodes_param_set__noise_mode', 'get_i_mode': '__qcodes_param_get__i_mode', 'set_i_mode': '__qcodes_param_set__i_mode', 'get_v_mode': '__qcodes_param_get__v_mode', 'set_v_mode': '__qcodes_param_set__v_mode', 'get_osc_sync': '__qcodes_param_get__osc_sync', 'set_osc_sync': '__qcodes_param_set__osc_sync', 'get_sensitivity': '__qcodes_param_get__sensitivity', 'set_sensitivity': '__qcodes_param_set__sensitivity', 'get_timeconstant': '__qcodes_param_get__timeconstant', 'set_timeconstant': '__qcodes_param_set__timeconstant'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def ask_raw(self, **kwargs):
        return self.call('ask_raw', kwargs=kwargs)

    def write_raw(self, **kwargs):
        return self.call('write_raw', kwargs=kwargs)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def get_x(self, **kwargs):
        return self.call('get_x', kwargs=kwargs)

    def get_y(self, **kwargs):
        return self.call('get_y', kwargs=kwargs)

    def get_xy(self, **kwargs):
        return self.call('get_xy', kwargs=kwargs)

    def get_r(self, **kwargs):
        return self.call('get_r', kwargs=kwargs)

    def get_phase(self, **kwargs):
        return self.call('get_phase', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def get_osc_amplitude(self, **kwargs):
        return self.call('get_osc_amplitude', kwargs=kwargs)

    def set_osc_amplitude(self, **kwargs):
        return self.call('set_osc_amplitude', kwargs=kwargs)

    def get_osc_frequency(self, **kwargs):
        return self.call('get_osc_frequency', kwargs=kwargs)

    def set_osc_frequency(self, **kwargs):
        return self.call('set_osc_frequency', kwargs=kwargs)

    def get_reference(self, **kwargs):
        return self.call('get_reference', kwargs=kwargs)

    def set_reference(self, **kwargs):
        return self.call('set_reference', kwargs=kwargs)

    def get_noise_mode(self, **kwargs):
        return self.call('get_noise_mode', kwargs=kwargs)

    def set_noise_mode(self, **kwargs):
        return self.call('set_noise_mode', kwargs=kwargs)

    def get_i_mode(self, **kwargs):
        return self.call('get_i_mode', kwargs=kwargs)

    def set_i_mode(self, **kwargs):
        return self.call('set_i_mode', kwargs=kwargs)

    def get_v_mode(self, **kwargs):
        return self.call('get_v_mode', kwargs=kwargs)

    def set_v_mode(self, **kwargs):
        return self.call('set_v_mode', kwargs=kwargs)

    def get_osc_sync(self, **kwargs):
        return self.call('get_osc_sync', kwargs=kwargs)

    def set_osc_sync(self, **kwargs):
        return self.call('set_osc_sync', kwargs=kwargs)

    def get_sensitivity(self, **kwargs):
        return self.call('get_sensitivity', kwargs=kwargs)

    def set_sensitivity(self, **kwargs):
        return self.call('set_sensitivity', kwargs=kwargs)

    def get_timeconstant(self, **kwargs):
        return self.call('get_timeconstant', kwargs=kwargs)

    def set_timeconstant(self, **kwargs):
        return self.call('set_timeconstant', kwargs=kwargs)

