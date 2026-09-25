from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubCroningpAnalyticallabware(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/croningp_analyticallabware', 'source_file': 'AnalyticalLabware/devices/Magritek/Spinsolve/spinsolve.py', 'class_name': 'SpinsolveNMR', 'import_roots': [], 'candidate_methods': ['check_last_shimming', 'connect', 'disconnect', 'send_message', 'receive_reply', 'initialise', 'is_instrument_ready', 'load_commands', 'shim', 'shim_on_sample', 'set_user_folder', 'user_data', 'user_data', 'user_data', 'solvent', 'solvent', 'solvent', 'sample', 'sample', 'sample'], 'metadata': {'repo': 'croningp/analyticallabware', 'repo_url': 'https://github.com/croningp/analyticallabware', 'unit_id': 'gh_agilent_hplc_chemstation', 'source_file': 'AnalyticalLabware/devices/Magritek/Spinsolve/spinsolve.py', 'candidate_score': 122, 'manufacturer': 'Agilent', 'model_name': 'Agilent HPLC (ChemStation)'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def check_last_shimming(self, **kwargs):
        return self.call('check_last_shimming', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def send_message(self, **kwargs):
        return self.call('send_message', kwargs=kwargs)

    def receive_reply(self, **kwargs):
        return self.call('receive_reply', kwargs=kwargs)

    def initialise(self, **kwargs):
        return self.call('initialise', kwargs=kwargs)

    def is_instrument_ready(self, **kwargs):
        return self.call('is_instrument_ready', kwargs=kwargs)

    def load_commands(self, **kwargs):
        return self.call('load_commands', kwargs=kwargs)

    def shim(self, **kwargs):
        return self.call('shim', kwargs=kwargs)

    def shim_on_sample(self, **kwargs):
        return self.call('shim_on_sample', kwargs=kwargs)

    def set_user_folder(self, **kwargs):
        return self.call('set_user_folder', kwargs=kwargs)

    def user_data(self, **kwargs):
        return self.call('user_data', kwargs=kwargs)

    def user_data(self, **kwargs):
        return self.call('user_data', kwargs=kwargs)

    def user_data(self, **kwargs):
        return self.call('user_data', kwargs=kwargs)

    def solvent(self, **kwargs):
        return self.call('solvent', kwargs=kwargs)

    def solvent(self, **kwargs):
        return self.call('solvent', kwargs=kwargs)

    def solvent(self, **kwargs):
        return self.call('solvent', kwargs=kwargs)

    def sample(self, **kwargs):
        return self.call('sample', kwargs=kwargs)

    def sample(self, **kwargs):
        return self.call('sample', kwargs=kwargs)

    def sample(self, **kwargs):
        return self.call('sample', kwargs=kwargs)

