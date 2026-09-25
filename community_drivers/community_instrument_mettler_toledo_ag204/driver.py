from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMettlerToledoAg204(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/cyclikal__cyp-mettler-ag204', 'source_file': 'mettler_ag204/mettler_ag204.py', 'class_name': 'MettlerLogger', 'import_roots': [], 'candidate_methods': ['communicate', 'get_balance_model', 'get_balance_serial', 'read'], 'action_targets': {}, 'metadata': {'repo': 'cyclikal/cyp-mettler-ag204', 'repo_url': 'https://github.com/cyclikal/cyp-mettler-ag204', 'brand': 'Mettler Toledo', 'model': 'AG204', 'device_type_cn': '电子天平', 'device_type_en': 'Electronic Balance', 'source_framework': '专用驱动', 'tag_id': '4426', 'tag_name': '电子天平', 'tag_name_en': 'Electronic Balance', 'candidate_score': 90, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def communicate(self, **kwargs):
        return self.call('communicate', kwargs=kwargs)

    def get_balance_model(self, **kwargs):
        return self.call('get_balance_model', kwargs=kwargs)

    def get_balance_serial(self, **kwargs):
        return self.call('get_balance_serial', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

