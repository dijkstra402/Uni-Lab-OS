from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThermoFisherTecnaiComServer(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/instamatic-dev__instamatic-tecnai-server', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'instamatic-dev/instamatic-tecnai-server', 'repo_url': 'https://github.com/instamatic-dev/instamatic-tecnai-server', 'brand': 'Thermo Fisher', 'model': 'Tecnai (COM server)', 'device_type_cn': '透射电子显微镜', 'device_type_en': 'TEM', 'source_framework': 'instamatic', 'tag_id': '4456', 'tag_name': '透射电子显微镜', 'tag_name_en': 'Transmission Electron Microscope', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


