from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentCoherentChameleonCompactOpo(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/ScopeFoundry__HW_chameleon_compact_opo', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'ScopeFoundry/HW_chameleon_compact_opo', 'repo_url': 'https://github.com/ScopeFoundry/HW_chameleon_compact_opo', 'brand': 'Coherent', 'model': 'Chameleon Compact OPO', 'device_type_cn': '光参量振荡器', 'device_type_en': 'Optical Parametric Oscillator', 'source_framework': 'ScopeFoundry', 'tag_id': '4439', 'tag_name': '紫外-可见分光光谱仪', 'tag_name_en': 'UV-Vis Spectrophotometer', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


