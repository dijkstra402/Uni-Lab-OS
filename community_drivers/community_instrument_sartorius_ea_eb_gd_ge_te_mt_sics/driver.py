from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentSartoriusEaEbGdGeTeMtSics(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/rgieseke__pySartorius', 'source_file': 'sartorius.py', 'class_name': 'Sartorius', 'import_roots': [], 'candidate_methods': ['value', 'display_unit', 'tara_zero', 'tara', 'zero'], 'action_targets': {}, 'metadata': {'repo': 'rgieseke/pySartorius', 'repo_url': 'https://github.com/rgieseke/pySartorius', 'brand': 'Sartorius', 'model': 'EA/EB/GD/GE/TE (MT-SICS协议)', 'device_type_cn': '电子天平', 'device_type_en': 'Electronic Balance', 'source_framework': '电化学/热分析/天平', 'tag_id': '4426', 'tag_name': '电子天平', 'tag_name_en': 'Electronic Balance', 'candidate_score': 90, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def value(self, **kwargs):
        return self.call('value', kwargs=kwargs)

    def display_unit(self, **kwargs):
        return self.call('display_unit', kwargs=kwargs)

    def tara_zero(self, **kwargs):
        return self.call('tara_zero', kwargs=kwargs)

    def tara(self, **kwargs):
        return self.call('tara', kwargs=kwargs)

    def zero(self, **kwargs):
        return self.call('zero', kwargs=kwargs)

