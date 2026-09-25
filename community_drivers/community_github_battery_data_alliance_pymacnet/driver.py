from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubBatteryDataAlliancePymacnet(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/battery-data-alliance_pymacnet', 'source_file': 'pymacnet/cycler_interface.py', 'class_name': 'CyclerInterface', 'import_roots': [], 'candidate_methods': ['get_num_channels', 'read_system_info', 'read_general_info', 'read_channel_status', 'read_all_channel_statuses'], 'metadata': {'repo': 'battery-data-alliance/pymacnet', 'repo_url': 'https://github.com/battery-data-alliance/pymacnet', 'unit_id': 'gh_maccor_macnet', 'source_file': 'pymacnet/cycler_interface.py', 'candidate_score': 122, 'manufacturer': 'Maccor', 'model_name': 'Maccor MacNet兼容系列'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def get_num_channels(self, **kwargs):
        return self.call('get_num_channels', kwargs=kwargs)

    def read_system_info(self, **kwargs):
        return self.call('read_system_info', kwargs=kwargs)

    def read_general_info(self, **kwargs):
        return self.call('read_general_info', kwargs=kwargs)

    def read_channel_status(self, **kwargs):
        return self.call('read_channel_status', kwargs=kwargs)

    def read_all_channel_statuses(self, **kwargs):
        return self.call('read_all_channel_statuses', kwargs=kwargs)

