from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAgilentn9000a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Agilent/Agilent_N9000A.py', 'class_name': 'Agilent_N9000A', 'import_roots': ['src'], 'candidate_methods': ['power_parser', 'get_rf_center_frequency', 'set_rf_center_frequency', 'get_video_bandwidth', 'set_video_bandwidth', 'get_resolution_bandwidth', 'set_resolution_bandwidth', 'get_power', 'get_power_spectral_density'], 'action_targets': {'get_rf_center_frequency': '__qcodes_param_get__rf_center_frequency', 'set_rf_center_frequency': '__qcodes_param_set__rf_center_frequency', 'get_video_bandwidth': '__qcodes_param_get__video_bandwidth', 'set_video_bandwidth': '__qcodes_param_set__video_bandwidth', 'get_resolution_bandwidth': '__qcodes_param_get__resolution_bandwidth', 'set_resolution_bandwidth': '__qcodes_param_set__resolution_bandwidth', 'get_power': '__qcodes_param_get__power', 'get_power_spectral_density': '__qcodes_param_get__power_spectral_density'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Agilent/Agilent_N9000A.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_rf_center_frequency': '__qcodes_param_get__rf_center_frequency', 'set_rf_center_frequency': '__qcodes_param_set__rf_center_frequency', 'get_video_bandwidth': '__qcodes_param_get__video_bandwidth', 'set_video_bandwidth': '__qcodes_param_set__video_bandwidth', 'get_resolution_bandwidth': '__qcodes_param_get__resolution_bandwidth', 'set_resolution_bandwidth': '__qcodes_param_set__resolution_bandwidth', 'get_power': '__qcodes_param_get__power', 'get_power_spectral_density': '__qcodes_param_get__power_spectral_density'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def power_parser(self, **kwargs):
        return self.call('power_parser', kwargs=kwargs)

    def get_rf_center_frequency(self, **kwargs):
        return self.call('get_rf_center_frequency', kwargs=kwargs)

    def set_rf_center_frequency(self, **kwargs):
        return self.call('set_rf_center_frequency', kwargs=kwargs)

    def get_video_bandwidth(self, **kwargs):
        return self.call('get_video_bandwidth', kwargs=kwargs)

    def set_video_bandwidth(self, **kwargs):
        return self.call('set_video_bandwidth', kwargs=kwargs)

    def get_resolution_bandwidth(self, **kwargs):
        return self.call('get_resolution_bandwidth', kwargs=kwargs)

    def set_resolution_bandwidth(self, **kwargs):
        return self.call('set_resolution_bandwidth', kwargs=kwargs)

    def get_power(self, **kwargs):
        return self.call('get_power', kwargs=kwargs)

    def get_power_spectral_density(self, **kwargs):
        return self.call('get_power_spectral_density', kwargs=kwargs)

