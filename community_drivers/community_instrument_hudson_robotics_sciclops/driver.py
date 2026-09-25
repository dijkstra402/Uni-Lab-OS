from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHudsonRoboticsSciclops(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AD-SDL__sciclops_module', 'source_file': 'src/sciclops_interface.py', 'class_name': 'SCICLOPS', 'import_roots': ['src'], 'candidate_methods': ['connect', 'disconnect', 'send_command', 'get_error', 'get_position', 'get_status', 'check_complete', 'check_complete_loop', 'get_version', 'reset', 'get_config', 'get_grip_length', 'get_steps_per_unit', 'home', 'open', 'close', 'check_open', 'check_closed', 'check_plate', 'set_speed', 'list_points', 'jog', 'loadpoint', 'deletepoint', 'move', 'move_neutral', 'get_plate', 'return_plate', 'limp', 'plate_to_stack'], 'action_targets': {}, 'metadata': {'repo': 'AD-SDL/sciclops_module', 'repo_url': 'https://github.com/AD-SDL/sciclops_module', 'brand': 'Hudson Robotics', 'model': 'Sciclops', 'device_type_cn': '取板机器人', 'device_type_en': 'Plate Robot', 'source_framework': 'AD-SDL', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 320, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def get_error(self, **kwargs):
        return self.call('get_error', kwargs=kwargs)

    def get_position(self, **kwargs):
        return self.call('get_position', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def check_complete(self, **kwargs):
        return self.call('check_complete', kwargs=kwargs)

    def check_complete_loop(self, **kwargs):
        return self.call('check_complete_loop', kwargs=kwargs)

    def get_version(self, **kwargs):
        return self.call('get_version', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def get_config(self, **kwargs):
        return self.call('get_config', kwargs=kwargs)

    def get_grip_length(self, **kwargs):
        return self.call('get_grip_length', kwargs=kwargs)

    def get_steps_per_unit(self, **kwargs):
        return self.call('get_steps_per_unit', kwargs=kwargs)

    def home(self, **kwargs):
        return self.call('home', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def check_open(self, **kwargs):
        return self.call('check_open', kwargs=kwargs)

    def check_closed(self, **kwargs):
        return self.call('check_closed', kwargs=kwargs)

    def check_plate(self, **kwargs):
        return self.call('check_plate', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

    def list_points(self, **kwargs):
        return self.call('list_points', kwargs=kwargs)

    def jog(self, **kwargs):
        return self.call('jog', kwargs=kwargs)

    def loadpoint(self, **kwargs):
        return self.call('loadpoint', kwargs=kwargs)

    def deletepoint(self, **kwargs):
        return self.call('deletepoint', kwargs=kwargs)

    def move(self, **kwargs):
        return self.call('move', kwargs=kwargs)

    def move_neutral(self, **kwargs):
        return self.call('move_neutral', kwargs=kwargs)

    def get_plate(self, **kwargs):
        return self.call('get_plate', kwargs=kwargs)

    def return_plate(self, **kwargs):
        return self.call('return_plate', kwargs=kwargs)

    def limp(self, **kwargs):
        return self.call('limp', kwargs=kwargs)

    def plate_to_stack(self, **kwargs):
        return self.call('plate_to_stack', kwargs=kwargs)

