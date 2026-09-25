from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingCukelarterChemyxSyringePump(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/cukelarter__Chemyx-Syringe-Pump', 'source_file': 'python_dist/core/connect.py', 'class_name': 'Connection', 'import_roots': [], 'candidate_methods': ['__init__', 'openConnection', 'closeConnection', 'sendCommand', 'getResponse', 'startPump', 'stopPump', 'pausePump', 'restartPump', 'setUnits', 'setDiameter', 'setRate', 'setVolume', 'setDelay', 'setTime', 'getParameterLimits', 'getParameters', 'getDisplacedVolume', 'getElapsedTime', 'getPumpStatus', 'setPump', 'addPump'], 'metadata': {'repo': 'cukelarter/Chemyx-Syringe-Pump', 'repo_url': 'https://github.com/cukelarter/Chemyx-Syringe-Pump', 'review_status': 'good', 'review_notes': ['泵操作覆盖完整。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def init(self, **kwargs):
        return self.call('__init__', kwargs=kwargs)

    def openConnection(self, **kwargs):
        return self.call('openConnection', kwargs=kwargs)

    def closeConnection(self, **kwargs):
        return self.call('closeConnection', kwargs=kwargs)

    def sendCommand(self, **kwargs):
        return self.call('sendCommand', kwargs=kwargs)

    def getResponse(self, **kwargs):
        return self.call('getResponse', kwargs=kwargs)

    def startPump(self, **kwargs):
        return self.call('startPump', kwargs=kwargs)

    def stopPump(self, **kwargs):
        return self.call('stopPump', kwargs=kwargs)

    def pausePump(self, **kwargs):
        return self.call('pausePump', kwargs=kwargs)

    def restartPump(self, **kwargs):
        return self.call('restartPump', kwargs=kwargs)

    def setUnits(self, **kwargs):
        return self.call('setUnits', kwargs=kwargs)

    def setDiameter(self, **kwargs):
        return self.call('setDiameter', kwargs=kwargs)

    def setRate(self, **kwargs):
        return self.call('setRate', kwargs=kwargs)

    def setVolume(self, **kwargs):
        return self.call('setVolume', kwargs=kwargs)

    def setDelay(self, **kwargs):
        return self.call('setDelay', kwargs=kwargs)

    def setTime(self, **kwargs):
        return self.call('setTime', kwargs=kwargs)

    def getParameterLimits(self, **kwargs):
        return self.call('getParameterLimits', kwargs=kwargs)

    def getParameters(self, **kwargs):
        return self.call('getParameters', kwargs=kwargs)

    def getDisplacedVolume(self, **kwargs):
        return self.call('getDisplacedVolume', kwargs=kwargs)

    def getElapsedTime(self, **kwargs):
        return self.call('getElapsedTime', kwargs=kwargs)

    def getPumpStatus(self, **kwargs):
        return self.call('getPumpStatus', kwargs=kwargs)

    def setPump(self, **kwargs):
        return self.call('setPump', kwargs=kwargs)

    def addPump(self, **kwargs):
        return self.call('addPump', kwargs=kwargs)

