from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHamiltonNimbus(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/liquid_handling/backends/hamilton/nimbus_backend.py', 'class_name': 'NimbusBackend', 'import_roots': [], 'candidate_methods': ['aspirate', 'aspirate96', 'can_pick_up_tip', 'dispense', 'dispense96', 'drop_resource', 'drop_tips', 'drop_tips96', 'get_channel_spacings', 'is_door_locked', 'lock_door', 'move_channel_x', 'move_channel_y', 'move_channel_z', 'move_picked_up_resource', 'park', 'pick_up_resource', 'pick_up_tips', 'pick_up_tips96', 'prepare_for_manual_channel_operation', 'read', 'read_exact', 'request_tip_presence', 'set_deck', 'set_heads', 'set_minimum_channel_traversal_height', 'setup', 'stop', 'unlock_door', 'write'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Hamilton', 'model': 'Nimbus', 'device_type_cn': '移液工作站', 'device_type_en': 'Liquid Handling Workstation', 'source_framework': 'PyLabRobot', 'tag_id': '4436', 'tag_name': '移液工作站', 'tag_name_en': 'Liquid Handling Workstation', 'candidate_score': 2342, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/liquid_handling/backends/hamilton/nimbus_backend.py', 'class_name': 'NimbusBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def aspirate(self, ops=None, use_channels=None, minimum_traverse_height_at_beginning_of_a_command=None, adc_enabled=None, lld_mode=None, lld_search_height=None, immersion_depth=None, surface_following_distance=None, gamma_lld_sensitivity=None, dp_lld_sensitivity=None, settling_time=None, transport_air_volume=None, pre_wetting_volume=None, swap_speed=None, mix_position_from_liquid_surface=None, limit_curve_index=None, tadm_enabled=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'adc_enabled': adc_enabled, 'lld_mode': lld_mode, 'lld_search_height': lld_search_height, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'gamma_lld_sensitivity': gamma_lld_sensitivity, 'dp_lld_sensitivity': dp_lld_sensitivity, 'settling_time': settling_time, 'transport_air_volume': transport_air_volume, 'pre_wetting_volume': pre_wetting_volume, 'swap_speed': swap_speed, 'mix_position_from_liquid_surface': mix_position_from_liquid_surface, 'limit_curve_index': limit_curve_index, 'tadm_enabled': tadm_enabled}
        _kw.update(kwargs)
        return self.call('aspirate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def aspirate96(self, aspiration=None, **kwargs):
        _kw = {'aspiration': aspiration}
        _kw.update(kwargs)
        return self.call('aspirate96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def can_pick_up_tip(self, channel_idx=None, tip=None, **kwargs):
        _kw = {'channel_idx': channel_idx, 'tip': tip}
        _kw.update(kwargs)
        return self.call('can_pick_up_tip', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispense(self, ops=None, use_channels=None, minimum_traverse_height_at_beginning_of_a_command=None, adc_enabled=None, lld_mode=None, lld_search_height=None, immersion_depth=None, surface_following_distance=None, gamma_lld_sensitivity=None, settling_time=None, transport_air_volume=None, swap_speed=None, mix_position_from_liquid_surface=None, limit_curve_index=None, tadm_enabled=None, cut_off_speed=None, stop_back_volume=None, side_touch_off_distance=None, dispense_offset=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'adc_enabled': adc_enabled, 'lld_mode': lld_mode, 'lld_search_height': lld_search_height, 'immersion_depth': immersion_depth, 'surface_following_distance': surface_following_distance, 'gamma_lld_sensitivity': gamma_lld_sensitivity, 'settling_time': settling_time, 'transport_air_volume': transport_air_volume, 'swap_speed': swap_speed, 'mix_position_from_liquid_surface': mix_position_from_liquid_surface, 'limit_curve_index': limit_curve_index, 'tadm_enabled': tadm_enabled, 'cut_off_speed': cut_off_speed, 'stop_back_volume': stop_back_volume, 'side_touch_off_distance': side_touch_off_distance, 'dispense_offset': dispense_offset}
        _kw.update(kwargs)
        return self.call('dispense', kwargs={k: v for k, v in _kw.items() if v is not None})

    def dispense96(self, dispense=None, **kwargs):
        _kw = {'dispense': dispense}
        _kw.update(kwargs)
        return self.call('dispense96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def drop_resource(self, drop=None, **kwargs):
        _kw = {'drop': drop}
        _kw.update(kwargs)
        return self.call('drop_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def drop_tips(self, ops=None, use_channels=None, default_waste=None, minimum_traverse_height_at_beginning_of_a_command=None, z_position_at_end_of_a_command=None, roll_distance=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'default_waste': default_waste, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command, 'z_position_at_end_of_a_command': z_position_at_end_of_a_command, 'roll_distance': roll_distance}
        _kw.update(kwargs)
        return self.call('drop_tips', kwargs={k: v for k, v in _kw.items() if v is not None})

    def drop_tips96(self, drop=None, **kwargs):
        _kw = {'drop': drop}
        _kw.update(kwargs)
        return self.call('drop_tips96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_channel_spacings(self, use_channels=None, **kwargs):
        _kw = {'use_channels': use_channels}
        _kw.update(kwargs)
        return self.call('get_channel_spacings', kwargs={k: v for k, v in _kw.items() if v is not None})

    def is_door_locked(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('is_door_locked', kwargs={k: v for k, v in _kw.items() if v is not None})

    def lock_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('lock_door', kwargs={k: v for k, v in _kw.items() if v is not None})

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

    def park(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('park', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_resource(self, pickup=None, **kwargs):
        _kw = {'pickup': pickup}
        _kw.update(kwargs)
        return self.call('pick_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_tips(self, ops=None, use_channels=None, minimum_traverse_height_at_beginning_of_a_command=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels, 'minimum_traverse_height_at_beginning_of_a_command': minimum_traverse_height_at_beginning_of_a_command}
        _kw.update(kwargs)
        return self.call('pick_up_tips', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_tips96(self, pickup=None, **kwargs):
        _kw = {'pickup': pickup}
        _kw.update(kwargs)
        return self.call('pick_up_tips96', kwargs={k: v for k, v in _kw.items() if v is not None})

    def prepare_for_manual_channel_operation(self, channel=None, **kwargs):
        _kw = {'channel': channel}
        _kw.update(kwargs)
        return self.call('prepare_for_manual_channel_operation', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read(self, num_bytes=None, timeout=None, **kwargs):
        _kw = {'num_bytes': num_bytes, 'timeout': timeout}
        _kw.update(kwargs)
        return self.call('read', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_exact(self, num_bytes=None, timeout=None, **kwargs):
        _kw = {'num_bytes': num_bytes, 'timeout': timeout}
        _kw.update(kwargs)
        return self.call('read_exact', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_tip_presence(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_tip_presence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_deck(self, deck=None, **kwargs):
        _kw = {'deck': deck}
        _kw.update(kwargs)
        return self.call('set_deck', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_heads(self, head=None, head96=None, **kwargs):
        _kw = {'head': head, 'head96': head96}
        _kw.update(kwargs)
        return self.call('set_heads', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_minimum_channel_traversal_height(self, traversal_height=None, **kwargs):
        _kw = {'traversal_height': traversal_height}
        _kw.update(kwargs)
        return self.call('set_minimum_channel_traversal_height', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, unlock_door=None, force_initialize=None, **kwargs):
        _kw = {'unlock_door': unlock_door, 'force_initialize': force_initialize}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def unlock_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('unlock_door', kwargs={k: v for k, v in _kw.items() if v is not None})

    def write(self, data=None, timeout=None, **kwargs):
        _kw = {'data': data, 'timeout': timeout}
        _kw.update(kwargs)
        return self.call('write', kwargs={k: v for k, v in _kw.items() if v is not None})

