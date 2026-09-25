from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentSeekThermalCompact(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/yaq-project__yaqd-seek', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'yaq-project/yaqd-seek', 'repo_url': 'https://github.com/yaq-project/yaqd-seek', 'brand': 'Seek Thermal', 'model': 'Compact', 'device_type_cn': '热像仪', 'device_type_en': 'Thermal Camera', 'source_framework': 'yaq', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


