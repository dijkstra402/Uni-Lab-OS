from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictBcs10(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Lakeshore/modules/bcs10.py', 'class_name': 'bcs10', 'import_roots': ['src'], 'candidate_methods': ['get_coupling', 'set_coupling', 'get_coupling_auto_enabled', 'set_coupling_auto_enabled', 'get_guard_state', 'set_guard_state', 'get_current_autorange_enabled', 'set_current_autorange_enabled', 'get_current_range', 'set_current_range', 'get_cmf_enabled', 'set_cmf_enabled', 'get_cmf_node', 'set_cmf_node', 'get_current_low_limit', 'set_current_low_limit', 'get_current_high_limit', 'set_current_high_limit', 'get_disable_on_compliance', 'set_disable_on_compliance', 'get_current_offset', 'set_current_offset', 'get_current_peak_amplitude', 'set_current_peak_amplitude', 'get_current_rms_amplitude', 'set_current_rms_amplitude', 'output_on', 'output_off', 'get_shape', 'set_shape', 'get_output_enabled', 'set_output_enabled', 'get_frequency', 'set_frequency', 'get_synchronize_enabled', 'set_synchronize_enabled', 'get_synchronize_phase', 'set_synchronize_phase', 'get_synchronize_source', 'set_synchronize_source', 'get_duty_cycle', 'set_duty_cycle', 'reset_to_default', 'get_model', 'get_serial'], 'action_targets': {'get_coupling': '__qcodes_param_get__coupling', 'set_coupling': '__qcodes_param_set__coupling', 'get_coupling_auto_enabled': '__qcodes_param_get__coupling_auto_enabled', 'set_coupling_auto_enabled': '__qcodes_param_set__coupling_auto_enabled', 'get_guard_state': '__qcodes_param_get__guard_state', 'set_guard_state': '__qcodes_param_set__guard_state', 'get_current_autorange_enabled': '__qcodes_param_get__current_autorange_enabled', 'set_current_autorange_enabled': '__qcodes_param_set__current_autorange_enabled', 'get_current_range': '__qcodes_param_get__current_range', 'set_current_range': '__qcodes_param_set__current_range', 'get_cmf_enabled': '__qcodes_param_get__cmf_enabled', 'set_cmf_enabled': '__qcodes_param_set__cmf_enabled', 'get_cmf_node': '__qcodes_param_get__cmf_node', 'set_cmf_node': '__qcodes_param_set__cmf_node', 'get_current_low_limit': '__qcodes_param_get__current_low_limit', 'set_current_low_limit': '__qcodes_param_set__current_low_limit', 'get_current_high_limit': '__qcodes_param_get__current_high_limit', 'set_current_high_limit': '__qcodes_param_set__current_high_limit', 'get_disable_on_compliance': '__qcodes_param_get__disable_on_compliance', 'set_disable_on_compliance': '__qcodes_param_set__disable_on_compliance', 'get_current_offset': '__qcodes_param_get__current_offset', 'set_current_offset': '__qcodes_param_set__current_offset', 'get_current_peak_amplitude': '__qcodes_param_get__current_peak_amplitude', 'set_current_peak_amplitude': '__qcodes_param_set__current_peak_amplitude', 'get_current_rms_amplitude': '__qcodes_param_get__current_rms_amplitude', 'set_current_rms_amplitude': '__qcodes_param_set__current_rms_amplitude', 'get_shape': '__qcodes_param_get__shape', 'set_shape': '__qcodes_param_set__shape', 'get_output_enabled': '__qcodes_param_get__output_enabled', 'set_output_enabled': '__qcodes_param_set__output_enabled', 'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_synchronize_enabled': '__qcodes_param_get__synchronize_enabled', 'set_synchronize_enabled': '__qcodes_param_set__synchronize_enabled', 'get_synchronize_phase': '__qcodes_param_get__synchronize_phase', 'set_synchronize_phase': '__qcodes_param_set__synchronize_phase', 'get_synchronize_source': '__qcodes_param_get__synchronize_source', 'set_synchronize_source': '__qcodes_param_set__synchronize_source', 'get_duty_cycle': '__qcodes_param_get__duty_cycle', 'set_duty_cycle': '__qcodes_param_set__duty_cycle', 'get_model': '__qcodes_param_get__model', 'get_serial': '__qcodes_param_get__serial'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Lakeshore/modules/bcs10.py', 'confidence': 0.75, 'quality_score': 0.83, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_coupling': '__qcodes_param_get__coupling', 'set_coupling': '__qcodes_param_set__coupling', 'get_coupling_auto_enabled': '__qcodes_param_get__coupling_auto_enabled', 'set_coupling_auto_enabled': '__qcodes_param_set__coupling_auto_enabled', 'get_guard_state': '__qcodes_param_get__guard_state', 'set_guard_state': '__qcodes_param_set__guard_state', 'get_current_autorange_enabled': '__qcodes_param_get__current_autorange_enabled', 'set_current_autorange_enabled': '__qcodes_param_set__current_autorange_enabled', 'get_current_range': '__qcodes_param_get__current_range', 'set_current_range': '__qcodes_param_set__current_range', 'get_cmf_enabled': '__qcodes_param_get__cmf_enabled', 'set_cmf_enabled': '__qcodes_param_set__cmf_enabled', 'get_cmf_node': '__qcodes_param_get__cmf_node', 'set_cmf_node': '__qcodes_param_set__cmf_node', 'get_current_low_limit': '__qcodes_param_get__current_low_limit', 'set_current_low_limit': '__qcodes_param_set__current_low_limit', 'get_current_high_limit': '__qcodes_param_get__current_high_limit', 'set_current_high_limit': '__qcodes_param_set__current_high_limit', 'get_disable_on_compliance': '__qcodes_param_get__disable_on_compliance', 'set_disable_on_compliance': '__qcodes_param_set__disable_on_compliance', 'get_current_offset': '__qcodes_param_get__current_offset', 'set_current_offset': '__qcodes_param_set__current_offset', 'get_current_peak_amplitude': '__qcodes_param_get__current_peak_amplitude', 'set_current_peak_amplitude': '__qcodes_param_set__current_peak_amplitude', 'get_current_rms_amplitude': '__qcodes_param_get__current_rms_amplitude', 'set_current_rms_amplitude': '__qcodes_param_set__current_rms_amplitude', 'get_shape': '__qcodes_param_get__shape', 'set_shape': '__qcodes_param_set__shape', 'get_output_enabled': '__qcodes_param_get__output_enabled', 'set_output_enabled': '__qcodes_param_set__output_enabled', 'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_synchronize_enabled': '__qcodes_param_get__synchronize_enabled', 'set_synchronize_enabled': '__qcodes_param_set__synchronize_enabled', 'get_synchronize_phase': '__qcodes_param_get__synchronize_phase', 'set_synchronize_phase': '__qcodes_param_set__synchronize_phase', 'get_synchronize_source': '__qcodes_param_get__synchronize_source', 'set_synchronize_source': '__qcodes_param_set__synchronize_source', 'get_duty_cycle': '__qcodes_param_get__duty_cycle', 'set_duty_cycle': '__qcodes_param_set__duty_cycle', 'get_model': '__qcodes_param_get__model', 'get_serial': '__qcodes_param_get__serial'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_coupling(self, **kwargs):
        return self.call('get_coupling', kwargs=kwargs)

    def set_coupling(self, **kwargs):
        return self.call('set_coupling', kwargs=kwargs)

    def get_coupling_auto_enabled(self, **kwargs):
        return self.call('get_coupling_auto_enabled', kwargs=kwargs)

    def set_coupling_auto_enabled(self, **kwargs):
        return self.call('set_coupling_auto_enabled', kwargs=kwargs)

    def get_guard_state(self, **kwargs):
        return self.call('get_guard_state', kwargs=kwargs)

    def set_guard_state(self, **kwargs):
        return self.call('set_guard_state', kwargs=kwargs)

    def get_current_autorange_enabled(self, **kwargs):
        return self.call('get_current_autorange_enabled', kwargs=kwargs)

    def set_current_autorange_enabled(self, **kwargs):
        return self.call('set_current_autorange_enabled', kwargs=kwargs)

    def get_current_range(self, **kwargs):
        return self.call('get_current_range', kwargs=kwargs)

    def set_current_range(self, **kwargs):
        return self.call('set_current_range', kwargs=kwargs)

    def get_cmf_enabled(self, **kwargs):
        return self.call('get_cmf_enabled', kwargs=kwargs)

    def set_cmf_enabled(self, **kwargs):
        return self.call('set_cmf_enabled', kwargs=kwargs)

    def get_cmf_node(self, **kwargs):
        return self.call('get_cmf_node', kwargs=kwargs)

    def set_cmf_node(self, **kwargs):
        return self.call('set_cmf_node', kwargs=kwargs)

    def get_current_low_limit(self, **kwargs):
        return self.call('get_current_low_limit', kwargs=kwargs)

    def set_current_low_limit(self, **kwargs):
        return self.call('set_current_low_limit', kwargs=kwargs)

    def get_current_high_limit(self, **kwargs):
        return self.call('get_current_high_limit', kwargs=kwargs)

    def set_current_high_limit(self, **kwargs):
        return self.call('set_current_high_limit', kwargs=kwargs)

    def get_disable_on_compliance(self, **kwargs):
        return self.call('get_disable_on_compliance', kwargs=kwargs)

    def set_disable_on_compliance(self, **kwargs):
        return self.call('set_disable_on_compliance', kwargs=kwargs)

    def get_current_offset(self, **kwargs):
        return self.call('get_current_offset', kwargs=kwargs)

    def set_current_offset(self, **kwargs):
        return self.call('set_current_offset', kwargs=kwargs)

    def get_current_peak_amplitude(self, **kwargs):
        return self.call('get_current_peak_amplitude', kwargs=kwargs)

    def set_current_peak_amplitude(self, **kwargs):
        return self.call('set_current_peak_amplitude', kwargs=kwargs)

    def get_current_rms_amplitude(self, **kwargs):
        return self.call('get_current_rms_amplitude', kwargs=kwargs)

    def set_current_rms_amplitude(self, **kwargs):
        return self.call('set_current_rms_amplitude', kwargs=kwargs)

    def output_on(self, **kwargs):
        return self.call('output_on', kwargs=kwargs)

    def output_off(self, **kwargs):
        return self.call('output_off', kwargs=kwargs)

    def get_shape(self, **kwargs):
        return self.call('get_shape', kwargs=kwargs)

    def set_shape(self, **kwargs):
        return self.call('set_shape', kwargs=kwargs)

    def get_output_enabled(self, **kwargs):
        return self.call('get_output_enabled', kwargs=kwargs)

    def set_output_enabled(self, **kwargs):
        return self.call('set_output_enabled', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def get_synchronize_enabled(self, **kwargs):
        return self.call('get_synchronize_enabled', kwargs=kwargs)

    def set_synchronize_enabled(self, **kwargs):
        return self.call('set_synchronize_enabled', kwargs=kwargs)

    def get_synchronize_phase(self, **kwargs):
        return self.call('get_synchronize_phase', kwargs=kwargs)

    def set_synchronize_phase(self, **kwargs):
        return self.call('set_synchronize_phase', kwargs=kwargs)

    def get_synchronize_source(self, **kwargs):
        return self.call('get_synchronize_source', kwargs=kwargs)

    def set_synchronize_source(self, **kwargs):
        return self.call('set_synchronize_source', kwargs=kwargs)

    def get_duty_cycle(self, **kwargs):
        return self.call('get_duty_cycle', kwargs=kwargs)

    def set_duty_cycle(self, **kwargs):
        return self.call('set_duty_cycle', kwargs=kwargs)

    def reset_to_default(self, **kwargs):
        return self.call('reset_to_default', kwargs=kwargs)

    def get_model(self, **kwargs):
        return self.call('get_model', kwargs=kwargs)

    def get_serial(self, **kwargs):
        return self.call('get_serial', kwargs=kwargs)

