from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubWyssMasterflex(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Wyss_masterflex', 'source_file': 'masterflex/masterflex.py', 'class_name': 'MasterflexSerial', 'import_roots': [], 'candidate_methods': ['findSerialPumps', 'requestAuxiliaryInputStatus', 'controlAuxiliaryOutputsOnG', 'requestCumulative', 'requestToGo', 'go', 'goContinuous', 'halt', 'requestStatus', 'requestFrontPanelSwitch', 'enableLocal', 'controlAuxiliaryOutputs', 'enableRemote', 'requestMotorSpeed', 'setMotorSpeed', 'renumber', 'setRevolutions', 'zeroToGo', 'zeroCumulative', 'cancel'], 'metadata': {'repo': 'wyss/masterflex', 'repo_url': 'https://github.com/Wyss/masterflex', 'unit_id': 'gh_masterflex_cole_parmer_l', 'source_file': 'masterflex/masterflex.py', 'candidate_score': 97, 'manufacturer': 'Masterflex (Cole-Parmer)', 'model_name': 'Masterflex (Cole-Parmer) L/S 07523系列'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def findSerialPumps(self, **kwargs):
        return self.call('findSerialPumps', kwargs=kwargs)

    def requestAuxiliaryInputStatus(self, **kwargs):
        return self.call('requestAuxiliaryInputStatus', kwargs=kwargs)

    def controlAuxiliaryOutputsOnG(self, **kwargs):
        return self.call('controlAuxiliaryOutputsOnG', kwargs=kwargs)

    def requestCumulative(self, **kwargs):
        return self.call('requestCumulative', kwargs=kwargs)

    def requestToGo(self, **kwargs):
        return self.call('requestToGo', kwargs=kwargs)

    def go(self, **kwargs):
        return self.call('go', kwargs=kwargs)

    def goContinuous(self, **kwargs):
        return self.call('goContinuous', kwargs=kwargs)

    def halt(self, **kwargs):
        return self.call('halt', kwargs=kwargs)

    def requestStatus(self, **kwargs):
        return self.call('requestStatus', kwargs=kwargs)

    def requestFrontPanelSwitch(self, **kwargs):
        return self.call('requestFrontPanelSwitch', kwargs=kwargs)

    def enableLocal(self, **kwargs):
        return self.call('enableLocal', kwargs=kwargs)

    def controlAuxiliaryOutputs(self, **kwargs):
        return self.call('controlAuxiliaryOutputs', kwargs=kwargs)

    def enableRemote(self, **kwargs):
        return self.call('enableRemote', kwargs=kwargs)

    def requestMotorSpeed(self, **kwargs):
        return self.call('requestMotorSpeed', kwargs=kwargs)

    def setMotorSpeed(self, **kwargs):
        return self.call('setMotorSpeed', kwargs=kwargs)

    def renumber(self, **kwargs):
        return self.call('renumber', kwargs=kwargs)

    def setRevolutions(self, **kwargs):
        return self.call('setRevolutions', kwargs=kwargs)

    def zeroToGo(self, **kwargs):
        return self.call('zeroToGo', kwargs=kwargs)

    def zeroCumulative(self, **kwargs):
        return self.call('zeroCumulative', kwargs=kwargs)

    def cancel(self, **kwargs):
        return self.call('cancel', kwargs=kwargs)

