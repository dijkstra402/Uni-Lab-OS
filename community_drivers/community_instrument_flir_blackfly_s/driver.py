from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentFlirBlackflyS(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Chris3Arcadia__BlackFlyPy', 'source_file': 'BlackFlyPy.py', 'class_name': 'BlackFlyPy', 'import_roots': [], 'candidate_methods': ['load_options', 'load_constants', 'set_path', 'ensure_path', 'notify', 'initialize_system', 'get_system', 'get_library_version', 'get_interfaces', 'about_interfaces', 'clear_interfaces', 'get_nodemap_property', 'get_cameras', 'about_cameras', 'clear_cameras', 'get_system_info', 'load_system_info', 'release', 'initialize_camera', 'deinitialize_camera', 'get_camera_information', 'get_camera_image'], 'action_targets': {}, 'metadata': {'repo': 'Chris3Arcadia/BlackFlyPy', 'repo_url': 'https://github.com/Chris3Arcadia/BlackFlyPy', 'brand': 'FLIR', 'model': 'BlackFly S', 'device_type_cn': '工业相机', 'device_type_en': 'Industrial Camera', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 246, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

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

    def get_camera_information(self, **kwargs):
        return self.call('get_camera_information', kwargs=kwargs)

    def get_camera_image(self, **kwargs):
        return self.call('get_camera_image', kwargs=kwargs)

