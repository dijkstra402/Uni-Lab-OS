from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBiologicSp240(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/bicarlsen__easy-biologic', 'source_file': 'src/easy_biologic/device.py', 'class_name': 'BiologicDeviceAsync', 'import_roots': ['src'], 'candidate_methods': ['address', 'idn', 'kind', 'info', 'plugged', 'channels', 'hardware_configuration', 'techniques', 'connect', 'disconnect', 'populate_info', 'is_connected', 'channel_configuration', 'set_channel_configuration', 'load_technique', 'load_techniques', 'update_parameters', 'start_channel', 'start_channels', 'stop_channel', 'stop_channels', 'channel_info', 'get_values', 'get_data'], 'action_targets': {}, 'metadata': {'repo': 'bicarlsen/easy-biologic', 'repo_url': 'https://github.com/bicarlsen/easy-biologic', 'brand': 'BioLogic', 'model': 'SP-240', 'device_type_cn': '恒电位仪', 'device_type_en': 'Potentiostat', 'source_framework': '电化学/热分析/天平', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 270, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def address(self, **kwargs):
        return self.call('address', kwargs=kwargs)

    def idn(self, **kwargs):
        return self.call('idn', kwargs=kwargs)

    def kind(self, **kwargs):
        return self.call('kind', kwargs=kwargs)

    def info(self, **kwargs):
        return self.call('info', kwargs=kwargs)

    def plugged(self, **kwargs):
        return self.call('plugged', kwargs=kwargs)

    def channels(self, **kwargs):
        return self.call('channels', kwargs=kwargs)

    def hardware_configuration(self, **kwargs):
        return self.call('hardware_configuration', kwargs=kwargs)

    def techniques(self, **kwargs):
        return self.call('techniques', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def populate_info(self, **kwargs):
        return self.call('populate_info', kwargs=kwargs)

    def is_connected(self, **kwargs):
        return self.call('is_connected', kwargs=kwargs)

    def channel_configuration(self, **kwargs):
        return self.call('channel_configuration', kwargs=kwargs)

    def set_channel_configuration(self, **kwargs):
        return self.call('set_channel_configuration', kwargs=kwargs)

    def load_technique(self, **kwargs):
        return self.call('load_technique', kwargs=kwargs)

    def load_techniques(self, **kwargs):
        return self.call('load_techniques', kwargs=kwargs)

    def update_parameters(self, **kwargs):
        return self.call('update_parameters', kwargs=kwargs)

    def start_channel(self, **kwargs):
        return self.call('start_channel', kwargs=kwargs)

    def start_channels(self, **kwargs):
        return self.call('start_channels', kwargs=kwargs)

    def stop_channel(self, **kwargs):
        return self.call('stop_channel', kwargs=kwargs)

    def stop_channels(self, **kwargs):
        return self.call('stop_channels', kwargs=kwargs)

    def channel_info(self, **kwargs):
        return self.call('channel_info', kwargs=kwargs)

    def get_values(self, **kwargs):
        return self.call('get_values', kwargs=kwargs)

    def get_data(self, **kwargs):
        return self.call('get_data', kwargs=kwargs)

