from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMicrochipMcp9600(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/yaq-project__yaqd-microchip', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'yaq-project/yaqd-microchip', 'repo_url': 'https://github.com/yaq-project/yaqd-microchip', 'brand': 'Microchip', 'model': 'MCP9600', 'device_type_cn': '温度传感器', 'device_type_en': 'Thermocouple EMF-to-Temperature Converter', 'source_framework': 'yaq', 'tag_id': '4438', 'tag_name': '箱式电阻炉', 'tag_name_en': 'Box Resistance Furnace', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


