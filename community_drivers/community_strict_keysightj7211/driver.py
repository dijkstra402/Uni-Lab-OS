from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictKeysightj7211(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Keysight/Keysight_J7211.py', 'class_name': 'Keysight_J7211', 'import_roots': ['src'], 'candidate_methods': ['get_attenuation', 'set_attenuation'], 'action_targets': {'get_attenuation': '__qcodes_param_get__attenuation', 'set_attenuation': '__qcodes_param_set__attenuation'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Keysight/Keysight_J7211.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {'get_attenuation': '__qcodes_param_get__attenuation', 'set_attenuation': '__qcodes_param_set__attenuation'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_attenuation(self, **kwargs):
        return self.call('get_attenuation', kwargs=kwargs)

    def set_attenuation(self, **kwargs):
        return self.call('set_attenuation', kwargs=kwargs)

