from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubFuziktPsdMvpControl(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/fuzikt_psd_mvp_control', 'source_file': 'hw_classes/serial_com.py', 'class_name': 'Serial_communication', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'send_command'], 'metadata': {'repo': 'fuzikt/psd_mvp_control', 'repo_url': 'https://github.com/fuzikt/psd_mvp_control', 'unit_id': 'gh_hamilton_psd', 'source_file': 'hw_classes/serial_com.py', 'candidate_score': 127, 'manufacturer': 'Hamilton', 'model_name': 'Hamilton PSD/4'}}

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

