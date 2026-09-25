from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHiokiIm3536(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Teslafly__Hioki-IM3536-Lcr-meter-python-IVI-driver', 'source_file': 'hioki/hiokiIM3536.py', 'class_name': 'hiokiIM3536', 'import_roots': [], 'candidate_methods': ['do_lcr_measurement', 'set_display_items', 'get_measurement_frequency', 'set_measurement_frequency'], 'action_targets': {'get_measurement_frequency': '_get_measurement_frequency', 'set_measurement_frequency': '_set_measurement_frequency'}, 'metadata': {'repo': 'Teslafly/Hioki-IM3536-Lcr-meter-python-IVI-driver', 'repo_url': 'https://github.com/Teslafly/Hioki-IM3536-Lcr-meter-python-IVI-driver', 'brand': 'Hioki', 'model': 'IM3536', 'device_type_cn': 'LCR表', 'device_type_en': 'LCR Meter', 'source_framework': '电化学/热分析/天平', 'tag_id': '4365', 'tag_name': '介电常数测定仪', 'tag_name_en': 'Dielectric Constant Meter', 'candidate_score': 132, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {'get_measurement_frequency': '_get_measurement_frequency', 'set_measurement_frequency': '_set_measurement_frequency'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def do_lcr_measurement(self, **kwargs):
        return self.call('do_lcr_measurement', kwargs=kwargs)

    def set_display_items(self, **kwargs):
        return self.call('set_display_items', kwargs=kwargs)

    def get_measurement_frequency(self, **kwargs):
        return self.call('get_measurement_frequency', kwargs=kwargs)

    def set_measurement_frequency(self, **kwargs):
        return self.call('set_measurement_frequency', kwargs=kwargs)

