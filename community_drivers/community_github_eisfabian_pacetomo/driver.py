from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubEisfabianPacetomo(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/eisfabian_PACEtomo', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'eisfabian/pacetomo', 'repo_url': 'https://github.com/eisfabian/PACEtomo', 'unit_id': 'gh_jeol_cryoarm_300', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'JEOL', 'model_name': 'JEOL cryoARM 300'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


