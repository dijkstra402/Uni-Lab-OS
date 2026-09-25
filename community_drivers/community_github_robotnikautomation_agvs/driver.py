from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubRobotnikautomationAgvs(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/RobotnikAutomation_agvs', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'robotnikautomation/agvs', 'repo_url': 'https://github.com/RobotnikAutomation/agvs', 'unit_id': 'gh_robotnik_agvs', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Robotnik', 'model_name': 'Robotnik AGVS'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


