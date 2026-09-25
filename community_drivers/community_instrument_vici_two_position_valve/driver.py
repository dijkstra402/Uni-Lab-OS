from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentViciTwoPositionValve(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/yaq-project__yaqd-vici', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'yaq-project/yaqd-vici', 'repo_url': 'https://github.com/yaq-project/yaqd-vici', 'brand': 'VICI', 'model': 'Two-Position Valve', 'device_type_cn': '多通阀', 'device_type_en': 'Multi-position Valve', 'source_framework': 'yaq', 'tag_id': '4382', 'tag_name': '多通阀', 'tag_name_en': 'Multi-Port Valve', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


