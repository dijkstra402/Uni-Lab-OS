from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOhausExplorerEx225dAd(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/amsikking__ohaus_EX225DAD', 'source_file': 'ohaus_EX225DAD.py', 'class_name': 'Controller', 'import_roots': [], 'candidate_methods': ['move_door', 'zero', 'tare', 'get_immediate_weight', 'close'], 'action_targets': {}, 'metadata': {'repo': 'amsikking/ohaus_EX225DAD', 'repo_url': 'https://github.com/amsikking/ohaus_EX225DAD', 'brand': 'Ohaus', 'model': 'Explorer EX225D/AD', 'device_type_cn': '电子天平', 'device_type_en': 'Electronic Balance', 'source_framework': '专用驱动', 'tag_id': '4426', 'tag_name': '电子天平', 'tag_name_en': 'Electronic Balance', 'candidate_score': 102, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def move_door(self, **kwargs):
        return self.call('move_door', kwargs=kwargs)

    def zero(self, **kwargs):
        return self.call('zero', kwargs=kwargs)

    def tare(self, **kwargs):
        return self.call('tare', kwargs=kwargs)

    def get_immediate_weight(self, **kwargs):
        return self.call('get_immediate_weight', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

