from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPicoquantTimeharpTh260(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyMoDAQ__pymodaq_plugins_picoquant', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'PyMoDAQ/pymodaq_plugins_picoquant', 'repo_url': 'https://github.com/PyMoDAQ/pymodaq_plugins_picoquant', 'brand': 'PicoQuant', 'model': 'TimeHarp TH260', 'device_type_cn': '时间相关单光子计数', 'device_type_en': 'TCSPC', 'source_framework': 'PyMoDAQ', 'tag_id': '4447', 'tag_name': '荧光显微镜', 'tag_name_en': 'Fluorescence Microscope', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


