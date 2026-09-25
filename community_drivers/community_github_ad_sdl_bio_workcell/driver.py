from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAdSdlBioWorkcell(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/AD-SDL_BIO_workcell', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'ad-sdl/bio_workcell', 'repo_url': 'https://github.com/AD-SDL/BIO_workcell', 'unit_id': 'gh_liconic_storex_stx88', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'LiCONiC', 'model_name': 'LiCONiC StoreX STX88'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


