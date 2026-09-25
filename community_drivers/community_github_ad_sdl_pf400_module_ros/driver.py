from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAdSdlPf400ModuleRos(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/AD-SDL_pf400_module_ros', 'source_file': 'pf400_driver/pf400_driver/tcp_driver.py', 'class_name': 'PF400', 'import_roots': [], 'candidate_methods': ['load_robot_data', 'load_robot_commands', 'load_error_codes', 'connect_robot', 'disconnect_robot', 'send_command', 'check_robot_state', 'enable_power', 'disable_power', 'attach_robot', 'home_robot', 'set_profile', 'initialize_robot', 'force_initialize_robot', 'set_motion_blend_tolerance', 'set_robot_mode', 'check_robot_heartbeat', 'check_general_state', 'stop_robot', 'wait_before_next_move'], 'metadata': {'repo': 'ad-sdl/pf400_module_ros', 'repo_url': 'https://github.com/AD-SDL/pf400_module_ros', 'unit_id': 'gh_precise_automation_pf400', 'source_file': 'pf400_driver/pf400_driver/tcp_driver.py', 'candidate_score': 120, 'manufacturer': 'Precise Automation', 'model_name': 'Precise Automation PF400'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def load_robot_data(self, **kwargs):
        return self.call('load_robot_data', kwargs=kwargs)

    def load_robot_commands(self, **kwargs):
        return self.call('load_robot_commands', kwargs=kwargs)

    def load_error_codes(self, **kwargs):
        return self.call('load_error_codes', kwargs=kwargs)

    def connect_robot(self, **kwargs):
        return self.call('connect_robot', kwargs=kwargs)

    def disconnect_robot(self, **kwargs):
        return self.call('disconnect_robot', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

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

    def set_profile(self, **kwargs):
        return self.call('set_profile', kwargs=kwargs)

    def initialize_robot(self, **kwargs):
        return self.call('initialize_robot', kwargs=kwargs)

    def force_initialize_robot(self, **kwargs):
        return self.call('force_initialize_robot', kwargs=kwargs)

    def set_motion_blend_tolerance(self, **kwargs):
        return self.call('set_motion_blend_tolerance', kwargs=kwargs)

    def set_robot_mode(self, **kwargs):
        return self.call('set_robot_mode', kwargs=kwargs)

    def check_robot_heartbeat(self, **kwargs):
        return self.call('check_robot_heartbeat', kwargs=kwargs)

    def check_general_state(self, **kwargs):
        return self.call('check_general_state', kwargs=kwargs)

    def stop_robot(self, **kwargs):
        return self.call('stop_robot', kwargs=kwargs)

    def wait_before_next_move(self, **kwargs):
        return self.call('wait_before_next_move', kwargs=kwargs)

