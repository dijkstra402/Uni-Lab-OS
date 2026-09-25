from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictLm500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Cryomagnetics/LM_500.py', 'class_name': 'LM_500', 'import_roots': ['src'], 'candidate_methods': ['get_he_level', 'get_units', 'set_units'], 'action_targets': {'get_he_level': '__qcodes_param_get__he_level', 'get_units': '__qcodes_param_get__units', 'set_units': '__qcodes_param_set__units'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Cryomagnetics/LM_500.py', 'confidence': 0.8, 'quality_score': 0.88, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {'get_he_level': '__qcodes_param_get__he_level', 'get_units': '__qcodes_param_get__units', 'set_units': '__qcodes_param_set__units'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_he_level(self, **kwargs):
        return self.call('get_he_level', kwargs=kwargs)

    def get_units(self, **kwargs):
        return self.call('get_units', kwargs=kwargs)

    def set_units(self, **kwargs):
        return self.call('set_units', kwargs=kwargs)

