from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBrooksXpeel(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AD-SDL__brooks_xpeel_module', 'source_file': 'src/brooks_xpeel_driver.py', 'class_name': 'BROOKS_PEELER_DRIVER', 'import_roots': ['src'], 'candidate_methods': ['connect_peeler', 'response_fun', 'send_command', 'error', 'get_status', 'check_version', 'reset', 'restart', 'peel', 'seal_check', 'tape_remaining', 'plate_check', 'sensor_threshold', 'sensor_threshold_higher', 'sensor_threshold_lower', 'conveyor_out', 'conveyor_in', 'elevator_down', 'elevator_up', 'move_spool'], 'action_targets': {}, 'metadata': {'repo': 'AD-SDL/brooks_xpeel_module', 'repo_url': 'https://github.com/AD-SDL/brooks_xpeel_module', 'brand': 'Brooks', 'model': 'XPeel', 'device_type_cn': '撕膜仪', 'device_type_en': 'Plate Desealer', 'source_framework': 'AD-SDL', 'tag_id': '4396', 'tag_name': '撕膜仪', 'tag_name_en': 'Plate Desealer', 'candidate_score': 226, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect_peeler(self, **kwargs):
        return self.call('connect_peeler', kwargs=kwargs)

    def response_fun(self, **kwargs):
        return self.call('response_fun', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def error(self, **kwargs):
        return self.call('error', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def check_version(self, **kwargs):
        return self.call('check_version', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def restart(self, **kwargs):
        return self.call('restart', kwargs=kwargs)

    def peel(self, **kwargs):
        return self.call('peel', kwargs=kwargs)

    def seal_check(self, **kwargs):
        return self.call('seal_check', kwargs=kwargs)

    def tape_remaining(self, **kwargs):
        return self.call('tape_remaining', kwargs=kwargs)

    def plate_check(self, **kwargs):
        return self.call('plate_check', kwargs=kwargs)

    def sensor_threshold(self, **kwargs):
        return self.call('sensor_threshold', kwargs=kwargs)

    def sensor_threshold_higher(self, **kwargs):
        return self.call('sensor_threshold_higher', kwargs=kwargs)

    def sensor_threshold_lower(self, **kwargs):
        return self.call('sensor_threshold_lower', kwargs=kwargs)

    def conveyor_out(self, **kwargs):
        return self.call('conveyor_out', kwargs=kwargs)

    def conveyor_in(self, **kwargs):
        return self.call('conveyor_in', kwargs=kwargs)

    def elevator_down(self, **kwargs):
        return self.call('elevator_down', kwargs=kwargs)

    def elevator_up(self, **kwargs):
        return self.call('elevator_up', kwargs=kwargs)

    def move_spool(self, **kwargs):
        return self.call('move_spool', kwargs=kwargs)

