from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHoribaEzspecSdk(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/HORIBAEzSpecSDK__python-sdk', 'source_file': 'horiba_sdk/devices/single_devices/ccd.py', 'class_name': 'ChargeCoupledDevice', 'import_roots': [], 'candidate_methods': ['open', 'close', 'is_open', 'restart', 'get_configuration', 'get_gain_token', 'set_gain', 'get_speed_token', 'set_speed', 'get_parallel_speed', 'set_parallel_speed', 'get_fit_parameters', 'set_fit_parameters', 'get_timer_resolution', 'set_timer_resolution', 'set_acquisition_format', 'set_region_of_interest', 'set_x_axis_conversion_type', 'get_x_axis_conversion_type', 'set_acquisition_count', 'get_acquisition_count', 'get_clean_count', 'set_clean_count', 'get_acquisition_data_size', 'get_chip_temperature', 'get_chip_size', 'get_exposure_time', 'set_exposure_time', 'get_trigger_input', 'set_trigger_input', 'get_signal_output', 'set_signal_output', 'get_acquisition_ready', 'acquisition_start', 'get_acquisition_busy', 'acquisition_abort', 'get_acquisition_data', 'set_center_wavelength', 'range_mode_center_wavelengths', 'raman_convert', 'set_em_gain', 'get_em_gain', 'pass_command'], 'action_targets': {}, 'metadata': {'repo': 'HORIBAEzSpecSDK/python-sdk', 'repo_url': 'https://github.com/HORIBAEzSpecSDK/python-sdk', 'brand': 'Horiba', 'model': 'EzSpec SDK', 'device_type_cn': '拉曼光谱仪', 'device_type_en': 'Raman Spectrometer', 'source_framework': 'horiba-sdk', 'tag_id': '4392', 'tag_name': '拉曼光谱仪', 'tag_name_en': 'Raman Spectrometer', 'candidate_score': 390, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

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

    def get_acquisition_count(self, **kwargs):
        return self.call('get_acquisition_count', kwargs=kwargs)

    def get_clean_count(self, **kwargs):
        return self.call('get_clean_count', kwargs=kwargs)

    def set_clean_count(self, **kwargs):
        return self.call('set_clean_count', kwargs=kwargs)

    def get_acquisition_data_size(self, **kwargs):
        return self.call('get_acquisition_data_size', kwargs=kwargs)

    def get_chip_temperature(self, **kwargs):
        return self.call('get_chip_temperature', kwargs=kwargs)

    def get_chip_size(self, **kwargs):
        return self.call('get_chip_size', kwargs=kwargs)

    def get_exposure_time(self, **kwargs):
        return self.call('get_exposure_time', kwargs=kwargs)

    def set_exposure_time(self, **kwargs):
        return self.call('set_exposure_time', kwargs=kwargs)

    def get_trigger_input(self, **kwargs):
        return self.call('get_trigger_input', kwargs=kwargs)

    def set_trigger_input(self, **kwargs):
        return self.call('set_trigger_input', kwargs=kwargs)

    def get_signal_output(self, **kwargs):
        return self.call('get_signal_output', kwargs=kwargs)

    def set_signal_output(self, **kwargs):
        return self.call('set_signal_output', kwargs=kwargs)

    def get_acquisition_ready(self, **kwargs):
        return self.call('get_acquisition_ready', kwargs=kwargs)

    def acquisition_start(self, **kwargs):
        return self.call('acquisition_start', kwargs=kwargs)

    def get_acquisition_busy(self, **kwargs):
        return self.call('get_acquisition_busy', kwargs=kwargs)

    def acquisition_abort(self, **kwargs):
        return self.call('acquisition_abort', kwargs=kwargs)

    def get_acquisition_data(self, **kwargs):
        return self.call('get_acquisition_data', kwargs=kwargs)

    def set_center_wavelength(self, **kwargs):
        return self.call('set_center_wavelength', kwargs=kwargs)

    def range_mode_center_wavelengths(self, **kwargs):
        return self.call('range_mode_center_wavelengths', kwargs=kwargs)

    def raman_convert(self, **kwargs):
        return self.call('raman_convert', kwargs=kwargs)

    def set_em_gain(self, **kwargs):
        return self.call('set_em_gain', kwargs=kwargs)

    def get_em_gain(self, **kwargs):
        return self.call('get_em_gain', kwargs=kwargs)

    def pass_command(self, **kwargs):
        return self.call('pass_command', kwargs=kwargs)

