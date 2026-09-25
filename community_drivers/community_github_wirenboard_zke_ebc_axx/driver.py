from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubWirenboardZkeEbcAxx(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/wirenboard_zke-ebc-axx', 'source_file': 'zke_ebc_axx/device.py', 'class_name': 'EBCDevice', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'send_command', 'send_command_16bit', 'send_stop', 'encode_value', 'decode_value', 'start_charge_predefined', 'adjust_charge_predefined', 'start_charge_cccv', 'adjust_charge_cccv', 'start_discharge_cc', 'adjust_discharge_cc', 'start_discharge_cp', 'adjust_discharge_cp', 'discard_unread', 'read_measurement', 'read_until_complete', 'charge_cccv', 'discharge_cc'], 'metadata': {'repo': 'wirenboard/zke-ebc-axx', 'repo_url': 'https://github.com/wirenboard/zke-ebc-axx', 'unit_id': 'gh_zke_ebc_a05', 'source_file': 'zke_ebc_axx/device.py', 'candidate_score': 165, 'manufacturer': 'ZKE', 'model_name': 'ZKE EBC-A05'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def send_command_16bit(self, **kwargs):
        return self.call('send_command_16bit', kwargs=kwargs)

    def send_stop(self, **kwargs):
        return self.call('send_stop', kwargs=kwargs)

    def encode_value(self, **kwargs):
        return self.call('encode_value', kwargs=kwargs)

    def decode_value(self, **kwargs):
        return self.call('decode_value', kwargs=kwargs)

    def start_charge_predefined(self, **kwargs):
        return self.call('start_charge_predefined', kwargs=kwargs)

    def adjust_charge_predefined(self, **kwargs):
        return self.call('adjust_charge_predefined', kwargs=kwargs)

    def start_charge_cccv(self, **kwargs):
        return self.call('start_charge_cccv', kwargs=kwargs)

    def adjust_charge_cccv(self, **kwargs):
        return self.call('adjust_charge_cccv', kwargs=kwargs)

    def start_discharge_cc(self, **kwargs):
        return self.call('start_discharge_cc', kwargs=kwargs)

    def adjust_discharge_cc(self, **kwargs):
        return self.call('adjust_discharge_cc', kwargs=kwargs)

    def start_discharge_cp(self, **kwargs):
        return self.call('start_discharge_cp', kwargs=kwargs)

    def adjust_discharge_cp(self, **kwargs):
        return self.call('adjust_discharge_cp', kwargs=kwargs)

    def discard_unread(self, **kwargs):
        return self.call('discard_unread', kwargs=kwargs)

    def read_measurement(self, **kwargs):
        return self.call('read_measurement', kwargs=kwargs)

    def read_until_complete(self, **kwargs):
        return self.call('read_until_complete', kwargs=kwargs)

    def charge_cccv(self, **kwargs):
        return self.call('charge_cccv', kwargs=kwargs)

    def discharge_cc(self, **kwargs):
        return self.call('discharge_cc', kwargs=kwargs)

