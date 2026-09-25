from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubDirkensteinPygcms(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/dirkenstein_pygcms', 'source_file': 'pygcms/device/busreader.py', 'class_name': 'BusReader', 'import_roots': [], 'candidate_methods': ['getGbpibAddr', 'statusb', 'getStb', 'loadSmartCard', 'cmd', 'getdevices', 'controller', 'deviceByName', 'isSmartCardDevice', 'needsLoading'], 'metadata': {'repo': 'dirkenstein/pygcms', 'repo_url': 'https://github.com/dirkenstein/pygcms', 'unit_id': 'gh_hp_5890_gc__5971', 'source_file': 'pygcms/device/busreader.py', 'candidate_score': 112, 'manufacturer': 'HP/Agilent', 'model_name': 'HP/Agilent 5890 GC + 5971/5972 MSD'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def getGbpibAddr(self, **kwargs):
        return self.call('getGbpibAddr', kwargs=kwargs)

    def statusb(self, **kwargs):
        return self.call('statusb', kwargs=kwargs)

    def getStb(self, **kwargs):
        return self.call('getStb', kwargs=kwargs)

    def loadSmartCard(self, **kwargs):
        return self.call('loadSmartCard', kwargs=kwargs)

    def cmd(self, **kwargs):
        return self.call('cmd', kwargs=kwargs)

    def getdevices(self, **kwargs):
        return self.call('getdevices', kwargs=kwargs)

    def controller(self, **kwargs):
        return self.call('controller', kwargs=kwargs)

    def deviceByName(self, **kwargs):
        return self.call('deviceByName', kwargs=kwargs)

    def isSmartCardDevice(self, **kwargs):
        return self.call('isSmartCardDevice', kwargs=kwargs)

    def needsLoading(self, **kwargs):
        return self.call('needsLoading', kwargs=kwargs)

