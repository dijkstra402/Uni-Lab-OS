from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingTomwphillipsPumpy(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/tomwphillips__pumpy', 'source_file': 'pumpy.py', 'class_name': 'Pump', 'import_roots': [], 'candidate_methods': ['__init__', '__repr__', 'write', 'read', 'setdiameter', 'setflowrate', 'infuse', 'withdraw', 'stop', 'settargetvolume', 'waituntiltarget'], 'metadata': {'repo': 'tomwphillips/pumpy', 'repo_url': 'https://github.com/tomwphillips/pumpy', 'review_status': 'good', 'review_notes': ['泵送动作完整。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def init(self, **kwargs):
        return self.call('__init__', kwargs=kwargs)

    def repr(self, **kwargs):
        return self.call('__repr__', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def setdiameter(self, **kwargs):
        return self.call('setdiameter', kwargs=kwargs)

    def setflowrate(self, **kwargs):
        return self.call('setflowrate', kwargs=kwargs)

    def infuse(self, **kwargs):
        return self.call('infuse', kwargs=kwargs)

    def withdraw(self, **kwargs):
        return self.call('withdraw', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def settargetvolume(self, **kwargs):
        return self.call('settargetvolume', kwargs=kwargs)

    def waituntiltarget(self, **kwargs):
        return self.call('waituntiltarget', kwargs=kwargs)

