from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPaulbnjlPyserspec(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/paulbnjl_PySerSpec', 'source_file': 'PySerSpec/connect.py', 'class_name': 'ConnectPort', 'import_roots': [], 'candidate_methods': ['get_port', 'open_port', 'close_port'], 'metadata': {'repo': 'paulbnjl/pyserspec', 'repo_url': 'https://github.com/paulbnjl/PySerSpec', 'unit_id': 'gh_shimadzu_uvmini_1240', 'source_file': 'PySerSpec/connect.py', 'candidate_score': 109, 'manufacturer': 'Shimadzu', 'model_name': 'Shimadzu UVmini-1240'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def get_port(self, **kwargs):
        return self.call('get_port', kwargs=kwargs)

    def open_port(self, **kwargs):
        return self.call('open_port', kwargs=kwargs)

    def close_port(self, **kwargs):
        return self.call('close_port', kwargs=kwargs)

