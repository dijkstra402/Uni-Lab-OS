from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubDensorobotOrinBcap(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/DENSORobot_orin_bcap', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'densorobot/orin_bcap', 'repo_url': 'https://github.com/DENSORobot/orin_bcap', 'unit_id': 'gh_denso_vs_060_rc8', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'DENSO', 'model_name': 'DENSO VS-060 (RC8)'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


