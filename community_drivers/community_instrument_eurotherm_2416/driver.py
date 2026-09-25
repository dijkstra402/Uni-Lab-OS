from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentEurotherm2416(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/CederGroupHub__alab_control', 'source_file': 'alab_control/phenom/phenom.py', 'class_name': 'PhenomDriver', 'import_roots': [], 'candidate_methods': ['install_license', 'connect', 'disconnect', 'reset_have_just_move_to_SEM', 'get_instrument_mode', 'get_operational_mode', 'activate', 'load', 'unload', 'standby', 'to_nav', 'to_SEM', 'auto_focus', 'auto_contrast_brightness', 'adjust_focus', 'move_to', 'move_by', 'position', 'get_sem_high_tension', 'set_sem_high_tension', 'get_sem_spot_size', 'set_sem_spot_size', 'get_frame_width', 'zoom', 'get_magnification', 'framewidth', 'save_image', 'get_image_metadata', 'get_pressure', 'set_detector', 'launch_SEMEDX_collection'], 'action_targets': {}, 'metadata': {'repo': 'CederGroupHub/alab_control', 'repo_url': 'https://github.com/CederGroupHub/alab_control', 'brand': 'Eurotherm', 'model': '2416', 'device_type_cn': '箱式电阻炉', 'device_type_en': 'Box Resistance Furnace', 'source_framework': 'alab_control', 'tag_id': '4438', 'tag_name': '箱式电阻炉', 'tag_name_en': 'Box Resistance Furnace', 'candidate_score': 302, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def install_license(self, **kwargs):
        return self.call('install_license', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def reset_have_just_move_to_SEM(self, **kwargs):
        return self.call('reset_have_just_move_to_SEM', kwargs=kwargs)

    def get_instrument_mode(self, **kwargs):
        return self.call('get_instrument_mode', kwargs=kwargs)

    def get_operational_mode(self, **kwargs):
        return self.call('get_operational_mode', kwargs=kwargs)

    def activate(self, **kwargs):
        return self.call('activate', kwargs=kwargs)

    def load(self, **kwargs):
        return self.call('load', kwargs=kwargs)

    def unload(self, **kwargs):
        return self.call('unload', kwargs=kwargs)

    def standby(self, **kwargs):
        return self.call('standby', kwargs=kwargs)

    def to_nav(self, **kwargs):
        return self.call('to_nav', kwargs=kwargs)

    def to_SEM(self, **kwargs):
        return self.call('to_SEM', kwargs=kwargs)

    def auto_focus(self, **kwargs):
        return self.call('auto_focus', kwargs=kwargs)

    def auto_contrast_brightness(self, **kwargs):
        return self.call('auto_contrast_brightness', kwargs=kwargs)

    def adjust_focus(self, **kwargs):
        return self.call('adjust_focus', kwargs=kwargs)

    def move_to(self, **kwargs):
        return self.call('move_to', kwargs=kwargs)

    def move_by(self, **kwargs):
        return self.call('move_by', kwargs=kwargs)

    def position(self, **kwargs):
        return self.call('position', kwargs=kwargs)

    def get_sem_high_tension(self, **kwargs):
        return self.call('get_sem_high_tension', kwargs=kwargs)

    def set_sem_high_tension(self, **kwargs):
        return self.call('set_sem_high_tension', kwargs=kwargs)

    def get_sem_spot_size(self, **kwargs):
        return self.call('get_sem_spot_size', kwargs=kwargs)

    def set_sem_spot_size(self, **kwargs):
        return self.call('set_sem_spot_size', kwargs=kwargs)

    def get_frame_width(self, **kwargs):
        return self.call('get_frame_width', kwargs=kwargs)

    def zoom(self, **kwargs):
        return self.call('zoom', kwargs=kwargs)

    def get_magnification(self, **kwargs):
        return self.call('get_magnification', kwargs=kwargs)

    def framewidth(self, **kwargs):
        return self.call('framewidth', kwargs=kwargs)

    def save_image(self, **kwargs):
        return self.call('save_image', kwargs=kwargs)

    def get_image_metadata(self, **kwargs):
        return self.call('get_image_metadata', kwargs=kwargs)

    def get_pressure(self, **kwargs):
        return self.call('get_pressure', kwargs=kwargs)

    def set_detector(self, **kwargs):
        return self.call('set_detector', kwargs=kwargs)

    def launch_SEMEDX_collection(self, **kwargs):
        return self.call('launch_SEMEDX_collection', kwargs=kwargs)

