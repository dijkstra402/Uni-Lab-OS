from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubQunLiuJeol2010f(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/qun-liu_jeol2010f', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'qun-liu/jeol2010f', 'repo_url': 'https://github.com/qun-liu/jeol2010f', 'unit_id': 'gh_jeol_2010f', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'JEOL', 'model_name': 'JEOL 2010F'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


