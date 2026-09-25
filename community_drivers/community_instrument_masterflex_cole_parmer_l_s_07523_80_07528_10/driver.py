from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMasterflexColeParmerLS07523800752810(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Wyss__masterflex', 'source_file': 'masterflex/masterflex.py', 'class_name': 'MasterflexSerial', 'import_roots': [], 'candidate_methods': ['findSerialPumps', 'requestAuxiliaryInputStatus', 'controlAuxiliaryOutputsOnG', 'requestCumulative', 'requestToGo', 'go', 'goContinuous', 'halt', 'requestStatus', 'requestFrontPanelSwitch', 'enableLocal', 'controlAuxiliaryOutputs', 'enableRemote', 'requestMotorSpeed', 'setMotorSpeed', 'renumber', 'setRevolutions', 'zeroToGo', 'zeroCumulative', 'cancel', 'enquire'], 'action_targets': {}, 'metadata': {'repo': 'Wyss/masterflex', 'repo_url': 'https://github.com/Wyss/masterflex', 'brand': 'Masterflex (Cole-Parmer)', 'model': 'L/S 07523-80/07528-10', 'device_type_cn': '蠕动泵', 'device_type_en': 'Peristaltic Pump', 'source_framework': '泵阀/液体处理', 'tag_id': '4451', 'tag_name': '蠕动泵', 'tag_name_en': 'Peristaltic Pump', 'candidate_score': 218, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

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

    def enquire(self, **kwargs):
        return self.call('enquire', kwargs=kwargs)

