from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubChenmingzhangScaleManipulator(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/chenmingzhang_scale_manipulator', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'chenmingzhang/scale_manipulator', 'repo_url': 'https://github.com/chenmingzhang/scale_manipulator', 'unit_id': 'gh_ohaus_ranger_3000', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Ohaus', 'model_name': 'Ohaus Ranger 3000'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


