from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubBec4Ovencontrol(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/bec4_ovenControl', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'bec4/ovencontrol', 'repo_url': 'https://github.com/bec4/ovenControl', 'unit_id': 'gh_memmert_un30', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Memmert', 'model_name': 'Memmert UN30'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


