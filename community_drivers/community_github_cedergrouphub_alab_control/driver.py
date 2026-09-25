from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubCedergrouphubAlabControl(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/CederGroupHub_alab_control', 'source_file': 'alab_control/dh_robotic_gripper/dh_robotic_gripper.py', 'class_name': 'GripperController', 'import_roots': [], 'candidate_methods': ['load_defaults', 'set_rotating_blocking', 'initialize', 'save_configuration', 'check_initialization', 'set_gripper_force', 'set_gripper_position', 'set_gripper_speed', 'read_gripper_position', 'read_gripper_status', 'set_rotation_speed', 'set_rotation_force', 'set_rotation_angle', 'stop_rotation', 'read_rotation_status', 'read_current_angle', 'rotate', 'grasp', 'open_to', 'close'], 'metadata': {'repo': 'cedergrouphub/alab_control', 'repo_url': 'https://github.com/CederGroupHub/alab_control', 'unit_id': 'gh_eurotherm_2416', 'source_file': 'alab_control/dh_robotic_gripper/dh_robotic_gripper.py', 'candidate_score': 113, 'manufacturer': 'Eurotherm', 'model_name': 'Eurotherm 2416'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def load_defaults(self, **kwargs):
        return self.call('load_defaults', kwargs=kwargs)

    def set_rotating_blocking(self, **kwargs):
        return self.call('set_rotating_blocking', kwargs=kwargs)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def save_configuration(self, **kwargs):
        return self.call('save_configuration', kwargs=kwargs)

    def check_initialization(self, **kwargs):
        return self.call('check_initialization', kwargs=kwargs)

    def set_gripper_force(self, **kwargs):
        return self.call('set_gripper_force', kwargs=kwargs)

    def set_gripper_position(self, **kwargs):
        return self.call('set_gripper_position', kwargs=kwargs)

    def set_gripper_speed(self, **kwargs):
        return self.call('set_gripper_speed', kwargs=kwargs)

    def read_gripper_position(self, **kwargs):
        return self.call('read_gripper_position', kwargs=kwargs)

    def read_gripper_status(self, **kwargs):
        return self.call('read_gripper_status', kwargs=kwargs)

    def set_rotation_speed(self, **kwargs):
        return self.call('set_rotation_speed', kwargs=kwargs)

    def set_rotation_force(self, **kwargs):
        return self.call('set_rotation_force', kwargs=kwargs)

    def set_rotation_angle(self, **kwargs):
        return self.call('set_rotation_angle', kwargs=kwargs)

    def stop_rotation(self, **kwargs):
        return self.call('stop_rotation', kwargs=kwargs)

    def read_rotation_status(self, **kwargs):
        return self.call('read_rotation_status', kwargs=kwargs)

    def read_current_angle(self, **kwargs):
        return self.call('read_current_angle', kwargs=kwargs)

    def rotate(self, **kwargs):
        return self.call('rotate', kwargs=kwargs)

    def grasp(self, **kwargs):
        return self.call('grasp', kwargs=kwargs)

    def open_to(self, **kwargs):
        return self.call('open_to', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

