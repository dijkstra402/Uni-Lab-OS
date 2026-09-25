from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMcc118(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/yaq-project__yaqd-mcc', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'yaq-project/yaqd-mcc', 'repo_url': 'https://github.com/yaq-project/yaqd-mcc', 'brand': 'MCC', 'model': '118', 'device_type_cn': '数据采集卡', 'device_type_en': 'DAQ Board', 'source_framework': 'yaq', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


