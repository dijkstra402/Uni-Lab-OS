from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubYaqProjectYaqdOmega(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/yaq-project_yaqd-omega', 'source_file': 'yaqd_omega/_omega_iseries_modbus.py', 'class_name': 'OmegaIseriesModbus', 'import_roots': [], 'candidate_methods': ['direct_serial_write', 'update_state'], 'metadata': {'repo': 'yaq-project/yaqd-omega', 'repo_url': 'https://github.com/yaq-project/yaqd-omega', 'unit_id': 'gh_omega_iseries', 'source_file': 'yaqd_omega/_omega_iseries_modbus.py', 'candidate_score': 67, 'manufacturer': 'Omega', 'model_name': 'Omega iSeries'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def direct_serial_write(self, **kwargs):
        return self.call('direct_serial_write', kwargs=kwargs)

    def update_state(self, **kwargs):
        return self.call('update_state', kwargs=kwargs)

