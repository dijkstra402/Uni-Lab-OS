from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentZeissSemRemcon32(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/ScopeFoundry__HW_zeiss_sem', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'ScopeFoundry/HW_zeiss_sem', 'repo_url': 'https://github.com/ScopeFoundry/HW_zeiss_sem', 'brand': 'Zeiss', 'model': 'SEM (REMCON32)', 'device_type_cn': '扫描电子显微镜', 'device_type_en': 'Scanning Electron Microscope', 'source_framework': 'ScopeFoundry', 'tag_id': '4390', 'tag_name': '扫描电子显微镜', 'tag_name_en': 'Scanning Electron Microscope', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


