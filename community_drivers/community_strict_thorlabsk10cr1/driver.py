from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictThorlabsk10cr1(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Thorlabs/K10CR1.py', 'class_name': 'Thorlabs_K10CR1', 'import_roots': ['src'], 'candidate_methods': ['get_idn', 'get_position', 'set_position', 'set_position_async', 'get_velocity_min', 'set_velocity_min', 'get_velocity_acceleration', 'set_velocity_acceleration', 'get_velocity_max', 'set_velocity_max', 'get_move_home_direction', 'set_move_home_direction', 'get_move_home_limit_switch', 'set_move_home_limit_switch', 'get_move_home_velocity', 'set_move_home_velocity', 'get_move_home_zero_offset', 'set_move_home_zero_offset'], 'action_targets': {'get_position': '__qcodes_param_get__position', 'set_position': '__qcodes_param_set__position', 'set_position_async': '__qcodes_param_set__position_async', 'get_velocity_min': '__qcodes_param_get__velocity_min', 'set_velocity_min': '__qcodes_param_set__velocity_min', 'get_velocity_acceleration': '__qcodes_param_get__velocity_acceleration', 'set_velocity_acceleration': '__qcodes_param_set__velocity_acceleration', 'get_velocity_max': '__qcodes_param_get__velocity_max', 'set_velocity_max': '__qcodes_param_set__velocity_max', 'get_move_home_direction': '__qcodes_param_get__move_home_direction', 'set_move_home_direction': '__qcodes_param_set__move_home_direction', 'get_move_home_limit_switch': '__qcodes_param_get__move_home_limit_switch', 'set_move_home_limit_switch': '__qcodes_param_set__move_home_limit_switch', 'get_move_home_velocity': '__qcodes_param_get__move_home_velocity', 'set_move_home_velocity': '__qcodes_param_set__move_home_velocity', 'get_move_home_zero_offset': '__qcodes_param_get__move_home_zero_offset', 'set_move_home_zero_offset': '__qcodes_param_set__move_home_zero_offset'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Thorlabs/K10CR1.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_position': '__qcodes_param_get__position', 'set_position': '__qcodes_param_set__position', 'set_position_async': '__qcodes_param_set__position_async', 'get_velocity_min': '__qcodes_param_get__velocity_min', 'set_velocity_min': '__qcodes_param_set__velocity_min', 'get_velocity_acceleration': '__qcodes_param_get__velocity_acceleration', 'set_velocity_acceleration': '__qcodes_param_set__velocity_acceleration', 'get_velocity_max': '__qcodes_param_get__velocity_max', 'set_velocity_max': '__qcodes_param_set__velocity_max', 'get_move_home_direction': '__qcodes_param_get__move_home_direction', 'set_move_home_direction': '__qcodes_param_set__move_home_direction', 'get_move_home_limit_switch': '__qcodes_param_get__move_home_limit_switch', 'set_move_home_limit_switch': '__qcodes_param_set__move_home_limit_switch', 'get_move_home_velocity': '__qcodes_param_get__move_home_velocity', 'set_move_home_velocity': '__qcodes_param_set__move_home_velocity', 'get_move_home_zero_offset': '__qcodes_param_get__move_home_zero_offset', 'set_move_home_zero_offset': '__qcodes_param_set__move_home_zero_offset'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def get_position(self, **kwargs):
        return self.call('get_position', kwargs=kwargs)

    def set_position(self, **kwargs):
        return self.call('set_position', kwargs=kwargs)

    def set_position_async(self, **kwargs):
        return self.call('set_position_async', kwargs=kwargs)

    def get_velocity_min(self, **kwargs):
        return self.call('get_velocity_min', kwargs=kwargs)

    def set_velocity_min(self, **kwargs):
        return self.call('set_velocity_min', kwargs=kwargs)

    def get_velocity_acceleration(self, **kwargs):
        return self.call('get_velocity_acceleration', kwargs=kwargs)

    def set_velocity_acceleration(self, **kwargs):
        return self.call('set_velocity_acceleration', kwargs=kwargs)

    def get_velocity_max(self, **kwargs):
        return self.call('get_velocity_max', kwargs=kwargs)

    def set_velocity_max(self, **kwargs):
        return self.call('set_velocity_max', kwargs=kwargs)

    def get_move_home_direction(self, **kwargs):
        return self.call('get_move_home_direction', kwargs=kwargs)

    def set_move_home_direction(self, **kwargs):
        return self.call('set_move_home_direction', kwargs=kwargs)

    def get_move_home_limit_switch(self, **kwargs):
        return self.call('get_move_home_limit_switch', kwargs=kwargs)

    def set_move_home_limit_switch(self, **kwargs):
        return self.call('set_move_home_limit_switch', kwargs=kwargs)

    def get_move_home_velocity(self, **kwargs):
        return self.call('get_move_home_velocity', kwargs=kwargs)

    def set_move_home_velocity(self, **kwargs):
        return self.call('set_move_home_velocity', kwargs=kwargs)

    def get_move_home_zero_offset(self, **kwargs):
        return self.call('get_move_home_zero_offset', kwargs=kwargs)

    def set_move_home_zero_offset(self, **kwargs):
        return self.call('set_move_home_zero_offset', kwargs=kwargs)

