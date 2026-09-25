from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTecanEvo(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/liquid_handling/backends/tecan/EVO_backend.py', 'class_name': 'EVOBackend', 'import_roots': [], 'candidate_methods': ['aspirate', 'aspirate96', 'can_pick_up_tip', 'dispense', 'dispense96', 'drop_resource', 'drop_tips', 'drop_tips96', 'get_channel_spacings', 'move_channel_x', 'move_channel_y', 'move_channel_z', 'move_picked_up_resource', 'parse_response', 'pick_up_resource', 'pick_up_tips', 'pick_up_tips96', 'prepare_for_manual_channel_operation', 'request_tip_presence', 'set_deck', 'set_heads', 'setup', 'setup_arm', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Tecan', 'model': 'EVO', 'device_type_cn': '移液工作站', 'device_type_en': 'Liquid Handling Workstation', 'source_framework': 'PyLabRobot', 'tag_id': '4436', 'tag_name': '移液工作站', 'tag_name_en': 'Liquid Handling Workstation', 'candidate_score': 2334, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/liquid_handling/backends/tecan/EVO_backend.py', 'class_name': 'EVOBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def aspirate(self, ops=None, use_channels=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels}
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

    def dispense(self, ops=None, use_channels=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels}
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

    def drop_tips(self, ops=None, use_channels=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels}
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

    def parse_response(self, resp=None, **kwargs):
        _kw = {'resp': resp}
        _kw.update(kwargs)
        return self.call('parse_response', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_resource(self, pickup=None, **kwargs):
        _kw = {'pickup': pickup}
        _kw.update(kwargs)
        return self.call('pick_up_resource', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pick_up_tips(self, ops=None, use_channels=None, **kwargs):
        _kw = {'ops': ops, 'use_channels': use_channels}
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

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup_arm(self, module=None, **kwargs):
        _kw = {'module': module}
        _kw.update(kwargs)
        return self.call('setup_arm', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

