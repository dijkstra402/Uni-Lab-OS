from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubNanoporetechMinknowApi(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/nanoporetech_minknow_api', 'source_file': 'python/minknow_api/__init__.py', 'class_name': 'Connection', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'nanoporetech/minknow_api', 'repo_url': 'https://github.com/nanoporetech/minknow_api', 'unit_id': 'gh_oxford_nanopore_minion', 'source_file': 'python/minknow_api/__init__.py', 'candidate_score': 54, 'manufacturer': 'Oxford Nanopore', 'model_name': 'Oxford Nanopore MinION'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


