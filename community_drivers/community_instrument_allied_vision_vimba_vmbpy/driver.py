from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAlliedVisionVimbaVmbpy(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/alliedvision__VimbaPython', 'source_file': 'vimba/camera.py', 'class_name': 'Camera', 'import_roots': [], 'candidate_methods': ['set_access_mode', 'get_access_mode', 'get_id', 'get_name', 'get_model', 'get_serial', 'get_permitted_access_modes', 'get_interface_id', 'read_memory', 'write_memory', 'read_registers', 'write_registers', 'get_all_features', 'get_features_affected_by', 'get_features_selected_by', 'get_features_by_type', 'get_features_by_category', 'get_feature_by_name', 'get_frame_generator', 'get_frame', 'start_streaming', 'stop_streaming', 'is_streaming', 'queue_frame', 'get_pixel_formats', 'get_pixel_format', 'set_pixel_format', 'save_settings', 'load_settings'], 'action_targets': {}, 'metadata': {'repo': 'alliedvision/VimbaPython', 'repo_url': 'https://github.com/alliedvision/VimbaPython', 'brand': 'Allied Vision', 'model': 'Vimba/VmbPy', 'device_type_cn': '工业相机', 'device_type_en': 'Industrial Camera', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 290, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def set_access_mode(self, **kwargs):
        return self.call('set_access_mode', kwargs=kwargs)

    def get_access_mode(self, **kwargs):
        return self.call('get_access_mode', kwargs=kwargs)

    def get_id(self, **kwargs):
        return self.call('get_id', kwargs=kwargs)

    def get_name(self, **kwargs):
        return self.call('get_name', kwargs=kwargs)

    def get_model(self, **kwargs):
        return self.call('get_model', kwargs=kwargs)

    def get_serial(self, **kwargs):
        return self.call('get_serial', kwargs=kwargs)

    def get_permitted_access_modes(self, **kwargs):
        return self.call('get_permitted_access_modes', kwargs=kwargs)

    def get_interface_id(self, **kwargs):
        return self.call('get_interface_id', kwargs=kwargs)

    def read_memory(self, **kwargs):
        return self.call('read_memory', kwargs=kwargs)

    def write_memory(self, **kwargs):
        return self.call('write_memory', kwargs=kwargs)

    def read_registers(self, **kwargs):
        return self.call('read_registers', kwargs=kwargs)

    def write_registers(self, **kwargs):
        return self.call('write_registers', kwargs=kwargs)

    def get_all_features(self, **kwargs):
        return self.call('get_all_features', kwargs=kwargs)

    def get_features_affected_by(self, **kwargs):
        return self.call('get_features_affected_by', kwargs=kwargs)

    def get_features_selected_by(self, **kwargs):
        return self.call('get_features_selected_by', kwargs=kwargs)

    def get_features_by_type(self, **kwargs):
        return self.call('get_features_by_type', kwargs=kwargs)

    def get_features_by_category(self, **kwargs):
        return self.call('get_features_by_category', kwargs=kwargs)

    def get_feature_by_name(self, **kwargs):
        return self.call('get_feature_by_name', kwargs=kwargs)

    def get_frame_generator(self, **kwargs):
        return self.call('get_frame_generator', kwargs=kwargs)

    def get_frame(self, **kwargs):
        return self.call('get_frame', kwargs=kwargs)

    def start_streaming(self, **kwargs):
        return self.call('start_streaming', kwargs=kwargs)

    def stop_streaming(self, **kwargs):
        return self.call('stop_streaming', kwargs=kwargs)

    def is_streaming(self, **kwargs):
        return self.call('is_streaming', kwargs=kwargs)

    def queue_frame(self, **kwargs):
        return self.call('queue_frame', kwargs=kwargs)

    def get_pixel_formats(self, **kwargs):
        return self.call('get_pixel_formats', kwargs=kwargs)

    def get_pixel_format(self, **kwargs):
        return self.call('get_pixel_format', kwargs=kwargs)

    def set_pixel_format(self, **kwargs):
        return self.call('set_pixel_format', kwargs=kwargs)

    def save_settings(self, **kwargs):
        return self.call('save_settings', kwargs=kwargs)

    def load_settings(self, **kwargs):
        return self.call('load_settings', kwargs=kwargs)

