from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentEurotherm24082416(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/NMGRL__pychron', 'source_file': 'pychron/database/adapters/isotope_adapter.py', 'class_name': 'IsotopeAdapter', 'import_roots': [], 'candidate_methods': ['get_mass_spectrometer_names', 'get_extraction_device_names', 'get_flux_value', 'get_level_identifiers', 'get_irradiation_names', 'get_analysis_info', 'set_analysis_sensitivity', 'save_flux', 'interpreted_age_factory', 'add_data_reduction_tag', 'add_data_reduction_tag_set', 'add_proc_action', 'add_mftable', 'add_analysis_group', 'add_analysis_group_set', 'add_interpreted_age_group_history', 'add_interpreted_age_group_set', 'add_history', 'add_mass_calibration_history', 'add_mass_calibration_scan', 'add_arar_history', 'add_arar', 'add_load', 'add_load_position', 'add_tag', 'add_import', 'add_snapshot', 'add_image', 'add_sample_image', 'add_monitor', 'add_analysis_position', 'add_note', 'add_interpreted_age_history', 'add_interpreted_age', 'add_interpreted_age_set', 'add_blanks_history', 'add_blanks', 'add_blanks_set', 'add_blank_set_value_table', 'add_backgrounds_history', 'add_backgrounds', 'add_backgrounds_set', 'add_detector', 'add_detector_parameter_history', 'add_detector_parameter', 'add_detector_intercalibration_history', 'add_detector_intercalibration', 'add_detector_intercalibration_set', 'add_experiment', 'add_extraction', 'add_extraction_device', 'add_figure_labnumber', 'add_figure', 'add_figure_preference', 'add_figure_analysis', 'add_fit_history', 'add_fit', 'add_flux', 'add_flux_history', 'add_flux_monitor', 'add_irradiation', 'add_load_holder', 'add_irradiation_holder', 'add_irradiation_production', 'add_irradiation_position', 'add_irradiation_chronology', 'add_irradiation_level', 'add_isotope', 'add_isotope_result', 'add_measurement', 'add_mass_spectrometer', 'add_material', 'add_molecular_weight', 'add_project', 'add_peak_center', 'add_user', 'add_sample', 'add_script', 'add_selected_histories', 'add_signal', 'add_spectrometer_parameters', 'add_deflection', 'add_labnumber', 'add_analysis', 'add_analysis_type', 'add_sensitivity', 'add_gain_history', 'add_gain', 'get_sample_image_count', 'get_sample_image', 'get_adjacent_analysis', 'make_gains_hash', 'get_gain_histories', 'get_gain_history', 'get_blanks', 'get_session_blank_histories', 'get_blanks_history', 'get_mftables', 'get_mftable', 'get_interpreted_age_group_history', 'get_interpreted_age_groups', 'get_analyzed_positions', 'get_analysis_group', 'get_analysis_groups', 'get_latest_interpreted_age_history', 'get_interpreted_age_histories', 'get_project_irradiation_labnumbers', 'get_project_labnumbers', 'get_project_analysis_count', 'get_project_figures', 'get_project_date_bins', 'get_project_date_range', 'get_labnumber_figures', 'get_preceding', 'get_analysis_mass_spectrometers', 'get_analysis_date_ranges', 'get_min_max_analysis_timestamp', 'get_labnumber_mass_spectrometers', 'get_labnumber_analyses', 'get_sample_analyses', 'get_analyses_date_range', 'get_loadtable', 'get_arar', 'get_last_labnumbers', 'get_last_labnumber', 'get_greatest_identifier', 'get_greatest_aliquot', 'get_greatest_step', 'get_last_analysis', 'get_unique_analysis', 'get_analyses_uuid', 'get_analysis_isotopes', 'get_analysis_isotope', 'get_analysis_runid', 'get_analysis_uuid', 'get_analysis_record', 'get_image', 'get_analysis', 'get_analysis_type', 'get_blanks_set', 'retrieve_blank', 'get_blank', 'get_background', 'get_backgrounds_history', 'get_detector', 'get_detector_intercalibration', 'get_detector_intercalibration_history', 'get_detector_intercalibrations_history', 'get_experiment', 'get_extraction', 'get_extraction_device', 'get_figure', 'get_irradiation_chronology', 'get_load_holder', 'get_irradiation_holder', 'get_irradiation_production', 'get_irradiation', 'get_irradiation_level_byid', 'get_irradiation_level', 'get_irradiation_position', 'get_irradiation_labnumbers', 'get_labnumber', 'get_mass_spectrometer', 'get_material', 'get_molecular_weight', 'get_molecular_weight_name', 'get_user', 'get_project', 'get_script', 'get_sample', 'get_flux_history', 'get_flux_monitor', 'get_tag', 'get_sensitivity', 'get_interpreted_age_history', 'get_data_reduction_tags', 'get_irradiation_holders', 'get_analyses', 'get_figures', 'get_aliquots', 'get_detectors', 'get_steps', 'get_materials', 'get_material_names', 'get_years_active', 'get_recent_labnumbers', 'get_recent_samples', 'get_samples', 'get_users', 'get_usernames', 'get_labnumbers_startswith', 'get_labnumbers', 'get_flux_monitors', 'get_labnumbers_join_analysis', 'get_irradiations_join_analysis', 'get_irradiations', 'get_irradiation_productions', 'get_projects', 'get_sensitivities', 'get_mass_spectrometers', 'get_extraction_devices', 'get_analysis_types', 'get_spectrometer_parameters', 'get_load_holders', 'get_latest_load', 'get_loads', 'get_molecular_weights', 'get_molecular_weight_names', 'get_tags', 'delete_tag', 'delete_irradiation_position', 'delete_analysis_group', 'delete_user', 'delete_project', 'delete_material', 'delete_sample', 'delete_labnumber', 'create_all', 'session_ctx', 'create_session', 'close_session', 'enabled', 'save_username', 'reset_connection', 'connect', 'rollback', 'flush', 'expire', 'expire_all', 'commit', 'delete', 'post_commit', 'add_item', 'get_migrate_version', 'get_versions', 'public_datasource_url', 'public_url', 'init_logger', 'report_logger_stats', 'unique_warning', 'unique_info', 'unique_debug', 'warning', 'info', 'debug_exception', 'warning_exception', 'critical', 'debug', 'log', 'warning_dialog', 'confirmation_dialog', 'information_dialog', 'message', 'open_file_dialog', 'save_file_dialog', 'open_directory_dialog', 'save_directory_dialog'], 'action_targets': {}, 'metadata': {'repo': 'NMGRL/pychron', 'repo_url': 'https://github.com/NMGRL/pychron', 'brand': 'Eurotherm', 'model': '2408/2416', 'device_type_cn': '箱式电阻炉', 'device_type_en': 'Box Resistance Furnace', 'source_framework': 'pychron', 'tag_id': '4438', 'tag_name': '箱式电阻炉', 'tag_name_en': 'Box Resistance Furnace', 'candidate_score': 1749, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_mass_spectrometer_names(self, **kwargs):
        return self.call('get_mass_spectrometer_names', kwargs=kwargs)

    def get_extraction_device_names(self, **kwargs):
        return self.call('get_extraction_device_names', kwargs=kwargs)

    def get_flux_value(self, **kwargs):
        return self.call('get_flux_value', kwargs=kwargs)

    def get_level_identifiers(self, **kwargs):
        return self.call('get_level_identifiers', kwargs=kwargs)

    def get_irradiation_names(self, **kwargs):
        return self.call('get_irradiation_names', kwargs=kwargs)

    def get_analysis_info(self, **kwargs):
        return self.call('get_analysis_info', kwargs=kwargs)

    def set_analysis_sensitivity(self, **kwargs):
        return self.call('set_analysis_sensitivity', kwargs=kwargs)

    def save_flux(self, **kwargs):
        return self.call('save_flux', kwargs=kwargs)

    def interpreted_age_factory(self, **kwargs):
        return self.call('interpreted_age_factory', kwargs=kwargs)

    def add_data_reduction_tag(self, **kwargs):
        return self.call('add_data_reduction_tag', kwargs=kwargs)

    def add_data_reduction_tag_set(self, **kwargs):
        return self.call('add_data_reduction_tag_set', kwargs=kwargs)

    def add_proc_action(self, **kwargs):
        return self.call('add_proc_action', kwargs=kwargs)

    def add_mftable(self, **kwargs):
        return self.call('add_mftable', kwargs=kwargs)

    def add_analysis_group(self, **kwargs):
        return self.call('add_analysis_group', kwargs=kwargs)

    def add_analysis_group_set(self, **kwargs):
        return self.call('add_analysis_group_set', kwargs=kwargs)

    def add_interpreted_age_group_history(self, **kwargs):
        return self.call('add_interpreted_age_group_history', kwargs=kwargs)

    def add_interpreted_age_group_set(self, **kwargs):
        return self.call('add_interpreted_age_group_set', kwargs=kwargs)

    def add_history(self, **kwargs):
        return self.call('add_history', kwargs=kwargs)

    def add_mass_calibration_history(self, **kwargs):
        return self.call('add_mass_calibration_history', kwargs=kwargs)

    def add_mass_calibration_scan(self, **kwargs):
        return self.call('add_mass_calibration_scan', kwargs=kwargs)

    def add_arar_history(self, **kwargs):
        return self.call('add_arar_history', kwargs=kwargs)

    def add_arar(self, **kwargs):
        return self.call('add_arar', kwargs=kwargs)

    def add_load(self, **kwargs):
        return self.call('add_load', kwargs=kwargs)

    def add_load_position(self, **kwargs):
        return self.call('add_load_position', kwargs=kwargs)

    def add_tag(self, **kwargs):
        return self.call('add_tag', kwargs=kwargs)

    def add_import(self, **kwargs):
        return self.call('add_import', kwargs=kwargs)

    def add_snapshot(self, **kwargs):
        return self.call('add_snapshot', kwargs=kwargs)

    def add_image(self, **kwargs):
        return self.call('add_image', kwargs=kwargs)

    def add_sample_image(self, **kwargs):
        return self.call('add_sample_image', kwargs=kwargs)

    def add_monitor(self, **kwargs):
        return self.call('add_monitor', kwargs=kwargs)

    def add_analysis_position(self, **kwargs):
        return self.call('add_analysis_position', kwargs=kwargs)

    def add_note(self, **kwargs):
        return self.call('add_note', kwargs=kwargs)

    def add_interpreted_age_history(self, **kwargs):
        return self.call('add_interpreted_age_history', kwargs=kwargs)

    def add_interpreted_age(self, **kwargs):
        return self.call('add_interpreted_age', kwargs=kwargs)

    def add_interpreted_age_set(self, **kwargs):
        return self.call('add_interpreted_age_set', kwargs=kwargs)

    def add_blanks_history(self, **kwargs):
        return self.call('add_blanks_history', kwargs=kwargs)

    def add_blanks(self, **kwargs):
        return self.call('add_blanks', kwargs=kwargs)

    def add_blanks_set(self, **kwargs):
        return self.call('add_blanks_set', kwargs=kwargs)

    def add_blank_set_value_table(self, **kwargs):
        return self.call('add_blank_set_value_table', kwargs=kwargs)

    def add_backgrounds_history(self, **kwargs):
        return self.call('add_backgrounds_history', kwargs=kwargs)

    def add_backgrounds(self, **kwargs):
        return self.call('add_backgrounds', kwargs=kwargs)

    def add_backgrounds_set(self, **kwargs):
        return self.call('add_backgrounds_set', kwargs=kwargs)

    def add_detector(self, **kwargs):
        return self.call('add_detector', kwargs=kwargs)

    def add_detector_parameter_history(self, **kwargs):
        return self.call('add_detector_parameter_history', kwargs=kwargs)

    def add_detector_parameter(self, **kwargs):
        return self.call('add_detector_parameter', kwargs=kwargs)

    def add_detector_intercalibration_history(self, **kwargs):
        return self.call('add_detector_intercalibration_history', kwargs=kwargs)

    def add_detector_intercalibration(self, **kwargs):
        return self.call('add_detector_intercalibration', kwargs=kwargs)

    def add_detector_intercalibration_set(self, **kwargs):
        return self.call('add_detector_intercalibration_set', kwargs=kwargs)

    def add_experiment(self, **kwargs):
        return self.call('add_experiment', kwargs=kwargs)

    def add_extraction(self, **kwargs):
        return self.call('add_extraction', kwargs=kwargs)

    def add_extraction_device(self, **kwargs):
        return self.call('add_extraction_device', kwargs=kwargs)

    def add_figure_labnumber(self, **kwargs):
        return self.call('add_figure_labnumber', kwargs=kwargs)

    def add_figure(self, **kwargs):
        return self.call('add_figure', kwargs=kwargs)

    def add_figure_preference(self, **kwargs):
        return self.call('add_figure_preference', kwargs=kwargs)

    def add_figure_analysis(self, **kwargs):
        return self.call('add_figure_analysis', kwargs=kwargs)

    def add_fit_history(self, **kwargs):
        return self.call('add_fit_history', kwargs=kwargs)

    def add_fit(self, **kwargs):
        return self.call('add_fit', kwargs=kwargs)

    def add_flux(self, **kwargs):
        return self.call('add_flux', kwargs=kwargs)

    def add_flux_history(self, **kwargs):
        return self.call('add_flux_history', kwargs=kwargs)

    def add_flux_monitor(self, **kwargs):
        return self.call('add_flux_monitor', kwargs=kwargs)

    def add_irradiation(self, **kwargs):
        return self.call('add_irradiation', kwargs=kwargs)

    def add_load_holder(self, **kwargs):
        return self.call('add_load_holder', kwargs=kwargs)

    def add_irradiation_holder(self, **kwargs):
        return self.call('add_irradiation_holder', kwargs=kwargs)

    def add_irradiation_production(self, **kwargs):
        return self.call('add_irradiation_production', kwargs=kwargs)

    def add_irradiation_position(self, **kwargs):
        return self.call('add_irradiation_position', kwargs=kwargs)

    def add_irradiation_chronology(self, **kwargs):
        return self.call('add_irradiation_chronology', kwargs=kwargs)

    def add_irradiation_level(self, **kwargs):
        return self.call('add_irradiation_level', kwargs=kwargs)

    def add_isotope(self, **kwargs):
        return self.call('add_isotope', kwargs=kwargs)

    def add_isotope_result(self, **kwargs):
        return self.call('add_isotope_result', kwargs=kwargs)

    def add_measurement(self, **kwargs):
        return self.call('add_measurement', kwargs=kwargs)

    def add_mass_spectrometer(self, **kwargs):
        return self.call('add_mass_spectrometer', kwargs=kwargs)

    def add_material(self, **kwargs):
        return self.call('add_material', kwargs=kwargs)

    def add_molecular_weight(self, **kwargs):
        return self.call('add_molecular_weight', kwargs=kwargs)

    def add_project(self, **kwargs):
        return self.call('add_project', kwargs=kwargs)

    def add_peak_center(self, **kwargs):
        return self.call('add_peak_center', kwargs=kwargs)

    def add_user(self, **kwargs):
        return self.call('add_user', kwargs=kwargs)

    def add_sample(self, **kwargs):
        return self.call('add_sample', kwargs=kwargs)

    def add_script(self, **kwargs):
        return self.call('add_script', kwargs=kwargs)

    def add_selected_histories(self, **kwargs):
        return self.call('add_selected_histories', kwargs=kwargs)

    def add_signal(self, **kwargs):
        return self.call('add_signal', kwargs=kwargs)

    def add_spectrometer_parameters(self, **kwargs):
        return self.call('add_spectrometer_parameters', kwargs=kwargs)

    def add_deflection(self, **kwargs):
        return self.call('add_deflection', kwargs=kwargs)

    def add_labnumber(self, **kwargs):
        return self.call('add_labnumber', kwargs=kwargs)

    def add_analysis(self, **kwargs):
        return self.call('add_analysis', kwargs=kwargs)

    def add_analysis_type(self, **kwargs):
        return self.call('add_analysis_type', kwargs=kwargs)

    def add_sensitivity(self, **kwargs):
        return self.call('add_sensitivity', kwargs=kwargs)

    def add_gain_history(self, **kwargs):
        return self.call('add_gain_history', kwargs=kwargs)

    def add_gain(self, **kwargs):
        return self.call('add_gain', kwargs=kwargs)

    def get_sample_image_count(self, **kwargs):
        return self.call('get_sample_image_count', kwargs=kwargs)

    def get_sample_image(self, **kwargs):
        return self.call('get_sample_image', kwargs=kwargs)

    def get_adjacent_analysis(self, **kwargs):
        return self.call('get_adjacent_analysis', kwargs=kwargs)

    def make_gains_hash(self, **kwargs):
        return self.call('make_gains_hash', kwargs=kwargs)

    def get_gain_histories(self, **kwargs):
        return self.call('get_gain_histories', kwargs=kwargs)

    def get_gain_history(self, **kwargs):
        return self.call('get_gain_history', kwargs=kwargs)

    def get_blanks(self, **kwargs):
        return self.call('get_blanks', kwargs=kwargs)

    def get_session_blank_histories(self, **kwargs):
        return self.call('get_session_blank_histories', kwargs=kwargs)

    def get_blanks_history(self, **kwargs):
        return self.call('get_blanks_history', kwargs=kwargs)

    def get_mftables(self, **kwargs):
        return self.call('get_mftables', kwargs=kwargs)

    def get_mftable(self, **kwargs):
        return self.call('get_mftable', kwargs=kwargs)

    def get_interpreted_age_group_history(self, **kwargs):
        return self.call('get_interpreted_age_group_history', kwargs=kwargs)

    def get_interpreted_age_groups(self, **kwargs):
        return self.call('get_interpreted_age_groups', kwargs=kwargs)

    def get_analyzed_positions(self, **kwargs):
        return self.call('get_analyzed_positions', kwargs=kwargs)

    def get_analysis_group(self, **kwargs):
        return self.call('get_analysis_group', kwargs=kwargs)

    def get_analysis_groups(self, **kwargs):
        return self.call('get_analysis_groups', kwargs=kwargs)

    def get_latest_interpreted_age_history(self, **kwargs):
        return self.call('get_latest_interpreted_age_history', kwargs=kwargs)

    def get_interpreted_age_histories(self, **kwargs):
        return self.call('get_interpreted_age_histories', kwargs=kwargs)

    def get_project_irradiation_labnumbers(self, **kwargs):
        return self.call('get_project_irradiation_labnumbers', kwargs=kwargs)

    def get_project_labnumbers(self, **kwargs):
        return self.call('get_project_labnumbers', kwargs=kwargs)

    def get_project_analysis_count(self, **kwargs):
        return self.call('get_project_analysis_count', kwargs=kwargs)

    def get_project_figures(self, **kwargs):
        return self.call('get_project_figures', kwargs=kwargs)

    def get_project_date_bins(self, **kwargs):
        return self.call('get_project_date_bins', kwargs=kwargs)

    def get_project_date_range(self, **kwargs):
        return self.call('get_project_date_range', kwargs=kwargs)

    def get_labnumber_figures(self, **kwargs):
        return self.call('get_labnumber_figures', kwargs=kwargs)

    def get_preceding(self, **kwargs):
        return self.call('get_preceding', kwargs=kwargs)

    def get_analysis_mass_spectrometers(self, **kwargs):
        return self.call('get_analysis_mass_spectrometers', kwargs=kwargs)

    def get_analysis_date_ranges(self, **kwargs):
        return self.call('get_analysis_date_ranges', kwargs=kwargs)

    def get_min_max_analysis_timestamp(self, **kwargs):
        return self.call('get_min_max_analysis_timestamp', kwargs=kwargs)

    def get_labnumber_mass_spectrometers(self, **kwargs):
        return self.call('get_labnumber_mass_spectrometers', kwargs=kwargs)

    def get_labnumber_analyses(self, **kwargs):
        return self.call('get_labnumber_analyses', kwargs=kwargs)

    def get_sample_analyses(self, **kwargs):
        return self.call('get_sample_analyses', kwargs=kwargs)

    def get_analyses_date_range(self, **kwargs):
        return self.call('get_analyses_date_range', kwargs=kwargs)

    def get_loadtable(self, **kwargs):
        return self.call('get_loadtable', kwargs=kwargs)

    def get_arar(self, **kwargs):
        return self.call('get_arar', kwargs=kwargs)

    def get_last_labnumbers(self, **kwargs):
        return self.call('get_last_labnumbers', kwargs=kwargs)

    def get_last_labnumber(self, **kwargs):
        return self.call('get_last_labnumber', kwargs=kwargs)

    def get_greatest_identifier(self, **kwargs):
        return self.call('get_greatest_identifier', kwargs=kwargs)

    def get_greatest_aliquot(self, **kwargs):
        return self.call('get_greatest_aliquot', kwargs=kwargs)

    def get_greatest_step(self, **kwargs):
        return self.call('get_greatest_step', kwargs=kwargs)

    def get_last_analysis(self, **kwargs):
        return self.call('get_last_analysis', kwargs=kwargs)

    def get_unique_analysis(self, **kwargs):
        return self.call('get_unique_analysis', kwargs=kwargs)

    def get_analyses_uuid(self, **kwargs):
        return self.call('get_analyses_uuid', kwargs=kwargs)

    def get_analysis_isotopes(self, **kwargs):
        return self.call('get_analysis_isotopes', kwargs=kwargs)

    def get_analysis_isotope(self, **kwargs):
        return self.call('get_analysis_isotope', kwargs=kwargs)

    def get_analysis_runid(self, **kwargs):
        return self.call('get_analysis_runid', kwargs=kwargs)

    def get_analysis_uuid(self, **kwargs):
        return self.call('get_analysis_uuid', kwargs=kwargs)

    def get_analysis_record(self, **kwargs):
        return self.call('get_analysis_record', kwargs=kwargs)

    def get_image(self, **kwargs):
        return self.call('get_image', kwargs=kwargs)

    def get_analysis(self, **kwargs):
        return self.call('get_analysis', kwargs=kwargs)

    def get_analysis_type(self, **kwargs):
        return self.call('get_analysis_type', kwargs=kwargs)

    def get_blanks_set(self, **kwargs):
        return self.call('get_blanks_set', kwargs=kwargs)

    def retrieve_blank(self, **kwargs):
        return self.call('retrieve_blank', kwargs=kwargs)

    def get_blank(self, **kwargs):
        return self.call('get_blank', kwargs=kwargs)

    def get_background(self, **kwargs):
        return self.call('get_background', kwargs=kwargs)

    def get_backgrounds_history(self, **kwargs):
        return self.call('get_backgrounds_history', kwargs=kwargs)

    def get_detector(self, **kwargs):
        return self.call('get_detector', kwargs=kwargs)

    def get_detector_intercalibration(self, **kwargs):
        return self.call('get_detector_intercalibration', kwargs=kwargs)

    def get_detector_intercalibration_history(self, **kwargs):
        return self.call('get_detector_intercalibration_history', kwargs=kwargs)

    def get_detector_intercalibrations_history(self, **kwargs):
        return self.call('get_detector_intercalibrations_history', kwargs=kwargs)

    def get_experiment(self, **kwargs):
        return self.call('get_experiment', kwargs=kwargs)

    def get_extraction(self, **kwargs):
        return self.call('get_extraction', kwargs=kwargs)

    def get_extraction_device(self, **kwargs):
        return self.call('get_extraction_device', kwargs=kwargs)

    def get_figure(self, **kwargs):
        return self.call('get_figure', kwargs=kwargs)

    def get_irradiation_chronology(self, **kwargs):
        return self.call('get_irradiation_chronology', kwargs=kwargs)

    def get_load_holder(self, **kwargs):
        return self.call('get_load_holder', kwargs=kwargs)

    def get_irradiation_holder(self, **kwargs):
        return self.call('get_irradiation_holder', kwargs=kwargs)

    def get_irradiation_production(self, **kwargs):
        return self.call('get_irradiation_production', kwargs=kwargs)

    def get_irradiation(self, **kwargs):
        return self.call('get_irradiation', kwargs=kwargs)

    def get_irradiation_level_byid(self, **kwargs):
        return self.call('get_irradiation_level_byid', kwargs=kwargs)

    def get_irradiation_level(self, **kwargs):
        return self.call('get_irradiation_level', kwargs=kwargs)

    def get_irradiation_position(self, **kwargs):
        return self.call('get_irradiation_position', kwargs=kwargs)

    def get_irradiation_labnumbers(self, **kwargs):
        return self.call('get_irradiation_labnumbers', kwargs=kwargs)

    def get_labnumber(self, **kwargs):
        return self.call('get_labnumber', kwargs=kwargs)

    def get_mass_spectrometer(self, **kwargs):
        return self.call('get_mass_spectrometer', kwargs=kwargs)

    def get_material(self, **kwargs):
        return self.call('get_material', kwargs=kwargs)

    def get_molecular_weight(self, **kwargs):
        return self.call('get_molecular_weight', kwargs=kwargs)

    def get_molecular_weight_name(self, **kwargs):
        return self.call('get_molecular_weight_name', kwargs=kwargs)

    def get_user(self, **kwargs):
        return self.call('get_user', kwargs=kwargs)

    def get_project(self, **kwargs):
        return self.call('get_project', kwargs=kwargs)

    def get_script(self, **kwargs):
        return self.call('get_script', kwargs=kwargs)

    def get_sample(self, **kwargs):
        return self.call('get_sample', kwargs=kwargs)

    def get_flux_history(self, **kwargs):
        return self.call('get_flux_history', kwargs=kwargs)

    def get_flux_monitor(self, **kwargs):
        return self.call('get_flux_monitor', kwargs=kwargs)

    def get_tag(self, **kwargs):
        return self.call('get_tag', kwargs=kwargs)

    def get_sensitivity(self, **kwargs):
        return self.call('get_sensitivity', kwargs=kwargs)

    def get_interpreted_age_history(self, **kwargs):
        return self.call('get_interpreted_age_history', kwargs=kwargs)

    def get_data_reduction_tags(self, **kwargs):
        return self.call('get_data_reduction_tags', kwargs=kwargs)

    def get_irradiation_holders(self, **kwargs):
        return self.call('get_irradiation_holders', kwargs=kwargs)

    def get_analyses(self, **kwargs):
        return self.call('get_analyses', kwargs=kwargs)

    def get_figures(self, **kwargs):
        return self.call('get_figures', kwargs=kwargs)

    def get_aliquots(self, **kwargs):
        return self.call('get_aliquots', kwargs=kwargs)

    def get_detectors(self, **kwargs):
        return self.call('get_detectors', kwargs=kwargs)

    def get_steps(self, **kwargs):
        return self.call('get_steps', kwargs=kwargs)

    def get_materials(self, **kwargs):
        return self.call('get_materials', kwargs=kwargs)

    def get_material_names(self, **kwargs):
        return self.call('get_material_names', kwargs=kwargs)

    def get_years_active(self, **kwargs):
        return self.call('get_years_active', kwargs=kwargs)

    def get_recent_labnumbers(self, **kwargs):
        return self.call('get_recent_labnumbers', kwargs=kwargs)

    def get_recent_samples(self, **kwargs):
        return self.call('get_recent_samples', kwargs=kwargs)

    def get_samples(self, **kwargs):
        return self.call('get_samples', kwargs=kwargs)

    def get_users(self, **kwargs):
        return self.call('get_users', kwargs=kwargs)

    def get_usernames(self, **kwargs):
        return self.call('get_usernames', kwargs=kwargs)

    def get_labnumbers_startswith(self, **kwargs):
        return self.call('get_labnumbers_startswith', kwargs=kwargs)

    def get_labnumbers(self, **kwargs):
        return self.call('get_labnumbers', kwargs=kwargs)

    def get_flux_monitors(self, **kwargs):
        return self.call('get_flux_monitors', kwargs=kwargs)

    def get_labnumbers_join_analysis(self, **kwargs):
        return self.call('get_labnumbers_join_analysis', kwargs=kwargs)

    def get_irradiations_join_analysis(self, **kwargs):
        return self.call('get_irradiations_join_analysis', kwargs=kwargs)

    def get_irradiations(self, **kwargs):
        return self.call('get_irradiations', kwargs=kwargs)

    def get_irradiation_productions(self, **kwargs):
        return self.call('get_irradiation_productions', kwargs=kwargs)

    def get_projects(self, **kwargs):
        return self.call('get_projects', kwargs=kwargs)

    def get_sensitivities(self, **kwargs):
        return self.call('get_sensitivities', kwargs=kwargs)

    def get_mass_spectrometers(self, **kwargs):
        return self.call('get_mass_spectrometers', kwargs=kwargs)

    def get_extraction_devices(self, **kwargs):
        return self.call('get_extraction_devices', kwargs=kwargs)

    def get_analysis_types(self, **kwargs):
        return self.call('get_analysis_types', kwargs=kwargs)

    def get_spectrometer_parameters(self, **kwargs):
        return self.call('get_spectrometer_parameters', kwargs=kwargs)

    def get_load_holders(self, **kwargs):
        return self.call('get_load_holders', kwargs=kwargs)

    def get_latest_load(self, **kwargs):
        return self.call('get_latest_load', kwargs=kwargs)

    def get_loads(self, **kwargs):
        return self.call('get_loads', kwargs=kwargs)

    def get_molecular_weights(self, **kwargs):
        return self.call('get_molecular_weights', kwargs=kwargs)

    def get_molecular_weight_names(self, **kwargs):
        return self.call('get_molecular_weight_names', kwargs=kwargs)

    def get_tags(self, **kwargs):
        return self.call('get_tags', kwargs=kwargs)

    def delete_tag(self, **kwargs):
        return self.call('delete_tag', kwargs=kwargs)

    def delete_irradiation_position(self, **kwargs):
        return self.call('delete_irradiation_position', kwargs=kwargs)

    def delete_analysis_group(self, **kwargs):
        return self.call('delete_analysis_group', kwargs=kwargs)

    def delete_user(self, **kwargs):
        return self.call('delete_user', kwargs=kwargs)

    def delete_project(self, **kwargs):
        return self.call('delete_project', kwargs=kwargs)

    def delete_material(self, **kwargs):
        return self.call('delete_material', kwargs=kwargs)

    def delete_sample(self, **kwargs):
        return self.call('delete_sample', kwargs=kwargs)

    def delete_labnumber(self, **kwargs):
        return self.call('delete_labnumber', kwargs=kwargs)

    def create_all(self, **kwargs):
        return self.call('create_all', kwargs=kwargs)

    def session_ctx(self, **kwargs):
        return self.call('session_ctx', kwargs=kwargs)

    def create_session(self, **kwargs):
        return self.call('create_session', kwargs=kwargs)

    def close_session(self, **kwargs):
        return self.call('close_session', kwargs=kwargs)

    def enabled(self, **kwargs):
        return self.call('enabled', kwargs=kwargs)

    def save_username(self, **kwargs):
        return self.call('save_username', kwargs=kwargs)

    def reset_connection(self, **kwargs):
        return self.call('reset_connection', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def rollback(self, **kwargs):
        return self.call('rollback', kwargs=kwargs)

    def flush(self, **kwargs):
        return self.call('flush', kwargs=kwargs)

    def expire(self, **kwargs):
        return self.call('expire', kwargs=kwargs)

    def expire_all(self, **kwargs):
        return self.call('expire_all', kwargs=kwargs)

    def commit(self, **kwargs):
        return self.call('commit', kwargs=kwargs)

    def delete(self, **kwargs):
        return self.call('delete', kwargs=kwargs)

    def post_commit(self, **kwargs):
        return self.call('post_commit', kwargs=kwargs)

    def add_item(self, **kwargs):
        return self.call('add_item', kwargs=kwargs)

    def get_migrate_version(self, **kwargs):
        return self.call('get_migrate_version', kwargs=kwargs)

    def get_versions(self, **kwargs):
        return self.call('get_versions', kwargs=kwargs)

    def public_datasource_url(self, **kwargs):
        return self.call('public_datasource_url', kwargs=kwargs)

    def public_url(self, **kwargs):
        return self.call('public_url', kwargs=kwargs)

    def init_logger(self, **kwargs):
        return self.call('init_logger', kwargs=kwargs)

    def report_logger_stats(self, **kwargs):
        return self.call('report_logger_stats', kwargs=kwargs)

    def unique_warning(self, **kwargs):
        return self.call('unique_warning', kwargs=kwargs)

    def unique_info(self, **kwargs):
        return self.call('unique_info', kwargs=kwargs)

    def unique_debug(self, **kwargs):
        return self.call('unique_debug', kwargs=kwargs)

    def warning(self, **kwargs):
        return self.call('warning', kwargs=kwargs)

    def info(self, **kwargs):
        return self.call('info', kwargs=kwargs)

    def debug_exception(self, **kwargs):
        return self.call('debug_exception', kwargs=kwargs)

    def warning_exception(self, **kwargs):
        return self.call('warning_exception', kwargs=kwargs)

    def critical(self, **kwargs):
        return self.call('critical', kwargs=kwargs)

    def debug(self, **kwargs):
        return self.call('debug', kwargs=kwargs)

    def log(self, **kwargs):
        return self.call('log', kwargs=kwargs)

    def warning_dialog(self, **kwargs):
        return self.call('warning_dialog', kwargs=kwargs)

    def confirmation_dialog(self, **kwargs):
        return self.call('confirmation_dialog', kwargs=kwargs)

    def information_dialog(self, **kwargs):
        return self.call('information_dialog', kwargs=kwargs)

    def message(self, **kwargs):
        return self.call('message', kwargs=kwargs)

    def open_file_dialog(self, **kwargs):
        return self.call('open_file_dialog', kwargs=kwargs)

    def save_file_dialog(self, **kwargs):
        return self.call('save_file_dialog', kwargs=kwargs)

    def open_directory_dialog(self, **kwargs):
        return self.call('open_directory_dialog', kwargs=kwargs)

    def save_directory_dialog(self, **kwargs):
        return self.call('save_directory_dialog', kwargs=kwargs)

