from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubZplabRpcScope(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/zplab_rpc-scope', 'source_file': 'scope/simple_rpc/rpc_client.py', 'class_name': 'ZMQClient', 'import_roots': [], 'candidate_methods': ['reconnect', 'timeout_sec', 'send_interrupt'], 'metadata': {'repo': 'zplab/rpc-scope', 'repo_url': 'https://github.com/zplab/rpc-scope', 'unit_id': 'gh_leica_dmi8', 'source_file': 'scope/simple_rpc/rpc_client.py', 'candidate_score': 107, 'manufacturer': 'Leica', 'model_name': 'Leica DMi8'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def reconnect(self, **kwargs):
        return self.call('reconnect', kwargs=kwargs)

    def timeout_sec(self, **kwargs):
        return self.call('timeout_sec', kwargs=kwargs)

    def send_interrupt(self, **kwargs):
        return self.call('send_interrupt', kwargs=kwargs)

