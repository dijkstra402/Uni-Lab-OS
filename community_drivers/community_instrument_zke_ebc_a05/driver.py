from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentZkeEbcA05(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/wirenboard__zke-ebc-axx', 'source_file': 'zke_ebc_axx/device.py', 'class_name': 'EBCDevice', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'send_command', 'send_command_16bit', 'send_stop', 'encode_value', 'decode_value', 'start_charge_predefined', 'adjust_charge_predefined', 'start_charge_cccv', 'adjust_charge_cccv', 'start_discharge_cc', 'adjust_discharge_cc', 'start_discharge_cp', 'adjust_discharge_cp', 'discard_unread', 'read_measurement', 'read_until_complete', 'charge_cccv', 'discharge_cc', 'discharge_cp', 'discharge_cv', 'charge_cv'], 'action_targets': {}, 'metadata': {'repo': 'wirenboard/zke-ebc-axx', 'repo_url': 'https://github.com/wirenboard/zke-ebc-axx', 'brand': 'ZKE', 'model': 'EBC-A05', 'device_type_cn': '电池测试柜', 'device_type_en': 'Battery Test Cabinet', 'source_framework': '专用驱动', 'tag_id': '4427', 'tag_name': '电池测试柜', 'tag_name_en': 'Battery Test Cabinet', 'candidate_score': 258, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

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

    def discharge_cp(self, **kwargs):
        return self.call('discharge_cp', kwargs=kwargs)

    def discharge_cv(self, **kwargs):
        return self.call('discharge_cv', kwargs=kwargs)

    def charge_cv(self, **kwargs):
        return self.call('charge_cv', kwargs=kwargs)

