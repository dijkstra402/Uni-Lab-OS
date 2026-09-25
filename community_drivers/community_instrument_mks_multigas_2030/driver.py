from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMksMultigas2030(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/yaq-project__yaqd-mks', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'yaq-project/yaqd-mks', 'repo_url': 'https://github.com/yaq-project/yaqd-mks', 'brand': 'MKS', 'model': 'MultiGas 2030', 'device_type_cn': '气体分析仪', 'device_type_en': 'FTIR Gas Analyzer', 'source_framework': 'yaq', 'tag_id': '4440', 'tag_name': '红外光谱仪', 'tag_name_en': 'Infrared Spectrometer', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


