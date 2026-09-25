from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictGalildmc4133arm(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes', 'source_file': 'src/qcodes/instrument_drivers/Galil/dmc_41x3.py', 'class_name': 'GalilDMC4133Arm', 'import_roots': ['src'], 'candidate_methods': ['current_row', 'current_pad', 'left_bottom_position', 'left_top_position', 'right_top_position', 'arm_pick_up_distance', 'speed', 'acceleration', 'deceleration', 'set_arm_kinematics', 'set_pick_up_distance', 'set_left_bottom_position', 'set_left_top_position', 'set_right_top_position', 'move_motor_a_by', 'move_motor_b_by', 'move_motor_c_by', 'move_towards_left_bottom_position', 'move_to_next_row', 'move_to_begin_row_pad_from_end_row_last_pad', 'move_to_row', 'move_to_pad', 'set_motor_a_forward_limit', 'set_motor_a_reverse_limit', 'set_motor_b_forward_limit', 'set_motor_b_reverse_limit', 'set_motor_c_forward_limit', 'set_motor_c_reverse_limit'], 'action_targets': {}, 'metadata': {'repo': 'QCoDeS/Qcodes', 'repo_url': 'https://github.com/QCoDeS/Qcodes', 'source_url': 'https://github.com/QCoDeS/Qcodes/blob/main/src/qcodes/instrument_drivers/Galil/dmc_41x3.py', 'confidence': 0.8, 'quality_score': 0.94, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def current_row(self, **kwargs):
        return self.call('current_row', kwargs=kwargs)

    def current_pad(self, **kwargs):
        return self.call('current_pad', kwargs=kwargs)

    def left_bottom_position(self, **kwargs):
        return self.call('left_bottom_position', kwargs=kwargs)

    def left_top_position(self, **kwargs):
        return self.call('left_top_position', kwargs=kwargs)

    def right_top_position(self, **kwargs):
        return self.call('right_top_position', kwargs=kwargs)

    def arm_pick_up_distance(self, **kwargs):
        return self.call('arm_pick_up_distance', kwargs=kwargs)

    def speed(self, **kwargs):
        return self.call('speed', kwargs=kwargs)

    def acceleration(self, **kwargs):
        return self.call('acceleration', kwargs=kwargs)

    def deceleration(self, **kwargs):
        return self.call('deceleration', kwargs=kwargs)

    def set_arm_kinematics(self, **kwargs):
        return self.call('set_arm_kinematics', kwargs=kwargs)

    def set_pick_up_distance(self, **kwargs):
        return self.call('set_pick_up_distance', kwargs=kwargs)

    def set_left_bottom_position(self, **kwargs):
        return self.call('set_left_bottom_position', kwargs=kwargs)

    def set_left_top_position(self, **kwargs):
        return self.call('set_left_top_position', kwargs=kwargs)

    def set_right_top_position(self, **kwargs):
        return self.call('set_right_top_position', kwargs=kwargs)

    def move_motor_a_by(self, **kwargs):
        return self.call('move_motor_a_by', kwargs=kwargs)

    def move_motor_b_by(self, **kwargs):
        return self.call('move_motor_b_by', kwargs=kwargs)

    def move_motor_c_by(self, **kwargs):
        return self.call('move_motor_c_by', kwargs=kwargs)

    def move_towards_left_bottom_position(self, **kwargs):
        return self.call('move_towards_left_bottom_position', kwargs=kwargs)

    def move_to_next_row(self, **kwargs):
        return self.call('move_to_next_row', kwargs=kwargs)

    def move_to_begin_row_pad_from_end_row_last_pad(self, **kwargs):
        return self.call('move_to_begin_row_pad_from_end_row_last_pad', kwargs=kwargs)

    def move_to_row(self, **kwargs):
        return self.call('move_to_row', kwargs=kwargs)

    def move_to_pad(self, **kwargs):
        return self.call('move_to_pad', kwargs=kwargs)

    def set_motor_a_forward_limit(self, **kwargs):
        return self.call('set_motor_a_forward_limit', kwargs=kwargs)

    def set_motor_a_reverse_limit(self, **kwargs):
        return self.call('set_motor_a_reverse_limit', kwargs=kwargs)

    def set_motor_b_forward_limit(self, **kwargs):
        return self.call('set_motor_b_forward_limit', kwargs=kwargs)

    def set_motor_b_reverse_limit(self, **kwargs):
        return self.call('set_motor_b_reverse_limit', kwargs=kwargs)

    def set_motor_c_forward_limit(self, **kwargs):
        return self.call('set_motor_c_forward_limit', kwargs=kwargs)

    def set_motor_c_reverse_limit(self, **kwargs):
        return self.call('set_motor_c_reverse_limit', kwargs=kwargs)

