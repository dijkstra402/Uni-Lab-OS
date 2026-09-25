from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHudsonRoboticsPlatecraneEx(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AD-SDL__hudson_platecrane_module', 'source_file': 'src/platecrane_driver/sciclops_driver.py', 'class_name': 'SCICLOPS', 'import_roots': ['src'], 'candidate_methods': ['connect_sciclops', 'disconnect_robot', 'load_plate_info', 'load_labware', 'send_command', 'get_error', 'get_position', 'get_status', 'check_complete', 'check_complete_loop', 'get_version', 'reset', 'get_config', 'get_grip_length', 'get_collapsed_distance', 'get_steps_per_unit', 'home', 'open', 'close', 'check_open', 'check_closed', 'check_plate', 'set_speed', 'list_points', 'jog', 'loadpoint', 'deletepoint', 'move', 'move_loc', 'get_plate', 'limp', 'check_for_lid', 'check_for_empty_nest', 'check_stack', 'remove_lid', 'replace_lid', 'plate_to_stack', 'lidnest_to_trash', 'plate_to_trash'], 'action_targets': {}, 'metadata': {'repo': 'AD-SDL/hudson_platecrane_module', 'repo_url': 'https://github.com/AD-SDL/hudson_platecrane_module', 'brand': 'Hudson Robotics', 'model': 'PlateCrane EX', 'device_type_cn': '板搬运机器人', 'device_type_en': 'Plate Handling Robot', 'source_framework': '生命科学', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 358, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect_sciclops(self, **kwargs):
        return self.call('connect_sciclops', kwargs=kwargs)

    def disconnect_robot(self, **kwargs):
        return self.call('disconnect_robot', kwargs=kwargs)

    def load_plate_info(self, **kwargs):
        return self.call('load_plate_info', kwargs=kwargs)

    def load_labware(self, **kwargs):
        return self.call('load_labware', kwargs=kwargs)

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

    def get_collapsed_distance(self, **kwargs):
        return self.call('get_collapsed_distance', kwargs=kwargs)

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

    def move_loc(self, **kwargs):
        return self.call('move_loc', kwargs=kwargs)

    def get_plate(self, **kwargs):
        return self.call('get_plate', kwargs=kwargs)

    def limp(self, **kwargs):
        return self.call('limp', kwargs=kwargs)

    def check_for_lid(self, **kwargs):
        return self.call('check_for_lid', kwargs=kwargs)

    def check_for_empty_nest(self, **kwargs):
        return self.call('check_for_empty_nest', kwargs=kwargs)

    def check_stack(self, **kwargs):
        return self.call('check_stack', kwargs=kwargs)

    def remove_lid(self, **kwargs):
        return self.call('remove_lid', kwargs=kwargs)

    def replace_lid(self, **kwargs):
        return self.call('replace_lid', kwargs=kwargs)

    def plate_to_stack(self, **kwargs):
        return self.call('plate_to_stack', kwargs=kwargs)

    def lidnest_to_trash(self, **kwargs):
        return self.call('lidnest_to_trash', kwargs=kwargs)

    def plate_to_trash(self, **kwargs):
        return self.call('plate_to_trash', kwargs=kwargs)

