from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubLeokogosHp4284aLcrMeterDriver(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/leokogos_hp-4284A-LCR-meter-driver', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'leokogos/hp-4284a-lcr-meter-driver', 'repo_url': 'https://github.com/leokogos/hp-4284A-LCR-meter-driver', 'unit_id': 'gh_hp_4284a', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'HP', 'model_name': 'HP 4284A'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


