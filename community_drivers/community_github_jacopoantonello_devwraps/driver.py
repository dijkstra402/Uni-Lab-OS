from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubJacopoantonelloDevwraps(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/jacopoantonello_devwraps', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'jacopoantonello/devwraps', 'repo_url': 'https://github.com/jacopoantonello/devwraps', 'unit_id': 'gh_boston_micromachines_multi_dm', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Boston Micromachines', 'model_name': 'Boston Micromachines Multi-DM/Kilo-C'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


