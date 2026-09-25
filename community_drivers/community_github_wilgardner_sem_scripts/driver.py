from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubWilgardnerSemScripts(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/wilgardner_sem-scripts', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'wilgardner/sem-scripts', 'repo_url': 'https://github.com/wilgardner/sem-scripts', 'unit_id': 'gh_hitachi_su7000', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Hitachi', 'model_name': 'Hitachi SU7000'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


