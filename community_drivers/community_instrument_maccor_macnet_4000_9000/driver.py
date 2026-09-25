from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMaccorMacnet40009000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/battery-data-alliance__pymacnet', 'source_file': 'pymacnet/channel_interface.py', 'class_name': 'ChannelInterface', 'import_roots': [], 'candidate_methods': ['get_channel_number', 'read_channel_status', 'read_aux', 'reset_channel', 'set_channel_variable', 'start_test_with_procedure', 'start_test_with_direct_control', 'set_direct_mode_output', 'get_num_channels', 'read_system_info', 'read_general_info', 'read_all_channel_statuses'], 'action_targets': {}, 'metadata': {'repo': 'battery-data-alliance/pymacnet', 'repo_url': 'https://github.com/battery-data-alliance/pymacnet', 'brand': 'Maccor', 'model': 'MacNet 4000/9000', 'device_type_cn': '电池测试柜', 'device_type_en': 'Battery Test Cabinet', 'source_framework': '专用驱动', 'tag_id': '4427', 'tag_name': '电池测试柜', 'tag_name_en': 'Battery Test Cabinet', 'candidate_score': 110, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_channel_number(self, **kwargs):
        return self.call('get_channel_number', kwargs=kwargs)

    def read_channel_status(self, **kwargs):
        return self.call('read_channel_status', kwargs=kwargs)

    def read_aux(self, **kwargs):
        return self.call('read_aux', kwargs=kwargs)

    def reset_channel(self, **kwargs):
        return self.call('reset_channel', kwargs=kwargs)

    def set_channel_variable(self, **kwargs):
        return self.call('set_channel_variable', kwargs=kwargs)

    def start_test_with_procedure(self, **kwargs):
        return self.call('start_test_with_procedure', kwargs=kwargs)

    def start_test_with_direct_control(self, **kwargs):
        return self.call('start_test_with_direct_control', kwargs=kwargs)

    def set_direct_mode_output(self, **kwargs):
        return self.call('set_direct_mode_output', kwargs=kwargs)

    def get_num_channels(self, **kwargs):
        return self.call('get_num_channels', kwargs=kwargs)

    def read_system_info(self, **kwargs):
        return self.call('read_system_info', kwargs=kwargs)

    def read_general_info(self, **kwargs):
        return self.call('read_general_info', kwargs=kwargs)

    def read_all_channel_statuses(self, **kwargs):
        return self.call('read_all_channel_statuses', kwargs=kwargs)

