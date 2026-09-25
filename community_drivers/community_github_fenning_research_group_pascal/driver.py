from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubFenningResearchGroupPascal(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/fenning-research-group_PASCAL', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'fenning-research-group/pascal', 'repo_url': 'https://github.com/fenning-research-group/PASCAL', 'unit_id': 'gh_laurell_ws_650', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Laurell', 'model_name': 'Laurell WS-650'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


