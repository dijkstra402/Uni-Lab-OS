from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPalmsensPalmsensSdk(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/PalmSens_PalmSens_SDK', 'source_file': 'python/src/pypalmsens/_instruments/instrument_manager_async.py', 'class_name': 'InstrumentManagerAsync', 'import_roots': [], 'candidate_methods': ['is_measuring', 'is_connected', 'ensure_connection', 'connect', 'status', 'set_cell', 'read_current', 'get_current_range', 'set_current_range', 'read_potential', 'set_potential', 'get_potential_range', 'set_potential_range', 'get_instrument_serial', 'register_status_callback', 'unregister_status_callback', 'validate_method', 'measure', 'wait_digital_trigger', 'abort'], 'metadata': {'repo': 'palmsens/palmsens_sdk', 'repo_url': 'https://github.com/PalmSens/PalmSens_SDK', 'unit_id': 'gh_palmsens_palmsens4', 'source_file': 'python/src/pypalmsens/_instruments/instrument_manager_async.py', 'candidate_score': 76, 'manufacturer': 'PalmSens', 'model_name': 'PalmSens PalmSens4'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def is_measuring(self, **kwargs):
        return self.call('is_measuring', kwargs=kwargs)

    def is_connected(self, **kwargs):
        return self.call('is_connected', kwargs=kwargs)

    def ensure_connection(self, **kwargs):
        return self.call('ensure_connection', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def status(self, **kwargs):
        return self.call('status', kwargs=kwargs)

    def set_cell(self, **kwargs):
        return self.call('set_cell', kwargs=kwargs)

    def read_current(self, **kwargs):
        return self.call('read_current', kwargs=kwargs)

    def get_current_range(self, **kwargs):
        return self.call('get_current_range', kwargs=kwargs)

    def set_current_range(self, **kwargs):
        return self.call('set_current_range', kwargs=kwargs)

    def read_potential(self, **kwargs):
        return self.call('read_potential', kwargs=kwargs)

    def set_potential(self, **kwargs):
        return self.call('set_potential', kwargs=kwargs)

    def get_potential_range(self, **kwargs):
        return self.call('get_potential_range', kwargs=kwargs)

    def set_potential_range(self, **kwargs):
        return self.call('set_potential_range', kwargs=kwargs)

    def get_instrument_serial(self, **kwargs):
        return self.call('get_instrument_serial', kwargs=kwargs)

    def register_status_callback(self, **kwargs):
        return self.call('register_status_callback', kwargs=kwargs)

    def unregister_status_callback(self, **kwargs):
        return self.call('unregister_status_callback', kwargs=kwargs)

    def validate_method(self, **kwargs):
        return self.call('validate_method', kwargs=kwargs)

    def measure(self, **kwargs):
        return self.call('measure', kwargs=kwargs)

    def wait_digital_trigger(self, **kwargs):
        return self.call('wait_digital_trigger', kwargs=kwargs)

    def abort(self, **kwargs):
        return self.call('abort', kwargs=kwargs)

