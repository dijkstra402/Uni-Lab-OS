from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubIsiscomputinggroupIbex(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/ISISComputingGroup_IBEX', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'isiscomputinggroup/ibex', 'repo_url': 'https://github.com/ISISComputingGroup/IBEX', 'unit_id': 'gh_jasco_pu_4180', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'JASCO', 'model_name': 'JASCO PU-4180'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


