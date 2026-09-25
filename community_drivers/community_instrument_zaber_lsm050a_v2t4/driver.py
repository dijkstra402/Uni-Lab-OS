from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentZaberLsm050aV2t4(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyMoDAQ__pymodaq_plugins_zaber', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'PyMoDAQ/pymodaq_plugins_zaber', 'repo_url': 'https://github.com/PyMoDAQ/pymodaq_plugins_zaber', 'brand': 'Zaber', 'model': 'LSM050A-V2T4', 'device_type_cn': '电动平移台', 'device_type_en': 'Motorized Translation Stage', 'source_framework': 'PyMoDAQ', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


