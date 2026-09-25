from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingMarcoestersDepositionIc6(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/marcoesters__deposition_ic6', 'source_file': '', 'class_name': '', 'import_roots': ['src'], 'candidate_methods': [], 'metadata': {'repo': 'marcoesters/deposition_ic6', 'repo_url': 'https://github.com/marcoesters/deposition_ic6', 'review_status': 'broken', 'review_notes': ['未识别到可用驱动入口。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


