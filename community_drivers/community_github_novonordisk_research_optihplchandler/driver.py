from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubNovonordiskResearchOptihplchandler(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/novonordisk-research_OptiHPLCHandler', 'source_file': 'src/OptiHPLCHandler/empower_api_core.py', 'class_name': 'EmpowerConnection', 'import_roots': [], 'candidate_methods': ['content_key', 'login', 'logout', 'get', 'post', 'password', 'header', 'raise_for_status'], 'metadata': {'repo': 'novonordisk-research/optihplchandler', 'repo_url': 'https://github.com/novonordisk-research/OptiHPLCHandler', 'unit_id': 'gh_waters_empower_hplc', 'source_file': 'src/OptiHPLCHandler/empower_api_core.py', 'candidate_score': 21, 'manufacturer': 'Waters', 'model_name': 'Waters Empower HPLC系统'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def content_key(self, **kwargs):
        return self.call('content_key', kwargs=kwargs)

    def login(self, **kwargs):
        return self.call('login', kwargs=kwargs)

    def logout(self, **kwargs):
        return self.call('logout', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def post(self, **kwargs):
        return self.call('post', kwargs=kwargs)

    def password(self, **kwargs):
        return self.call('password', kwargs=kwargs)

    def header(self, **kwargs):
        return self.call('header', kwargs=kwargs)

    def raise_for_status(self, **kwargs):
        return self.call('raise_for_status', kwargs=kwargs)

