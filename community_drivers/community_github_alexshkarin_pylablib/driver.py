from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAlexshkarinPylablib(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/AlexShkarin_pyLabLib', 'source_file': 'pylablib/core/devio/comm_backend.py', 'class_name': 'SerialDeviceBackend', 'import_roots': [], 'candidate_methods': ['open', 'close', 'is_opened', 'single_op', 'set_timeout', 'get_timeout', 'readline', 'read', 'read_multichar_term', 'write', 'list_resources'], 'metadata': {'repo': 'alexshkarin/pylablib', 'repo_url': 'https://github.com/AlexShkarin/pyLabLib', 'unit_id': 'gh_andor_ixon', 'source_file': 'pylablib/core/devio/comm_backend.py', 'candidate_score': 217, 'manufacturer': 'Andor', 'model_name': 'Andor iXon'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def is_opened(self, **kwargs):
        return self.call('is_opened', kwargs=kwargs)

    def single_op(self, **kwargs):
        return self.call('single_op', kwargs=kwargs)

    def set_timeout(self, **kwargs):
        return self.call('set_timeout', kwargs=kwargs)

    def get_timeout(self, **kwargs):
        return self.call('get_timeout', kwargs=kwargs)

    def readline(self, **kwargs):
        return self.call('readline', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def read_multichar_term(self, **kwargs):
        return self.call('read_multichar_term', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def list_resources(self, **kwargs):
        return self.call('list_resources', kwargs=kwargs)

