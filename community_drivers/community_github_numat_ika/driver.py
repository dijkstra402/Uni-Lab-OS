from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubNumatIka(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/numat_ika', 'source_file': 'ika/util.py', 'class_name': 'SerialClient', 'import_roots': [], 'candidate_methods': ['close'], 'metadata': {'repo': 'numat/ika', 'repo_url': 'https://github.com/numat/ika', 'unit_id': 'gh_ika_rct_5_digital', 'source_file': 'ika/util.py', 'candidate_score': 155, 'manufacturer': 'IKA', 'model_name': 'IKA RCT 5 digital / C-MAG HS 7'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

