from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubRomerolabSyringePumpController(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/RomeroLab_syringe-pump-controller', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'romerolab/syringe-pump-controller', 'repo_url': 'https://github.com/RomeroLab/syringe-pump-controller', 'unit_id': 'gh_new_era_ne_500', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'New Era', 'model_name': 'New Era NE-500'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


