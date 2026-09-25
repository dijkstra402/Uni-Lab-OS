from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilentBenchcel(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/liquid_handling/backends/hamilton/STAR_backend.py', 'class_name': 'STARBackend', 'import_roots': [], 'candidate_methods': ['machine_conf', 'autoload_installed', 'iswap_installed', 'core96_head_installed', 'num_arms', 'head96_installed', 'unsafe', 'num_channels', 'set_minimum_traversal_height', 'set_minimum_channel_traversal_height', 'set_minimum_iswap_traversal_height', 'iswap_minimum_traversal_height', 'iswap_traversal_height', 'module_id_length', 'extended_conf', 'iswap_parked', 'core_parked', 'get_iswap_version', 'request_pip_channel_version', 'get_id_from_fw_response', 'check_fw_string_error', 'setup', 'stop', 'setup_done', 'channel_request_y_minimum_spacing', 'channels_request_y_minimum_spacing', 'can_reach_position', 'ensure_can_reach_position', 'channel_request_cycle_counts', 'channels_request_cycle_counts', 'pick_up_tips', 'drop_tips', 'execute_batched', 'probe_liquid_heights', 'probe_liquid_volumes', 'channel_dispensing_drive_request_position', 'channel_dispensing_drive_move_to_volume_position', 'empty_tip', 'empty_tips', 'aspirate', 'dispense', 'pick_up_tips96', 'drop_tips96', 'aspirate96', 'dispense96', 'iswap_move_picked_up_resource', 'core_pick_up_resource', 'core_move_picked_up_resource', 'core_release_picked_up_resource', 'pick_up_resource', 'move_picked_up_resource', 'drop_resource', 'prepare_for_manual_channel_operation', 'move_channel_x', 'move_channel_y', 'move_channel_z', 'move_channel_stop_disk_z', 'move_channel_tool_z', 'move_channel_x_relative', 'move_channel_y_relative', 'move_channel_z_relative', 'get_channel_spacings', 'can_pick_up_tip', 'core_check_resource_exists_at_location_center', 'pre_initialize_instrument', 'define_tip_needle', 'request_error_code', 'request_firmware_version', 'request_parameter_value', 'request_electronic_board_type', 'request_supply_voltage', 'request_instrument_initialization_status', 'request_autoload_initialization_status', 'request_name_of_last_faulty_parameter', 'request_master_status', 'request_number_of_presence_sensors_installed', 'request_eeprom_data_correctness', 'set_single_step_mode', 'trigger_next_step', 'halt', 'save_all_cycle_counters', 'set_not_stop', 'store_installation_data', 'store_verification_data', 'additional_time_stamp', 'set_x_offset_x_axis_iswap', 'set_x_offset_x_axis_core_96_head', 'set_x_offset_x_axis_core_nano_pipettor_head', 'save_download_date', 'save_technical_status_of_assemblies', 'set_instrument_configuration', 'save_pip_channel_validation_status', 'save_xl_channel_validation_status', 'configure_node_names', 'set_deck_data', 'request_technical_status_of_assemblies', 'request_installation_data', 'request_device_serial_number', 'request_download_date', 'request_verification_data', 'request_additional_timestamp_data', 'request_pip_channel_validation_status', 'request_xl_channel_validation_status', 'request_machine_configuration', 'request_extended_configuration', 'request_node_names', 'request_deck_data', 'position_left_x_arm_', 'position_right_x_arm_', 'move_left_x_arm_to_position_with_all_attached_components_in_z_safety_position', 'move_right_x_arm_to_position_with_all_attached_components_in_z_safety_position', 'occupy_and_provide_area_for_external_access', 'release_occupied_area', 'release_all_occupied_areas', 'request_left_x_arm_position', 'request_right_x_arm_position', 'request_maximal_ranges_of_x_drives', 'request_present_wrap_size_of_installed_arms', 'request_left_x_arm_last_collision_type', 'request_right_x_arm_last_collision_type', 'initialize_pip', 'initialize_pipetting_channels', 'pick_up_tip', 'discard_tip', 'aspirate_pip', 'dispense_pip', 'get_core', 'pick_up_core_gripper_tools', 'put_core', 'return_core_gripper_tools', 'core_open_gripper', 'core_get_plate', 'core_put_plate', 'core_move_plate_to_position', 'core_read_barcode_of_picked_up_resource', 'position_single_pipetting_channel_in_y_direction', 'position_single_pipetting_channel_in_z_direction', 'search_for_teach_in_signal_using_pipetting_channel_n_in_x_direction', 'spread_pip_channels', 'move_all_pipetting_channels_to_defined_position', 'position_max_free_y_for_n', 'move_all_channels_in_z_safety', 'request_x_pos_channel_n', 'request_y_pos_channel_n', 'request_z_pos_channel_n', 'request_tip_bottom_z_position', 'request_tip_presence', 'channels_sense_tip_presence', 'request_pip_height_last_lld', 'request_tadm_status', 'head96_request_firmware_version', 'head96_request_type', 'initialize_core_96_head', 'request_core_96_head_initialization_status', 'head96_dispensing_drive_and_squeezer_driver_initialize', 'move_core_96_to_safe_position', 'head96_move_to_z_safety', 'head96_park', 'head96_move_x', 'head96_move_y', 'head96_move_z', 'pick_up_tips_core96', 'discard_tips_core96', 'head96_dispensing_drive_move_to_home_volume', 'aspirate_core_96', 'dispense_core_96', 'move_core_96_head_to_defined_position', 'head96_move_to_coordinate', 'head96_dispensing_drive_move_to_position', 'move_core_96_head_x', 'move_core_96_head_y', 'move_core_96_head_z', 'move_96head_to_coordinate', 'request_tip_presence_in_core_96_head', 'head96_request_tip_presence', 'request_position_of_core_96_head', 'head96_request_position', 'request_core_96_head_channel_tadm_status', 'request_core_96_head_channel_tadm_error_status', 'head96_dispensing_drive_request_position_mm', 'head96_dispensing_drive_request_position_uL', 'initialize_auto_load', 'initialize_autoload', 'move_auto_load_to_z_save_position', 'move_autoload_to_save_z_position', 'move_autoload_to_safe_z_position', 'request_auto_load_slot_position', 'request_autoload_track', 'request_autoload_type', 'request_presence_of_carriers_on_deck', 'request_presence_of_carriers_on_loading_tray', 'request_presence_of_single_carrier_on_loading_tray', 'request_single_carrier_presence', 'move_autoload_to_slot', 'move_autoload_to_track', 'park_autoload', 'take_carrier_out_to_autoload_belt', 'set_1d_barcode_type', 'set_barcode_type', 'load_carrier_from_tray_and_scan_carrier_barcode', 'unload_carrier_after_carrier_barcode_scanning', 'set_carrier_monitoring', 'load_carrier_from_autoload_belt', 'load_carrier', 'set_loading_indicators', 'verify_and_wait_for_carriers', 'unload_carrier', 'request_pump_settings', 'initialize_dual_pump_station_valves', 'fill_selected_dual_chamber', 'drain_dual_chamber_system', 'initialize_iswap', 'position_components_for_free_iswap_y_range', 'move_iswap_x_relative', 'move_iswap_y_relative', 'move_iswap_z_relative', 'move_iswap_x', 'move_iswap_y', 'move_iswap_z', 'open_not_initialized_gripper', 'iswap_open_gripper', 'iswap_close_gripper', 'park_iswap', 'iswap_get_plate', 'iswap_put_plate', 'request_iswap_rotation_drive_position_increments', 'request_iswap_rotation_drive_orientation', 'request_iswap_wrist_drive_position_increments', 'request_iswap_wrist_drive_orientation', 'iswap_rotate', 'iswap_dangerous_release_break', 'iswap_reengage_break', 'iswap_initialize_z_axis', 'move_plate_to_position', 'collapse_gripper_arm', 'prepare_iswap_teaching', 'get_logic_iswap_position', 'request_iswap_in_parking_position', 'request_plate_in_iswap', 'request_iswap_position', 'iswap_rotation_drive_request_y', 'request_iswap_initialization_status', 'request_iswap_version', 'lock_cover', 'unlock_cover', 'disable_cover_control', 'enable_cover_control', 'set_cover_output', 'reset_output', 'request_cover_open', 'mm_to_y_drive_increment', 'y_drive_increment_to_mm', 'mm_to_z_drive_increment', 'z_drive_increment_to_mm', 'dispensing_drive_vol_to_increment', 'dispensing_drive_increment_to_volume', 'dispensing_drive_mm_to_increment', 'dispensing_drive_increment_to_mm', 'dispensing_drive_vol_to_mm', 'dispensing_drive_mm_to_vol', 'clld_probe_x_position_using_channel', 'clld_probe_y_position_using_channel', 'clld_probe_z_height_using_channel', 'plld_probe_z_height_using_channel', 'request_probe_z_position', 'request_tip_len_on_channel', 'ztouch_probe_z_height_using_channel', 'rotate_iswap_rotation_drive', 'rotate_iswap_wrist', 'channel_id', 'get_channels_y_positions', 'position_channels_in_y_direction', 'get_channels_z_positions', 'position_channels_in_z_direction', 'pierce_foil', 'step_off_foil', 'request_volume_in_tip', 'slow_iswap', 'send_hhs_command', 'check_type_is_hhc', 'initialize_hhc', 'start_temperature_control_at_hhc', 'get_temperature_at_hhc', 'query_whether_temperature_reached_at_hhc', 'stop_temperature_control_at_hhc', 'serialize', 'send_command', 'get_or_assign_tip_type_index', 'send_raw_command', 'set_deck', 'set_heads', 'deck', 'head', 'head96', 'deserialize', 'get_all_instances'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Agilent', 'model': 'BenchCel', 'device_type_cn': '耗材堆栈', 'device_type_en': 'Plate Storage', 'source_framework': 'PyLabRobot', 'tag_id': '4446', 'tag_name': '自动化耗材堆栈', 'tag_name_en': 'Automated Consumable Stack', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def machine_conf(self, **kwargs):
        return self.call('machine_conf', kwargs=kwargs)

    def autoload_installed(self, **kwargs):
        return self.call('autoload_installed', kwargs=kwargs)

    def iswap_installed(self, **kwargs):
        return self.call('iswap_installed', kwargs=kwargs)

    def core96_head_installed(self, **kwargs):
        return self.call('core96_head_installed', kwargs=kwargs)

    def num_arms(self, **kwargs):
        return self.call('num_arms', kwargs=kwargs)

    def head96_installed(self, **kwargs):
        return self.call('head96_installed', kwargs=kwargs)

    def unsafe(self, **kwargs):
        return self.call('unsafe', kwargs=kwargs)

    def num_channels(self, **kwargs):
        return self.call('num_channels', kwargs=kwargs)

    def set_minimum_traversal_height(self, **kwargs):
        return self.call('set_minimum_traversal_height', kwargs=kwargs)

    def set_minimum_channel_traversal_height(self, **kwargs):
        return self.call('set_minimum_channel_traversal_height', kwargs=kwargs)

    def set_minimum_iswap_traversal_height(self, **kwargs):
        return self.call('set_minimum_iswap_traversal_height', kwargs=kwargs)

    def iswap_minimum_traversal_height(self, **kwargs):
        return self.call('iswap_minimum_traversal_height', kwargs=kwargs)

    def iswap_traversal_height(self, **kwargs):
        return self.call('iswap_traversal_height', kwargs=kwargs)

    def module_id_length(self, **kwargs):
        return self.call('module_id_length', kwargs=kwargs)

    def extended_conf(self, **kwargs):
        return self.call('extended_conf', kwargs=kwargs)

    def iswap_parked(self, **kwargs):
        return self.call('iswap_parked', kwargs=kwargs)

    def core_parked(self, **kwargs):
        return self.call('core_parked', kwargs=kwargs)

    def get_iswap_version(self, **kwargs):
        return self.call('get_iswap_version', kwargs=kwargs)

    def request_pip_channel_version(self, **kwargs):
        return self.call('request_pip_channel_version', kwargs=kwargs)

    def get_id_from_fw_response(self, **kwargs):
        return self.call('get_id_from_fw_response', kwargs=kwargs)

    def check_fw_string_error(self, **kwargs):
        return self.call('check_fw_string_error', kwargs=kwargs)

    def setup(self, **kwargs):
        return self.call('setup', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def setup_done(self, **kwargs):
        return self.call('setup_done', kwargs=kwargs)

    def channel_request_y_minimum_spacing(self, **kwargs):
        return self.call('channel_request_y_minimum_spacing', kwargs=kwargs)

    def channels_request_y_minimum_spacing(self, **kwargs):
        return self.call('channels_request_y_minimum_spacing', kwargs=kwargs)

    def can_reach_position(self, **kwargs):
        return self.call('can_reach_position', kwargs=kwargs)

    def ensure_can_reach_position(self, **kwargs):
        return self.call('ensure_can_reach_position', kwargs=kwargs)

    def channel_request_cycle_counts(self, **kwargs):
        return self.call('channel_request_cycle_counts', kwargs=kwargs)

    def channels_request_cycle_counts(self, **kwargs):
        return self.call('channels_request_cycle_counts', kwargs=kwargs)

    def pick_up_tips(self, **kwargs):
        return self.call('pick_up_tips', kwargs=kwargs)

    def drop_tips(self, **kwargs):
        return self.call('drop_tips', kwargs=kwargs)

    def execute_batched(self, **kwargs):
        return self.call('execute_batched', kwargs=kwargs)

    def probe_liquid_heights(self, **kwargs):
        return self.call('probe_liquid_heights', kwargs=kwargs)

    def probe_liquid_volumes(self, **kwargs):
        return self.call('probe_liquid_volumes', kwargs=kwargs)

    def channel_dispensing_drive_request_position(self, **kwargs):
        return self.call('channel_dispensing_drive_request_position', kwargs=kwargs)

    def channel_dispensing_drive_move_to_volume_position(self, **kwargs):
        return self.call('channel_dispensing_drive_move_to_volume_position', kwargs=kwargs)

    def empty_tip(self, **kwargs):
        return self.call('empty_tip', kwargs=kwargs)

    def empty_tips(self, **kwargs):
        return self.call('empty_tips', kwargs=kwargs)

    def aspirate(self, **kwargs):
        return self.call('aspirate', kwargs=kwargs)

    def dispense(self, **kwargs):
        return self.call('dispense', kwargs=kwargs)

    def pick_up_tips96(self, **kwargs):
        return self.call('pick_up_tips96', kwargs=kwargs)

    def drop_tips96(self, **kwargs):
        return self.call('drop_tips96', kwargs=kwargs)

    def aspirate96(self, **kwargs):
        return self.call('aspirate96', kwargs=kwargs)

    def dispense96(self, **kwargs):
        return self.call('dispense96', kwargs=kwargs)

    def iswap_move_picked_up_resource(self, **kwargs):
        return self.call('iswap_move_picked_up_resource', kwargs=kwargs)

    def core_pick_up_resource(self, **kwargs):
        return self.call('core_pick_up_resource', kwargs=kwargs)

    def core_move_picked_up_resource(self, **kwargs):
        return self.call('core_move_picked_up_resource', kwargs=kwargs)

    def core_release_picked_up_resource(self, **kwargs):
        return self.call('core_release_picked_up_resource', kwargs=kwargs)

    def pick_up_resource(self, **kwargs):
        return self.call('pick_up_resource', kwargs=kwargs)

    def move_picked_up_resource(self, **kwargs):
        return self.call('move_picked_up_resource', kwargs=kwargs)

    def drop_resource(self, **kwargs):
        return self.call('drop_resource', kwargs=kwargs)

    def prepare_for_manual_channel_operation(self, **kwargs):
        return self.call('prepare_for_manual_channel_operation', kwargs=kwargs)

    def move_channel_x(self, **kwargs):
        return self.call('move_channel_x', kwargs=kwargs)

    def move_channel_y(self, **kwargs):
        return self.call('move_channel_y', kwargs=kwargs)

    def move_channel_z(self, **kwargs):
        return self.call('move_channel_z', kwargs=kwargs)

    def move_channel_stop_disk_z(self, **kwargs):
        return self.call('move_channel_stop_disk_z', kwargs=kwargs)

    def move_channel_tool_z(self, **kwargs):
        return self.call('move_channel_tool_z', kwargs=kwargs)

    def move_channel_x_relative(self, **kwargs):
        return self.call('move_channel_x_relative', kwargs=kwargs)

    def move_channel_y_relative(self, **kwargs):
        return self.call('move_channel_y_relative', kwargs=kwargs)

    def move_channel_z_relative(self, **kwargs):
        return self.call('move_channel_z_relative', kwargs=kwargs)

    def get_channel_spacings(self, **kwargs):
        return self.call('get_channel_spacings', kwargs=kwargs)

    def can_pick_up_tip(self, **kwargs):
        return self.call('can_pick_up_tip', kwargs=kwargs)

    def core_check_resource_exists_at_location_center(self, **kwargs):
        return self.call('core_check_resource_exists_at_location_center', kwargs=kwargs)

    def pre_initialize_instrument(self, **kwargs):
        return self.call('pre_initialize_instrument', kwargs=kwargs)

    def define_tip_needle(self, **kwargs):
        return self.call('define_tip_needle', kwargs=kwargs)

    def request_error_code(self, **kwargs):
        return self.call('request_error_code', kwargs=kwargs)

    def request_firmware_version(self, **kwargs):
        return self.call('request_firmware_version', kwargs=kwargs)

    def request_parameter_value(self, **kwargs):
        return self.call('request_parameter_value', kwargs=kwargs)

    def request_electronic_board_type(self, **kwargs):
        return self.call('request_electronic_board_type', kwargs=kwargs)

    def request_supply_voltage(self, **kwargs):
        return self.call('request_supply_voltage', kwargs=kwargs)

    def request_instrument_initialization_status(self, **kwargs):
        return self.call('request_instrument_initialization_status', kwargs=kwargs)

    def request_autoload_initialization_status(self, **kwargs):
        return self.call('request_autoload_initialization_status', kwargs=kwargs)

    def request_name_of_last_faulty_parameter(self, **kwargs):
        return self.call('request_name_of_last_faulty_parameter', kwargs=kwargs)

    def request_master_status(self, **kwargs):
        return self.call('request_master_status', kwargs=kwargs)

    def request_number_of_presence_sensors_installed(self, **kwargs):
        return self.call('request_number_of_presence_sensors_installed', kwargs=kwargs)

    def request_eeprom_data_correctness(self, **kwargs):
        return self.call('request_eeprom_data_correctness', kwargs=kwargs)

    def set_single_step_mode(self, **kwargs):
        return self.call('set_single_step_mode', kwargs=kwargs)

    def trigger_next_step(self, **kwargs):
        return self.call('trigger_next_step', kwargs=kwargs)

    def halt(self, **kwargs):
        return self.call('halt', kwargs=kwargs)

    def save_all_cycle_counters(self, **kwargs):
        return self.call('save_all_cycle_counters', kwargs=kwargs)

    def set_not_stop(self, **kwargs):
        return self.call('set_not_stop', kwargs=kwargs)

    def store_installation_data(self, **kwargs):
        return self.call('store_installation_data', kwargs=kwargs)

    def store_verification_data(self, **kwargs):
        return self.call('store_verification_data', kwargs=kwargs)

    def additional_time_stamp(self, **kwargs):
        return self.call('additional_time_stamp', kwargs=kwargs)

    def set_x_offset_x_axis_iswap(self, **kwargs):
        return self.call('set_x_offset_x_axis_iswap', kwargs=kwargs)

    def set_x_offset_x_axis_core_96_head(self, **kwargs):
        return self.call('set_x_offset_x_axis_core_96_head', kwargs=kwargs)

    def set_x_offset_x_axis_core_nano_pipettor_head(self, **kwargs):
        return self.call('set_x_offset_x_axis_core_nano_pipettor_head', kwargs=kwargs)

    def save_download_date(self, **kwargs):
        return self.call('save_download_date', kwargs=kwargs)

    def save_technical_status_of_assemblies(self, **kwargs):
        return self.call('save_technical_status_of_assemblies', kwargs=kwargs)

    def set_instrument_configuration(self, **kwargs):
        return self.call('set_instrument_configuration', kwargs=kwargs)

    def save_pip_channel_validation_status(self, **kwargs):
        return self.call('save_pip_channel_validation_status', kwargs=kwargs)

    def save_xl_channel_validation_status(self, **kwargs):
        return self.call('save_xl_channel_validation_status', kwargs=kwargs)

    def configure_node_names(self, **kwargs):
        return self.call('configure_node_names', kwargs=kwargs)

    def set_deck_data(self, **kwargs):
        return self.call('set_deck_data', kwargs=kwargs)

    def request_technical_status_of_assemblies(self, **kwargs):
        return self.call('request_technical_status_of_assemblies', kwargs=kwargs)

    def request_installation_data(self, **kwargs):
        return self.call('request_installation_data', kwargs=kwargs)

    def request_device_serial_number(self, **kwargs):
        return self.call('request_device_serial_number', kwargs=kwargs)

    def request_download_date(self, **kwargs):
        return self.call('request_download_date', kwargs=kwargs)

    def request_verification_data(self, **kwargs):
        return self.call('request_verification_data', kwargs=kwargs)

    def request_additional_timestamp_data(self, **kwargs):
        return self.call('request_additional_timestamp_data', kwargs=kwargs)

    def request_pip_channel_validation_status(self, **kwargs):
        return self.call('request_pip_channel_validation_status', kwargs=kwargs)

    def request_xl_channel_validation_status(self, **kwargs):
        return self.call('request_xl_channel_validation_status', kwargs=kwargs)

    def request_machine_configuration(self, **kwargs):
        return self.call('request_machine_configuration', kwargs=kwargs)

    def request_extended_configuration(self, **kwargs):
        return self.call('request_extended_configuration', kwargs=kwargs)

    def request_node_names(self, **kwargs):
        return self.call('request_node_names', kwargs=kwargs)

    def request_deck_data(self, **kwargs):
        return self.call('request_deck_data', kwargs=kwargs)

    def position_left_x_arm(self, **kwargs):
        return self.call('position_left_x_arm_', kwargs=kwargs)

    def position_right_x_arm(self, **kwargs):
        return self.call('position_right_x_arm_', kwargs=kwargs)

    def move_left_x_arm_to_position_with_all_attached_components_in_z_safety_position(self, **kwargs):
        return self.call('move_left_x_arm_to_position_with_all_attached_components_in_z_safety_position', kwargs=kwargs)

    def move_right_x_arm_to_position_with_all_attached_components_in_z_safety_position(self, **kwargs):
        return self.call('move_right_x_arm_to_position_with_all_attached_components_in_z_safety_position', kwargs=kwargs)

    def occupy_and_provide_area_for_external_access(self, **kwargs):
        return self.call('occupy_and_provide_area_for_external_access', kwargs=kwargs)

    def release_occupied_area(self, **kwargs):
        return self.call('release_occupied_area', kwargs=kwargs)

    def release_all_occupied_areas(self, **kwargs):
        return self.call('release_all_occupied_areas', kwargs=kwargs)

    def request_left_x_arm_position(self, **kwargs):
        return self.call('request_left_x_arm_position', kwargs=kwargs)

    def request_right_x_arm_position(self, **kwargs):
        return self.call('request_right_x_arm_position', kwargs=kwargs)

    def request_maximal_ranges_of_x_drives(self, **kwargs):
        return self.call('request_maximal_ranges_of_x_drives', kwargs=kwargs)

    def request_present_wrap_size_of_installed_arms(self, **kwargs):
        return self.call('request_present_wrap_size_of_installed_arms', kwargs=kwargs)

    def request_left_x_arm_last_collision_type(self, **kwargs):
        return self.call('request_left_x_arm_last_collision_type', kwargs=kwargs)

    def request_right_x_arm_last_collision_type(self, **kwargs):
        return self.call('request_right_x_arm_last_collision_type', kwargs=kwargs)

    def initialize_pip(self, **kwargs):
        return self.call('initialize_pip', kwargs=kwargs)

    def initialize_pipetting_channels(self, **kwargs):
        return self.call('initialize_pipetting_channels', kwargs=kwargs)

    def pick_up_tip(self, **kwargs):
        return self.call('pick_up_tip', kwargs=kwargs)

    def discard_tip(self, **kwargs):
        return self.call('discard_tip', kwargs=kwargs)

    def aspirate_pip(self, **kwargs):
        return self.call('aspirate_pip', kwargs=kwargs)

    def dispense_pip(self, **kwargs):
        return self.call('dispense_pip', kwargs=kwargs)

    def get_core(self, **kwargs):
        return self.call('get_core', kwargs=kwargs)

    def pick_up_core_gripper_tools(self, **kwargs):
        return self.call('pick_up_core_gripper_tools', kwargs=kwargs)

    def put_core(self, **kwargs):
        return self.call('put_core', kwargs=kwargs)

    def return_core_gripper_tools(self, **kwargs):
        return self.call('return_core_gripper_tools', kwargs=kwargs)

    def core_open_gripper(self, **kwargs):
        return self.call('core_open_gripper', kwargs=kwargs)

    def core_get_plate(self, **kwargs):
        return self.call('core_get_plate', kwargs=kwargs)

    def core_put_plate(self, **kwargs):
        return self.call('core_put_plate', kwargs=kwargs)

    def core_move_plate_to_position(self, **kwargs):
        return self.call('core_move_plate_to_position', kwargs=kwargs)

    def core_read_barcode_of_picked_up_resource(self, **kwargs):
        return self.call('core_read_barcode_of_picked_up_resource', kwargs=kwargs)

    def position_single_pipetting_channel_in_y_direction(self, **kwargs):
        return self.call('position_single_pipetting_channel_in_y_direction', kwargs=kwargs)

    def position_single_pipetting_channel_in_z_direction(self, **kwargs):
        return self.call('position_single_pipetting_channel_in_z_direction', kwargs=kwargs)

    def search_for_teach_in_signal_using_pipetting_channel_n_in_x_direction(self, **kwargs):
        return self.call('search_for_teach_in_signal_using_pipetting_channel_n_in_x_direction', kwargs=kwargs)

    def spread_pip_channels(self, **kwargs):
        return self.call('spread_pip_channels', kwargs=kwargs)

    def move_all_pipetting_channels_to_defined_position(self, **kwargs):
        return self.call('move_all_pipetting_channels_to_defined_position', kwargs=kwargs)

    def position_max_free_y_for_n(self, **kwargs):
        return self.call('position_max_free_y_for_n', kwargs=kwargs)

    def move_all_channels_in_z_safety(self, **kwargs):
        return self.call('move_all_channels_in_z_safety', kwargs=kwargs)

    def request_x_pos_channel_n(self, **kwargs):
        return self.call('request_x_pos_channel_n', kwargs=kwargs)

    def request_y_pos_channel_n(self, **kwargs):
        return self.call('request_y_pos_channel_n', kwargs=kwargs)

    def request_z_pos_channel_n(self, **kwargs):
        return self.call('request_z_pos_channel_n', kwargs=kwargs)

    def request_tip_bottom_z_position(self, **kwargs):
        return self.call('request_tip_bottom_z_position', kwargs=kwargs)

    def request_tip_presence(self, **kwargs):
        return self.call('request_tip_presence', kwargs=kwargs)

    def channels_sense_tip_presence(self, **kwargs):
        return self.call('channels_sense_tip_presence', kwargs=kwargs)

    def request_pip_height_last_lld(self, **kwargs):
        return self.call('request_pip_height_last_lld', kwargs=kwargs)

    def request_tadm_status(self, **kwargs):
        return self.call('request_tadm_status', kwargs=kwargs)

    def head96_request_firmware_version(self, **kwargs):
        return self.call('head96_request_firmware_version', kwargs=kwargs)

    def head96_request_type(self, **kwargs):
        return self.call('head96_request_type', kwargs=kwargs)

    def initialize_core_96_head(self, **kwargs):
        return self.call('initialize_core_96_head', kwargs=kwargs)

    def request_core_96_head_initialization_status(self, **kwargs):
        return self.call('request_core_96_head_initialization_status', kwargs=kwargs)

    def head96_dispensing_drive_and_squeezer_driver_initialize(self, **kwargs):
        return self.call('head96_dispensing_drive_and_squeezer_driver_initialize', kwargs=kwargs)

    def move_core_96_to_safe_position(self, **kwargs):
        return self.call('move_core_96_to_safe_position', kwargs=kwargs)

    def head96_move_to_z_safety(self, **kwargs):
        return self.call('head96_move_to_z_safety', kwargs=kwargs)

    def head96_park(self, **kwargs):
        return self.call('head96_park', kwargs=kwargs)

    def head96_move_x(self, **kwargs):
        return self.call('head96_move_x', kwargs=kwargs)

    def head96_move_y(self, **kwargs):
        return self.call('head96_move_y', kwargs=kwargs)

    def head96_move_z(self, **kwargs):
        return self.call('head96_move_z', kwargs=kwargs)

    def pick_up_tips_core96(self, **kwargs):
        return self.call('pick_up_tips_core96', kwargs=kwargs)

    def discard_tips_core96(self, **kwargs):
        return self.call('discard_tips_core96', kwargs=kwargs)

    def head96_dispensing_drive_move_to_home_volume(self, **kwargs):
        return self.call('head96_dispensing_drive_move_to_home_volume', kwargs=kwargs)

    def aspirate_core_96(self, **kwargs):
        return self.call('aspirate_core_96', kwargs=kwargs)

    def dispense_core_96(self, **kwargs):
        return self.call('dispense_core_96', kwargs=kwargs)

    def move_core_96_head_to_defined_position(self, **kwargs):
        return self.call('move_core_96_head_to_defined_position', kwargs=kwargs)

    def head96_move_to_coordinate(self, **kwargs):
        return self.call('head96_move_to_coordinate', kwargs=kwargs)

    def head96_dispensing_drive_move_to_position(self, **kwargs):
        return self.call('head96_dispensing_drive_move_to_position', kwargs=kwargs)

    def move_core_96_head_x(self, **kwargs):
        return self.call('move_core_96_head_x', kwargs=kwargs)

    def move_core_96_head_y(self, **kwargs):
        return self.call('move_core_96_head_y', kwargs=kwargs)

    def move_core_96_head_z(self, **kwargs):
        return self.call('move_core_96_head_z', kwargs=kwargs)

    def move_96head_to_coordinate(self, **kwargs):
        return self.call('move_96head_to_coordinate', kwargs=kwargs)

    def request_tip_presence_in_core_96_head(self, **kwargs):
        return self.call('request_tip_presence_in_core_96_head', kwargs=kwargs)

    def head96_request_tip_presence(self, **kwargs):
        return self.call('head96_request_tip_presence', kwargs=kwargs)

    def request_position_of_core_96_head(self, **kwargs):
        return self.call('request_position_of_core_96_head', kwargs=kwargs)

    def head96_request_position(self, **kwargs):
        return self.call('head96_request_position', kwargs=kwargs)

    def request_core_96_head_channel_tadm_status(self, **kwargs):
        return self.call('request_core_96_head_channel_tadm_status', kwargs=kwargs)

    def request_core_96_head_channel_tadm_error_status(self, **kwargs):
        return self.call('request_core_96_head_channel_tadm_error_status', kwargs=kwargs)

    def head96_dispensing_drive_request_position_mm(self, **kwargs):
        return self.call('head96_dispensing_drive_request_position_mm', kwargs=kwargs)

    def head96_dispensing_drive_request_position_uL(self, **kwargs):
        return self.call('head96_dispensing_drive_request_position_uL', kwargs=kwargs)

    def initialize_auto_load(self, **kwargs):
        return self.call('initialize_auto_load', kwargs=kwargs)

    def initialize_autoload(self, **kwargs):
        return self.call('initialize_autoload', kwargs=kwargs)

    def move_auto_load_to_z_save_position(self, **kwargs):
        return self.call('move_auto_load_to_z_save_position', kwargs=kwargs)

    def move_autoload_to_save_z_position(self, **kwargs):
        return self.call('move_autoload_to_save_z_position', kwargs=kwargs)

    def move_autoload_to_safe_z_position(self, **kwargs):
        return self.call('move_autoload_to_safe_z_position', kwargs=kwargs)

    def request_auto_load_slot_position(self, **kwargs):
        return self.call('request_auto_load_slot_position', kwargs=kwargs)

    def request_autoload_track(self, **kwargs):
        return self.call('request_autoload_track', kwargs=kwargs)

    def request_autoload_type(self, **kwargs):
        return self.call('request_autoload_type', kwargs=kwargs)

    def request_presence_of_carriers_on_deck(self, **kwargs):
        return self.call('request_presence_of_carriers_on_deck', kwargs=kwargs)

    def request_presence_of_carriers_on_loading_tray(self, **kwargs):
        return self.call('request_presence_of_carriers_on_loading_tray', kwargs=kwargs)

    def request_presence_of_single_carrier_on_loading_tray(self, **kwargs):
        return self.call('request_presence_of_single_carrier_on_loading_tray', kwargs=kwargs)

    def request_single_carrier_presence(self, **kwargs):
        return self.call('request_single_carrier_presence', kwargs=kwargs)

    def move_autoload_to_slot(self, **kwargs):
        return self.call('move_autoload_to_slot', kwargs=kwargs)

    def move_autoload_to_track(self, **kwargs):
        return self.call('move_autoload_to_track', kwargs=kwargs)

    def park_autoload(self, **kwargs):
        return self.call('park_autoload', kwargs=kwargs)

    def take_carrier_out_to_autoload_belt(self, **kwargs):
        return self.call('take_carrier_out_to_autoload_belt', kwargs=kwargs)

    def set_1d_barcode_type(self, **kwargs):
        return self.call('set_1d_barcode_type', kwargs=kwargs)

    def set_barcode_type(self, **kwargs):
        return self.call('set_barcode_type', kwargs=kwargs)

    def load_carrier_from_tray_and_scan_carrier_barcode(self, **kwargs):
        return self.call('load_carrier_from_tray_and_scan_carrier_barcode', kwargs=kwargs)

    def unload_carrier_after_carrier_barcode_scanning(self, **kwargs):
        return self.call('unload_carrier_after_carrier_barcode_scanning', kwargs=kwargs)

    def set_carrier_monitoring(self, **kwargs):
        return self.call('set_carrier_monitoring', kwargs=kwargs)

    def load_carrier_from_autoload_belt(self, **kwargs):
        return self.call('load_carrier_from_autoload_belt', kwargs=kwargs)

    def load_carrier(self, **kwargs):
        return self.call('load_carrier', kwargs=kwargs)

    def set_loading_indicators(self, **kwargs):
        return self.call('set_loading_indicators', kwargs=kwargs)

    def verify_and_wait_for_carriers(self, **kwargs):
        return self.call('verify_and_wait_for_carriers', kwargs=kwargs)

    def unload_carrier(self, **kwargs):
        return self.call('unload_carrier', kwargs=kwargs)

    def request_pump_settings(self, **kwargs):
        return self.call('request_pump_settings', kwargs=kwargs)

    def initialize_dual_pump_station_valves(self, **kwargs):
        return self.call('initialize_dual_pump_station_valves', kwargs=kwargs)

    def fill_selected_dual_chamber(self, **kwargs):
        return self.call('fill_selected_dual_chamber', kwargs=kwargs)

    def drain_dual_chamber_system(self, **kwargs):
        return self.call('drain_dual_chamber_system', kwargs=kwargs)

    def initialize_iswap(self, **kwargs):
        return self.call('initialize_iswap', kwargs=kwargs)

    def position_components_for_free_iswap_y_range(self, **kwargs):
        return self.call('position_components_for_free_iswap_y_range', kwargs=kwargs)

    def move_iswap_x_relative(self, **kwargs):
        return self.call('move_iswap_x_relative', kwargs=kwargs)

    def move_iswap_y_relative(self, **kwargs):
        return self.call('move_iswap_y_relative', kwargs=kwargs)

    def move_iswap_z_relative(self, **kwargs):
        return self.call('move_iswap_z_relative', kwargs=kwargs)

    def move_iswap_x(self, **kwargs):
        return self.call('move_iswap_x', kwargs=kwargs)

    def move_iswap_y(self, **kwargs):
        return self.call('move_iswap_y', kwargs=kwargs)

    def move_iswap_z(self, **kwargs):
        return self.call('move_iswap_z', kwargs=kwargs)

    def open_not_initialized_gripper(self, **kwargs):
        return self.call('open_not_initialized_gripper', kwargs=kwargs)

    def iswap_open_gripper(self, **kwargs):
        return self.call('iswap_open_gripper', kwargs=kwargs)

    def iswap_close_gripper(self, **kwargs):
        return self.call('iswap_close_gripper', kwargs=kwargs)

    def park_iswap(self, **kwargs):
        return self.call('park_iswap', kwargs=kwargs)

    def iswap_get_plate(self, **kwargs):
        return self.call('iswap_get_plate', kwargs=kwargs)

    def iswap_put_plate(self, **kwargs):
        return self.call('iswap_put_plate', kwargs=kwargs)

    def request_iswap_rotation_drive_position_increments(self, **kwargs):
        return self.call('request_iswap_rotation_drive_position_increments', kwargs=kwargs)

    def request_iswap_rotation_drive_orientation(self, **kwargs):
        return self.call('request_iswap_rotation_drive_orientation', kwargs=kwargs)

    def request_iswap_wrist_drive_position_increments(self, **kwargs):
        return self.call('request_iswap_wrist_drive_position_increments', kwargs=kwargs)

    def request_iswap_wrist_drive_orientation(self, **kwargs):
        return self.call('request_iswap_wrist_drive_orientation', kwargs=kwargs)

    def iswap_rotate(self, **kwargs):
        return self.call('iswap_rotate', kwargs=kwargs)

    def iswap_dangerous_release_break(self, **kwargs):
        return self.call('iswap_dangerous_release_break', kwargs=kwargs)

    def iswap_reengage_break(self, **kwargs):
        return self.call('iswap_reengage_break', kwargs=kwargs)

    def iswap_initialize_z_axis(self, **kwargs):
        return self.call('iswap_initialize_z_axis', kwargs=kwargs)

    def move_plate_to_position(self, **kwargs):
        return self.call('move_plate_to_position', kwargs=kwargs)

    def collapse_gripper_arm(self, **kwargs):
        return self.call('collapse_gripper_arm', kwargs=kwargs)

    def prepare_iswap_teaching(self, **kwargs):
        return self.call('prepare_iswap_teaching', kwargs=kwargs)

    def get_logic_iswap_position(self, **kwargs):
        return self.call('get_logic_iswap_position', kwargs=kwargs)

    def request_iswap_in_parking_position(self, **kwargs):
        return self.call('request_iswap_in_parking_position', kwargs=kwargs)

    def request_plate_in_iswap(self, **kwargs):
        return self.call('request_plate_in_iswap', kwargs=kwargs)

    def request_iswap_position(self, **kwargs):
        return self.call('request_iswap_position', kwargs=kwargs)

    def iswap_rotation_drive_request_y(self, **kwargs):
        return self.call('iswap_rotation_drive_request_y', kwargs=kwargs)

    def request_iswap_initialization_status(self, **kwargs):
        return self.call('request_iswap_initialization_status', kwargs=kwargs)

    def request_iswap_version(self, **kwargs):
        return self.call('request_iswap_version', kwargs=kwargs)

    def lock_cover(self, **kwargs):
        return self.call('lock_cover', kwargs=kwargs)

    def unlock_cover(self, **kwargs):
        return self.call('unlock_cover', kwargs=kwargs)

    def disable_cover_control(self, **kwargs):
        return self.call('disable_cover_control', kwargs=kwargs)

    def enable_cover_control(self, **kwargs):
        return self.call('enable_cover_control', kwargs=kwargs)

    def set_cover_output(self, **kwargs):
        return self.call('set_cover_output', kwargs=kwargs)

    def reset_output(self, **kwargs):
        return self.call('reset_output', kwargs=kwargs)

    def request_cover_open(self, **kwargs):
        return self.call('request_cover_open', kwargs=kwargs)

    def mm_to_y_drive_increment(self, **kwargs):
        return self.call('mm_to_y_drive_increment', kwargs=kwargs)

    def y_drive_increment_to_mm(self, **kwargs):
        return self.call('y_drive_increment_to_mm', kwargs=kwargs)

    def mm_to_z_drive_increment(self, **kwargs):
        return self.call('mm_to_z_drive_increment', kwargs=kwargs)

    def z_drive_increment_to_mm(self, **kwargs):
        return self.call('z_drive_increment_to_mm', kwargs=kwargs)

    def dispensing_drive_vol_to_increment(self, **kwargs):
        return self.call('dispensing_drive_vol_to_increment', kwargs=kwargs)

    def dispensing_drive_increment_to_volume(self, **kwargs):
        return self.call('dispensing_drive_increment_to_volume', kwargs=kwargs)

    def dispensing_drive_mm_to_increment(self, **kwargs):
        return self.call('dispensing_drive_mm_to_increment', kwargs=kwargs)

    def dispensing_drive_increment_to_mm(self, **kwargs):
        return self.call('dispensing_drive_increment_to_mm', kwargs=kwargs)

    def dispensing_drive_vol_to_mm(self, **kwargs):
        return self.call('dispensing_drive_vol_to_mm', kwargs=kwargs)

    def dispensing_drive_mm_to_vol(self, **kwargs):
        return self.call('dispensing_drive_mm_to_vol', kwargs=kwargs)

    def clld_probe_x_position_using_channel(self, **kwargs):
        return self.call('clld_probe_x_position_using_channel', kwargs=kwargs)

    def clld_probe_y_position_using_channel(self, **kwargs):
        return self.call('clld_probe_y_position_using_channel', kwargs=kwargs)

    def clld_probe_z_height_using_channel(self, **kwargs):
        return self.call('clld_probe_z_height_using_channel', kwargs=kwargs)

    def plld_probe_z_height_using_channel(self, **kwargs):
        return self.call('plld_probe_z_height_using_channel', kwargs=kwargs)

    def request_probe_z_position(self, **kwargs):
        return self.call('request_probe_z_position', kwargs=kwargs)

    def request_tip_len_on_channel(self, **kwargs):
        return self.call('request_tip_len_on_channel', kwargs=kwargs)

    def ztouch_probe_z_height_using_channel(self, **kwargs):
        return self.call('ztouch_probe_z_height_using_channel', kwargs=kwargs)

    def rotate_iswap_rotation_drive(self, **kwargs):
        return self.call('rotate_iswap_rotation_drive', kwargs=kwargs)

    def rotate_iswap_wrist(self, **kwargs):
        return self.call('rotate_iswap_wrist', kwargs=kwargs)

    def channel_id(self, **kwargs):
        return self.call('channel_id', kwargs=kwargs)

    def get_channels_y_positions(self, **kwargs):
        return self.call('get_channels_y_positions', kwargs=kwargs)

    def position_channels_in_y_direction(self, **kwargs):
        return self.call('position_channels_in_y_direction', kwargs=kwargs)

    def get_channels_z_positions(self, **kwargs):
        return self.call('get_channels_z_positions', kwargs=kwargs)

    def position_channels_in_z_direction(self, **kwargs):
        return self.call('position_channels_in_z_direction', kwargs=kwargs)

    def pierce_foil(self, **kwargs):
        return self.call('pierce_foil', kwargs=kwargs)

    def step_off_foil(self, **kwargs):
        return self.call('step_off_foil', kwargs=kwargs)

    def request_volume_in_tip(self, **kwargs):
        return self.call('request_volume_in_tip', kwargs=kwargs)

    def slow_iswap(self, **kwargs):
        return self.call('slow_iswap', kwargs=kwargs)

    def send_hhs_command(self, **kwargs):
        return self.call('send_hhs_command', kwargs=kwargs)

    def check_type_is_hhc(self, **kwargs):
        return self.call('check_type_is_hhc', kwargs=kwargs)

    def initialize_hhc(self, **kwargs):
        return self.call('initialize_hhc', kwargs=kwargs)

    def start_temperature_control_at_hhc(self, **kwargs):
        return self.call('start_temperature_control_at_hhc', kwargs=kwargs)

    def get_temperature_at_hhc(self, **kwargs):
        return self.call('get_temperature_at_hhc', kwargs=kwargs)

    def query_whether_temperature_reached_at_hhc(self, **kwargs):
        return self.call('query_whether_temperature_reached_at_hhc', kwargs=kwargs)

    def stop_temperature_control_at_hhc(self, **kwargs):
        return self.call('stop_temperature_control_at_hhc', kwargs=kwargs)

    def serialize(self, **kwargs):
        return self.call('serialize', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def get_or_assign_tip_type_index(self, **kwargs):
        return self.call('get_or_assign_tip_type_index', kwargs=kwargs)

    def send_raw_command(self, **kwargs):
        return self.call('send_raw_command', kwargs=kwargs)

    def set_deck(self, **kwargs):
        return self.call('set_deck', kwargs=kwargs)

    def set_heads(self, **kwargs):
        return self.call('set_heads', kwargs=kwargs)

    def deck(self, **kwargs):
        return self.call('deck', kwargs=kwargs)

    def head(self, **kwargs):
        return self.call('head', kwargs=kwargs)

    def head96(self, **kwargs):
        return self.call('head96', kwargs=kwargs)

    def deserialize(self, **kwargs):
        return self.call('deserialize', kwargs=kwargs)

    def get_all_instances(self, **kwargs):
        return self.call('get_all_instances', kwargs=kwargs)

