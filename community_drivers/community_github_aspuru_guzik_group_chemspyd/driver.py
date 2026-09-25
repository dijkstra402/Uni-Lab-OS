from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAspuruGuzikGroupChemspyd(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/aspuru-guzik-group_chemspyd', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'aspuru-guzik-group/chemspyd', 'repo_url': 'https://github.com/aspuru-guzik-group/chemspyd', 'unit_id': 'gh_chemspeed_flex', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'Chemspeed', 'model_name': 'Chemspeed FLEX/iSynth'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


