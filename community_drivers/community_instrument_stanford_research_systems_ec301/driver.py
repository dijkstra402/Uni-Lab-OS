from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentStanfordResearchSystemsEc301(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/mdmurbach__ec301-eis', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'mdmurbach/ec301-eis', 'repo_url': 'https://github.com/mdmurbach/ec301-eis', 'brand': 'Stanford Research Systems', 'model': 'EC301', 'device_type_cn': '恒电位仪/EIS', 'device_type_en': 'Potentiostat/EIS', 'source_framework': '电化学/热分析/天平', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': -999, 'parse_status': 'class_not_found', 'quality_status': 'broken', 'quality_reasons': ['no_class_found'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


