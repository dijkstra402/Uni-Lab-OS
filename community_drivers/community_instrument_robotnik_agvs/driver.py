from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentRobotnikAgvs(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/RobotnikAutomation__agvs', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'RobotnikAutomation/agvs', 'repo_url': 'https://github.com/RobotnikAutomation/agvs', 'brand': 'Robotnik', 'model': 'AGVS', 'device_type_cn': 'AGV自动导引车', 'device_type_en': 'AGV', 'source_framework': 'ROS', 'tag_id': '4360', 'tag_name': 'AGV', 'tag_name_en': 'AGV', 'candidate_score': -999, 'parse_status': 'class_not_found', 'quality_status': 'broken', 'quality_reasons': ['no_class_found'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


