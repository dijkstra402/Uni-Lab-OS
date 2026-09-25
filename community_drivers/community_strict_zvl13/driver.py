from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictZvl13(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/RohdeSchwarz/ZVL13.py', 'class_name': 'ZVL13', 'import_roots': ['src'], 'candidate_methods': ['reset', 'calibration', 'sa_mode', 'na_mode', 'update_traces', 'get_mode', 'set_mode', 'get_start', 'set_start', 'get_stop', 'set_stop', 'get_center', 'set_center', 'get_span', 'set_span', 'get_npts', 'set_npts', 'get_power', 'set_power', 'get_format', 'set_format', 'get_avg', 'set_avg', 'get_num_ports', 'get_s_parameter', 'set_s_parameter', 'get_trace_mag_phase', 'get_trace', 'get_s_trace', 'get_spectrum', 'get_status', 'set_status', 'get_rf_power', 'set_rf_power', 'get_bandwidth', 'set_bandwidth', 'get_freq_step', 'set_freq_step'], 'action_targets': {'get_mode': '__qcodes_param_get__mode', 'set_mode': '__qcodes_param_set__mode', 'get_start': '__qcodes_param_get__start', 'set_start': '__qcodes_param_set__start', 'get_stop': '__qcodes_param_get__stop', 'set_stop': '__qcodes_param_set__stop', 'get_center': '__qcodes_param_get__center', 'set_center': '__qcodes_param_set__center', 'get_span': '__qcodes_param_get__span', 'set_span': '__qcodes_param_set__span', 'get_npts': '__qcodes_param_get__npts', 'set_npts': '__qcodes_param_set__npts', 'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power', 'get_format': '__qcodes_param_get__format', 'set_format': '__qcodes_param_set__format', 'get_avg': '__qcodes_param_get__avg', 'set_avg': '__qcodes_param_set__avg', 'get_num_ports': '__qcodes_param_get__num_ports', 'get_s_parameter': '__qcodes_param_get__s_parameter', 'set_s_parameter': '__qcodes_param_set__s_parameter', 'get_trace_mag_phase': '__qcodes_param_get__trace_mag_phase', 'get_trace': '__qcodes_param_get__trace', 'get_s_trace': '__qcodes_param_get__s_trace', 'get_spectrum': '__qcodes_param_get__spectrum', 'get_status': '__qcodes_param_get__status', 'set_status': '__qcodes_param_set__status', 'get_rf_power': '__qcodes_param_get__rf_power', 'set_rf_power': '__qcodes_param_set__rf_power', 'get_bandwidth': '__qcodes_param_get__bandwidth', 'set_bandwidth': '__qcodes_param_set__bandwidth', 'get_freq_step': '__qcodes_param_get__freq_step', 'set_freq_step': '__qcodes_param_set__freq_step'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/RohdeSchwarz/ZVL13.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_mode': '__qcodes_param_get__mode', 'set_mode': '__qcodes_param_set__mode', 'get_start': '__qcodes_param_get__start', 'set_start': '__qcodes_param_set__start', 'get_stop': '__qcodes_param_get__stop', 'set_stop': '__qcodes_param_set__stop', 'get_center': '__qcodes_param_get__center', 'set_center': '__qcodes_param_set__center', 'get_span': '__qcodes_param_get__span', 'set_span': '__qcodes_param_set__span', 'get_npts': '__qcodes_param_get__npts', 'set_npts': '__qcodes_param_set__npts', 'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power', 'get_format': '__qcodes_param_get__format', 'set_format': '__qcodes_param_set__format', 'get_avg': '__qcodes_param_get__avg', 'set_avg': '__qcodes_param_set__avg', 'get_num_ports': '__qcodes_param_get__num_ports', 'get_s_parameter': '__qcodes_param_get__s_parameter', 'set_s_parameter': '__qcodes_param_set__s_parameter', 'get_trace_mag_phase': '__qcodes_param_get__trace_mag_phase', 'get_trace': '__qcodes_param_get__trace', 'get_s_trace': '__qcodes_param_get__s_trace', 'get_spectrum': '__qcodes_param_get__spectrum', 'get_status': '__qcodes_param_get__status', 'set_status': '__qcodes_param_set__status', 'get_rf_power': '__qcodes_param_get__rf_power', 'set_rf_power': '__qcodes_param_set__rf_power', 'get_bandwidth': '__qcodes_param_get__bandwidth', 'set_bandwidth': '__qcodes_param_set__bandwidth', 'get_freq_step': '__qcodes_param_get__freq_step', 'set_freq_step': '__qcodes_param_set__freq_step'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def calibration(self, **kwargs):
        return self.call('calibration', kwargs=kwargs)

    def sa_mode(self, **kwargs):
        return self.call('sa_mode', kwargs=kwargs)

    def na_mode(self, **kwargs):
        return self.call('na_mode', kwargs=kwargs)

    def update_traces(self, **kwargs):
        return self.call('update_traces', kwargs=kwargs)

    def get_mode(self, **kwargs):
        return self.call('get_mode', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def get_start(self, **kwargs):
        return self.call('get_start', kwargs=kwargs)

    def set_start(self, **kwargs):
        return self.call('set_start', kwargs=kwargs)

    def get_stop(self, **kwargs):
        return self.call('get_stop', kwargs=kwargs)

    def set_stop(self, **kwargs):
        return self.call('set_stop', kwargs=kwargs)

    def get_center(self, **kwargs):
        return self.call('get_center', kwargs=kwargs)

    def set_center(self, **kwargs):
        return self.call('set_center', kwargs=kwargs)

    def get_span(self, **kwargs):
        return self.call('get_span', kwargs=kwargs)

    def set_span(self, **kwargs):
        return self.call('set_span', kwargs=kwargs)

    def get_npts(self, **kwargs):
        return self.call('get_npts', kwargs=kwargs)

    def set_npts(self, **kwargs):
        return self.call('set_npts', kwargs=kwargs)

    def get_power(self, **kwargs):
        return self.call('get_power', kwargs=kwargs)

    def set_power(self, **kwargs):
        return self.call('set_power', kwargs=kwargs)

    def get_format(self, **kwargs):
        return self.call('get_format', kwargs=kwargs)

    def set_format(self, **kwargs):
        return self.call('set_format', kwargs=kwargs)

    def get_avg(self, **kwargs):
        return self.call('get_avg', kwargs=kwargs)

    def set_avg(self, **kwargs):
        return self.call('set_avg', kwargs=kwargs)

    def get_num_ports(self, **kwargs):
        return self.call('get_num_ports', kwargs=kwargs)

    def get_s_parameter(self, **kwargs):
        return self.call('get_s_parameter', kwargs=kwargs)

    def set_s_parameter(self, **kwargs):
        return self.call('set_s_parameter', kwargs=kwargs)

    def get_trace_mag_phase(self, **kwargs):
        return self.call('get_trace_mag_phase', kwargs=kwargs)

    def get_trace(self, **kwargs):
        return self.call('get_trace', kwargs=kwargs)

    def get_s_trace(self, **kwargs):
        return self.call('get_s_trace', kwargs=kwargs)

    def get_spectrum(self, **kwargs):
        return self.call('get_spectrum', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def set_status(self, **kwargs):
        return self.call('set_status', kwargs=kwargs)

    def get_rf_power(self, **kwargs):
        return self.call('get_rf_power', kwargs=kwargs)

    def set_rf_power(self, **kwargs):
        return self.call('set_rf_power', kwargs=kwargs)

    def get_bandwidth(self, **kwargs):
        return self.call('get_bandwidth', kwargs=kwargs)

    def set_bandwidth(self, **kwargs):
        return self.call('set_bandwidth', kwargs=kwargs)

    def get_freq_step(self, **kwargs):
        return self.call('get_freq_step', kwargs=kwargs)

    def set_freq_step(self, **kwargs):
        return self.call('set_freq_step', kwargs=kwargs)

