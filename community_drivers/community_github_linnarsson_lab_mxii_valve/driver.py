from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubLinnarssonLabMxiiValve(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/linnarsson-lab_MXII-valve', 'source_file': 'MXII_valve.py', 'class_name': 'MX_valve', 'import_roots': [], 'candidate_methods': ['stripped_hex', 'wait_ready', 'message_builder', 'read_message', 'write_message', 'response_interpret', 'get_port', 'change_port'], 'metadata': {'repo': 'linnarsson-lab/mxii-valve', 'repo_url': 'https://github.com/linnarsson-lab/MXII-valve', 'unit_id': 'gh_idex_rheodyne_mx_series_ii', 'source_file': 'MXII_valve.py', 'candidate_score': 107, 'manufacturer': 'IDEX (Rheodyne)', 'model_name': 'IDEX (Rheodyne) MX Series II'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def stripped_hex(self, **kwargs):
        return self.call('stripped_hex', kwargs=kwargs)

    def wait_ready(self, **kwargs):
        return self.call('wait_ready', kwargs=kwargs)

    def message_builder(self, **kwargs):
        return self.call('message_builder', kwargs=kwargs)

    def read_message(self, **kwargs):
        return self.call('read_message', kwargs=kwargs)

    def write_message(self, **kwargs):
        return self.call('write_message', kwargs=kwargs)

    def response_interpret(self, **kwargs):
        return self.call('response_interpret', kwargs=kwargs)

    def get_port(self, **kwargs):
        return self.call('get_port', kwargs=kwargs)

    def change_port(self, **kwargs):
        return self.call('change_port', kwargs=kwargs)

