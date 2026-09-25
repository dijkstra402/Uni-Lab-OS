from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubBowmanlabPlateReader(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/bowmanlab_plate_reader', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'bowmanlab/plate_reader', 'repo_url': 'https://github.com/bowmanlab/plate_reader', 'unit_id': 'gh_biotek_synergy_h1m', 'source_file': '', 'candidate_score': 0, 'manufacturer': 'BioTek', 'model_name': 'BioTek Synergy H1M'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


