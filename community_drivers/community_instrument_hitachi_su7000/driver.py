from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHitachiSu7000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/wilgardner__sem-scripts', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'wilgardner/sem-scripts', 'repo_url': 'https://github.com/wilgardner/sem-scripts', 'brand': 'Hitachi', 'model': 'SU7000', 'device_type_cn': '扫描电子显微镜', 'device_type_en': 'Scanning Electron Microscope', 'source_framework': '专用驱动', 'tag_id': '4390', 'tag_name': '扫描电子显微镜', 'tag_name_en': 'Scanning Electron Microscope', 'candidate_score': -999, 'parse_status': 'class_not_found', 'quality_status': 'broken', 'quality_reasons': ['no_class_found'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


