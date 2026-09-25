from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAdSdlHudsonPlatecraneModule(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/AD-SDL_hudson_platecrane_module', 'source_file': 'src/platecrane_driver/serial_port.py', 'class_name': 'SerialPort', 'import_roots': [], 'candidate_methods': ['send_command', 'receive_command'], 'metadata': {'repo': 'ad-sdl/hudson_platecrane_module', 'repo_url': 'https://github.com/AD-SDL/hudson_platecrane_module', 'unit_id': 'gh_hudson_robotics_platecrane_ex', 'source_file': 'src/platecrane_driver/serial_port.py', 'candidate_score': 137, 'manufacturer': 'Hudson Robotics', 'model_name': 'Hudson Robotics PlateCrane EX'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def receive_command(self, **kwargs):
        return self.call('receive_command', kwargs=kwargs)

