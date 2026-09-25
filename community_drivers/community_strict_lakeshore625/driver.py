from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictLakeshore625(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Lakeshore/Model_625.py', 'class_name': 'Lakeshore625', 'import_roots': ['src'], 'candidate_methods': ['set_field', 'get_current_limit', 'set_current_limit', 'get_voltage_limit', 'set_voltage_limit', 'get_current_rate_limit', 'set_current_rate_limit', 'get_voltage', 'set_voltage', 'get_current', 'set_current', 'get_current_ramp_rate', 'set_current_ramp_rate', 'get_ramp_segments', 'set_ramp_segments', 'get_persistent_switch_heater', 'set_persistent_switch_heater', 'get_quench_detection', 'set_quench_detection', 'get_quench_current_step_limit', 'set_quench_current_step_limit', 'get_ramping_state', 'get_operational_error_status', 'get_oer_quench', 'get_coil_constant_unit', 'set_coil_constant_unit', 'get_coil_constant', 'set_coil_constant', 'get_field', 'get_field_ramp_rate', 'set_field_ramp_rate', 'get_persistent_switch_heater_state', 'set_persistent_switch_heater_state', 'get_persistent_switch_heater_last_turn_off_current'], 'action_targets': {'set_field': '__qcodes_param_set__field', 'get_current_limit': '__qcodes_param_get__current_limit', 'set_current_limit': '__qcodes_param_set__current_limit', 'get_voltage_limit': '__qcodes_param_get__voltage_limit', 'set_voltage_limit': '__qcodes_param_set__voltage_limit', 'get_current_rate_limit': '__qcodes_param_get__current_rate_limit', 'set_current_rate_limit': '__qcodes_param_set__current_rate_limit', 'get_voltage': '__qcodes_param_get__voltage', 'set_voltage': '__qcodes_param_set__voltage', 'get_current': '__qcodes_param_get__current', 'set_current': '__qcodes_param_set__current', 'get_current_ramp_rate': '__qcodes_param_get__current_ramp_rate', 'set_current_ramp_rate': '__qcodes_param_set__current_ramp_rate', 'get_ramp_segments': '__qcodes_param_get__ramp_segments', 'set_ramp_segments': '__qcodes_param_set__ramp_segments', 'get_persistent_switch_heater': '__qcodes_param_get__persistent_switch_heater', 'set_persistent_switch_heater': '__qcodes_param_set__persistent_switch_heater', 'get_quench_detection': '__qcodes_param_get__quench_detection', 'set_quench_detection': '__qcodes_param_set__quench_detection', 'get_quench_current_step_limit': '__qcodes_param_get__quench_current_step_limit', 'set_quench_current_step_limit': '__qcodes_param_set__quench_current_step_limit', 'get_ramping_state': '__qcodes_param_get__ramping_state', 'get_operational_error_status': '__qcodes_param_get__operational_error_status', 'get_oer_quench': '__qcodes_param_get__oer_quench', 'get_coil_constant_unit': '__qcodes_param_get__coil_constant_unit', 'set_coil_constant_unit': '__qcodes_param_set__coil_constant_unit', 'get_coil_constant': '__qcodes_param_get__coil_constant', 'set_coil_constant': '__qcodes_param_set__coil_constant', 'get_field': '__qcodes_param_get__field', 'get_field_ramp_rate': '__qcodes_param_get__field_ramp_rate', 'set_field_ramp_rate': '__qcodes_param_set__field_ramp_rate', 'get_persistent_switch_heater_state': '__qcodes_param_get__persistent_switch_heater_state', 'set_persistent_switch_heater_state': '__qcodes_param_set__persistent_switch_heater_state', 'get_persistent_switch_heater_last_turn_off_current': '__qcodes_param_get__persistent_switch_heater_last_turn_off_current'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Lakeshore/Model_625.py', 'confidence': 0.8, 'quality_score': 0.88, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'set_field': '__qcodes_param_set__field', 'get_current_limit': '__qcodes_param_get__current_limit', 'set_current_limit': '__qcodes_param_set__current_limit', 'get_voltage_limit': '__qcodes_param_get__voltage_limit', 'set_voltage_limit': '__qcodes_param_set__voltage_limit', 'get_current_rate_limit': '__qcodes_param_get__current_rate_limit', 'set_current_rate_limit': '__qcodes_param_set__current_rate_limit', 'get_voltage': '__qcodes_param_get__voltage', 'set_voltage': '__qcodes_param_set__voltage', 'get_current': '__qcodes_param_get__current', 'set_current': '__qcodes_param_set__current', 'get_current_ramp_rate': '__qcodes_param_get__current_ramp_rate', 'set_current_ramp_rate': '__qcodes_param_set__current_ramp_rate', 'get_ramp_segments': '__qcodes_param_get__ramp_segments', 'set_ramp_segments': '__qcodes_param_set__ramp_segments', 'get_persistent_switch_heater': '__qcodes_param_get__persistent_switch_heater', 'set_persistent_switch_heater': '__qcodes_param_set__persistent_switch_heater', 'get_quench_detection': '__qcodes_param_get__quench_detection', 'set_quench_detection': '__qcodes_param_set__quench_detection', 'get_quench_current_step_limit': '__qcodes_param_get__quench_current_step_limit', 'set_quench_current_step_limit': '__qcodes_param_set__quench_current_step_limit', 'get_ramping_state': '__qcodes_param_get__ramping_state', 'get_operational_error_status': '__qcodes_param_get__operational_error_status', 'get_oer_quench': '__qcodes_param_get__oer_quench', 'get_coil_constant_unit': '__qcodes_param_get__coil_constant_unit', 'set_coil_constant_unit': '__qcodes_param_set__coil_constant_unit', 'get_coil_constant': '__qcodes_param_get__coil_constant', 'set_coil_constant': '__qcodes_param_set__coil_constant', 'get_field': '__qcodes_param_get__field', 'get_field_ramp_rate': '__qcodes_param_get__field_ramp_rate', 'set_field_ramp_rate': '__qcodes_param_set__field_ramp_rate', 'get_persistent_switch_heater_state': '__qcodes_param_get__persistent_switch_heater_state', 'set_persistent_switch_heater_state': '__qcodes_param_set__persistent_switch_heater_state', 'get_persistent_switch_heater_last_turn_off_current': '__qcodes_param_get__persistent_switch_heater_last_turn_off_current'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def set_field(self, **kwargs):
        return self.call('set_field', kwargs=kwargs)

    def get_current_limit(self, **kwargs):
        return self.call('get_current_limit', kwargs=kwargs)

    def set_current_limit(self, **kwargs):
        return self.call('set_current_limit', kwargs=kwargs)

    def get_voltage_limit(self, **kwargs):
        return self.call('get_voltage_limit', kwargs=kwargs)

    def set_voltage_limit(self, **kwargs):
        return self.call('set_voltage_limit', kwargs=kwargs)

    def get_current_rate_limit(self, **kwargs):
        return self.call('get_current_rate_limit', kwargs=kwargs)

    def set_current_rate_limit(self, **kwargs):
        return self.call('set_current_rate_limit', kwargs=kwargs)

    def get_voltage(self, **kwargs):
        return self.call('get_voltage', kwargs=kwargs)

    def set_voltage(self, **kwargs):
        return self.call('set_voltage', kwargs=kwargs)

    def get_current(self, **kwargs):
        return self.call('get_current', kwargs=kwargs)

    def set_current(self, **kwargs):
        return self.call('set_current', kwargs=kwargs)

    def get_current_ramp_rate(self, **kwargs):
        return self.call('get_current_ramp_rate', kwargs=kwargs)

    def set_current_ramp_rate(self, **kwargs):
        return self.call('set_current_ramp_rate', kwargs=kwargs)

    def get_ramp_segments(self, **kwargs):
        return self.call('get_ramp_segments', kwargs=kwargs)

    def set_ramp_segments(self, **kwargs):
        return self.call('set_ramp_segments', kwargs=kwargs)

    def get_persistent_switch_heater(self, **kwargs):
        return self.call('get_persistent_switch_heater', kwargs=kwargs)

    def set_persistent_switch_heater(self, **kwargs):
        return self.call('set_persistent_switch_heater', kwargs=kwargs)

    def get_quench_detection(self, **kwargs):
        return self.call('get_quench_detection', kwargs=kwargs)

    def set_quench_detection(self, **kwargs):
        return self.call('set_quench_detection', kwargs=kwargs)

    def get_quench_current_step_limit(self, **kwargs):
        return self.call('get_quench_current_step_limit', kwargs=kwargs)

    def set_quench_current_step_limit(self, **kwargs):
        return self.call('set_quench_current_step_limit', kwargs=kwargs)

    def get_ramping_state(self, **kwargs):
        return self.call('get_ramping_state', kwargs=kwargs)

    def get_operational_error_status(self, **kwargs):
        return self.call('get_operational_error_status', kwargs=kwargs)

    def get_oer_quench(self, **kwargs):
        return self.call('get_oer_quench', kwargs=kwargs)

    def get_coil_constant_unit(self, **kwargs):
        return self.call('get_coil_constant_unit', kwargs=kwargs)

    def set_coil_constant_unit(self, **kwargs):
        return self.call('set_coil_constant_unit', kwargs=kwargs)

    def get_coil_constant(self, **kwargs):
        return self.call('get_coil_constant', kwargs=kwargs)

    def set_coil_constant(self, **kwargs):
        return self.call('set_coil_constant', kwargs=kwargs)

    def get_field(self, **kwargs):
        return self.call('get_field', kwargs=kwargs)

    def get_field_ramp_rate(self, **kwargs):
        return self.call('get_field_ramp_rate', kwargs=kwargs)

    def set_field_ramp_rate(self, **kwargs):
        return self.call('set_field_ramp_rate', kwargs=kwargs)

    def get_persistent_switch_heater_state(self, **kwargs):
        return self.call('get_persistent_switch_heater_state', kwargs=kwargs)

    def set_persistent_switch_heater_state(self, **kwargs):
        return self.call('set_persistent_switch_heater_state', kwargs=kwargs)

    def get_persistent_switch_heater_last_turn_off_current(self, **kwargs):
        return self.call('get_persistent_switch_heater_last_turn_off_current', kwargs=kwargs)

