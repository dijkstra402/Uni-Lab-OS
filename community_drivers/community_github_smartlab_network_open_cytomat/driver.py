from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubSmartlabNetworkOpenCytomat(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/smartlab-network_open-cytomat', 'source_file': 'src/cytomat/serial_port.py', 'class_name': 'SerialPort', 'import_roots': [], 'candidate_methods': ['close', 'open', 'issue_action_command', 'issue_status_command'], 'metadata': {'repo': 'smartlab-network/open-cytomat', 'repo_url': 'https://github.com/smartlab-network/open-cytomat', 'unit_id': 'gh_thermo_fisher_cytomat_2c', 'source_file': 'src/cytomat/serial_port.py', 'candidate_score': 122, 'manufacturer': 'Thermo Fisher', 'model_name': 'Thermo Fisher Cytomat 2C/6001'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def issue_action_command(self, **kwargs):
        return self.call('issue_action_command', kwargs=kwargs)

    def issue_status_command(self, **kwargs):
        return self.call('issue_status_command', kwargs=kwargs)

