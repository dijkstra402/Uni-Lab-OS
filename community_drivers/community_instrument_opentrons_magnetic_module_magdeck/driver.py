from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOpentronsMagneticModuleMagdeck(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Opentrons__opentrons', 'source_file': 'api/src/opentrons/hardware_control/ot3api.py', 'class_name': 'OT3API', 'import_roots': [], 'candidate_methods': ['is_idle_mount', 'door_state', 'module_door_serial', 'gantry_load', 'set_gantry_load', 'get_serial_number', 'set_system_constraints_for_plunger_acceleration', 'restore_system_constrants', 'grab_pressure', 'get_deck_from_machine', 'build_hardware_controller', 'build_hardware_simulator', 'loop', 'is_simulator', 'register_callback', 'get_fw_version', 'fw_version', 'board_revision', 'update_firmware', 'set_lights', 'get_lights', 'identify', 'set_status_bar_state', 'set_status_bar_enabled', 'get_status_bar_enabled', 'get_status_bar_state', 'add_status_bar_listener', 'delay', 'attached_modules', 'create_simulating_module', 'cache_pipette', 'get_pressure_sensor_available', 'cache_gripper', 'get_all_attached_instr', 'cache_instruments', 'reset_tip_detectors', 'pause', 'pause_with_message', 'resume', 'is_movement_execution_taskified', 'should_taskify_movement_execution', 'cancel_execution_and_running_tasks', 'halt', 'stop', 'reset', 'home_z', 'home_gripper_jaw', 'home_plunger', 'home_gear_motors', 'current_position', 'current_position_ot3', 'refresh_positions', 'motor_status_ok', 'encoder_status_ok', 'encoder_current_position', 'encoder_current_position_ot3', 'gantry_position', 'update_axis_position_estimations', 'move_to', 'move_axes', 'move_rel', 'prepare_for_mount_movement', 'idle_gripper', 'raise_error_if_gripper_pickup_failed', 'gripper_jaw_can_home', 'home', 'get_engaged_axes', 'engaged_axes', 'disengage_axes', 'engage_axes', 'axis_is_present', 'get_limit_switches', 'retract', 'retract_axis', 'config', 'get_config', 'set_config', 'update_config', 'hardware_feature_flags', 'grip', 'ungrip', 'hold_jaw_width', 'tip_pickup_moves', 'configure_for_volume', 'set_liquid_class', 'prepare_for_aspirate', 'aspirate', 'dispense', 'blow_out', 'get_tip_presence_status', 'verify_tip_presence', 'pick_up_tip', 'set_current_tiprack_diameter', 'set_working_volume', 'tip_drop_moves', 'drop_tip', 'clean_up', 'critical_point_for', 'hardware_pipettes', 'hardware_gripper', 'hardware_instruments', 'get_attached_pipettes', 'get_attached_instruments', 'get_instrument_state', 'reset_instrument', 'get_instrument_offset', 'reset_instrument_offset', 'save_instrument_offset', 'save_module_offset', 'get_module_calibration_offset', 'get_attached_pipette', 'get_attached_instrument', 'attached_instruments', 'attached_pipettes', 'attached_gripper', 'has_gripper', 'calibrate_plunger', 'set_flow_rate', 'set_pipette_speed', 'get_instrument_max_height', 'update_nozzle_configuration_for_mount', 'add_tip', 'cache_tip', 'remove_tip', 'add_gripper_probe', 'remove_gripper_probe', 'liquid_probe_non_responsive_z_distance', 'liquid_probe', 'capacitive_probe', 'capacitive_sweep', 'aspirate_while_tracking', 'dispense_while_tracking', 'attached_subsystems', 'estop_status', 'estop_acknowledge_and_clear', 'get_estop_state', 'set_hepa_fan_state', 'get_hepa_fan_state', 'set_hepa_uv_state', 'get_hepa_uv_state', 'increase_evo_disp_count', 'read_stem_temperature', 'read_stem_humidity', 'read_stem_pressure', 'read_stem_capacitance', 'touch_probe', 'taskify_movement_execution', 'execution_manager', 'wait_for_running', 'do_delay', 'robot_calibration', 'reset_robot_calibration', 'reset_deck_calibration', 'load_deck_calibration', 'set_robot_calibration', 'validate_calibration', 'build_temporary_identity_calibration', 'get_robot_type', 'file_path', 'short_sha', 'to_json', 'from_dict', 'from_json'], 'action_targets': {}, 'metadata': {'repo': 'Opentrons/opentrons', 'repo_url': 'https://github.com/Opentrons/opentrons', 'brand': 'Opentrons', 'model': 'Magnetic Module (MagDeck)', 'device_type_cn': '磁珠纯化模块', 'device_type_en': 'Magnetic Bead Purification Module', 'source_framework': 'Opentrons SDK', 'tag_id': '4432', 'tag_name': '磁珠纯化模块', 'tag_name_en': 'Magnetic Bead Purification Module', 'candidate_score': 1206, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def is_idle_mount(self, **kwargs):
        return self.call('is_idle_mount', kwargs=kwargs)

    def door_state(self, **kwargs):
        return self.call('door_state', kwargs=kwargs)

    def module_door_serial(self, **kwargs):
        return self.call('module_door_serial', kwargs=kwargs)

    def gantry_load(self, **kwargs):
        return self.call('gantry_load', kwargs=kwargs)

    def set_gantry_load(self, **kwargs):
        return self.call('set_gantry_load', kwargs=kwargs)

    def get_serial_number(self, **kwargs):
        return self.call('get_serial_number', kwargs=kwargs)

    def set_system_constraints_for_plunger_acceleration(self, **kwargs):
        return self.call('set_system_constraints_for_plunger_acceleration', kwargs=kwargs)

    def restore_system_constrants(self, **kwargs):
        return self.call('restore_system_constrants', kwargs=kwargs)

    def grab_pressure(self, **kwargs):
        return self.call('grab_pressure', kwargs=kwargs)

    def get_deck_from_machine(self, **kwargs):
        return self.call('get_deck_from_machine', kwargs=kwargs)

    def build_hardware_controller(self, **kwargs):
        return self.call('build_hardware_controller', kwargs=kwargs)

    def build_hardware_simulator(self, **kwargs):
        return self.call('build_hardware_simulator', kwargs=kwargs)

    def loop(self, **kwargs):
        return self.call('loop', kwargs=kwargs)

    def is_simulator(self, **kwargs):
        return self.call('is_simulator', kwargs=kwargs)

    def register_callback(self, **kwargs):
        return self.call('register_callback', kwargs=kwargs)

    def get_fw_version(self, **kwargs):
        return self.call('get_fw_version', kwargs=kwargs)

    def fw_version(self, **kwargs):
        return self.call('fw_version', kwargs=kwargs)

    def board_revision(self, **kwargs):
        return self.call('board_revision', kwargs=kwargs)

    def update_firmware(self, **kwargs):
        return self.call('update_firmware', kwargs=kwargs)

    def set_lights(self, **kwargs):
        return self.call('set_lights', kwargs=kwargs)

    def get_lights(self, **kwargs):
        return self.call('get_lights', kwargs=kwargs)

    def identify(self, **kwargs):
        return self.call('identify', kwargs=kwargs)

    def set_status_bar_state(self, **kwargs):
        return self.call('set_status_bar_state', kwargs=kwargs)

    def set_status_bar_enabled(self, **kwargs):
        return self.call('set_status_bar_enabled', kwargs=kwargs)

    def get_status_bar_enabled(self, **kwargs):
        return self.call('get_status_bar_enabled', kwargs=kwargs)

    def get_status_bar_state(self, **kwargs):
        return self.call('get_status_bar_state', kwargs=kwargs)

    def add_status_bar_listener(self, **kwargs):
        return self.call('add_status_bar_listener', kwargs=kwargs)

    def delay(self, **kwargs):
        return self.call('delay', kwargs=kwargs)

    def attached_modules(self, **kwargs):
        return self.call('attached_modules', kwargs=kwargs)

    def create_simulating_module(self, **kwargs):
        return self.call('create_simulating_module', kwargs=kwargs)

    def cache_pipette(self, **kwargs):
        return self.call('cache_pipette', kwargs=kwargs)

    def get_pressure_sensor_available(self, **kwargs):
        return self.call('get_pressure_sensor_available', kwargs=kwargs)

    def cache_gripper(self, **kwargs):
        return self.call('cache_gripper', kwargs=kwargs)

    def get_all_attached_instr(self, **kwargs):
        return self.call('get_all_attached_instr', kwargs=kwargs)

    def cache_instruments(self, **kwargs):
        return self.call('cache_instruments', kwargs=kwargs)

    def reset_tip_detectors(self, **kwargs):
        return self.call('reset_tip_detectors', kwargs=kwargs)

    def pause(self, **kwargs):
        return self.call('pause', kwargs=kwargs)

    def pause_with_message(self, **kwargs):
        return self.call('pause_with_message', kwargs=kwargs)

    def resume(self, **kwargs):
        return self.call('resume', kwargs=kwargs)

    def is_movement_execution_taskified(self, **kwargs):
        return self.call('is_movement_execution_taskified', kwargs=kwargs)

    def should_taskify_movement_execution(self, **kwargs):
        return self.call('should_taskify_movement_execution', kwargs=kwargs)

    def cancel_execution_and_running_tasks(self, **kwargs):
        return self.call('cancel_execution_and_running_tasks', kwargs=kwargs)

    def halt(self, **kwargs):
        return self.call('halt', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def home_z(self, **kwargs):
        return self.call('home_z', kwargs=kwargs)

    def home_gripper_jaw(self, **kwargs):
        return self.call('home_gripper_jaw', kwargs=kwargs)

    def home_plunger(self, **kwargs):
        return self.call('home_plunger', kwargs=kwargs)

    def home_gear_motors(self, **kwargs):
        return self.call('home_gear_motors', kwargs=kwargs)

    def current_position(self, **kwargs):
        return self.call('current_position', kwargs=kwargs)

    def current_position_ot3(self, **kwargs):
        return self.call('current_position_ot3', kwargs=kwargs)

    def refresh_positions(self, **kwargs):
        return self.call('refresh_positions', kwargs=kwargs)

    def motor_status_ok(self, **kwargs):
        return self.call('motor_status_ok', kwargs=kwargs)

    def encoder_status_ok(self, **kwargs):
        return self.call('encoder_status_ok', kwargs=kwargs)

    def encoder_current_position(self, **kwargs):
        return self.call('encoder_current_position', kwargs=kwargs)

    def encoder_current_position_ot3(self, **kwargs):
        return self.call('encoder_current_position_ot3', kwargs=kwargs)

    def gantry_position(self, **kwargs):
        return self.call('gantry_position', kwargs=kwargs)

    def update_axis_position_estimations(self, **kwargs):
        return self.call('update_axis_position_estimations', kwargs=kwargs)

    def move_to(self, **kwargs):
        return self.call('move_to', kwargs=kwargs)

    def move_axes(self, **kwargs):
        return self.call('move_axes', kwargs=kwargs)

    def move_rel(self, **kwargs):
        return self.call('move_rel', kwargs=kwargs)

    def prepare_for_mount_movement(self, **kwargs):
        return self.call('prepare_for_mount_movement', kwargs=kwargs)

    def idle_gripper(self, **kwargs):
        return self.call('idle_gripper', kwargs=kwargs)

    def raise_error_if_gripper_pickup_failed(self, **kwargs):
        return self.call('raise_error_if_gripper_pickup_failed', kwargs=kwargs)

    def gripper_jaw_can_home(self, **kwargs):
        return self.call('gripper_jaw_can_home', kwargs=kwargs)

    def home(self, **kwargs):
        return self.call('home', kwargs=kwargs)

    def get_engaged_axes(self, **kwargs):
        return self.call('get_engaged_axes', kwargs=kwargs)

    def engaged_axes(self, **kwargs):
        return self.call('engaged_axes', kwargs=kwargs)

    def disengage_axes(self, **kwargs):
        return self.call('disengage_axes', kwargs=kwargs)

    def engage_axes(self, **kwargs):
        return self.call('engage_axes', kwargs=kwargs)

    def axis_is_present(self, **kwargs):
        return self.call('axis_is_present', kwargs=kwargs)

    def get_limit_switches(self, **kwargs):
        return self.call('get_limit_switches', kwargs=kwargs)

    def retract(self, **kwargs):
        return self.call('retract', kwargs=kwargs)

    def retract_axis(self, **kwargs):
        return self.call('retract_axis', kwargs=kwargs)

    def config(self, **kwargs):
        return self.call('config', kwargs=kwargs)

    def get_config(self, **kwargs):
        return self.call('get_config', kwargs=kwargs)

    def set_config(self, **kwargs):
        return self.call('set_config', kwargs=kwargs)

    def update_config(self, **kwargs):
        return self.call('update_config', kwargs=kwargs)

    def hardware_feature_flags(self, **kwargs):
        return self.call('hardware_feature_flags', kwargs=kwargs)

    def grip(self, **kwargs):
        return self.call('grip', kwargs=kwargs)

    def ungrip(self, **kwargs):
        return self.call('ungrip', kwargs=kwargs)

    def hold_jaw_width(self, **kwargs):
        return self.call('hold_jaw_width', kwargs=kwargs)

    def tip_pickup_moves(self, **kwargs):
        return self.call('tip_pickup_moves', kwargs=kwargs)

    def configure_for_volume(self, **kwargs):
        return self.call('configure_for_volume', kwargs=kwargs)

    def set_liquid_class(self, **kwargs):
        return self.call('set_liquid_class', kwargs=kwargs)

    def prepare_for_aspirate(self, **kwargs):
        return self.call('prepare_for_aspirate', kwargs=kwargs)

    def aspirate(self, **kwargs):
        return self.call('aspirate', kwargs=kwargs)

    def dispense(self, **kwargs):
        return self.call('dispense', kwargs=kwargs)

    def blow_out(self, **kwargs):
        return self.call('blow_out', kwargs=kwargs)

    def get_tip_presence_status(self, **kwargs):
        return self.call('get_tip_presence_status', kwargs=kwargs)

    def verify_tip_presence(self, **kwargs):
        return self.call('verify_tip_presence', kwargs=kwargs)

    def pick_up_tip(self, **kwargs):
        return self.call('pick_up_tip', kwargs=kwargs)

    def set_current_tiprack_diameter(self, **kwargs):
        return self.call('set_current_tiprack_diameter', kwargs=kwargs)

    def set_working_volume(self, **kwargs):
        return self.call('set_working_volume', kwargs=kwargs)

    def tip_drop_moves(self, **kwargs):
        return self.call('tip_drop_moves', kwargs=kwargs)

    def drop_tip(self, **kwargs):
        return self.call('drop_tip', kwargs=kwargs)

    def clean_up(self, **kwargs):
        return self.call('clean_up', kwargs=kwargs)

    def critical_point_for(self, **kwargs):
        return self.call('critical_point_for', kwargs=kwargs)

    def hardware_pipettes(self, **kwargs):
        return self.call('hardware_pipettes', kwargs=kwargs)

    def hardware_gripper(self, **kwargs):
        return self.call('hardware_gripper', kwargs=kwargs)

    def hardware_instruments(self, **kwargs):
        return self.call('hardware_instruments', kwargs=kwargs)

    def get_attached_pipettes(self, **kwargs):
        return self.call('get_attached_pipettes', kwargs=kwargs)

    def get_attached_instruments(self, **kwargs):
        return self.call('get_attached_instruments', kwargs=kwargs)

    def get_instrument_state(self, **kwargs):
        return self.call('get_instrument_state', kwargs=kwargs)

    def reset_instrument(self, **kwargs):
        return self.call('reset_instrument', kwargs=kwargs)

    def get_instrument_offset(self, **kwargs):
        return self.call('get_instrument_offset', kwargs=kwargs)

    def reset_instrument_offset(self, **kwargs):
        return self.call('reset_instrument_offset', kwargs=kwargs)

    def save_instrument_offset(self, **kwargs):
        return self.call('save_instrument_offset', kwargs=kwargs)

    def save_module_offset(self, **kwargs):
        return self.call('save_module_offset', kwargs=kwargs)

    def get_module_calibration_offset(self, **kwargs):
        return self.call('get_module_calibration_offset', kwargs=kwargs)

    def get_attached_pipette(self, **kwargs):
        return self.call('get_attached_pipette', kwargs=kwargs)

    def get_attached_instrument(self, **kwargs):
        return self.call('get_attached_instrument', kwargs=kwargs)

    def attached_instruments(self, **kwargs):
        return self.call('attached_instruments', kwargs=kwargs)

    def attached_pipettes(self, **kwargs):
        return self.call('attached_pipettes', kwargs=kwargs)

    def attached_gripper(self, **kwargs):
        return self.call('attached_gripper', kwargs=kwargs)

    def has_gripper(self, **kwargs):
        return self.call('has_gripper', kwargs=kwargs)

    def calibrate_plunger(self, **kwargs):
        return self.call('calibrate_plunger', kwargs=kwargs)

    def set_flow_rate(self, **kwargs):
        return self.call('set_flow_rate', kwargs=kwargs)

    def set_pipette_speed(self, **kwargs):
        return self.call('set_pipette_speed', kwargs=kwargs)

    def get_instrument_max_height(self, **kwargs):
        return self.call('get_instrument_max_height', kwargs=kwargs)

    def update_nozzle_configuration_for_mount(self, **kwargs):
        return self.call('update_nozzle_configuration_for_mount', kwargs=kwargs)

    def add_tip(self, **kwargs):
        return self.call('add_tip', kwargs=kwargs)

    def cache_tip(self, **kwargs):
        return self.call('cache_tip', kwargs=kwargs)

    def remove_tip(self, **kwargs):
        return self.call('remove_tip', kwargs=kwargs)

    def add_gripper_probe(self, **kwargs):
        return self.call('add_gripper_probe', kwargs=kwargs)

    def remove_gripper_probe(self, **kwargs):
        return self.call('remove_gripper_probe', kwargs=kwargs)

    def liquid_probe_non_responsive_z_distance(self, **kwargs):
        return self.call('liquid_probe_non_responsive_z_distance', kwargs=kwargs)

    def liquid_probe(self, **kwargs):
        return self.call('liquid_probe', kwargs=kwargs)

    def capacitive_probe(self, **kwargs):
        return self.call('capacitive_probe', kwargs=kwargs)

    def capacitive_sweep(self, **kwargs):
        return self.call('capacitive_sweep', kwargs=kwargs)

    def aspirate_while_tracking(self, **kwargs):
        return self.call('aspirate_while_tracking', kwargs=kwargs)

    def dispense_while_tracking(self, **kwargs):
        return self.call('dispense_while_tracking', kwargs=kwargs)

    def attached_subsystems(self, **kwargs):
        return self.call('attached_subsystems', kwargs=kwargs)

    def estop_status(self, **kwargs):
        return self.call('estop_status', kwargs=kwargs)

    def estop_acknowledge_and_clear(self, **kwargs):
        return self.call('estop_acknowledge_and_clear', kwargs=kwargs)

    def get_estop_state(self, **kwargs):
        return self.call('get_estop_state', kwargs=kwargs)

    def set_hepa_fan_state(self, **kwargs):
        return self.call('set_hepa_fan_state', kwargs=kwargs)

    def get_hepa_fan_state(self, **kwargs):
        return self.call('get_hepa_fan_state', kwargs=kwargs)

    def set_hepa_uv_state(self, **kwargs):
        return self.call('set_hepa_uv_state', kwargs=kwargs)

    def get_hepa_uv_state(self, **kwargs):
        return self.call('get_hepa_uv_state', kwargs=kwargs)

    def increase_evo_disp_count(self, **kwargs):
        return self.call('increase_evo_disp_count', kwargs=kwargs)

    def read_stem_temperature(self, **kwargs):
        return self.call('read_stem_temperature', kwargs=kwargs)

    def read_stem_humidity(self, **kwargs):
        return self.call('read_stem_humidity', kwargs=kwargs)

    def read_stem_pressure(self, **kwargs):
        return self.call('read_stem_pressure', kwargs=kwargs)

    def read_stem_capacitance(self, **kwargs):
        return self.call('read_stem_capacitance', kwargs=kwargs)

    def touch_probe(self, **kwargs):
        return self.call('touch_probe', kwargs=kwargs)

    def taskify_movement_execution(self, **kwargs):
        return self.call('taskify_movement_execution', kwargs=kwargs)

    def execution_manager(self, **kwargs):
        return self.call('execution_manager', kwargs=kwargs)

    def wait_for_running(self, **kwargs):
        return self.call('wait_for_running', kwargs=kwargs)

    def do_delay(self, **kwargs):
        return self.call('do_delay', kwargs=kwargs)

    def robot_calibration(self, **kwargs):
        return self.call('robot_calibration', kwargs=kwargs)

    def reset_robot_calibration(self, **kwargs):
        return self.call('reset_robot_calibration', kwargs=kwargs)

    def reset_deck_calibration(self, **kwargs):
        return self.call('reset_deck_calibration', kwargs=kwargs)

    def load_deck_calibration(self, **kwargs):
        return self.call('load_deck_calibration', kwargs=kwargs)

    def set_robot_calibration(self, **kwargs):
        return self.call('set_robot_calibration', kwargs=kwargs)

    def validate_calibration(self, **kwargs):
        return self.call('validate_calibration', kwargs=kwargs)

    def build_temporary_identity_calibration(self, **kwargs):
        return self.call('build_temporary_identity_calibration', kwargs=kwargs)

    def get_robot_type(self, **kwargs):
        return self.call('get_robot_type', kwargs=kwargs)

    def file_path(self, **kwargs):
        return self.call('file_path', kwargs=kwargs)

    def short_sha(self, **kwargs):
        return self.call('short_sha', kwargs=kwargs)

    def to_json(self, **kwargs):
        return self.call('to_json', kwargs=kwargs)

    def from_dict(self, **kwargs):
        return self.call('from_dict', kwargs=kwargs)

    def from_json(self, **kwargs):
        return self.call('from_json', kwargs=kwargs)

