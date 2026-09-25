from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHamiltonStar(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/liquid_handling/backends/hamilton/STAR_backend.py', 'class_name': 'STARBackend', 'import_roots': [], 'candidate_methods': ['additional_time_stamp', 'aspirate', 'aspirate96', 'aspirate_core_96', 'aspirate_pip', 'can_pick_up_tip', 'can_reach_position', 'channel_dispensing_drive_move_to_volume_position', 'channel_dispensing_drive_request_position', 'channel_id', 'channel_request_cycle_counts', 'channel_request_y_minimum_spacing', 'channels_request_cycle_counts', 'channels_request_y_minimum_spacing', 'channels_sense_tip_presence', 'check_fw_string_error', 'check_type_is_hhc', 'clld_probe_x_position_using_channel', 'clld_probe_y_position_using_channel', 'clld_probe_z_height_using_channel', 'collapse_gripper_arm', 'configure_node_names', 'core_check_resource_exists_at_location_center', 'core_get_plate', 'core_move_picked_up_resource', 'core_move_plate_to_position', 'core_open_gripper', 'core_pick_up_resource', 'core_put_plate', 'core_read_barcode_of_picked_up_resource', 'core_release_picked_up_resource', 'define_tip_needle', 'disable_cover_control', 'discard_tip', 'discard_tips_core96', 'dispense', 'dispense96', 'dispense_core_96', 'dispense_pip', 'dispensing_drive_increment_to_mm', 'dispensing_drive_increment_to_volume', 'dispensing_drive_mm_to_increment', 'dispensing_drive_mm_to_vol', 'dispensing_drive_vol_to_increment', 'dispensing_drive_vol_to_mm', 'drain_dual_chamber_system', 'drop_resource', 'drop_tips', 'drop_tips96', 'empty_tip', 'empty_tips', 'enable_cover_control', 'ensure_can_reach_position', 'execute_batched', 'fill_selected_dual_chamber', 'get_channel_spacings', 'get_channels_y_positions', 'get_channels_z_positions', 'get_core', 'get_id_from_fw_response', 'get_iswap_version', 'get_logic_iswap_position', 'get_or_assign_tip_type_index', 'get_temperature_at_hhc', 'halt', 'head96_dispensing_drive_and_squeezer_driver_initialize', 'head96_dispensing_drive_move_to_home_volume', 'head96_dispensing_drive_move_to_position', 'head96_dispensing_drive_request_position_mm', 'head96_dispensing_drive_request_position_uL', 'head96_move_to_coordinate', 'head96_move_to_z_safety', 'head96_move_x', 'head96_move_y', 'head96_move_z', 'head96_park', 'head96_request_firmware_version', 'head96_request_position', 'head96_request_tip_presence', 'head96_request_type', 'initialize_auto_load', 'initialize_autoload', 'initialize_core_96_head', 'initialize_dual_pump_station_valves', 'initialize_hhc', 'initialize_iswap', 'initialize_pip', 'initialize_pipetting_channels', 'iswap_close_gripper', 'iswap_dangerous_release_break', 'iswap_get_plate', 'iswap_initialize_z_axis', 'iswap_minimum_traversal_height', 'iswap_move_picked_up_resource', 'iswap_open_gripper', 'iswap_put_plate', 'iswap_reengage_break', 'iswap_rotate', 'iswap_rotation_drive_request_y', 'load_carrier', 'load_carrier_from_autoload_belt', 'load_carrier_from_tray_and_scan_carrier_barcode', 'lock_cover', 'mm_to_y_drive_increment', 'mm_to_z_drive_increment', 'move_96head_to_coordinate', 'move_all_channels_in_z_safety', 'move_all_pipetting_channels_to_defined_position', 'move_auto_load_to_z_save_position', 'move_autoload_to_safe_z_position', 'move_autoload_to_save_z_position', 'move_autoload_to_slot', 'move_autoload_to_track', 'move_channel_stop_disk_z', 'move_channel_tool_z', 'move_channel_x', 'move_channel_x_relative', 'move_channel_y', 'move_channel_y_relative', 'move_channel_z', 'move_channel_z_relative', 'move_core_96_head_to_defined_position', 'move_core_96_head_x', 'move_core_96_head_y', 'move_core_96_head_z', 'move_core_96_to_safe_position', 'move_iswap_x', 'move_iswap_x_relative', 'move_iswap_y', 'move_iswap_y_relative', 'move_iswap_z', 'move_iswap_z_relative', 'move_left_x_arm_to_position_with_all_attached_components_in_z_safety_position', 'move_picked_up_resource', 'move_plate_to_position', 'move_right_x_arm_to_position_with_all_attached_components_in_z_safety_position', 'occupy_and_provide_area_for_external_access', 'open_not_initialized_gripper', 'park_autoload', 'park_iswap', 'pick_up_core_gripper_tools', 'pick_up_resource', 'pick_up_tip', 'pick_up_tips', 'pick_up_tips96', 'pick_up_tips_core96', 'pierce_foil', 'plld_probe_z_height_using_channel', 'position_channels_in_y_direction', 'position_channels_in_z_direction', 'position_components_for_free_iswap_y_range', 'position_left_x_arm_', 'position_max_free_y_for_n', 'position_right_x_arm_', 'position_single_pipetting_channel_in_y_direction', 'position_single_pipetting_channel_in_z_direction', 'pre_initialize_instrument', 'prepare_for_manual_channel_operation', 'prepare_iswap_teaching', 'probe_liquid_heights', 'probe_liquid_volumes', 'put_core', 'query_whether_temperature_reached_at_hhc', 'release_all_occupied_areas', 'release_occupied_area', 'request_additional_timestamp_data', 'request_auto_load_slot_position', 'request_autoload_initialization_status', 'request_autoload_track', 'request_autoload_type', 'request_core_96_head_channel_tadm_error_status', 'request_core_96_head_channel_tadm_status', 'request_core_96_head_initialization_status', 'request_cover_open', 'request_deck_data', 'request_device_serial_number', 'request_download_date', 'request_eeprom_data_correctness', 'request_electronic_board_type', 'request_error_code', 'request_extended_configuration', 'request_firmware_version', 'request_installation_data', 'request_instrument_initialization_status', 'request_iswap_in_parking_position', 'request_iswap_initialization_status', 'request_iswap_position', 'request_iswap_rotation_drive_orientation', 'request_iswap_rotation_drive_position_increments', 'request_iswap_version', 'request_iswap_wrist_drive_orientation', 'request_iswap_wrist_drive_position_increments', 'request_left_x_arm_last_collision_type', 'request_left_x_arm_position', 'request_machine_configuration', 'request_master_status', 'request_maximal_ranges_of_x_drives', 'request_name_of_last_faulty_parameter', 'request_node_names', 'request_number_of_presence_sensors_installed', 'request_parameter_value', 'request_pip_channel_validation_status', 'request_pip_channel_version', 'request_pip_height_last_lld', 'request_plate_in_iswap', 'request_position_of_core_96_head', 'request_presence_of_carriers_on_deck', 'request_presence_of_carriers_on_loading_tray', 'request_presence_of_single_carrier_on_loading_tray', 'request_present_wrap_size_of_installed_arms', 'request_probe_z_position', 'request_pump_settings', 'request_right_x_arm_last_collision_type', 'request_right_x_arm_position', 'request_single_carrier_presence', 'request_supply_voltage', 'request_tadm_status', 'request_technical_status_of_assemblies', 'request_tip_bottom_z_position', 'request_tip_len_on_channel', 'request_tip_presence', 'request_tip_presence_in_core_96_head', 'request_verification_data', 'request_volume_in_tip', 'request_x_pos_channel_n', 'request_xl_channel_validation_status', 'request_y_pos_channel_n', 'request_z_pos_channel_n', 'reset_output', 'return_core_gripper_tools', 'rotate_iswap_rotation_drive', 'rotate_iswap_wrist', 'save_all_cycle_counters', 'save_download_date', 'save_pip_channel_validation_status', 'save_technical_status_of_assemblies', 'save_xl_channel_validation_status', 'search_for_teach_in_signal_using_pipetting_channel_n_in_x_direction', 'send_hhs_command', 'send_raw_command', 'set_1d_barcode_type', 'set_barcode_type', 'set_carrier_monitoring', 'set_cover_output', 'set_deck', 'set_deck_data', 'set_heads', 'set_instrument_configuration', 'set_loading_indicators', 'set_minimum_channel_traversal_height', 'set_minimum_iswap_traversal_height', 'set_minimum_traversal_height', 'set_not_stop', 'set_single_step_mode', 'set_x_offset_x_axis_core_96_head', 'set_x_offset_x_axis_core_nano_pipettor_head', 'set_x_offset_x_axis_iswap', 'setup', 'slow_iswap', 'spread_pip_channels', 'start_temperature_control_at_hhc', 'step_off_foil', 'stop', 'stop_temperature_control_at_hhc', 'store_installation_data', 'store_verification_data', 'take_carrier_out_to_autoload_belt', 'trigger_next_step', 'unload_carrier', 'unload_carrier_after_carrier_barcode_scanning', 'unlock_cover', 'verify_and_wait_for_carriers', 'y_drive_increment_to_mm', 'z_drive_increment_to_mm', 'ztouch_probe_z_height_using_channel'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Hamilton', 'model': 'STAR/STARlet', 'device_type_cn': '移液工作站', 'device_type_en': 'Liquid Handling Workstation', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/liquid_handling/backends/hamilton/STAR_backend.py', 'class_name': 'STARBackend', 'candidate_methods': ['additional_time_stamp', 'aspirate', 'aspirate96', 'aspirate_core_96', 'aspirate_pip', 'can_pick_up_tip', 'can_reach_position', 'channel_dispensing_drive_move_to_volume_position', 'channel_dispensing_drive_request_position', 'channel_id', 'channel_request_cycle_counts', 'channel_request_y_minimum_spacing', 'channels_request_cycle_counts', 'channels_request_y_minimum_spacing', 'channels_sense_tip_presence', 'check_fw_string_error', 'check_type_is_hhc', 'clld_probe_x_position_using_channel', 'clld_probe_y_position_using_channel', 'clld_probe_z_height_using_channel', 'collapse_gripper_arm', 'configure_node_names', 'core_check_resource_exists_at_location_center', 'core_get_plate', 'core_move_picked_up_resource', 'core_move_plate_to_position', 'core_open_gripper', 'core_pick_up_resource', 'core_put_plate', 'core_read_barcode_of_picked_up_resource', 'core_release_picked_up_resource', 'define_tip_needle', 'disable_cover_control', 'discard_tip', 'discard_tips_core96', 'dispense', 'dispense96', 'dispense_core_96', 'dispense_pip', 'dispensing_drive_increment_to_mm', 'dispensing_drive_increment_to_volume', 'dispensing_drive_mm_to_increment', 'dispensing_drive_mm_to_vol', 'dispensing_drive_vol_to_increment', 'dispensing_drive_vol_to_mm', 'drain_dual_chamber_system', 'drop_resource', 'drop_tips', 'drop_tips96', 'empty_tip', 'empty_tips', 'enable_cover_control', 'ensure_can_reach_position', 'execute_batched', 'fill_selected_dual_chamber', 'get_channel_spacings', 'get_channels_y_positions', 'get_channels_z_positions', 'get_core', 'get_id_from_fw_response', 'get_iswap_version', 'get_logic_iswap_position', 'get_or_assign_tip_type_index', 'get_temperature_at_hhc', 'halt', 'head96_dispensing_drive_and_squeezer_driver_initialize', 'head96_dispensing_drive_move_to_home_volume', 'head96_dispensing_drive_move_to_position', 'head96_dispensing_drive_request_position_mm', 'head96_dispensing_drive_request_position_uL', 'head96_move_to_coordinate', 'head96_move_to_z_safety', 'head96_move_x', 'head96_move_y', 'head96_move_z', 'head96_park', 'head96_request_firmware_version', 'head96_request_position', 'head96_request_tip_presence', 'head96_request_type', 'initialize_auto_load', 'initialize_autoload', 'initialize_core_96_head', 'initialize_dual_pump_station_valves', 'initialize_hhc', 'initialize_iswap', 'initialize_pip', 'initialize_pipetting_channels', 'iswap_close_gripper', 'iswap_dangerous_release_break', 'iswap_get_plate', 'iswap_initialize_z_axis', 'iswap_minimum_traversal_height', 'iswap_move_picked_up_resource', 'iswap_open_gripper', 'iswap_put_plate', 'iswap_reengage_break', 'iswap_rotate', 'iswap_rotation_drive_request_y', 'load_carrier', 'load_carrier_from_autoload_belt', 'load_carrier_from_tray_and_scan_carrier_barcode', 'lock_cover', 'mm_to_y_drive_increment', 'mm_to_z_drive_increment', 'move_96head_to_coordinate', 'move_all_channels_in_z_safety', 'move_all_pipetting_channels_to_defined_position', 'move_auto_load_to_z_save_position', 'move_autoload_to_safe_z_position', 'move_autoload_to_save_z_position', 'move_autoload_to_slot', 'move_autoload_to_track', 'move_channel_stop_disk_z', 'move_channel_tool_z', 'move_channel_x', 'move_channel_x_relative', 'move_channel_y', 'move_channel_y_relative', 'move_channel_z', 'move_channel_z_relative', 'move_core_96_head_to_defined_position', 'move_core_96_head_x', 'move_core_96_head_y', 'move_core_96_head_z', 'move_core_96_to_safe_position', 'move_iswap_x', 'move_iswap_x_relative', 'move_iswap_y', 'move_iswap_y_relative', 'move_iswap_z', 'move_iswap_z_relative', 'move_left_x_arm_to_position_with_all_attached_components_in_z_safety_position', 'move_picked_up_resource', 'move_plate_to_position', 'move_right_x_arm_to_position_with_all_attached_components_in_z_safety_position', 'occupy_and_provide_area_for_external_access', 'open_not_initialized_gripper', 'park_autoload', 'park_iswap', 'pick_up_core_gripper_tools', 'pick_up_resource', 'pick_up_tip', 'pick_up_tips', 'pick_up_tips96', 'pick_up_tips_core96', 'pierce_foil', 'plld_probe_z_height_using_channel', 'position_channels_in_y_direction', 'position_channels_in_z_direction', 'position_components_for_free_iswap_y_range', 'position_left_x_arm_', 'position_max_free_y_for_n', 'position_right_x_arm_', 'position_single_pipetting_channel_in_y_direction', 'position_single_pipetting_channel_in_z_direction', 'pre_initialize_instrument', 'prepare_for_manual_channel_operation', 'prepare_iswap_teaching', 'probe_liquid_heights', 'probe_liquid_volumes', 'put_core', 'query_whether_temperature_reached_at_hhc', 'release_all_occupied_areas', 'release_occupied_area', 'request_additional_timestamp_data', 'request_auto_load_slot_position', 'request_autoload_initialization_status', 'request_autoload_track', 'request_autoload_type', 'request_core_96_head_channel_tadm_error_status', 'request_core_96_head_channel_tadm_status', 'request_core_96_head_initialization_status', 'request_cover_open', 'request_deck_data', 'request_device_serial_number', 'request_download_date', 'request_eeprom_data_correctness', 'request_electronic_board_type', 'request_error_code', 'request_extended_configuration', 'request_firmware_version', 'request_installation_data', 'request_instrument_initialization_status', 'request_iswap_in_parking_position', 'request_iswap_initialization_status', 'request_iswap_position', 'request_iswap_rotation_drive_orientation', 'request_iswap_rotation_drive_position_increments', 'request_iswap_version', 'request_iswap_wrist_drive_orientation', 'request_iswap_wrist_drive_position_increments', 'request_left_x_arm_last_collision_type', 'request_left_x_arm_position', 'request_machine_configuration', 'request_master_status', 'request_maximal_ranges_of_x_drives', 'request_name_of_last_faulty_parameter', 'request_node_names', 'request_number_of_presence_sensors_installed', 'request_parameter_value', 'request_pip_channel_validation_status', 'request_pip_channel_version', 'request_pip_height_last_lld', 'request_plate_in_iswap', 'request_position_of_core_96_head', 'request_presence_of_carriers_on_deck', 'request_presence_of_carriers_on_loading_tray', 'request_presence_of_single_carrier_on_loading_tray', 'request_present_wrap_size_of_installed_arms', 'request_probe_z_position', 'request_pump_settings', 'request_right_x_arm_last_collision_type', 'request_right_x_arm_position', 'request_single_carrier_presence', 'request_supply_voltage', 'request_tadm_status', 'request_technical_status_of_assemblies', 'request_tip_bottom_z_position', 'request_tip_len_on_channel', 'request_tip_presence', 'request_tip_presence_in_core_96_head', 'request_verification_data', 'request_volume_in_tip', 'request_x_pos_channel_n', 'request_xl_channel_validation_status', 'request_y_pos_channel_n', 'request_z_pos_channel_n', 'reset_output', 'return_core_gripper_tools', 'rotate_iswap_rotation_drive', 'rotate_iswap_wrist', 'save_all_cycle_counters', 'save_download_date', 'save_pip_channel_validation_status', 'save_technical_status_of_assemblies', 'save_xl_channel_validation_status', 'search_for_teach_in_signal_using_pipetting_channel_n_in_x_direction', 'send_hhs_command', 'send_raw_command', 'set_1d_barcode_type', 'set_barcode_type', 'set_carrier_monitoring', 'set_cover_output', 'set_deck', 'set_deck_data', 'set_heads', 'set_instrument_configuration', 'set_loading_indicators', 'set_minimum_channel_traversal_height', 'set_minimum_iswap_traversal_height', 'set_minimum_traversal_height', 'set_not_stop', 'set_single_step_mode', 'set_x_offset_x_axis_core_96_head', 'set_x_offset_x_axis_core_nano_pipettor_head', 'set_x_offset_x_axis_iswap', 'setup', 'slow_iswap', 'spread_pip_channels', 'start_temperature_control_at_hhc', 'step_off_foil', 'stop', 'stop_temperature_control_at_hhc', 'store_installation_data', 'store_verification_data', 'take_carrier_out_to_autoload_belt', 'trigger_next_step', 'unload_carrier', 'unload_carrier_after_carrier_barcode_scanning', 'unlock_cover', 'verify_and_wait_for_carriers', 'y_drive_increment_to_mm', 'z_drive_increment_to_mm', 'ztouch_probe_z_height_using_channel']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def additional_time_stamp(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('additional_time_stamp', kwargs={k: v for k, v in _kw.items() if v is not None})

    def aspirate(self, ops=None, use_channels=None, jet=None, blow_out=None, lld_search_height=None, clot_detection_height=None, pull_out_distance_transport_air=None, second_section_height=None, second_section_ratio=None, minimum_height=None, immersion_depth=None, surface_following_distance=None, transport_air_volume=None, pre_wetting_volume=None, lld_mode=None, gamma_lld_sensitivity=None, dp_lld_sensitivity=None, aspirate_position_above_z_touch_off=None, detection_height_difference_for_dual_lld=None, swap_speed=None, settling_time=None, mix_position_from_liquid_surface=None, mix_surface_following_distance=None, limit_curve_index=None, use_2nd_section_aspiration=None, retract_height_over_2nd_section_to_empty_tip=None, dispensation_speed_during_emptying_tip=None, dosing_drive_speed_during_2nd_section_search=None, z_drive_speed_during_2nd_section_search=None, cup_upper_edge=None, ratio_liquid_rise_to_tip_deep_in=None, immersion_depth_2nd_section=None, minimum_traverse_height_at_beginning_of_a_command=None, min_z_endpos=None, liquid_surface_no_lld=None, probe_liquid_height=None, auto_surface_following_distance=None, hamilton_liquid_classes=None, disable_volume_correction=None, mix_volume=None, mix_cycles=None, mix_speed=None, immersion_depth_direction=None, liquid_surfaces_no_lld=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'jet': jet, 'blow_out': blow_out, 'lld_search_height': lld_search_height, 'clot_detection_height': clot_detection_height, 'pull_out_distance_transport_air': pull_out_distance_transport_air, 'second_section_height': second_section_height, 'second_section_ratio': second_section_ratio, 'minimum_height': minimum_height, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'transport_air_volume': transport_air_volume, 'pre_wetting_volume': pre_wetting_volume, 'lld_mode': lld_mode, 'gamma_lld_sensitivity': gamma_lld_sensitivity, 'dp_lld_sensitivity': dp_lld_sensitivity, 'aspirate_position_above_z_touch_off': aspirate_position_above_z_touch_off, 'detection_height_difference_for_dual_lld': detection_height_difference_for_dual_lld, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_position_from_liquid_surface': mix_position_from_liquid_surface, 'mix_surface_following_distance': mix_surface_following_distance, 'limit_curve_index': limit_curve_index, 'use_2nd_section_aspiration': use_2nd_section_aspiration, 'retract_height_over_2nd_section_to_empty_tip': retract_height_over_2nd_section_to_empty_tip, 'dispensation_speed_during_emptying_tip': dispensation_speed_during_emptying_tip, 'dosing_drive_speed_during_2nd_section_search': dosing_drive_speed_during_2nd_section_search, 'z_drive_speed_during_2nd_section_search': z_drive_speed_during_2nd_section_search, 'cup_upper_edge': cup_upper_edge, 'ratio_liquid_rise_to_tip_deep_in': ratio_liquid_rise_to_tip_deep_in, 'immersion_depth_2nd_section': immersion_depth_2nd_section, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'min_z_endpos': min_z_endpos, 'liquid_surface_no_lld': liquid_surface_no_lld, 'probe_liquid_height': probe_liquid_height, 'auto_surface_following_distance': auto_surface_following_distance, 'hamilton_liquid_classes': hamilton_liquid_classes, 'disable_volume_correction': disable_volume_correction, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_speed': mix_speed, 'immersion_depth_direction': immersion_depth_direction, 'liquid_surfaces_no_lld': liquid_surfaces_no_lld}
        _kw.update(kwargs)
        return self.call('aspirate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def aspirate96(self, aspiration=None, jet=None, blow_out=None, use_lld=None, pull_out_distance_transport_air=None, hlc=None, aspiration_type=None, minimum_traverse_height_at_beginning_of_a_command=None, min_z_endpos=None, lld_search_height=None, minimum_height=None, second_section_height=None, second_section_ratio=None, immersion_depth=None, surface_following_distance=None, transport_air_volume=None, pre_wetting_volume=None, gamma_lld_sensitivity=None, swap_speed=None, settling_time=None, mix_position_from_liquid_surface=None, mix_surface_following_distance=None, limit_curve_index=None, disable_volume_correction=None, liquid_surface_sink_distance_at_the_end_of_aspiration=None, minimal_end_height=None, air_transport_retract_dist=None, maximum_immersion_depth=None, surface_following_distance_during_mix=None, tube_2nd_section_height_measured_from_zm=None, tube_2nd_section_ratio=None, immersion_depth_direction=None, mix_volume=None, mix_cycles=None, speed_of_mix=None, **kwargs):
        _kw = {'aspiration': aspiration, 'jet': jet, 'blow_out': blow_out, 'use_lld': use_lld, 'pull_out_distance_transport_air': pull_out_distance_transport_air, 'hlc': hlc, 'aspiration_type': aspiration_type, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'min_z_endpos': min_z_endpos, 'lld_search_height': lld_search_height, 'minimum_height': minimum_height, 'second_section_height': second_section_height, 'second_section_ratio': second_section_ratio, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'transport_air_volume': transport_air_volume, 'pre_wetting_volume': pre_wetting_volume, 'gamma_lld_sensitivity': gamma_lld_sensitivity, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_position_from_liquid_surface': mix_position_from_liquid_surface, 'mix_surface_following_distance': mix_surface_following_distance, 'limit_curve_index': limit_curve_index, 'disable_volume_correction': disable_volume_correction, 'liquid_surface_sink_distance_at_the_end_of_aspiration': liquid_surface_sink_distance_at_the_end_of_aspiration, 'minimal_end_height': minimal_end_height, 'air_transport_retract_dist': air_transport_retract_dist, 'maximum_immersion_depth': maximum_immersion_depth, 'surface_following_distance_during_mix': surface_following_distance_during_mix, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'immersion_depth_direction': immersion_depth_direction, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'speed_of_mix': speed_of_mix}
        _kw.update(kwargs)
        return self.call('aspirate96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def aspirate_core_96(self, aspiration_type=None, x_position=None, x_direction=None, y_positions=None, minimum_traverse_height_at_beginning_of_a_command=None, min_z_endpos=None, lld_search_height=None, liquid_surface_no_lld=None, pull_out_distance_transport_air=None, minimum_height=None, second_section_height=None, second_section_ratio=None, immersion_depth=None, immersion_depth_direction=None, surface_following_distance=None, aspiration_volumes=None, aspiration_speed=None, transport_air_volume=None, blow_out_air_volume=None, pre_wetting_volume=None, lld_mode=None, gamma_lld_sensitivity=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_from_liquid_surface=None, mix_surface_following_distance=None, speed_of_mix=None, channel_pattern=None, limit_curve_index=None, tadm_algorithm=None, recording_mode=None, liquid_surface_sink_distance_at_the_end_of_aspiration=None, minimal_end_height=None, liquid_surface_at_function_without_lld=None, pull_out_distance_to_take_transport_air_in_function_without_lld=None, maximum_immersion_depth=None, surface_following_distance_during_mix=None, tube_2nd_section_ratio=None, tube_2nd_section_height_measured_from_zm=None, **kwargs):
        _kw = {'aspiration_type': aspiration_type, 'x_position': x_position, 'x_direction': x_direction, 'y_positions': y_positions, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'min_z_endpos': min_z_endpos, 'lld_search_height': lld_search_height, 'liquid_surface_no_lld': liquid_surface_no_lld, 'pull_out_distance_transport_air': pull_out_distance_transport_air, 'minimum_height': minimum_height, 'second_section_height': second_section_height, 'second_section_ratio': second_section_ratio, 'immersion_depth': immersion_depth, 'immersion_depth_direction': immersion_depth_direction, 'surface_following_distance': surface_following_distance, 'aspiration_volumes': aspiration_volumes, 'aspiration_speed': aspiration_speed, 'transport_air_volume': transport_air_volume, 'blow_out_air_volume': blow_out_air_volume, 'pre_wetting_volume': pre_wetting_volume, 'lld_mode': lld_mode, 'gamma_lld_sensitivity': gamma_lld_sensitivity, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_from_liquid_surface': mix_position_from_liquid_surface, 'mix_surface_following_distance': mix_surface_following_distance, 'speed_of_mix': speed_of_mix, 'channel_pattern': channel_pattern, 'limit_curve_index': limit_curve_index, 'tadm_algorithm': tadm_algorithm, 'recording_mode': recording_mode, 'liquid_surface_sink_distance_at_the_end_of_aspiration': liquid_surface_sink_distance_at_the_end_of_aspiration, 'minimal_end_height': minimal_end_height, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'pull_out_distance_to_take_transport_air_in_function_without_lld': pull_out_distance_to_take_transport_air_in_function_without_lld, 'maximum_immersion_depth': maximum_immersion_depth, 'surface_following_distance_during_mix': surface_following_distance_during_mix, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm}
        _kw.update(kwargs)
        return self.call('aspirate_core_96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def aspirate_pip(self, aspiration_type=None, tip_pattern=None, x_positions=None, y_positions=None, minimum_traverse_height_at_beginning_of_a_command=None, min_z_endpos=None, lld_search_height=None, clot_detection_height=None, liquid_surface_no_lld=None, pull_out_distance_transport_air=None, second_section_height=None, second_section_ratio=None, minimum_height=None, immersion_depth=None, immersion_depth_direction=None, surface_following_distance=None, aspiration_volumes=None, aspiration_speed=None, transport_air_volume=None, blow_out_air_volume=None, pre_wetting_volume=None, lld_mode=None, gamma_lld_sensitivity=None, dp_lld_sensitivity=None, aspirate_position_above_z_touch_off=None, detection_height_difference_for_dual_lld=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_from_liquid_surface=None, mix_speed=None, mix_surface_following_distance=None, limit_curve_index=None, tadm_algorithm=None, recording_mode=None, use_2nd_section_aspiration=None, retract_height_over_2nd_section_to_empty_tip=None, dispensation_speed_during_emptying_tip=None, dosing_drive_speed_during_2nd_section_search=None, z_drive_speed_during_2nd_section_search=None, cup_upper_edge=None, ratio_liquid_rise_to_tip_deep_in=None, immersion_depth_2nd_section=None, **kwargs):
        _kw = {'aspiration_type': aspiration_type, 'tip_pattern': tip_pattern, 'x_positions': x_positions, 'y_positions': y_positions, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'min_z_endpos': min_z_endpos, 'lld_search_height': lld_search_height, 'clot_detection_height': clot_detection_height, 'liquid_surface_no_lld': liquid_surface_no_lld, 'pull_out_distance_transport_air': pull_out_distance_transport_air, 'second_section_height': second_section_height, 'second_section_ratio': second_section_ratio, 'minimum_height': minimum_height, 'immersion_depth': immersion_depth, 'immersion_depth_direction': immersion_depth_direction, 'surface_following_distance': surface_following_distance, 'aspiration_volumes': aspiration_volumes, 'aspiration_speed': aspiration_speed, 'transport_air_volume': transport_air_volume, 'blow_out_air_volume': blow_out_air_volume, 'pre_wetting_volume': pre_wetting_volume, 'lld_mode': lld_mode, 'gamma_lld_sensitivity': gamma_lld_sensitivity, 'dp_lld_sensitivity': dp_lld_sensitivity, 'aspirate_position_above_z_touch_off': aspirate_position_above_z_touch_off, 'detection_height_difference_for_dual_lld': detection_height_difference_for_dual_lld, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_from_liquid_surface': mix_position_from_liquid_surface, 'mix_speed': mix_speed, 'mix_surface_following_distance': mix_surface_following_distance, 'limit_curve_index': limit_curve_index, 'tadm_algorithm': tadm_algorithm, 'recording_mode': recording_mode, 'use_2nd_section_aspiration': use_2nd_section_aspiration, 'retract_height_over_2nd_section_to_empty_tip': retract_height_over_2nd_section_to_empty_tip, 'dispensation_speed_during_emptying_tip': dispensation_speed_during_emptying_tip, 'dosing_drive_speed_during_2nd_section_search': dosing_drive_speed_during_2nd_section_search, 'z_drive_speed_during_2nd_section_search': z_drive_speed_during_2nd_section_search, 'cup_upper_edge': cup_upper_edge, 'ratio_liquid_rise_to_tip_deep_in': ratio_liquid_rise_to_tip_deep_in, 'immersion_depth_2nd_section': immersion_depth_2nd_section}
        _kw.update(kwargs)
        return self.call('aspirate_pip', kwargs={k: v for k, v in _kw.items() if v is not None})

    def can_pick_up_tip(self, channel_idx=None, tip=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'tip': tip}
        _kw.update(kwargs)
        return self.call('can_pick_up_tip', kwargs={k: v for k, v in _kw.items() if v is not None})

    def can_reach_position(self, channel_idx=None, position=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'position': position}
        _kw.update(kwargs)
        return self.call('can_reach_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def channel_dispensing_drive_move_to_volume_position(self, channel_idx=None, vol=None, flow_rate=None, acceleration=None, current_limit=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'vol': vol, 'flow_rate': flow_rate, 'acceleration': acceleration, 'current_limit': current_limit}
        _kw.update(kwargs)
        return self.call('channel_dispensing_drive_move_to_volume_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def channel_dispensing_drive_request_position(self, channel_idx=None, **kwargs):
        _kw = {'channel_idx': channel_idx}
        _kw.update(kwargs)
        return self.call('channel_dispensing_drive_request_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def channel_id(self, channel_idx=None, **kwargs):
        _kw = {'channel_idx': channel_idx}
        _kw.update(kwargs)
        return self.call('channel_id', kwargs={k: v for k, v in _kw.items() if v is not None})

    def channel_request_cycle_counts(self, channel_idx=None, **kwargs):
        _kw = {'channel_idx': channel_idx}
        _kw.update(kwargs)
        return self.call('channel_request_cycle_counts', kwargs={k: v for k, v in _kw.items() if v is not None})

    def channel_request_y_minimum_spacing(self, channel_idx=None, **kwargs):
        _kw = {'channel_idx': channel_idx}
        _kw.update(kwargs)
        return self.call('channel_request_y_minimum_spacing', kwargs={k: v for k, v in _kw.items() if v is not None})

    def channels_request_cycle_counts(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('channels_request_cycle_counts', kwargs={k: v for k, v in _kw.items() if v is not None})

    def channels_request_y_minimum_spacing(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('channels_request_y_minimum_spacing', kwargs={k: v for k, v in _kw.items() if v is not None})

    def channels_sense_tip_presence(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('channels_sense_tip_presence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def check_fw_string_error(self, resp=None, **kwargs):
        _kw = {'resp': resp}
        _kw.update(kwargs)
        return self.call('check_fw_string_error', kwargs={k: v for k, v in _kw.items() if v is not None})

    def check_type_is_hhc(self, device_number=None, **kwargs):
        _kw = {'device_number': device_number}
        _kw.update(kwargs)
        return self.call('check_type_is_hhc', kwargs={k: v for k, v in _kw.items() if v is not None})

    def clld_probe_x_position_using_channel(self, channel_idx=None, probing_direction=None, end_pos_search=None, post_detection_dist=None, tip_bottom_diameter=None, read_timeout=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'probing_direction': probing_direction, 'end_pos_search': end_pos_search, 'post_detection_dist': post_detection_dist, 'tip_bottom_diameter': tip_bottom_diameter, 'read_timeout': read_timeout}
        _kw.update(kwargs)
        return self.call('clld_probe_x_position_using_channel', kwargs={k: v for k, v in _kw.items() if v is not None})

    def clld_probe_y_position_using_channel(self, channel_idx=None, probing_direction=None, start_pos_search=None, end_pos_search=None, channel_speed=None, channel_acceleration_int=None, detection_edge=None, current_limit_int=None, post_detection_dist=None, tip_bottom_diameter=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'probing_direction': probing_direction, 'start_pos_search': start_pos_search, 'end_pos_search': end_pos_search, 'channel_speed': channel_speed, 'channel_acceleration_int': channel_acceleration_int, 'detection_edge': detection_edge, 'current_limit_int': current_limit_int, 'post_detection_dist': post_detection_dist, 'tip_bottom_diameter': tip_bottom_diameter}
        _kw.update(kwargs)
        return self.call('clld_probe_y_position_using_channel', kwargs={k: v for k, v in _kw.items() if v is not None})

    def clld_probe_z_height_using_channel(self, channel_idx=None, lowest_immers_pos=None, start_pos_search=None, channel_speed=None, channel_acceleration=None, detection_edge=None, detection_drop=None, post_detection_trajectory=None, post_detection_dist=None, move_channels_to_safe_pos_after=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'lowest_immers_pos': lowest_immers_pos, 'start_pos_search': start_pos_search, 'channel_speed': channel_speed, 'channel_acceleration': channel_acceleration, 'detection_edge': detection_edge, 'detection_drop': detection_drop, 'post_detection_trajectory': post_detection_trajectory, 'post_detection_dist': post_detection_dist, 'move_channels_to_safe_pos_after': move_channels_to_safe_pos_after}
        _kw.update(kwargs)
        return self.call('clld_probe_z_height_using_channel', kwargs={k: v for k, v in _kw.items() if v is not None})

    def collapse_gripper_arm(self, minimum_traverse_height_at_beginning_of_a_command=None, iswap_fold_up_sequence_at_the_end_of_process=None, **kwargs):
        _kw = {'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'iswap_fold_up_sequence_at_the_end_of_process': iswap_fold_up_sequence_at_the_end_of_process}
        _kw.update(kwargs)
        return self.call('collapse_gripper_arm', kwargs={k: v for k, v in _kw.items() if v is not None})

    def configure_node_names(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('configure_node_names', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core_check_resource_exists_at_location_center(self, location=None, resource=None, gripper_y_margin=None, offset=None, minimum_traverse_height_at_beginning_of_a_command=None, z_position_at_the_command_end=None, enable_recovery=None, audio_feedback=None, **kwargs):
        _kw = {'location': location, 'resource': resource, 'gripper_y_margin': gripper_y_margin, 'offset': offset, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'z_position_at_the_command_end': z_position_at_the_command_end, 'enable_recovery': enable_recovery, 'audio_feedback': audio_feedback}
        _kw.update(kwargs)
        return self.call('core_check_resource_exists_at_location_center', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core_get_plate(self, x_position=None, x_direction=None, y_position=None, y_gripping_speed=None, z_position=None, z_speed=None, open_gripper_position=None, plate_width=None, grip_strength=None, minimum_traverse_height_at_beginning_of_a_command=None, minimum_z_position_at_the_command_end=None, **kwargs):
        _kw = {'x_position': x_position, 'x_direction': x_direction, 'y_position': y_position, 'y_gripping_speed': y_gripping_speed, 'z_position': z_position, 'z_speed': z_speed, 'open_gripper_position': open_gripper_position, 'plate_width': plate_width, 'grip_strength': grip_strength, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'minimum_z_position_at_the_command_end': minimum_z_position_at_the_command_end}
        _kw.update(kwargs)
        return self.call('core_get_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core_move_picked_up_resource(self, center=None, minimum_traverse_height_at_beginning_of_a_command=None, acceleration_index=None, z_speed=None, **kwargs):
        _kw = {'center': center, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'acceleration_index': acceleration_index, 'z_speed': z_speed}
        _kw.update(kwargs)
        return self.call('core_move_picked_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core_move_plate_to_position(self, x_position=None, x_direction=None, x_acceleration_index=None, y_position=None, z_position=None, z_speed=None, minimum_traverse_height_at_beginning_of_a_command=None, **kwargs):
        _kw = {'x_position': x_position, 'x_direction': x_direction, 'x_acceleration_index': x_acceleration_index, 'y_position': y_position, 'z_position': z_position, 'z_speed': z_speed, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command}
        _kw.update(kwargs)
        return self.call('core_move_plate_to_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core_open_gripper(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('core_open_gripper', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core_pick_up_resource(self, resource=None, pickup_distance_from_top=None, offset=None, minimum_traverse_height_at_beginning_of_a_command=None, minimum_z_position_at_the_command_end=None, grip_strength=None, z_speed=None, y_gripping_speed=None, front_channel=None, **kwargs):
        _kw = {'resource': resource, 'pickup_distance_from_top': pickup_distance_from_top, 'offset': offset, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'minimum_z_position_at_the_command_end': minimum_z_position_at_the_command_end, 'grip_strength': grip_strength, 'z_speed': z_speed, 'y_gripping_speed': y_gripping_speed, 'front_channel': front_channel}
        _kw.update(kwargs)
        return self.call('core_pick_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core_put_plate(self, x_position=None, x_direction=None, y_position=None, z_position=None, z_press_on_distance=None, z_speed=None, open_gripper_position=None, minimum_traverse_height_at_beginning_of_a_command=None, z_position_at_the_command_end=None, return_tool=None, **kwargs):
        _kw = {'x_position': x_position, 'x_direction': x_direction, 'y_position': y_position, 'z_position': z_position, 'z_press_on_distance': z_press_on_distance, 'z_speed': z_speed, 'open_gripper_position': open_gripper_position, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'z_position_at_the_command_end': z_position_at_the_command_end, 'return_tool': return_tool}
        _kw.update(kwargs)
        return self.call('core_put_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core_read_barcode_of_picked_up_resource(self, rails=None, reading_direction=None, minimal_z_position=None, traverse_height_at_beginning_of_a_command=None, z_speed=None, allow_manual_input=None, labware_description=None, **kwargs):
        _kw = {'rails': rails, 'reading_direction': reading_direction, 'minimal_z_position': minimal_z_position, 'traverse_height_at_beginning_of_a_command': traverse_height_at_beginning_of_a_command, 'z_speed': z_speed, 'allow_manual_input': allow_manual_input, 'labware_description': labware_description}
        _kw.update(kwargs)
        return self.call('core_read_barcode_of_picked_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core_release_picked_up_resource(self, location=None, resource=None, pickup_distance_from_top=None, minimum_traverse_height_at_beginning_of_a_command=None, z_position_at_the_command_end=None, return_tool=None, **kwargs):
        _kw = {'location': location, 'resource': resource, 'pickup_distance_from_top': pickup_distance_from_top, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'z_position_at_the_command_end': z_position_at_the_command_end, 'return_tool': return_tool}
        _kw.update(kwargs)
        return self.call('core_release_picked_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def define_tip_needle(self, tip_type_table_index=None, has_filter=None, tip_length=None, maximum_tip_volume=None, tip_size=None, pickup_method=None, **kwargs):
        _kw = {'tip_type_table_index': tip_type_table_index, 'has_filter': has_filter, 'tip_length': tip_length, 'maximum_tip_volume': maximum_tip_volume, 'tip_size': tip_size, 'pickup_method': pickup_method}
        _kw.update(kwargs)
        return self.call('define_tip_needle', kwargs={k: v for k, v in _kw.items() if v is not None})

    def disable_cover_control(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('disable_cover_control', kwargs={k: v for k, v in _kw.items() if v is not None})

    def discard_tip(self, x_positions=None, y_positions=None, tip_pattern=None, begin_tip_deposit_process=None, end_tip_deposit_process=None, minimum_traverse_height_at_beginning_of_a_command=None, z_position_at_end_of_a_command=None, discarding_method=None, **kwargs):
        _kw = {'x_positions': x_positions, 'y_positions': y_positions, 'tip_pattern': tip_pattern, 'begin_tip_deposit_process': begin_tip_deposit_process, 'end_tip_deposit_process': end_tip_deposit_process, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'z_position_at_end_of_a_command': z_position_at_end_of_a_command, 'discarding_method': discarding_method}
        _kw.update(kwargs)
        return self.call('discard_tip', kwargs={k: v for k, v in _kw.items() if v is not None})

    def discard_tips_core96(self, x_position=None, x_direction=None, y_position=None, z_deposit_position=None, minimum_traverse_height_at_beginning_of_a_command=None, minimum_height_command_end=None, **kwargs):
        _kw = {'x_position': x_position, 'x_direction': x_direction, 'y_position': y_position, 'z_deposit_position': z_deposit_position, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'minimum_height_command_end': minimum_height_command_end}
        _kw.update(kwargs)
        return self.call('discard_tips_core96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispense(self, ops=None, use_channels=None, lld_search_height=None, liquid_surface_no_lld=None, pull_out_distance_transport_air=None, second_section_height=None, second_section_ratio=None, minimum_height=None, immersion_depth=None, surface_following_distance=None, cut_off_speed=None, stop_back_volume=None, transport_air_volume=None, lld_mode=None, dispense_position_above_z_touch_off=None, gamma_lld_sensitivity=None, dp_lld_sensitivity=None, swap_speed=None, settling_time=None, mix_position_from_liquid_surface=None, mix_surface_following_distance=None, limit_curve_index=None, minimum_traverse_height_at_beginning_of_a_command=None, min_z_endpos=None, side_touch_off_distance=None, jet=None, blow_out=None, empty=None, probe_liquid_height=None, auto_surface_following_distance=None, hamilton_liquid_classes=None, disable_volume_correction=None, immersion_depth_direction=None, mix_volume=None, mix_cycles=None, mix_speed=None, dispensing_mode=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'lld_search_height': lld_search_height, 'liquid_surface_no_lld': liquid_surface_no_lld, 'pull_out_distance_transport_air': pull_out_distance_transport_air, 'second_section_height': second_section_height, 'second_section_ratio': second_section_ratio, 'minimum_height': minimum_height, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'cut_off_speed': cut_off_speed, 'stop_back_volume': stop_back_volume, 'transport_air_volume': transport_air_volume, 'lld_mode': lld_mode, 'dispense_position_above_z_touch_off': dispense_position_above_z_touch_off, 'gamma_lld_sensitivity': gamma_lld_sensitivity, 'dp_lld_sensitivity': dp_lld_sensitivity, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_position_from_liquid_surface': mix_position_from_liquid_surface, 'mix_surface_following_distance': mix_surface_following_distance, 'limit_curve_index': limit_curve_index, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'min_z_endpos': min_z_endpos, 'side_touch_off_distance': side_touch_off_distance, 'jet': jet, 'blow_out': blow_out, 'empty': empty, 'probe_liquid_height': probe_liquid_height, 'auto_surface_following_distance': auto_surface_following_distance, 'hamilton_liquid_classes': hamilton_liquid_classes, 'disable_volume_correction': disable_volume_correction, 'immersion_depth_direction': immersion_depth_direction, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_speed': mix_speed, 'dispensing_mode': dispensing_mode}
        _kw.update(kwargs)
        return self.call('dispense', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispense96(self, dispense=None, jet=None, empty=None, blow_out=None, hlc=None, pull_out_distance_transport_air=None, use_lld=None, minimum_traverse_height_at_beginning_of_a_command=None, min_z_endpos=None, lld_search_height=None, minimum_height=None, second_section_height=None, second_section_ratio=None, immersion_depth=None, surface_following_distance=None, transport_air_volume=None, gamma_lld_sensitivity=None, swap_speed=None, settling_time=None, mix_position_from_liquid_surface=None, mix_surface_following_distance=None, limit_curve_index=None, cut_off_speed=None, stop_back_volume=None, disable_volume_correction=None, liquid_surface_sink_distance_at_the_end_of_dispense=None, maximum_immersion_depth=None, minimal_end_height=None, mixing_position_from_liquid_surface=None, surface_following_distance_during_mixing=None, air_transport_retract_dist=None, tube_2nd_section_ratio=None, tube_2nd_section_height_measured_from_zm=None, immersion_depth_direction=None, mixing_volume=None, mixing_cycles=None, speed_of_mixing=None, dispense_mode=None, **kwargs):
        _kw = {'dispense': dispense, 'jet': jet, 'empty': empty, 'blow_out': blow_out, 'hlc': hlc, 'pull_out_distance_transport_air': pull_out_distance_transport_air, 'use_lld': use_lld, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'min_z_endpos': min_z_endpos, 'lld_search_height': lld_search_height, 'minimum_height': minimum_height, 'second_section_height': second_section_height, 'second_section_ratio': second_section_ratio, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'transport_air_volume': transport_air_volume, 'gamma_lld_sensitivity': gamma_lld_sensitivity, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_position_from_liquid_surface': mix_position_from_liquid_surface, 'mix_surface_following_distance': mix_surface_following_distance, 'limit_curve_index': limit_curve_index, 'cut_off_speed': cut_off_speed, 'stop_back_volume': stop_back_volume, 'disable_volume_correction': disable_volume_correction, 'liquid_surface_sink_distance_at_the_end_of_dispense': liquid_surface_sink_distance_at_the_end_of_dispense, 'maximum_immersion_depth': maximum_immersion_depth, 'minimal_end_height': minimal_end_height, 'mixing_position_from_liquid_surface': mixing_position_from_liquid_surface, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'air_transport_retract_dist': air_transport_retract_dist, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm, 'immersion_depth_direction': immersion_depth_direction, 'mixing_volume': mixing_volume, 'mixing_cycles': mixing_cycles, 'speed_of_mixing': speed_of_mixing, 'dispense_mode': dispense_mode}
        _kw.update(kwargs)
        return self.call('dispense96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispense_core_96(self, dispensing_mode=None, x_position=None, x_direction=None, y_position=None, second_section_height=None, second_section_ratio=None, lld_search_height=None, liquid_surface_no_lld=None, pull_out_distance_transport_air=None, minimum_height=None, immersion_depth=None, immersion_depth_direction=None, surface_following_distance=None, minimum_traverse_height_at_beginning_of_a_command=None, min_z_endpos=None, dispense_volume=None, dispense_speed=None, cut_off_speed=None, stop_back_volume=None, transport_air_volume=None, blow_out_air_volume=None, lld_mode=None, gamma_lld_sensitivity=None, side_touch_off_distance=None, swap_speed=None, settling_time=None, mixing_volume=None, mixing_cycles=None, mix_position_from_liquid_surface=None, mix_surface_following_distance=None, speed_of_mixing=None, channel_pattern=None, limit_curve_index=None, tadm_algorithm=None, recording_mode=None, liquid_surface_sink_distance_at_the_end_of_dispense=None, tube_2nd_section_ratio=None, liquid_surface_at_function_without_lld=None, maximum_immersion_depth=None, minimal_end_height=None, mixing_position_from_liquid_surface=None, surface_following_distance_during_mixing=None, pull_out_distance_to_take_transport_air_in_function_without_lld=None, tube_2nd_section_height_measured_from_zm=None, **kwargs):
        _kw = {'dispensing_mode': dispensing_mode, 'x_position': x_position, 'x_direction': x_direction, 'y_position': y_position, 'second_section_height': second_section_height, 'second_section_ratio': second_section_ratio, 'lld_search_height': lld_search_height, 'liquid_surface_no_lld': liquid_surface_no_lld, 'pull_out_distance_transport_air': pull_out_distance_transport_air, 'minimum_height': minimum_height, 'immersion_depth': immersion_depth, 'immersion_depth_direction': immersion_depth_direction, 'surface_following_distance': surface_following_distance, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'min_z_endpos': min_z_endpos, 'dispense_volume': dispense_volume, 'dispense_speed': dispense_speed, 'cut_off_speed': cut_off_speed, 'stop_back_volume': stop_back_volume, 'transport_air_volume': transport_air_volume, 'blow_out_air_volume': blow_out_air_volume, 'lld_mode': lld_mode, 'gamma_lld_sensitivity': gamma_lld_sensitivity, 'side_touch_off_distance': side_touch_off_distance, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mixing_volume': mixing_volume, 'mixing_cycles': mixing_cycles, 'mix_position_from_liquid_surface': mix_position_from_liquid_surface, 'mix_surface_following_distance': mix_surface_following_distance, 'speed_of_mixing': speed_of_mixing, 'channel_pattern': channel_pattern, 'limit_curve_index': limit_curve_index, 'tadm_algorithm': tadm_algorithm, 'recording_mode': recording_mode, 'liquid_surface_sink_distance_at_the_end_of_dispense': liquid_surface_sink_distance_at_the_end_of_dispense, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'maximum_immersion_depth': maximum_immersion_depth, 'minimal_end_height': minimal_end_height, 'mixing_position_from_liquid_surface': mixing_position_from_liquid_surface, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'pull_out_distance_to_take_transport_air_in_function_without_lld': pull_out_distance_to_take_transport_air_in_function_without_lld, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm}
        _kw.update(kwargs)
        return self.call('dispense_core_96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispense_pip(self, tip_pattern=None, dispensing_mode=None, x_positions=None, y_positions=None, minimum_height=None, lld_search_height=None, liquid_surface_no_lld=None, pull_out_distance_transport_air=None, immersion_depth=None, immersion_depth_direction=None, surface_following_distance=None, second_section_height=None, second_section_ratio=None, minimum_traverse_height_at_beginning_of_a_command=None, min_z_endpos=None, dispense_volumes=None, dispense_speed=None, cut_off_speed=None, stop_back_volume=None, transport_air_volume=None, blow_out_air_volume=None, lld_mode=None, side_touch_off_distance=None, dispense_position_above_z_touch_off=None, gamma_lld_sensitivity=None, dp_lld_sensitivity=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_from_liquid_surface=None, mix_speed=None, mix_surface_following_distance=None, limit_curve_index=None, tadm_algorithm=None, recording_mode=None, **kwargs):
        _kw = {'tip_pattern': tip_pattern, 'dispensing_mode': dispensing_mode, 'x_positions': x_positions, 'y_positions': y_positions, 'minimum_height': minimum_height, 'lld_search_height': lld_search_height, 'liquid_surface_no_lld': liquid_surface_no_lld, 'pull_out_distance_transport_air': pull_out_distance_transport_air, 'immersion_depth': immersion_depth, 'immersion_depth_direction': immersion_depth_direction, 'surface_following_distance': surface_following_distance, 'second_section_height': second_section_height, 'second_section_ratio': second_section_ratio, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'min_z_endpos': min_z_endpos, 'dispense_volumes': dispense_volumes, 'dispense_speed': dispense_speed, 'cut_off_speed': cut_off_speed, 'stop_back_volume': stop_back_volume, 'transport_air_volume': transport_air_volume, 'blow_out_air_volume': blow_out_air_volume, 'lld_mode': lld_mode, 'side_touch_off_distance': side_touch_off_distance, 'dispense_position_above_z_touch_off': dispense_position_above_z_touch_off, 'gamma_lld_sensitivity': gamma_lld_sensitivity, 'dp_lld_sensitivity': dp_lld_sensitivity, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_from_liquid_surface': mix_position_from_liquid_surface, 'mix_speed': mix_speed, 'mix_surface_following_distance': mix_surface_following_distance, 'limit_curve_index': limit_curve_index, 'tadm_algorithm': tadm_algorithm, 'recording_mode': recording_mode}
        _kw.update(kwargs)
        return self.call('dispense_pip', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispensing_drive_increment_to_mm(self, position_increment=None, **kwargs):
        _kw = {'position_increment': position_increment}
        _kw.update(kwargs)
        return self.call('dispensing_drive_increment_to_mm', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispensing_drive_increment_to_volume(self, position_increment=None, **kwargs):
        _kw = {'position_increment': position_increment}
        _kw.update(kwargs)
        return self.call('dispensing_drive_increment_to_volume', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispensing_drive_mm_to_increment(self, position_mm=None, **kwargs):
        _kw = {'position_mm': position_mm}
        _kw.update(kwargs)
        return self.call('dispensing_drive_mm_to_increment', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispensing_drive_mm_to_vol(self, position_mm=None, **kwargs):
        _kw = {'position_mm': position_mm}
        _kw.update(kwargs)
        return self.call('dispensing_drive_mm_to_vol', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispensing_drive_vol_to_increment(self, volume=None, **kwargs):
        _kw = {'volume': volume}
        _kw.update(kwargs)
        return self.call('dispensing_drive_vol_to_increment', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispensing_drive_vol_to_mm(self, vol=None, **kwargs):
        _kw = {'vol': vol}
        _kw.update(kwargs)
        return self.call('dispensing_drive_vol_to_mm', kwargs={k: v for k, v in _kw.items() if v is not None})

    def drain_dual_chamber_system(self, pump_station=None, **kwargs):
        _kw = {'pump_station': pump_station}
        _kw.update(kwargs)
        return self.call('drain_dual_chamber_system', kwargs={k: v for k, v in _kw.items() if v is not None})

    def drop_resource(self, drop=None, use_arm=None, return_core_gripper=None, minimum_traverse_height_at_beginning_of_a_command=None, z_position_at_the_command_end=None, open_gripper_position=None, hotel_depth=None, hotel_clearance_height=None, hotel_high_speed=None, use_unsafe_hotel=None, iswap_collision_control_level=None, iswap_fold_up_sequence_at_the_end_of_process=None, **kwargs):
        _kw = {'drop': drop, 'use_arm': use_arm, 'return_core_gripper': return_core_gripper, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'z_position_at_the_command_end': z_position_at_the_command_end, 'open_gripper_position': open_gripper_position, 'hotel_depth': hotel_depth, 'hotel_clearance_height': hotel_clearance_height, 'hotel_high_speed': hotel_high_speed, 'use_unsafe_hotel': use_unsafe_hotel, 'iswap_collision_control_level': iswap_collision_control_level, 'iswap_fold_up_sequence_at_the_end_of_process': iswap_fold_up_sequence_at_the_end_of_process}
        _kw.update(kwargs)
        return self.call('drop_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def drop_tips(self, ops=None, use_channels=None, drop_method=None, begin_tip_deposit_process=None, end_tip_deposit_process=None, minimum_traverse_height_at_beginning_of_a_command=None, z_position_at_end_of_a_command=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'drop_method': drop_method, 'begin_tip_deposit_process': begin_tip_deposit_process, 'end_tip_deposit_process': end_tip_deposit_process, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'z_position_at_end_of_a_command': z_position_at_end_of_a_command}
        _kw.update(kwargs)
        return self.call('drop_tips', kwargs={k: v for k, v in _kw.items() if v is not None})

    def drop_tips96(self, drop=None, minimum_height_command_end=None, minimum_traverse_height_at_beginning_of_a_command=None, experimental_alignment_tipspot_identifier=None, **kwargs):
        _kw = {'drop': drop, 'minimum_height_command_end': minimum_height_command_end, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'experimental_alignment_tipspot_identifier': experimental_alignment_tipspot_identifier}
        _kw.update(kwargs)
        return self.call('drop_tips96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def empty_tip(self, channel_idx=None, vol=None, flow_rate=None, acceleration=None, current_limit=None, reset_dispensing_drive_after=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'vol': vol, 'flow_rate': flow_rate, 'acceleration': acceleration, 'current_limit': current_limit, 'reset_dispensing_drive_after': reset_dispensing_drive_after}
        _kw.update(kwargs)
        return self.call('empty_tip', kwargs={k: v for k, v in _kw.items() if v is not None})

    def empty_tips(self, channels=None, vol=None, flow_rate=None, acceleration=None, current_limit=None, reset_dispensing_drive_after=None, **kwargs):
        _kw = {'channels': channels, 'vol': vol, 'flow_rate': flow_rate, 'acceleration': acceleration, 'current_limit': current_limit, 'reset_dispensing_drive_after': reset_dispensing_drive_after}
        _kw.update(kwargs)
        return self.call('empty_tips', kwargs={k: v for k, v in _kw.items() if v is not None})

    def enable_cover_control(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('enable_cover_control', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ensure_can_reach_position(self, use_channels=None, ops=None, op_name=None, **kwargs):
        _kw = {'use_channels': use_channels, 'ops': ops, 'op_name': op_name}
        _kw.update(kwargs)
        return self.call('ensure_can_reach_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def execute_batched(self, func=None, resources=None, use_channels=None, resource_offsets=None, min_traverse_height_during_command=None, **kwargs):
        _kw = {'func': func, 'resources': resources, 'use_channels': use_channels, 'resource_offsets': resource_offsets, 'min_traverse_height_during_command': min_traverse_height_during_command}
        _kw.update(kwargs)
        return self.call('execute_batched', kwargs={k: v for k, v in _kw.items() if v is not None})

    def fill_selected_dual_chamber(self, pump_station=None, drain_before_refill=None, wash_fluid=None, chamber=None, waste_chamber_suck_time_after_sensor_change=None, **kwargs):
        _kw = {'pump_station': pump_station, 'drain_before_refill': drain_before_refill, 'wash_fluid': wash_fluid, 'chamber': chamber, 'waste_chamber_suck_time_after_sensor_change': waste_chamber_suck_time_after_sensor_change}
        _kw.update(kwargs)
        return self.call('fill_selected_dual_chamber', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_channel_spacings(self, use_channels=None, **kwargs):
        _kw = {'use_channels': use_channels}
        _kw.update(kwargs)
        return self.call('get_channel_spacings', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_channels_y_positions(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_channels_y_positions', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_channels_z_positions(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_channels_z_positions', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_core(self, p1=None, p2=None, **kwargs):
        _kw = {'p1': p1, 'p2': p2}
        _kw.update(kwargs)
        return self.call('get_core', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_id_from_fw_response(self, resp=None, **kwargs):
        _kw = {'resp': resp}
        _kw.update(kwargs)
        return self.call('get_id_from_fw_response', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_iswap_version(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_iswap_version', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_logic_iswap_position(self, x_position=None, x_direction=None, y_position=None, y_direction=None, z_position=None, z_direction=None, location=None, hotel_depth=None, grip_direction=None, collision_control_level=None, **kwargs):
        _kw = {'x_position': x_position, 'x_direction': x_direction, 'y_position': y_position, 'y_direction': y_direction, 'z_position': z_position, 'z_direction': z_direction, 'location': location, 'hotel_depth': hotel_depth, 'grip_direction': grip_direction, 'collision_control_level': collision_control_level}
        _kw.update(kwargs)
        return self.call('get_logic_iswap_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_or_assign_tip_type_index(self, tip=None, **kwargs):
        _kw = {'tip': tip}
        _kw.update(kwargs)
        return self.call('get_or_assign_tip_type_index', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_temperature_at_hhc(self, device_number=None, **kwargs):
        _kw = {'device_number': device_number}
        _kw.update(kwargs)
        return self.call('get_temperature_at_hhc', kwargs={k: v for k, v in _kw.items() if v is not None})

    def halt(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('halt', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_dispensing_drive_and_squeezer_driver_initialize(self, squeezer_speed=None, squeezer_acceleration=None, squeezer_current_limit=None, dispensing_drive_current_limit=None, **kwargs):
        _kw = {'squeezer_speed': squeezer_speed, 'squeezer_acceleration': squeezer_acceleration, 'squeezer_current_limit': squeezer_current_limit, 'dispensing_drive_current_limit': dispensing_drive_current_limit}
        _kw.update(kwargs)
        return self.call('head96_dispensing_drive_and_squeezer_driver_initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_dispensing_drive_move_to_home_volume(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('head96_dispensing_drive_move_to_home_volume', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_dispensing_drive_move_to_position(self, position=None, speed=None, stop_speed=None, acceleration=None, current_protection_limiter=None, **kwargs):
        _kw = {'position': position, 'speed': speed, 'stop_speed': stop_speed, 'acceleration': acceleration, 'current_protection_limiter': current_protection_limiter}
        _kw.update(kwargs)
        return self.call('head96_dispensing_drive_move_to_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_dispensing_drive_request_position_mm(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('head96_dispensing_drive_request_position_mm', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_dispensing_drive_request_position_uL(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('head96_dispensing_drive_request_position_uL', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_move_to_coordinate(self, coordinate=None, minimum_height_at_beginning_of_a_command=None, **kwargs):
        _kw = {'coordinate': coordinate, 'minimum_height_at_beginning_of_a_command': minimum_height_at_beginning_of_a_command}
        _kw.update(kwargs)
        return self.call('head96_move_to_coordinate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_move_to_z_safety(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('head96_move_to_z_safety', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_move_x(self, x=None, **kwargs):
        _kw = {'x': x}
        _kw.update(kwargs)
        return self.call('head96_move_x', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_move_y(self, y=None, speed=None, acceleration=None, current_protection_limiter=None, **kwargs):
        _kw = {'y': y, 'speed': speed, 'acceleration': acceleration, 'current_protection_limiter': current_protection_limiter}
        _kw.update(kwargs)
        return self.call('head96_move_y', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_move_z(self, z=None, speed=None, acceleration=None, current_protection_limiter=None, **kwargs):
        _kw = {'z': z, 'speed': speed, 'acceleration': acceleration, 'current_protection_limiter': current_protection_limiter}
        _kw.update(kwargs)
        return self.call('head96_move_z', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_park(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('head96_park', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_request_firmware_version(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('head96_request_firmware_version', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_request_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('head96_request_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_request_tip_presence(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('head96_request_tip_presence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def head96_request_type(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('head96_request_type', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize_auto_load(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('initialize_auto_load', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize_autoload(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('initialize_autoload', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize_core_96_head(self, trash96=None, z_position_at_the_command_end=None, **kwargs):
        _kw = {'trash96': trash96, 'z_position_at_the_command_end': z_position_at_the_command_end}
        _kw.update(kwargs)
        return self.call('initialize_core_96_head', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize_dual_pump_station_valves(self, pump_station=None, **kwargs):
        _kw = {'pump_station': pump_station}
        _kw.update(kwargs)
        return self.call('initialize_dual_pump_station_valves', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize_hhc(self, device_number=None, **kwargs):
        _kw = {'device_number': device_number}
        _kw.update(kwargs)
        return self.call('initialize_hhc', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize_iswap(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('initialize_iswap', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize_pip(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('initialize_pip', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize_pipetting_channels(self, x_positions=None, y_positions=None, begin_of_tip_deposit_process=None, end_of_tip_deposit_process=None, z_position_at_end_of_a_command=None, tip_pattern=None, tip_type=None, discarding_method=None, **kwargs):
        _kw = {'x_positions': x_positions, 'y_positions': y_positions, 'begin_of_tip_deposit_process': begin_of_tip_deposit_process, 'end_of_tip_deposit_process': end_of_tip_deposit_process, 'z_position_at_end_of_a_command': z_position_at_end_of_a_command, 'tip_pattern': tip_pattern, 'tip_type': tip_type, 'discarding_method': discarding_method}
        _kw.update(kwargs)
        return self.call('initialize_pipetting_channels', kwargs={k: v for k, v in _kw.items() if v is not None})

    def iswap_close_gripper(self, grip_strength=None, plate_width=None, plate_width_tolerance=None, **kwargs):
        _kw = {'grip_strength': grip_strength, 'plate_width': plate_width, 'plate_width_tolerance': plate_width_tolerance}
        _kw.update(kwargs)
        return self.call('iswap_close_gripper', kwargs={k: v for k, v in _kw.items() if v is not None})

    def iswap_dangerous_release_break(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('iswap_dangerous_release_break', kwargs={k: v for k, v in _kw.items() if v is not None})

    def iswap_get_plate(self, x_position=None, x_direction=None, y_position=None, y_direction=None, z_position=None, z_direction=None, grip_direction=None, minimum_traverse_height_at_beginning_of_a_command=None, z_position_at_the_command_end=None, grip_strength=None, open_gripper_position=None, plate_width=None, plate_width_tolerance=None, collision_control_level=None, acceleration_index_high_acc=None, acceleration_index_low_acc=None, iswap_fold_up_sequence_at_the_end_of_process=None, **kwargs):
        _kw = {'x_position': x_position, 'x_direction': x_direction, 'y_position': y_position, 'y_direction': y_direction, 'z_position': z_position, 'z_direction': z_direction, 'grip_direction': grip_direction, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'z_position_at_the_command_end': z_position_at_the_command_end, 'grip_strength': grip_strength, 'open_gripper_position': open_gripper_position, 'plate_width': plate_width, 'plate_width_tolerance': plate_width_tolerance, 'collision_control_level': collision_control_level, 'acceleration_index_high_acc': acceleration_index_high_acc, 'acceleration_index_low_acc': acceleration_index_low_acc, 'iswap_fold_up_sequence_at_the_end_of_process': iswap_fold_up_sequence_at_the_end_of_process}
        _kw.update(kwargs)
        return self.call('iswap_get_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def iswap_initialize_z_axis(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('iswap_initialize_z_axis', kwargs={k: v for k, v in _kw.items() if v is not None})

    def iswap_minimum_traversal_height(self, traversal_height=None, **kwargs):
        _kw = {'traversal_height': traversal_height}
        _kw.update(kwargs)
        return self.call('iswap_minimum_traversal_height', kwargs={k: v for k, v in _kw.items() if v is not None})

    def iswap_move_picked_up_resource(self, center=None, grip_direction=None, minimum_traverse_height_at_beginning_of_a_command=None, collision_control_level=None, acceleration_index_high_acc=None, acceleration_index_low_acc=None, **kwargs):
        _kw = {'center': center, 'grip_direction': grip_direction, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'collision_control_level': collision_control_level, 'acceleration_index_high_acc': acceleration_index_high_acc, 'acceleration_index_low_acc': acceleration_index_low_acc}
        _kw.update(kwargs)
        return self.call('iswap_move_picked_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def iswap_open_gripper(self, open_position=None, **kwargs):
        _kw = {'open_position': open_position}
        _kw.update(kwargs)
        return self.call('iswap_open_gripper', kwargs={k: v for k, v in _kw.items() if v is not None})

    def iswap_put_plate(self, x_position=None, x_direction=None, y_position=None, y_direction=None, z_position=None, z_direction=None, grip_direction=None, minimum_traverse_height_at_beginning_of_a_command=None, z_position_at_the_command_end=None, open_gripper_position=None, collision_control_level=None, acceleration_index_high_acc=None, acceleration_index_low_acc=None, iswap_fold_up_sequence_at_the_end_of_process=None, **kwargs):
        _kw = {'x_position': x_position, 'x_direction': x_direction, 'y_position': y_position, 'y_direction': y_direction, 'z_position': z_position, 'z_direction': z_direction, 'grip_direction': grip_direction, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'z_position_at_the_command_end': z_position_at_the_command_end, 'open_gripper_position': open_gripper_position, 'collision_control_level': collision_control_level, 'acceleration_index_high_acc': acceleration_index_high_acc, 'acceleration_index_low_acc': acceleration_index_low_acc, 'iswap_fold_up_sequence_at_the_end_of_process': iswap_fold_up_sequence_at_the_end_of_process}
        _kw.update(kwargs)
        return self.call('iswap_put_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def iswap_reengage_break(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('iswap_reengage_break', kwargs={k: v for k, v in _kw.items() if v is not None})

    def iswap_rotate(self, rotation_drive=None, grip_direction=None, gripper_velocity=None, gripper_acceleration=None, gripper_protection=None, wrist_velocity=None, wrist_acceleration=None, wrist_protection=None, **kwargs):
        _kw = {'rotation_drive': rotation_drive, 'grip_direction': grip_direction, 'gripper_velocity': gripper_velocity, 'gripper_acceleration': gripper_acceleration, 'gripper_protection': gripper_protection, 'wrist_velocity': wrist_velocity, 'wrist_acceleration': wrist_acceleration, 'wrist_protection': wrist_protection}
        _kw.update(kwargs)
        return self.call('iswap_rotate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def iswap_rotation_drive_request_y(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('iswap_rotation_drive_request_y', kwargs={k: v for k, v in _kw.items() if v is not None})

    def load_carrier(self, carrier=None, carrier_barcode_reading=None, barcode_reading=None, barcode_reading_direction=None, barcode_symbology=None, no_container_per_carrier=None, reading_position_of_first_barcode=None, distance_between_containers=None, width_of_reading_window=None, reading_speed=None, park_autoload_after=None, **kwargs):
        _kw = {'carrier': carrier, 'carrier_barcode_reading': carrier_barcode_reading, 'barcode_reading': barcode_reading, 'barcode_reading_direction': barcode_reading_direction, 'barcode_symbology': barcode_symbology, 'no_container_per_carrier': no_container_per_carrier, 'reading_position_of_first_barcode': reading_position_of_first_barcode, 'distance_between_containers': distance_between_containers, 'width_of_reading_window': width_of_reading_window, 'reading_speed': reading_speed, 'park_autoload_after': park_autoload_after}
        _kw.update(kwargs)
        return self.call('load_carrier', kwargs={k: v for k, v in _kw.items() if v is not None})

    def load_carrier_from_autoload_belt(self, barcode_reading=None, barcode_reading_direction=None, barcode_symbology=None, reading_position_of_first_barcode=None, no_container_per_carrier=None, distance_between_containers=None, width_of_reading_window=None, reading_speed=None, park_autoload_after=None, **kwargs):
        _kw = {'barcode_reading': barcode_reading, 'barcode_reading_direction': barcode_reading_direction, 'barcode_symbology': barcode_symbology, 'reading_position_of_first_barcode': reading_position_of_first_barcode, 'no_container_per_carrier': no_container_per_carrier, 'distance_between_containers': distance_between_containers, 'width_of_reading_window': width_of_reading_window, 'reading_speed': reading_speed, 'park_autoload_after': park_autoload_after}
        _kw.update(kwargs)
        return self.call('load_carrier_from_autoload_belt', kwargs={k: v for k, v in _kw.items() if v is not None})

    def load_carrier_from_tray_and_scan_carrier_barcode(self, carrier=None, carrier_barcode_reading=None, barcode_symbology=None, barcode_position=None, barcode_reading_window_width=None, reading_speed=None, **kwargs):
        _kw = {'carrier': carrier, 'carrier_barcode_reading': carrier_barcode_reading, 'barcode_symbology': barcode_symbology, 'barcode_position': barcode_position, 'barcode_reading_window_width': barcode_reading_window_width, 'reading_speed': reading_speed}
        _kw.update(kwargs)
        return self.call('load_carrier_from_tray_and_scan_carrier_barcode', kwargs={k: v for k, v in _kw.items() if v is not None})

    def lock_cover(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('lock_cover', kwargs={k: v for k, v in _kw.items() if v is not None})

    def mm_to_y_drive_increment(self, value_mm=None, **kwargs):
        _kw = {'value_mm': value_mm}
        _kw.update(kwargs)
        return self.call('mm_to_y_drive_increment', kwargs={k: v for k, v in _kw.items() if v is not None})

    def mm_to_z_drive_increment(self, value_mm=None, **kwargs):
        _kw = {'value_mm': value_mm}
        _kw.update(kwargs)
        return self.call('mm_to_z_drive_increment', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_96head_to_coordinate(self, coordinate=None, minimum_height_at_beginning_of_a_command=None, **kwargs):
        _kw = {'coordinate': coordinate, 'minimum_height_at_beginning_of_a_command': minimum_height_at_beginning_of_a_command}
        _kw.update(kwargs)
        return self.call('move_96head_to_coordinate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_all_channels_in_z_safety(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('move_all_channels_in_z_safety', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_all_pipetting_channels_to_defined_position(self, tip_pattern=None, x_positions=None, y_positions=None, minimum_traverse_height_at_beginning_of_command=None, z_endpos=None, **kwargs):
        _kw = {'tip_pattern': tip_pattern, 'x_positions': x_positions, 'y_positions': y_positions, 'minimum_traverse_height_at_beginning_of_command': minimum_traverse_height_at_beginning_of_command, 'z_endpos': z_endpos}
        _kw.update(kwargs)
        return self.call('move_all_pipetting_channels_to_defined_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_auto_load_to_z_save_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('move_auto_load_to_z_save_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_autoload_to_safe_z_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('move_autoload_to_safe_z_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_autoload_to_save_z_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('move_autoload_to_save_z_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_autoload_to_slot(self, slot_number=None, **kwargs):
        _kw = {'slot_number': slot_number}
        _kw.update(kwargs)
        return self.call('move_autoload_to_slot', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_autoload_to_track(self, track=None, **kwargs):
        _kw = {'track': track}
        _kw.update(kwargs)
        return self.call('move_autoload_to_track', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_channel_stop_disk_z(self, channel_idx=None, z=None, speed=None, acceleration=None, current_limit=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'z': z, 'speed': speed, 'acceleration': acceleration, 'current_limit': current_limit}
        _kw.update(kwargs)
        return self.call('move_channel_stop_disk_z', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_channel_tool_z(self, channel_idx=None, z=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'z': z}
        _kw.update(kwargs)
        return self.call('move_channel_tool_z', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_channel_x(self, channel=None, x=None, **kwargs):
        _kw = {'channel': channel, 'x': x}
        _kw.update(kwargs)
        return self.call('move_channel_x', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_channel_x_relative(self, channel=None, distance=None, **kwargs):
        _kw = {'channel': channel, 'distance': distance}
        _kw.update(kwargs)
        return self.call('move_channel_x_relative', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_channel_y(self, channel=None, y=None, **kwargs):
        _kw = {'channel': channel, 'y': y}
        _kw.update(kwargs)
        return self.call('move_channel_y', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_channel_y_relative(self, channel=None, distance=None, **kwargs):
        _kw = {'channel': channel, 'distance': distance}
        _kw.update(kwargs)
        return self.call('move_channel_y_relative', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_channel_z(self, channel=None, z=None, **kwargs):
        _kw = {'channel': channel, 'z': z}
        _kw.update(kwargs)
        return self.call('move_channel_z', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_channel_z_relative(self, channel=None, distance=None, **kwargs):
        _kw = {'channel': channel, 'distance': distance}
        _kw.update(kwargs)
        return self.call('move_channel_z_relative', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_core_96_head_to_defined_position(self, x=None, y=None, z=None, minimum_height_at_beginning_of_a_command=None, **kwargs):
        _kw = {'x': x, 'y': y, 'z': z, 'minimum_height_at_beginning_of_a_command': minimum_height_at_beginning_of_a_command}
        _kw.update(kwargs)
        return self.call('move_core_96_head_to_defined_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_core_96_head_x(self, x_position=None, **kwargs):
        _kw = {'x_position': x_position}
        _kw.update(kwargs)
        return self.call('move_core_96_head_x', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_core_96_head_y(self, y_position=None, **kwargs):
        _kw = {'y_position': y_position}
        _kw.update(kwargs)
        return self.call('move_core_96_head_y', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_core_96_head_z(self, z_position=None, **kwargs):
        _kw = {'z_position': z_position}
        _kw.update(kwargs)
        return self.call('move_core_96_head_z', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_core_96_to_safe_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('move_core_96_to_safe_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_iswap_x(self, x_position=None, **kwargs):
        _kw = {'x_position': x_position}
        _kw.update(kwargs)
        return self.call('move_iswap_x', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_iswap_x_relative(self, step_size=None, allow_splitting=None, **kwargs):
        _kw = {'step_size': step_size, 'allow_splitting': allow_splitting}
        _kw.update(kwargs)
        return self.call('move_iswap_x_relative', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_iswap_y(self, y_position=None, **kwargs):
        _kw = {'y_position': y_position}
        _kw.update(kwargs)
        return self.call('move_iswap_y', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_iswap_y_relative(self, step_size=None, allow_splitting=None, **kwargs):
        _kw = {'step_size': step_size, 'allow_splitting': allow_splitting}
        _kw.update(kwargs)
        return self.call('move_iswap_y_relative', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_iswap_z(self, z_position=None, **kwargs):
        _kw = {'z_position': z_position}
        _kw.update(kwargs)
        return self.call('move_iswap_z', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_iswap_z_relative(self, step_size=None, allow_splitting=None, **kwargs):
        _kw = {'step_size': step_size, 'allow_splitting': allow_splitting}
        _kw.update(kwargs)
        return self.call('move_iswap_z_relative', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_left_x_arm_to_position_with_all_attached_components_in_z_safety_position(self, x_position=None, **kwargs):
        _kw = {'x_position': x_position}
        _kw.update(kwargs)
        return self.call('move_left_x_arm_to_position_with_all_attached_components_in_z_safety_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_picked_up_resource(self, move=None, use_arm=None, **kwargs):
        _kw = {'move': move, 'use_arm': use_arm}
        _kw.update(kwargs)
        return self.call('move_picked_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_plate_to_position(self, x_position=None, x_direction=None, y_position=None, y_direction=None, z_position=None, z_direction=None, grip_direction=None, minimum_traverse_height_at_beginning_of_a_command=None, collision_control_level=None, acceleration_index_high_acc=None, acceleration_index_low_acc=None, **kwargs):
        _kw = {'x_position': x_position, 'x_direction': x_direction, 'y_position': y_position, 'y_direction': y_direction, 'z_position': z_position, 'z_direction': z_direction, 'grip_direction': grip_direction, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'collision_control_level': collision_control_level, 'acceleration_index_high_acc': acceleration_index_high_acc, 'acceleration_index_low_acc': acceleration_index_low_acc}
        _kw.update(kwargs)
        return self.call('move_plate_to_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_right_x_arm_to_position_with_all_attached_components_in_z_safety_position(self, x_position=None, **kwargs):
        _kw = {'x_position': x_position}
        _kw.update(kwargs)
        return self.call('move_right_x_arm_to_position_with_all_attached_components_in_z_safety_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def occupy_and_provide_area_for_external_access(self, taken_area_identification_number=None, taken_area_left_margin=None, taken_area_left_margin_direction=None, taken_area_size=None, arm_preposition_mode_related_to_taken_areas=None, **kwargs):
        _kw = {'taken_area_identification_number': taken_area_identification_number, 'taken_area_left_margin': taken_area_left_margin, 'taken_area_left_margin_direction': taken_area_left_margin_direction, 'taken_area_size': taken_area_size, 'arm_preposition_mode_related_to_taken_areas': arm_preposition_mode_related_to_taken_areas}
        _kw.update(kwargs)
        return self.call('occupy_and_provide_area_for_external_access', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open_not_initialized_gripper(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open_not_initialized_gripper', kwargs={k: v for k, v in _kw.items() if v is not None})

    def park_autoload(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('park_autoload', kwargs={k: v for k, v in _kw.items() if v is not None})

    def park_iswap(self, minimum_traverse_height_at_beginning_of_a_command=None, **kwargs):
        _kw = {'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command}
        _kw.update(kwargs)
        return self.call('park_iswap', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_core_gripper_tools(self, front_channel=None, front_offset=None, back_offset=None, **kwargs):
        _kw = {'front_channel': front_channel, 'front_offset': front_offset, 'back_offset': back_offset}
        _kw.update(kwargs)
        return self.call('pick_up_core_gripper_tools', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_resource(self, pickup=None, use_arm=None, core_front_channel=None, iswap_grip_strength=None, core_grip_strength=None, minimum_traverse_height_at_beginning_of_a_command=None, z_position_at_the_command_end=None, plate_width_tolerance=None, open_gripper_position=None, hotel_depth=None, hotel_clearance_height=None, high_speed=None, plate_width=None, use_unsafe_hotel=None, iswap_collision_control_level=None, iswap_fold_up_sequence_at_the_end_of_process=None, channel_1=None, channel_2=None, **kwargs):
        _kw = {'pickup': pickup, 'use_arm': use_arm, 'core_front_channel': core_front_channel, 'iswap_grip_strength': iswap_grip_strength, 'core_grip_strength': core_grip_strength, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'z_position_at_the_command_end': z_position_at_the_command_end, 'plate_width_tolerance': plate_width_tolerance, 'open_gripper_position': open_gripper_position, 'hotel_depth': hotel_depth, 'hotel_clearance_height': hotel_clearance_height, 'high_speed': high_speed, 'plate_width': plate_width, 'use_unsafe_hotel': use_unsafe_hotel, 'iswap_collision_control_level': iswap_collision_control_level, 'iswap_fold_up_sequence_at_the_end_of_process': iswap_fold_up_sequence_at_the_end_of_process, 'channel_1': channel_1, 'channel_2': channel_2}
        _kw.update(kwargs)
        return self.call('pick_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_tip(self, x_positions=None, y_positions=None, tip_pattern=None, tip_type_idx=None, begin_tip_pick_up_process=None, end_tip_pick_up_process=None, minimum_traverse_height_at_beginning_of_a_command=None, pickup_method=None, **kwargs):
        _kw = {'x_positions': x_positions, 'y_positions': y_positions, 'tip_pattern': tip_pattern, 'tip_type_idx': tip_type_idx, 'begin_tip_pick_up_process': begin_tip_pick_up_process, 'end_tip_pick_up_process': end_tip_pick_up_process, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'pickup_method': pickup_method}
        _kw.update(kwargs)
        return self.call('pick_up_tip', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_tips(self, ops=None, use_channels=None, begin_tip_pick_up_process=None, end_tip_pick_up_process=None, minimum_traverse_height_at_beginning_of_a_command=None, pickup_method=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'begin_tip_pick_up_process': begin_tip_pick_up_process, 'end_tip_pick_up_process': end_tip_pick_up_process, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'pickup_method': pickup_method}
        _kw.update(kwargs)
        return self.call('pick_up_tips', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_tips96(self, pickup=None, tip_pickup_method=None, minimum_height_command_end=None, minimum_traverse_height_at_beginning_of_a_command=None, experimental_alignment_tipspot_identifier=None, **kwargs):
        _kw = {'pickup': pickup, 'tip_pickup_method': tip_pickup_method, 'minimum_height_command_end': minimum_height_command_end, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'experimental_alignment_tipspot_identifier': experimental_alignment_tipspot_identifier}
        _kw.update(kwargs)
        return self.call('pick_up_tips96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_tips_core96(self, x_position=None, x_direction=None, y_position=None, tip_type_idx=None, tip_pickup_method=None, z_deposit_position=None, minimum_traverse_height_at_beginning_of_a_command=None, minimum_height_command_end=None, **kwargs):
        _kw = {'x_position': x_position, 'x_direction': x_direction, 'y_position': y_position, 'tip_type_idx': tip_type_idx, 'tip_pickup_method': tip_pickup_method, 'z_deposit_position': z_deposit_position, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'minimum_height_command_end': minimum_height_command_end}
        _kw.update(kwargs)
        return self.call('pick_up_tips_core96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pierce_foil(self, wells=None, piercing_channels=None, hold_down_channels=None, move_inwards=None, spread=None, one_by_one=None, distance_from_bottom=None, **kwargs):
        _kw = {'wells': wells, 'piercing_channels': piercing_channels, 'hold_down_channels': hold_down_channels, 'move_inwards': move_inwards, 'spread': spread, 'one_by_one': one_by_one, 'distance_from_bottom': distance_from_bottom}
        _kw.update(kwargs)
        return self.call('pierce_foil', kwargs={k: v for k, v in _kw.items() if v is not None})

    def plld_probe_z_height_using_channel(self, channel_idx=None, lowest_immers_pos=None, start_pos_search=None, channel_speed_above_start_pos_search=None, channel_speed=None, channel_acceleration=None, z_drive_current_limit=None, tip_has_filter=None, dispense_drive_speed=None, dispense_drive_acceleration=None, dispense_drive_max_speed=None, dispense_drive_current_limit=None, plld_detection_edge=None, plld_detection_drop=None, clld_verification=None, clld_detection_edge=None, clld_detection_drop=None, max_delta_plld_clld=None, plld_mode=None, plld_foam_detection_drop=None, plld_foam_detection_edge_tolerance=None, plld_foam_ad_values=None, plld_foam_search_speed=None, dispense_back_plld_volume=None, post_detection_trajectory=None, post_detection_dist=None, move_channels_to_safe_pos_after=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'lowest_immers_pos': lowest_immers_pos, 'start_pos_search': start_pos_search, 'channel_speed_above_start_pos_search': channel_speed_above_start_pos_search, 'channel_speed': channel_speed, 'channel_acceleration': channel_acceleration, 'z_drive_current_limit': z_drive_current_limit, 'tip_has_filter': tip_has_filter, 'dispense_drive_speed': dispense_drive_speed, 'dispense_drive_acceleration': dispense_drive_acceleration, 'dispense_drive_max_speed': dispense_drive_max_speed, 'dispense_drive_current_limit': dispense_drive_current_limit, 'plld_detection_edge': plld_detection_edge, 'plld_detection_drop': plld_detection_drop, 'clld_verification': clld_verification, 'clld_detection_edge': clld_detection_edge, 'clld_detection_drop': clld_detection_drop, 'max_delta_plld_clld': max_delta_plld_clld, 'plld_mode': plld_mode, 'plld_foam_detection_drop': plld_foam_detection_drop, 'plld_foam_detection_edge_tolerance': plld_foam_detection_edge_tolerance, 'plld_foam_ad_values': plld_foam_ad_values, 'plld_foam_search_speed': plld_foam_search_speed, 'dispense_back_plld_volume': dispense_back_plld_volume, 'post_detection_trajectory': post_detection_trajectory, 'post_detection_dist': post_detection_dist, 'move_channels_to_safe_pos_after': move_channels_to_safe_pos_after}
        _kw.update(kwargs)
        return self.call('plld_probe_z_height_using_channel', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_channels_in_y_direction(self, ys=None, make_space=None, **kwargs):
        _kw = {'ys': ys, 'make_space': make_space}
        _kw.update(kwargs)
        return self.call('position_channels_in_y_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_channels_in_z_direction(self, zs=None, **kwargs):
        _kw = {'zs': zs}
        _kw.update(kwargs)
        return self.call('position_channels_in_z_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_components_for_free_iswap_y_range(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('position_components_for_free_iswap_y_range', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_left_x_arm_(self, x_position=None, **kwargs):
        _kw = {'x_position': x_position}
        _kw.update(kwargs)
        return self.call('position_left_x_arm_', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_max_free_y_for_n(self, pipetting_channel_index=None, **kwargs):
        _kw = {'pipetting_channel_index': pipetting_channel_index}
        _kw.update(kwargs)
        return self.call('position_max_free_y_for_n', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_right_x_arm_(self, x_position=None, **kwargs):
        _kw = {'x_position': x_position}
        _kw.update(kwargs)
        return self.call('position_right_x_arm_', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_single_pipetting_channel_in_y_direction(self, pipetting_channel_index=None, y_position=None, **kwargs):
        _kw = {'pipetting_channel_index': pipetting_channel_index, 'y_position': y_position}
        _kw.update(kwargs)
        return self.call('position_single_pipetting_channel_in_y_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_single_pipetting_channel_in_z_direction(self, pipetting_channel_index=None, z_position=None, **kwargs):
        _kw = {'pipetting_channel_index': pipetting_channel_index, 'z_position': z_position}
        _kw.update(kwargs)
        return self.call('position_single_pipetting_channel_in_z_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pre_initialize_instrument(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('pre_initialize_instrument', kwargs={k: v for k, v in _kw.items() if v is not None})

    def prepare_for_manual_channel_operation(self, channel=None, **kwargs):
        _kw = {'channel': channel}
        _kw.update(kwargs)
        return self.call('prepare_for_manual_channel_operation', kwargs={k: v for k, v in _kw.items() if v is not None})

    def prepare_iswap_teaching(self, x_position=None, x_direction=None, y_position=None, y_direction=None, z_position=None, z_direction=None, location=None, hotel_depth=None, grip_direction=None, minimum_traverse_height_at_beginning_of_a_command=None, collision_control_level=None, acceleration_index_high_acc=None, acceleration_index_low_acc=None, **kwargs):
        _kw = {'x_position': x_position, 'x_direction': x_direction, 'y_position': y_position, 'y_direction': y_direction, 'z_position': z_position, 'z_direction': z_direction, 'location': location, 'hotel_depth': hotel_depth, 'grip_direction': grip_direction, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'collision_control_level': collision_control_level, 'acceleration_index_high_acc': acceleration_index_high_acc, 'acceleration_index_low_acc': acceleration_index_low_acc}
        _kw.update(kwargs)
        return self.call('prepare_iswap_teaching', kwargs={k: v for k, v in _kw.items() if v is not None})

    def probe_liquid_heights(self, containers=None, use_channels=None, resource_offsets=None, lld_mode=None, search_speed=None, n_replicates=None, min_traverse_height_at_beginning_of_command=None, min_traverse_height_during_command=None, z_position_at_end_of_command=None, move_to_z_safety_after=None, **kwargs):
        _kw = {'containers': containers, 'use_channels': use_channels, 'resource_offsets': resource_offsets, 'lld_mode': lld_mode, 'search_speed': search_speed, 'n_replicates': n_replicates, 'min_traverse_height_at_beginning_of_command': min_traverse_height_at_beginning_of_command, 'min_traverse_height_during_command': min_traverse_height_during_command, 'z_position_at_end_of_command': z_position_at_end_of_command, 'move_to_z_safety_after': move_to_z_safety_after}
        _kw.update(kwargs)
        return self.call('probe_liquid_heights', kwargs={k: v for k, v in _kw.items() if v is not None})

    def probe_liquid_volumes(self, containers=None, use_channels=None, resource_offsets=None, lld_mode=None, search_speed=None, n_replicates=None, move_to_z_safety_after=None, **kwargs):
        _kw = {'containers': containers, 'use_channels': use_channels, 'resource_offsets': resource_offsets, 'lld_mode': lld_mode, 'search_speed': search_speed, 'n_replicates': n_replicates, 'move_to_z_safety_after': move_to_z_safety_after}
        _kw.update(kwargs)
        return self.call('probe_liquid_volumes', kwargs={k: v for k, v in _kw.items() if v is not None})

    def put_core(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('put_core', kwargs={k: v for k, v in _kw.items() if v is not None})

    def query_whether_temperature_reached_at_hhc(self, device_number=None, **kwargs):
        _kw = {'device_number': device_number}
        _kw.update(kwargs)
        return self.call('query_whether_temperature_reached_at_hhc', kwargs={k: v for k, v in _kw.items() if v is not None})

    def release_all_occupied_areas(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('release_all_occupied_areas', kwargs={k: v for k, v in _kw.items() if v is not None})

    def release_occupied_area(self, taken_area_identification_number=None, **kwargs):
        _kw = {'taken_area_identification_number': taken_area_identification_number}
        _kw.update(kwargs)
        return self.call('release_occupied_area', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_additional_timestamp_data(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_additional_timestamp_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_auto_load_slot_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_auto_load_slot_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_autoload_initialization_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_autoload_initialization_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_autoload_track(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_autoload_track', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_autoload_type(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_autoload_type', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_core_96_head_channel_tadm_error_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_core_96_head_channel_tadm_error_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_core_96_head_channel_tadm_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_core_96_head_channel_tadm_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_core_96_head_initialization_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_core_96_head_initialization_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_cover_open(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_cover_open', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_deck_data(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_deck_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_device_serial_number(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_device_serial_number', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_download_date(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_download_date', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_eeprom_data_correctness(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_eeprom_data_correctness', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_electronic_board_type(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_electronic_board_type', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_error_code(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_error_code', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_extended_configuration(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_extended_configuration', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_firmware_version(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_firmware_version', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_installation_data(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_installation_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_instrument_initialization_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_instrument_initialization_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_iswap_in_parking_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_iswap_in_parking_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_iswap_initialization_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_iswap_initialization_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_iswap_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_iswap_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_iswap_rotation_drive_orientation(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_iswap_rotation_drive_orientation', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_iswap_rotation_drive_position_increments(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_iswap_rotation_drive_position_increments', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_iswap_version(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_iswap_version', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_iswap_wrist_drive_orientation(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_iswap_wrist_drive_orientation', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_iswap_wrist_drive_position_increments(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_iswap_wrist_drive_position_increments', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_left_x_arm_last_collision_type(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_left_x_arm_last_collision_type', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_left_x_arm_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_left_x_arm_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_machine_configuration(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_machine_configuration', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_master_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_master_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_maximal_ranges_of_x_drives(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_maximal_ranges_of_x_drives', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_name_of_last_faulty_parameter(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_name_of_last_faulty_parameter', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_node_names(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_node_names', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_number_of_presence_sensors_installed(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_number_of_presence_sensors_installed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_parameter_value(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_parameter_value', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_pip_channel_validation_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_pip_channel_validation_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_pip_channel_version(self, channel=None, **kwargs):
        _kw = {'channel': channel}
        _kw.update(kwargs)
        return self.call('request_pip_channel_version', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_pip_height_last_lld(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_pip_height_last_lld', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_plate_in_iswap(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_plate_in_iswap', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_position_of_core_96_head(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_position_of_core_96_head', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_presence_of_carriers_on_deck(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_presence_of_carriers_on_deck', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_presence_of_carriers_on_loading_tray(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_presence_of_carriers_on_loading_tray', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_presence_of_single_carrier_on_loading_tray(self, track=None, **kwargs):
        _kw = {'track': track}
        _kw.update(kwargs)
        return self.call('request_presence_of_single_carrier_on_loading_tray', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_present_wrap_size_of_installed_arms(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_present_wrap_size_of_installed_arms', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_probe_z_position(self, channel_idx=None, **kwargs):
        _kw = {'channel_idx': channel_idx}
        _kw.update(kwargs)
        return self.call('request_probe_z_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_pump_settings(self, pump_station=None, **kwargs):
        _kw = {'pump_station': pump_station}
        _kw.update(kwargs)
        return self.call('request_pump_settings', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_right_x_arm_last_collision_type(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_right_x_arm_last_collision_type', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_right_x_arm_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_right_x_arm_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_single_carrier_presence(self, carrier_position=None, **kwargs):
        _kw = {'carrier_position': carrier_position}
        _kw.update(kwargs)
        return self.call('request_single_carrier_presence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_supply_voltage(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_supply_voltage', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_tadm_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_tadm_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_technical_status_of_assemblies(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_technical_status_of_assemblies', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_tip_bottom_z_position(self, channel_idx=None, **kwargs):
        _kw = {'channel_idx': channel_idx}
        _kw.update(kwargs)
        return self.call('request_tip_bottom_z_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_tip_len_on_channel(self, channel_idx=None, **kwargs):
        _kw = {'channel_idx': channel_idx}
        _kw.update(kwargs)
        return self.call('request_tip_len_on_channel', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_tip_presence(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_tip_presence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_tip_presence_in_core_96_head(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_tip_presence_in_core_96_head', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_verification_data(self, verification_subject=None, **kwargs):
        _kw = {'verification_subject': verification_subject}
        _kw.update(kwargs)
        return self.call('request_verification_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_volume_in_tip(self, channel=None, **kwargs):
        _kw = {'channel': channel}
        _kw.update(kwargs)
        return self.call('request_volume_in_tip', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_x_pos_channel_n(self, pipetting_channel_index=None, **kwargs):
        _kw = {'pipetting_channel_index': pipetting_channel_index}
        _kw.update(kwargs)
        return self.call('request_x_pos_channel_n', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_xl_channel_validation_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_xl_channel_validation_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_y_pos_channel_n(self, pipetting_channel_index=None, **kwargs):
        _kw = {'pipetting_channel_index': pipetting_channel_index}
        _kw.update(kwargs)
        return self.call('request_y_pos_channel_n', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_z_pos_channel_n(self, pipetting_channel_index=None, **kwargs):
        _kw = {'pipetting_channel_index': pipetting_channel_index}
        _kw.update(kwargs)
        return self.call('request_z_pos_channel_n', kwargs={k: v for k, v in _kw.items() if v is not None})

    def reset_output(self, output=None, **kwargs):
        _kw = {'output': output}
        _kw.update(kwargs)
        return self.call('reset_output', kwargs={k: v for k, v in _kw.items() if v is not None})

    def return_core_gripper_tools(self, front_offset=None, back_offset=None, **kwargs):
        _kw = {'front_offset': front_offset, 'back_offset': back_offset}
        _kw.update(kwargs)
        return self.call('return_core_gripper_tools', kwargs={k: v for k, v in _kw.items() if v is not None})

    def rotate_iswap_rotation_drive(self, orientation=None, **kwargs):
        _kw = {'orientation': orientation}
        _kw.update(kwargs)
        return self.call('rotate_iswap_rotation_drive', kwargs={k: v for k, v in _kw.items() if v is not None})

    def rotate_iswap_wrist(self, orientation=None, **kwargs):
        _kw = {'orientation': orientation}
        _kw.update(kwargs)
        return self.call('rotate_iswap_wrist', kwargs={k: v for k, v in _kw.items() if v is not None})

    def save_all_cycle_counters(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('save_all_cycle_counters', kwargs={k: v for k, v in _kw.items() if v is not None})

    def save_download_date(self, date=None, **kwargs):
        _kw = {'date': date}
        _kw.update(kwargs)
        return self.call('save_download_date', kwargs={k: v for k, v in _kw.items() if v is not None})

    def save_pip_channel_validation_status(self, validation_status=None, **kwargs):
        _kw = {'validation_status': validation_status}
        _kw.update(kwargs)
        return self.call('save_pip_channel_validation_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def save_technical_status_of_assemblies(self, processor_board=None, power_supply=None, **kwargs):
        _kw = {'processor_board': processor_board, 'power_supply': power_supply}
        _kw.update(kwargs)
        return self.call('save_technical_status_of_assemblies', kwargs={k: v for k, v in _kw.items() if v is not None})

    def save_xl_channel_validation_status(self, validation_status=None, **kwargs):
        _kw = {'validation_status': validation_status}
        _kw.update(kwargs)
        return self.call('save_xl_channel_validation_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def search_for_teach_in_signal_using_pipetting_channel_n_in_x_direction(self, pipetting_channel_index=None, x_position=None, **kwargs):
        _kw = {'pipetting_channel_index': pipetting_channel_index, 'x_position': x_position}
        _kw.update(kwargs)
        return self.call('search_for_teach_in_signal_using_pipetting_channel_n_in_x_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def send_hhs_command(self, index=None, command=None, **kwargs):
        _kw = {'index': index, 'command': command}
        _kw.update(kwargs)
        return self.call('send_hhs_command', kwargs={k: v for k, v in _kw.items() if v is not None})

    def send_raw_command(self, command=None, write_timeout=None, read_timeout=None, wait=None, **kwargs):
        _kw = {'command': command, 'write_timeout': write_timeout, 'read_timeout': read_timeout, 'wait': wait}
        _kw.update(kwargs)
        return self.call('send_raw_command', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_1d_barcode_type(self, barcode_symbology=None, **kwargs):
        _kw = {'barcode_symbology': barcode_symbology}
        _kw.update(kwargs)
        return self.call('set_1d_barcode_type', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_barcode_type(self, ISBT_Standard=None, code128=None, code39=None, codebar=None, code2_5=None, UPC_AE=None, EAN8=None, **kwargs):
        _kw = {'ISBT_Standard': ISBT_Standard, 'code128': code128, 'code39': code39, 'codebar': codebar, 'code2_5': code2_5, 'UPC_AE': UPC_AE, 'EAN8': EAN8}
        _kw.update(kwargs)
        return self.call('set_barcode_type', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_carrier_monitoring(self, should_monitor=None, **kwargs):
        _kw = {'should_monitor': should_monitor}
        _kw.update(kwargs)
        return self.call('set_carrier_monitoring', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_cover_output(self, output=None, **kwargs):
        _kw = {'output': output}
        _kw.update(kwargs)
        return self.call('set_cover_output', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_deck(self, deck=None, **kwargs):
        _kw = {'deck': deck}
        _kw.update(kwargs)
        return self.call('set_deck', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_deck_data(self, data_index=None, data_stream=None, **kwargs):
        _kw = {'data_index': data_index, 'data_stream': data_stream}
        _kw.update(kwargs)
        return self.call('set_deck_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_heads(self, head=None, head96=None, **kwargs):
        _kw = {'head': head, 'head96': head96}
        _kw.update(kwargs)
        return self.call('set_heads', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_instrument_configuration(self, configuration_data_1=None, configuration_data_2=None, configuration_data_3=None, instrument_size_in_slots_x_range=None, auto_load_size_in_slots=None, tip_waste_x_position=None, right_x_drive_configuration_byte_1=None, right_x_drive_configuration_byte_2=None, minimal_iswap_collision_free_position=None, maximal_iswap_collision_free_position=None, left_x_arm_width=None, right_x_arm_width=None, num_pip_channels=None, num_xl_channels=None, num_robotic_channels=None, minimal_raster_pitch_of_pip_channels=None, minimal_raster_pitch_of_xl_channels=None, minimal_raster_pitch_of_robotic_channels=None, pip_maximal_y_position=None, left_arm_minimal_y_position=None, right_arm_minimal_y_position=None, **kwargs):
        _kw = {'configuration_data_1': configuration_data_1, 'configuration_data_2': configuration_data_2, 'configuration_data_3': configuration_data_3, 'instrument_size_in_slots_x_range': instrument_size_in_slots_x_range, 'auto_load_size_in_slots': auto_load_size_in_slots, 'tip_waste_x_position': tip_waste_x_position, 'right_x_drive_configuration_byte_1': right_x_drive_configuration_byte_1, 'right_x_drive_configuration_byte_2': right_x_drive_configuration_byte_2, 'minimal_iswap_collision_free_position': minimal_iswap_collision_free_position, 'maximal_iswap_collision_free_position': maximal_iswap_collision_free_position, 'left_x_arm_width': left_x_arm_width, 'right_x_arm_width': right_x_arm_width, 'num_pip_channels': num_pip_channels, 'num_xl_channels': num_xl_channels, 'num_robotic_channels': num_robotic_channels, 'minimal_raster_pitch_of_pip_channels': minimal_raster_pitch_of_pip_channels, 'minimal_raster_pitch_of_xl_channels': minimal_raster_pitch_of_xl_channels, 'minimal_raster_pitch_of_robotic_channels': minimal_raster_pitch_of_robotic_channels, 'pip_maximal_y_position': pip_maximal_y_position, 'left_arm_minimal_y_position': left_arm_minimal_y_position, 'right_arm_minimal_y_position': right_arm_minimal_y_position}
        _kw.update(kwargs)
        return self.call('set_instrument_configuration', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_loading_indicators(self, bit_pattern=None, blink_pattern=None, **kwargs):
        _kw = {'bit_pattern': bit_pattern, 'blink_pattern': blink_pattern}
        _kw.update(kwargs)
        return self.call('set_loading_indicators', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_minimum_channel_traversal_height(self, traversal_height=None, **kwargs):
        _kw = {'traversal_height': traversal_height}
        _kw.update(kwargs)
        return self.call('set_minimum_channel_traversal_height', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_minimum_iswap_traversal_height(self, traversal_height=None, **kwargs):
        _kw = {'traversal_height': traversal_height}
        _kw.update(kwargs)
        return self.call('set_minimum_iswap_traversal_height', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_minimum_traversal_height(self, traversal_height=None, **kwargs):
        _kw = {'traversal_height': traversal_height}
        _kw.update(kwargs)
        return self.call('set_minimum_traversal_height', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_not_stop(self, non_stop=None, **kwargs):
        _kw = {'non_stop': non_stop}
        _kw.update(kwargs)
        return self.call('set_not_stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_single_step_mode(self, single_step_mode=None, **kwargs):
        _kw = {'single_step_mode': single_step_mode}
        _kw.update(kwargs)
        return self.call('set_single_step_mode', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_x_offset_x_axis_core_96_head(self, x_offset=None, **kwargs):
        _kw = {'x_offset': x_offset}
        _kw.update(kwargs)
        return self.call('set_x_offset_x_axis_core_96_head', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_x_offset_x_axis_core_nano_pipettor_head(self, x_offset=None, **kwargs):
        _kw = {'x_offset': x_offset}
        _kw.update(kwargs)
        return self.call('set_x_offset_x_axis_core_nano_pipettor_head', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_x_offset_x_axis_iswap(self, x_offset=None, **kwargs):
        _kw = {'x_offset': x_offset}
        _kw.update(kwargs)
        return self.call('set_x_offset_x_axis_iswap', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, skip_instrument_initialization=None, skip_pip=None, skip_autoload=None, skip_iswap=None, skip_core96_head=None, **kwargs):
        _kw = {'skip_instrument_initialization': skip_instrument_initialization, 'skip_pip': skip_pip, 'skip_autoload': skip_autoload, 'skip_iswap': skip_iswap, 'skip_core96_head': skip_core96_head}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def slow_iswap(self, wrist_velocity=None, gripper_velocity=None, **kwargs):
        _kw = {'wrist_velocity': wrist_velocity, 'gripper_velocity': gripper_velocity}
        _kw.update(kwargs)
        return self.call('slow_iswap', kwargs={k: v for k, v in _kw.items() if v is not None})

    def spread_pip_channels(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('spread_pip_channels', kwargs={k: v for k, v in _kw.items() if v is not None})

    def start_temperature_control_at_hhc(self, device_number=None, temp=None, **kwargs):
        _kw = {'device_number': device_number, 'temp': temp}
        _kw.update(kwargs)
        return self.call('start_temperature_control_at_hhc', kwargs={k: v for k, v in _kw.items() if v is not None})

    def step_off_foil(self, wells=None, front_channel=None, back_channel=None, move_inwards=None, move_height=None, **kwargs):
        _kw = {'wells': wells, 'front_channel': front_channel, 'back_channel': back_channel, 'move_inwards': move_inwards, 'move_height': move_height}
        _kw.update(kwargs)
        return self.call('step_off_foil', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_temperature_control_at_hhc(self, device_number=None, **kwargs):
        _kw = {'device_number': device_number}
        _kw.update(kwargs)
        return self.call('stop_temperature_control_at_hhc', kwargs={k: v for k, v in _kw.items() if v is not None})

    def store_installation_data(self, date=None, serial_number=None, **kwargs):
        _kw = {'date': date, 'serial_number': serial_number}
        _kw.update(kwargs)
        return self.call('store_installation_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def store_verification_data(self, verification_subject=None, date=None, verification_status=None, **kwargs):
        _kw = {'verification_subject': verification_subject, 'date': date, 'verification_status': verification_status}
        _kw.update(kwargs)
        return self.call('store_verification_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def take_carrier_out_to_autoload_belt(self, carrier=None, **kwargs):
        _kw = {'carrier': carrier}
        _kw.update(kwargs)
        return self.call('take_carrier_out_to_autoload_belt', kwargs={k: v for k, v in _kw.items() if v is not None})

    def trigger_next_step(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('trigger_next_step', kwargs={k: v for k, v in _kw.items() if v is not None})

    def unload_carrier(self, carrier=None, park_autoload_after=None, **kwargs):
        _kw = {'carrier': carrier, 'park_autoload_after': park_autoload_after}
        _kw.update(kwargs)
        return self.call('unload_carrier', kwargs={k: v for k, v in _kw.items() if v is not None})

    def unload_carrier_after_carrier_barcode_scanning(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('unload_carrier_after_carrier_barcode_scanning', kwargs={k: v for k, v in _kw.items() if v is not None})

    def unlock_cover(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('unlock_cover', kwargs={k: v for k, v in _kw.items() if v is not None})

    def verify_and_wait_for_carriers(self, check_interval=None, **kwargs):
        _kw = {'check_interval': check_interval}
        _kw.update(kwargs)
        return self.call('verify_and_wait_for_carriers', kwargs={k: v for k, v in _kw.items() if v is not None})

    def y_drive_increment_to_mm(self, value_mm=None, **kwargs):
        _kw = {'value_mm': value_mm}
        _kw.update(kwargs)
        return self.call('y_drive_increment_to_mm', kwargs={k: v for k, v in _kw.items() if v is not None})

    def z_drive_increment_to_mm(self, value_increments=None, **kwargs):
        _kw = {'value_increments': value_increments}
        _kw.update(kwargs)
        return self.call('z_drive_increment_to_mm', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ztouch_probe_z_height_using_channel(self, channel_idx=None, tip_len=None, lowest_immers_pos=None, start_pos_search=None, channel_speed=None, channel_acceleration=None, channel_speed_upwards=None, detection_limiter_in_PWM=None, push_down_force_in_PWM=None, post_detection_dist=None, move_channels_to_safe_pos_after=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'tip_len': tip_len, 'lowest_immers_pos': lowest_immers_pos, 'start_pos_search': start_pos_search, 'channel_speed': channel_speed, 'channel_acceleration': channel_acceleration, 'channel_speed_upwards': channel_speed_upwards, 'detection_limiter_in_PWM': detection_limiter_in_PWM, 'push_down_force_in_PWM': push_down_force_in_PWM, 'post_detection_dist': post_detection_dist, 'move_channels_to_safe_pos_after': move_channels_to_safe_pos_after}
        _kw.update(kwargs)
        return self.call('ztouch_probe_z_height_using_channel', kwargs={k: v for k, v in _kw.items() if v is not None})

