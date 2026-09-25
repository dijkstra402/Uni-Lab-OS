from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentFrankaEmikaPanda(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/iamlab-cmu__frankapy', 'source_file': 'frankapy/franka_arm.py', 'class_name': 'FrankaArm', 'import_roots': [], 'candidate_methods': ['wait_for_franka_interface', 'wait_for_skill', 'wait_for_gripper', 'is_skill_done', 'stop_skill', 'goto_pose', 'goto_pose_delta', 'goto_joints', 'execute_cartesian_velocities', 'execute_joint_velocities', 'execute_joint_torques', 'execute_joint_dmp', 'execute_pose_dmp', 'execute_quaternion_pose_dmp', 'apply_effector_forces_torques', 'apply_effector_forces_along_axis', 'goto_gripper', 'selective_guidance_mode', 'open_gripper', 'close_gripper', 'home_gripper', 'stop_gripper', 'run_guide_mode', 'run_dynamic_force_position', 'get_robot_state', 'get_pose', 'get_joints', 'get_joint_torques', 'get_joint_velocities', 'get_gripper_width', 'get_gripper_is_grasped', 'get_tool_base_pose', 'get_ee_force_torque', 'get_finger_poses', 'set_tool_delta_pose', 'get_links_transforms', 'get_jacobian', 'get_collision_boxes_poses', 'publish_sensor_values', 'publish_joints', 'publish_collision_boxes', 'check_box_collision', 'is_joints_in_collision_with_boxes', 'reset_joints', 'reset_pose', 'is_joints_reachable', 'apply_joint_torques', 'set_speed', 'get_speed'], 'action_targets': {}, 'metadata': {'repo': 'iamlab-cmu/frankapy', 'repo_url': 'https://github.com/iamlab-cmu/frankapy', 'brand': 'Franka Emika', 'model': 'Panda', 'device_type_cn': '协作机械臂', 'device_type_en': 'Collaborative Robot', 'source_framework': '机器人/运动控制', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 470, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def wait_for_franka_interface(self, **kwargs):
        return self.call('wait_for_franka_interface', kwargs=kwargs)

    def wait_for_skill(self, **kwargs):
        return self.call('wait_for_skill', kwargs=kwargs)

    def wait_for_gripper(self, **kwargs):
        return self.call('wait_for_gripper', kwargs=kwargs)

    def is_skill_done(self, **kwargs):
        return self.call('is_skill_done', kwargs=kwargs)

    def stop_skill(self, **kwargs):
        return self.call('stop_skill', kwargs=kwargs)

    def goto_pose(self, **kwargs):
        return self.call('goto_pose', kwargs=kwargs)

    def goto_pose_delta(self, **kwargs):
        return self.call('goto_pose_delta', kwargs=kwargs)

    def goto_joints(self, **kwargs):
        return self.call('goto_joints', kwargs=kwargs)

    def execute_cartesian_velocities(self, **kwargs):
        return self.call('execute_cartesian_velocities', kwargs=kwargs)

    def execute_joint_velocities(self, **kwargs):
        return self.call('execute_joint_velocities', kwargs=kwargs)

    def execute_joint_torques(self, **kwargs):
        return self.call('execute_joint_torques', kwargs=kwargs)

    def execute_joint_dmp(self, **kwargs):
        return self.call('execute_joint_dmp', kwargs=kwargs)

    def execute_pose_dmp(self, **kwargs):
        return self.call('execute_pose_dmp', kwargs=kwargs)

    def execute_quaternion_pose_dmp(self, **kwargs):
        return self.call('execute_quaternion_pose_dmp', kwargs=kwargs)

    def apply_effector_forces_torques(self, **kwargs):
        return self.call('apply_effector_forces_torques', kwargs=kwargs)

    def apply_effector_forces_along_axis(self, **kwargs):
        return self.call('apply_effector_forces_along_axis', kwargs=kwargs)

    def goto_gripper(self, **kwargs):
        return self.call('goto_gripper', kwargs=kwargs)

    def selective_guidance_mode(self, **kwargs):
        return self.call('selective_guidance_mode', kwargs=kwargs)

    def open_gripper(self, **kwargs):
        return self.call('open_gripper', kwargs=kwargs)

    def close_gripper(self, **kwargs):
        return self.call('close_gripper', kwargs=kwargs)

    def home_gripper(self, **kwargs):
        return self.call('home_gripper', kwargs=kwargs)

    def stop_gripper(self, **kwargs):
        return self.call('stop_gripper', kwargs=kwargs)

    def run_guide_mode(self, **kwargs):
        return self.call('run_guide_mode', kwargs=kwargs)

    def run_dynamic_force_position(self, **kwargs):
        return self.call('run_dynamic_force_position', kwargs=kwargs)

    def get_robot_state(self, **kwargs):
        return self.call('get_robot_state', kwargs=kwargs)

    def get_pose(self, **kwargs):
        return self.call('get_pose', kwargs=kwargs)

    def get_joints(self, **kwargs):
        return self.call('get_joints', kwargs=kwargs)

    def get_joint_torques(self, **kwargs):
        return self.call('get_joint_torques', kwargs=kwargs)

    def get_joint_velocities(self, **kwargs):
        return self.call('get_joint_velocities', kwargs=kwargs)

    def get_gripper_width(self, **kwargs):
        return self.call('get_gripper_width', kwargs=kwargs)

    def get_gripper_is_grasped(self, **kwargs):
        return self.call('get_gripper_is_grasped', kwargs=kwargs)

    def get_tool_base_pose(self, **kwargs):
        return self.call('get_tool_base_pose', kwargs=kwargs)

    def get_ee_force_torque(self, **kwargs):
        return self.call('get_ee_force_torque', kwargs=kwargs)

    def get_finger_poses(self, **kwargs):
        return self.call('get_finger_poses', kwargs=kwargs)

    def set_tool_delta_pose(self, **kwargs):
        return self.call('set_tool_delta_pose', kwargs=kwargs)

    def get_links_transforms(self, **kwargs):
        return self.call('get_links_transforms', kwargs=kwargs)

    def get_jacobian(self, **kwargs):
        return self.call('get_jacobian', kwargs=kwargs)

    def get_collision_boxes_poses(self, **kwargs):
        return self.call('get_collision_boxes_poses', kwargs=kwargs)

    def publish_sensor_values(self, **kwargs):
        return self.call('publish_sensor_values', kwargs=kwargs)

    def publish_joints(self, **kwargs):
        return self.call('publish_joints', kwargs=kwargs)

    def publish_collision_boxes(self, **kwargs):
        return self.call('publish_collision_boxes', kwargs=kwargs)

    def check_box_collision(self, **kwargs):
        return self.call('check_box_collision', kwargs=kwargs)

    def is_joints_in_collision_with_boxes(self, **kwargs):
        return self.call('is_joints_in_collision_with_boxes', kwargs=kwargs)

    def reset_joints(self, **kwargs):
        return self.call('reset_joints', kwargs=kwargs)

    def reset_pose(self, **kwargs):
        return self.call('reset_pose', kwargs=kwargs)

    def is_joints_reachable(self, **kwargs):
        return self.call('is_joints_reachable', kwargs=kwargs)

    def apply_joint_torques(self, **kwargs):
        return self.call('apply_joint_torques', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

    def get_speed(self, **kwargs):
        return self.call('get_speed', kwargs=kwargs)

