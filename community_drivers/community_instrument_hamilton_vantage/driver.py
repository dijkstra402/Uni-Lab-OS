from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHamiltonVantage(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/liquid_handling/backends/hamilton/vantage_backend.py', 'class_name': 'VantageBackend', 'import_roots': [], 'candidate_methods': ['arm_pre_initialize', 'arm_request_instrument_initialization_status', 'aspirate', 'aspirate96', 'calculates_check_sums_and_compares_them_with_the_value_saved_in_flash_eprom', 'can_pick_up_tip', 'check_fw_string_error', 'core96_aspiration_of_liquid', 'core96_dispensing_of_liquid', 'core96_empty_washed_tips', 'core96_initialize', 'core96_move_to_defined_position', 'core96_query_tip_presence', 'core96_request_initialization_status', 'core96_request_position', 'core96_request_tadm_error_status', 'core96_search_for_teach_in_signal_in_x_direction', 'core96_set_any_parameter', 'core96_tip_discard', 'core96_tip_pick_up', 'core96_wash_tips', 'define_tip_needle', 'discard_core_gripper_tool', 'disco_mode', 'dispense', 'dispense96', 'dispense_on_fly', 'drop_resource', 'drop_tips', 'drop_tips96', 'expose_channel_n', 'get_channel_spacings', 'get_id_from_fw_response', 'get_or_assign_tip_type_index', 'grip_plate', 'ipg_expose_channel_n', 'ipg_get_parking_status', 'ipg_grip_plate', 'ipg_initialize', 'ipg_move_to_defined_position', 'ipg_park', 'ipg_prepare_gripper_orientation', 'ipg_put_plate', 'ipg_query_tip_presence', 'ipg_release_object', 'ipg_request_access_range', 'ipg_request_actual_angular_dimensions', 'ipg_request_configuration', 'ipg_request_initialization_status', 'ipg_request_position', 'ipg_search_for_teach_in_signal_in_x_direction', 'ipg_set_any_parameter_within_this_module', 'loading_cover_initialize', 'loading_cover_request_initialization_status', 'move_channel_x', 'move_channel_y', 'move_channel_z', 'move_picked_up_resource', 'move_to_defined_position', 'move_to_position', 'nano_pulse_dispense', 'pick_up_resource', 'pick_up_tips', 'pick_up_tips96', 'pip_aspirate', 'pip_dispense', 'pip_initialize', 'pip_request_initialization_status', 'pip_tip_discard', 'pip_tip_pick_up', 'position_all_channels_in_y_direction', 'position_all_channels_in_z_direction', 'position_single_channel_in_y_direction', 'position_single_channel_in_z_direction', 'prepare_for_manual_channel_operation', 'put_plate', 'query_tip_presence', 'release_object', 'request_channel_dispense_on_fly_status', 'request_height_of_last_lld', 'request_tip_presence', 'request_y_position_of_channel_n', 'request_y_positions_of_all_channels', 'request_z_position_of_channel_n', 'request_z_positions_of_all_channels', 'russian_roulette', 'search_for_teach_in_signal_in_x_direction', 'send_raw_command', 'set_any_parameter_within_this_module', 'set_deck', 'set_heads', 'set_led_color', 'set_loading_cover', 'set_minimum_traversal_height', 'setup', 'simultaneous_aspiration_dispensation_of_liquid', 'stop', 'teach_rack_using_channel_n', 'wash_tips', 'x_arm_initialize', 'x_arm_move_arm_relatively_in_x', 'x_arm_move_to_x_position', 'x_arm_move_to_x_position_with_all_attached_components_in_z_safety_position', 'x_arm_request_arm_x_position', 'x_arm_request_error_code', 'x_arm_request_x_drive_recorded_data', 'x_arm_search_x_for_teach_signal', 'x_arm_send_message_to_motion_controller', 'x_arm_set_any_parameter_within_this_module', 'x_arm_set_x_drive_angle_of_alignment', 'x_arm_turn_x_drive_off'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Hamilton', 'model': 'Vantage', 'device_type_cn': '移液工作站', 'device_type_en': 'Liquid Handling Workstation', 'source_framework': 'PyLabRobot', 'tag_id': '4436', 'tag_name': '移液工作站', 'tag_name_en': 'Liquid Handling Workstation', 'candidate_score': 2342, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/liquid_handling/backends/hamilton/vantage_backend.py', 'class_name': 'VantageBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def arm_pre_initialize(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('arm_pre_initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def arm_request_instrument_initialization_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('arm_request_instrument_initialization_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def aspirate(self, ops=None, use_channels=None, jet=None, blow_out=None, hlcs=None, type_of_aspiration=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, lld_search_height=None, clot_detection_height=None, liquid_surface_at_function_without_lld=None, pull_out_distance_to_take_transport_air_in_function_without_lld=None, tube_2nd_section_height_measured_from_zm=None, tube_2nd_section_ratio=None, minimum_height=None, immersion_depth=None, surface_following_distance=None, transport_air_volume=None, pre_wetting_volume=None, lld_mode=None, lld_sensitivity=None, pressure_lld_sensitivity=None, aspirate_position_above_z_touch_off=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_in_z_direction_from_liquid_surface=None, mix_speed=None, surface_following_distance_during_mixing=None, TODO_DA_5=None, capacitive_mad_supervision_on_off=None, pressure_mad_supervision_on_off=None, tadm_algorithm_on_off=None, limit_curve_index=None, recording_mode=None, disable_volume_correction=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'jet': jet, 'blow_out': blow_out, 'hlcs': hlcs, 'type_of_aspiration': type_of_aspiration, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'lld_search_height': lld_search_height, 'clot_detection_height': clot_detection_height, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'pull_out_distance_to_take_transport_air_in_function_without_lld': pull_out_distance_to_take_transport_air_in_function_without_lld, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'minimum_height': minimum_height, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'transport_air_volume': transport_air_volume, 'pre_wetting_volume': pre_wetting_volume, 'lld_mode': lld_mode, 'lld_sensitivity': lld_sensitivity, 'pressure_lld_sensitivity': pressure_lld_sensitivity, 'aspirate_position_above_z_touch_off': aspirate_position_above_z_touch_off, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_in_z_direction_from_liquid_surface': mix_position_in_z_direction_from_liquid_surface, 'mix_speed': mix_speed, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'TODO_DA_5': TODO_DA_5, 'capacitive_mad_supervision_on_off': capacitive_mad_supervision_on_off, 'pressure_mad_supervision_on_off': pressure_mad_supervision_on_off, 'tadm_algorithm_on_off': tadm_algorithm_on_off, 'limit_curve_index': limit_curve_index, 'recording_mode': recording_mode, 'disable_volume_correction': disable_volume_correction}
        _kw.update(kwargs)
        return self.call('aspirate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def aspirate96(self, aspiration=None, jet=None, blow_out=None, hlc=None, type_of_aspiration=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, pull_out_distance_to_take_transport_air_in_function_without_lld=None, tube_2nd_section_height_measured_from_zm=None, tube_2nd_section_ratio=None, immersion_depth=None, surface_following_distance=None, transport_air_volume=None, blow_out_air_volume=None, pre_wetting_volume=None, lld_mode=None, lld_sensitivity=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_in_z_direction_from_liquid_surface=None, surface_following_distance_during_mixing=None, mix_speed=None, limit_curve_index=None, tadm_channel_pattern=None, tadm_algorithm_on_off=None, recording_mode=None, disable_volume_correction=None, **kwargs):
        _kw = {'aspiration': aspiration, 'jet': jet, 'blow_out': blow_out, 'hlc': hlc, 'type_of_aspiration': type_of_aspiration, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'pull_out_distance_to_take_transport_air_in_function_without_lld': pull_out_distance_to_take_transport_air_in_function_without_lld, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'transport_air_volume': transport_air_volume, 'blow_out_air_volume': blow_out_air_volume, 'pre_wetting_volume': pre_wetting_volume, 'lld_mode': lld_mode, 'lld_sensitivity': lld_sensitivity, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_in_z_direction_from_liquid_surface': mix_position_in_z_direction_from_liquid_surface, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'mix_speed': mix_speed, 'limit_curve_index': limit_curve_index, 'tadm_channel_pattern': tadm_channel_pattern, 'tadm_algorithm_on_off': tadm_algorithm_on_off, 'recording_mode': recording_mode, 'disable_volume_correction': disable_volume_correction}
        _kw.update(kwargs)
        return self.call('aspirate96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def calculates_check_sums_and_compares_them_with_the_value_saved_in_flash_eprom(self, TODO_DC_0=None, TODO_DC_1=None, tip_type=None, TODO_DC_2=None, z_deposit_position=None, minimal_traverse_height_at_begin_of_command=None, first_pip_channel_node_no=None, **kwargs):
        _kw = {'TODO_DC_0': TODO_DC_0, 'TODO_DC_1': TODO_DC_1, 'tip_type': tip_type, 'TODO_DC_2': TODO_DC_2, 'z_deposit_position': z_deposit_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'first_pip_channel_node_no': first_pip_channel_node_no}
        _kw.update(kwargs)
        return self.call('calculates_check_sums_and_compares_them_with_the_value_saved_in_flash_eprom', kwargs={k: v for k, v in _kw.items() if v is not None})

    def can_pick_up_tip(self, channel_idx=None, tip=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'tip': tip}
        _kw.update(kwargs)
        return self.call('can_pick_up_tip', kwargs={k: v for k, v in _kw.items() if v is not None})

    def check_fw_string_error(self, resp=None, **kwargs):
        _kw = {'resp': resp}
        _kw.update(kwargs)
        return self.call('check_fw_string_error', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_aspiration_of_liquid(self, type_of_aspiration=None, x_position=None, y_position=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, lld_search_height=None, liquid_surface_at_function_without_lld=None, pull_out_distance_to_take_transport_air_in_function_without_lld=None, minimum_height=None, tube_2nd_section_height_measured_from_zm=None, tube_2nd_section_ratio=None, immersion_depth=None, surface_following_distance=None, aspiration_volume=None, aspiration_speed=None, transport_air_volume=None, blow_out_air_volume=None, pre_wetting_volume=None, lld_mode=None, lld_sensitivity=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_in_z_direction_from_liquid_surface=None, surface_following_distance_during_mixing=None, mix_speed=None, limit_curve_index=None, tadm_channel_pattern=None, tadm_algorithm_on_off=None, recording_mode=None, **kwargs):
        _kw = {'type_of_aspiration': type_of_aspiration, 'x_position': x_position, 'y_position': y_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'lld_search_height': lld_search_height, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'pull_out_distance_to_take_transport_air_in_function_without_lld': pull_out_distance_to_take_transport_air_in_function_without_lld, 'minimum_height': minimum_height, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'aspiration_volume': aspiration_volume, 'aspiration_speed': aspiration_speed, 'transport_air_volume': transport_air_volume, 'blow_out_air_volume': blow_out_air_volume, 'pre_wetting_volume': pre_wetting_volume, 'lld_mode': lld_mode, 'lld_sensitivity': lld_sensitivity, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_in_z_direction_from_liquid_surface': mix_position_in_z_direction_from_liquid_surface, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'mix_speed': mix_speed, 'limit_curve_index': limit_curve_index, 'tadm_channel_pattern': tadm_channel_pattern, 'tadm_algorithm_on_off': tadm_algorithm_on_off, 'recording_mode': recording_mode}
        _kw.update(kwargs)
        return self.call('core96_aspiration_of_liquid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_dispensing_of_liquid(self, type_of_dispensing_mode=None, x_position=None, y_position=None, minimum_height=None, tube_2nd_section_height_measured_from_zm=None, tube_2nd_section_ratio=None, lld_search_height=None, liquid_surface_at_function_without_lld=None, pull_out_distance_to_take_transport_air_in_function_without_lld=None, immersion_depth=None, surface_following_distance=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, dispense_volume=None, dispense_speed=None, cut_off_speed=None, stop_back_volume=None, transport_air_volume=None, blow_out_air_volume=None, lld_mode=None, lld_sensitivity=None, side_touch_off_distance=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_in_z_direction_from_liquid_surface=None, surface_following_distance_during_mixing=None, mix_speed=None, limit_curve_index=None, tadm_channel_pattern=None, tadm_algorithm_on_off=None, recording_mode=None, **kwargs):
        _kw = {'type_of_dispensing_mode': type_of_dispensing_mode, 'x_position': x_position, 'y_position': y_position, 'minimum_height': minimum_height, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'lld_search_height': lld_search_height, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'pull_out_distance_to_take_transport_air_in_function_without_lld': pull_out_distance_to_take_transport_air_in_function_without_lld, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'dispense_volume': dispense_volume, 'dispense_speed': dispense_speed, 'cut_off_speed': cut_off_speed, 'stop_back_volume': stop_back_volume, 'transport_air_volume': transport_air_volume, 'blow_out_air_volume': blow_out_air_volume, 'lld_mode': lld_mode, 'lld_sensitivity': lld_sensitivity, 'side_touch_off_distance': side_touch_off_distance, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_in_z_direction_from_liquid_surface': mix_position_in_z_direction_from_liquid_surface, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'mix_speed': mix_speed, 'limit_curve_index': limit_curve_index, 'tadm_channel_pattern': tadm_channel_pattern, 'tadm_algorithm_on_off': tadm_algorithm_on_off, 'recording_mode': recording_mode}
        _kw.update(kwargs)
        return self.call('core96_dispensing_of_liquid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_empty_washed_tips(self, liquid_surface_at_function_without_lld=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('core96_empty_washed_tips', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_initialize(self, x_position=None, y_position=None, z_position=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, end_z_deposit_position=None, tip_type=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'z_position': z_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'end_z_deposit_position': end_z_deposit_position, 'tip_type': tip_type}
        _kw.update(kwargs)
        return self.call('core96_initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_move_to_defined_position(self, x_position=None, y_position=None, z_position=None, minimal_traverse_height_at_begin_of_command=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'z_position': z_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command}
        _kw.update(kwargs)
        return self.call('core96_move_to_defined_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_query_tip_presence(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('core96_query_tip_presence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_request_initialization_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('core96_request_initialization_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_request_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('core96_request_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_request_tadm_error_status(self, tadm_channel_pattern=None, **kwargs):
        _kw = {'tadm_channel_pattern': tadm_channel_pattern}
        _kw.update(kwargs)
        return self.call('core96_request_tadm_error_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_search_for_teach_in_signal_in_x_direction(self, x_search_distance=None, x_speed=None, **kwargs):
        _kw = {'x_search_distance': x_search_distance, 'x_speed': x_speed}
        _kw.update(kwargs)
        return self.call('core96_search_for_teach_in_signal_in_x_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_set_any_parameter(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('core96_set_any_parameter', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_tip_discard(self, x_position=None, y_position=None, z_deposit_position=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'z_deposit_position': z_deposit_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('core96_tip_discard', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_tip_pick_up(self, x_position=None, y_position=None, tip_type=None, tip_handling_method=None, z_deposit_position=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'tip_type': tip_type, 'tip_handling_method': tip_handling_method, 'z_deposit_position': z_deposit_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('core96_tip_pick_up', kwargs={k: v for k, v in _kw.items() if v is not None})

    def core96_wash_tips(self, x_position=None, y_position=None, liquid_surface_at_function_without_lld=None, minimum_height=None, surface_following_distance_during_mixing=None, minimal_traverse_height_at_begin_of_command=None, mix_volume=None, mix_cycles=None, mix_speed=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'minimum_height': minimum_height, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_speed': mix_speed}
        _kw.update(kwargs)
        return self.call('core96_wash_tips', kwargs={k: v for k, v in _kw.items() if v is not None})

    def define_tip_needle(self, tip_type_table_index=None, has_filter=None, tip_length=None, maximum_tip_volume=None, tip_size=None, pickup_method=None, **kwargs):
        _kw = {'tip_type_table_index': tip_type_table_index, 'has_filter': has_filter, 'tip_length': tip_length, 'maximum_tip_volume': maximum_tip_volume, 'tip_size': tip_size, 'pickup_method': pickup_method}
        _kw.update(kwargs)
        return self.call('define_tip_needle', kwargs={k: v for k, v in _kw.items() if v is not None})

    def discard_core_gripper_tool(self, gripper_tool_x_position=None, first_gripper_tool_y_pos=None, tip_type=None, begin_z_deposit_position=None, end_z_deposit_position=None, minimal_traverse_height_at_begin_of_command=None, first_pip_channel_node_no=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'gripper_tool_x_position': gripper_tool_x_position, 'first_gripper_tool_y_pos': first_gripper_tool_y_pos, 'tip_type': tip_type, 'begin_z_deposit_position': begin_z_deposit_position, 'end_z_deposit_position': end_z_deposit_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'first_pip_channel_node_no': first_pip_channel_node_no, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('discard_core_gripper_tool', kwargs={k: v for k, v in _kw.items() if v is not None})

    def disco_mode(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('disco_mode', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispense(self, ops=None, use_channels=None, jet=None, blow_out=None, empty=None, hlcs=None, type_of_dispensing_mode=None, minimum_height=None, pull_out_distance_to_take_transport_air_in_function_without_lld=None, immersion_depth=None, surface_following_distance=None, tube_2nd_section_height_measured_from_zm=None, tube_2nd_section_ratio=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, lld_search_height=None, cut_off_speed=None, stop_back_volume=None, transport_air_volume=None, lld_mode=None, side_touch_off_distance=None, dispense_position_above_z_touch_off=None, lld_sensitivity=None, pressure_lld_sensitivity=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_in_z_direction_from_liquid_surface=None, mix_speed=None, surface_following_distance_during_mixing=None, TODO_DD_2=None, tadm_algorithm_on_off=None, limit_curve_index=None, recording_mode=None, disable_volume_correction=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'jet': jet, 'blow_out': blow_out, 'empty': empty, 'hlcs': hlcs, 'type_of_dispensing_mode': type_of_dispensing_mode, 'minimum_height': minimum_height, 'pull_out_distance_to_take_transport_air_in_function_without_lld': pull_out_distance_to_take_transport_air_in_function_without_lld, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'lld_search_height': lld_search_height, 'cut_off_speed': cut_off_speed, 'stop_back_volume': stop_back_volume, 'transport_air_volume': transport_air_volume, 'lld_mode': lld_mode, 'side_touch_off_distance': side_touch_off_distance, 'dispense_position_above_z_touch_off': dispense_position_above_z_touch_off, 'lld_sensitivity': lld_sensitivity, 'pressure_lld_sensitivity': pressure_lld_sensitivity, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_in_z_direction_from_liquid_surface': mix_position_in_z_direction_from_liquid_surface, 'mix_speed': mix_speed, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'TODO_DD_2': TODO_DD_2, 'tadm_algorithm_on_off': tadm_algorithm_on_off, 'limit_curve_index': limit_curve_index, 'recording_mode': recording_mode, 'disable_volume_correction': disable_volume_correction}
        _kw.update(kwargs)
        return self.call('dispense', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispense96(self, dispense=None, jet=None, blow_out=None, empty=None, hlc=None, type_of_dispensing_mode=None, tube_2nd_section_height_measured_from_zm=None, tube_2nd_section_ratio=None, pull_out_distance_to_take_transport_air_in_function_without_lld=None, immersion_depth=None, surface_following_distance=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, cut_off_speed=None, stop_back_volume=None, transport_air_volume=None, blow_out_air_volume=None, lld_mode=None, lld_sensitivity=None, side_touch_off_distance=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_in_z_direction_from_liquid_surface=None, surface_following_distance_during_mixing=None, mix_speed=None, limit_curve_index=None, tadm_channel_pattern=None, tadm_algorithm_on_off=None, recording_mode=None, disable_volume_correction=None, **kwargs):
        _kw = {'dispense': dispense, 'jet': jet, 'blow_out': blow_out, 'empty': empty, 'hlc': hlc, 'type_of_dispensing_mode': type_of_dispensing_mode, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'pull_out_distance_to_take_transport_air_in_function_without_lld': pull_out_distance_to_take_transport_air_in_function_without_lld, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'cut_off_speed': cut_off_speed, 'stop_back_volume': stop_back_volume, 'transport_air_volume': transport_air_volume, 'blow_out_air_volume': blow_out_air_volume, 'lld_mode': lld_mode, 'lld_sensitivity': lld_sensitivity, 'side_touch_off_distance': side_touch_off_distance, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_in_z_direction_from_liquid_surface': mix_position_in_z_direction_from_liquid_surface, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'mix_speed': mix_speed, 'limit_curve_index': limit_curve_index, 'tadm_channel_pattern': tadm_channel_pattern, 'tadm_algorithm_on_off': tadm_algorithm_on_off, 'recording_mode': recording_mode, 'disable_volume_correction': disable_volume_correction}
        _kw.update(kwargs)
        return self.call('dispense96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispense_on_fly(self, y_position=None, tip_pattern=None, first_shoot_x_pos=None, dispense_on_fly_pos_command_end=None, x_acceleration_distance_before_first_shoot=None, space_between_shoots=None, x_speed=None, number_of_shoots=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, liquid_surface_at_function_without_lld=None, dispense_volume=None, dispense_speed=None, cut_off_speed=None, stop_back_volume=None, transport_air_volume=None, tadm_algorithm_on_off=None, limit_curve_index=None, recording_mode=None, **kwargs):
        _kw = {'y_position': y_position, 'tip_pattern': tip_pattern, 'first_shoot_x_pos': first_shoot_x_pos, 'dispense_on_fly_pos_command_end': dispense_on_fly_pos_command_end, 'x_acceleration_distance_before_first_shoot': x_acceleration_distance_before_first_shoot, 'space_between_shoots': space_between_shoots, 'x_speed': x_speed, 'number_of_shoots': number_of_shoots, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'dispense_volume': dispense_volume, 'dispense_speed': dispense_speed, 'cut_off_speed': cut_off_speed, 'stop_back_volume': stop_back_volume, 'transport_air_volume': transport_air_volume, 'tadm_algorithm_on_off': tadm_algorithm_on_off, 'limit_curve_index': limit_curve_index, 'recording_mode': recording_mode}
        _kw.update(kwargs)
        return self.call('dispense_on_fly', kwargs={k: v for k, v in _kw.items() if v is not None})

    def drop_resource(self, drop=None, z_clearance_height=None, press_on_distance=None, hotel_depth=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'drop': drop, 'z_clearance_height': z_clearance_height, 'press_on_distance': press_on_distance, 'hotel_depth': hotel_depth, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('drop_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def drop_tips(self, ops=None, use_channels=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('drop_tips', kwargs={k: v for k, v in _kw.items() if v is not None})

    def drop_tips96(self, drop=None, z_deposit_position=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'drop': drop, 'z_deposit_position': z_deposit_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('drop_tips96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def expose_channel_n(self, channel_index=None, **kwargs):
        _kw = {'channel_index': channel_index}
        _kw.update(kwargs)
        return self.call('expose_channel_n', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_channel_spacings(self, use_channels=None, **kwargs):
        _kw = {'use_channels': use_channels}
        _kw.update(kwargs)
        return self.call('get_channel_spacings', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_id_from_fw_response(self, resp=None, **kwargs):
        _kw = {'resp': resp}
        _kw.update(kwargs)
        return self.call('get_id_from_fw_response', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_or_assign_tip_type_index(self, tip=None, **kwargs):
        _kw = {'tip': tip}
        _kw.update(kwargs)
        return self.call('get_or_assign_tip_type_index', kwargs={k: v for k, v in _kw.items() if v is not None})

    def grip_plate(self, plate_center_x_direction=None, plate_center_y_direction=None, plate_center_z_direction=None, z_speed=None, open_gripper_position=None, plate_width=None, acceleration_index=None, grip_strength=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'plate_center_x_direction': plate_center_x_direction, 'plate_center_y_direction': plate_center_y_direction, 'plate_center_z_direction': plate_center_z_direction, 'z_speed': z_speed, 'open_gripper_position': open_gripper_position, 'plate_width': plate_width, 'acceleration_index': acceleration_index, 'grip_strength': grip_strength, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('grip_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_expose_channel_n(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('ipg_expose_channel_n', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_get_parking_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('ipg_get_parking_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_grip_plate(self, x_position=None, y_position=None, z_position=None, grip_strength=None, open_gripper_position=None, plate_width=None, plate_width_tolerance=None, acceleration_index=None, z_clearance_height=None, hotel_depth=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'z_position': z_position, 'grip_strength': grip_strength, 'open_gripper_position': open_gripper_position, 'plate_width': plate_width, 'plate_width_tolerance': plate_width_tolerance, 'acceleration_index': acceleration_index, 'z_clearance_height': z_clearance_height, 'hotel_depth': hotel_depth, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('ipg_grip_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_initialize(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('ipg_initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_move_to_defined_position(self, x_position=None, y_position=None, z_position=None, minimal_traverse_height_at_begin_of_command=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'z_position': z_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command}
        _kw.update(kwargs)
        return self.call('ipg_move_to_defined_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_park(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('ipg_park', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_prepare_gripper_orientation(self, grip_orientation=None, minimal_traverse_height_at_begin_of_command=None, **kwargs):
        _kw = {'grip_orientation': grip_orientation, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command}
        _kw.update(kwargs)
        return self.call('ipg_prepare_gripper_orientation', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_put_plate(self, x_position=None, y_position=None, z_position=None, open_gripper_position=None, z_clearance_height=None, press_on_distance=None, hotel_depth=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'z_position': z_position, 'open_gripper_position': open_gripper_position, 'z_clearance_height': z_clearance_height, 'press_on_distance': press_on_distance, 'hotel_depth': hotel_depth, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('ipg_put_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_query_tip_presence(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('ipg_query_tip_presence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_release_object(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('ipg_release_object', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_request_access_range(self, grip_orientation=None, **kwargs):
        _kw = {'grip_orientation': grip_orientation}
        _kw.update(kwargs)
        return self.call('ipg_request_access_range', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_request_actual_angular_dimensions(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('ipg_request_actual_angular_dimensions', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_request_configuration(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('ipg_request_configuration', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_request_initialization_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('ipg_request_initialization_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_request_position(self, grip_orientation=None, **kwargs):
        _kw = {'grip_orientation': grip_orientation}
        _kw.update(kwargs)
        return self.call('ipg_request_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_search_for_teach_in_signal_in_x_direction(self, x_search_distance=None, x_speed=None, **kwargs):
        _kw = {'x_search_distance': x_search_distance, 'x_speed': x_speed}
        _kw.update(kwargs)
        return self.call('ipg_search_for_teach_in_signal_in_x_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def ipg_set_any_parameter_within_this_module(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('ipg_set_any_parameter_within_this_module', kwargs={k: v for k, v in _kw.items() if v is not None})

    def loading_cover_initialize(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('loading_cover_initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def loading_cover_request_initialization_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('loading_cover_request_initialization_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_channel_x(self, channel=None, x=None, **kwargs):
        _kw = {'channel': channel, 'x': x}
        _kw.update(kwargs)
        return self.call('move_channel_x', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_channel_y(self, channel=None, y=None, **kwargs):
        _kw = {'channel': channel, 'y': y}
        _kw.update(kwargs)
        return self.call('move_channel_y', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_channel_z(self, channel=None, z=None, **kwargs):
        _kw = {'channel': channel, 'z': z}
        _kw.update(kwargs)
        return self.call('move_channel_z', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_picked_up_resource(self, move=None, **kwargs):
        _kw = {'move': move}
        _kw.update(kwargs)
        return self.call('move_picked_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_to_defined_position(self, x_position=None, y_position=None, tip_pattern=None, minimal_traverse_height_at_begin_of_command=None, z_position=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'tip_pattern': tip_pattern, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'z_position': z_position}
        _kw.update(kwargs)
        return self.call('move_to_defined_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_to_position(self, plate_center_x_direction=None, plate_center_y_direction=None, plate_center_z_direction=None, z_speed=None, minimal_traverse_height_at_begin_of_command=None, **kwargs):
        _kw = {'plate_center_x_direction': plate_center_x_direction, 'plate_center_y_direction': plate_center_y_direction, 'plate_center_z_direction': plate_center_z_direction, 'z_speed': z_speed, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command}
        _kw.update(kwargs)
        return self.call('move_to_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def nano_pulse_dispense(self, x_position=None, y_position=None, TODO_DB_0=None, liquid_surface_at_function_without_lld=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, TODO_DB_1=None, TODO_DB_2=None, TODO_DB_3=None, TODO_DB_4=None, TODO_DB_5=None, TODO_DB_6=None, TODO_DB_7=None, TODO_DB_8=None, TODO_DB_9=None, TODO_DB_10=None, TODO_DB_11=None, TODO_DB_12=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'TODO_DB_0': TODO_DB_0, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'TODO_DB_1': TODO_DB_1, 'TODO_DB_2': TODO_DB_2, 'TODO_DB_3': TODO_DB_3, 'TODO_DB_4': TODO_DB_4, 'TODO_DB_5': TODO_DB_5, 'TODO_DB_6': TODO_DB_6, 'TODO_DB_7': TODO_DB_7, 'TODO_DB_8': TODO_DB_8, 'TODO_DB_9': TODO_DB_9, 'TODO_DB_10': TODO_DB_10, 'TODO_DB_11': TODO_DB_11, 'TODO_DB_12': TODO_DB_12}
        _kw.update(kwargs)
        return self.call('nano_pulse_dispense', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_resource(self, pickup=None, grip_strength=None, plate_width_tolerance=None, acceleration_index=None, z_clearance_height=None, hotel_depth=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'pickup': pickup, 'grip_strength': grip_strength, 'plate_width_tolerance': plate_width_tolerance, 'acceleration_index': acceleration_index, 'z_clearance_height': z_clearance_height, 'hotel_depth': hotel_depth, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('pick_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_tips(self, ops=None, use_channels=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('pick_up_tips', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_tips96(self, pickup=None, tip_handling_method=None, z_deposit_position=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'pickup': pickup, 'tip_handling_method': tip_handling_method, 'z_deposit_position': z_deposit_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('pick_up_tips96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pip_aspirate(self, x_position=None, y_position=None, type_of_aspiration=None, tip_pattern=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, lld_search_height=None, clot_detection_height=None, liquid_surface_at_function_without_lld=None, pull_out_distance_to_take_transport_air_in_function_without_lld=None, tube_2nd_section_height_measured_from_zm=None, tube_2nd_section_ratio=None, minimum_height=None, immersion_depth=None, surface_following_distance=None, aspiration_volume=None, TODO_DA_2=None, aspiration_speed=None, transport_air_volume=None, blow_out_air_volume=None, pre_wetting_volume=None, lld_mode=None, lld_sensitivity=None, pressure_lld_sensitivity=None, aspirate_position_above_z_touch_off=None, TODO_DA_4=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_in_z_direction_from_liquid_surface=None, mix_speed=None, surface_following_distance_during_mixing=None, TODO_DA_5=None, capacitive_mad_supervision_on_off=None, pressure_mad_supervision_on_off=None, tadm_algorithm_on_off=None, limit_curve_index=None, recording_mode=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'type_of_aspiration': type_of_aspiration, 'tip_pattern': tip_pattern, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'lld_search_height': lld_search_height, 'clot_detection_height': clot_detection_height, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'pull_out_distance_to_take_transport_air_in_function_without_lld': pull_out_distance_to_take_transport_air_in_function_without_lld, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'minimum_height': minimum_height, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'aspiration_volume': aspiration_volume, 'TODO_DA_2': TODO_DA_2, 'aspiration_speed': aspiration_speed, 'transport_air_volume': transport_air_volume, 'blow_out_air_volume': blow_out_air_volume, 'pre_wetting_volume': pre_wetting_volume, 'lld_mode': lld_mode, 'lld_sensitivity': lld_sensitivity, 'pressure_lld_sensitivity': pressure_lld_sensitivity, 'aspirate_position_above_z_touch_off': aspirate_position_above_z_touch_off, 'TODO_DA_4': TODO_DA_4, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_in_z_direction_from_liquid_surface': mix_position_in_z_direction_from_liquid_surface, 'mix_speed': mix_speed, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'TODO_DA_5': TODO_DA_5, 'capacitive_mad_supervision_on_off': capacitive_mad_supervision_on_off, 'pressure_mad_supervision_on_off': pressure_mad_supervision_on_off, 'tadm_algorithm_on_off': tadm_algorithm_on_off, 'limit_curve_index': limit_curve_index, 'recording_mode': recording_mode}
        _kw.update(kwargs)
        return self.call('pip_aspirate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pip_dispense(self, x_position=None, y_position=None, type_of_dispensing_mode=None, tip_pattern=None, minimum_height=None, lld_search_height=None, liquid_surface_at_function_without_lld=None, pull_out_distance_to_take_transport_air_in_function_without_lld=None, immersion_depth=None, surface_following_distance=None, tube_2nd_section_height_measured_from_zm=None, tube_2nd_section_ratio=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, dispense_volume=None, dispense_speed=None, cut_off_speed=None, stop_back_volume=None, transport_air_volume=None, blow_out_air_volume=None, lld_mode=None, side_touch_off_distance=None, dispense_position_above_z_touch_off=None, lld_sensitivity=None, pressure_lld_sensitivity=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_in_z_direction_from_liquid_surface=None, mix_speed=None, surface_following_distance_during_mixing=None, TODO_DD_2=None, tadm_algorithm_on_off=None, limit_curve_index=None, recording_mode=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'type_of_dispensing_mode': type_of_dispensing_mode, 'tip_pattern': tip_pattern, 'minimum_height': minimum_height, 'lld_search_height': lld_search_height, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'pull_out_distance_to_take_transport_air_in_function_without_lld': pull_out_distance_to_take_transport_air_in_function_without_lld, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'dispense_volume': dispense_volume, 'dispense_speed': dispense_speed, 'cut_off_speed': cut_off_speed, 'stop_back_volume': stop_back_volume, 'transport_air_volume': transport_air_volume, 'blow_out_air_volume': blow_out_air_volume, 'lld_mode': lld_mode, 'side_touch_off_distance': side_touch_off_distance, 'dispense_position_above_z_touch_off': dispense_position_above_z_touch_off, 'lld_sensitivity': lld_sensitivity, 'pressure_lld_sensitivity': pressure_lld_sensitivity, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_in_z_direction_from_liquid_surface': mix_position_in_z_direction_from_liquid_surface, 'mix_speed': mix_speed, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'TODO_DD_2': TODO_DD_2, 'tadm_algorithm_on_off': tadm_algorithm_on_off, 'limit_curve_index': limit_curve_index, 'recording_mode': recording_mode}
        _kw.update(kwargs)
        return self.call('pip_dispense', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pip_initialize(self, x_position=None, y_position=None, begin_z_deposit_position=None, end_z_deposit_position=None, minimal_height_at_command_end=None, tip_pattern=None, tip_type=None, TODO_DI_2=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'begin_z_deposit_position': begin_z_deposit_position, 'end_z_deposit_position': end_z_deposit_position, 'minimal_height_at_command_end': minimal_height_at_command_end, 'tip_pattern': tip_pattern, 'tip_type': tip_type, 'TODO_DI_2': TODO_DI_2}
        _kw.update(kwargs)
        return self.call('pip_initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pip_request_initialization_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('pip_request_initialization_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pip_tip_discard(self, x_position=None, y_position=None, begin_z_deposit_position=None, end_z_deposit_position=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, tip_pattern=None, TODO_TR_2=None, tip_handling_method=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'begin_z_deposit_position': begin_z_deposit_position, 'end_z_deposit_position': end_z_deposit_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'tip_pattern': tip_pattern, 'TODO_TR_2': TODO_TR_2, 'tip_handling_method': tip_handling_method}
        _kw.update(kwargs)
        return self.call('pip_tip_discard', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pip_tip_pick_up(self, x_position=None, y_position=None, tip_pattern=None, tip_type=None, begin_z_deposit_position=None, end_z_deposit_position=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, blow_out_air_volume=None, tip_handling_method=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'tip_pattern': tip_pattern, 'tip_type': tip_type, 'begin_z_deposit_position': begin_z_deposit_position, 'end_z_deposit_position': end_z_deposit_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'blow_out_air_volume': blow_out_air_volume, 'tip_handling_method': tip_handling_method}
        _kw.update(kwargs)
        return self.call('pip_tip_pick_up', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_all_channels_in_y_direction(self, y_position=None, **kwargs):
        _kw = {'y_position': y_position}
        _kw.update(kwargs)
        return self.call('position_all_channels_in_y_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_all_channels_in_z_direction(self, z_position=None, **kwargs):
        _kw = {'z_position': z_position}
        _kw.update(kwargs)
        return self.call('position_all_channels_in_z_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_single_channel_in_y_direction(self, channel_index=None, y_position=None, **kwargs):
        _kw = {'channel_index': channel_index, 'y_position': y_position}
        _kw.update(kwargs)
        return self.call('position_single_channel_in_y_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def position_single_channel_in_z_direction(self, channel_index=None, z_position=None, **kwargs):
        _kw = {'channel_index': channel_index, 'z_position': z_position}
        _kw.update(kwargs)
        return self.call('position_single_channel_in_z_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def prepare_for_manual_channel_operation(self, channel=None, **kwargs):
        _kw = {'channel': channel}
        _kw.update(kwargs)
        return self.call('prepare_for_manual_channel_operation', kwargs={k: v for k, v in _kw.items() if v is not None})

    def put_plate(self, plate_center_x_direction=None, plate_center_y_direction=None, plate_center_z_direction=None, press_on_distance=None, z_speed=None, open_gripper_position=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'plate_center_x_direction': plate_center_x_direction, 'plate_center_y_direction': plate_center_y_direction, 'plate_center_z_direction': plate_center_z_direction, 'press_on_distance': press_on_distance, 'z_speed': z_speed, 'open_gripper_position': open_gripper_position, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('put_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def query_tip_presence(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('query_tip_presence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def release_object(self, first_pip_channel_node_no=None, **kwargs):
        _kw = {'first_pip_channel_node_no': first_pip_channel_node_no}
        _kw.update(kwargs)
        return self.call('release_object', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_channel_dispense_on_fly_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_channel_dispense_on_fly_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_height_of_last_lld(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_height_of_last_lld', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_tip_presence(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_tip_presence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_y_position_of_channel_n(self, channel_index=None, **kwargs):
        _kw = {'channel_index': channel_index}
        _kw.update(kwargs)
        return self.call('request_y_position_of_channel_n', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_y_positions_of_all_channels(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_y_positions_of_all_channels', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_z_position_of_channel_n(self, channel_index=None, **kwargs):
        _kw = {'channel_index': channel_index}
        _kw.update(kwargs)
        return self.call('request_z_position_of_channel_n', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_z_positions_of_all_channels(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_z_positions_of_all_channels', kwargs={k: v for k, v in _kw.items() if v is not None})

    def russian_roulette(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('russian_roulette', kwargs={k: v for k, v in _kw.items() if v is not None})

    def search_for_teach_in_signal_in_x_direction(self, channel_index=None, x_search_distance=None, x_speed=None, **kwargs):
        _kw = {'channel_index': channel_index, 'x_search_distance': x_search_distance, 'x_speed': x_speed}
        _kw.update(kwargs)
        return self.call('search_for_teach_in_signal_in_x_direction', kwargs={k: v for k, v in _kw.items() if v is not None})

    def send_raw_command(self, command=None, write_timeout=None, read_timeout=None, wait=None, **kwargs):
        _kw = {'command': command, 'write_timeout': write_timeout, 'read_timeout': read_timeout, 'wait': wait}
        _kw.update(kwargs)
        return self.call('send_raw_command', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_any_parameter_within_this_module(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('set_any_parameter_within_this_module', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_deck(self, deck=None, **kwargs):
        _kw = {'deck': deck}
        _kw.update(kwargs)
        return self.call('set_deck', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_heads(self, head=None, head96=None, **kwargs):
        _kw = {'head': head, 'head96': head96}
        _kw.update(kwargs)
        return self.call('set_heads', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_led_color(self, mode=None, intensity=None, white=None, red=None, green=None, blue=None, uv=None, blink_interval=None, **kwargs):
        _kw = {'mode': mode, 'intensity': intensity, 'white': white, 'red': red, 'green': green, 'blue': blue, 'uv': uv, 'blink_interval': blink_interval}
        _kw.update(kwargs)
        return self.call('set_led_color', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_loading_cover(self, cover_open=None, **kwargs):
        _kw = {'cover_open': cover_open}
        _kw.update(kwargs)
        return self.call('set_loading_cover', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_minimum_traversal_height(self, traversal_height=None, **kwargs):
        _kw = {'traversal_height': traversal_height}
        _kw.update(kwargs)
        return self.call('set_minimum_traversal_height', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, skip_loading_cover=None, skip_core96=None, skip_ipg=None, **kwargs):
        _kw = {'skip_loading_cover': skip_loading_cover, 'skip_core96': skip_core96, 'skip_ipg': skip_ipg}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def simultaneous_aspiration_dispensation_of_liquid(self, x_position=None, y_position=None, type_of_aspiration=None, type_of_dispensing_mode=None, tip_pattern=None, TODO_DM_1=None, minimal_traverse_height_at_begin_of_command=None, minimal_height_at_command_end=None, lld_search_height=None, clot_detection_height=None, liquid_surface_at_function_without_lld=None, pull_out_distance_to_take_transport_air_in_function_without_lld=None, minimum_height=None, immersion_depth=None, surface_following_distance=None, tube_2nd_section_height_measured_from_zm=None, tube_2nd_section_ratio=None, aspiration_volume=None, TODO_DM_3=None, aspiration_speed=None, dispense_volume=None, dispense_speed=None, cut_off_speed=None, stop_back_volume=None, transport_air_volume=None, blow_out_air_volume=None, pre_wetting_volume=None, lld_mode=None, aspirate_position_above_z_touch_off=None, lld_sensitivity=None, pressure_lld_sensitivity=None, swap_speed=None, settling_time=None, mix_volume=None, mix_cycles=None, mix_position_in_z_direction_from_liquid_surface=None, mix_speed=None, surface_following_distance_during_mixing=None, TODO_DM_5=None, capacitive_mad_supervision_on_off=None, pressure_mad_supervision_on_off=None, tadm_algorithm_on_off=None, limit_curve_index=None, recording_mode=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'type_of_aspiration': type_of_aspiration, 'type_of_dispensing_mode': type_of_dispensing_mode, 'tip_pattern': tip_pattern, 'TODO_DM_1': TODO_DM_1, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'minimal_height_at_command_end': minimal_height_at_command_end, 'lld_search_height': lld_search_height, 'clot_detection_height': clot_detection_height, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'pull_out_distance_to_take_transport_air_in_function_without_lld': pull_out_distance_to_take_transport_air_in_function_without_lld, 'minimum_height': minimum_height, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'tube_2nd_section_height_measured_from_zm': tube_2nd_section_height_measured_from_zm, 'tube_2nd_section_ratio': tube_2nd_section_ratio, 'aspiration_volume': aspiration_volume, 'TODO_DM_3': TODO_DM_3, 'aspiration_speed': aspiration_speed, 'dispense_volume': dispense_volume, 'dispense_speed': dispense_speed, 'cut_off_speed': cut_off_speed, 'stop_back_volume': stop_back_volume, 'transport_air_volume': transport_air_volume, 'blow_out_air_volume': blow_out_air_volume, 'pre_wetting_volume': pre_wetting_volume, 'lld_mode': lld_mode, 'aspirate_position_above_z_touch_off': aspirate_position_above_z_touch_off, 'lld_sensitivity': lld_sensitivity, 'pressure_lld_sensitivity': pressure_lld_sensitivity, 'swap_speed': swap_speed, 'settling_time': settling_time, 'mix_volume': mix_volume, 'mix_cycles': mix_cycles, 'mix_position_in_z_direction_from_liquid_surface': mix_position_in_z_direction_from_liquid_surface, 'mix_speed': mix_speed, 'surface_following_distance_during_mixing': surface_following_distance_during_mixing, 'TODO_DM_5': TODO_DM_5, 'capacitive_mad_supervision_on_off': capacitive_mad_supervision_on_off, 'pressure_mad_supervision_on_off': pressure_mad_supervision_on_off, 'tadm_algorithm_on_off': tadm_algorithm_on_off, 'limit_curve_index': limit_curve_index, 'recording_mode': recording_mode}
        _kw.update(kwargs)
        return self.call('simultaneous_aspiration_dispensation_of_liquid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def teach_rack_using_channel_n(self, channel_index=None, gap_center_x_direction=None, gap_center_y_direction=None, gap_center_z_direction=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'channel_index': channel_index, 'gap_center_x_direction': gap_center_x_direction, 'gap_center_y_direction': gap_center_y_direction, 'gap_center_z_direction': gap_center_z_direction, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('teach_rack_using_channel_n', kwargs={k: v for k, v in _kw.items() if v is not None})

    def wash_tips(self, x_position=None, y_position=None, tip_pattern=None, minimal_traverse_height_at_begin_of_command=None, liquid_surface_at_function_without_lld=None, aspiration_volume=None, aspiration_speed=None, dispense_speed=None, swap_speed=None, soak_time=None, wash_cycles=None, minimal_height_at_command_end=None, **kwargs):
        _kw = {'x_position': x_position, 'y_position': y_position, 'tip_pattern': tip_pattern, 'minimal_traverse_height_at_begin_of_command': minimal_traverse_height_at_begin_of_command, 'liquid_surface_at_function_without_lld': liquid_surface_at_function_without_lld, 'aspiration_volume': aspiration_volume, 'aspiration_speed': aspiration_speed, 'dispense_speed': dispense_speed, 'swap_speed': swap_speed, 'soak_time': soak_time, 'wash_cycles': wash_cycles, 'minimal_height_at_command_end': minimal_height_at_command_end}
        _kw.update(kwargs)
        return self.call('wash_tips', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_initialize(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('x_arm_initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_move_arm_relatively_in_x(self, x_search_distance=None, x_speed=None, TODO_XS_1=None, **kwargs):
        _kw = {'x_search_distance': x_search_distance, 'x_speed': x_speed, 'TODO_XS_1': TODO_XS_1}
        _kw.update(kwargs)
        return self.call('x_arm_move_arm_relatively_in_x', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_move_to_x_position(self, x_position=None, x_speed=None, TODO_XI_1=None, **kwargs):
        _kw = {'x_position': x_position, 'x_speed': x_speed, 'TODO_XI_1': TODO_XI_1}
        _kw.update(kwargs)
        return self.call('x_arm_move_to_x_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_move_to_x_position_with_all_attached_components_in_z_safety_position(self, x_position=None, x_speed=None, TODO_XA_1=None, **kwargs):
        _kw = {'x_position': x_position, 'x_speed': x_speed, 'TODO_XA_1': TODO_XA_1}
        _kw.update(kwargs)
        return self.call('x_arm_move_to_x_position_with_all_attached_components_in_z_safety_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_request_arm_x_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('x_arm_request_arm_x_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_request_error_code(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('x_arm_request_error_code', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_request_x_drive_recorded_data(self, TODO_QL_1=None, TODO_QL_2=None, **kwargs):
        _kw = {'TODO_QL_1': TODO_QL_1, 'TODO_QL_2': TODO_QL_2}
        _kw.update(kwargs)
        return self.call('x_arm_request_x_drive_recorded_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_search_x_for_teach_signal(self, x_search_distance=None, x_speed=None, TODO_XT_1=None, **kwargs):
        _kw = {'x_search_distance': x_search_distance, 'x_speed': x_speed, 'TODO_XT_1': TODO_XT_1}
        _kw.update(kwargs)
        return self.call('x_arm_search_x_for_teach_signal', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_send_message_to_motion_controller(self, TODO_BD_1=None, **kwargs):
        _kw = {'TODO_BD_1': TODO_BD_1}
        _kw.update(kwargs)
        return self.call('x_arm_send_message_to_motion_controller', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_set_any_parameter_within_this_module(self, TODO_AA_1=None, TODO_AA_2=None, **kwargs):
        _kw = {'TODO_AA_1': TODO_AA_1, 'TODO_AA_2': TODO_AA_2}
        _kw.update(kwargs)
        return self.call('x_arm_set_any_parameter_within_this_module', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_set_x_drive_angle_of_alignment(self, TODO_XL_1=None, **kwargs):
        _kw = {'TODO_XL_1': TODO_XL_1}
        _kw.update(kwargs)
        return self.call('x_arm_set_x_drive_angle_of_alignment', kwargs={k: v for k, v in _kw.items() if v is not None})

    def x_arm_turn_x_drive_off(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('x_arm_turn_x_drive_off', kwargs={k: v for k, v in _kw.items() if v is not None})

