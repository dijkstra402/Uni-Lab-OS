from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAnuwragOpentronsTools(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/anuwrag_Opentrons-Tools', 'source_file': 'Run-Module-from-Computer/temp_driver.py', 'class_name': 'TempDeckDriver', 'import_roots': [], 'candidate_methods': ['create', 'connect', 'disconnect', 'is_connected', 'deactivate', 'set_temperature', 'get_temperature', 'get_device_info', 'enter_programming_mode'], 'metadata': {'repo': 'anuwrag/opentrons-tools', 'repo_url': 'https://github.com/anuwrag/Opentrons-Tools', 'unit_id': 'gh_opentrons_heater_shaker_module', 'source_file': 'Run-Module-from-Computer/temp_driver.py', 'candidate_score': 74, 'manufacturer': 'Opentrons', 'model_name': 'Opentrons Heater-Shaker Module'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def create(self, **kwargs):
        return self.call('create', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def is_connected(self, **kwargs):
        return self.call('is_connected', kwargs=kwargs)

    def deactivate(self, **kwargs):
        return self.call('deactivate', kwargs=kwargs)

    def set_temperature(self, **kwargs):
        return self.call('set_temperature', kwargs=kwargs)

    def get_temperature(self, **kwargs):
        return self.call('get_temperature', kwargs=kwargs)

    def get_device_info(self, **kwargs):
        return self.call('get_device_info', kwargs=kwargs)

    def enter_programming_mode(self, **kwargs):
        return self.call('enter_programming_mode', kwargs=kwargs)

