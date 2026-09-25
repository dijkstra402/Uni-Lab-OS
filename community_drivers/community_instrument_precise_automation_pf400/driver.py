from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPreciseAutomationPf400(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AD-SDL__pf400_module_ros', 'source_file': 'pf400_driver/pf400_driver/pf400_driver.py', 'class_name': 'PF400', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'send_command', 'init_connection_mode', 'handle_error_output', 'check_robot_state', 'enable_power', 'disable_power', 'attach_robot', 'home_robot', 'initialize_robot', 'force_initialize_robot', 'status_port_initilization', 'refresh_joint_state', 'get_robot_movement_state', 'get_overall_state', 'get_joint_states', 'get_cartesian_coordinates', 'get_gripper_lenght', 'get_gripper_state', 'set_profile', 'set_gripper_open', 'set_gripper_close', 'set_plate_rotation', 'check_incorrect_plate_orientation', 'move_joint', 'move_cartesian', 'move_in_one_axis_from_target', 'move_in_one_axis', 'grab_plate', 'release_plate', 'gripper_open', 'gripper_close', 'move_one_joint', 'move_multiple_joint', 'move_gripper_safe_zone', 'move_gripper_neutral', 'move_arm_neutral', 'move_rails_neutral', 'move_all_joints_neutral', 'remove_lid', 'replace_lid', 'rotate_plate_on_deck', 'pick_plate', 'place_plate', 'transfer', 'forward_kinematics', 'inverse_kinematics'], 'action_targets': {}, 'metadata': {'repo': 'AD-SDL/pf400_module_ros', 'repo_url': 'https://github.com/AD-SDL/pf400_module_ros', 'brand': 'Precise Automation', 'model': 'PF400', 'device_type_cn': '协作机器人臂', 'device_type_en': 'Collaborative Robot Arm', 'source_framework': '生命科学', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 448, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def init_connection_mode(self, **kwargs):
        return self.call('init_connection_mode', kwargs=kwargs)

    def handle_error_output(self, **kwargs):
        return self.call('handle_error_output', kwargs=kwargs)

    def check_robot_state(self, **kwargs):
        return self.call('check_robot_state', kwargs=kwargs)

    def enable_power(self, **kwargs):
        return self.call('enable_power', kwargs=kwargs)

    def disable_power(self, **kwargs):
        return self.call('disable_power', kwargs=kwargs)

    def attach_robot(self, **kwargs):
        return self.call('attach_robot', kwargs=kwargs)

    def home_robot(self, **kwargs):
        return self.call('home_robot', kwargs=kwargs)

    def initialize_robot(self, **kwargs):
        return self.call('initialize_robot', kwargs=kwargs)

    def force_initialize_robot(self, **kwargs):
        return self.call('force_initialize_robot', kwargs=kwargs)

    def status_port_initilization(self, **kwargs):
        return self.call('status_port_initilization', kwargs=kwargs)

    def refresh_joint_state(self, **kwargs):
        return self.call('refresh_joint_state', kwargs=kwargs)

    def get_robot_movement_state(self, **kwargs):
        return self.call('get_robot_movement_state', kwargs=kwargs)

    def get_overall_state(self, **kwargs):
        return self.call('get_overall_state', kwargs=kwargs)

    def get_joint_states(self, **kwargs):
        return self.call('get_joint_states', kwargs=kwargs)

    def get_cartesian_coordinates(self, **kwargs):
        return self.call('get_cartesian_coordinates', kwargs=kwargs)

    def get_gripper_lenght(self, **kwargs):
        return self.call('get_gripper_lenght', kwargs=kwargs)

    def get_gripper_state(self, **kwargs):
        return self.call('get_gripper_state', kwargs=kwargs)

    def set_profile(self, **kwargs):
        return self.call('set_profile', kwargs=kwargs)

    def set_gripper_open(self, **kwargs):
        return self.call('set_gripper_open', kwargs=kwargs)

    def set_gripper_close(self, **kwargs):
        return self.call('set_gripper_close', kwargs=kwargs)

    def set_plate_rotation(self, **kwargs):
        return self.call('set_plate_rotation', kwargs=kwargs)

    def check_incorrect_plate_orientation(self, **kwargs):
        return self.call('check_incorrect_plate_orientation', kwargs=kwargs)

    def move_joint(self, **kwargs):
        return self.call('move_joint', kwargs=kwargs)

    def move_cartesian(self, **kwargs):
        return self.call('move_cartesian', kwargs=kwargs)

    def move_in_one_axis_from_target(self, **kwargs):
        return self.call('move_in_one_axis_from_target', kwargs=kwargs)

    def move_in_one_axis(self, **kwargs):
        return self.call('move_in_one_axis', kwargs=kwargs)

    def grab_plate(self, **kwargs):
        return self.call('grab_plate', kwargs=kwargs)

    def release_plate(self, **kwargs):
        return self.call('release_plate', kwargs=kwargs)

    def gripper_open(self, **kwargs):
        return self.call('gripper_open', kwargs=kwargs)

    def gripper_close(self, **kwargs):
        return self.call('gripper_close', kwargs=kwargs)

    def move_one_joint(self, **kwargs):
        return self.call('move_one_joint', kwargs=kwargs)

    def move_multiple_joint(self, **kwargs):
        return self.call('move_multiple_joint', kwargs=kwargs)

    def move_gripper_safe_zone(self, **kwargs):
        return self.call('move_gripper_safe_zone', kwargs=kwargs)

    def move_gripper_neutral(self, **kwargs):
        return self.call('move_gripper_neutral', kwargs=kwargs)

    def move_arm_neutral(self, **kwargs):
        return self.call('move_arm_neutral', kwargs=kwargs)

    def move_rails_neutral(self, **kwargs):
        return self.call('move_rails_neutral', kwargs=kwargs)

    def move_all_joints_neutral(self, **kwargs):
        return self.call('move_all_joints_neutral', kwargs=kwargs)

    def remove_lid(self, **kwargs):
        return self.call('remove_lid', kwargs=kwargs)

    def replace_lid(self, **kwargs):
        return self.call('replace_lid', kwargs=kwargs)

    def rotate_plate_on_deck(self, **kwargs):
        return self.call('rotate_plate_on_deck', kwargs=kwargs)

    def pick_plate(self, **kwargs):
        return self.call('pick_plate', kwargs=kwargs)

    def place_plate(self, **kwargs):
        return self.call('place_plate', kwargs=kwargs)

    def transfer(self, **kwargs):
        return self.call('transfer', kwargs=kwargs)

    def forward_kinematics(self, **kwargs):
        return self.call('forward_kinematics', kwargs=kwargs)

    def inverse_kinematics(self, **kwargs):
        return self.call('inverse_kinematics', kwargs=kwargs)

