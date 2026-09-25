from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTricontinentC3000C24000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/croningp__pycont', 'source_file': 'pycont/controller.py', 'class_name': 'C3000Controller', 'import_roots': [], 'candidate_methods': ['from_config', 'write_and_read_from_pump', 'volume_to_step', 'step_to_volume', 'is_idle', 'is_busy', 'wait_until_idle', 'is_initialized', 'smart_initialize', 'initialize', 'initialize_valve_right', 'initialize_valve_left', 'initialize_no_valve', 'initialize_valve_only', 'init_all_pump_parameters', 'set_microstep_mode', 'check_top_velocity_within_range', 'set_default_top_velocity', 'get_default_top_velocity', 'ensure_default_top_velocity', 'set_top_velocity', 'get_top_velocity', 'get_plunger_position', 'current_steps', 'remaining_steps', 'get_volume', 'current_volume', 'remaining_volume', 'is_volume_pumpable', 'pump', 'is_volume_deliverable', 'deliver', 'transfer', 'is_volume_valid', 'go_to_volume', 'go_to_max_volume', 'get_raw_valve_position', 'get_valve_position', 'set_valve_position', 'set_eeprom_config', 'set_eeprom_lowlevel_config', 'flash_eeprom_3_way_y_valve', 'flash_eeprom_3_way_t_valve', 'flash_eeprom_4_way_nondist_valve', 'flash_eeprom_4_way_dist_valve', 'get_eeprom_config', 'get_current_valve_config', 'terminate'], 'action_targets': {}, 'metadata': {'repo': 'croningp/pycont', 'repo_url': 'https://github.com/croningp/pycont', 'brand': 'Tricontinent', 'model': 'C3000/C24000', 'device_type_cn': '柱塞泵', 'device_type_en': 'Plunger Pump', 'source_framework': 'pycont', 'tag_id': '4403', 'tag_name': '柱塞泵', 'tag_name_en': 'Plunger Pump', 'candidate_score': 442, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def from_config(self, **kwargs):
        return self.call('from_config', kwargs=kwargs)

    def write_and_read_from_pump(self, **kwargs):
        return self.call('write_and_read_from_pump', kwargs=kwargs)

    def volume_to_step(self, **kwargs):
        return self.call('volume_to_step', kwargs=kwargs)

    def step_to_volume(self, **kwargs):
        return self.call('step_to_volume', kwargs=kwargs)

    def is_idle(self, **kwargs):
        return self.call('is_idle', kwargs=kwargs)

    def is_busy(self, **kwargs):
        return self.call('is_busy', kwargs=kwargs)

    def wait_until_idle(self, **kwargs):
        return self.call('wait_until_idle', kwargs=kwargs)

    def is_initialized(self, **kwargs):
        return self.call('is_initialized', kwargs=kwargs)

    def smart_initialize(self, **kwargs):
        return self.call('smart_initialize', kwargs=kwargs)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def initialize_valve_right(self, **kwargs):
        return self.call('initialize_valve_right', kwargs=kwargs)

    def initialize_valve_left(self, **kwargs):
        return self.call('initialize_valve_left', kwargs=kwargs)

    def initialize_no_valve(self, **kwargs):
        return self.call('initialize_no_valve', kwargs=kwargs)

    def initialize_valve_only(self, **kwargs):
        return self.call('initialize_valve_only', kwargs=kwargs)

    def init_all_pump_parameters(self, **kwargs):
        return self.call('init_all_pump_parameters', kwargs=kwargs)

    def set_microstep_mode(self, **kwargs):
        return self.call('set_microstep_mode', kwargs=kwargs)

    def check_top_velocity_within_range(self, **kwargs):
        return self.call('check_top_velocity_within_range', kwargs=kwargs)

    def set_default_top_velocity(self, **kwargs):
        return self.call('set_default_top_velocity', kwargs=kwargs)

    def get_default_top_velocity(self, **kwargs):
        return self.call('get_default_top_velocity', kwargs=kwargs)

    def ensure_default_top_velocity(self, **kwargs):
        return self.call('ensure_default_top_velocity', kwargs=kwargs)

    def set_top_velocity(self, **kwargs):
        return self.call('set_top_velocity', kwargs=kwargs)

    def get_top_velocity(self, **kwargs):
        return self.call('get_top_velocity', kwargs=kwargs)

    def get_plunger_position(self, **kwargs):
        return self.call('get_plunger_position', kwargs=kwargs)

    def current_steps(self, **kwargs):
        return self.call('current_steps', kwargs=kwargs)

    def remaining_steps(self, **kwargs):
        return self.call('remaining_steps', kwargs=kwargs)

    def get_volume(self, **kwargs):
        return self.call('get_volume', kwargs=kwargs)

    def current_volume(self, **kwargs):
        return self.call('current_volume', kwargs=kwargs)

    def remaining_volume(self, **kwargs):
        return self.call('remaining_volume', kwargs=kwargs)

    def is_volume_pumpable(self, **kwargs):
        return self.call('is_volume_pumpable', kwargs=kwargs)

    def pump(self, **kwargs):
        return self.call('pump', kwargs=kwargs)

    def is_volume_deliverable(self, **kwargs):
        return self.call('is_volume_deliverable', kwargs=kwargs)

    def deliver(self, **kwargs):
        return self.call('deliver', kwargs=kwargs)

    def transfer(self, **kwargs):
        return self.call('transfer', kwargs=kwargs)

    def is_volume_valid(self, **kwargs):
        return self.call('is_volume_valid', kwargs=kwargs)

    def go_to_volume(self, **kwargs):
        return self.call('go_to_volume', kwargs=kwargs)

    def go_to_max_volume(self, **kwargs):
        return self.call('go_to_max_volume', kwargs=kwargs)

    def get_raw_valve_position(self, **kwargs):
        return self.call('get_raw_valve_position', kwargs=kwargs)

    def get_valve_position(self, **kwargs):
        return self.call('get_valve_position', kwargs=kwargs)

    def set_valve_position(self, **kwargs):
        return self.call('set_valve_position', kwargs=kwargs)

    def set_eeprom_config(self, **kwargs):
        return self.call('set_eeprom_config', kwargs=kwargs)

    def set_eeprom_lowlevel_config(self, **kwargs):
        return self.call('set_eeprom_lowlevel_config', kwargs=kwargs)

    def flash_eeprom_3_way_y_valve(self, **kwargs):
        return self.call('flash_eeprom_3_way_y_valve', kwargs=kwargs)

    def flash_eeprom_3_way_t_valve(self, **kwargs):
        return self.call('flash_eeprom_3_way_t_valve', kwargs=kwargs)

    def flash_eeprom_4_way_nondist_valve(self, **kwargs):
        return self.call('flash_eeprom_4_way_nondist_valve', kwargs=kwargs)

    def flash_eeprom_4_way_dist_valve(self, **kwargs):
        return self.call('flash_eeprom_4_way_dist_valve', kwargs=kwargs)

    def get_eeprom_config(self, **kwargs):
        return self.call('get_eeprom_config', kwargs=kwargs)

    def get_current_valve_config(self, **kwargs):
        return self.call('get_current_valve_config', kwargs=kwargs)

    def terminate(self, **kwargs):
        return self.call('terminate', kwargs=kwargs)

