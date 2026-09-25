from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentInficonXtm2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/SweepMe__instrument-drivers', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'SweepMe/instrument-drivers', 'repo_url': 'https://github.com/SweepMe/instrument-drivers', 'brand': 'Inficon', 'model': 'XTM2', 'device_type_cn': '膜厚仪', 'device_type_en': 'Thin Film Deposition Controller', 'source_framework': 'SweepMe', 'tag_id': '4449', 'tag_name': '蒸镀仪', 'tag_name_en': 'Evaporation Coater', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


