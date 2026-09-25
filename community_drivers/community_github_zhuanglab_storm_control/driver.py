from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubZhuanglabStormControl(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/ZhuangLab_storm-control', 'source_file': 'storm_control/fluidics/pumps/rainin_rp1.py', 'class_name': 'APump', 'import_roots': [], 'candidate_methods': ['connectPump', 'disconnectPump', 'close', 'enableRemoteControl', 'getPumpIdentification', 'getStatus', 'readDisplay', 'requestStatus', 'sendBufferedCommand', 'sendImmediateCommand', 'setFlowDirection', 'setSpeed', 'startFlow', 'stopFlow', 'write', 'read'], 'metadata': {'repo': 'zhuanglab/storm-control', 'repo_url': 'https://github.com/ZhuangLab/storm-control', 'unit_id': 'gh_hamamatsu_orca_flash_4_0', 'source_file': 'storm_control/fluidics/pumps/rainin_rp1.py', 'candidate_score': 137, 'manufacturer': 'Hamamatsu', 'model_name': 'Hamamatsu ORCA Flash 4.0'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def connectPump(self, **kwargs):
        return self.call('connectPump', kwargs=kwargs)

    def disconnectPump(self, **kwargs):
        return self.call('disconnectPump', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def enableRemoteControl(self, **kwargs):
        return self.call('enableRemoteControl', kwargs=kwargs)

    def getPumpIdentification(self, **kwargs):
        return self.call('getPumpIdentification', kwargs=kwargs)

    def getStatus(self, **kwargs):
        return self.call('getStatus', kwargs=kwargs)

    def readDisplay(self, **kwargs):
        return self.call('readDisplay', kwargs=kwargs)

    def requestStatus(self, **kwargs):
        return self.call('requestStatus', kwargs=kwargs)

    def sendBufferedCommand(self, **kwargs):
        return self.call('sendBufferedCommand', kwargs=kwargs)

    def sendImmediateCommand(self, **kwargs):
        return self.call('sendImmediateCommand', kwargs=kwargs)

    def setFlowDirection(self, **kwargs):
        return self.call('setFlowDirection', kwargs=kwargs)

    def setSpeed(self, **kwargs):
        return self.call('setSpeed', kwargs=kwargs)

    def startFlow(self, **kwargs):
        return self.call('startFlow', kwargs=kwargs)

    def stopFlow(self, **kwargs):
        return self.call('stopFlow', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

