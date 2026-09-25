from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentZahnerZennium(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Zahner-elektrik__Thales-Remote-Python', 'source_file': 'thales_remote/script_wrapper.py', 'class_name': 'ThalesRemoteScriptWrapper', 'import_roots': [], 'candidate_methods': ['getCurrent', 'getPotential', 'getVoltage', 'setCurrent', 'setPotential', 'setVoltage', 'setMaximumShunt', 'setMinimumShunt', 'setShuntIndex', 'setVoltageRangeIndex', 'selectPotentiostat', 'selectPotentiostatWithoutPotentiostatStateChange', 'switchToSCPIControl', 'switchToSCPIControlWithoutPotentiostatStateChange', 'loadPotentiostatSettings', 'savePotentiostatSettings', 'getSerialNumber', 'getDeviceInformation', 'getDeviceName', 'readSetup', 'calibrateOffsets', 'enablePotentiostat', 'disablePotentiostat', 'setPotentiostatMode', 'enableRuleFileUsage', 'disableRuleFileUsage', 'setupPad4Channel', 'setupPad4ModeGlobal', 'enablePad4Global', 'disablePad4Global', 'readPad4SetupGlobal', 'setFrequency', 'setAmplitude', 'setNumberOfPeriods', 'setUpperFrequencyLimit', 'setLowerFrequencyLimit', 'setStartFrequency', 'setUpperStepsPerDecade', 'setLowerStepsPerDecade', 'setUpperNumberOfPeriods', 'setLowerNumberOfPeriods', 'setScanStrategy', 'setScanDirection', 'getImpedance', 'getImpedanceAsArray', 'getImpedancePad4', 'getImpedancePad4AsArray', 'setEISNaming', 'setEISCounter', 'setEISOutputPath', 'setEISOutputFileName', 'measureEIS', 'setCVStartPotential', 'setCVUpperReversingPotential', 'setCVLowerReversingPotential', 'setCVEndPotential', 'setCVStartHoldTime', 'setCVEndHoldTime', 'setCVScanRate', 'setCVCycles', 'setCVSamplesPerCycle', 'setCVMaximumCurrent', 'setCVMinimumCurrent', 'setCVOhmicDrop', 'enableCVAutoRestartAtCurrentOverflow', 'disableCVAutoRestartAtCurrentOverflow', 'enableCVAutoRestartAtCurrentUnderflow', 'disableCVAutoRestartAtCurrentUnderflow', 'enableCVAnalogFunctionGenerator', 'disableCVAnalogFunctionGenerator', 'setCVNaming', 'setCVCounter', 'setCVOutputPath', 'setCVOutputFileName', 'checkCVSetup', 'readCVSetup', 'measureCV', 'setIEFirstEdgePotential', 'setIESecondEdgePotential', 'setIEThirdEdgePotential', 'setIEFourthEdgePotential', 'setIEFirstEdgePotentialRelation', 'setIESecondEdgePotentialRelation', 'setIEThirdEdgePotentialRelation', 'setIEFourthEdgePotentialRelation', 'setIEPotentialResolution', 'setIEMinimumWaitingTime', 'setIEMaximumWaitingTime', 'setIERelativeTolerance', 'setIEAbsoluteTolerance', 'setIEOhmicDrop', 'setIESweepMode', 'setIEScanRate', 'setIEMaximumCurrent', 'setIEMinimumCurrent', 'setIENaming', 'setIECounter', 'setIEOutputPath', 'setIEOutputFileName', 'checkIESetup', 'readIESetup', 'measureIE', 'selectSequence', 'setSequenceNaming', 'setSequenceCounter', 'setSequenceOutputPath', 'setSequenceOutputFileName', 'enableSequenceAcqGlobal', 'disableSequenceAcqGlobal', 'enableSequenceAcqChannel', 'disableSequenceAcqChannel', 'readSequenceAcqSetup', 'runSequence', 'runSequenceFile', 'setSequenceOhmicDrop', 'setSequenceMaximumRuntime', 'setSequenceUpperPotentialLimit', 'setSequenceLowerPotentialLimit', 'setSequenceUpperCurrentLimit', 'setSequenceLowerCurrentLimit', 'setSequenceCurrentRange', 'setSequencePotentialLatencyWindow', 'setSequenceCurrentLatencyWindow', 'enableFraMode', 'readFraSetup', 'disableFraMode', 'setFraVoltageInputGain', 'setFraVoltageInputOffset', 'setFraVoltageOutputGain', 'setFraVoltageOutputOffset', 'setFraVoltageMinimum', 'setFraVoltageMaximum', 'setFraCurrentInputGain', 'setFraCurrentInputOffset', 'setFraCurrentOutputGain', 'setFraCurrentOutputOffset', 'setFraCurrentMinimum', 'setFraCurrentMaximum', 'setFraPotentiostatMode', 'readAcqSetup', 'readAllAcqChannels', 'readAcqChannel', 'disableAcq', 'enableAcq', 'setValue', 'executeRemoteCommand', 'forceThalesIntoRemoteScript', 'hideWindow', 'showWindow', 'getThalesVersion', 'getWorkstationHeartBeat', 'getSerialNumberFromTerm', 'getTermIsActive'], 'action_targets': {}, 'metadata': {'repo': 'Zahner-elektrik/Thales-Remote-Python', 'repo_url': 'https://github.com/Zahner-elektrik/Thales-Remote-Python', 'brand': 'Zahner', 'model': 'Zennium', 'device_type_cn': '恒电位仪/EIS', 'device_type_en': 'Potentiostat/EIS', 'source_framework': '电化学/热分析/天平', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 1294, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def getCurrent(self, **kwargs):
        return self.call('getCurrent', kwargs=kwargs)

    def getPotential(self, **kwargs):
        return self.call('getPotential', kwargs=kwargs)

    def getVoltage(self, **kwargs):
        return self.call('getVoltage', kwargs=kwargs)

    def setCurrent(self, **kwargs):
        return self.call('setCurrent', kwargs=kwargs)

    def setPotential(self, **kwargs):
        return self.call('setPotential', kwargs=kwargs)

    def setVoltage(self, **kwargs):
        return self.call('setVoltage', kwargs=kwargs)

    def setMaximumShunt(self, **kwargs):
        return self.call('setMaximumShunt', kwargs=kwargs)

    def setMinimumShunt(self, **kwargs):
        return self.call('setMinimumShunt', kwargs=kwargs)

    def setShuntIndex(self, **kwargs):
        return self.call('setShuntIndex', kwargs=kwargs)

    def setVoltageRangeIndex(self, **kwargs):
        return self.call('setVoltageRangeIndex', kwargs=kwargs)

    def selectPotentiostat(self, **kwargs):
        return self.call('selectPotentiostat', kwargs=kwargs)

    def selectPotentiostatWithoutPotentiostatStateChange(self, **kwargs):
        return self.call('selectPotentiostatWithoutPotentiostatStateChange', kwargs=kwargs)

    def switchToSCPIControl(self, **kwargs):
        return self.call('switchToSCPIControl', kwargs=kwargs)

    def switchToSCPIControlWithoutPotentiostatStateChange(self, **kwargs):
        return self.call('switchToSCPIControlWithoutPotentiostatStateChange', kwargs=kwargs)

    def loadPotentiostatSettings(self, **kwargs):
        return self.call('loadPotentiostatSettings', kwargs=kwargs)

    def savePotentiostatSettings(self, **kwargs):
        return self.call('savePotentiostatSettings', kwargs=kwargs)

    def getSerialNumber(self, **kwargs):
        return self.call('getSerialNumber', kwargs=kwargs)

    def getDeviceInformation(self, **kwargs):
        return self.call('getDeviceInformation', kwargs=kwargs)

    def getDeviceName(self, **kwargs):
        return self.call('getDeviceName', kwargs=kwargs)

    def readSetup(self, **kwargs):
        return self.call('readSetup', kwargs=kwargs)

    def calibrateOffsets(self, **kwargs):
        return self.call('calibrateOffsets', kwargs=kwargs)

    def enablePotentiostat(self, **kwargs):
        return self.call('enablePotentiostat', kwargs=kwargs)

    def disablePotentiostat(self, **kwargs):
        return self.call('disablePotentiostat', kwargs=kwargs)

    def setPotentiostatMode(self, **kwargs):
        return self.call('setPotentiostatMode', kwargs=kwargs)

    def enableRuleFileUsage(self, **kwargs):
        return self.call('enableRuleFileUsage', kwargs=kwargs)

    def disableRuleFileUsage(self, **kwargs):
        return self.call('disableRuleFileUsage', kwargs=kwargs)

    def setupPad4Channel(self, **kwargs):
        return self.call('setupPad4Channel', kwargs=kwargs)

    def setupPad4ModeGlobal(self, **kwargs):
        return self.call('setupPad4ModeGlobal', kwargs=kwargs)

    def enablePad4Global(self, **kwargs):
        return self.call('enablePad4Global', kwargs=kwargs)

    def disablePad4Global(self, **kwargs):
        return self.call('disablePad4Global', kwargs=kwargs)

    def readPad4SetupGlobal(self, **kwargs):
        return self.call('readPad4SetupGlobal', kwargs=kwargs)

    def setFrequency(self, **kwargs):
        return self.call('setFrequency', kwargs=kwargs)

    def setAmplitude(self, **kwargs):
        return self.call('setAmplitude', kwargs=kwargs)

    def setNumberOfPeriods(self, **kwargs):
        return self.call('setNumberOfPeriods', kwargs=kwargs)

    def setUpperFrequencyLimit(self, **kwargs):
        return self.call('setUpperFrequencyLimit', kwargs=kwargs)

    def setLowerFrequencyLimit(self, **kwargs):
        return self.call('setLowerFrequencyLimit', kwargs=kwargs)

    def setStartFrequency(self, **kwargs):
        return self.call('setStartFrequency', kwargs=kwargs)

    def setUpperStepsPerDecade(self, **kwargs):
        return self.call('setUpperStepsPerDecade', kwargs=kwargs)

    def setLowerStepsPerDecade(self, **kwargs):
        return self.call('setLowerStepsPerDecade', kwargs=kwargs)

    def setUpperNumberOfPeriods(self, **kwargs):
        return self.call('setUpperNumberOfPeriods', kwargs=kwargs)

    def setLowerNumberOfPeriods(self, **kwargs):
        return self.call('setLowerNumberOfPeriods', kwargs=kwargs)

    def setScanStrategy(self, **kwargs):
        return self.call('setScanStrategy', kwargs=kwargs)

    def setScanDirection(self, **kwargs):
        return self.call('setScanDirection', kwargs=kwargs)

    def getImpedance(self, **kwargs):
        return self.call('getImpedance', kwargs=kwargs)

    def getImpedanceAsArray(self, **kwargs):
        return self.call('getImpedanceAsArray', kwargs=kwargs)

    def getImpedancePad4(self, **kwargs):
        return self.call('getImpedancePad4', kwargs=kwargs)

    def getImpedancePad4AsArray(self, **kwargs):
        return self.call('getImpedancePad4AsArray', kwargs=kwargs)

    def setEISNaming(self, **kwargs):
        return self.call('setEISNaming', kwargs=kwargs)

    def setEISCounter(self, **kwargs):
        return self.call('setEISCounter', kwargs=kwargs)

    def setEISOutputPath(self, **kwargs):
        return self.call('setEISOutputPath', kwargs=kwargs)

    def setEISOutputFileName(self, **kwargs):
        return self.call('setEISOutputFileName', kwargs=kwargs)

    def measureEIS(self, **kwargs):
        return self.call('measureEIS', kwargs=kwargs)

    def setCVStartPotential(self, **kwargs):
        return self.call('setCVStartPotential', kwargs=kwargs)

    def setCVUpperReversingPotential(self, **kwargs):
        return self.call('setCVUpperReversingPotential', kwargs=kwargs)

    def setCVLowerReversingPotential(self, **kwargs):
        return self.call('setCVLowerReversingPotential', kwargs=kwargs)

    def setCVEndPotential(self, **kwargs):
        return self.call('setCVEndPotential', kwargs=kwargs)

    def setCVStartHoldTime(self, **kwargs):
        return self.call('setCVStartHoldTime', kwargs=kwargs)

    def setCVEndHoldTime(self, **kwargs):
        return self.call('setCVEndHoldTime', kwargs=kwargs)

    def setCVScanRate(self, **kwargs):
        return self.call('setCVScanRate', kwargs=kwargs)

    def setCVCycles(self, **kwargs):
        return self.call('setCVCycles', kwargs=kwargs)

    def setCVSamplesPerCycle(self, **kwargs):
        return self.call('setCVSamplesPerCycle', kwargs=kwargs)

    def setCVMaximumCurrent(self, **kwargs):
        return self.call('setCVMaximumCurrent', kwargs=kwargs)

    def setCVMinimumCurrent(self, **kwargs):
        return self.call('setCVMinimumCurrent', kwargs=kwargs)

    def setCVOhmicDrop(self, **kwargs):
        return self.call('setCVOhmicDrop', kwargs=kwargs)

    def enableCVAutoRestartAtCurrentOverflow(self, **kwargs):
        return self.call('enableCVAutoRestartAtCurrentOverflow', kwargs=kwargs)

    def disableCVAutoRestartAtCurrentOverflow(self, **kwargs):
        return self.call('disableCVAutoRestartAtCurrentOverflow', kwargs=kwargs)

    def enableCVAutoRestartAtCurrentUnderflow(self, **kwargs):
        return self.call('enableCVAutoRestartAtCurrentUnderflow', kwargs=kwargs)

    def disableCVAutoRestartAtCurrentUnderflow(self, **kwargs):
        return self.call('disableCVAutoRestartAtCurrentUnderflow', kwargs=kwargs)

    def enableCVAnalogFunctionGenerator(self, **kwargs):
        return self.call('enableCVAnalogFunctionGenerator', kwargs=kwargs)

    def disableCVAnalogFunctionGenerator(self, **kwargs):
        return self.call('disableCVAnalogFunctionGenerator', kwargs=kwargs)

    def setCVNaming(self, **kwargs):
        return self.call('setCVNaming', kwargs=kwargs)

    def setCVCounter(self, **kwargs):
        return self.call('setCVCounter', kwargs=kwargs)

    def setCVOutputPath(self, **kwargs):
        return self.call('setCVOutputPath', kwargs=kwargs)

    def setCVOutputFileName(self, **kwargs):
        return self.call('setCVOutputFileName', kwargs=kwargs)

    def checkCVSetup(self, **kwargs):
        return self.call('checkCVSetup', kwargs=kwargs)

    def readCVSetup(self, **kwargs):
        return self.call('readCVSetup', kwargs=kwargs)

    def measureCV(self, **kwargs):
        return self.call('measureCV', kwargs=kwargs)

    def setIEFirstEdgePotential(self, **kwargs):
        return self.call('setIEFirstEdgePotential', kwargs=kwargs)

    def setIESecondEdgePotential(self, **kwargs):
        return self.call('setIESecondEdgePotential', kwargs=kwargs)

    def setIEThirdEdgePotential(self, **kwargs):
        return self.call('setIEThirdEdgePotential', kwargs=kwargs)

    def setIEFourthEdgePotential(self, **kwargs):
        return self.call('setIEFourthEdgePotential', kwargs=kwargs)

    def setIEFirstEdgePotentialRelation(self, **kwargs):
        return self.call('setIEFirstEdgePotentialRelation', kwargs=kwargs)

    def setIESecondEdgePotentialRelation(self, **kwargs):
        return self.call('setIESecondEdgePotentialRelation', kwargs=kwargs)

    def setIEThirdEdgePotentialRelation(self, **kwargs):
        return self.call('setIEThirdEdgePotentialRelation', kwargs=kwargs)

    def setIEFourthEdgePotentialRelation(self, **kwargs):
        return self.call('setIEFourthEdgePotentialRelation', kwargs=kwargs)

    def setIEPotentialResolution(self, **kwargs):
        return self.call('setIEPotentialResolution', kwargs=kwargs)

    def setIEMinimumWaitingTime(self, **kwargs):
        return self.call('setIEMinimumWaitingTime', kwargs=kwargs)

    def setIEMaximumWaitingTime(self, **kwargs):
        return self.call('setIEMaximumWaitingTime', kwargs=kwargs)

    def setIERelativeTolerance(self, **kwargs):
        return self.call('setIERelativeTolerance', kwargs=kwargs)

    def setIEAbsoluteTolerance(self, **kwargs):
        return self.call('setIEAbsoluteTolerance', kwargs=kwargs)

    def setIEOhmicDrop(self, **kwargs):
        return self.call('setIEOhmicDrop', kwargs=kwargs)

    def setIESweepMode(self, **kwargs):
        return self.call('setIESweepMode', kwargs=kwargs)

    def setIEScanRate(self, **kwargs):
        return self.call('setIEScanRate', kwargs=kwargs)

    def setIEMaximumCurrent(self, **kwargs):
        return self.call('setIEMaximumCurrent', kwargs=kwargs)

    def setIEMinimumCurrent(self, **kwargs):
        return self.call('setIEMinimumCurrent', kwargs=kwargs)

    def setIENaming(self, **kwargs):
        return self.call('setIENaming', kwargs=kwargs)

    def setIECounter(self, **kwargs):
        return self.call('setIECounter', kwargs=kwargs)

    def setIEOutputPath(self, **kwargs):
        return self.call('setIEOutputPath', kwargs=kwargs)

    def setIEOutputFileName(self, **kwargs):
        return self.call('setIEOutputFileName', kwargs=kwargs)

    def checkIESetup(self, **kwargs):
        return self.call('checkIESetup', kwargs=kwargs)

    def readIESetup(self, **kwargs):
        return self.call('readIESetup', kwargs=kwargs)

    def measureIE(self, **kwargs):
        return self.call('measureIE', kwargs=kwargs)

    def selectSequence(self, **kwargs):
        return self.call('selectSequence', kwargs=kwargs)

    def setSequenceNaming(self, **kwargs):
        return self.call('setSequenceNaming', kwargs=kwargs)

    def setSequenceCounter(self, **kwargs):
        return self.call('setSequenceCounter', kwargs=kwargs)

    def setSequenceOutputPath(self, **kwargs):
        return self.call('setSequenceOutputPath', kwargs=kwargs)

    def setSequenceOutputFileName(self, **kwargs):
        return self.call('setSequenceOutputFileName', kwargs=kwargs)

    def enableSequenceAcqGlobal(self, **kwargs):
        return self.call('enableSequenceAcqGlobal', kwargs=kwargs)

    def disableSequenceAcqGlobal(self, **kwargs):
        return self.call('disableSequenceAcqGlobal', kwargs=kwargs)

    def enableSequenceAcqChannel(self, **kwargs):
        return self.call('enableSequenceAcqChannel', kwargs=kwargs)

    def disableSequenceAcqChannel(self, **kwargs):
        return self.call('disableSequenceAcqChannel', kwargs=kwargs)

    def readSequenceAcqSetup(self, **kwargs):
        return self.call('readSequenceAcqSetup', kwargs=kwargs)

    def runSequence(self, **kwargs):
        return self.call('runSequence', kwargs=kwargs)

    def runSequenceFile(self, **kwargs):
        return self.call('runSequenceFile', kwargs=kwargs)

    def setSequenceOhmicDrop(self, **kwargs):
        return self.call('setSequenceOhmicDrop', kwargs=kwargs)

    def setSequenceMaximumRuntime(self, **kwargs):
        return self.call('setSequenceMaximumRuntime', kwargs=kwargs)

    def setSequenceUpperPotentialLimit(self, **kwargs):
        return self.call('setSequenceUpperPotentialLimit', kwargs=kwargs)

    def setSequenceLowerPotentialLimit(self, **kwargs):
        return self.call('setSequenceLowerPotentialLimit', kwargs=kwargs)

    def setSequenceUpperCurrentLimit(self, **kwargs):
        return self.call('setSequenceUpperCurrentLimit', kwargs=kwargs)

    def setSequenceLowerCurrentLimit(self, **kwargs):
        return self.call('setSequenceLowerCurrentLimit', kwargs=kwargs)

    def setSequenceCurrentRange(self, **kwargs):
        return self.call('setSequenceCurrentRange', kwargs=kwargs)

    def setSequencePotentialLatencyWindow(self, **kwargs):
        return self.call('setSequencePotentialLatencyWindow', kwargs=kwargs)

    def setSequenceCurrentLatencyWindow(self, **kwargs):
        return self.call('setSequenceCurrentLatencyWindow', kwargs=kwargs)

    def enableFraMode(self, **kwargs):
        return self.call('enableFraMode', kwargs=kwargs)

    def readFraSetup(self, **kwargs):
        return self.call('readFraSetup', kwargs=kwargs)

    def disableFraMode(self, **kwargs):
        return self.call('disableFraMode', kwargs=kwargs)

    def setFraVoltageInputGain(self, **kwargs):
        return self.call('setFraVoltageInputGain', kwargs=kwargs)

    def setFraVoltageInputOffset(self, **kwargs):
        return self.call('setFraVoltageInputOffset', kwargs=kwargs)

    def setFraVoltageOutputGain(self, **kwargs):
        return self.call('setFraVoltageOutputGain', kwargs=kwargs)

    def setFraVoltageOutputOffset(self, **kwargs):
        return self.call('setFraVoltageOutputOffset', kwargs=kwargs)

    def setFraVoltageMinimum(self, **kwargs):
        return self.call('setFraVoltageMinimum', kwargs=kwargs)

    def setFraVoltageMaximum(self, **kwargs):
        return self.call('setFraVoltageMaximum', kwargs=kwargs)

    def setFraCurrentInputGain(self, **kwargs):
        return self.call('setFraCurrentInputGain', kwargs=kwargs)

    def setFraCurrentInputOffset(self, **kwargs):
        return self.call('setFraCurrentInputOffset', kwargs=kwargs)

    def setFraCurrentOutputGain(self, **kwargs):
        return self.call('setFraCurrentOutputGain', kwargs=kwargs)

    def setFraCurrentOutputOffset(self, **kwargs):
        return self.call('setFraCurrentOutputOffset', kwargs=kwargs)

    def setFraCurrentMinimum(self, **kwargs):
        return self.call('setFraCurrentMinimum', kwargs=kwargs)

    def setFraCurrentMaximum(self, **kwargs):
        return self.call('setFraCurrentMaximum', kwargs=kwargs)

    def setFraPotentiostatMode(self, **kwargs):
        return self.call('setFraPotentiostatMode', kwargs=kwargs)

    def readAcqSetup(self, **kwargs):
        return self.call('readAcqSetup', kwargs=kwargs)

    def readAllAcqChannels(self, **kwargs):
        return self.call('readAllAcqChannels', kwargs=kwargs)

    def readAcqChannel(self, **kwargs):
        return self.call('readAcqChannel', kwargs=kwargs)

    def disableAcq(self, **kwargs):
        return self.call('disableAcq', kwargs=kwargs)

    def enableAcq(self, **kwargs):
        return self.call('enableAcq', kwargs=kwargs)

    def setValue(self, **kwargs):
        return self.call('setValue', kwargs=kwargs)

    def executeRemoteCommand(self, **kwargs):
        return self.call('executeRemoteCommand', kwargs=kwargs)

    def forceThalesIntoRemoteScript(self, **kwargs):
        return self.call('forceThalesIntoRemoteScript', kwargs=kwargs)

    def hideWindow(self, **kwargs):
        return self.call('hideWindow', kwargs=kwargs)

    def showWindow(self, **kwargs):
        return self.call('showWindow', kwargs=kwargs)

    def getThalesVersion(self, **kwargs):
        return self.call('getThalesVersion', kwargs=kwargs)

    def getWorkstationHeartBeat(self, **kwargs):
        return self.call('getWorkstationHeartBeat', kwargs=kwargs)

    def getSerialNumberFromTerm(self, **kwargs):
        return self.call('getSerialNumberFromTerm', kwargs=kwargs)

    def getTermIsActive(self, **kwargs):
        return self.call('getTermIsActive', kwargs=kwargs)

