from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLinkamT962(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/swinburne-sensing__pylinkam', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'swinburne-sensing/pylinkam', 'repo_url': 'https://github.com/swinburne-sensing/pylinkam', 'brand': 'Linkam', 'model': 'T96 (热分析)', 'device_type_cn': '温度控制台(热分析联用)', 'device_type_en': 'Temperature Controller (Thermal Analysis)', 'source_framework': 'pylinkam', 'tag_id': '4420', 'tag_name': '热分析联用仪', 'tag_name_en': 'Thermal Analysis System', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


