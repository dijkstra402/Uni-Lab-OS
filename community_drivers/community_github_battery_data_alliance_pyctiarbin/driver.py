from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubBatteryDataAlliancePyctiarbin(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/battery-data-alliance_pyctiarbin', 'source_file': 'pyctiarbin/cycler_interface.py', 'class_name': 'CyclerInterface', 'import_roots': [], 'candidate_methods': ['get_num_channels', 'get_login_feedback', 'read_channel_status'], 'metadata': {'repo': 'battery-data-alliance/pyctiarbin', 'repo_url': 'https://github.com/battery-data-alliance/pyctiarbin', 'unit_id': 'gh_arbin_mits_pro', 'source_file': 'pyctiarbin/cycler_interface.py', 'candidate_score': 112, 'manufacturer': 'Arbin', 'model_name': 'Arbin MITS Pro系列'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def get_num_channels(self, **kwargs):
        return self.call('get_num_channels', kwargs=kwargs)

    def get_login_feedback(self, **kwargs):
        return self.call('get_login_feedback', kwargs=kwargs)

    def read_channel_status(self, **kwargs):
        return self.call('read_channel_status', kwargs=kwargs)

