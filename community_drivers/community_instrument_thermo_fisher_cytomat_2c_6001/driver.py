from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThermoFisherCytomat2c6001(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/smartlab-network__open-cytomat', 'source_file': 'src/cytomat/plate_handler.py', 'class_name': 'PlateHandler', 'import_roots': ['src'], 'candidate_methods': ['initialize', 'move_plate_from_transfer_station_to_slot', 'move_plate_from_slot_to_transfer_station', 'execute_low_level', 'move_plate_from_transfer_station_to_handler', 'move_plate_from_handler_to_transfer_station', 'move_plate_from_exposed_position_to_inside', 'move_plate_from_inside_to_exposed_position', 'move_plate_from_handler_to_slot', 'move_plate_from_slot_to_handler', 'move_plate_from_exposed_position_to_slot', 'move_plate_from_slot_to_exposed_position', 'retract_shovel', 'extend_shovel', 'close_transfer_door', 'open_transfer_door', 'reset_handler_position', 'move_handler_below_slot_height', 'move_handler_above_slot_height', 'rotate_handler_to_slot', 'rotate_handler_to_transfer_station', 'move_x_to_slot', 'warning_msg', 'run_shovel_in_absolute_steps', 'run_shovel_in_relative_steps', 'run_turn_in_absolute_steps', 'run_turn_in_relative_steps', 'run_height_in_absolute_steps', 'run_height_in_relative_steps', 'run_turntable_in_absolute_steps', 'run_turntable_in_relative_steps', 'run_x_axis_in_absolute_steps', 'run_x_axis_in_relative_steps', 'run_transfer_station_in_absolute_steps', 'run_transfer_station_in_relative_steps'], 'action_targets': {}, 'metadata': {'repo': 'smartlab-network/open-cytomat', 'repo_url': 'https://github.com/smartlab-network/open-cytomat', 'brand': 'Thermo Fisher', 'model': 'Cytomat 2C/6001', 'device_type_cn': '自动化耗材堆栈', 'device_type_en': 'Automated Consumable Stack', 'source_framework': '专用驱动', 'tag_id': '4446', 'tag_name': '自动化耗材堆栈', 'tag_name_en': 'Automated Consumable Stack', 'candidate_score': 318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def move_plate_from_transfer_station_to_slot(self, **kwargs):
        return self.call('move_plate_from_transfer_station_to_slot', kwargs=kwargs)

    def move_plate_from_slot_to_transfer_station(self, **kwargs):
        return self.call('move_plate_from_slot_to_transfer_station', kwargs=kwargs)

    def execute_low_level(self, **kwargs):
        return self.call('execute_low_level', kwargs=kwargs)

    def move_plate_from_transfer_station_to_handler(self, **kwargs):
        return self.call('move_plate_from_transfer_station_to_handler', kwargs=kwargs)

    def move_plate_from_handler_to_transfer_station(self, **kwargs):
        return self.call('move_plate_from_handler_to_transfer_station', kwargs=kwargs)

    def move_plate_from_exposed_position_to_inside(self, **kwargs):
        return self.call('move_plate_from_exposed_position_to_inside', kwargs=kwargs)

    def move_plate_from_inside_to_exposed_position(self, **kwargs):
        return self.call('move_plate_from_inside_to_exposed_position', kwargs=kwargs)

    def move_plate_from_handler_to_slot(self, **kwargs):
        return self.call('move_plate_from_handler_to_slot', kwargs=kwargs)

    def move_plate_from_slot_to_handler(self, **kwargs):
        return self.call('move_plate_from_slot_to_handler', kwargs=kwargs)

    def move_plate_from_exposed_position_to_slot(self, **kwargs):
        return self.call('move_plate_from_exposed_position_to_slot', kwargs=kwargs)

    def move_plate_from_slot_to_exposed_position(self, **kwargs):
        return self.call('move_plate_from_slot_to_exposed_position', kwargs=kwargs)

    def retract_shovel(self, **kwargs):
        return self.call('retract_shovel', kwargs=kwargs)

    def extend_shovel(self, **kwargs):
        return self.call('extend_shovel', kwargs=kwargs)

    def close_transfer_door(self, **kwargs):
        return self.call('close_transfer_door', kwargs=kwargs)

    def open_transfer_door(self, **kwargs):
        return self.call('open_transfer_door', kwargs=kwargs)

    def reset_handler_position(self, **kwargs):
        return self.call('reset_handler_position', kwargs=kwargs)

    def move_handler_below_slot_height(self, **kwargs):
        return self.call('move_handler_below_slot_height', kwargs=kwargs)

    def move_handler_above_slot_height(self, **kwargs):
        return self.call('move_handler_above_slot_height', kwargs=kwargs)

    def rotate_handler_to_slot(self, **kwargs):
        return self.call('rotate_handler_to_slot', kwargs=kwargs)

    def rotate_handler_to_transfer_station(self, **kwargs):
        return self.call('rotate_handler_to_transfer_station', kwargs=kwargs)

    def move_x_to_slot(self, **kwargs):
        return self.call('move_x_to_slot', kwargs=kwargs)

    def warning_msg(self, **kwargs):
        return self.call('warning_msg', kwargs=kwargs)

    def run_shovel_in_absolute_steps(self, **kwargs):
        return self.call('run_shovel_in_absolute_steps', kwargs=kwargs)

    def run_shovel_in_relative_steps(self, **kwargs):
        return self.call('run_shovel_in_relative_steps', kwargs=kwargs)

    def run_turn_in_absolute_steps(self, **kwargs):
        return self.call('run_turn_in_absolute_steps', kwargs=kwargs)

    def run_turn_in_relative_steps(self, **kwargs):
        return self.call('run_turn_in_relative_steps', kwargs=kwargs)

    def run_height_in_absolute_steps(self, **kwargs):
        return self.call('run_height_in_absolute_steps', kwargs=kwargs)

    def run_height_in_relative_steps(self, **kwargs):
        return self.call('run_height_in_relative_steps', kwargs=kwargs)

    def run_turntable_in_absolute_steps(self, **kwargs):
        return self.call('run_turntable_in_absolute_steps', kwargs=kwargs)

    def run_turntable_in_relative_steps(self, **kwargs):
        return self.call('run_turntable_in_relative_steps', kwargs=kwargs)

    def run_x_axis_in_absolute_steps(self, **kwargs):
        return self.call('run_x_axis_in_absolute_steps', kwargs=kwargs)

    def run_x_axis_in_relative_steps(self, **kwargs):
        return self.call('run_x_axis_in_relative_steps', kwargs=kwargs)

    def run_transfer_station_in_absolute_steps(self, **kwargs):
        return self.call('run_transfer_station_in_absolute_steps', kwargs=kwargs)

    def run_transfer_station_in_relative_steps(self, **kwargs):
        return self.call('run_transfer_station_in_relative_steps', kwargs=kwargs)

