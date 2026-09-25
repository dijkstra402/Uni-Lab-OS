from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubTraecpRigakuSmartlab(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Traecp_Rigaku-SmartLab', 'source_file': 'SmartLab.py', 'class_name': 'RasFile', 'import_roots': [], 'candidate_methods': ['parse'], 'metadata': {'repo': 'traecp/rigaku-smartlab', 'repo_url': 'https://github.com/Traecp/Rigaku-SmartLab', 'unit_id': 'gh_rigaku_smartlab__ras', 'source_file': 'SmartLab.py', 'candidate_score': 16, 'manufacturer': 'Rigaku', 'model_name': 'Rigaku SmartLab (.RAS)'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def parse(self, **kwargs):
        return self.call('parse', kwargs=kwargs)

