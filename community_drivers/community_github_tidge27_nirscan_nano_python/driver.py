from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubTidge27NirscanNanoPython(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/tidge27_NIRScan_Nano_Python', 'source_file': 'scan.py', 'class_name': 'Spectrometer', 'import_roots': [], 'candidate_methods': ['reconnect_device', 'write_command', 'read_command', 'perform_scan', 'get_file', 'check_hibernate_flag'], 'metadata': {'repo': 'tidge27/nirscan_nano_python', 'repo_url': 'https://github.com/tidge27/NIRScan_Nano_Python', 'unit_id': 'gh_ti_dlp_nirscan_nano', 'source_file': 'scan.py', 'candidate_score': 71, 'manufacturer': 'TI', 'model_name': 'TI DLP NIRscan Nano'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def reconnect_device(self, **kwargs):
        return self.call('reconnect_device', kwargs=kwargs)

    def write_command(self, **kwargs):
        return self.call('write_command', kwargs=kwargs)

    def read_command(self, **kwargs):
        return self.call('read_command', kwargs=kwargs)

    def perform_scan(self, **kwargs):
        return self.call('perform_scan', kwargs=kwargs)

    def get_file(self, **kwargs):
        return self.call('get_file', kwargs=kwargs)

    def check_hibernate_flag(self, **kwargs):
        return self.call('check_hibernate_flag', kwargs=kwargs)

