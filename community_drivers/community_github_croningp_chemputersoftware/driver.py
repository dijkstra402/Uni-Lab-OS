from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubCroningpChemputersoftware(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/croningp_ChemputerSoftware', 'source_file': 'platform_server/modules/serial_labware/SerialDevice/serial_labware.py', 'class_name': 'SerialDevice', 'import_roots': [], 'candidate_methods': ['launch_command_handler', 'open_connection', 'close_connection', 'send_message', 'non_blocking_wait', 'keepalive'], 'metadata': {'repo': 'croningp/chemputersoftware', 'repo_url': 'https://github.com/croningp/ChemputerSoftware', 'unit_id': 'gh_heidolph_mr_hei_connect', 'source_file': 'platform_server/modules/serial_labware/SerialDevice/serial_labware.py', 'candidate_score': 129, 'manufacturer': 'Heidolph', 'model_name': 'Heidolph MR Hei-Connect'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def launch_command_handler(self, **kwargs):
        return self.call('launch_command_handler', kwargs=kwargs)

    def open_connection(self, **kwargs):
        return self.call('open_connection', kwargs=kwargs)

    def close_connection(self, **kwargs):
        return self.call('close_connection', kwargs=kwargs)

    def send_message(self, **kwargs):
        return self.call('send_message', kwargs=kwargs)

    def non_blocking_wait(self, **kwargs):
        return self.call('non_blocking_wait', kwargs=kwargs)

    def keepalive(self, **kwargs):
        return self.call('keepalive', kwargs=kwargs)

