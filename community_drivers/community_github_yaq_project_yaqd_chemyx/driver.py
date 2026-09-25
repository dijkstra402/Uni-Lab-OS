from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubYaqProjectYaqdChemyx(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/yaq-project_yaqd-chemyx', 'source_file': 'yaqd_chemyx/_chemyx_fusion.py', 'class_name': 'ChemyxFusion', 'import_roots': [], 'candidate_methods': ['close', 'direct_serial_write', 'get_rate', 'prime', 'purge', 'set_rate', 'update_state'], 'metadata': {'repo': 'yaq-project/yaqd-chemyx', 'repo_url': 'https://github.com/yaq-project/yaqd-chemyx', 'unit_id': 'gh_chemyx_fusion', 'source_file': 'yaqd_chemyx/_chemyx_fusion.py', 'candidate_score': 49, 'manufacturer': 'Chemyx', 'model_name': 'Chemyx Fusion'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def direct_serial_write(self, **kwargs):
        return self.call('direct_serial_write', kwargs=kwargs)

    def get_rate(self, **kwargs):
        return self.call('get_rate', kwargs=kwargs)

    def prime(self, **kwargs):
        return self.call('prime', kwargs=kwargs)

    def purge(self, **kwargs):
        return self.call('purge', kwargs=kwargs)

    def set_rate(self, **kwargs):
        return self.call('set_rate', kwargs=kwargs)

    def update_state(self, **kwargs):
        return self.call('update_state', kwargs=kwargs)

