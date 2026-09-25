from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictThorlabstdc001(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Thorlabs/TDC001.py', 'class_name': 'Thorlabs_TDC001', 'import_roots': ['src'], 'candidate_methods': ['identify', 'get_idn', 'go_home', 'wait_for_completion', 'is_moving', 'move_to', 'move_by', 'move_continuous', 'jog', 'stop', 'close', 'get_position', 'set_position', 'get_max_position', 'set_max_position', 'get_min_position', 'set_min_position', 'get_velocity', 'set_velocity', 'get_jog_velocity', 'set_jog_velocity', 'get_homing_velocity', 'set_homing_velocity', 'get_acceleration', 'set_acceleration', 'get_jog_acceleration', 'set_jog_acceleration', 'get_jog_mode', 'set_jog_mode', 'get_jog_step_size', 'set_jog_step_size', 'get_stop_mode', 'set_stop_mode', 'get_soft_limits_mode', 'set_soft_limits_mode', 'get_backlash', 'set_backlash', 'enable_simulation', 'disable_simulation'], 'action_targets': {'get_position': '__qcodes_param_get__position', 'set_position': '__qcodes_param_set__position', 'get_max_position': '__qcodes_param_get__max_position', 'set_max_position': '__qcodes_param_set__max_position', 'get_min_position': '__qcodes_param_get__min_position', 'set_min_position': '__qcodes_param_set__min_position', 'get_velocity': '__qcodes_param_get__velocity', 'set_velocity': '__qcodes_param_set__velocity', 'get_jog_velocity': '__qcodes_param_get__jog_velocity', 'set_jog_velocity': '__qcodes_param_set__jog_velocity', 'get_homing_velocity': '__qcodes_param_get__homing_velocity', 'set_homing_velocity': '__qcodes_param_set__homing_velocity', 'get_acceleration': '__qcodes_param_get__acceleration', 'set_acceleration': '__qcodes_param_set__acceleration', 'get_jog_acceleration': '__qcodes_param_get__jog_acceleration', 'set_jog_acceleration': '__qcodes_param_set__jog_acceleration', 'get_jog_mode': '__qcodes_param_get__jog_mode', 'set_jog_mode': '__qcodes_param_set__jog_mode', 'get_jog_step_size': '__qcodes_param_get__jog_step_size', 'set_jog_step_size': '__qcodes_param_set__jog_step_size', 'get_stop_mode': '__qcodes_param_get__stop_mode', 'set_stop_mode': '__qcodes_param_set__stop_mode', 'get_soft_limits_mode': '__qcodes_param_get__soft_limits_mode', 'set_soft_limits_mode': '__qcodes_param_set__soft_limits_mode', 'get_backlash': '__qcodes_param_get__backlash', 'set_backlash': '__qcodes_param_set__backlash'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Thorlabs/TDC001.py', 'confidence': 0.9, 'quality_score': 1.06, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_position': '__qcodes_param_get__position', 'set_position': '__qcodes_param_set__position', 'get_max_position': '__qcodes_param_get__max_position', 'set_max_position': '__qcodes_param_set__max_position', 'get_min_position': '__qcodes_param_get__min_position', 'set_min_position': '__qcodes_param_set__min_position', 'get_velocity': '__qcodes_param_get__velocity', 'set_velocity': '__qcodes_param_set__velocity', 'get_jog_velocity': '__qcodes_param_get__jog_velocity', 'set_jog_velocity': '__qcodes_param_set__jog_velocity', 'get_homing_velocity': '__qcodes_param_get__homing_velocity', 'set_homing_velocity': '__qcodes_param_set__homing_velocity', 'get_acceleration': '__qcodes_param_get__acceleration', 'set_acceleration': '__qcodes_param_set__acceleration', 'get_jog_acceleration': '__qcodes_param_get__jog_acceleration', 'set_jog_acceleration': '__qcodes_param_set__jog_acceleration', 'get_jog_mode': '__qcodes_param_get__jog_mode', 'set_jog_mode': '__qcodes_param_set__jog_mode', 'get_jog_step_size': '__qcodes_param_get__jog_step_size', 'set_jog_step_size': '__qcodes_param_set__jog_step_size', 'get_stop_mode': '__qcodes_param_get__stop_mode', 'set_stop_mode': '__qcodes_param_set__stop_mode', 'get_soft_limits_mode': '__qcodes_param_get__soft_limits_mode', 'set_soft_limits_mode': '__qcodes_param_set__soft_limits_mode', 'get_backlash': '__qcodes_param_get__backlash', 'set_backlash': '__qcodes_param_set__backlash'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def identify(self, **kwargs):
        return self.call('identify', kwargs=kwargs)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def go_home(self, **kwargs):
        return self.call('go_home', kwargs=kwargs)

    def wait_for_completion(self, **kwargs):
        return self.call('wait_for_completion', kwargs=kwargs)

    def is_moving(self, **kwargs):
        return self.call('is_moving', kwargs=kwargs)

    def move_to(self, **kwargs):
        return self.call('move_to', kwargs=kwargs)

    def move_by(self, **kwargs):
        return self.call('move_by', kwargs=kwargs)

    def move_continuous(self, **kwargs):
        return self.call('move_continuous', kwargs=kwargs)

    def jog(self, **kwargs):
        return self.call('jog', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def get_position(self, **kwargs):
        return self.call('get_position', kwargs=kwargs)

    def set_position(self, **kwargs):
        return self.call('set_position', kwargs=kwargs)

    def get_max_position(self, **kwargs):
        return self.call('get_max_position', kwargs=kwargs)

    def set_max_position(self, **kwargs):
        return self.call('set_max_position', kwargs=kwargs)

    def get_min_position(self, **kwargs):
        return self.call('get_min_position', kwargs=kwargs)

    def set_min_position(self, **kwargs):
        return self.call('set_min_position', kwargs=kwargs)

    def get_velocity(self, **kwargs):
        return self.call('get_velocity', kwargs=kwargs)

    def set_velocity(self, **kwargs):
        return self.call('set_velocity', kwargs=kwargs)

    def get_jog_velocity(self, **kwargs):
        return self.call('get_jog_velocity', kwargs=kwargs)

    def set_jog_velocity(self, **kwargs):
        return self.call('set_jog_velocity', kwargs=kwargs)

    def get_homing_velocity(self, **kwargs):
        return self.call('get_homing_velocity', kwargs=kwargs)

    def set_homing_velocity(self, **kwargs):
        return self.call('set_homing_velocity', kwargs=kwargs)

    def get_acceleration(self, **kwargs):
        return self.call('get_acceleration', kwargs=kwargs)

    def set_acceleration(self, **kwargs):
        return self.call('set_acceleration', kwargs=kwargs)

    def get_jog_acceleration(self, **kwargs):
        return self.call('get_jog_acceleration', kwargs=kwargs)

    def set_jog_acceleration(self, **kwargs):
        return self.call('set_jog_acceleration', kwargs=kwargs)

    def get_jog_mode(self, **kwargs):
        return self.call('get_jog_mode', kwargs=kwargs)

    def set_jog_mode(self, **kwargs):
        return self.call('set_jog_mode', kwargs=kwargs)

    def get_jog_step_size(self, **kwargs):
        return self.call('get_jog_step_size', kwargs=kwargs)

    def set_jog_step_size(self, **kwargs):
        return self.call('set_jog_step_size', kwargs=kwargs)

    def get_stop_mode(self, **kwargs):
        return self.call('get_stop_mode', kwargs=kwargs)

    def set_stop_mode(self, **kwargs):
        return self.call('set_stop_mode', kwargs=kwargs)

    def get_soft_limits_mode(self, **kwargs):
        return self.call('get_soft_limits_mode', kwargs=kwargs)

    def set_soft_limits_mode(self, **kwargs):
        return self.call('set_soft_limits_mode', kwargs=kwargs)

    def get_backlash(self, **kwargs):
        return self.call('get_backlash', kwargs=kwargs)

    def set_backlash(self, **kwargs):
        return self.call('set_backlash', kwargs=kwargs)

    def enable_simulation(self, **kwargs):
        return self.call('enable_simulation', kwargs=kwargs)

    def disable_simulation(self, **kwargs):
        return self.call('disable_simulation', kwargs=kwargs)

