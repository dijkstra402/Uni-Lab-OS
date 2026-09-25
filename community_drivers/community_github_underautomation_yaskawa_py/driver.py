from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubUnderautomationYaskawaPy(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/underautomation_Yaskawa.py', 'source_file': 'underautomation/yaskawa/yaskawa_robot.py', 'class_name': 'YaskawaRobot', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'register_license', 'connected', 'high_speed_e_server', 'license_info'], 'metadata': {'repo': 'underautomation/yaskawa.py', 'repo_url': 'https://github.com/underautomation/Yaskawa.py', 'unit_id': 'gh_yaskawa_motoman_yrc1000', 'source_file': 'underautomation/yaskawa/yaskawa_robot.py', 'candidate_score': 48, 'manufacturer': 'Yaskawa', 'model_name': 'Yaskawa Motoman YRC1000'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def register_license(self, **kwargs):
        return self.call('register_license', kwargs=kwargs)

    def connected(self, **kwargs):
        return self.call('connected', kwargs=kwargs)

    def high_speed_e_server(self, **kwargs):
        return self.call('high_speed_e_server', kwargs=kwargs)

    def license_info(self, **kwargs):
        return self.call('license_info', kwargs=kwargs)

