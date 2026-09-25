from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubQedsoftwareBrukeropusreader(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/qedsoftware_brukeropusreader', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'qedsoftware/brukeropusreader', 'repo_url': 'https://github.com/qedsoftware/brukeropusreader', 'unit_id': 'gh_bruker_tensor_27', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Bruker', 'model_name': 'Bruker Tensor 27'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


