from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentEpsonScaraRc90Rc700(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AustralianSynchrotron__aspyrobot', 'source_file': 'aspyrobot/server.py', 'class_name': 'RobotServer', 'import_roots': [], 'candidate_methods': ['setup', 'shutdown', 'operation_update', 'values_update', 'refresh', 'clear'], 'action_targets': {}, 'metadata': {'repo': 'AustralianSynchrotron/aspyrobot', 'repo_url': 'https://github.com/AustralianSynchrotron/aspyrobot', 'brand': 'Epson', 'model': 'SCARA (RC90/RC700)', 'device_type_cn': 'SCARA机械臂', 'device_type_en': 'SCARA Robot', 'source_framework': '机器人/运动控制', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 114, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def setup(self, **kwargs):
        return self.call('setup', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

    def operation_update(self, **kwargs):
        return self.call('operation_update', kwargs=kwargs)

    def values_update(self, **kwargs):
        return self.call('values_update', kwargs=kwargs)

    def refresh(self, **kwargs):
        return self.call('refresh', kwargs=kwargs)

    def clear(self, **kwargs):
        return self.call('clear', kwargs=kwargs)

