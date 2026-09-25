from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubHolgiSartoriusb(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/holgi_sartoriusb', 'source_file': 'sartoriusb/__init__.py', 'class_name': 'SartoriusUsb', 'import_roots': [], 'candidate_methods': ['connection', 'connect', 'open', 'close', 'send', 'read', 'readline', 'readlines', 'get', 'measure'], 'metadata': {'repo': 'holgi/sartoriusb', 'repo_url': 'https://github.com/holgi/sartoriusb', 'unit_id': 'gh_sartorius_quintix', 'source_file': 'sartoriusb/__init__.py', 'candidate_score': 127, 'manufacturer': 'Sartorius', 'model_name': 'Sartorius Quintix'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def connection(self, **kwargs):
        return self.call('connection', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def send(self, **kwargs):
        return self.call('send', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def readline(self, **kwargs):
        return self.call('readline', kwargs=kwargs)

    def readlines(self, **kwargs):
        return self.call('readlines', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def measure(self, **kwargs):
        return self.call('measure', kwargs=kwargs)

