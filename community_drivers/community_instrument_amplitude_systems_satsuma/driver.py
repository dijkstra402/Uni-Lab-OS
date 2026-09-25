from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAmplitudeSystemsSatsuma(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyMoDAQ__pymodaq_plugins_amplitude', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'PyMoDAQ/pymodaq_plugins_amplitude', 'repo_url': 'https://github.com/PyMoDAQ/pymodaq_plugins_amplitude', 'brand': 'Amplitude Systems', 'model': 'Satsuma', 'device_type_cn': '飞秒激光器', 'device_type_en': 'Femtosecond Laser', 'source_framework': 'PyMoDAQ', 'tag_id': '4439', 'tag_name': '紫外-可见分光光谱仪', 'tag_name_en': 'UV-Vis Spectrophotometer', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


