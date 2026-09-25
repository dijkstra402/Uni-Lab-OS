from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictThorlabsprm1z8(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Thorlabs/PRM1Z8.py', 'class_name': 'Thorlabs_PRM1Z8', 'import_roots': ['src'], 'candidate_methods': ['get_idn', 'get_position', 'set_position'], 'action_targets': {'get_position': '__qcodes_param_get__position', 'set_position': '__qcodes_param_set__position'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Thorlabs/PRM1Z8.py', 'confidence': 0.9, 'quality_score': 1.06, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {'get_position': '__qcodes_param_get__position', 'set_position': '__qcodes_param_set__position'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def get_position(self, **kwargs):
        return self.call('get_position', kwargs=kwargs)

    def set_position(self, **kwargs):
        return self.call('set_position', kwargs=kwargs)

