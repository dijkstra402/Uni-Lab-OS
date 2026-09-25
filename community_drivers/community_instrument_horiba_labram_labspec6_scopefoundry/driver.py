from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHoribaLabramLabspec6Scopefoundry(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/UBene__HW_labspec', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'UBene/HW_labspec', 'repo_url': 'https://github.com/UBene/HW_labspec', 'brand': 'Horiba', 'model': 'LabRAM/LabSpec6 (ScopeFoundry)', 'device_type_cn': '拉曼光谱仪', 'device_type_en': 'Raman Spectrometer', 'source_framework': 'ScopeFoundry', 'tag_id': '4392', 'tag_name': '拉曼光谱仪', 'tag_name_en': 'Raman Spectrometer', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


