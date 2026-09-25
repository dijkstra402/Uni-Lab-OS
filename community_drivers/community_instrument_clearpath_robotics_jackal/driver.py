from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentClearpathRoboticsJackal(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/jackal__jackal_robot', 'source_file': 'jackal_bringup/src/jackal_bringup/multicast/Receiver.py', 'class_name': 'Datagram', 'import_roots': [], 'candidate_methods': ['bind', 'pipe', 'pipeone', 'read', 'cleanup', 'close'], 'action_targets': {}, 'metadata': {'repo': 'jackal/jackal_robot', 'repo_url': 'https://github.com/jackal/jackal_robot', 'brand': 'Clearpath Robotics', 'model': 'Jackal', 'device_type_cn': '自主移动机器人', 'device_type_en': 'AGV', 'source_framework': 'ROS-jackal', 'tag_id': '4360', 'tag_name': 'AGV', 'tag_name_en': 'AGV', 'candidate_score': 86, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def bind(self, **kwargs):
        return self.call('bind', kwargs=kwargs)

    def pipe(self, **kwargs):
        return self.call('pipe', kwargs=kwargs)

    def pipeone(self, **kwargs):
        return self.call('pipeone', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def cleanup(self, **kwargs):
        return self.call('cleanup', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

