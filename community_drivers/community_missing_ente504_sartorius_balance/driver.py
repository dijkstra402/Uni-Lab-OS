from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingEnte504SartoriusBalance(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/ente504__Sartorius_Balance', 'source_file': 't_publishData.py', 'class_name': 'MqttPublisher', 'import_roots': [], 'candidate_methods': [], 'metadata': {'repo': 'ente504/Sartorius_Balance', 'repo_url': 'https://github.com/ente504/Sartorius_Balance', 'review_status': 'broken', 'review_notes': ['当前识别到的是 MQTT 发布辅助代码，不是天平驱动。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


