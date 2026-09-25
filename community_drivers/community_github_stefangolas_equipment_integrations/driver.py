from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubStefangolasEquipmentIntegrations(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/stefangolas_Equipment_Integrations', 'source_file': 'shaker.py', 'class_name': 'PyShaker', 'import_roots': [], 'candidate_methods': ['start', 'stop', 'get_speed'], 'metadata': {'repo': 'stefangolas/equipment_integrations', 'repo_url': 'https://github.com/stefangolas/Equipment_Integrations', 'unit_id': 'gh_biotek_elx405', 'source_file': 'shaker.py', 'candidate_score': 67, 'manufacturer': 'BioTek', 'model_name': 'BioTek ELx405'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def get_speed(self, **kwargs):
        return self.call('get_speed', kwargs=kwargs)

