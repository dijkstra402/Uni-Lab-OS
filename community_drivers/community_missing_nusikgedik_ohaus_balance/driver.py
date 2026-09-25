from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingNusikgedikOhausBalance(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/nusikgedik__ohaus-balance', 'source_file': 'ohaus.py', 'class_name': 'Balance', 'import_roots': [], 'candidate_methods': ['__init__', 'write_utf8_with_nr', 'on', 'off', 'set_unit', 'tare', 'zero', 'read_weigh', 'open_door', 'close_doors'], 'metadata': {'repo': 'nusikgedik/ohaus-balance', 'repo_url': 'https://github.com/nusikgedik/ohaus-balance', 'review_status': 'good', 'review_notes': ['天平核心动作清晰。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def init(self, **kwargs):
        return self.call('__init__', kwargs=kwargs)

    def write_utf8_with_nr(self, **kwargs):
        return self.call('write_utf8_with_nr', kwargs=kwargs)

    def on(self, **kwargs):
        return self.call('on', kwargs=kwargs)

    def off(self, **kwargs):
        return self.call('off', kwargs=kwargs)

    def set_unit(self, **kwargs):
        return self.call('set_unit', kwargs=kwargs)

    def tare(self, **kwargs):
        return self.call('tare', kwargs=kwargs)

    def zero(self, **kwargs):
        return self.call('zero', kwargs=kwargs)

    def read_weigh(self, **kwargs):
        return self.call('read_weigh', kwargs=kwargs)

    def open_door(self, **kwargs):
        return self.call('open_door', kwargs=kwargs)

    def close_doors(self, **kwargs):
        return self.call('close_doors', kwargs=kwargs)

