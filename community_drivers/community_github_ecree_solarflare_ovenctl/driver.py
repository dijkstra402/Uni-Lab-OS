from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubEcreeSolarflareOvenctl(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/ecree-solarflare_ovenctl', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'ecree-solarflare/ovenctl', 'repo_url': 'https://github.com/ecree-solarflare/ovenctl', 'unit_id': 'gh_binder_mk_53', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'BINDER', 'model_name': 'BINDER MK 53'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


