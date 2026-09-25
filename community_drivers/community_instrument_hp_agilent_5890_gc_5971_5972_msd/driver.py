from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHpAgilent5890Gc59715972Msd(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/dirkenstein__pygcms', 'source_file': 'pygcms/device/hp5971.py', 'class_name': 'HP5971', 'import_roots': [], 'candidate_methods': ['reset', 'scanSeqInit', 'getErrors', 'getAvc', 'getCivc', 'getRevisionWord', 'diagIO', 'getLogAmpScale', 'readyOff', 'rvrOff', 'rvrOn', 'getFaultStat', 'getSourceTemp', 'getPressure', 'isDiffPumpOn', 'isPFTBAOn', 'vent', 'massParms', 'massRange', 'tuningParms', 'filtSetupStd', 'filtSetupStdCoeff', 'qualSetupMaxOf3', 'calValve', 'isReady', 'readyOn', 'clearBuf', 'simSetup', 'simAct', 'simRamp', 'scanSetup', 'getScanType', 'scanStart', 'clearLensTable', 'dataMode', 'readData', 'merge', 'getConfig', 'scanSeq', 'scanDone', 'emit_dummy', 'msdInit', 'scanInit', 'getAScan', 'getPartialScan', 'getSpec', 'getSpecs', 'getStoredConfig', 'runStat', 'getAer', 'getRunTime', 'setRunDuration', 'setSrcEs', 'runReady', 'createRunTable', 'createSIMTable', 'createRunTableSIM', 'runTableOverride', 'override', 'scanStrtSeqInt', 'tunePeak', 'adjScanParms', 'scanStartSeq', 'getRunStat', 'getNrec', 'runStop', 'endRun', 'runReadyOff', 'faultmsgs', 'status'], 'action_targets': {}, 'metadata': {'repo': 'dirkenstein/pygcms', 'repo_url': 'https://github.com/dirkenstein/pygcms', 'brand': 'HP/Agilent', 'model': '5890 GC + 5971/5972 MSD', 'device_type_cn': 'GC-MS', 'device_type_en': 'Gas Chromatograph Mass Spectrometer', 'source_framework': '色谱/质谱', 'tag_id': '4411', 'tag_name': '气相色谱质谱联用仪', 'tag_name_en': 'GC-MS', 'candidate_score': 618, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def scanSeqInit(self, **kwargs):
        return self.call('scanSeqInit', kwargs=kwargs)

    def getErrors(self, **kwargs):
        return self.call('getErrors', kwargs=kwargs)

    def getAvc(self, **kwargs):
        return self.call('getAvc', kwargs=kwargs)

    def getCivc(self, **kwargs):
        return self.call('getCivc', kwargs=kwargs)

    def getRevisionWord(self, **kwargs):
        return self.call('getRevisionWord', kwargs=kwargs)

    def diagIO(self, **kwargs):
        return self.call('diagIO', kwargs=kwargs)

    def getLogAmpScale(self, **kwargs):
        return self.call('getLogAmpScale', kwargs=kwargs)

    def readyOff(self, **kwargs):
        return self.call('readyOff', kwargs=kwargs)

    def rvrOff(self, **kwargs):
        return self.call('rvrOff', kwargs=kwargs)

    def rvrOn(self, **kwargs):
        return self.call('rvrOn', kwargs=kwargs)

    def getFaultStat(self, **kwargs):
        return self.call('getFaultStat', kwargs=kwargs)

    def getSourceTemp(self, **kwargs):
        return self.call('getSourceTemp', kwargs=kwargs)

    def getPressure(self, **kwargs):
        return self.call('getPressure', kwargs=kwargs)

    def isDiffPumpOn(self, **kwargs):
        return self.call('isDiffPumpOn', kwargs=kwargs)

    def isPFTBAOn(self, **kwargs):
        return self.call('isPFTBAOn', kwargs=kwargs)

    def vent(self, **kwargs):
        return self.call('vent', kwargs=kwargs)

    def massParms(self, **kwargs):
        return self.call('massParms', kwargs=kwargs)

    def massRange(self, **kwargs):
        return self.call('massRange', kwargs=kwargs)

    def tuningParms(self, **kwargs):
        return self.call('tuningParms', kwargs=kwargs)

    def filtSetupStd(self, **kwargs):
        return self.call('filtSetupStd', kwargs=kwargs)

    def filtSetupStdCoeff(self, **kwargs):
        return self.call('filtSetupStdCoeff', kwargs=kwargs)

    def qualSetupMaxOf3(self, **kwargs):
        return self.call('qualSetupMaxOf3', kwargs=kwargs)

    def calValve(self, **kwargs):
        return self.call('calValve', kwargs=kwargs)

    def isReady(self, **kwargs):
        return self.call('isReady', kwargs=kwargs)

    def readyOn(self, **kwargs):
        return self.call('readyOn', kwargs=kwargs)

    def clearBuf(self, **kwargs):
        return self.call('clearBuf', kwargs=kwargs)

    def simSetup(self, **kwargs):
        return self.call('simSetup', kwargs=kwargs)

    def simAct(self, **kwargs):
        return self.call('simAct', kwargs=kwargs)

    def simRamp(self, **kwargs):
        return self.call('simRamp', kwargs=kwargs)

    def scanSetup(self, **kwargs):
        return self.call('scanSetup', kwargs=kwargs)

    def getScanType(self, **kwargs):
        return self.call('getScanType', kwargs=kwargs)

    def scanStart(self, **kwargs):
        return self.call('scanStart', kwargs=kwargs)

    def clearLensTable(self, **kwargs):
        return self.call('clearLensTable', kwargs=kwargs)

    def dataMode(self, **kwargs):
        return self.call('dataMode', kwargs=kwargs)

    def readData(self, **kwargs):
        return self.call('readData', kwargs=kwargs)

    def merge(self, **kwargs):
        return self.call('merge', kwargs=kwargs)

    def getConfig(self, **kwargs):
        return self.call('getConfig', kwargs=kwargs)

    def scanSeq(self, **kwargs):
        return self.call('scanSeq', kwargs=kwargs)

    def scanDone(self, **kwargs):
        return self.call('scanDone', kwargs=kwargs)

    def emit_dummy(self, **kwargs):
        return self.call('emit_dummy', kwargs=kwargs)

    def msdInit(self, **kwargs):
        return self.call('msdInit', kwargs=kwargs)

    def scanInit(self, **kwargs):
        return self.call('scanInit', kwargs=kwargs)

    def getAScan(self, **kwargs):
        return self.call('getAScan', kwargs=kwargs)

    def getPartialScan(self, **kwargs):
        return self.call('getPartialScan', kwargs=kwargs)

    def getSpec(self, **kwargs):
        return self.call('getSpec', kwargs=kwargs)

    def getSpecs(self, **kwargs):
        return self.call('getSpecs', kwargs=kwargs)

    def getStoredConfig(self, **kwargs):
        return self.call('getStoredConfig', kwargs=kwargs)

    def runStat(self, **kwargs):
        return self.call('runStat', kwargs=kwargs)

    def getAer(self, **kwargs):
        return self.call('getAer', kwargs=kwargs)

    def getRunTime(self, **kwargs):
        return self.call('getRunTime', kwargs=kwargs)

    def setRunDuration(self, **kwargs):
        return self.call('setRunDuration', kwargs=kwargs)

    def setSrcEs(self, **kwargs):
        return self.call('setSrcEs', kwargs=kwargs)

    def runReady(self, **kwargs):
        return self.call('runReady', kwargs=kwargs)

    def createRunTable(self, **kwargs):
        return self.call('createRunTable', kwargs=kwargs)

    def createSIMTable(self, **kwargs):
        return self.call('createSIMTable', kwargs=kwargs)

    def createRunTableSIM(self, **kwargs):
        return self.call('createRunTableSIM', kwargs=kwargs)

    def runTableOverride(self, **kwargs):
        return self.call('runTableOverride', kwargs=kwargs)

    def override(self, **kwargs):
        return self.call('override', kwargs=kwargs)

    def scanStrtSeqInt(self, **kwargs):
        return self.call('scanStrtSeqInt', kwargs=kwargs)

    def tunePeak(self, **kwargs):
        return self.call('tunePeak', kwargs=kwargs)

    def adjScanParms(self, **kwargs):
        return self.call('adjScanParms', kwargs=kwargs)

    def scanStartSeq(self, **kwargs):
        return self.call('scanStartSeq', kwargs=kwargs)

    def getRunStat(self, **kwargs):
        return self.call('getRunStat', kwargs=kwargs)

    def getNrec(self, **kwargs):
        return self.call('getNrec', kwargs=kwargs)

    def runStop(self, **kwargs):
        return self.call('runStop', kwargs=kwargs)

    def endRun(self, **kwargs):
        return self.call('endRun', kwargs=kwargs)

    def runReadyOff(self, **kwargs):
        return self.call('runReadyOff', kwargs=kwargs)

    def faultmsgs(self, **kwargs):
        return self.call('faultmsgs', kwargs=kwargs)

    def status(self, **kwargs):
        return self.call('status', kwargs=kwargs)

