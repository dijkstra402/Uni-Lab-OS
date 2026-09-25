from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKernEocDe(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/ellery-it__odoo-serial-scale-drivers', 'source_file': '24.10/SSD-KernEOC.py', 'class_name': 'KernEOCDriver', 'import_roots': [], 'candidate_methods': ['supported'], 'action_targets': {}, 'metadata': {'repo': 'ellery-it/odoo-serial-scale-drivers', 'repo_url': 'https://github.com/ellery-it/odoo-serial-scale-drivers', 'brand': 'Kern', 'model': 'EOC / DE (串口协议)', 'device_type_cn': '电子天平', 'device_type_en': 'Electronic Balance', 'source_framework': '电化学/热分析/天平', 'tag_id': '4426', 'tag_name': '电子天平', 'tag_name_en': 'Electronic Balance', 'candidate_score': 86, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def supported(self, **kwargs):
        return self.call('supported', kwargs=kwargs)

