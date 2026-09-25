from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentRaspberryPiPicamera(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/python-microscope__microscope', 'source_file': 'microscope/cameras/picamera.py', 'class_name': 'PiCamera', 'import_roots': [], 'candidate_methods': ['get_awb_mode', 'set_awb_mode', 'set_iso_mode', 'HW_trigger', 'initialize', 'make_safe', 'abort', 'set_trigger', 'trigger_mode', 'trigger_type', 'setLED', 'set_exposure_time', 'get_exposure_time', 'get_cycle_time', 'get_framerate', 'set_framerate', 'zoom', 'soft_trigger', 'shuttering_mode', 'get_transform', 'set_transform', 'get_sensor_shape', 'get_binning', 'set_binning', 'get_roi', 'set_roi', 'trigger', 'enable', 'disable', 'set_client', 'update_settings', 'receiveClient', 'grab_next_data', 'receiveData', 'get_is_enabled', 'shutdown', 'add_setting', 'get_setting', 'get_all_settings', 'set_setting', 'describe_setting', 'describe_settings'], 'action_targets': {}, 'metadata': {'repo': 'python-microscope/microscope', 'repo_url': 'https://github.com/python-microscope/microscope', 'brand': 'Raspberry Pi', 'model': 'PiCamera', 'device_type_cn': '单板机相机', 'device_type_en': 'SBC Camera', 'source_framework': 'python-microscope', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 252, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_awb_mode(self, **kwargs):
        return self.call('get_awb_mode', kwargs=kwargs)

    def set_awb_mode(self, **kwargs):
        return self.call('set_awb_mode', kwargs=kwargs)

    def set_iso_mode(self, **kwargs):
        return self.call('set_iso_mode', kwargs=kwargs)

    def HW_trigger(self, **kwargs):
        return self.call('HW_trigger', kwargs=kwargs)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def make_safe(self, **kwargs):
        return self.call('make_safe', kwargs=kwargs)

    def abort(self, **kwargs):
        return self.call('abort', kwargs=kwargs)

    def set_trigger(self, **kwargs):
        return self.call('set_trigger', kwargs=kwargs)

    def trigger_mode(self, **kwargs):
        return self.call('trigger_mode', kwargs=kwargs)

    def trigger_type(self, **kwargs):
        return self.call('trigger_type', kwargs=kwargs)

    def setLED(self, **kwargs):
        return self.call('setLED', kwargs=kwargs)

    def set_exposure_time(self, **kwargs):
        return self.call('set_exposure_time', kwargs=kwargs)

    def get_exposure_time(self, **kwargs):
        return self.call('get_exposure_time', kwargs=kwargs)

    def get_cycle_time(self, **kwargs):
        return self.call('get_cycle_time', kwargs=kwargs)

    def get_framerate(self, **kwargs):
        return self.call('get_framerate', kwargs=kwargs)

    def set_framerate(self, **kwargs):
        return self.call('set_framerate', kwargs=kwargs)

    def zoom(self, **kwargs):
        return self.call('zoom', kwargs=kwargs)

    def soft_trigger(self, **kwargs):
        return self.call('soft_trigger', kwargs=kwargs)

    def shuttering_mode(self, **kwargs):
        return self.call('shuttering_mode', kwargs=kwargs)

    def get_transform(self, **kwargs):
        return self.call('get_transform', kwargs=kwargs)

    def set_transform(self, **kwargs):
        return self.call('set_transform', kwargs=kwargs)

    def get_sensor_shape(self, **kwargs):
        return self.call('get_sensor_shape', kwargs=kwargs)

    def get_binning(self, **kwargs):
        return self.call('get_binning', kwargs=kwargs)

    def set_binning(self, **kwargs):
        return self.call('set_binning', kwargs=kwargs)

    def get_roi(self, **kwargs):
        return self.call('get_roi', kwargs=kwargs)

    def set_roi(self, **kwargs):
        return self.call('set_roi', kwargs=kwargs)

    def trigger(self, **kwargs):
        return self.call('trigger', kwargs=kwargs)

    def enable(self, **kwargs):
        return self.call('enable', kwargs=kwargs)

    def disable(self, **kwargs):
        return self.call('disable', kwargs=kwargs)

    def set_client(self, **kwargs):
        return self.call('set_client', kwargs=kwargs)

    def update_settings(self, **kwargs):
        return self.call('update_settings', kwargs=kwargs)

    def receiveClient(self, **kwargs):
        return self.call('receiveClient', kwargs=kwargs)

    def grab_next_data(self, **kwargs):
        return self.call('grab_next_data', kwargs=kwargs)

    def receiveData(self, **kwargs):
        return self.call('receiveData', kwargs=kwargs)

    def get_is_enabled(self, **kwargs):
        return self.call('get_is_enabled', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

    def add_setting(self, **kwargs):
        return self.call('add_setting', kwargs=kwargs)

    def get_setting(self, **kwargs):
        return self.call('get_setting', kwargs=kwargs)

    def get_all_settings(self, **kwargs):
        return self.call('get_all_settings', kwargs=kwargs)

    def set_setting(self, **kwargs):
        return self.call('set_setting', kwargs=kwargs)

    def describe_setting(self, **kwargs):
        return self.call('describe_setting', kwargs=kwargs)

    def describe_settings(self, **kwargs):
        return self.call('describe_settings', kwargs=kwargs)

