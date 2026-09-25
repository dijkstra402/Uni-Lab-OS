from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubCroningpPycont(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/croningp_pycont', 'source_file': 'pycont/controller.py', 'class_name': 'PumpIO', 'import_roots': [], 'candidate_methods': ['from_config', 'from_configfile', 'open', 'close', 'flush_input', 'write', 'readline', 'write_and_readline'], 'metadata': {'repo': 'croningp/pycont', 'repo_url': 'https://github.com/croningp/pycont', 'unit_id': 'gh_tricontinent_c3000', 'source_file': 'pycont/controller.py', 'candidate_score': 157, 'manufacturer': 'Tricontinent', 'model_name': 'Tricontinent C3000'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def from_config(self, **kwargs):
        return self.call('from_config', kwargs=kwargs)

    def from_configfile(self, **kwargs):
        return self.call('from_configfile', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def flush_input(self, **kwargs):
        return self.call('flush_input', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def readline(self, **kwargs):
        return self.call('readline', kwargs=kwargs)

    def write_and_readline(self, **kwargs):
        return self.call('write_and_readline', kwargs=kwargs)

