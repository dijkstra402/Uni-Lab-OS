from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubEmpaeconversionAuroraNeware(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/EmpaEconversion_aurora-neware', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'empaeconversion/aurora-neware', 'repo_url': 'https://github.com/EmpaEconversion/aurora-neware', 'unit_id': 'gh_neware_bts_8_0', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Neware', 'model_name': 'Neware BTS 8.0系列'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


