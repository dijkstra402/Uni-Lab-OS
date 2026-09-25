from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubMdmurbachEc301Eis(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/mdmurbach_ec301-eis', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'mdmurbach/ec301-eis', 'repo_url': 'https://github.com/mdmurbach/ec301-eis', 'unit_id': 'gh_srs_ec301', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'SRS', 'model_name': 'SRS EC301'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


