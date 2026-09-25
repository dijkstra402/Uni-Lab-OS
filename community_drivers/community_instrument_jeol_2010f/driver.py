from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentJeol2010f(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/qun-liu__jeol2010f', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'qun-liu/jeol2010f', 'repo_url': 'https://github.com/qun-liu/jeol2010f', 'brand': 'JEOL', 'model': '2010F', 'device_type_cn': 'TEM', 'device_type_en': 'Transmission Electron Microscope', 'source_framework': '显微镜/成像', 'tag_id': '4456', 'tag_name': '透射电子显微镜', 'tag_name_en': 'Transmission Electron Microscope', 'candidate_score': -999, 'parse_status': 'class_not_found', 'quality_status': 'broken', 'quality_reasons': ['no_class_found'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


