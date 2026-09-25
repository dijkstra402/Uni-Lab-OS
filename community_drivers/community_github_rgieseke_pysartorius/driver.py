from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubRgiesekePysartorius(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/rgieseke_pySartorius', 'source_file': 'sartorius.py', 'class_name': 'Sartorius', 'import_roots': [], 'candidate_methods': ['value', 'display_unit', 'tara_zero', 'tara', 'zero'], 'metadata': {'repo': 'rgieseke/pysartorius', 'repo_url': 'https://github.com/rgieseke/pySartorius', 'unit_id': 'gh_sartorius_ea', 'source_file': 'sartorius.py', 'candidate_score': 66, 'manufacturer': 'Sartorius', 'model_name': 'Sartorius EA/EB/GD/GE/TE系列'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def value(self, **kwargs):
        return self.call('value', kwargs=kwargs)

    def display_unit(self, **kwargs):
        return self.call('display_unit', kwargs=kwargs)

    def tara_zero(self, **kwargs):
        return self.call('tara_zero', kwargs=kwargs)

    def tara(self, **kwargs):
        return self.call('tara', kwargs=kwargs)

    def zero(self, **kwargs):
        return self.call('zero', kwargs=kwargs)

