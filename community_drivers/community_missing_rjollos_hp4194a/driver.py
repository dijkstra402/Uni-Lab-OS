from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingRjollosHp4194a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/rjollos__hp4194a', 'source_file': 'hp4194a.py', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'rjollos/hp4194a', 'repo_url': 'https://github.com/rjollos/hp4194a', 'review_status': 'broken', 'review_notes': ['当前识别到的是 CLI 脚本函数，不是仪器接口。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


