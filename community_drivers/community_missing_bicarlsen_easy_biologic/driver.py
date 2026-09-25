from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingBicarlsenEasyBiologic(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/bicarlsen__easy-biologic', 'source_file': 'src/easy_biologic/device.py', 'class_name': 'BiologicDevice', 'import_roots': ['src'], 'candidate_methods': ['__init__', '__del__', 'address', 'idn', 'kind', 'info', 'plugged', 'channels', 'hardware_configuration', 'techniques', 'connect', 'disconnect', 'populate_info', 'is_connected', 'channel_configuration', 'set_channel_configuration', 'load_technique', 'load_techniques', 'update_parameters', 'start_channel', 'start_channels', 'stop_channel', 'stop_channels', 'channel_info', 'get_values', 'get_data', '_validate_connection', '__init_variables'], 'metadata': {'repo': 'bicarlsen/easy-biologic', 'repo_url': 'https://github.com/bicarlsen/easy-biologic', 'review_status': 'pending_review', 'review_notes': ['尚未完成人工仪器级复核。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def init(self, **kwargs):
        return self.call('__init__', kwargs=kwargs)

    def delete_(self, **kwargs):
        return self.call('__del__', kwargs=kwargs)

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

    def validate_connection(self, **kwargs):
        return self.call('_validate_connection', kwargs=kwargs)

    def init_variables(self, **kwargs):
        return self.call('__init_variables', kwargs=kwargs)

