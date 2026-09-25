from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingDgrettonPyhamilton(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/dgretton__pyhamilton', 'source_file': 'pyhamilton/interface.py', 'class_name': 'HamiltonInterface', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'dgretton/pyhamilton', 'repo_url': 'https://github.com/dgretton/pyhamilton', 'review_status': 'broken', 'review_notes': ['动作列表混入大量内部日志/解析方法。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


