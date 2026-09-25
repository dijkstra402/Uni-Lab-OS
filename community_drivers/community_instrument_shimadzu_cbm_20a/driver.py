from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentShimadzuCbm20a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/paulscherrerinstitute__shimadzu_pump', 'source_file': 'shimadzu_pump/shimadzu_driver.py', 'class_name': 'ShimadzuCbm20', 'import_roots': [], 'candidate_methods': ['login', 'logout', 'start', 'stop', 'set', 'get', 'get_all'], 'action_targets': {}, 'metadata': {'repo': 'paulscherrerinstitute/shimadzu_pump', 'repo_url': 'https://github.com/paulscherrerinstitute/shimadzu_pump', 'brand': 'Shimadzu', 'model': 'CBM-20A', 'device_type_cn': 'HPLC控制器/泵', 'device_type_en': 'HPLC Controller/Pump', 'source_framework': '泵阀/液体处理', 'tag_id': '4418', 'tag_name': '液相色谱质谱联用仪', 'tag_name_en': 'LC-MS', 'candidate_score': 126, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def login(self, **kwargs):
        return self.call('login', kwargs=kwargs)

    def logout(self, **kwargs):
        return self.call('logout', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def set(self, **kwargs):
        return self.call('set', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def get_all(self, **kwargs):
        return self.call('get_all', kwargs=kwargs)

