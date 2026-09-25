from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHamiltonStarStarlet(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/dgretton__pyhamilton', 'source_file': 'pyhamilton/interface.py', 'class_name': 'HamiltonInterface', 'import_roots': [], 'candidate_methods': ['start', 'stop', 'is_open', 'send_command', 'wait_on_response', 'parse_response', 'set_log_dir', 'log', 'log_and_raise', 'initialize', 'aspirate', 'dispense', 'tip_pick_up', 'tip_eject', 'tip_pick_up_96', 'tip_eject_96', 'aspirate_96', 'tip_pick_up_mph_columns', 'dispense_96', 'aspirate_384_quadrant', 'dispense_384_quadrant', 'set_labware_property', 'move_plate', 'move_by_seq', 'get_plate_gripper_seq', 'move_plate_gripper_seq', 'place_plate_gripper_seq', 'move_plate_gripper', 'move_sequence', 'load_carrier', 'unload_carrier'], 'action_targets': {}, 'metadata': {'repo': 'dgretton/pyhamilton', 'repo_url': 'https://github.com/dgretton/pyhamilton', 'brand': 'Hamilton', 'model': 'STAR/STARlet', 'device_type_cn': '移液管', 'device_type_en': 'Pipette Tube', 'source_framework': 'pyhamilton', 'tag_id': '4437', 'tag_name': '移液管', 'tag_name_en': 'Pipette Tube', 'candidate_score': 306, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def is_open(self, **kwargs):
        return self.call('is_open', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def wait_on_response(self, **kwargs):
        return self.call('wait_on_response', kwargs=kwargs)

    def parse_response(self, **kwargs):
        return self.call('parse_response', kwargs=kwargs)

    def set_log_dir(self, **kwargs):
        return self.call('set_log_dir', kwargs=kwargs)

    def log(self, **kwargs):
        return self.call('log', kwargs=kwargs)

    def log_and_raise(self, **kwargs):
        return self.call('log_and_raise', kwargs=kwargs)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def aspirate(self, **kwargs):
        return self.call('aspirate', kwargs=kwargs)

    def dispense(self, **kwargs):
        return self.call('dispense', kwargs=kwargs)

    def tip_pick_up(self, **kwargs):
        return self.call('tip_pick_up', kwargs=kwargs)

    def tip_eject(self, **kwargs):
        return self.call('tip_eject', kwargs=kwargs)

    def tip_pick_up_96(self, **kwargs):
        return self.call('tip_pick_up_96', kwargs=kwargs)

    def tip_eject_96(self, **kwargs):
        return self.call('tip_eject_96', kwargs=kwargs)

    def aspirate_96(self, **kwargs):
        return self.call('aspirate_96', kwargs=kwargs)

    def tip_pick_up_mph_columns(self, **kwargs):
        return self.call('tip_pick_up_mph_columns', kwargs=kwargs)

    def dispense_96(self, **kwargs):
        return self.call('dispense_96', kwargs=kwargs)

    def aspirate_384_quadrant(self, **kwargs):
        return self.call('aspirate_384_quadrant', kwargs=kwargs)

    def dispense_384_quadrant(self, **kwargs):
        return self.call('dispense_384_quadrant', kwargs=kwargs)

    def set_labware_property(self, **kwargs):
        return self.call('set_labware_property', kwargs=kwargs)

    def move_plate(self, **kwargs):
        return self.call('move_plate', kwargs=kwargs)

    def move_by_seq(self, **kwargs):
        return self.call('move_by_seq', kwargs=kwargs)

    def get_plate_gripper_seq(self, **kwargs):
        return self.call('get_plate_gripper_seq', kwargs=kwargs)

    def move_plate_gripper_seq(self, **kwargs):
        return self.call('move_plate_gripper_seq', kwargs=kwargs)

    def place_plate_gripper_seq(self, **kwargs):
        return self.call('place_plate_gripper_seq', kwargs=kwargs)

    def move_plate_gripper(self, **kwargs):
        return self.call('move_plate_gripper', kwargs=kwargs)

    def move_sequence(self, **kwargs):
        return self.call('move_sequence', kwargs=kwargs)

    def load_carrier(self, **kwargs):
        return self.call('load_carrier', kwargs=kwargs)

    def unload_carrier(self, **kwargs):
        return self.call('unload_carrier', kwargs=kwargs)

