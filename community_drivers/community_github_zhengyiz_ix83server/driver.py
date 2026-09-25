from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubZhengyizIx83server(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/ZhengyiZ_IX83Server', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'zhengyiz/ix83server', 'repo_url': 'https://github.com/ZhengyiZ/IX83Server', 'unit_id': 'gh_olympus_ix83', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Olympus/Evident', 'model_name': 'Olympus/Evident IX83'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


