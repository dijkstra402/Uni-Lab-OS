from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentDobotMagician(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/luismesas__pydobot', 'source_file': 'pydobot/dobot.py', 'class_name': 'Dobot', 'import_roots': [], 'candidate_methods': ['get_eio', 'set_eio', 'close', 'go', 'move_to', 'suck', 'grip', 'speed', 'wait', 'pose'], 'action_targets': {}, 'metadata': {'repo': 'luismesas/pydobot', 'repo_url': 'https://github.com/luismesas/pydobot', 'brand': 'Dobot', 'model': 'Magician', 'device_type_cn': '教育机械臂', 'device_type_en': 'Educational Robot Arm', 'source_framework': '机器人/运动控制', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 138, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_eio(self, **kwargs):
        return self.call('get_eio', kwargs=kwargs)

    def set_eio(self, **kwargs):
        return self.call('set_eio', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def go(self, **kwargs):
        return self.call('go', kwargs=kwargs)

    def move_to(self, **kwargs):
        return self.call('move_to', kwargs=kwargs)

    def suck(self, **kwargs):
        return self.call('suck', kwargs=kwargs)

    def grip(self, **kwargs):
        return self.call('grip', kwargs=kwargs)

    def speed(self, **kwargs):
        return self.call('speed', kwargs=kwargs)

    def wait(self, **kwargs):
        return self.call('wait', kwargs=kwargs)

    def pose(self, **kwargs):
        return self.call('pose', kwargs=kwargs)

