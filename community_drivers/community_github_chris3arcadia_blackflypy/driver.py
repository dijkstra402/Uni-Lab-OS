from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubChris3arcadiaBlackflypy(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Chris3Arcadia_BlackFlyPy', 'source_file': 'BlackFlyPy.py', 'class_name': 'BlackFlyPy', 'import_roots': [], 'candidate_methods': ['load_options', 'load_constants', 'set_path', 'ensure_path', 'notify', 'initialize_system', 'get_system', 'get_library_version', 'get_interfaces', 'about_interfaces', 'clear_interfaces', 'get_nodemap_property', 'get_cameras', 'about_cameras', 'clear_cameras', 'get_system_info', 'load_system_info', 'release', 'initialize_camera', 'deinitialize_camera'], 'metadata': {'repo': 'chris3arcadia/blackflypy', 'repo_url': 'https://github.com/Chris3Arcadia/BlackFlyPy', 'unit_id': 'gh_flir_blackfly_s', 'source_file': 'BlackFlyPy.py', 'candidate_score': 28, 'manufacturer': 'FLIR', 'model_name': 'FLIR BlackFly S'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def load_options(self, **kwargs):
        return self.call('load_options', kwargs=kwargs)

    def load_constants(self, **kwargs):
        return self.call('load_constants', kwargs=kwargs)

    def set_path(self, **kwargs):
        return self.call('set_path', kwargs=kwargs)

    def ensure_path(self, **kwargs):
        return self.call('ensure_path', kwargs=kwargs)

    def notify(self, **kwargs):
        return self.call('notify', kwargs=kwargs)

    def initialize_system(self, **kwargs):
        return self.call('initialize_system', kwargs=kwargs)

    def get_system(self, **kwargs):
        return self.call('get_system', kwargs=kwargs)

    def get_library_version(self, **kwargs):
        return self.call('get_library_version', kwargs=kwargs)

    def get_interfaces(self, **kwargs):
        return self.call('get_interfaces', kwargs=kwargs)

    def about_interfaces(self, **kwargs):
        return self.call('about_interfaces', kwargs=kwargs)

    def clear_interfaces(self, **kwargs):
        return self.call('clear_interfaces', kwargs=kwargs)

    def get_nodemap_property(self, **kwargs):
        return self.call('get_nodemap_property', kwargs=kwargs)

    def get_cameras(self, **kwargs):
        return self.call('get_cameras', kwargs=kwargs)

    def about_cameras(self, **kwargs):
        return self.call('about_cameras', kwargs=kwargs)

    def clear_cameras(self, **kwargs):
        return self.call('clear_cameras', kwargs=kwargs)

    def get_system_info(self, **kwargs):
        return self.call('get_system_info', kwargs=kwargs)

    def load_system_info(self, **kwargs):
        return self.call('load_system_info', kwargs=kwargs)

    def release(self, **kwargs):
        return self.call('release', kwargs=kwargs)

    def initialize_camera(self, **kwargs):
        return self.call('initialize_camera', kwargs=kwargs)

    def deinitialize_camera(self, **kwargs):
        return self.call('deinitialize_camera', kwargs=kwargs)

