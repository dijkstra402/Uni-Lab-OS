from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAdSdlA4sSealerModule(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/AD-SDL_a4s_sealer_module', 'source_file': 'src/a4s_sealer_driver.py', 'class_name': 'A4S_SEALER_DRIVER', 'import_roots': [], 'candidate_methods': ['connect_sealer', 'get_status', 'send_command', 'reset', 'open_gate', 'close_gate', 'set_temp', 'set_time', 'seal', 'config_robot'], 'metadata': {'repo': 'ad-sdl/a4s_sealer_module', 'repo_url': 'https://github.com/AD-SDL/a4s_sealer_module', 'unit_id': 'gh_azenta_a4s', 'source_file': 'src/a4s_sealer_driver.py', 'candidate_score': 114, 'manufacturer': 'Azenta', 'model_name': 'Azenta a4S'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def connect_sealer(self, **kwargs):
        return self.call('connect_sealer', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def open_gate(self, **kwargs):
        return self.call('open_gate', kwargs=kwargs)

    def close_gate(self, **kwargs):
        return self.call('close_gate', kwargs=kwargs)

    def set_temp(self, **kwargs):
        return self.call('set_temp', kwargs=kwargs)

    def set_time(self, **kwargs):
        return self.call('set_time', kwargs=kwargs)

    def seal(self, **kwargs):
        return self.call('seal', kwargs=kwargs)

    def config_robot(self, **kwargs):
        return self.call('config_robot', kwargs=kwargs)

