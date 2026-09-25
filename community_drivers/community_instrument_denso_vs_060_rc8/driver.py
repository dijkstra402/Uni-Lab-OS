from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentDensoVs060Rc8(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/DENSORobot__orin_bcap', 'source_file': '', 'class_name': '', 'import_roots': ['python'], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'DENSORobot/orin_bcap', 'repo_url': 'https://github.com/DENSORobot/orin_bcap', 'brand': 'Denso', 'model': 'VS-060 (RC8)', 'device_type_cn': '工业机械臂', 'device_type_en': 'Industrial Robot Arm', 'source_framework': '机器人/运动控制', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': -999, 'parse_status': 'class_not_found', 'quality_status': 'broken', 'quality_reasons': ['no_class_found'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


