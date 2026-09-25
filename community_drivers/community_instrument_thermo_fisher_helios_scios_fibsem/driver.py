from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThermoFisherHeliosSciosFibsem(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/DeMarcoLab__fibsem', 'source_file': 'fibsem/microscope.py', 'class_name': 'FibsemMicroscope', 'import_roots': [], 'candidate_methods': ['connect_to_microscope', 'disconnect', 'acquire_image', 'last_image', 'is_acquiring', 'start_acquisition', 'stop_acquisition', 'acquire_chamber_image', 'autocontrast', 'auto_focus', 'reset_beam_shifts', 'beam_shift', 'get_stage_position', 'move_stage_absolute', 'move_stage_relative', 'stable_move', 'vertical_move', 'project_stable_move', 'move_flat_to_beam', 'safe_absolute_stage_movement', 'get_manipulator_state', 'get_manipulator_position', 'insert_manipulator', 'retract_manipulator', 'move_manipulator_relative', 'move_manipulator_absolute', 'move_manipulator_corrected', 'move_manipulator_to_position_offset', 'setup_milling', 'run_milling', 'finish_milling', 'stop_milling', 'pause_milling', 'resume_milling', 'get_milling_state', 'estimate_milling_time', 'draw_rectangle', 'draw_line', 'draw_circle', 'draw_bitmap_pattern', 'cryo_deposition_v2', 'setup_sputter', 'draw_sputter_pattern', 'run_sputter', 'finish_sputter', 'get_available_values', 'get', 'set', 'get_imaging_settings', 'set_imaging_settings', 'get_beam_settings', 'set_beam_settings', 'get_beam_system_settings', 'set_beam_system_settings', 'get_detector_settings', 'set_detector_settings', 'get_microscope_state', 'set_microscope_state', 'set_milling_settings', 'is_available', 'set_available', 'apply_configuration', 'check_available_values', 'home', 'link_stage', 'pump', 'vent', 'turn_on', 'turn_off', 'is_on', 'blank', 'unblank', 'is_blanked', 'get_available_beams', 'set_spot_scanning_mode', 'set_reduced_area_scanning_mode', 'set_full_frame_scanning_mode', 'get_beam_current', 'set_beam_current', 'get_beam_voltage', 'set_beam_voltage', 'set_resolution', 'get_resolution', 'get_field_of_view', 'set_field_of_view', 'get_working_distance', 'set_working_distance', 'get_dwell_time', 'set_dwell_time', 'get_stigmation', 'set_stigmation', 'get_beam_shift', 'set_beam_shift', 'get_scan_rotation', 'set_scan_rotation', 'get_detector_type', 'set_detector_type', 'get_detector_mode', 'set_detector_mode', 'get_detector_contrast', 'set_detector_contrast', 'get_detector_brightness', 'set_detector_brightness', 'get_target_position', 'get_stage_orientation', 'get_orientation', 'get_current_milling_angle'], 'action_targets': {}, 'metadata': {'repo': 'DeMarcoLab/fibsem', 'repo_url': 'https://github.com/DeMarcoLab/fibsem', 'brand': 'Thermo Fisher', 'model': 'Helios/Scios (fibsem)', 'device_type_cn': '扫描电子显微镜', 'device_type_en': 'SEM', 'source_framework': 'fibsem', 'tag_id': '4390', 'tag_name': '扫描电子显微镜', 'tag_name_en': 'Scanning Electron Microscope', 'candidate_score': 954, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect_to_microscope(self, **kwargs):
        return self.call('connect_to_microscope', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def acquire_image(self, **kwargs):
        return self.call('acquire_image', kwargs=kwargs)

    def last_image(self, **kwargs):
        return self.call('last_image', kwargs=kwargs)

    def is_acquiring(self, **kwargs):
        return self.call('is_acquiring', kwargs=kwargs)

    def start_acquisition(self, **kwargs):
        return self.call('start_acquisition', kwargs=kwargs)

    def stop_acquisition(self, **kwargs):
        return self.call('stop_acquisition', kwargs=kwargs)

    def acquire_chamber_image(self, **kwargs):
        return self.call('acquire_chamber_image', kwargs=kwargs)

    def autocontrast(self, **kwargs):
        return self.call('autocontrast', kwargs=kwargs)

    def auto_focus(self, **kwargs):
        return self.call('auto_focus', kwargs=kwargs)

    def reset_beam_shifts(self, **kwargs):
        return self.call('reset_beam_shifts', kwargs=kwargs)

    def beam_shift(self, **kwargs):
        return self.call('beam_shift', kwargs=kwargs)

    def get_stage_position(self, **kwargs):
        return self.call('get_stage_position', kwargs=kwargs)

    def move_stage_absolute(self, **kwargs):
        return self.call('move_stage_absolute', kwargs=kwargs)

    def move_stage_relative(self, **kwargs):
        return self.call('move_stage_relative', kwargs=kwargs)

    def stable_move(self, **kwargs):
        return self.call('stable_move', kwargs=kwargs)

    def vertical_move(self, **kwargs):
        return self.call('vertical_move', kwargs=kwargs)

    def project_stable_move(self, **kwargs):
        return self.call('project_stable_move', kwargs=kwargs)

    def move_flat_to_beam(self, **kwargs):
        return self.call('move_flat_to_beam', kwargs=kwargs)

    def safe_absolute_stage_movement(self, **kwargs):
        return self.call('safe_absolute_stage_movement', kwargs=kwargs)

    def get_manipulator_state(self, **kwargs):
        return self.call('get_manipulator_state', kwargs=kwargs)

    def get_manipulator_position(self, **kwargs):
        return self.call('get_manipulator_position', kwargs=kwargs)

    def insert_manipulator(self, **kwargs):
        return self.call('insert_manipulator', kwargs=kwargs)

    def retract_manipulator(self, **kwargs):
        return self.call('retract_manipulator', kwargs=kwargs)

    def move_manipulator_relative(self, **kwargs):
        return self.call('move_manipulator_relative', kwargs=kwargs)

    def move_manipulator_absolute(self, **kwargs):
        return self.call('move_manipulator_absolute', kwargs=kwargs)

    def move_manipulator_corrected(self, **kwargs):
        return self.call('move_manipulator_corrected', kwargs=kwargs)

    def move_manipulator_to_position_offset(self, **kwargs):
        return self.call('move_manipulator_to_position_offset', kwargs=kwargs)

    def setup_milling(self, **kwargs):
        return self.call('setup_milling', kwargs=kwargs)

    def run_milling(self, **kwargs):
        return self.call('run_milling', kwargs=kwargs)

    def finish_milling(self, **kwargs):
        return self.call('finish_milling', kwargs=kwargs)

    def stop_milling(self, **kwargs):
        return self.call('stop_milling', kwargs=kwargs)

    def pause_milling(self, **kwargs):
        return self.call('pause_milling', kwargs=kwargs)

    def resume_milling(self, **kwargs):
        return self.call('resume_milling', kwargs=kwargs)

    def get_milling_state(self, **kwargs):
        return self.call('get_milling_state', kwargs=kwargs)

    def estimate_milling_time(self, **kwargs):
        return self.call('estimate_milling_time', kwargs=kwargs)

    def draw_rectangle(self, **kwargs):
        return self.call('draw_rectangle', kwargs=kwargs)

    def draw_line(self, **kwargs):
        return self.call('draw_line', kwargs=kwargs)

    def draw_circle(self, **kwargs):
        return self.call('draw_circle', kwargs=kwargs)

    def draw_bitmap_pattern(self, **kwargs):
        return self.call('draw_bitmap_pattern', kwargs=kwargs)

    def cryo_deposition_v2(self, **kwargs):
        return self.call('cryo_deposition_v2', kwargs=kwargs)

    def setup_sputter(self, **kwargs):
        return self.call('setup_sputter', kwargs=kwargs)

    def draw_sputter_pattern(self, **kwargs):
        return self.call('draw_sputter_pattern', kwargs=kwargs)

    def run_sputter(self, **kwargs):
        return self.call('run_sputter', kwargs=kwargs)

    def finish_sputter(self, **kwargs):
        return self.call('finish_sputter', kwargs=kwargs)

    def get_available_values(self, **kwargs):
        return self.call('get_available_values', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def set(self, **kwargs):
        return self.call('set', kwargs=kwargs)

    def get_imaging_settings(self, **kwargs):
        return self.call('get_imaging_settings', kwargs=kwargs)

    def set_imaging_settings(self, **kwargs):
        return self.call('set_imaging_settings', kwargs=kwargs)

    def get_beam_settings(self, **kwargs):
        return self.call('get_beam_settings', kwargs=kwargs)

    def set_beam_settings(self, **kwargs):
        return self.call('set_beam_settings', kwargs=kwargs)

    def get_beam_system_settings(self, **kwargs):
        return self.call('get_beam_system_settings', kwargs=kwargs)

    def set_beam_system_settings(self, **kwargs):
        return self.call('set_beam_system_settings', kwargs=kwargs)

    def get_detector_settings(self, **kwargs):
        return self.call('get_detector_settings', kwargs=kwargs)

    def set_detector_settings(self, **kwargs):
        return self.call('set_detector_settings', kwargs=kwargs)

    def get_microscope_state(self, **kwargs):
        return self.call('get_microscope_state', kwargs=kwargs)

    def set_microscope_state(self, **kwargs):
        return self.call('set_microscope_state', kwargs=kwargs)

    def set_milling_settings(self, **kwargs):
        return self.call('set_milling_settings', kwargs=kwargs)

    def is_available(self, **kwargs):
        return self.call('is_available', kwargs=kwargs)

    def set_available(self, **kwargs):
        return self.call('set_available', kwargs=kwargs)

    def apply_configuration(self, **kwargs):
        return self.call('apply_configuration', kwargs=kwargs)

    def check_available_values(self, **kwargs):
        return self.call('check_available_values', kwargs=kwargs)

    def home(self, **kwargs):
        return self.call('home', kwargs=kwargs)

    def link_stage(self, **kwargs):
        return self.call('link_stage', kwargs=kwargs)

    def pump(self, **kwargs):
        return self.call('pump', kwargs=kwargs)

    def vent(self, **kwargs):
        return self.call('vent', kwargs=kwargs)

    def turn_on(self, **kwargs):
        return self.call('turn_on', kwargs=kwargs)

    def turn_off(self, **kwargs):
        return self.call('turn_off', kwargs=kwargs)

    def is_on(self, **kwargs):
        return self.call('is_on', kwargs=kwargs)

    def blank(self, **kwargs):
        return self.call('blank', kwargs=kwargs)

    def unblank(self, **kwargs):
        return self.call('unblank', kwargs=kwargs)

    def is_blanked(self, **kwargs):
        return self.call('is_blanked', kwargs=kwargs)

    def get_available_beams(self, **kwargs):
        return self.call('get_available_beams', kwargs=kwargs)

    def set_spot_scanning_mode(self, **kwargs):
        return self.call('set_spot_scanning_mode', kwargs=kwargs)

    def set_reduced_area_scanning_mode(self, **kwargs):
        return self.call('set_reduced_area_scanning_mode', kwargs=kwargs)

    def set_full_frame_scanning_mode(self, **kwargs):
        return self.call('set_full_frame_scanning_mode', kwargs=kwargs)

    def get_beam_current(self, **kwargs):
        return self.call('get_beam_current', kwargs=kwargs)

    def set_beam_current(self, **kwargs):
        return self.call('set_beam_current', kwargs=kwargs)

    def get_beam_voltage(self, **kwargs):
        return self.call('get_beam_voltage', kwargs=kwargs)

    def set_beam_voltage(self, **kwargs):
        return self.call('set_beam_voltage', kwargs=kwargs)

    def set_resolution(self, **kwargs):
        return self.call('set_resolution', kwargs=kwargs)

    def get_resolution(self, **kwargs):
        return self.call('get_resolution', kwargs=kwargs)

    def get_field_of_view(self, **kwargs):
        return self.call('get_field_of_view', kwargs=kwargs)

    def set_field_of_view(self, **kwargs):
        return self.call('set_field_of_view', kwargs=kwargs)

    def get_working_distance(self, **kwargs):
        return self.call('get_working_distance', kwargs=kwargs)

    def set_working_distance(self, **kwargs):
        return self.call('set_working_distance', kwargs=kwargs)

    def get_dwell_time(self, **kwargs):
        return self.call('get_dwell_time', kwargs=kwargs)

    def set_dwell_time(self, **kwargs):
        return self.call('set_dwell_time', kwargs=kwargs)

    def get_stigmation(self, **kwargs):
        return self.call('get_stigmation', kwargs=kwargs)

    def set_stigmation(self, **kwargs):
        return self.call('set_stigmation', kwargs=kwargs)

    def get_beam_shift(self, **kwargs):
        return self.call('get_beam_shift', kwargs=kwargs)

    def set_beam_shift(self, **kwargs):
        return self.call('set_beam_shift', kwargs=kwargs)

    def get_scan_rotation(self, **kwargs):
        return self.call('get_scan_rotation', kwargs=kwargs)

    def set_scan_rotation(self, **kwargs):
        return self.call('set_scan_rotation', kwargs=kwargs)

    def get_detector_type(self, **kwargs):
        return self.call('get_detector_type', kwargs=kwargs)

    def set_detector_type(self, **kwargs):
        return self.call('set_detector_type', kwargs=kwargs)

    def get_detector_mode(self, **kwargs):
        return self.call('get_detector_mode', kwargs=kwargs)

    def set_detector_mode(self, **kwargs):
        return self.call('set_detector_mode', kwargs=kwargs)

    def get_detector_contrast(self, **kwargs):
        return self.call('get_detector_contrast', kwargs=kwargs)

    def set_detector_contrast(self, **kwargs):
        return self.call('set_detector_contrast', kwargs=kwargs)

    def get_detector_brightness(self, **kwargs):
        return self.call('get_detector_brightness', kwargs=kwargs)

    def set_detector_brightness(self, **kwargs):
        return self.call('set_detector_brightness', kwargs=kwargs)

    def get_target_position(self, **kwargs):
        return self.call('get_target_position', kwargs=kwargs)

    def get_stage_orientation(self, **kwargs):
        return self.call('get_stage_orientation', kwargs=kwargs)

    def get_orientation(self, **kwargs):
        return self.call('get_orientation', kwargs=kwargs)

    def get_current_milling_angle(self, **kwargs):
        return self.call('get_current_milling_angle', kwargs=kwargs)

