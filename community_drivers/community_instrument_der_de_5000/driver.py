from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentDerDe5000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/4x1md__de5000_lcr_py', 'source_file': '', 'class_name': '', 'import_roots': ['src'], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': '4x1md/de5000_lcr_py', 'repo_url': 'https://github.com/4x1md/de5000_lcr_py', 'brand': 'DER', 'model': 'DE-5000', 'device_type_cn': '介电常数测定仪', 'device_type_en': 'Dielectric Constant Meter', 'source_framework': '专用驱动', 'tag_id': '4365', 'tag_name': '介电常数测定仪', 'tag_name_en': 'Dielectric Constant Meter', 'candidate_score': -999, 'parse_status': 'class_not_found', 'quality_status': 'broken', 'quality_reasons': ['no_class_found'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


