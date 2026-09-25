from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAndorIxon(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AlexShkarin__pyLabLib', 'source_file': 'pylablib/devices/Andor/AndorSDK2.py', 'class_name': 'AndorSDK2Camera', 'import_roots': [], 'candidate_methods': ['open', 'close', 'is_opened', 'get_device_info', 'get_status', 'acquisition_in_progress', 'get_capabilities', 'get_pixel_size', 'is_cooler_on', 'set_cooler', 'get_temperature_status', 'get_temperature', 'set_temperature', 'get_temperature_setpoint', 'get_temperature_range', 'get_all_amp_modes', 'get_max_vsspeed', 'get_all_vsspeeds', 'set_amp_mode', 'get_amp_mode', 'set_vsspeed', 'get_channel', 'get_channel_bitdepth', 'get_oamp', 'get_oamp_desc', 'get_hsspeed', 'get_hsspeed_frequency', 'get_preamp', 'get_preamp_gain', 'get_vsspeed', 'get_vsspeed_period', 'get_EMCCD_gain', 'set_EMCCD_gain', 'init_amp_mode', 'get_min_shutter_times', 'setup_shutter', 'get_shutter_parameters', 'get_shutter', 'set_fan_mode', 'get_fan_mode', 'read_in_aux_port', 'set_out_aux_port', 'set_trigger_mode', 'get_trigger_mode', 'get_trigger_level_limits', 'setup_ext_trigger', 'get_ext_trigger_parameters', 'send_software_trigger', 'set_acquisition_mode', 'get_acquisition_mode', 'setup_accum_mode', 'get_accum_mode_parameters', 'setup_kinetic_mode', 'get_kinetic_mode_parameters', 'setup_fast_kinetic_mode', 'get_fast_kinetic_mode_parameters', 'setup_cont_mode', 'get_cont_mode_parameters', 'set_exposure', 'get_exposure', 'set_frame_period', 'enable_frame_transfer_mode', 'is_frame_transfer_enabled', 'get_cycle_timings', 'get_frame_timings', 'get_readout_time', 'get_keepclean_time', 'set_read_mode', 'get_read_mode', 'setup_single_track_mode', 'get_single_track_mode_parameters', 'setup_multi_track_mode', 'get_multi_track_mode_parameters', 'setup_random_track_mode', 'get_random_track_mode_parameters', 'setup_image_mode', 'get_image_mode_parameters', 'get_detector_size', 'get_roi', 'set_roi', 'get_roi_limits', 'setup_acquisition', 'clear_acquisition', 'start_acquisition', 'stop_acquisition', 'get_acquisition_progress', 'get_buffer_size', 'is_acquisition_setup', 'get_acquisition_parameters', 'pausing_acquisition', 'get_frames_status', 'wait_for_frame', 'get_image_indexing', 'set_image_indexing', 'get_data_dimensions', 'get_frame_format', 'set_frame_format', 'get_frame_info_format', 'set_frame_info_format', 'get_frame_info_period', 'set_frame_info_period', 'get_frame_info_fields', 'get_new_images_range', 'read_multiple_images', 'read_oldest_image', 'read_newest_image', 'grab', 'snap', 'get_settings', 'get_full_status', 'get_full_info', 'apply_settings', 'get_device_variable', 'set_device_variable', 'get_frame_period'], 'action_targets': {}, 'metadata': {'repo': 'AlexShkarin/pyLabLib', 'repo_url': 'https://github.com/AlexShkarin/pyLabLib', 'brand': 'Andor', 'model': 'iXon', 'device_type_cn': 'EMCCD相机', 'device_type_en': 'EMCCD Camera', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 766, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def is_opened(self, **kwargs):
        return self.call('is_opened', kwargs=kwargs)

    def get_device_info(self, **kwargs):
        return self.call('get_device_info', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def acquisition_in_progress(self, **kwargs):
        return self.call('acquisition_in_progress', kwargs=kwargs)

    def get_capabilities(self, **kwargs):
        return self.call('get_capabilities', kwargs=kwargs)

    def get_pixel_size(self, **kwargs):
        return self.call('get_pixel_size', kwargs=kwargs)

    def is_cooler_on(self, **kwargs):
        return self.call('is_cooler_on', kwargs=kwargs)

    def set_cooler(self, **kwargs):
        return self.call('set_cooler', kwargs=kwargs)

    def get_temperature_status(self, **kwargs):
        return self.call('get_temperature_status', kwargs=kwargs)

    def get_temperature(self, **kwargs):
        return self.call('get_temperature', kwargs=kwargs)

    def set_temperature(self, **kwargs):
        return self.call('set_temperature', kwargs=kwargs)

    def get_temperature_setpoint(self, **kwargs):
        return self.call('get_temperature_setpoint', kwargs=kwargs)

    def get_temperature_range(self, **kwargs):
        return self.call('get_temperature_range', kwargs=kwargs)

    def get_all_amp_modes(self, **kwargs):
        return self.call('get_all_amp_modes', kwargs=kwargs)

    def get_max_vsspeed(self, **kwargs):
        return self.call('get_max_vsspeed', kwargs=kwargs)

    def get_all_vsspeeds(self, **kwargs):
        return self.call('get_all_vsspeeds', kwargs=kwargs)

    def set_amp_mode(self, **kwargs):
        return self.call('set_amp_mode', kwargs=kwargs)

    def get_amp_mode(self, **kwargs):
        return self.call('get_amp_mode', kwargs=kwargs)

    def set_vsspeed(self, **kwargs):
        return self.call('set_vsspeed', kwargs=kwargs)

    def get_channel(self, **kwargs):
        return self.call('get_channel', kwargs=kwargs)

    def get_channel_bitdepth(self, **kwargs):
        return self.call('get_channel_bitdepth', kwargs=kwargs)

    def get_oamp(self, **kwargs):
        return self.call('get_oamp', kwargs=kwargs)

    def get_oamp_desc(self, **kwargs):
        return self.call('get_oamp_desc', kwargs=kwargs)

    def get_hsspeed(self, **kwargs):
        return self.call('get_hsspeed', kwargs=kwargs)

    def get_hsspeed_frequency(self, **kwargs):
        return self.call('get_hsspeed_frequency', kwargs=kwargs)

    def get_preamp(self, **kwargs):
        return self.call('get_preamp', kwargs=kwargs)

    def get_preamp_gain(self, **kwargs):
        return self.call('get_preamp_gain', kwargs=kwargs)

    def get_vsspeed(self, **kwargs):
        return self.call('get_vsspeed', kwargs=kwargs)

    def get_vsspeed_period(self, **kwargs):
        return self.call('get_vsspeed_period', kwargs=kwargs)

    def get_EMCCD_gain(self, **kwargs):
        return self.call('get_EMCCD_gain', kwargs=kwargs)

    def set_EMCCD_gain(self, **kwargs):
        return self.call('set_EMCCD_gain', kwargs=kwargs)

    def init_amp_mode(self, **kwargs):
        return self.call('init_amp_mode', kwargs=kwargs)

    def get_min_shutter_times(self, **kwargs):
        return self.call('get_min_shutter_times', kwargs=kwargs)

    def setup_shutter(self, **kwargs):
        return self.call('setup_shutter', kwargs=kwargs)

    def get_shutter_parameters(self, **kwargs):
        return self.call('get_shutter_parameters', kwargs=kwargs)

    def get_shutter(self, **kwargs):
        return self.call('get_shutter', kwargs=kwargs)

    def set_fan_mode(self, **kwargs):
        return self.call('set_fan_mode', kwargs=kwargs)

    def get_fan_mode(self, **kwargs):
        return self.call('get_fan_mode', kwargs=kwargs)

    def read_in_aux_port(self, **kwargs):
        return self.call('read_in_aux_port', kwargs=kwargs)

    def set_out_aux_port(self, **kwargs):
        return self.call('set_out_aux_port', kwargs=kwargs)

    def set_trigger_mode(self, **kwargs):
        return self.call('set_trigger_mode', kwargs=kwargs)

    def get_trigger_mode(self, **kwargs):
        return self.call('get_trigger_mode', kwargs=kwargs)

    def get_trigger_level_limits(self, **kwargs):
        return self.call('get_trigger_level_limits', kwargs=kwargs)

    def setup_ext_trigger(self, **kwargs):
        return self.call('setup_ext_trigger', kwargs=kwargs)

    def get_ext_trigger_parameters(self, **kwargs):
        return self.call('get_ext_trigger_parameters', kwargs=kwargs)

    def send_software_trigger(self, **kwargs):
        return self.call('send_software_trigger', kwargs=kwargs)

    def set_acquisition_mode(self, **kwargs):
        return self.call('set_acquisition_mode', kwargs=kwargs)

    def get_acquisition_mode(self, **kwargs):
        return self.call('get_acquisition_mode', kwargs=kwargs)

    def setup_accum_mode(self, **kwargs):
        return self.call('setup_accum_mode', kwargs=kwargs)

    def get_accum_mode_parameters(self, **kwargs):
        return self.call('get_accum_mode_parameters', kwargs=kwargs)

    def setup_kinetic_mode(self, **kwargs):
        return self.call('setup_kinetic_mode', kwargs=kwargs)

    def get_kinetic_mode_parameters(self, **kwargs):
        return self.call('get_kinetic_mode_parameters', kwargs=kwargs)

    def setup_fast_kinetic_mode(self, **kwargs):
        return self.call('setup_fast_kinetic_mode', kwargs=kwargs)

    def get_fast_kinetic_mode_parameters(self, **kwargs):
        return self.call('get_fast_kinetic_mode_parameters', kwargs=kwargs)

    def setup_cont_mode(self, **kwargs):
        return self.call('setup_cont_mode', kwargs=kwargs)

    def get_cont_mode_parameters(self, **kwargs):
        return self.call('get_cont_mode_parameters', kwargs=kwargs)

    def set_exposure(self, **kwargs):
        return self.call('set_exposure', kwargs=kwargs)

    def get_exposure(self, **kwargs):
        return self.call('get_exposure', kwargs=kwargs)

    def set_frame_period(self, **kwargs):
        return self.call('set_frame_period', kwargs=kwargs)

    def enable_frame_transfer_mode(self, **kwargs):
        return self.call('enable_frame_transfer_mode', kwargs=kwargs)

    def is_frame_transfer_enabled(self, **kwargs):
        return self.call('is_frame_transfer_enabled', kwargs=kwargs)

    def get_cycle_timings(self, **kwargs):
        return self.call('get_cycle_timings', kwargs=kwargs)

    def get_frame_timings(self, **kwargs):
        return self.call('get_frame_timings', kwargs=kwargs)

    def get_readout_time(self, **kwargs):
        return self.call('get_readout_time', kwargs=kwargs)

    def get_keepclean_time(self, **kwargs):
        return self.call('get_keepclean_time', kwargs=kwargs)

    def set_read_mode(self, **kwargs):
        return self.call('set_read_mode', kwargs=kwargs)

    def get_read_mode(self, **kwargs):
        return self.call('get_read_mode', kwargs=kwargs)

    def setup_single_track_mode(self, **kwargs):
        return self.call('setup_single_track_mode', kwargs=kwargs)

    def get_single_track_mode_parameters(self, **kwargs):
        return self.call('get_single_track_mode_parameters', kwargs=kwargs)

    def setup_multi_track_mode(self, **kwargs):
        return self.call('setup_multi_track_mode', kwargs=kwargs)

    def get_multi_track_mode_parameters(self, **kwargs):
        return self.call('get_multi_track_mode_parameters', kwargs=kwargs)

    def setup_random_track_mode(self, **kwargs):
        return self.call('setup_random_track_mode', kwargs=kwargs)

    def get_random_track_mode_parameters(self, **kwargs):
        return self.call('get_random_track_mode_parameters', kwargs=kwargs)

    def setup_image_mode(self, **kwargs):
        return self.call('setup_image_mode', kwargs=kwargs)

    def get_image_mode_parameters(self, **kwargs):
        return self.call('get_image_mode_parameters', kwargs=kwargs)

    def get_detector_size(self, **kwargs):
        return self.call('get_detector_size', kwargs=kwargs)

    def get_roi(self, **kwargs):
        return self.call('get_roi', kwargs=kwargs)

    def set_roi(self, **kwargs):
        return self.call('set_roi', kwargs=kwargs)

    def get_roi_limits(self, **kwargs):
        return self.call('get_roi_limits', kwargs=kwargs)

    def setup_acquisition(self, **kwargs):
        return self.call('setup_acquisition', kwargs=kwargs)

    def clear_acquisition(self, **kwargs):
        return self.call('clear_acquisition', kwargs=kwargs)

    def start_acquisition(self, **kwargs):
        return self.call('start_acquisition', kwargs=kwargs)

    def stop_acquisition(self, **kwargs):
        return self.call('stop_acquisition', kwargs=kwargs)

    def get_acquisition_progress(self, **kwargs):
        return self.call('get_acquisition_progress', kwargs=kwargs)

    def get_buffer_size(self, **kwargs):
        return self.call('get_buffer_size', kwargs=kwargs)

    def is_acquisition_setup(self, **kwargs):
        return self.call('is_acquisition_setup', kwargs=kwargs)

    def get_acquisition_parameters(self, **kwargs):
        return self.call('get_acquisition_parameters', kwargs=kwargs)

    def pausing_acquisition(self, **kwargs):
        return self.call('pausing_acquisition', kwargs=kwargs)

    def get_frames_status(self, **kwargs):
        return self.call('get_frames_status', kwargs=kwargs)

    def wait_for_frame(self, **kwargs):
        return self.call('wait_for_frame', kwargs=kwargs)

    def get_image_indexing(self, **kwargs):
        return self.call('get_image_indexing', kwargs=kwargs)

    def set_image_indexing(self, **kwargs):
        return self.call('set_image_indexing', kwargs=kwargs)

    def get_data_dimensions(self, **kwargs):
        return self.call('get_data_dimensions', kwargs=kwargs)

    def get_frame_format(self, **kwargs):
        return self.call('get_frame_format', kwargs=kwargs)

    def set_frame_format(self, **kwargs):
        return self.call('set_frame_format', kwargs=kwargs)

    def get_frame_info_format(self, **kwargs):
        return self.call('get_frame_info_format', kwargs=kwargs)

    def set_frame_info_format(self, **kwargs):
        return self.call('set_frame_info_format', kwargs=kwargs)

    def get_frame_info_period(self, **kwargs):
        return self.call('get_frame_info_period', kwargs=kwargs)

    def set_frame_info_period(self, **kwargs):
        return self.call('set_frame_info_period', kwargs=kwargs)

    def get_frame_info_fields(self, **kwargs):
        return self.call('get_frame_info_fields', kwargs=kwargs)

    def get_new_images_range(self, **kwargs):
        return self.call('get_new_images_range', kwargs=kwargs)

    def read_multiple_images(self, **kwargs):
        return self.call('read_multiple_images', kwargs=kwargs)

    def read_oldest_image(self, **kwargs):
        return self.call('read_oldest_image', kwargs=kwargs)

    def read_newest_image(self, **kwargs):
        return self.call('read_newest_image', kwargs=kwargs)

    def grab(self, **kwargs):
        return self.call('grab', kwargs=kwargs)

    def snap(self, **kwargs):
        return self.call('snap', kwargs=kwargs)

    def get_settings(self, **kwargs):
        return self.call('get_settings', kwargs=kwargs)

    def get_full_status(self, **kwargs):
        return self.call('get_full_status', kwargs=kwargs)

    def get_full_info(self, **kwargs):
        return self.call('get_full_info', kwargs=kwargs)

    def apply_settings(self, **kwargs):
        return self.call('apply_settings', kwargs=kwargs)

    def get_device_variable(self, **kwargs):
        return self.call('get_device_variable', kwargs=kwargs)

    def set_device_variable(self, **kwargs):
        return self.call('set_device_variable', kwargs=kwargs)

    def get_frame_period(self, **kwargs):
        return self.call('get_frame_period', kwargs=kwargs)

