from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubZserg8Pylabware(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/zserg8_pylabware', 'source_file': 'PyLabware/connections.py', 'class_name': 'TCPIPConnection', 'import_roots': [], 'candidate_methods': ['open_connection', 'connection_listener', 'close_connection', 'is_connection_open', 'transmit', 'receive'], 'metadata': {'repo': 'zserg8/pylabware', 'repo_url': 'https://github.com/zserg8/pylabware', 'unit_id': 'gh_tecan_cavro_xlp_6000', 'source_file': 'PyLabware/connections.py', 'candidate_score': 145, 'manufacturer': 'Tecan Cavro', 'model_name': 'Tecan Cavro XLP 6000'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def open_connection(self, **kwargs):
        return self.call('open_connection', kwargs=kwargs)

    def connection_listener(self, **kwargs):
        return self.call('connection_listener', kwargs=kwargs)

    def close_connection(self, **kwargs):
        return self.call('close_connection', kwargs=kwargs)

    def is_connection_open(self, **kwargs):
        return self.call('is_connection_open', kwargs=kwargs)

    def transmit(self, **kwargs):
        return self.call('transmit', kwargs=kwargs)

    def receive(self, **kwargs):
        return self.call('receive', kwargs=kwargs)

