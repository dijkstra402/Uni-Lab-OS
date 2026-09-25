from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubHoribaezspecsdkPythonSdk(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/HORIBAEzSpecSDK_python-sdk', 'source_file': 'horiba_sdk/devices/single_devices/ccd.py', 'class_name': 'ChargeCoupledDevice', 'import_roots': [], 'candidate_methods': ['open', 'close', 'is_open', 'restart', 'get_configuration', 'get_gain_token', 'set_gain', 'get_speed_token', 'set_speed', 'get_parallel_speed', 'set_parallel_speed', 'get_fit_parameters', 'set_fit_parameters', 'get_timer_resolution', 'set_timer_resolution', 'set_acquisition_format', 'set_region_of_interest', 'set_x_axis_conversion_type', 'get_x_axis_conversion_type', 'set_acquisition_count'], 'metadata': {'repo': 'horibaezspecsdk/python-sdk', 'repo_url': 'https://github.com/HORIBAEzSpecSDK/python-sdk', 'unit_id': 'gh_horiba_ihr', 'source_file': 'horiba_sdk/devices/single_devices/ccd.py', 'candidate_score': 92, 'manufacturer': 'Horiba', 'model_name': 'Horiba iHR系列单色仪'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def is_open(self, **kwargs):
        return self.call('is_open', kwargs=kwargs)

    def restart(self, **kwargs):
        return self.call('restart', kwargs=kwargs)

    def get_configuration(self, **kwargs):
        return self.call('get_configuration', kwargs=kwargs)

    def get_gain_token(self, **kwargs):
        return self.call('get_gain_token', kwargs=kwargs)

    def set_gain(self, **kwargs):
        return self.call('set_gain', kwargs=kwargs)

    def get_speed_token(self, **kwargs):
        return self.call('get_speed_token', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

    def get_parallel_speed(self, **kwargs):
        return self.call('get_parallel_speed', kwargs=kwargs)

    def set_parallel_speed(self, **kwargs):
        return self.call('set_parallel_speed', kwargs=kwargs)

    def get_fit_parameters(self, **kwargs):
        return self.call('get_fit_parameters', kwargs=kwargs)

    def set_fit_parameters(self, **kwargs):
        return self.call('set_fit_parameters', kwargs=kwargs)

    def get_timer_resolution(self, **kwargs):
        return self.call('get_timer_resolution', kwargs=kwargs)

    def set_timer_resolution(self, **kwargs):
        return self.call('set_timer_resolution', kwargs=kwargs)

    def set_acquisition_format(self, **kwargs):
        return self.call('set_acquisition_format', kwargs=kwargs)

    def set_region_of_interest(self, **kwargs):
        return self.call('set_region_of_interest', kwargs=kwargs)

    def set_x_axis_conversion_type(self, **kwargs):
        return self.call('set_x_axis_conversion_type', kwargs=kwargs)

    def get_x_axis_conversion_type(self, **kwargs):
        return self.call('get_x_axis_conversion_type', kwargs=kwargs)

    def set_acquisition_count(self, **kwargs):
        return self.call('set_acquisition_count', kwargs=kwargs)

