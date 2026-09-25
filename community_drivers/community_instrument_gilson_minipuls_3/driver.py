from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentGilsonMinipuls3(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/qiyaolin__Minipuls3', 'source_file': 'debugv2.py', 'class_name': 'MinipulsController', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'send_buffered_command', 'set_command_interval', 'set_remote_mode', 'set_keypad_mode', 'start_forward', 'start_backward', 'stop', 'set_speed'], 'action_targets': {}, 'metadata': {'repo': 'qiyaolin/Minipuls3', 'repo_url': 'https://github.com/qiyaolin/Minipuls3', 'brand': 'Gilson', 'model': 'Minipuls 3', 'device_type_cn': '蠕动泵', 'device_type_en': 'Peristaltic Pump', 'source_framework': '专用驱动', 'tag_id': '4451', 'tag_name': '蠕动泵', 'tag_name_en': 'Peristaltic Pump', 'candidate_score': 130, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def send_buffered_command(self, **kwargs):
        return self.call('send_buffered_command', kwargs=kwargs)

    def set_command_interval(self, **kwargs):
        return self.call('set_command_interval', kwargs=kwargs)

    def set_remote_mode(self, **kwargs):
        return self.call('set_remote_mode', kwargs=kwargs)

    def set_keypad_mode(self, **kwargs):
        return self.call('set_keypad_mode', kwargs=kwargs)

    def start_forward(self, **kwargs):
        return self.call('start_forward', kwargs=kwargs)

    def start_backward(self, **kwargs):
        return self.call('start_backward', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

