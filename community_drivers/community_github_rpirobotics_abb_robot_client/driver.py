from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubRpiroboticsAbbRobotClient(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/rpiRobotics_abb_robot_client', 'source_file': 'src/abb_robot_client/rws.py', 'class_name': 'RWS', 'import_roots': [], 'candidate_methods': ['start', 'activate_task', 'deactivate_task', 'stop', 'resetpp', 'get_ramdisk_path', 'get_execution_state', 'get_controller_state', 'set_controller_state', 'get_operation_mode', 'get_digital_io', 'set_digital_io', 'get_analog_io', 'set_analog_io', 'get_rapid_variables', 'get_rapid_variable', 'set_rapid_variable', 'read_file', 'upload_file', 'delete_file'], 'metadata': {'repo': 'rpirobotics/abb_robot_client', 'repo_url': 'https://github.com/rpiRobotics/abb_robot_client', 'unit_id': 'gh_abb_irb_irc5', 'source_file': 'src/abb_robot_client/rws.py', 'candidate_score': 88, 'manufacturer': 'ABB', 'model_name': 'ABB IRB系列 (IRC5)'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def activate_task(self, **kwargs):
        return self.call('activate_task', kwargs=kwargs)

    def deactivate_task(self, **kwargs):
        return self.call('deactivate_task', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def resetpp(self, **kwargs):
        return self.call('resetpp', kwargs=kwargs)

    def get_ramdisk_path(self, **kwargs):
        return self.call('get_ramdisk_path', kwargs=kwargs)

    def get_execution_state(self, **kwargs):
        return self.call('get_execution_state', kwargs=kwargs)

    def get_controller_state(self, **kwargs):
        return self.call('get_controller_state', kwargs=kwargs)

    def set_controller_state(self, **kwargs):
        return self.call('set_controller_state', kwargs=kwargs)

    def get_operation_mode(self, **kwargs):
        return self.call('get_operation_mode', kwargs=kwargs)

    def get_digital_io(self, **kwargs):
        return self.call('get_digital_io', kwargs=kwargs)

    def set_digital_io(self, **kwargs):
        return self.call('set_digital_io', kwargs=kwargs)

    def get_analog_io(self, **kwargs):
        return self.call('get_analog_io', kwargs=kwargs)

    def set_analog_io(self, **kwargs):
        return self.call('set_analog_io', kwargs=kwargs)

    def get_rapid_variables(self, **kwargs):
        return self.call('get_rapid_variables', kwargs=kwargs)

    def get_rapid_variable(self, **kwargs):
        return self.call('get_rapid_variable', kwargs=kwargs)

    def set_rapid_variable(self, **kwargs):
        return self.call('set_rapid_variable', kwargs=kwargs)

    def read_file(self, **kwargs):
        return self.call('read_file', kwargs=kwargs)

    def upload_file(self, **kwargs):
        return self.call('upload_file', kwargs=kwargs)

    def delete_file(self, **kwargs):
        return self.call('delete_file', kwargs=kwargs)

