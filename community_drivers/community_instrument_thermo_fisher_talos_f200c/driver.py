from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThermoFisherTalosF200c(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/niermann__temscript', 'source_file': 'temscript/base_microscope.py', 'class_name': 'BaseMicroscope', 'import_roots': [], 'candidate_methods': ['get_family', 'get_microscope_id', 'get_version', 'get_voltage', 'get_vacuum', 'get_column_valves_open', 'set_column_valves_open', 'get_stage_holder', 'get_stage_status', 'get_stage_limits', 'get_stage_position', 'set_stage_position', 'get_cameras', 'get_stem_detectors', 'get_detectors', 'get_camera_param', 'set_camera_param', 'get_stem_detector_param', 'set_stem_detector_param', 'get_stem_acquisition_param', 'set_stem_acquisition_param', 'get_detector_param', 'set_detector_param', 'acquire', 'get_image_shift', 'set_image_shift', 'get_beam_shift', 'set_beam_shift', 'get_beam_tilt', 'set_beam_tilt', 'normalize', 'get_projection_sub_mode', 'get_projection_mode', 'set_projection_mode', 'get_projection_mode_string', 'get_magnification_index', 'set_magnification_index', 'get_indicated_camera_length', 'get_indicated_magnification', 'get_defocus', 'set_defocus', 'get_objective_excitation', 'get_intensity', 'set_intensity', 'get_objective_stigmator', 'set_objective_stigmator', 'get_condenser_stigmator', 'set_condenser_stigmator', 'get_diffraction_shift', 'set_diffraction_shift', 'get_screen_current', 'get_screen_position', 'set_screen_position', 'get_illumination_mode', 'set_illumination_mode', 'get_condenser_mode', 'set_condenser_mode', 'get_stem_magnification', 'set_stem_magnification', 'get_stem_rotation', 'set_stem_rotation', 'get_illuminated_area', 'set_illuminated_area', 'get_probe_defocus', 'set_probe_defocus', 'get_convergence_angle', 'set_convergence_angle', 'get_spot_size_index', 'set_spot_size_index', 'get_dark_field_mode', 'set_dark_field_mode', 'get_beam_blanked', 'set_beam_blanked', 'is_stem_available', 'get_instrument_mode', 'set_instrument_mode', 'get_state', 'get_optics_state'], 'action_targets': {}, 'metadata': {'repo': 'niermann/temscript', 'repo_url': 'https://github.com/niermann/temscript', 'brand': 'Thermo Fisher', 'model': 'Talos F200C', 'device_type_cn': '透射电子显微镜', 'device_type_en': 'Transmission Electron Microscope', 'source_framework': 'temscript', 'tag_id': '4456', 'tag_name': '透射电子显微镜', 'tag_name_en': 'Transmission Electron Microscope', 'candidate_score': 665, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_family(self, **kwargs):
        return self.call('get_family', kwargs=kwargs)

    def get_microscope_id(self, **kwargs):
        return self.call('get_microscope_id', kwargs=kwargs)

    def get_version(self, **kwargs):
        return self.call('get_version', kwargs=kwargs)

    def get_voltage(self, **kwargs):
        return self.call('get_voltage', kwargs=kwargs)

    def get_vacuum(self, **kwargs):
        return self.call('get_vacuum', kwargs=kwargs)

    def get_column_valves_open(self, **kwargs):
        return self.call('get_column_valves_open', kwargs=kwargs)

    def set_column_valves_open(self, **kwargs):
        return self.call('set_column_valves_open', kwargs=kwargs)

    def get_stage_holder(self, **kwargs):
        return self.call('get_stage_holder', kwargs=kwargs)

    def get_stage_status(self, **kwargs):
        return self.call('get_stage_status', kwargs=kwargs)

    def get_stage_limits(self, **kwargs):
        return self.call('get_stage_limits', kwargs=kwargs)

    def get_stage_position(self, **kwargs):
        return self.call('get_stage_position', kwargs=kwargs)

    def set_stage_position(self, **kwargs):
        return self.call('set_stage_position', kwargs=kwargs)

    def get_cameras(self, **kwargs):
        return self.call('get_cameras', kwargs=kwargs)

    def get_stem_detectors(self, **kwargs):
        return self.call('get_stem_detectors', kwargs=kwargs)

    def get_detectors(self, **kwargs):
        return self.call('get_detectors', kwargs=kwargs)

    def get_camera_param(self, **kwargs):
        return self.call('get_camera_param', kwargs=kwargs)

    def set_camera_param(self, **kwargs):
        return self.call('set_camera_param', kwargs=kwargs)

    def get_stem_detector_param(self, **kwargs):
        return self.call('get_stem_detector_param', kwargs=kwargs)

    def set_stem_detector_param(self, **kwargs):
        return self.call('set_stem_detector_param', kwargs=kwargs)

    def get_stem_acquisition_param(self, **kwargs):
        return self.call('get_stem_acquisition_param', kwargs=kwargs)

    def set_stem_acquisition_param(self, **kwargs):
        return self.call('set_stem_acquisition_param', kwargs=kwargs)

    def get_detector_param(self, **kwargs):
        return self.call('get_detector_param', kwargs=kwargs)

    def set_detector_param(self, **kwargs):
        return self.call('set_detector_param', kwargs=kwargs)

    def acquire(self, **kwargs):
        return self.call('acquire', kwargs=kwargs)

    def get_image_shift(self, **kwargs):
        return self.call('get_image_shift', kwargs=kwargs)

    def set_image_shift(self, **kwargs):
        return self.call('set_image_shift', kwargs=kwargs)

    def get_beam_shift(self, **kwargs):
        return self.call('get_beam_shift', kwargs=kwargs)

    def set_beam_shift(self, **kwargs):
        return self.call('set_beam_shift', kwargs=kwargs)

    def get_beam_tilt(self, **kwargs):
        return self.call('get_beam_tilt', kwargs=kwargs)

    def set_beam_tilt(self, **kwargs):
        return self.call('set_beam_tilt', kwargs=kwargs)

    def normalize(self, **kwargs):
        return self.call('normalize', kwargs=kwargs)

    def get_projection_sub_mode(self, **kwargs):
        return self.call('get_projection_sub_mode', kwargs=kwargs)

    def get_projection_mode(self, **kwargs):
        return self.call('get_projection_mode', kwargs=kwargs)

    def set_projection_mode(self, **kwargs):
        return self.call('set_projection_mode', kwargs=kwargs)

    def get_projection_mode_string(self, **kwargs):
        return self.call('get_projection_mode_string', kwargs=kwargs)

    def get_magnification_index(self, **kwargs):
        return self.call('get_magnification_index', kwargs=kwargs)

    def set_magnification_index(self, **kwargs):
        return self.call('set_magnification_index', kwargs=kwargs)

    def get_indicated_camera_length(self, **kwargs):
        return self.call('get_indicated_camera_length', kwargs=kwargs)

    def get_indicated_magnification(self, **kwargs):
        return self.call('get_indicated_magnification', kwargs=kwargs)

    def get_defocus(self, **kwargs):
        return self.call('get_defocus', kwargs=kwargs)

    def set_defocus(self, **kwargs):
        return self.call('set_defocus', kwargs=kwargs)

    def get_objective_excitation(self, **kwargs):
        return self.call('get_objective_excitation', kwargs=kwargs)

    def get_intensity(self, **kwargs):
        return self.call('get_intensity', kwargs=kwargs)

    def set_intensity(self, **kwargs):
        return self.call('set_intensity', kwargs=kwargs)

    def get_objective_stigmator(self, **kwargs):
        return self.call('get_objective_stigmator', kwargs=kwargs)

    def set_objective_stigmator(self, **kwargs):
        return self.call('set_objective_stigmator', kwargs=kwargs)

    def get_condenser_stigmator(self, **kwargs):
        return self.call('get_condenser_stigmator', kwargs=kwargs)

    def set_condenser_stigmator(self, **kwargs):
        return self.call('set_condenser_stigmator', kwargs=kwargs)

    def get_diffraction_shift(self, **kwargs):
        return self.call('get_diffraction_shift', kwargs=kwargs)

    def set_diffraction_shift(self, **kwargs):
        return self.call('set_diffraction_shift', kwargs=kwargs)

    def get_screen_current(self, **kwargs):
        return self.call('get_screen_current', kwargs=kwargs)

    def get_screen_position(self, **kwargs):
        return self.call('get_screen_position', kwargs=kwargs)

    def set_screen_position(self, **kwargs):
        return self.call('set_screen_position', kwargs=kwargs)

    def get_illumination_mode(self, **kwargs):
        return self.call('get_illumination_mode', kwargs=kwargs)

    def set_illumination_mode(self, **kwargs):
        return self.call('set_illumination_mode', kwargs=kwargs)

    def get_condenser_mode(self, **kwargs):
        return self.call('get_condenser_mode', kwargs=kwargs)

    def set_condenser_mode(self, **kwargs):
        return self.call('set_condenser_mode', kwargs=kwargs)

    def get_stem_magnification(self, **kwargs):
        return self.call('get_stem_magnification', kwargs=kwargs)

    def set_stem_magnification(self, **kwargs):
        return self.call('set_stem_magnification', kwargs=kwargs)

    def get_stem_rotation(self, **kwargs):
        return self.call('get_stem_rotation', kwargs=kwargs)

    def set_stem_rotation(self, **kwargs):
        return self.call('set_stem_rotation', kwargs=kwargs)

    def get_illuminated_area(self, **kwargs):
        return self.call('get_illuminated_area', kwargs=kwargs)

    def set_illuminated_area(self, **kwargs):
        return self.call('set_illuminated_area', kwargs=kwargs)

    def get_probe_defocus(self, **kwargs):
        return self.call('get_probe_defocus', kwargs=kwargs)

    def set_probe_defocus(self, **kwargs):
        return self.call('set_probe_defocus', kwargs=kwargs)

    def get_convergence_angle(self, **kwargs):
        return self.call('get_convergence_angle', kwargs=kwargs)

    def set_convergence_angle(self, **kwargs):
        return self.call('set_convergence_angle', kwargs=kwargs)

    def get_spot_size_index(self, **kwargs):
        return self.call('get_spot_size_index', kwargs=kwargs)

    def set_spot_size_index(self, **kwargs):
        return self.call('set_spot_size_index', kwargs=kwargs)

    def get_dark_field_mode(self, **kwargs):
        return self.call('get_dark_field_mode', kwargs=kwargs)

    def set_dark_field_mode(self, **kwargs):
        return self.call('set_dark_field_mode', kwargs=kwargs)

    def get_beam_blanked(self, **kwargs):
        return self.call('get_beam_blanked', kwargs=kwargs)

    def set_beam_blanked(self, **kwargs):
        return self.call('set_beam_blanked', kwargs=kwargs)

    def is_stem_available(self, **kwargs):
        return self.call('is_stem_available', kwargs=kwargs)

    def get_instrument_mode(self, **kwargs):
        return self.call('get_instrument_mode', kwargs=kwargs)

    def set_instrument_mode(self, **kwargs):
        return self.call('set_instrument_mode', kwargs=kwargs)

    def get_state(self, **kwargs):
        return self.call('get_state', kwargs=kwargs)

    def get_optics_state(self, **kwargs):
        return self.call('get_optics_state', kwargs=kwargs)

