from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubModi1987Iiwapy3(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Modi1987_iiwaPy3', 'source_file': 'python_client/mySock.py', 'class_name': 'mySock', 'import_roots': [], 'candidate_methods': ['send', 'receive', 'close'], 'metadata': {'repo': 'modi1987/iiwapy3', 'repo_url': 'https://github.com/Modi1987/iiwaPy3', 'unit_id': 'gh_kuka_iiwa_7r800', 'source_file': 'python_client/mySock.py', 'candidate_score': 87, 'manufacturer': 'KUKA', 'model_name': 'KUKA iiwa 7R800 / iiwa 14R820'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def send(self, **kwargs):
        return self.call('send', kwargs=kwargs)

    def receive(self, **kwargs):
        return self.call('receive', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

