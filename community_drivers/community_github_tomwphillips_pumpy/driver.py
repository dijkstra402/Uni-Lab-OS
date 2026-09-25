from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubTomwphillipsPumpy(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/tomwphillips_pumpy', 'source_file': 'pumpy.py', 'class_name': 'Pump', 'import_roots': [], 'candidate_methods': ['write', 'read', 'setdiameter', 'setflowrate', 'infuse', 'withdraw', 'stop', 'settargetvolume', 'waituntiltarget'], 'metadata': {'repo': 'tomwphillips/pumpy', 'repo_url': 'https://github.com/tomwphillips/pumpy', 'unit_id': 'gh_harvard_apparatus_pump_11', 'source_file': 'pumpy.py', 'candidate_score': 93, 'manufacturer': 'Harvard Apparatus', 'model_name': 'Harvard Apparatus Pump 11 / PHD 2000'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


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

