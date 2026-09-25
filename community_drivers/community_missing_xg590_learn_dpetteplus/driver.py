from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingXg590LearnDpetteplus(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/xg590__Learn_dPettePlus', 'source_file': 'dPettePlus.py', 'class_name': 'DPETTE', 'import_roots': [], 'candidate_methods': ['__init__', 'send', 'receive', 'hello', 'get_pipette_info', 'set_mode', 'set_speed', 'set_pipette_volume', 'action'], 'metadata': {'repo': 'xg590/Learn_dPettePlus', 'repo_url': 'https://github.com/xg590/Learn_dPettePlus', 'review_status': 'good', 'review_notes': ['电子移液核心动作准确。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def init(self, **kwargs):
        return self.call('__init__', kwargs=kwargs)

    def send(self, **kwargs):
        return self.call('send', kwargs=kwargs)

    def receive(self, **kwargs):
        return self.call('receive', kwargs=kwargs)

    def hello(self, **kwargs):
        return self.call('hello', kwargs=kwargs)

    def get_pipette_info(self, **kwargs):
        return self.call('get_pipette_info', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

    def set_pipette_volume(self, **kwargs):
        return self.call('set_pipette_volume', kwargs=kwargs)

    def action(self, **kwargs):
        return self.call('action', kwargs=kwargs)

