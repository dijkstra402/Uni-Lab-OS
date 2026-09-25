from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKernPcb60000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/ncadou__kern-odoo-driver', 'source_file': 'kern_pcb6000.py', 'class_name': 'KernPCBScaleDriver', 'import_roots': [], 'candidate_methods': ['supported', 'get_weight', 'tare', 'zero', 'action', 'disconnect'], 'action_targets': {}, 'metadata': {'repo': 'ncadou/kern-odoo-driver', 'repo_url': 'https://github.com/ncadou/kern-odoo-driver', 'brand': 'Kern', 'model': 'PCB 6000-0', 'device_type_cn': '电子天平', 'device_type_en': 'Electronic Balance', 'source_framework': '专用驱动', 'tag_id': '4426', 'tag_name': '电子天平', 'tag_name_en': 'Electronic Balance', 'candidate_score': 146, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def supported(self, **kwargs):
        return self.call('supported', kwargs=kwargs)

    def get_weight(self, **kwargs):
        return self.call('get_weight', kwargs=kwargs)

    def tare(self, **kwargs):
        return self.call('tare', kwargs=kwargs)

    def zero(self, **kwargs):
        return self.call('zero', kwargs=kwargs)

    def action(self, **kwargs):
        return self.call('action', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

