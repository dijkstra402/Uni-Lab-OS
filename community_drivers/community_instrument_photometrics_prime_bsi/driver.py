from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPhotometricsPrimeBsi(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Photometrics__PyVCAM', 'source_file': 'src/pyvcam/camera.py', 'class_name': 'Camera', 'import_roots': ['src'], 'candidate_methods': ['get_available_camera_names', 'detect_camera', 'select_camera', 'open', 'close', 'check_frame_status', 'get_param', 'set_param', 'check_param', 'read_enum', 'reset_pp', 'reset_rois', 'set_roi', 'poll_frame', 'get_frame', 'get_sequence', 'get_vtm_sequence', 'start_live', 'start_seq', 'finish', 'abort', 'sw_trigger', 'set_post_processing_param', 'get_post_processing_param', 'handle', 'is_open', 'name', 'post_processing_table', 'port_speed_gain_table', 'readout_ports', 'centroids_modes', 'clear_modes', 'exp_modes', 'exp_out_modes', 'exp_resolutions', 'fan_speeds', 'prog_scan_modes', 'prog_scan_dirs', 'driver_version', 'cam_fw', 'chip_name', 'sensor_size', 'serial_no', 'bit_depth', 'bit_depth_host', 'pix_time', 'readout_port', 'speed', 'speed_table_index', 'speed_name', 'trigger_table', 'adc_offset', 'gain', 'gain_name', 'binnings', 'binning', 'bin_x', 'bin_y', 'rois', 'shape', 'live_roi', 'last_exp_time', 'exp_res', 'exp_res_index', 'exp_time', 'exp_mode', 'exp_out_mode', 'vtm_exp_time', 'clear_mode', 'fan_speed', 'temp', 'temp_setpoint', 'readout_time', 'clear_time', 'pre_trigger_delay', 'post_trigger_delay', 'centroids_mode', 'prog_scan_mode', 'prog_scan_dir', 'prog_scan_dir_reset', 'prog_scan_line_delay', 'prog_scan_line_time', 'scan_line_time', 'prog_scan_width', 'metadata_enabled', 'meta_data_enabled', 'smart_stream_mode_enabled', 'smart_stream_mode', 'smart_stream_exp_params'], 'action_targets': {}, 'metadata': {'repo': 'Photometrics/PyVCAM', 'repo_url': 'https://github.com/Photometrics/PyVCAM', 'brand': 'Photometrics', 'model': 'Prime BSI', 'device_type_cn': 'sCMOS相机', 'device_type_en': 'sCMOS Camera', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 770, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_available_camera_names(self, **kwargs):
        return self.call('get_available_camera_names', kwargs=kwargs)

    def detect_camera(self, **kwargs):
        return self.call('detect_camera', kwargs=kwargs)

    def select_camera(self, **kwargs):
        return self.call('select_camera', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def check_frame_status(self, **kwargs):
        return self.call('check_frame_status', kwargs=kwargs)

    def get_param(self, **kwargs):
        return self.call('get_param', kwargs=kwargs)

    def set_param(self, **kwargs):
        return self.call('set_param', kwargs=kwargs)

    def check_param(self, **kwargs):
        return self.call('check_param', kwargs=kwargs)

    def read_enum(self, **kwargs):
        return self.call('read_enum', kwargs=kwargs)

    def reset_pp(self, **kwargs):
        return self.call('reset_pp', kwargs=kwargs)

    def reset_rois(self, **kwargs):
        return self.call('reset_rois', kwargs=kwargs)

    def set_roi(self, **kwargs):
        return self.call('set_roi', kwargs=kwargs)

    def poll_frame(self, **kwargs):
        return self.call('poll_frame', kwargs=kwargs)

    def get_frame(self, **kwargs):
        return self.call('get_frame', kwargs=kwargs)

    def get_sequence(self, **kwargs):
        return self.call('get_sequence', kwargs=kwargs)

    def get_vtm_sequence(self, **kwargs):
        return self.call('get_vtm_sequence', kwargs=kwargs)

    def start_live(self, **kwargs):
        return self.call('start_live', kwargs=kwargs)

    def start_seq(self, **kwargs):
        return self.call('start_seq', kwargs=kwargs)

    def finish(self, **kwargs):
        return self.call('finish', kwargs=kwargs)

    def abort(self, **kwargs):
        return self.call('abort', kwargs=kwargs)

    def sw_trigger(self, **kwargs):
        return self.call('sw_trigger', kwargs=kwargs)

    def set_post_processing_param(self, **kwargs):
        return self.call('set_post_processing_param', kwargs=kwargs)

    def get_post_processing_param(self, **kwargs):
        return self.call('get_post_processing_param', kwargs=kwargs)

    def handle(self, **kwargs):
        return self.call('handle', kwargs=kwargs)

    def is_open(self, **kwargs):
        return self.call('is_open', kwargs=kwargs)

    def name(self, **kwargs):
        return self.call('name', kwargs=kwargs)

    def post_processing_table(self, **kwargs):
        return self.call('post_processing_table', kwargs=kwargs)

    def port_speed_gain_table(self, **kwargs):
        return self.call('port_speed_gain_table', kwargs=kwargs)

    def readout_ports(self, **kwargs):
        return self.call('readout_ports', kwargs=kwargs)

    def centroids_modes(self, **kwargs):
        return self.call('centroids_modes', kwargs=kwargs)

    def clear_modes(self, **kwargs):
        return self.call('clear_modes', kwargs=kwargs)

    def exp_modes(self, **kwargs):
        return self.call('exp_modes', kwargs=kwargs)

    def exp_out_modes(self, **kwargs):
        return self.call('exp_out_modes', kwargs=kwargs)

    def exp_resolutions(self, **kwargs):
        return self.call('exp_resolutions', kwargs=kwargs)

    def fan_speeds(self, **kwargs):
        return self.call('fan_speeds', kwargs=kwargs)

    def prog_scan_modes(self, **kwargs):
        return self.call('prog_scan_modes', kwargs=kwargs)

    def prog_scan_dirs(self, **kwargs):
        return self.call('prog_scan_dirs', kwargs=kwargs)

    def driver_version(self, **kwargs):
        return self.call('driver_version', kwargs=kwargs)

    def cam_fw(self, **kwargs):
        return self.call('cam_fw', kwargs=kwargs)

    def chip_name(self, **kwargs):
        return self.call('chip_name', kwargs=kwargs)

    def sensor_size(self, **kwargs):
        return self.call('sensor_size', kwargs=kwargs)

    def serial_no(self, **kwargs):
        return self.call('serial_no', kwargs=kwargs)

    def bit_depth(self, **kwargs):
        return self.call('bit_depth', kwargs=kwargs)

    def bit_depth_host(self, **kwargs):
        return self.call('bit_depth_host', kwargs=kwargs)

    def pix_time(self, **kwargs):
        return self.call('pix_time', kwargs=kwargs)

    def readout_port(self, **kwargs):
        return self.call('readout_port', kwargs=kwargs)

    def speed(self, **kwargs):
        return self.call('speed', kwargs=kwargs)

    def speed_table_index(self, **kwargs):
        return self.call('speed_table_index', kwargs=kwargs)

    def speed_name(self, **kwargs):
        return self.call('speed_name', kwargs=kwargs)

    def trigger_table(self, **kwargs):
        return self.call('trigger_table', kwargs=kwargs)

    def adc_offset(self, **kwargs):
        return self.call('adc_offset', kwargs=kwargs)

    def gain(self, **kwargs):
        return self.call('gain', kwargs=kwargs)

    def gain_name(self, **kwargs):
        return self.call('gain_name', kwargs=kwargs)

    def binnings(self, **kwargs):
        return self.call('binnings', kwargs=kwargs)

    def binning(self, **kwargs):
        return self.call('binning', kwargs=kwargs)

    def bin_x(self, **kwargs):
        return self.call('bin_x', kwargs=kwargs)

    def bin_y(self, **kwargs):
        return self.call('bin_y', kwargs=kwargs)

    def rois(self, **kwargs):
        return self.call('rois', kwargs=kwargs)

    def shape(self, **kwargs):
        return self.call('shape', kwargs=kwargs)

    def live_roi(self, **kwargs):
        return self.call('live_roi', kwargs=kwargs)

    def last_exp_time(self, **kwargs):
        return self.call('last_exp_time', kwargs=kwargs)

    def exp_res(self, **kwargs):
        return self.call('exp_res', kwargs=kwargs)

    def exp_res_index(self, **kwargs):
        return self.call('exp_res_index', kwargs=kwargs)

    def exp_time(self, **kwargs):
        return self.call('exp_time', kwargs=kwargs)

    def exp_mode(self, **kwargs):
        return self.call('exp_mode', kwargs=kwargs)

    def exp_out_mode(self, **kwargs):
        return self.call('exp_out_mode', kwargs=kwargs)

    def vtm_exp_time(self, **kwargs):
        return self.call('vtm_exp_time', kwargs=kwargs)

    def clear_mode(self, **kwargs):
        return self.call('clear_mode', kwargs=kwargs)

    def fan_speed(self, **kwargs):
        return self.call('fan_speed', kwargs=kwargs)

    def temp(self, **kwargs):
        return self.call('temp', kwargs=kwargs)

    def temp_setpoint(self, **kwargs):
        return self.call('temp_setpoint', kwargs=kwargs)

    def readout_time(self, **kwargs):
        return self.call('readout_time', kwargs=kwargs)

    def clear_time(self, **kwargs):
        return self.call('clear_time', kwargs=kwargs)

    def pre_trigger_delay(self, **kwargs):
        return self.call('pre_trigger_delay', kwargs=kwargs)

    def post_trigger_delay(self, **kwargs):
        return self.call('post_trigger_delay', kwargs=kwargs)

    def centroids_mode(self, **kwargs):
        return self.call('centroids_mode', kwargs=kwargs)

    def prog_scan_mode(self, **kwargs):
        return self.call('prog_scan_mode', kwargs=kwargs)

    def prog_scan_dir(self, **kwargs):
        return self.call('prog_scan_dir', kwargs=kwargs)

    def prog_scan_dir_reset(self, **kwargs):
        return self.call('prog_scan_dir_reset', kwargs=kwargs)

    def prog_scan_line_delay(self, **kwargs):
        return self.call('prog_scan_line_delay', kwargs=kwargs)

    def prog_scan_line_time(self, **kwargs):
        return self.call('prog_scan_line_time', kwargs=kwargs)

    def scan_line_time(self, **kwargs):
        return self.call('scan_line_time', kwargs=kwargs)

    def prog_scan_width(self, **kwargs):
        return self.call('prog_scan_width', kwargs=kwargs)

    def metadata_enabled(self, **kwargs):
        return self.call('metadata_enabled', kwargs=kwargs)

    def meta_data_enabled(self, **kwargs):
        return self.call('meta_data_enabled', kwargs=kwargs)

    def smart_stream_mode_enabled(self, **kwargs):
        return self.call('smart_stream_mode_enabled', kwargs=kwargs)

    def smart_stream_mode(self, **kwargs):
        return self.call('smart_stream_mode', kwargs=kwargs)

    def smart_stream_exp_params(self, **kwargs):
        return self.call('smart_stream_exp_params', kwargs=kwargs)

