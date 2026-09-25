from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubDaanGilson215(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/daan_gilson215', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'daan/gilson215', 'repo_url': 'https://github.com/daan/gilson215', 'unit_id': 'gh_gilson_215_liquid_handler', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Gilson', 'model_name': 'Gilson 215 Liquid Handler'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


