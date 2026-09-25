from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLaurellWs650(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/fenning-research-group__PASCAL', 'source_file': 'hardware/thorlabs cameras/source/tl_camera.py', 'class_name': 'TLCamera', 'import_roots': [], 'candidate_methods': ['dispose', 'get_pending_frame_or_null', 'get_measured_frame_rate_fps', 'get_is_data_rate_supported', 'get_is_taps_supported', 'get_is_operation_mode_supported', 'get_color_correction_matrix', 'get_default_white_balance_matrix', 'arm', 'issue_software_trigger', 'disarm', 'convert_gain_to_decibels', 'convert_decibels_to_gain', 'exposure_time_us', 'image_poll_timeout_ms', 'exposure_time_range_us', 'firmware_version', 'frame_time_us', 'trigger_polarity', 'binx', 'sensor_readout_time_ns', 'binx_range', 'is_hot_pixel_correction_enabled', 'hot_pixel_correction_threshold', 'hot_pixel_correction_threshold_range', 'sensor_width_pixels', 'gain_range', 'image_width_range_pixels', 'sensor_height_pixels', 'image_height_range_pixels', 'model', 'name', 'name_string_length_range', 'frames_per_trigger_zero_for_unlimited', 'frames_per_trigger_range', 'usb_port_type', 'communication_interface', 'operation_mode', 'is_armed', 'is_eep_supported', 'is_led_supported', 'is_cooling_supported', 'is_cooling_enabled', 'is_nir_boost_supported', 'camera_sensor_type', 'color_filter_array_phase', 'camera_color_correction_matrix_output_color_space', 'data_rate', 'sensor_pixel_size_bytes', 'sensor_pixel_width_um', 'sensor_pixel_height_um', 'bit_depth', 'roi', 'roi_range', 'serial_number', 'serial_number_string_length_range', 'is_led_on', 'eep_status', 'is_eep_enabled', 'biny', 'biny_range', 'gain', 'black_level', 'black_level_range', 'image_width_pixels', 'image_height_pixels', 'polar_phase', 'frame_rate_control_value_range', 'is_frame_rate_control_enabled', 'frame_rate_control_value'], 'action_targets': {}, 'metadata': {'repo': 'fenning-research-group/PASCAL', 'repo_url': 'https://github.com/fenning-research-group/PASCAL', 'brand': 'Laurell', 'model': 'WS-650', 'device_type_cn': '匀胶机', 'device_type_en': 'Spin Coater', 'source_framework': '专用驱动', 'tag_id': '4372', 'tag_name': '匀胶机', 'tag_name_en': 'Spin Coater', 'candidate_score': 590, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def dispose(self, **kwargs):
        return self.call('dispose', kwargs=kwargs)

    def get_pending_frame_or_null(self, **kwargs):
        return self.call('get_pending_frame_or_null', kwargs=kwargs)

    def get_measured_frame_rate_fps(self, **kwargs):
        return self.call('get_measured_frame_rate_fps', kwargs=kwargs)

    def get_is_data_rate_supported(self, **kwargs):
        return self.call('get_is_data_rate_supported', kwargs=kwargs)

    def get_is_taps_supported(self, **kwargs):
        return self.call('get_is_taps_supported', kwargs=kwargs)

    def get_is_operation_mode_supported(self, **kwargs):
        return self.call('get_is_operation_mode_supported', kwargs=kwargs)

    def get_color_correction_matrix(self, **kwargs):
        return self.call('get_color_correction_matrix', kwargs=kwargs)

    def get_default_white_balance_matrix(self, **kwargs):
        return self.call('get_default_white_balance_matrix', kwargs=kwargs)

    def arm(self, **kwargs):
        return self.call('arm', kwargs=kwargs)

    def issue_software_trigger(self, **kwargs):
        return self.call('issue_software_trigger', kwargs=kwargs)

    def disarm(self, **kwargs):
        return self.call('disarm', kwargs=kwargs)

    def convert_gain_to_decibels(self, **kwargs):
        return self.call('convert_gain_to_decibels', kwargs=kwargs)

    def convert_decibels_to_gain(self, **kwargs):
        return self.call('convert_decibels_to_gain', kwargs=kwargs)

    def exposure_time_us(self, **kwargs):
        return self.call('exposure_time_us', kwargs=kwargs)

    def image_poll_timeout_ms(self, **kwargs):
        return self.call('image_poll_timeout_ms', kwargs=kwargs)

    def exposure_time_range_us(self, **kwargs):
        return self.call('exposure_time_range_us', kwargs=kwargs)

    def firmware_version(self, **kwargs):
        return self.call('firmware_version', kwargs=kwargs)

    def frame_time_us(self, **kwargs):
        return self.call('frame_time_us', kwargs=kwargs)

    def trigger_polarity(self, **kwargs):
        return self.call('trigger_polarity', kwargs=kwargs)

    def binx(self, **kwargs):
        return self.call('binx', kwargs=kwargs)

    def sensor_readout_time_ns(self, **kwargs):
        return self.call('sensor_readout_time_ns', kwargs=kwargs)

    def binx_range(self, **kwargs):
        return self.call('binx_range', kwargs=kwargs)

    def is_hot_pixel_correction_enabled(self, **kwargs):
        return self.call('is_hot_pixel_correction_enabled', kwargs=kwargs)

    def hot_pixel_correction_threshold(self, **kwargs):
        return self.call('hot_pixel_correction_threshold', kwargs=kwargs)

    def hot_pixel_correction_threshold_range(self, **kwargs):
        return self.call('hot_pixel_correction_threshold_range', kwargs=kwargs)

    def sensor_width_pixels(self, **kwargs):
        return self.call('sensor_width_pixels', kwargs=kwargs)

    def gain_range(self, **kwargs):
        return self.call('gain_range', kwargs=kwargs)

    def image_width_range_pixels(self, **kwargs):
        return self.call('image_width_range_pixels', kwargs=kwargs)

    def sensor_height_pixels(self, **kwargs):
        return self.call('sensor_height_pixels', kwargs=kwargs)

    def image_height_range_pixels(self, **kwargs):
        return self.call('image_height_range_pixels', kwargs=kwargs)

    def model(self, **kwargs):
        return self.call('model', kwargs=kwargs)

    def name(self, **kwargs):
        return self.call('name', kwargs=kwargs)

    def name_string_length_range(self, **kwargs):
        return self.call('name_string_length_range', kwargs=kwargs)

    def frames_per_trigger_zero_for_unlimited(self, **kwargs):
        return self.call('frames_per_trigger_zero_for_unlimited', kwargs=kwargs)

    def frames_per_trigger_range(self, **kwargs):
        return self.call('frames_per_trigger_range', kwargs=kwargs)

    def usb_port_type(self, **kwargs):
        return self.call('usb_port_type', kwargs=kwargs)

    def communication_interface(self, **kwargs):
        return self.call('communication_interface', kwargs=kwargs)

    def operation_mode(self, **kwargs):
        return self.call('operation_mode', kwargs=kwargs)

    def is_armed(self, **kwargs):
        return self.call('is_armed', kwargs=kwargs)

    def is_eep_supported(self, **kwargs):
        return self.call('is_eep_supported', kwargs=kwargs)

    def is_led_supported(self, **kwargs):
        return self.call('is_led_supported', kwargs=kwargs)

    def is_cooling_supported(self, **kwargs):
        return self.call('is_cooling_supported', kwargs=kwargs)

    def is_cooling_enabled(self, **kwargs):
        return self.call('is_cooling_enabled', kwargs=kwargs)

    def is_nir_boost_supported(self, **kwargs):
        return self.call('is_nir_boost_supported', kwargs=kwargs)

    def camera_sensor_type(self, **kwargs):
        return self.call('camera_sensor_type', kwargs=kwargs)

    def color_filter_array_phase(self, **kwargs):
        return self.call('color_filter_array_phase', kwargs=kwargs)

    def camera_color_correction_matrix_output_color_space(self, **kwargs):
        return self.call('camera_color_correction_matrix_output_color_space', kwargs=kwargs)

    def data_rate(self, **kwargs):
        return self.call('data_rate', kwargs=kwargs)

    def sensor_pixel_size_bytes(self, **kwargs):
        return self.call('sensor_pixel_size_bytes', kwargs=kwargs)

    def sensor_pixel_width_um(self, **kwargs):
        return self.call('sensor_pixel_width_um', kwargs=kwargs)

    def sensor_pixel_height_um(self, **kwargs):
        return self.call('sensor_pixel_height_um', kwargs=kwargs)

    def bit_depth(self, **kwargs):
        return self.call('bit_depth', kwargs=kwargs)

    def roi(self, **kwargs):
        return self.call('roi', kwargs=kwargs)

    def roi_range(self, **kwargs):
        return self.call('roi_range', kwargs=kwargs)

    def serial_number(self, **kwargs):
        return self.call('serial_number', kwargs=kwargs)

    def serial_number_string_length_range(self, **kwargs):
        return self.call('serial_number_string_length_range', kwargs=kwargs)

    def is_led_on(self, **kwargs):
        return self.call('is_led_on', kwargs=kwargs)

    def eep_status(self, **kwargs):
        return self.call('eep_status', kwargs=kwargs)

    def is_eep_enabled(self, **kwargs):
        return self.call('is_eep_enabled', kwargs=kwargs)

    def biny(self, **kwargs):
        return self.call('biny', kwargs=kwargs)

    def biny_range(self, **kwargs):
        return self.call('biny_range', kwargs=kwargs)

    def gain(self, **kwargs):
        return self.call('gain', kwargs=kwargs)

    def black_level(self, **kwargs):
        return self.call('black_level', kwargs=kwargs)

    def black_level_range(self, **kwargs):
        return self.call('black_level_range', kwargs=kwargs)

    def image_width_pixels(self, **kwargs):
        return self.call('image_width_pixels', kwargs=kwargs)

    def image_height_pixels(self, **kwargs):
        return self.call('image_height_pixels', kwargs=kwargs)

    def polar_phase(self, **kwargs):
        return self.call('polar_phase', kwargs=kwargs)

    def frame_rate_control_value_range(self, **kwargs):
        return self.call('frame_rate_control_value_range', kwargs=kwargs)

    def is_frame_rate_control_enabled(self, **kwargs):
        return self.call('is_frame_rate_control_enabled', kwargs=kwargs)

    def frame_rate_control_value(self, **kwargs):
        return self.call('frame_rate_control_value', kwargs=kwargs)

