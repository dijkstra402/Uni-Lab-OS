from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentJeolJsm7800fIt500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/SBEMimage__SBEMimage', 'source_file': 'src/MainControls.py', 'class_name': 'MainControls', 'import_roots': ['src'], 'candidate_methods': ['initialize_main_controls_gui', 'tab_changed', 'try_to_create_directory', 'update_main_controls_grid_selector', 'update_main_controls_ov_selector', 'change_grid_settings_display', 'change_ov_settings_display', 'show_current_settings', 'show_stack_acq_estimates', 'update_acq_options', 'set_active_user_flag', 'clear_activate_user_flag', 'update_acq_notes', 'acq_notes_text_changed', 'save_acq_notes', 'initialize_array_gui', 'find_array_from_model_index', 'find_model_from_array_index', 'find_grid_from_model_index', 'array_select_all', 'array_deselect_all', 'array_check_selected', 'array_uncheck_selected', 'array_invert_selection', 'array_toggle_selection', 'array_select_checked', 'array_select_string_sections', 'array_set_check_items', 'array_select_items', 'array_actions_selected_sections_changed', 'array_activate_checked_sections', 'array_activate_checked_item', 'array_checked_section', 'array_double_clicked_section', 'array_set_section_state_in_table', 'array_reset_dialog', 'array_trigger_landmark_uncalibrated', 'array_reset', 'array_trigger_landmark_calibrated', 'array_trigger_landmark_calibratable', 'array_trigger_landmark_uncalibratable', 'array_open_import_dlg', 'array_init_gui', 'array_open_import_image', 'array_set_import_image', 'array_create_grids', 'array_open_landmark_calibration_dlg', 'open_mag_calibration_dlg', 'open_save_settings_new_file_dlg', 'open_sem_dlg', 'open_microtome_dlg', 'open_calibration_dlg', 'open_cut_duration_dlg', 'open_ov_dlg', 'update_from_ov_dlg', 'get_open_grid_dlg', 'open_grid_dlg', 'update_from_grid_dlg', 'open_acq_settings_dlg', 'open_pre_stack_dlg', 'open_export_dlg', 'open_update_dlg', 'open_email_monitoring_dlg', 'open_debris_dlg', 'open_ask_user_dlg', 'open_tcp_settings_dlg', 'open_mirror_drive_dlg', 'open_image_monitoring_dlg', 'open_autofocus_settings_dlg', 'open_run_autofocus_dlg', 'open_plasma_cleaner_dlg', 'open_approach_dlg', 'open_grab_frame_dlg', 'open_variable_pressure_dlg', 'open_charge_compensator_dlg', 'open_eht_dlg', 'open_motor_test_dlg', 'open_motor_status_dlg', 'open_send_command_dlg', 'open_about_box', 'show_stack_progress', 'show_current_stage_xy', 'show_current_stage_z', 'set_statusbar', 'set_status', 'event', 'process_signal', 'ask_debris_first_ov', 'ask_debris_confirmation', 'restrict_gui', 'restrict_focus_tool_gui', 'restrict_tests_gui', 'restrict_gui_for_simulation_mode', 'restrict_gui_for_sem_stage', 'restrict_gui_wo_gcib', 'write_current_log_to_file', 'manual_sweep', 'manual_sweep_success', 'save_viewport_screenshot', 'test_get_mag', 'test_set_mag', 'test_get_wd', 'test_set_wd', 'test_autofocus', 'test_zeiss_api_version', 'test_get_stage', 'test_set_stage', 'test_near_knife', 'test_clear_knife', 'test_run_maintenance_moves', 'test_run_maintenance_moves_finished', 'test_get_mill_pos', 'test_set_mill_pos', 'test_set_pos_prior_mill_mov', 'test_mill_mov', 'test_milling', 'test_stop_dm_script', 'test_send_email', 'test_plasma_cleaner', 'test_server_request', 'debris_detection_test', 'custom_test', 'initialize_plasma_cleaner', 'start_acquisition', 'pause_acquisition', 'reset_acquisition', 'completion_stop', 'remote_stop', 'error_pause', 'acq_not_in_progress_update_gui', 'leave_simulation_mode', 'save_settings', 'save_config_to_disk', 'closeEvent', 'ft_initialize', 'ft_clear_display', 'ft_start', 'ft_ask_user_save', 'ft_open_set_params_dlg', 'ft_use_autofocus', 'ft_set_new_wd_stig', 'ft_show_updated_stage_position', 'ft_open_move_dlg', 'ft_run_cycle', 'ft_move_and_acq_thread', 'ft_reset', 'ft_series_complete', 'ft_acquire_focus_series', 'ft_acquire_stig_series', 'ft_display_during_cycle', 'ft_move_up', 'ft_move_down', 'ft_update_stig_display', 'ft_update_wd_display', 'ft_clear_wd_stig_display', 'ft_update_grid_selector', 'ft_update_tile_selector', 'ft_update_ov_selector', 'ft_change_grid_selection', 'ft_load_selected_tile', 'ft_load_selected_ov', 'ft_set_selection_from_viewport', 'ft_toggle_zoom', 'ft_toggle_use_current_position', 'keyPressEvent', 'wheelEvent'], 'action_targets': {}, 'metadata': {'repo': 'SBEMimage/SBEMimage', 'repo_url': 'https://github.com/SBEMimage/SBEMimage', 'brand': 'JEOL', 'model': 'JSM-7800F/IT500', 'device_type_cn': '扫描电子显微镜', 'device_type_en': 'Scanning Electron Microscope', 'source_framework': 'SBEMimage', 'tag_id': '4390', 'tag_name': '扫描电子显微镜', 'tag_name_en': 'Scanning Electron Microscope', 'candidate_score': 1358, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def initialize_main_controls_gui(self, **kwargs):
        return self.call('initialize_main_controls_gui', kwargs=kwargs)

    def tab_changed(self, **kwargs):
        return self.call('tab_changed', kwargs=kwargs)

    def try_to_create_directory(self, **kwargs):
        return self.call('try_to_create_directory', kwargs=kwargs)

    def update_main_controls_grid_selector(self, **kwargs):
        return self.call('update_main_controls_grid_selector', kwargs=kwargs)

    def update_main_controls_ov_selector(self, **kwargs):
        return self.call('update_main_controls_ov_selector', kwargs=kwargs)

    def change_grid_settings_display(self, **kwargs):
        return self.call('change_grid_settings_display', kwargs=kwargs)

    def change_ov_settings_display(self, **kwargs):
        return self.call('change_ov_settings_display', kwargs=kwargs)

    def show_current_settings(self, **kwargs):
        return self.call('show_current_settings', kwargs=kwargs)

    def show_stack_acq_estimates(self, **kwargs):
        return self.call('show_stack_acq_estimates', kwargs=kwargs)

    def update_acq_options(self, **kwargs):
        return self.call('update_acq_options', kwargs=kwargs)

    def set_active_user_flag(self, **kwargs):
        return self.call('set_active_user_flag', kwargs=kwargs)

    def clear_activate_user_flag(self, **kwargs):
        return self.call('clear_activate_user_flag', kwargs=kwargs)

    def update_acq_notes(self, **kwargs):
        return self.call('update_acq_notes', kwargs=kwargs)

    def acq_notes_text_changed(self, **kwargs):
        return self.call('acq_notes_text_changed', kwargs=kwargs)

    def save_acq_notes(self, **kwargs):
        return self.call('save_acq_notes', kwargs=kwargs)

    def initialize_array_gui(self, **kwargs):
        return self.call('initialize_array_gui', kwargs=kwargs)

    def find_array_from_model_index(self, **kwargs):
        return self.call('find_array_from_model_index', kwargs=kwargs)

    def find_model_from_array_index(self, **kwargs):
        return self.call('find_model_from_array_index', kwargs=kwargs)

    def find_grid_from_model_index(self, **kwargs):
        return self.call('find_grid_from_model_index', kwargs=kwargs)

    def array_select_all(self, **kwargs):
        return self.call('array_select_all', kwargs=kwargs)

    def array_deselect_all(self, **kwargs):
        return self.call('array_deselect_all', kwargs=kwargs)

    def array_check_selected(self, **kwargs):
        return self.call('array_check_selected', kwargs=kwargs)

    def array_uncheck_selected(self, **kwargs):
        return self.call('array_uncheck_selected', kwargs=kwargs)

    def array_invert_selection(self, **kwargs):
        return self.call('array_invert_selection', kwargs=kwargs)

    def array_toggle_selection(self, **kwargs):
        return self.call('array_toggle_selection', kwargs=kwargs)

    def array_select_checked(self, **kwargs):
        return self.call('array_select_checked', kwargs=kwargs)

    def array_select_string_sections(self, **kwargs):
        return self.call('array_select_string_sections', kwargs=kwargs)

    def array_set_check_items(self, **kwargs):
        return self.call('array_set_check_items', kwargs=kwargs)

    def array_select_items(self, **kwargs):
        return self.call('array_select_items', kwargs=kwargs)

    def array_actions_selected_sections_changed(self, **kwargs):
        return self.call('array_actions_selected_sections_changed', kwargs=kwargs)

    def array_activate_checked_sections(self, **kwargs):
        return self.call('array_activate_checked_sections', kwargs=kwargs)

    def array_activate_checked_item(self, **kwargs):
        return self.call('array_activate_checked_item', kwargs=kwargs)

    def array_checked_section(self, **kwargs):
        return self.call('array_checked_section', kwargs=kwargs)

    def array_double_clicked_section(self, **kwargs):
        return self.call('array_double_clicked_section', kwargs=kwargs)

    def array_set_section_state_in_table(self, **kwargs):
        return self.call('array_set_section_state_in_table', kwargs=kwargs)

    def array_reset_dialog(self, **kwargs):
        return self.call('array_reset_dialog', kwargs=kwargs)

    def array_trigger_landmark_uncalibrated(self, **kwargs):
        return self.call('array_trigger_landmark_uncalibrated', kwargs=kwargs)

    def array_reset(self, **kwargs):
        return self.call('array_reset', kwargs=kwargs)

    def array_trigger_landmark_calibrated(self, **kwargs):
        return self.call('array_trigger_landmark_calibrated', kwargs=kwargs)

    def array_trigger_landmark_calibratable(self, **kwargs):
        return self.call('array_trigger_landmark_calibratable', kwargs=kwargs)

    def array_trigger_landmark_uncalibratable(self, **kwargs):
        return self.call('array_trigger_landmark_uncalibratable', kwargs=kwargs)

    def array_open_import_dlg(self, **kwargs):
        return self.call('array_open_import_dlg', kwargs=kwargs)

    def array_init_gui(self, **kwargs):
        return self.call('array_init_gui', kwargs=kwargs)

    def array_open_import_image(self, **kwargs):
        return self.call('array_open_import_image', kwargs=kwargs)

    def array_set_import_image(self, **kwargs):
        return self.call('array_set_import_image', kwargs=kwargs)

    def array_create_grids(self, **kwargs):
        return self.call('array_create_grids', kwargs=kwargs)

    def array_open_landmark_calibration_dlg(self, **kwargs):
        return self.call('array_open_landmark_calibration_dlg', kwargs=kwargs)

    def open_mag_calibration_dlg(self, **kwargs):
        return self.call('open_mag_calibration_dlg', kwargs=kwargs)

    def open_save_settings_new_file_dlg(self, **kwargs):
        return self.call('open_save_settings_new_file_dlg', kwargs=kwargs)

    def open_sem_dlg(self, **kwargs):
        return self.call('open_sem_dlg', kwargs=kwargs)

    def open_microtome_dlg(self, **kwargs):
        return self.call('open_microtome_dlg', kwargs=kwargs)

    def open_calibration_dlg(self, **kwargs):
        return self.call('open_calibration_dlg', kwargs=kwargs)

    def open_cut_duration_dlg(self, **kwargs):
        return self.call('open_cut_duration_dlg', kwargs=kwargs)

    def open_ov_dlg(self, **kwargs):
        return self.call('open_ov_dlg', kwargs=kwargs)

    def update_from_ov_dlg(self, **kwargs):
        return self.call('update_from_ov_dlg', kwargs=kwargs)

    def get_open_grid_dlg(self, **kwargs):
        return self.call('get_open_grid_dlg', kwargs=kwargs)

    def open_grid_dlg(self, **kwargs):
        return self.call('open_grid_dlg', kwargs=kwargs)

    def update_from_grid_dlg(self, **kwargs):
        return self.call('update_from_grid_dlg', kwargs=kwargs)

    def open_acq_settings_dlg(self, **kwargs):
        return self.call('open_acq_settings_dlg', kwargs=kwargs)

    def open_pre_stack_dlg(self, **kwargs):
        return self.call('open_pre_stack_dlg', kwargs=kwargs)

    def open_export_dlg(self, **kwargs):
        return self.call('open_export_dlg', kwargs=kwargs)

    def open_update_dlg(self, **kwargs):
        return self.call('open_update_dlg', kwargs=kwargs)

    def open_email_monitoring_dlg(self, **kwargs):
        return self.call('open_email_monitoring_dlg', kwargs=kwargs)

    def open_debris_dlg(self, **kwargs):
        return self.call('open_debris_dlg', kwargs=kwargs)

    def open_ask_user_dlg(self, **kwargs):
        return self.call('open_ask_user_dlg', kwargs=kwargs)

    def open_tcp_settings_dlg(self, **kwargs):
        return self.call('open_tcp_settings_dlg', kwargs=kwargs)

    def open_mirror_drive_dlg(self, **kwargs):
        return self.call('open_mirror_drive_dlg', kwargs=kwargs)

    def open_image_monitoring_dlg(self, **kwargs):
        return self.call('open_image_monitoring_dlg', kwargs=kwargs)

    def open_autofocus_settings_dlg(self, **kwargs):
        return self.call('open_autofocus_settings_dlg', kwargs=kwargs)

    def open_run_autofocus_dlg(self, **kwargs):
        return self.call('open_run_autofocus_dlg', kwargs=kwargs)

    def open_plasma_cleaner_dlg(self, **kwargs):
        return self.call('open_plasma_cleaner_dlg', kwargs=kwargs)

    def open_approach_dlg(self, **kwargs):
        return self.call('open_approach_dlg', kwargs=kwargs)

    def open_grab_frame_dlg(self, **kwargs):
        return self.call('open_grab_frame_dlg', kwargs=kwargs)

    def open_variable_pressure_dlg(self, **kwargs):
        return self.call('open_variable_pressure_dlg', kwargs=kwargs)

    def open_charge_compensator_dlg(self, **kwargs):
        return self.call('open_charge_compensator_dlg', kwargs=kwargs)

    def open_eht_dlg(self, **kwargs):
        return self.call('open_eht_dlg', kwargs=kwargs)

    def open_motor_test_dlg(self, **kwargs):
        return self.call('open_motor_test_dlg', kwargs=kwargs)

    def open_motor_status_dlg(self, **kwargs):
        return self.call('open_motor_status_dlg', kwargs=kwargs)

    def open_send_command_dlg(self, **kwargs):
        return self.call('open_send_command_dlg', kwargs=kwargs)

    def open_about_box(self, **kwargs):
        return self.call('open_about_box', kwargs=kwargs)

    def show_stack_progress(self, **kwargs):
        return self.call('show_stack_progress', kwargs=kwargs)

    def show_current_stage_xy(self, **kwargs):
        return self.call('show_current_stage_xy', kwargs=kwargs)

    def show_current_stage_z(self, **kwargs):
        return self.call('show_current_stage_z', kwargs=kwargs)

    def set_statusbar(self, **kwargs):
        return self.call('set_statusbar', kwargs=kwargs)

    def set_status(self, **kwargs):
        return self.call('set_status', kwargs=kwargs)

    def event(self, **kwargs):
        return self.call('event', kwargs=kwargs)

    def process_signal(self, **kwargs):
        return self.call('process_signal', kwargs=kwargs)

    def ask_debris_first_ov(self, **kwargs):
        return self.call('ask_debris_first_ov', kwargs=kwargs)

    def ask_debris_confirmation(self, **kwargs):
        return self.call('ask_debris_confirmation', kwargs=kwargs)

    def restrict_gui(self, **kwargs):
        return self.call('restrict_gui', kwargs=kwargs)

    def restrict_focus_tool_gui(self, **kwargs):
        return self.call('restrict_focus_tool_gui', kwargs=kwargs)

    def restrict_tests_gui(self, **kwargs):
        return self.call('restrict_tests_gui', kwargs=kwargs)

    def restrict_gui_for_simulation_mode(self, **kwargs):
        return self.call('restrict_gui_for_simulation_mode', kwargs=kwargs)

    def restrict_gui_for_sem_stage(self, **kwargs):
        return self.call('restrict_gui_for_sem_stage', kwargs=kwargs)

    def restrict_gui_wo_gcib(self, **kwargs):
        return self.call('restrict_gui_wo_gcib', kwargs=kwargs)

    def write_current_log_to_file(self, **kwargs):
        return self.call('write_current_log_to_file', kwargs=kwargs)

    def manual_sweep(self, **kwargs):
        return self.call('manual_sweep', kwargs=kwargs)

    def manual_sweep_success(self, **kwargs):
        return self.call('manual_sweep_success', kwargs=kwargs)

    def save_viewport_screenshot(self, **kwargs):
        return self.call('save_viewport_screenshot', kwargs=kwargs)

    def test_get_mag(self, **kwargs):
        return self.call('test_get_mag', kwargs=kwargs)

    def test_set_mag(self, **kwargs):
        return self.call('test_set_mag', kwargs=kwargs)

    def test_get_wd(self, **kwargs):
        return self.call('test_get_wd', kwargs=kwargs)

    def test_set_wd(self, **kwargs):
        return self.call('test_set_wd', kwargs=kwargs)

    def test_autofocus(self, **kwargs):
        return self.call('test_autofocus', kwargs=kwargs)

    def test_zeiss_api_version(self, **kwargs):
        return self.call('test_zeiss_api_version', kwargs=kwargs)

    def test_get_stage(self, **kwargs):
        return self.call('test_get_stage', kwargs=kwargs)

    def test_set_stage(self, **kwargs):
        return self.call('test_set_stage', kwargs=kwargs)

    def test_near_knife(self, **kwargs):
        return self.call('test_near_knife', kwargs=kwargs)

    def test_clear_knife(self, **kwargs):
        return self.call('test_clear_knife', kwargs=kwargs)

    def test_run_maintenance_moves(self, **kwargs):
        return self.call('test_run_maintenance_moves', kwargs=kwargs)

    def test_run_maintenance_moves_finished(self, **kwargs):
        return self.call('test_run_maintenance_moves_finished', kwargs=kwargs)

    def test_get_mill_pos(self, **kwargs):
        return self.call('test_get_mill_pos', kwargs=kwargs)

    def test_set_mill_pos(self, **kwargs):
        return self.call('test_set_mill_pos', kwargs=kwargs)

    def test_set_pos_prior_mill_mov(self, **kwargs):
        return self.call('test_set_pos_prior_mill_mov', kwargs=kwargs)

    def test_mill_mov(self, **kwargs):
        return self.call('test_mill_mov', kwargs=kwargs)

    def test_milling(self, **kwargs):
        return self.call('test_milling', kwargs=kwargs)

    def test_stop_dm_script(self, **kwargs):
        return self.call('test_stop_dm_script', kwargs=kwargs)

    def test_send_email(self, **kwargs):
        return self.call('test_send_email', kwargs=kwargs)

    def test_plasma_cleaner(self, **kwargs):
        return self.call('test_plasma_cleaner', kwargs=kwargs)

    def test_server_request(self, **kwargs):
        return self.call('test_server_request', kwargs=kwargs)

    def debris_detection_test(self, **kwargs):
        return self.call('debris_detection_test', kwargs=kwargs)

    def custom_test(self, **kwargs):
        return self.call('custom_test', kwargs=kwargs)

    def initialize_plasma_cleaner(self, **kwargs):
        return self.call('initialize_plasma_cleaner', kwargs=kwargs)

    def start_acquisition(self, **kwargs):
        return self.call('start_acquisition', kwargs=kwargs)

    def pause_acquisition(self, **kwargs):
        return self.call('pause_acquisition', kwargs=kwargs)

    def reset_acquisition(self, **kwargs):
        return self.call('reset_acquisition', kwargs=kwargs)

    def completion_stop(self, **kwargs):
        return self.call('completion_stop', kwargs=kwargs)

    def remote_stop(self, **kwargs):
        return self.call('remote_stop', kwargs=kwargs)

    def error_pause(self, **kwargs):
        return self.call('error_pause', kwargs=kwargs)

    def acq_not_in_progress_update_gui(self, **kwargs):
        return self.call('acq_not_in_progress_update_gui', kwargs=kwargs)

    def leave_simulation_mode(self, **kwargs):
        return self.call('leave_simulation_mode', kwargs=kwargs)

    def save_settings(self, **kwargs):
        return self.call('save_settings', kwargs=kwargs)

    def save_config_to_disk(self, **kwargs):
        return self.call('save_config_to_disk', kwargs=kwargs)

    def closeEvent(self, **kwargs):
        return self.call('closeEvent', kwargs=kwargs)

    def ft_initialize(self, **kwargs):
        return self.call('ft_initialize', kwargs=kwargs)

    def ft_clear_display(self, **kwargs):
        return self.call('ft_clear_display', kwargs=kwargs)

    def ft_start(self, **kwargs):
        return self.call('ft_start', kwargs=kwargs)

    def ft_ask_user_save(self, **kwargs):
        return self.call('ft_ask_user_save', kwargs=kwargs)

    def ft_open_set_params_dlg(self, **kwargs):
        return self.call('ft_open_set_params_dlg', kwargs=kwargs)

    def ft_use_autofocus(self, **kwargs):
        return self.call('ft_use_autofocus', kwargs=kwargs)

    def ft_set_new_wd_stig(self, **kwargs):
        return self.call('ft_set_new_wd_stig', kwargs=kwargs)

    def ft_show_updated_stage_position(self, **kwargs):
        return self.call('ft_show_updated_stage_position', kwargs=kwargs)

    def ft_open_move_dlg(self, **kwargs):
        return self.call('ft_open_move_dlg', kwargs=kwargs)

    def ft_run_cycle(self, **kwargs):
        return self.call('ft_run_cycle', kwargs=kwargs)

    def ft_move_and_acq_thread(self, **kwargs):
        return self.call('ft_move_and_acq_thread', kwargs=kwargs)

    def ft_reset(self, **kwargs):
        return self.call('ft_reset', kwargs=kwargs)

    def ft_series_complete(self, **kwargs):
        return self.call('ft_series_complete', kwargs=kwargs)

    def ft_acquire_focus_series(self, **kwargs):
        return self.call('ft_acquire_focus_series', kwargs=kwargs)

    def ft_acquire_stig_series(self, **kwargs):
        return self.call('ft_acquire_stig_series', kwargs=kwargs)

    def ft_display_during_cycle(self, **kwargs):
        return self.call('ft_display_during_cycle', kwargs=kwargs)

    def ft_move_up(self, **kwargs):
        return self.call('ft_move_up', kwargs=kwargs)

    def ft_move_down(self, **kwargs):
        return self.call('ft_move_down', kwargs=kwargs)

    def ft_update_stig_display(self, **kwargs):
        return self.call('ft_update_stig_display', kwargs=kwargs)

    def ft_update_wd_display(self, **kwargs):
        return self.call('ft_update_wd_display', kwargs=kwargs)

    def ft_clear_wd_stig_display(self, **kwargs):
        return self.call('ft_clear_wd_stig_display', kwargs=kwargs)

    def ft_update_grid_selector(self, **kwargs):
        return self.call('ft_update_grid_selector', kwargs=kwargs)

    def ft_update_tile_selector(self, **kwargs):
        return self.call('ft_update_tile_selector', kwargs=kwargs)

    def ft_update_ov_selector(self, **kwargs):
        return self.call('ft_update_ov_selector', kwargs=kwargs)

    def ft_change_grid_selection(self, **kwargs):
        return self.call('ft_change_grid_selection', kwargs=kwargs)

    def ft_load_selected_tile(self, **kwargs):
        return self.call('ft_load_selected_tile', kwargs=kwargs)

    def ft_load_selected_ov(self, **kwargs):
        return self.call('ft_load_selected_ov', kwargs=kwargs)

    def ft_set_selection_from_viewport(self, **kwargs):
        return self.call('ft_set_selection_from_viewport', kwargs=kwargs)

    def ft_toggle_zoom(self, **kwargs):
        return self.call('ft_toggle_zoom', kwargs=kwargs)

    def ft_toggle_use_current_position(self, **kwargs):
        return self.call('ft_toggle_use_current_position', kwargs=kwargs)

    def keyPressEvent(self, **kwargs):
        return self.call('keyPressEvent', kwargs=kwargs)

    def wheelEvent(self, **kwargs):
        return self.call('wheelEvent', kwargs=kwargs)

