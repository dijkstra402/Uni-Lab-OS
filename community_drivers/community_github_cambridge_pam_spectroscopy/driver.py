from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubCambridgePamSpectroscopy(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Cambridge-PAM_spectroscopy', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'cambridge-pam/spectroscopy', 'repo_url': 'https://github.com/Cambridge-PAM/spectroscopy', 'unit_id': 'gh_perkinelmer_lambda_750', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'PerkinElmer', 'model_name': 'PerkinElmer Lambda 750'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


