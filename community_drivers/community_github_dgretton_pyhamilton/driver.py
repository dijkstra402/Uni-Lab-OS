from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubDgrettonPyhamilton(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/dgretton_pyhamilton', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'dgretton/pyhamilton', 'repo_url': 'https://github.com/dgretton/pyhamilton', 'unit_id': 'gh_hamilton_star', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Hamilton', 'model_name': 'Hamilton STAR/STARlet'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


