from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBrooksPf400(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/arms/precise_flex/precise_flex_backend.py', 'class_name': 'PreciseFlexBackend', 'import_roots': [], 'candidate_methods': ['approach', 'are_grippers_closed', 'attach', 'change_config', 'change_config2', 'close_gripper', 'dest_c', 'dest_j', 'detach', 'drop_resource', 'end_freedrive_mode', 'exit', 'freedrive_mode', 'get_active_gripper', 'get_base', 'get_cartesian_position', 'get_grasp_data', 'get_joint_position', 'get_location_angles', 'get_location_config', 'get_location_xyz', 'get_location_z_clearance', 'get_mode', 'get_monitor_speed', 'get_motion_profile_values', 'get_pallet_index', 'get_pallet_origin', 'get_pallet_x', 'get_pallet_y', 'get_pallet_z', 'get_parameter', 'get_payload', 'get_power_state', 'get_profile_accel', 'get_profile_accel_ramp', 'get_profile_decel', 'get_profile_decel_ramp', 'get_profile_in_range', 'get_profile_speed', 'get_profile_speed2', 'get_profile_straight', 'get_rail_position', 'get_selected_robot', 'get_signal', 'get_speed', 'get_station_type', 'get_system_state', 'get_tool_transformation_values', 'get_version', 'halt', 'here_c', 'here_j', 'home', 'home_all', 'home_all_if_no_plate', 'is_gripper_closed', 'move_c', 'move_extra_axis', 'move_j', 'move_one_axis', 'move_rail', 'move_to', 'move_to_safe', 'move_to_stored_location', 'move_to_stored_location_appro', 'nop', 'open_gripper', 'pick_plate_from_stored_position', 'pick_plate_station', 'pick_up_resource', 'place_plate_station', 'place_plate_to_stored_position', 'power_off_robot', 'power_on_robot', 'release_brake', 'reset', 'select_robot', 'set_active_gripper', 'set_base', 'set_brake', 'set_grasp_data', 'set_joint_angles', 'set_location_config', 'set_location_xyz', 'set_location_z_clearance', 'set_monitor_speed', 'set_motion_profile_values', 'set_pallet_index', 'set_pallet_origin', 'set_pallet_x', 'set_pallet_y', 'set_pallet_z', 'set_parameter', 'set_payload', 'set_power', 'set_profile_accel', 'set_profile_accel_ramp', 'set_profile_decel', 'set_profile_decel_ramp', 'set_profile_in_range', 'set_profile_speed', 'set_profile_speed2', 'set_profile_straight', 'set_rail_position', 'set_response_mode', 'set_signal', 'set_speed', 'set_station_type', 'set_tool_transformation_values', 'setup', 'state', 'stop', 'teach_plate_station', 'teach_position', 'wait_for_eom', 'zero_torque'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Brooks Automation', 'model': 'PF400', 'device_type_cn': '机械臂', 'device_type_en': 'Robotic Arm', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/arms/precise_flex/precise_flex_backend.py', 'class_name': 'PreciseFlexBackend', 'candidate_methods': ['approach', 'are_grippers_closed', 'attach', 'change_config', 'change_config2', 'close_gripper', 'dest_c', 'dest_j', 'detach', 'drop_resource', 'end_freedrive_mode', 'exit', 'freedrive_mode', 'get_active_gripper', 'get_base', 'get_cartesian_position', 'get_grasp_data', 'get_joint_position', 'get_location_angles', 'get_location_config', 'get_location_xyz', 'get_location_z_clearance', 'get_mode', 'get_monitor_speed', 'get_motion_profile_values', 'get_pallet_index', 'get_pallet_origin', 'get_pallet_x', 'get_pallet_y', 'get_pallet_z', 'get_parameter', 'get_payload', 'get_power_state', 'get_profile_accel', 'get_profile_accel_ramp', 'get_profile_decel', 'get_profile_decel_ramp', 'get_profile_in_range', 'get_profile_speed', 'get_profile_speed2', 'get_profile_straight', 'get_rail_position', 'get_selected_robot', 'get_signal', 'get_speed', 'get_station_type', 'get_system_state', 'get_tool_transformation_values', 'get_version', 'halt', 'here_c', 'here_j', 'home', 'home_all', 'home_all_if_no_plate', 'is_gripper_closed', 'move_c', 'move_extra_axis', 'move_j', 'move_one_axis', 'move_rail', 'move_to', 'move_to_safe', 'move_to_stored_location', 'move_to_stored_location_appro', 'nop', 'open_gripper', 'pick_plate_from_stored_position', 'pick_plate_station', 'pick_up_resource', 'place_plate_station', 'place_plate_to_stored_position', 'power_off_robot', 'power_on_robot', 'release_brake', 'reset', 'select_robot', 'set_active_gripper', 'set_base', 'set_brake', 'set_grasp_data', 'set_joint_angles', 'set_location_config', 'set_location_xyz', 'set_location_z_clearance', 'set_monitor_speed', 'set_motion_profile_values', 'set_pallet_index', 'set_pallet_origin', 'set_pallet_x', 'set_pallet_y', 'set_pallet_z', 'set_parameter', 'set_payload', 'set_power', 'set_profile_accel', 'set_profile_accel_ramp', 'set_profile_decel', 'set_profile_decel_ramp', 'set_profile_in_range', 'set_profile_speed', 'set_profile_speed2', 'set_profile_straight', 'set_rail_position', 'set_response_mode', 'set_signal', 'set_speed', 'set_station_type', 'set_tool_transformation_values', 'setup', 'state', 'stop', 'teach_plate_station', 'teach_position', 'wait_for_eom', 'zero_torque']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def approach(self, position=None, access=None, **kwargs):
        _kw = {'position': position, 'access': access}
        _kw.update(kwargs)
        return self.call('approach', kwargs={k: v for k, v in _kw.items() if v is not None})

    def are_grippers_closed(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('are_grippers_closed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def attach(self, attach_state=None, **kwargs):
        _kw = {'attach_state': attach_state}
        _kw.update(kwargs)
        return self.call('attach', kwargs={k: v for k, v in _kw.items() if v is not None})

    def change_config(self, grip_mode=None, **kwargs):
        _kw = {'grip_mode': grip_mode}
        _kw.update(kwargs)
        return self.call('change_config', kwargs={k: v for k, v in _kw.items() if v is not None})

    def change_config2(self, grip_mode=None, **kwargs):
        _kw = {'grip_mode': grip_mode}
        _kw.update(kwargs)
        return self.call('change_config2', kwargs={k: v for k, v in _kw.items() if v is not None})

    def close_gripper(self, gripper_width=None, **kwargs):
        _kw = {'gripper_width': gripper_width}
        _kw.update(kwargs)
        return self.call('close_gripper', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dest_c(self, arg1=None, **kwargs):
        _kw = {'arg1': arg1}
        _kw.update(kwargs)
        return self.call('dest_c', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dest_j(self, arg1=None, **kwargs):
        _kw = {'arg1': arg1}
        _kw.update(kwargs)
        return self.call('dest_j', kwargs={k: v for k, v in _kw.items() if v is not None})

    def detach(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('detach', kwargs={k: v for k, v in _kw.items() if v is not None})

    def drop_resource(self, position=None, access=None, **kwargs):
        _kw = {'position': position, 'access': access}
        _kw.update(kwargs)
        return self.call('drop_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def end_freedrive_mode(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('end_freedrive_mode', kwargs={k: v for k, v in _kw.items() if v is not None})

    def exit(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('exit', kwargs={k: v for k, v in _kw.items() if v is not None})

    def freedrive_mode(self, free_axes=None, **kwargs):
        _kw = {'free_axes': free_axes}
        _kw.update(kwargs)
        return self.call('freedrive_mode', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_active_gripper(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_active_gripper', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_base(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_base', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_cartesian_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_cartesian_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_grasp_data(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_grasp_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_joint_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_joint_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_location_angles(self, location_index=None, **kwargs):
        _kw = {'location_index': location_index}
        _kw.update(kwargs)
        return self.call('get_location_angles', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_location_config(self, location_index=None, **kwargs):
        _kw = {'location_index': location_index}
        _kw.update(kwargs)
        return self.call('get_location_config', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_location_xyz(self, location_index=None, **kwargs):
        _kw = {'location_index': location_index}
        _kw.update(kwargs)
        return self.call('get_location_xyz', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_location_z_clearance(self, location_index=None, **kwargs):
        _kw = {'location_index': location_index}
        _kw.update(kwargs)
        return self.call('get_location_z_clearance', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_mode(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_mode', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_monitor_speed(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_monitor_speed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_motion_profile_values(self, profile=None, **kwargs):
        _kw = {'profile': profile}
        _kw.update(kwargs)
        return self.call('get_motion_profile_values', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_pallet_index(self, station_id=None, **kwargs):
        _kw = {'station_id': station_id}
        _kw.update(kwargs)
        return self.call('get_pallet_index', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_pallet_origin(self, station_id=None, **kwargs):
        _kw = {'station_id': station_id}
        _kw.update(kwargs)
        return self.call('get_pallet_origin', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_pallet_x(self, station_id=None, **kwargs):
        _kw = {'station_id': station_id}
        _kw.update(kwargs)
        return self.call('get_pallet_x', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_pallet_y(self, station_id=None, **kwargs):
        _kw = {'station_id': station_id}
        _kw.update(kwargs)
        return self.call('get_pallet_y', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_pallet_z(self, station_id=None, **kwargs):
        _kw = {'station_id': station_id}
        _kw.update(kwargs)
        return self.call('get_pallet_z', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_parameter(self, data_id=None, unit_number=None, sub_unit=None, array_index=None, **kwargs):
        _kw = {'data_id': data_id, 'unit_number': unit_number, 'sub_unit': sub_unit, 'array_index': array_index}
        _kw.update(kwargs)
        return self.call('get_parameter', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_payload(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_payload', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_power_state(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_power_state', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_profile_accel(self, profile_index=None, **kwargs):
        _kw = {'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('get_profile_accel', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_profile_accel_ramp(self, profile_index=None, **kwargs):
        _kw = {'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('get_profile_accel_ramp', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_profile_decel(self, profile_index=None, **kwargs):
        _kw = {'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('get_profile_decel', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_profile_decel_ramp(self, profile_index=None, **kwargs):
        _kw = {'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('get_profile_decel_ramp', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_profile_in_range(self, profile_index=None, **kwargs):
        _kw = {'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('get_profile_in_range', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_profile_speed(self, profile_index=None, **kwargs):
        _kw = {'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('get_profile_speed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_profile_speed2(self, profile_index=None, **kwargs):
        _kw = {'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('get_profile_speed2', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_profile_straight(self, profile_index=None, **kwargs):
        _kw = {'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('get_profile_straight', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_rail_position(self, station_id=None, **kwargs):
        _kw = {'station_id': station_id}
        _kw.update(kwargs)
        return self.call('get_rail_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_selected_robot(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_selected_robot', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_signal(self, signal_number=None, **kwargs):
        _kw = {'signal_number': signal_number}
        _kw.update(kwargs)
        return self.call('get_signal', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_speed(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_speed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_station_type(self, station_id=None, **kwargs):
        _kw = {'station_id': station_id}
        _kw.update(kwargs)
        return self.call('get_station_type', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_system_state(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_system_state', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_tool_transformation_values(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_tool_transformation_values', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_version(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_version', kwargs={k: v for k, v in _kw.items() if v is not None})

    def halt(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('halt', kwargs={k: v for k, v in _kw.items() if v is not None})

    def here_c(self, location_index=None, **kwargs):
        _kw = {'location_index': location_index}
        _kw.update(kwargs)
        return self.call('here_c', kwargs={k: v for k, v in _kw.items() if v is not None})

    def here_j(self, location_index=None, **kwargs):
        _kw = {'location_index': location_index}
        _kw.update(kwargs)
        return self.call('here_j', kwargs={k: v for k, v in _kw.items() if v is not None})

    def home(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('home', kwargs={k: v for k, v in _kw.items() if v is not None})

    def home_all(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('home_all', kwargs={k: v for k, v in _kw.items() if v is not None})

    def home_all_if_no_plate(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('home_all_if_no_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def is_gripper_closed(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('is_gripper_closed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_c(self, profile_index=None, cartesian_coords=None, **kwargs):
        _kw = {'profile_index': profile_index, 'cartesian_coords': cartesian_coords}
        _kw.update(kwargs)
        return self.call('move_c', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_extra_axis(self, axis1_position=None, axis2_position=None, **kwargs):
        _kw = {'axis1_position': axis1_position, 'axis2_position': axis2_position}
        _kw.update(kwargs)
        return self.call('move_extra_axis', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_j(self, profile_index=None, joint_coords=None, **kwargs):
        _kw = {'profile_index': profile_index, 'joint_coords': joint_coords}
        _kw.update(kwargs)
        return self.call('move_j', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_one_axis(self, axis_number=None, destination_position=None, profile_index=None, **kwargs):
        _kw = {'axis_number': axis_number, 'destination_position': destination_position, 'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('move_one_axis', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_rail(self, station_id=None, mode=None, rail_destination=None, **kwargs):
        _kw = {'station_id': station_id, 'mode': mode, 'rail_destination': rail_destination}
        _kw.update(kwargs)
        return self.call('move_rail', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_to(self, position=None, **kwargs):
        _kw = {'position': position}
        _kw.update(kwargs)
        return self.call('move_to', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_to_safe(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('move_to_safe', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_to_stored_location(self, location_index=None, profile_index=None, **kwargs):
        _kw = {'location_index': location_index, 'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('move_to_stored_location', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_to_stored_location_appro(self, location_index=None, profile_index=None, **kwargs):
        _kw = {'location_index': location_index, 'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('move_to_stored_location_appro', kwargs={k: v for k, v in _kw.items() if v is not None})

    def nop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('nop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open_gripper(self, gripper_width=None, **kwargs):
        _kw = {'gripper_width': gripper_width}
        _kw.update(kwargs)
        return self.call('open_gripper', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_plate_from_stored_position(self, position_id=None, horizontal_compliance=None, horizontal_compliance_torque=None, **kwargs):
        _kw = {'position_id': position_id, 'horizontal_compliance': horizontal_compliance, 'horizontal_compliance_torque': horizontal_compliance_torque}
        _kw.update(kwargs)
        return self.call('pick_plate_from_stored_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_plate_station(self, station_id=None, horizontal_compliance=None, horizontal_compliance_torque=None, **kwargs):
        _kw = {'station_id': station_id, 'horizontal_compliance': horizontal_compliance, 'horizontal_compliance_torque': horizontal_compliance_torque}
        _kw.update(kwargs)
        return self.call('pick_plate_station', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_resource(self, position=None, plate_width=None, access=None, finger_speed_percent=None, grasp_force=None, **kwargs):
        _kw = {'position': position, 'plate_width': plate_width, 'access': access, 'finger_speed_percent': finger_speed_percent, 'grasp_force': grasp_force}
        _kw.update(kwargs)
        return self.call('pick_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def place_plate_station(self, station_id=None, horizontal_compliance=None, horizontal_compliance_torque=None, **kwargs):
        _kw = {'station_id': station_id, 'horizontal_compliance': horizontal_compliance, 'horizontal_compliance_torque': horizontal_compliance_torque}
        _kw.update(kwargs)
        return self.call('place_plate_station', kwargs={k: v for k, v in _kw.items() if v is not None})

    def place_plate_to_stored_position(self, position_id=None, horizontal_compliance=None, horizontal_compliance_torque=None, **kwargs):
        _kw = {'position_id': position_id, 'horizontal_compliance': horizontal_compliance, 'horizontal_compliance_torque': horizontal_compliance_torque}
        _kw.update(kwargs)
        return self.call('place_plate_to_stored_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def power_off_robot(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('power_off_robot', kwargs={k: v for k, v in _kw.items() if v is not None})

    def power_on_robot(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('power_on_robot', kwargs={k: v for k, v in _kw.items() if v is not None})

    def release_brake(self, axis=None, **kwargs):
        _kw = {'axis': axis}
        _kw.update(kwargs)
        return self.call('release_brake', kwargs={k: v for k, v in _kw.items() if v is not None})

    def reset(self, robot_number=None, **kwargs):
        _kw = {'robot_number': robot_number}
        _kw.update(kwargs)
        return self.call('reset', kwargs={k: v for k, v in _kw.items() if v is not None})

    def select_robot(self, robot_number=None, **kwargs):
        _kw = {'robot_number': robot_number}
        _kw.update(kwargs)
        return self.call('select_robot', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_active_gripper(self, gripper_id=None, spin_mode=None, profile_index=None, **kwargs):
        _kw = {'gripper_id': gripper_id, 'spin_mode': spin_mode, 'profile_index': profile_index}
        _kw.update(kwargs)
        return self.call('set_active_gripper', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_base(self, x_offset=None, y_offset=None, z_offset=None, z_rotation=None, **kwargs):
        _kw = {'x_offset': x_offset, 'y_offset': y_offset, 'z_offset': z_offset, 'z_rotation': z_rotation}
        _kw.update(kwargs)
        return self.call('set_base', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_brake(self, axis=None, **kwargs):
        _kw = {'axis': axis}
        _kw.update(kwargs)
        return self.call('set_brake', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_grasp_data(self, plate_width=None, finger_speed_percent=None, grasp_force=None, **kwargs):
        _kw = {'plate_width': plate_width, 'finger_speed_percent': finger_speed_percent, 'grasp_force': grasp_force}
        _kw.update(kwargs)
        return self.call('set_grasp_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_joint_angles(self, location_index=None, joint_position=None, **kwargs):
        _kw = {'location_index': location_index, 'joint_position': joint_position}
        _kw.update(kwargs)
        return self.call('set_joint_angles', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_location_config(self, location_index=None, config_value=None, **kwargs):
        _kw = {'location_index': location_index, 'config_value': config_value}
        _kw.update(kwargs)
        return self.call('set_location_config', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_location_xyz(self, location_index=None, cartesian_position=None, **kwargs):
        _kw = {'location_index': location_index, 'cartesian_position': cartesian_position}
        _kw.update(kwargs)
        return self.call('set_location_xyz', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_location_z_clearance(self, location_index=None, z_clearance=None, z_world=None, **kwargs):
        _kw = {'location_index': location_index, 'z_clearance': z_clearance, 'z_world': z_world}
        _kw.update(kwargs)
        return self.call('set_location_z_clearance', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_monitor_speed(self, speed_percent=None, **kwargs):
        _kw = {'speed_percent': speed_percent}
        _kw.update(kwargs)
        return self.call('set_monitor_speed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_motion_profile_values(self, profile=None, speed=None, speed2=None, acceleration=None, deceleration=None, acceleration_ramp=None, deceleration_ramp=None, in_range=None, straight=None, **kwargs):
        _kw = {'profile': profile, 'speed': speed, 'speed2': speed2, 'acceleration': acceleration, 'deceleration': deceleration, 'acceleration_ramp': acceleration_ramp, 'deceleration_ramp': deceleration_ramp, 'in_range': in_range, 'straight': straight}
        _kw.update(kwargs)
        return self.call('set_motion_profile_values', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_pallet_index(self, station_id=None, pallet_index_x=None, pallet_index_y=None, pallet_index_z=None, **kwargs):
        _kw = {'station_id': station_id, 'pallet_index_x': pallet_index_x, 'pallet_index_y': pallet_index_y, 'pallet_index_z': pallet_index_z}
        _kw.update(kwargs)
        return self.call('set_pallet_index', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_pallet_origin(self, station_id=None, cartesian_coords=None, **kwargs):
        _kw = {'station_id': station_id, 'cartesian_coords': cartesian_coords}
        _kw.update(kwargs)
        return self.call('set_pallet_origin', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_pallet_x(self, station_id=None, x_position_count=None, world_x=None, world_y=None, world_z=None, **kwargs):
        _kw = {'station_id': station_id, 'x_position_count': x_position_count, 'world_x': world_x, 'world_y': world_y, 'world_z': world_z}
        _kw.update(kwargs)
        return self.call('set_pallet_x', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_pallet_y(self, station_id=None, y_position_count=None, world_x=None, world_y=None, world_z=None, **kwargs):
        _kw = {'station_id': station_id, 'y_position_count': y_position_count, 'world_x': world_x, 'world_y': world_y, 'world_z': world_z}
        _kw.update(kwargs)
        return self.call('set_pallet_y', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_pallet_z(self, station_id=None, z_position_count=None, world_x=None, world_y=None, world_z=None, **kwargs):
        _kw = {'station_id': station_id, 'z_position_count': z_position_count, 'world_x': world_x, 'world_y': world_y, 'world_z': world_z}
        _kw.update(kwargs)
        return self.call('set_pallet_z', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_parameter(self, data_id=None, value=None, unit_number=None, sub_unit=None, array_index=None, **kwargs):
        _kw = {'data_id': data_id, 'value': value, 'unit_number': unit_number, 'sub_unit': sub_unit, 'array_index': array_index}
        _kw.update(kwargs)
        return self.call('set_parameter', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_payload(self, payload_percent=None, **kwargs):
        _kw = {'payload_percent': payload_percent}
        _kw.update(kwargs)
        return self.call('set_payload', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_power(self, enable=None, timeout=None, **kwargs):
        _kw = {'enable': enable, 'timeout': timeout}
        _kw.update(kwargs)
        return self.call('set_power', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_profile_accel(self, profile_index=None, accel_percent=None, **kwargs):
        _kw = {'profile_index': profile_index, 'accel_percent': accel_percent}
        _kw.update(kwargs)
        return self.call('set_profile_accel', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_profile_accel_ramp(self, profile_index=None, accel_ramp_seconds=None, **kwargs):
        _kw = {'profile_index': profile_index, 'accel_ramp_seconds': accel_ramp_seconds}
        _kw.update(kwargs)
        return self.call('set_profile_accel_ramp', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_profile_decel(self, profile_index=None, decel_percent=None, **kwargs):
        _kw = {'profile_index': profile_index, 'decel_percent': decel_percent}
        _kw.update(kwargs)
        return self.call('set_profile_decel', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_profile_decel_ramp(self, profile_index=None, decel_ramp_seconds=None, **kwargs):
        _kw = {'profile_index': profile_index, 'decel_ramp_seconds': decel_ramp_seconds}
        _kw.update(kwargs)
        return self.call('set_profile_decel_ramp', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_profile_in_range(self, profile_index=None, in_range_value=None, **kwargs):
        _kw = {'profile_index': profile_index, 'in_range_value': in_range_value}
        _kw.update(kwargs)
        return self.call('set_profile_in_range', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_profile_speed(self, profile_index=None, speed_percent=None, **kwargs):
        _kw = {'profile_index': profile_index, 'speed_percent': speed_percent}
        _kw.update(kwargs)
        return self.call('set_profile_speed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_profile_speed2(self, profile_index=None, speed2_percent=None, **kwargs):
        _kw = {'profile_index': profile_index, 'speed2_percent': speed2_percent}
        _kw.update(kwargs)
        return self.call('set_profile_speed2', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_profile_straight(self, profile_index=None, straight_mode=None, **kwargs):
        _kw = {'profile_index': profile_index, 'straight_mode': straight_mode}
        _kw.update(kwargs)
        return self.call('set_profile_straight', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_rail_position(self, station_id=None, rail_position=None, **kwargs):
        _kw = {'station_id': station_id, 'rail_position': rail_position}
        _kw.update(kwargs)
        return self.call('set_rail_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_response_mode(self, mode=None, **kwargs):
        _kw = {'mode': mode}
        _kw.update(kwargs)
        return self.call('set_response_mode', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_signal(self, signal_number=None, value=None, **kwargs):
        _kw = {'signal_number': signal_number, 'value': value}
        _kw.update(kwargs)
        return self.call('set_signal', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_speed(self, speed_percent=None, **kwargs):
        _kw = {'speed_percent': speed_percent}
        _kw.update(kwargs)
        return self.call('set_speed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_station_type(self, station_id=None, access_type=None, location_type=None, z_clearance=None, z_above=None, z_grasp_offset=None, **kwargs):
        _kw = {'station_id': station_id, 'access_type': access_type, 'location_type': location_type, 'z_clearance': z_clearance, 'z_above': z_above, 'z_grasp_offset': z_grasp_offset}
        _kw.update(kwargs)
        return self.call('set_station_type', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_tool_transformation_values(self, x=None, y=None, z=None, yaw=None, pitch=None, roll=None, **kwargs):
        _kw = {'x': x, 'y': y, 'z': z, 'yaw': yaw, 'pitch': pitch, 'roll': roll}
        _kw.update(kwargs)
        return self.call('set_tool_transformation_values', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, skip_home=None, **kwargs):
        _kw = {'skip_home': skip_home}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def state(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('state', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def teach_plate_station(self, station_id=None, z_clearance=None, **kwargs):
        _kw = {'station_id': station_id, 'z_clearance': z_clearance}
        _kw.update(kwargs)
        return self.call('teach_plate_station', kwargs={k: v for k, v in _kw.items() if v is not None})

    def teach_position(self, position_id=None, z_clearance=None, **kwargs):
        _kw = {'position_id': position_id, 'z_clearance': z_clearance}
        _kw.update(kwargs)
        return self.call('teach_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def wait_for_eom(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('wait_for_eom', kwargs={k: v for k, v in _kw.items() if v is not None})

    def zero_torque(self, enable=None, axis_mask=None, **kwargs):
        _kw = {'enable': enable, 'axis_mask': axis_mask}
        _kw.update(kwargs)
        return self.call('zero_torque', kwargs={k: v for k, v in _kw.items() if v is not None})

