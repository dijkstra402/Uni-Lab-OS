from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPhysikInstrumenteE861(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/delmic__odemis', 'source_file': 'src/odemis/driver/autoscript_client.py', 'class_name': 'SEM', 'import_roots': ['src'], 'candidate_methods': ['terminate', 'transfer_latest_package', 'get_software_version', 'get_hardware_version', 'move_stage_absolute', 'move_stage_relative', 'stop_stage_movement', 'get_stage_position', 'stage_info', 'set_default_stage_coordinate_system', 'get_stage_coordinate_system', 'home_stage', 'is_homed', 'link', 'is_linked', 'pump', 'vent', 'get_chamber_state', 'get_pressure', 'pressure_info', 'set_external_scan_mode', 'set_full_frame_scan_mode', 'set_spot_scan_mode', 'set_line_scan_mode', 'set_crossover_scan_mode', 'set_reduced_area_scan_mode', 'set_scan_mode', 'get_scan_mode', 'scan_mode_info', 'set_spotsize', 'get_spotsize', 'spotsize_info', 'set_dwell_time', 'get_dwell_time', 'dwell_time_info', 'set_field_of_view', 'get_field_of_view', 'field_of_view_info', 'set_high_voltage', 'get_high_voltage', 'high_voltage_info', 'set_beam_current', 'get_beam_current', 'beam_current_info', 'blank_beam', 'unblank_beam', 'beam_is_blanked', 'beam_is_installed', 'get_working_distance', 'set_working_distance', 'working_distance_info', 'get_beam_shift', 'set_beam_shift', 'move_beam_shift', 'beam_shift_info', 'get_stigmator', 'set_stigmator', 'stigmator_info', 'get_scan_rotation', 'set_scan_rotation', 'scan_rotation_info', 'set_resolution', 'get_resolution', 'resolution_info', 'set_beam_power', 'get_beam_is_on', 'set_detector_mode', 'get_detector_mode', 'detector_mode_info', 'set_detector_type', 'get_detector_type', 'detector_type_info', 'set_contrast', 'get_contrast', 'contrast_info', 'set_brightness', 'get_brightness', 'brightness_info', 'get_active_view', 'get_active_device', 'set_active_view', 'set_active_device', 'set_channel', 'acquire_image', 'get_last_image', 'start_acquisition', 'stop_acquisition', 'get_imaging_state', 'set_scanning_filter', 'get_scanning_filter', 'get_scanning_filter_info', 'run_auto_contrast_brightness', 'create_rectangle', 'create_cleaning_cross_section', 'create_regular_cross_section', 'create_line', 'create_circle', 'start_milling', 'run_milling', 'pause_milling', 'stop_milling', 'resume_milling', 'get_patterning_state', 'get_patterning_mode', 'set_patterning_mode', 'clear_patterns', 'set_default_application_file', 'set_default_patterning_beam_type', 'get_available_application_files', 'estimate_milling_time', 'role', 'swVersion', 'hwVersion', 'updateMetadata', 'getMetadata', 'selfTest', 'parent', 'name'], 'action_targets': {}, 'metadata': {'repo': 'delmic/odemis', 'repo_url': 'https://github.com/delmic/odemis', 'brand': 'Physik Instrumente', 'model': 'E-861', 'device_type_cn': '压电电机控制器', 'device_type_en': 'Piezo Motor Controller', 'source_framework': 'odemis', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 918, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def terminate(self, **kwargs):
        return self.call('terminate', kwargs=kwargs)

    def transfer_latest_package(self, **kwargs):
        return self.call('transfer_latest_package', kwargs=kwargs)

    def get_software_version(self, **kwargs):
        return self.call('get_software_version', kwargs=kwargs)

    def get_hardware_version(self, **kwargs):
        return self.call('get_hardware_version', kwargs=kwargs)

    def move_stage_absolute(self, **kwargs):
        return self.call('move_stage_absolute', kwargs=kwargs)

    def move_stage_relative(self, **kwargs):
        return self.call('move_stage_relative', kwargs=kwargs)

    def stop_stage_movement(self, **kwargs):
        return self.call('stop_stage_movement', kwargs=kwargs)

    def get_stage_position(self, **kwargs):
        return self.call('get_stage_position', kwargs=kwargs)

    def stage_info(self, **kwargs):
        return self.call('stage_info', kwargs=kwargs)

    def set_default_stage_coordinate_system(self, **kwargs):
        return self.call('set_default_stage_coordinate_system', kwargs=kwargs)

    def get_stage_coordinate_system(self, **kwargs):
        return self.call('get_stage_coordinate_system', kwargs=kwargs)

    def home_stage(self, **kwargs):
        return self.call('home_stage', kwargs=kwargs)

    def is_homed(self, **kwargs):
        return self.call('is_homed', kwargs=kwargs)

    def link(self, **kwargs):
        return self.call('link', kwargs=kwargs)

    def is_linked(self, **kwargs):
        return self.call('is_linked', kwargs=kwargs)

    def pump(self, **kwargs):
        return self.call('pump', kwargs=kwargs)

    def vent(self, **kwargs):
        return self.call('vent', kwargs=kwargs)

    def get_chamber_state(self, **kwargs):
        return self.call('get_chamber_state', kwargs=kwargs)

    def get_pressure(self, **kwargs):
        return self.call('get_pressure', kwargs=kwargs)

    def pressure_info(self, **kwargs):
        return self.call('pressure_info', kwargs=kwargs)

    def set_external_scan_mode(self, **kwargs):
        return self.call('set_external_scan_mode', kwargs=kwargs)

    def set_full_frame_scan_mode(self, **kwargs):
        return self.call('set_full_frame_scan_mode', kwargs=kwargs)

    def set_spot_scan_mode(self, **kwargs):
        return self.call('set_spot_scan_mode', kwargs=kwargs)

    def set_line_scan_mode(self, **kwargs):
        return self.call('set_line_scan_mode', kwargs=kwargs)

    def set_crossover_scan_mode(self, **kwargs):
        return self.call('set_crossover_scan_mode', kwargs=kwargs)

    def set_reduced_area_scan_mode(self, **kwargs):
        return self.call('set_reduced_area_scan_mode', kwargs=kwargs)

    def set_scan_mode(self, **kwargs):
        return self.call('set_scan_mode', kwargs=kwargs)

    def get_scan_mode(self, **kwargs):
        return self.call('get_scan_mode', kwargs=kwargs)

    def scan_mode_info(self, **kwargs):
        return self.call('scan_mode_info', kwargs=kwargs)

    def set_spotsize(self, **kwargs):
        return self.call('set_spotsize', kwargs=kwargs)

    def get_spotsize(self, **kwargs):
        return self.call('get_spotsize', kwargs=kwargs)

    def spotsize_info(self, **kwargs):
        return self.call('spotsize_info', kwargs=kwargs)

    def set_dwell_time(self, **kwargs):
        return self.call('set_dwell_time', kwargs=kwargs)

    def get_dwell_time(self, **kwargs):
        return self.call('get_dwell_time', kwargs=kwargs)

    def dwell_time_info(self, **kwargs):
        return self.call('dwell_time_info', kwargs=kwargs)

    def set_field_of_view(self, **kwargs):
        return self.call('set_field_of_view', kwargs=kwargs)

    def get_field_of_view(self, **kwargs):
        return self.call('get_field_of_view', kwargs=kwargs)

    def field_of_view_info(self, **kwargs):
        return self.call('field_of_view_info', kwargs=kwargs)

    def set_high_voltage(self, **kwargs):
        return self.call('set_high_voltage', kwargs=kwargs)

    def get_high_voltage(self, **kwargs):
        return self.call('get_high_voltage', kwargs=kwargs)

    def high_voltage_info(self, **kwargs):
        return self.call('high_voltage_info', kwargs=kwargs)

    def set_beam_current(self, **kwargs):
        return self.call('set_beam_current', kwargs=kwargs)

    def get_beam_current(self, **kwargs):
        return self.call('get_beam_current', kwargs=kwargs)

    def beam_current_info(self, **kwargs):
        return self.call('beam_current_info', kwargs=kwargs)

    def blank_beam(self, **kwargs):
        return self.call('blank_beam', kwargs=kwargs)

    def unblank_beam(self, **kwargs):
        return self.call('unblank_beam', kwargs=kwargs)

    def beam_is_blanked(self, **kwargs):
        return self.call('beam_is_blanked', kwargs=kwargs)

    def beam_is_installed(self, **kwargs):
        return self.call('beam_is_installed', kwargs=kwargs)

    def get_working_distance(self, **kwargs):
        return self.call('get_working_distance', kwargs=kwargs)

    def set_working_distance(self, **kwargs):
        return self.call('set_working_distance', kwargs=kwargs)

    def working_distance_info(self, **kwargs):
        return self.call('working_distance_info', kwargs=kwargs)

    def get_beam_shift(self, **kwargs):
        return self.call('get_beam_shift', kwargs=kwargs)

    def set_beam_shift(self, **kwargs):
        return self.call('set_beam_shift', kwargs=kwargs)

    def move_beam_shift(self, **kwargs):
        return self.call('move_beam_shift', kwargs=kwargs)

    def beam_shift_info(self, **kwargs):
        return self.call('beam_shift_info', kwargs=kwargs)

    def get_stigmator(self, **kwargs):
        return self.call('get_stigmator', kwargs=kwargs)

    def set_stigmator(self, **kwargs):
        return self.call('set_stigmator', kwargs=kwargs)

    def stigmator_info(self, **kwargs):
        return self.call('stigmator_info', kwargs=kwargs)

    def get_scan_rotation(self, **kwargs):
        return self.call('get_scan_rotation', kwargs=kwargs)

    def set_scan_rotation(self, **kwargs):
        return self.call('set_scan_rotation', kwargs=kwargs)

    def scan_rotation_info(self, **kwargs):
        return self.call('scan_rotation_info', kwargs=kwargs)

    def set_resolution(self, **kwargs):
        return self.call('set_resolution', kwargs=kwargs)

    def get_resolution(self, **kwargs):
        return self.call('get_resolution', kwargs=kwargs)

    def resolution_info(self, **kwargs):
        return self.call('resolution_info', kwargs=kwargs)

    def set_beam_power(self, **kwargs):
        return self.call('set_beam_power', kwargs=kwargs)

    def get_beam_is_on(self, **kwargs):
        return self.call('get_beam_is_on', kwargs=kwargs)

    def set_detector_mode(self, **kwargs):
        return self.call('set_detector_mode', kwargs=kwargs)

    def get_detector_mode(self, **kwargs):
        return self.call('get_detector_mode', kwargs=kwargs)

    def detector_mode_info(self, **kwargs):
        return self.call('detector_mode_info', kwargs=kwargs)

    def set_detector_type(self, **kwargs):
        return self.call('set_detector_type', kwargs=kwargs)

    def get_detector_type(self, **kwargs):
        return self.call('get_detector_type', kwargs=kwargs)

    def detector_type_info(self, **kwargs):
        return self.call('detector_type_info', kwargs=kwargs)

    def set_contrast(self, **kwargs):
        return self.call('set_contrast', kwargs=kwargs)

    def get_contrast(self, **kwargs):
        return self.call('get_contrast', kwargs=kwargs)

    def contrast_info(self, **kwargs):
        return self.call('contrast_info', kwargs=kwargs)

    def set_brightness(self, **kwargs):
        return self.call('set_brightness', kwargs=kwargs)

    def get_brightness(self, **kwargs):
        return self.call('get_brightness', kwargs=kwargs)

    def brightness_info(self, **kwargs):
        return self.call('brightness_info', kwargs=kwargs)

    def get_active_view(self, **kwargs):
        return self.call('get_active_view', kwargs=kwargs)

    def get_active_device(self, **kwargs):
        return self.call('get_active_device', kwargs=kwargs)

    def set_active_view(self, **kwargs):
        return self.call('set_active_view', kwargs=kwargs)

    def set_active_device(self, **kwargs):
        return self.call('set_active_device', kwargs=kwargs)

    def set_channel(self, **kwargs):
        return self.call('set_channel', kwargs=kwargs)

    def acquire_image(self, **kwargs):
        return self.call('acquire_image', kwargs=kwargs)

    def get_last_image(self, **kwargs):
        return self.call('get_last_image', kwargs=kwargs)

    def start_acquisition(self, **kwargs):
        return self.call('start_acquisition', kwargs=kwargs)

    def stop_acquisition(self, **kwargs):
        return self.call('stop_acquisition', kwargs=kwargs)

    def get_imaging_state(self, **kwargs):
        return self.call('get_imaging_state', kwargs=kwargs)

    def set_scanning_filter(self, **kwargs):
        return self.call('set_scanning_filter', kwargs=kwargs)

    def get_scanning_filter(self, **kwargs):
        return self.call('get_scanning_filter', kwargs=kwargs)

    def get_scanning_filter_info(self, **kwargs):
        return self.call('get_scanning_filter_info', kwargs=kwargs)

    def run_auto_contrast_brightness(self, **kwargs):
        return self.call('run_auto_contrast_brightness', kwargs=kwargs)

    def create_rectangle(self, **kwargs):
        return self.call('create_rectangle', kwargs=kwargs)

    def create_cleaning_cross_section(self, **kwargs):
        return self.call('create_cleaning_cross_section', kwargs=kwargs)

    def create_regular_cross_section(self, **kwargs):
        return self.call('create_regular_cross_section', kwargs=kwargs)

    def create_line(self, **kwargs):
        return self.call('create_line', kwargs=kwargs)

    def create_circle(self, **kwargs):
        return self.call('create_circle', kwargs=kwargs)

    def start_milling(self, **kwargs):
        return self.call('start_milling', kwargs=kwargs)

    def run_milling(self, **kwargs):
        return self.call('run_milling', kwargs=kwargs)

    def pause_milling(self, **kwargs):
        return self.call('pause_milling', kwargs=kwargs)

    def stop_milling(self, **kwargs):
        return self.call('stop_milling', kwargs=kwargs)

    def resume_milling(self, **kwargs):
        return self.call('resume_milling', kwargs=kwargs)

    def get_patterning_state(self, **kwargs):
        return self.call('get_patterning_state', kwargs=kwargs)

    def get_patterning_mode(self, **kwargs):
        return self.call('get_patterning_mode', kwargs=kwargs)

    def set_patterning_mode(self, **kwargs):
        return self.call('set_patterning_mode', kwargs=kwargs)

    def clear_patterns(self, **kwargs):
        return self.call('clear_patterns', kwargs=kwargs)

    def set_default_application_file(self, **kwargs):
        return self.call('set_default_application_file', kwargs=kwargs)

    def set_default_patterning_beam_type(self, **kwargs):
        return self.call('set_default_patterning_beam_type', kwargs=kwargs)

    def get_available_application_files(self, **kwargs):
        return self.call('get_available_application_files', kwargs=kwargs)

    def estimate_milling_time(self, **kwargs):
        return self.call('estimate_milling_time', kwargs=kwargs)

    def role(self, **kwargs):
        return self.call('role', kwargs=kwargs)

    def swVersion(self, **kwargs):
        return self.call('swVersion', kwargs=kwargs)

    def hwVersion(self, **kwargs):
        return self.call('hwVersion', kwargs=kwargs)

    def updateMetadata(self, **kwargs):
        return self.call('updateMetadata', kwargs=kwargs)

    def getMetadata(self, **kwargs):
        return self.call('getMetadata', kwargs=kwargs)

    def selfTest(self, **kwargs):
        return self.call('selfTest', kwargs=kwargs)

    def parent(self, **kwargs):
        return self.call('parent', kwargs=kwargs)

    def name(self, **kwargs):
        return self.call('name', kwargs=kwargs)

