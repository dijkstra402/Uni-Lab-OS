from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubNumatIsmatec(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/numat_ismatec', 'source_file': 'ismatec/util.py', 'class_name': 'SerialCommunicator', 'import_roots': [], 'candidate_methods': ['read', 'readline', 'write', 'close'], 'metadata': {'repo': 'numat/ismatec', 'repo_url': 'https://github.com/numat/ismatec', 'unit_id': 'gh_ismatec_reglo_icc', 'source_file': 'ismatec/util.py', 'candidate_score': 155, 'manufacturer': 'Ismatec', 'model_name': 'Ismatec Reglo ICC'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def readline(self, **kwargs):
        return self.call('readline', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

