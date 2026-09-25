from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubNmgrlPychron(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/NMGRL_pychron', 'source_file': 'pychron/hardware/core/communicators/serial_communicator.py', 'class_name': 'SerialCommunicator', 'import_roots': [], 'candidate_methods': ['address', 'test_connection', 'reset', 'close', 'load_comdict', 'load', 'set_parity', 'set_stopbits', 'tell', 'read', 'ask', 'open'], 'metadata': {'repo': 'nmgrl/pychron', 'repo_url': 'https://github.com/NMGRL/pychron', 'unit_id': 'gh_eurotherm_series_2000', 'source_file': 'pychron/hardware/core/communicators/serial_communicator.py', 'candidate_score': 190, 'manufacturer': 'Eurotherm', 'model_name': 'Eurotherm Series 2000'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def address(self, **kwargs):
        return self.call('address', kwargs=kwargs)

    def test_connection(self, **kwargs):
        return self.call('test_connection', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def load_comdict(self, **kwargs):
        return self.call('load_comdict', kwargs=kwargs)

    def load(self, **kwargs):
        return self.call('load', kwargs=kwargs)

    def set_parity(self, **kwargs):
        return self.call('set_parity', kwargs=kwargs)

    def set_stopbits(self, **kwargs):
        return self.call('set_stopbits', kwargs=kwargs)

    def tell(self, **kwargs):
        return self.call('tell', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def ask(self, **kwargs):
        return self.call('ask', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

