from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentQsonicaSonicator(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/machineagency__science-jubilee', 'source_file': 'src/science_jubilee/Machine.py', 'class_name': 'Machine', 'import_roots': ['src'], 'candidate_methods': ['connect', 'configured_axes', 'configured_tools', 'active_tool_index', 'tool_z_offsets', 'axis_limits', 'position', 'load_deck', 'split_response_objects', 'gcode', 'delay_time', 'push_machine_state', 'pop_machine_state', 'download_file', 'reset', 'home_all', 'home_xyu', 'home_x', 'home_y', 'home_u', 'home_v', 'home_z', 'home_e', 'home_in_place', 'set_tool_offset', 'move_to', 'move', 'dwell', 'safe_z_movement', 'load_tool', 'reload_tool', 'pickup_tool', 'park_tool', 'get_position', 'load_labware', 'tool_lock', 'tool_unlock', 'disconnect'], 'action_targets': {}, 'metadata': {'repo': 'machineagency/science-jubilee', 'repo_url': 'https://github.com/machineagency/science-jubilee', 'brand': 'Qsonica', 'model': 'Sonicator', 'device_type_cn': '超声破碎仪', 'device_type_en': 'Ultrasonic Homogenizer', 'source_framework': 'science-jubilee', 'tag_id': '4453', 'tag_name': '超声破碎仪', 'tag_name_en': 'Ultrasonic Homogenizer', 'candidate_score': 350, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def configured_axes(self, **kwargs):
        return self.call('configured_axes', kwargs=kwargs)

    def configured_tools(self, **kwargs):
        return self.call('configured_tools', kwargs=kwargs)

    def active_tool_index(self, **kwargs):
        return self.call('active_tool_index', kwargs=kwargs)

    def tool_z_offsets(self, **kwargs):
        return self.call('tool_z_offsets', kwargs=kwargs)

    def axis_limits(self, **kwargs):
        return self.call('axis_limits', kwargs=kwargs)

    def position(self, **kwargs):
        return self.call('position', kwargs=kwargs)

    def load_deck(self, **kwargs):
        return self.call('load_deck', kwargs=kwargs)

    def split_response_objects(self, **kwargs):
        return self.call('split_response_objects', kwargs=kwargs)

    def gcode(self, **kwargs):
        return self.call('gcode', kwargs=kwargs)

    def delay_time(self, **kwargs):
        return self.call('delay_time', kwargs=kwargs)

    def push_machine_state(self, **kwargs):
        return self.call('push_machine_state', kwargs=kwargs)

    def pop_machine_state(self, **kwargs):
        return self.call('pop_machine_state', kwargs=kwargs)

    def download_file(self, **kwargs):
        return self.call('download_file', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def home_all(self, **kwargs):
        return self.call('home_all', kwargs=kwargs)

    def home_xyu(self, **kwargs):
        return self.call('home_xyu', kwargs=kwargs)

    def home_x(self, **kwargs):
        return self.call('home_x', kwargs=kwargs)

    def home_y(self, **kwargs):
        return self.call('home_y', kwargs=kwargs)

    def home_u(self, **kwargs):
        return self.call('home_u', kwargs=kwargs)

    def home_v(self, **kwargs):
        return self.call('home_v', kwargs=kwargs)

    def home_z(self, **kwargs):
        return self.call('home_z', kwargs=kwargs)

    def home_e(self, **kwargs):
        return self.call('home_e', kwargs=kwargs)

    def home_in_place(self, **kwargs):
        return self.call('home_in_place', kwargs=kwargs)

    def set_tool_offset(self, **kwargs):
        return self.call('set_tool_offset', kwargs=kwargs)

    def move_to(self, **kwargs):
        return self.call('move_to', kwargs=kwargs)

    def move(self, **kwargs):
        return self.call('move', kwargs=kwargs)

    def dwell(self, **kwargs):
        return self.call('dwell', kwargs=kwargs)

    def safe_z_movement(self, **kwargs):
        return self.call('safe_z_movement', kwargs=kwargs)

    def load_tool(self, **kwargs):
        return self.call('load_tool', kwargs=kwargs)

    def reload_tool(self, **kwargs):
        return self.call('reload_tool', kwargs=kwargs)

    def pickup_tool(self, **kwargs):
        return self.call('pickup_tool', kwargs=kwargs)

    def park_tool(self, **kwargs):
        return self.call('park_tool', kwargs=kwargs)

    def get_position(self, **kwargs):
        return self.call('get_position', kwargs=kwargs)

    def load_labware(self, **kwargs):
        return self.call('load_labware', kwargs=kwargs)

    def tool_lock(self, **kwargs):
        return self.call('tool_lock', kwargs=kwargs)

    def tool_unlock(self, **kwargs):
        return self.call('tool_unlock', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

