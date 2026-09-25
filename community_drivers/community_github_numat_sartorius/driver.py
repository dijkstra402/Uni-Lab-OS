from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubNumatSartorius(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/numat_sartorius', 'source_file': 'sartorius/util.py', 'class_name': 'SerialClient', 'import_roots': [], 'candidate_methods': ['close'], 'metadata': {'repo': 'numat/sartorius', 'repo_url': 'https://github.com/numat/sartorius', 'unit_id': 'gh_sartorius_entris', 'source_file': 'sartorius/util.py', 'candidate_score': 100, 'manufacturer': 'Sartorius', 'model_name': 'Sartorius Entris'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

