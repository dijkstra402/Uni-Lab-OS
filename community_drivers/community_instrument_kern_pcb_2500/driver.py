from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKernPcb2500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/cooper-group-uol-robotics__kern_pcb_balance', 'source_file': 'kern_pcb_balance_driver/src/kern_pcb_balance_driver/kern_serial_driver.py', 'class_name': 'KernDriver', 'import_roots': [], 'candidate_methods': ['weight', 'zero'], 'action_targets': {}, 'metadata': {'repo': 'cooper-group-uol-robotics/kern_pcb_balance', 'repo_url': 'https://github.com/cooper-group-uol-robotics/kern_pcb_balance', 'brand': 'Kern', 'model': 'PCB 2500', 'device_type_cn': '电子天平', 'device_type_en': 'Balance', 'source_framework': '独立驱动', 'tag_id': '4426', 'tag_name': '电子天平', 'tag_name_en': 'Electronic Balance', 'candidate_score': 90, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def weight(self, **kwargs):
        return self.call('weight', kwargs=kwargs)

    def zero(self, **kwargs):
        return self.call('zero', kwargs=kwargs)

