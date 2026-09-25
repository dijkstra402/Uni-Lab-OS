from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubFlorianLappNespLibPy(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/florian-lapp_nesp-lib-py', 'source_file': 'nesp_lib/port.py', 'class_name': 'Port', 'import_roots': [], 'candidate_methods': ['close'], 'metadata': {'repo': 'florian-lapp/nesp-lib-py', 'repo_url': 'https://github.com/florian-lapp/nesp-lib-py', 'unit_id': 'gh_new_era_ne_1000', 'source_file': 'nesp_lib/port.py', 'candidate_score': 102, 'manufacturer': 'New Era', 'model_name': 'New Era NE-1000'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

