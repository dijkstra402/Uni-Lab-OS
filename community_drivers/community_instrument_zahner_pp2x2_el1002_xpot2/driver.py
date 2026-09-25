from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentZahnerPp2x2El1002Xpot2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Zahner-elektrik__zahner_potentiostat', 'source_file': 'zahner_potentiostat/scpi_control/control.py', 'class_name': 'SCPIDevice', 'import_roots': [], 'candidate_methods': ['close', 'getDataReceiver', 'setRaiseOnErrorEnabled', 'getRaiseOnErrorEnabled', 'IDN', 'readDeviceInformations', 'clearState', 'readState', 'checkResetStatus', 'resetCommand', 'abortCommand', 'calibrateOffsets', 'switchToEPCControl', 'switchToEPCControlWithoutPotentiostatStateChange', 'setLineFrequency', 'getLineFrequency', 'setDateTime', 'getDateTime', 'getDateTimeStruct', 'getSoftwareInfo', 'getPotential', 'getVoltage', 'getPotentialMedian', 'getVoltageMedian', 'getCurrent', 'getCurrentMedian', 'setPotentiostatEnabled', 'setVoltageRelation', 'setVoltageValue', 'setCurrentValue', 'getMACAddress', 'setVoltageRange', 'setVoltageRangeIndex', 'setAutorangingEnabled', 'setInterpolationEnabled', 'setMinimumShuntIndex', 'setMaximumShuntIndex', 'setShuntIndex', 'setCurrentRange', 'setTimeParameter', 'setMaximumTimeParameter', 'setMinimumTimeParameter', 'setVoltageParameterRelation', 'setVoltageParameter', 'setCurrentParameter', 'setScanRateParameter', 'setCoupling', 'setBandwith', 'setFilterFrequency', 'setParameterLimitCheckToleranceTime', 'setMinMaxVoltageParameterCheckEnabled', 'setMinMaxCurrentParameterCheckEnabled', 'setMaximumVoltageParameter', 'setMinimumVoltageParameter', 'setMaximumCurrentParameter', 'setMinimumCurrentParameter', 'setGlobalLimitCheckToleranceTime', 'setGlobalVoltageCheckEnabled', 'setGlobalCurrentCheckEnabled', 'setMaximumVoltageGlobal', 'setMinimumVoltageGlobal', 'setMaximumCurrentGlobal', 'setMinimumCurrentGlobal', 'setSamplingFrequency', 'setToleranceBreakEnabled', 'setAbsoluteTolerance', 'setRelativeTolerance', 'setChargeBreakEnabled', 'setMaximumCharge', 'setMinimumCharge', 'getTemperature', 'setStepSize', 'measureRampValueInTime', 'measureRampValueInScanRate', 'measureRampScanRateForTime', 'measurePolarization', 'measureOCVScan', 'measureOCV', 'measureIEStairs', 'checkConnectionPolarity', 'measureCharge', 'measureDischarge', 'measureProfile', 'measurePITT', 'measureGITT'], 'action_targets': {}, 'metadata': {'repo': 'Zahner-elektrik/zahner_potentiostat', 'repo_url': 'https://github.com/Zahner-elektrik/zahner_potentiostat', 'brand': 'Zahner', 'model': 'PP2x2/EL1002/XPOT2', 'device_type_cn': '电化学工作站', 'device_type_en': 'Electrochemical Workstation', 'source_framework': '官方SDK', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 734, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

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

    def getPotential(self, **kwargs):
        return self.call('getPotential', kwargs=kwargs)

    def getVoltage(self, **kwargs):
        return self.call('getVoltage', kwargs=kwargs)

    def getPotentialMedian(self, **kwargs):
        return self.call('getPotentialMedian', kwargs=kwargs)

    def getVoltageMedian(self, **kwargs):
        return self.call('getVoltageMedian', kwargs=kwargs)

    def getCurrent(self, **kwargs):
        return self.call('getCurrent', kwargs=kwargs)

    def getCurrentMedian(self, **kwargs):
        return self.call('getCurrentMedian', kwargs=kwargs)

    def setPotentiostatEnabled(self, **kwargs):
        return self.call('setPotentiostatEnabled', kwargs=kwargs)

    def setVoltageRelation(self, **kwargs):
        return self.call('setVoltageRelation', kwargs=kwargs)

    def setVoltageValue(self, **kwargs):
        return self.call('setVoltageValue', kwargs=kwargs)

    def setCurrentValue(self, **kwargs):
        return self.call('setCurrentValue', kwargs=kwargs)

    def getMACAddress(self, **kwargs):
        return self.call('getMACAddress', kwargs=kwargs)

    def setVoltageRange(self, **kwargs):
        return self.call('setVoltageRange', kwargs=kwargs)

    def setVoltageRangeIndex(self, **kwargs):
        return self.call('setVoltageRangeIndex', kwargs=kwargs)

    def setAutorangingEnabled(self, **kwargs):
        return self.call('setAutorangingEnabled', kwargs=kwargs)

    def setInterpolationEnabled(self, **kwargs):
        return self.call('setInterpolationEnabled', kwargs=kwargs)

    def setMinimumShuntIndex(self, **kwargs):
        return self.call('setMinimumShuntIndex', kwargs=kwargs)

    def setMaximumShuntIndex(self, **kwargs):
        return self.call('setMaximumShuntIndex', kwargs=kwargs)

    def setShuntIndex(self, **kwargs):
        return self.call('setShuntIndex', kwargs=kwargs)

    def setCurrentRange(self, **kwargs):
        return self.call('setCurrentRange', kwargs=kwargs)

    def setTimeParameter(self, **kwargs):
        return self.call('setTimeParameter', kwargs=kwargs)

    def setMaximumTimeParameter(self, **kwargs):
        return self.call('setMaximumTimeParameter', kwargs=kwargs)

    def setMinimumTimeParameter(self, **kwargs):
        return self.call('setMinimumTimeParameter', kwargs=kwargs)

    def setVoltageParameterRelation(self, **kwargs):
        return self.call('setVoltageParameterRelation', kwargs=kwargs)

    def setVoltageParameter(self, **kwargs):
        return self.call('setVoltageParameter', kwargs=kwargs)

    def setCurrentParameter(self, **kwargs):
        return self.call('setCurrentParameter', kwargs=kwargs)

    def setScanRateParameter(self, **kwargs):
        return self.call('setScanRateParameter', kwargs=kwargs)

    def setCoupling(self, **kwargs):
        return self.call('setCoupling', kwargs=kwargs)

    def setBandwith(self, **kwargs):
        return self.call('setBandwith', kwargs=kwargs)

    def setFilterFrequency(self, **kwargs):
        return self.call('setFilterFrequency', kwargs=kwargs)

    def setParameterLimitCheckToleranceTime(self, **kwargs):
        return self.call('setParameterLimitCheckToleranceTime', kwargs=kwargs)

    def setMinMaxVoltageParameterCheckEnabled(self, **kwargs):
        return self.call('setMinMaxVoltageParameterCheckEnabled', kwargs=kwargs)

    def setMinMaxCurrentParameterCheckEnabled(self, **kwargs):
        return self.call('setMinMaxCurrentParameterCheckEnabled', kwargs=kwargs)

    def setMaximumVoltageParameter(self, **kwargs):
        return self.call('setMaximumVoltageParameter', kwargs=kwargs)

    def setMinimumVoltageParameter(self, **kwargs):
        return self.call('setMinimumVoltageParameter', kwargs=kwargs)

    def setMaximumCurrentParameter(self, **kwargs):
        return self.call('setMaximumCurrentParameter', kwargs=kwargs)

    def setMinimumCurrentParameter(self, **kwargs):
        return self.call('setMinimumCurrentParameter', kwargs=kwargs)

    def setGlobalLimitCheckToleranceTime(self, **kwargs):
        return self.call('setGlobalLimitCheckToleranceTime', kwargs=kwargs)

    def setGlobalVoltageCheckEnabled(self, **kwargs):
        return self.call('setGlobalVoltageCheckEnabled', kwargs=kwargs)

    def setGlobalCurrentCheckEnabled(self, **kwargs):
        return self.call('setGlobalCurrentCheckEnabled', kwargs=kwargs)

    def setMaximumVoltageGlobal(self, **kwargs):
        return self.call('setMaximumVoltageGlobal', kwargs=kwargs)

    def setMinimumVoltageGlobal(self, **kwargs):
        return self.call('setMinimumVoltageGlobal', kwargs=kwargs)

    def setMaximumCurrentGlobal(self, **kwargs):
        return self.call('setMaximumCurrentGlobal', kwargs=kwargs)

    def setMinimumCurrentGlobal(self, **kwargs):
        return self.call('setMinimumCurrentGlobal', kwargs=kwargs)

    def setSamplingFrequency(self, **kwargs):
        return self.call('setSamplingFrequency', kwargs=kwargs)

    def setToleranceBreakEnabled(self, **kwargs):
        return self.call('setToleranceBreakEnabled', kwargs=kwargs)

    def setAbsoluteTolerance(self, **kwargs):
        return self.call('setAbsoluteTolerance', kwargs=kwargs)

    def setRelativeTolerance(self, **kwargs):
        return self.call('setRelativeTolerance', kwargs=kwargs)

    def setChargeBreakEnabled(self, **kwargs):
        return self.call('setChargeBreakEnabled', kwargs=kwargs)

    def setMaximumCharge(self, **kwargs):
        return self.call('setMaximumCharge', kwargs=kwargs)

    def setMinimumCharge(self, **kwargs):
        return self.call('setMinimumCharge', kwargs=kwargs)

    def getTemperature(self, **kwargs):
        return self.call('getTemperature', kwargs=kwargs)

    def setStepSize(self, **kwargs):
        return self.call('setStepSize', kwargs=kwargs)

    def measureRampValueInTime(self, **kwargs):
        return self.call('measureRampValueInTime', kwargs=kwargs)

    def measureRampValueInScanRate(self, **kwargs):
        return self.call('measureRampValueInScanRate', kwargs=kwargs)

    def measureRampScanRateForTime(self, **kwargs):
        return self.call('measureRampScanRateForTime', kwargs=kwargs)

    def measurePolarization(self, **kwargs):
        return self.call('measurePolarization', kwargs=kwargs)

    def measureOCVScan(self, **kwargs):
        return self.call('measureOCVScan', kwargs=kwargs)

    def measureOCV(self, **kwargs):
        return self.call('measureOCV', kwargs=kwargs)

    def measureIEStairs(self, **kwargs):
        return self.call('measureIEStairs', kwargs=kwargs)

    def checkConnectionPolarity(self, **kwargs):
        return self.call('checkConnectionPolarity', kwargs=kwargs)

    def measureCharge(self, **kwargs):
        return self.call('measureCharge', kwargs=kwargs)

    def measureDischarge(self, **kwargs):
        return self.call('measureDischarge', kwargs=kwargs)

    def measureProfile(self, **kwargs):
        return self.call('measureProfile', kwargs=kwargs)

    def measurePITT(self, **kwargs):
        return self.call('measurePITT', kwargs=kwargs)

    def measureGITT(self, **kwargs):
        return self.call('measureGITT', kwargs=kwargs)

