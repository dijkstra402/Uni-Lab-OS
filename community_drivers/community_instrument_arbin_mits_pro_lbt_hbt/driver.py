from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentArbinMitsProLbtHbt(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/battery-data-alliance__pyctiarbin', 'source_file': 'pyctiarbin/channel_interface.py', 'class_name': 'ChannelInterface', 'import_roots': [], 'candidate_methods': ['read_channel_status', 'assign_schedule', 'start_test', 'stop_test', 'set_meta_variable', 'get_num_channels', 'get_login_feedback'], 'action_targets': {}, 'metadata': {'repo': 'battery-data-alliance/pyctiarbin', 'repo_url': 'https://github.com/battery-data-alliance/pyctiarbin', 'brand': 'Arbin', 'model': 'MITS Pro LBT/HBT', 'device_type_cn': '电池测试柜', 'device_type_en': 'Battery Test Cabinet', 'source_framework': '专用驱动', 'tag_id': '4427', 'tag_name': '电池测试柜', 'tag_name_en': 'Battery Test Cabinet', 'candidate_score': 86, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def read_channel_status(self, **kwargs):
        return self.call('read_channel_status', kwargs=kwargs)

    def assign_schedule(self, **kwargs):
        return self.call('assign_schedule', kwargs=kwargs)

    def start_test(self, **kwargs):
        return self.call('start_test', kwargs=kwargs)

    def stop_test(self, **kwargs):
        return self.call('stop_test', kwargs=kwargs)

    def set_meta_variable(self, **kwargs):
        return self.call('set_meta_variable', kwargs=kwargs)

    def get_num_channels(self, **kwargs):
        return self.call('get_num_channels', kwargs=kwargs)

    def get_login_feedback(self, **kwargs):
        return self.call('get_login_feedback', kwargs=kwargs)

