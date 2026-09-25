from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentGilson215LiquidHandler(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/daan__gilson215', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'daan/gilson215', 'repo_url': 'https://github.com/daan/gilson215', 'brand': 'Gilson', 'model': '215 Liquid Handler', 'device_type_cn': '固相萃取设备', 'device_type_en': 'Solid Phase Extraction System', 'source_framework': '专用驱动', 'tag_id': '4379', 'tag_name': '固相萃取设备', 'tag_name_en': 'Solid Phase Extraction System', 'candidate_score': -999, 'parse_status': 'class_not_found', 'quality_status': 'broken', 'quality_reasons': ['no_class_found'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


