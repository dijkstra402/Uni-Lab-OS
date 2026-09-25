from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIkaRv10DigitalChemputer(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/croningp__ChemputerConvergence', 'source_file': 'libraries/Chempiler/chempiler/tools/module_execution/pump_execution.py', 'class_name': 'PumpExecutioner', 'import_roots': [], 'candidate_methods': ['default_discriminant', 'attached_conductivity_sensor', 'separate_phases', 'connect_valve', 'connect_nodes', 'get_pump_from_valve_name', 'get_max_syringe_volume', 'routing_nodes', 'connect_routing_valve_cmds', 'prune_steps', 'remove_full_routing_steps', 'combine_steps_with_routes', 'move_duration', 'cmd_duration', 'move_locks', 'validate_port', 'check_move_args', 'assign_default_ports', 'move', 'split_movement_path', 'insert_steps', 'move_log_message', 'print_pipelined_steps', 'pipeline_path', 'expected_n_pump_step_groups', 'validate_len_pipeline', 'validate_src_dest_volumes', 'validate_one_command_per_group_per_node', 'validate_pump_moves', 'validate_valve_switches', 'print_pipelined_step_list', 'validate_pipelined_step_list', 'pipeline_step_list', 'execute_pipelined_steps', 'execute_cmd', 'execute_step', 'connect_valve_cmd', 'single_pump_valve_combo', 'dual_pump_valve_combo'], 'action_targets': {}, 'metadata': {'repo': 'croningp/ChemputerConvergence', 'repo_url': 'https://github.com/croningp/ChemputerConvergence', 'brand': 'IKA', 'model': 'RV10 Digital (Chemputer)', 'device_type_cn': '旋转蒸发器', 'device_type_en': 'Rotary Evaporator', 'source_framework': 'SerialLabware', 'tag_id': '4397', 'tag_name': '旋转蒸发器', 'tag_name_en': 'Rotary Evaporator', 'candidate_score': 350, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def default_discriminant(self, **kwargs):
        return self.call('default_discriminant', kwargs=kwargs)

    def attached_conductivity_sensor(self, **kwargs):
        return self.call('attached_conductivity_sensor', kwargs=kwargs)

    def separate_phases(self, **kwargs):
        return self.call('separate_phases', kwargs=kwargs)

    def connect_valve(self, **kwargs):
        return self.call('connect_valve', kwargs=kwargs)

    def connect_nodes(self, **kwargs):
        return self.call('connect_nodes', kwargs=kwargs)

    def get_pump_from_valve_name(self, **kwargs):
        return self.call('get_pump_from_valve_name', kwargs=kwargs)

    def get_max_syringe_volume(self, **kwargs):
        return self.call('get_max_syringe_volume', kwargs=kwargs)

    def routing_nodes(self, **kwargs):
        return self.call('routing_nodes', kwargs=kwargs)

    def connect_routing_valve_cmds(self, **kwargs):
        return self.call('connect_routing_valve_cmds', kwargs=kwargs)

    def prune_steps(self, **kwargs):
        return self.call('prune_steps', kwargs=kwargs)

    def remove_full_routing_steps(self, **kwargs):
        return self.call('remove_full_routing_steps', kwargs=kwargs)

    def combine_steps_with_routes(self, **kwargs):
        return self.call('combine_steps_with_routes', kwargs=kwargs)

    def move_duration(self, **kwargs):
        return self.call('move_duration', kwargs=kwargs)

    def cmd_duration(self, **kwargs):
        return self.call('cmd_duration', kwargs=kwargs)

    def move_locks(self, **kwargs):
        return self.call('move_locks', kwargs=kwargs)

    def validate_port(self, **kwargs):
        return self.call('validate_port', kwargs=kwargs)

    def check_move_args(self, **kwargs):
        return self.call('check_move_args', kwargs=kwargs)

    def assign_default_ports(self, **kwargs):
        return self.call('assign_default_ports', kwargs=kwargs)

    def move(self, **kwargs):
        return self.call('move', kwargs=kwargs)

    def split_movement_path(self, **kwargs):
        return self.call('split_movement_path', kwargs=kwargs)

    def insert_steps(self, **kwargs):
        return self.call('insert_steps', kwargs=kwargs)

    def move_log_message(self, **kwargs):
        return self.call('move_log_message', kwargs=kwargs)

    def print_pipelined_steps(self, **kwargs):
        return self.call('print_pipelined_steps', kwargs=kwargs)

    def pipeline_path(self, **kwargs):
        return self.call('pipeline_path', kwargs=kwargs)

    def expected_n_pump_step_groups(self, **kwargs):
        return self.call('expected_n_pump_step_groups', kwargs=kwargs)

    def validate_len_pipeline(self, **kwargs):
        return self.call('validate_len_pipeline', kwargs=kwargs)

    def validate_src_dest_volumes(self, **kwargs):
        return self.call('validate_src_dest_volumes', kwargs=kwargs)

    def validate_one_command_per_group_per_node(self, **kwargs):
        return self.call('validate_one_command_per_group_per_node', kwargs=kwargs)

    def validate_pump_moves(self, **kwargs):
        return self.call('validate_pump_moves', kwargs=kwargs)

    def validate_valve_switches(self, **kwargs):
        return self.call('validate_valve_switches', kwargs=kwargs)

    def print_pipelined_step_list(self, **kwargs):
        return self.call('print_pipelined_step_list', kwargs=kwargs)

    def validate_pipelined_step_list(self, **kwargs):
        return self.call('validate_pipelined_step_list', kwargs=kwargs)

    def pipeline_step_list(self, **kwargs):
        return self.call('pipeline_step_list', kwargs=kwargs)

    def execute_pipelined_steps(self, **kwargs):
        return self.call('execute_pipelined_steps', kwargs=kwargs)

    def execute_cmd(self, **kwargs):
        return self.call('execute_cmd', kwargs=kwargs)

    def execute_step(self, **kwargs):
        return self.call('execute_step', kwargs=kwargs)

    def connect_valve_cmd(self, **kwargs):
        return self.call('connect_valve_cmd', kwargs=kwargs)

    def single_pump_valve_combo(self, **kwargs):
        return self.call('single_pump_valve_combo', kwargs=kwargs)

    def dual_pump_valve_combo(self, **kwargs):
        return self.call('dual_pump_valve_combo', kwargs=kwargs)

