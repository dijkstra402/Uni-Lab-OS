from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictCryocon26(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Cryocon/cryocon_26.py', 'class_name': 'Cryocon_26', 'import_roots': ['src'], 'candidate_methods': ['get_control_enabled'], 'action_targets': {'get_control_enabled': '__qcodes_param_get__control_enabled'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Cryocon/cryocon_26.py', 'confidence': 0.8, 'quality_score': 0.88, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {'get_control_enabled': '__qcodes_param_get__control_enabled'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_control_enabled(self, **kwargs):
        return self.call('get_control_enabled', kwargs=kwargs)

