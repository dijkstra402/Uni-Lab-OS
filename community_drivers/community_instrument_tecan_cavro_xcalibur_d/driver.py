from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTecanCavroXcaliburD(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/benpruitt__tecancavro', 'source_file': 'tecancavro/models.py', 'class_name': 'XCaliburD', 'import_roots': [], 'candidate_methods': ['initDebugLogging', 'logCall', 'logDebug', 'init', 'extractToWaste', 'primePort', 'executeChain', 'resetChain', 'updateSimState', 'cacheSimSpeeds', 'restoreSimSpeeds', 'execWrap', 'dispenseToWaste', 'extract', 'dispense', 'changePort', 'movePlungerAbs', 'movePlungerRel', 'setSpeed', 'setStartSpeed', 'setTopSpeed', 'setCutoffSpeed', 'setSlope', 'repeatCmdSeq', 'markRepeatStart', 'delayExec', 'haltExec', 'updateSpeeds', 'getPlungerPos', 'getStartSpeed', 'getTopSpeed', 'getCutoffSpeed', 'getEncoderPos', 'getCurPort', 'getBufferStatus', 'setMicrostep', 'terminateCmd', 'waitReady', 'sendRcv'], 'action_targets': {}, 'metadata': {'repo': 'benpruitt/tecancavro', 'repo_url': 'https://github.com/benpruitt/tecancavro', 'brand': 'Tecan Cavro', 'model': 'XCalibur D', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': '泵阀/液体处理', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 378, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def initDebugLogging(self, **kwargs):
        return self.call('initDebugLogging', kwargs=kwargs)

    def logCall(self, **kwargs):
        return self.call('logCall', kwargs=kwargs)

    def logDebug(self, **kwargs):
        return self.call('logDebug', kwargs=kwargs)

    def init(self, **kwargs):
        return self.call('init', kwargs=kwargs)

    def extractToWaste(self, **kwargs):
        return self.call('extractToWaste', kwargs=kwargs)

    def primePort(self, **kwargs):
        return self.call('primePort', kwargs=kwargs)

    def executeChain(self, **kwargs):
        return self.call('executeChain', kwargs=kwargs)

    def resetChain(self, **kwargs):
        return self.call('resetChain', kwargs=kwargs)

    def updateSimState(self, **kwargs):
        return self.call('updateSimState', kwargs=kwargs)

    def cacheSimSpeeds(self, **kwargs):
        return self.call('cacheSimSpeeds', kwargs=kwargs)

    def restoreSimSpeeds(self, **kwargs):
        return self.call('restoreSimSpeeds', kwargs=kwargs)

    def execWrap(self, **kwargs):
        return self.call('execWrap', kwargs=kwargs)

    def dispenseToWaste(self, **kwargs):
        return self.call('dispenseToWaste', kwargs=kwargs)

    def extract(self, **kwargs):
        return self.call('extract', kwargs=kwargs)

    def dispense(self, **kwargs):
        return self.call('dispense', kwargs=kwargs)

    def changePort(self, **kwargs):
        return self.call('changePort', kwargs=kwargs)

    def movePlungerAbs(self, **kwargs):
        return self.call('movePlungerAbs', kwargs=kwargs)

    def movePlungerRel(self, **kwargs):
        return self.call('movePlungerRel', kwargs=kwargs)

    def setSpeed(self, **kwargs):
        return self.call('setSpeed', kwargs=kwargs)

    def setStartSpeed(self, **kwargs):
        return self.call('setStartSpeed', kwargs=kwargs)

    def setTopSpeed(self, **kwargs):
        return self.call('setTopSpeed', kwargs=kwargs)

    def setCutoffSpeed(self, **kwargs):
        return self.call('setCutoffSpeed', kwargs=kwargs)

    def setSlope(self, **kwargs):
        return self.call('setSlope', kwargs=kwargs)

    def repeatCmdSeq(self, **kwargs):
        return self.call('repeatCmdSeq', kwargs=kwargs)

    def markRepeatStart(self, **kwargs):
        return self.call('markRepeatStart', kwargs=kwargs)

    def delayExec(self, **kwargs):
        return self.call('delayExec', kwargs=kwargs)

    def haltExec(self, **kwargs):
        return self.call('haltExec', kwargs=kwargs)

    def updateSpeeds(self, **kwargs):
        return self.call('updateSpeeds', kwargs=kwargs)

    def getPlungerPos(self, **kwargs):
        return self.call('getPlungerPos', kwargs=kwargs)

    def getStartSpeed(self, **kwargs):
        return self.call('getStartSpeed', kwargs=kwargs)

    def getTopSpeed(self, **kwargs):
        return self.call('getTopSpeed', kwargs=kwargs)

    def getCutoffSpeed(self, **kwargs):
        return self.call('getCutoffSpeed', kwargs=kwargs)

    def getEncoderPos(self, **kwargs):
        return self.call('getEncoderPos', kwargs=kwargs)

    def getCurPort(self, **kwargs):
        return self.call('getCurPort', kwargs=kwargs)

    def getBufferStatus(self, **kwargs):
        return self.call('getBufferStatus', kwargs=kwargs)

    def setMicrostep(self, **kwargs):
        return self.call('setMicrostep', kwargs=kwargs)

    def terminateCmd(self, **kwargs):
        return self.call('terminateCmd', kwargs=kwargs)

    def waitReady(self, **kwargs):
        return self.call('waitReady', kwargs=kwargs)

    def sendRcv(self, **kwargs):
        return self.call('sendRcv', kwargs=kwargs)

