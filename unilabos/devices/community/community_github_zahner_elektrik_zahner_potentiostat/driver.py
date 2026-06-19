from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubZahnerElektrikZahnerPotentiostat(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Zahner-elektrik_zahner_potentiostat', 'source_file': 'zahner_potentiostat/scpi_control/control.py', 'class_name': 'SCPIDevice', 'import_roots': [], 'candidate_methods': ['close', 'getDataReceiver', 'setRaiseOnErrorEnabled', 'getRaiseOnErrorEnabled', 'IDN', 'readDeviceInformations', 'clearState', 'readState', 'checkResetStatus', 'resetCommand', 'abortCommand', 'calibrateOffsets', 'switchToEPCControl', 'switchToEPCControlWithoutPotentiostatStateChange', 'setLineFrequency', 'getLineFrequency', 'setDateTime', 'getDateTime', 'getDateTimeStruct', 'getSoftwareInfo'], 'metadata': {'repo': 'zahner-elektrik/zahner_potentiostat', 'repo_url': 'https://github.com/Zahner-elektrik/zahner_potentiostat', 'unit_id': 'gh_zahner_pp212', 'source_file': 'zahner_potentiostat/scpi_control/control.py', 'candidate_score': 129, 'manufacturer': 'Zahner', 'model_name': 'Zahner PP212/PP222/PP242'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def getDataReceiver(self, **kwargs):
        return self.call('getDataReceiver', kwargs=kwargs)

    def setRaiseOnErrorEnabled(self, **kwargs):
        return self.call('setRaiseOnErrorEnabled', kwargs=kwargs)

    def getRaiseOnErrorEnabled(self, **kwargs):
        return self.call('getRaiseOnErrorEnabled', kwargs=kwargs)

    def IDN(self, **kwargs):
        return self.call('IDN', kwargs=kwargs)

    def readDeviceInformations(self, **kwargs):
        return self.call('readDeviceInformations', kwargs=kwargs)

    def clearState(self, **kwargs):
        return self.call('clearState', kwargs=kwargs)

    def readState(self, **kwargs):
        return self.call('readState', kwargs=kwargs)

    def checkResetStatus(self, **kwargs):
        return self.call('checkResetStatus', kwargs=kwargs)

    def resetCommand(self, **kwargs):
        return self.call('resetCommand', kwargs=kwargs)

    def abortCommand(self, **kwargs):
        return self.call('abortCommand', kwargs=kwargs)

    def calibrateOffsets(self, **kwargs):
        return self.call('calibrateOffsets', kwargs=kwargs)

    def switchToEPCControl(self, **kwargs):
        return self.call('switchToEPCControl', kwargs=kwargs)

    def switchToEPCControlWithoutPotentiostatStateChange(self, **kwargs):
        return self.call('switchToEPCControlWithoutPotentiostatStateChange', kwargs=kwargs)

    def setLineFrequency(self, **kwargs):
        return self.call('setLineFrequency', kwargs=kwargs)

    def getLineFrequency(self, **kwargs):
        return self.call('getLineFrequency', kwargs=kwargs)

    def setDateTime(self, **kwargs):
        return self.call('setDateTime', kwargs=kwargs)

    def getDateTime(self, **kwargs):
        return self.call('getDateTime', kwargs=kwargs)

    def getDateTimeStruct(self, **kwargs):
        return self.call('getDateTimeStruct', kwargs=kwargs)

    def getSoftwareInfo(self, **kwargs):
        return self.call('getSoftwareInfo', kwargs=kwargs)

