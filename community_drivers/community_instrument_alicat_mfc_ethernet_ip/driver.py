from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAlicatMfcEthernetIp(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/ScopeFoundry__HW_alicat_eip', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'ScopeFoundry/HW_alicat_eip', 'repo_url': 'https://github.com/ScopeFoundry/HW_alicat_eip', 'brand': 'Alicat', 'model': 'MFC (EtherNet/IP)', 'device_type_cn': '质量流量控制器', 'device_type_en': 'Mass Flow Controller', 'source_framework': 'ScopeFoundry', 'tag_id': '4373', 'tag_name': '化学气相沉积设备', 'tag_name_en': 'Chemical Vapor Deposition System', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


