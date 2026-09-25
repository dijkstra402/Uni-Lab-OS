from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubNimwegenlabMimNikonti(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/nimwegenLab_MiM_NikonTi', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'nimwegenlab/mim_nikonti', 'repo_url': 'https://github.com/nimwegenLab/MiM_NikonTi', 'unit_id': 'gh_nikon_ti_e', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Nikon', 'model_name': 'Nikon Ti-E'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


