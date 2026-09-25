from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentChemspeedCstApiChemspeedAgent(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/ignaczgerg__chemspeed-agent', 'source_file': 'gp_api.py', 'class_name': 'TanimotoKernel', 'import_roots': [], 'candidate_methods': ['K', 'Kdiag', 'update_gradients_full', 'gradients_X', 'to_dict', 'from_dict'], 'action_targets': {}, 'metadata': {'repo': 'ignaczgerg/chemspeed-agent', 'repo_url': 'https://github.com/ignaczgerg/chemspeed-agent', 'brand': 'Chemspeed', 'model': 'CST-API (chemspeed-agent)', 'device_type_cn': '并行反应仪', 'device_type_en': 'Parallel Synthesizer', 'source_framework': '独立驱动', 'tag_id': '4385', 'tag_name': '并行反应仪', 'tag_name_en': 'Parallel Reactor', 'candidate_score': 86, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def K(self, **kwargs):
        return self.call('K', kwargs=kwargs)

    def Kdiag(self, **kwargs):
        return self.call('Kdiag', kwargs=kwargs)

    def update_gradients_full(self, **kwargs):
        return self.call('update_gradients_full', kwargs=kwargs)

    def gradients_X(self, **kwargs):
        return self.call('gradients_X', kwargs=kwargs)

    def to_dict(self, **kwargs):
        return self.call('to_dict', kwargs=kwargs)

    def from_dict(self, **kwargs):
        return self.call('from_dict', kwargs=kwargs)

