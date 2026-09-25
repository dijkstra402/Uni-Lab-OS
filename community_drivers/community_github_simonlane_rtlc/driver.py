from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubSimonlaneRtlc(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/SimonLane_RTLC', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'simonlane/rtlc', 'repo_url': 'https://github.com/SimonLane/RTLC', 'unit_id': 'gh_leica_tcs_sp8', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Leica', 'model_name': 'Leica TCS SP8'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


