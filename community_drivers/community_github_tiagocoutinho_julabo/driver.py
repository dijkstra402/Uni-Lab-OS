from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubTiagocoutinhoJulabo(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/tiagocoutinho_julabo', 'source_file': 'julabo/connection.py', 'class_name': 'Serial', 'import_roots': [], 'candidate_methods': ['open', 'close', 'read', 'write', 'readline', 'write_readline'], 'metadata': {'repo': 'tiagocoutinho/julabo', 'repo_url': 'https://github.com/tiagocoutinho/julabo', 'unit_id': 'gh_julabo_cf31', 'source_file': 'julabo/connection.py', 'candidate_score': 92, 'manufacturer': 'Julabo', 'model_name': 'Julabo CF31/HL-4/MS-1000f'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def readline(self, **kwargs):
        return self.call('readline', kwargs=kwargs)

    def write_readline(self, **kwargs):
        return self.call('write_readline', kwargs=kwargs)

