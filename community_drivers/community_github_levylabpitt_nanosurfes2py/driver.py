from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubLevylabpittNanosurfes2py(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/levylabpitt_NanosurfES2Py', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'levylabpitt/nanosurfes2py', 'repo_url': 'https://github.com/levylabpitt/NanosurfES2Py', 'unit_id': 'gh_nanosurf_easyscan_2', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Nanosurf', 'model_name': 'Nanosurf EasyScan 2'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


