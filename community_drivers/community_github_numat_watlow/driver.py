from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubNumatWatlow(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/numat_watlow', 'source_file': 'watlow/driver.py', 'class_name': 'TemperatureController', 'import_roots': [], 'candidate_methods': ['open', 'close', 'get', 'set'], 'metadata': {'repo': 'numat/watlow', 'repo_url': 'https://github.com/numat/watlow', 'unit_id': 'gh_watlow_ez_zone_pm', 'source_file': 'watlow/driver.py', 'candidate_score': 142, 'manufacturer': 'Watlow', 'model_name': 'Watlow EZ-Zone PM'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def set(self, **kwargs):
        return self.call('set', kwargs=kwargs)

