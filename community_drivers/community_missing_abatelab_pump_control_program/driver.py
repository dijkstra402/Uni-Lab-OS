from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingAbatelabPumpControlProgram(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/AbateLab__Pump-Control-Program', 'source_file': 'pump_control.py', 'class_name': 'PumpControl', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'AbateLab/Pump-Control-Program', 'repo_url': 'https://github.com/AbateLab/Pump-Control-Program', 'review_status': 'broken', 'review_notes': ['当前入口混入 Qt GUI 代码；运行时仅完成纳管，不代表可驱动。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


