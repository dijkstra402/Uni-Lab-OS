from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubBadariraoEurotemp(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/badarirao_Eurotemp', 'source_file': 'eurotherm.py', 'class_name': 'Eurotherm', 'import_roots': [], 'candidate_methods': ['send_read_param', 'read_param', 'write_param', 'get_current_temperature', 'set_temperature', 'get_setpoint_temperature'], 'metadata': {'repo': 'badarirao/eurotemp', 'repo_url': 'https://github.com/badarirao/Eurotemp', 'unit_id': 'gh_eurotherm_2408', 'source_file': 'eurotherm.py', 'candidate_score': 79, 'manufacturer': 'Eurotherm', 'model_name': 'Eurotherm 2408'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def send_read_param(self, **kwargs):
        return self.call('send_read_param', kwargs=kwargs)

    def read_param(self, **kwargs):
        return self.call('read_param', kwargs=kwargs)

    def write_param(self, **kwargs):
        return self.call('write_param', kwargs=kwargs)

    def get_current_temperature(self, **kwargs):
        return self.call('get_current_temperature', kwargs=kwargs)

    def set_temperature(self, **kwargs):
        return self.call('set_temperature', kwargs=kwargs)

    def get_setpoint_temperature(self, **kwargs):
        return self.call('get_setpoint_temperature', kwargs=kwargs)

