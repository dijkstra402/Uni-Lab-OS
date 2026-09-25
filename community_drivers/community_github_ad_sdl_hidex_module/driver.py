from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAdSdlHidexModule(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/AD-SDL_hidex_module', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'ad-sdl/hidex_module', 'repo_url': 'https://github.com/AD-SDL/hidex_module', 'unit_id': 'gh_hidex_sense', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Hidex', 'model_name': 'Hidex Sense'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


