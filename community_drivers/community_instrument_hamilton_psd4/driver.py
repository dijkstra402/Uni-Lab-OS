from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHamiltonPsd4(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/todddangerfarr__hamilton-psd4-pump-controller', 'source_file': 'hamilton_pump_controller/ui/main_window.py', 'class_name': 'MainWindow', 'import_roots': [], 'candidate_methods': ['add_accel', 'add_delay', 'add_move', 'add_speed', 'add_valve', 'build_and_send_command', 'change_position', 'check_port', 'command_list_changed', 'connect_to_port', 'get_available_accels', 'get_available_speeds', 'init_pump', 'load_command_file', 'move_down', 'move_to_position', 'move_up', 'open_close_valve', 'populate_speed_and_accel', 'remove_selected_command', 'save_to_file', 'search_for_ports', 'send_command', 'set_pump_accel', 'set_pump_speed'], 'action_targets': {}, 'metadata': {'repo': 'todddangerfarr/hamilton-psd4-pump-controller', 'repo_url': 'https://github.com/todddangerfarr/hamilton-psd4-pump-controller', 'brand': 'Hamilton', 'model': 'PSD4', 'device_type_cn': '柱塞泵', 'device_type_en': 'Plunger Pump', 'source_framework': '专用驱动', 'tag_id': '4403', 'tag_name': '柱塞泵', 'tag_name_en': 'Plunger Pump', 'candidate_score': 254, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def add_accel(self, **kwargs):
        return self.call('add_accel', kwargs=kwargs)

    def add_delay(self, **kwargs):
        return self.call('add_delay', kwargs=kwargs)

    def add_move(self, **kwargs):
        return self.call('add_move', kwargs=kwargs)

    def add_speed(self, **kwargs):
        return self.call('add_speed', kwargs=kwargs)

    def add_valve(self, **kwargs):
        return self.call('add_valve', kwargs=kwargs)

    def build_and_send_command(self, **kwargs):
        return self.call('build_and_send_command', kwargs=kwargs)

    def change_position(self, **kwargs):
        return self.call('change_position', kwargs=kwargs)

    def check_port(self, **kwargs):
        return self.call('check_port', kwargs=kwargs)

    def command_list_changed(self, **kwargs):
        return self.call('command_list_changed', kwargs=kwargs)

    def connect_to_port(self, **kwargs):
        return self.call('connect_to_port', kwargs=kwargs)

    def get_available_accels(self, **kwargs):
        return self.call('get_available_accels', kwargs=kwargs)

    def get_available_speeds(self, **kwargs):
        return self.call('get_available_speeds', kwargs=kwargs)

    def init_pump(self, **kwargs):
        return self.call('init_pump', kwargs=kwargs)

    def load_command_file(self, **kwargs):
        return self.call('load_command_file', kwargs=kwargs)

    def move_down(self, **kwargs):
        return self.call('move_down', kwargs=kwargs)

    def move_to_position(self, **kwargs):
        return self.call('move_to_position', kwargs=kwargs)

    def move_up(self, **kwargs):
        return self.call('move_up', kwargs=kwargs)

    def open_close_valve(self, **kwargs):
        return self.call('open_close_valve', kwargs=kwargs)

    def populate_speed_and_accel(self, **kwargs):
        return self.call('populate_speed_and_accel', kwargs=kwargs)

    def remove_selected_command(self, **kwargs):
        return self.call('remove_selected_command', kwargs=kwargs)

    def save_to_file(self, **kwargs):
        return self.call('save_to_file', kwargs=kwargs)

    def search_for_ports(self, **kwargs):
        return self.call('search_for_ports', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def set_pump_accel(self, **kwargs):
        return self.call('set_pump_accel', kwargs=kwargs)

    def set_pump_speed(self, **kwargs):
        return self.call('set_pump_speed', kwargs=kwargs)

