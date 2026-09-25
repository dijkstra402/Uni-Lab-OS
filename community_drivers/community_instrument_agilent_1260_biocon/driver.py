from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilent1260Biocon(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/biocatiit__beamline-control-user', 'source_file': 'biocon/XPS_C8_drivers.py', 'class_name': 'XPS', 'import_roots': [], 'candidate_methods': ['withValidSocket', 'Send', 'TCP_ConnectToServer', 'TCP_SetTimeout', 'TCP_CloseSocket', 'GetLibraryVersion', 'ControllerMotionKernelTimeLoadGet', 'ControllerStatusGet', 'ControllerStatusStringGet', 'ElapsedTimeGet', 'ErrorStringGet', 'FirmwareVersionGet', 'TCLScriptExecute', 'TCLScriptExecuteAndWait', 'TCLScriptExecuteWithPriority', 'TCLScriptKill', 'TimerGet', 'TimerSet', 'Reboot', 'Login', 'CloseAllOtherSockets', 'HardwareDateAndTimeGet', 'HardwareDateAndTimeSet', 'EventAdd', 'EventGet', 'EventRemove', 'EventWait', 'EventExtendedConfigurationTriggerSet', 'EventExtendedConfigurationTriggerGet', 'EventExtendedConfigurationActionSet', 'EventExtendedConfigurationActionGet', 'EventExtendedStart', 'EventExtendedAllGet', 'EventExtendedGet', 'EventExtendedRemove', 'EventExtendedWait', 'GatheringConfigurationGet', 'GatheringConfigurationSet', 'GatheringCurrentNumberGet', 'GatheringStopAndSave', 'GatheringDataAcquire', 'GatheringDataGet', 'GatheringDataMultipleLinesGet', 'GatheringReset', 'GatheringRun', 'GatheringRunAppend', 'GatheringStop', 'GatheringExternalConfigurationSet', 'GatheringExternalConfigurationGet', 'GatheringExternalCurrentNumberGet', 'GatheringExternalDataGet', 'GatheringExternalStopAndSave', 'GlobalArrayGet', 'GlobalArraySet', 'DoubleGlobalArrayGet', 'DoubleGlobalArraySet', 'GPIOAnalogGet', 'GPIOAnalogSet', 'GPIOAnalogGainGet', 'GPIOAnalogGainSet', 'GPIODigitalGet', 'GPIODigitalSet', 'GroupAccelerationSetpointGet', 'GroupAnalogTrackingModeEnable', 'GroupAnalogTrackingModeDisable', 'GroupCorrectorOutputGet', 'GroupCurrentFollowingErrorGet', 'GroupHomeSearch', 'GroupHomeSearchAndRelativeMove', 'GroupInitialize', 'GroupInitializeWithEncoderCalibration', 'GroupJogParametersSet', 'GroupJogParametersGet', 'GroupJogCurrentGet', 'GroupJogModeEnable', 'GroupJogModeDisable', 'GroupKill', 'GroupMoveAbort', 'GroupMoveAbsolute', 'GroupMoveRelative', 'GroupMotionDisable', 'GroupMotionEnable', 'GroupPositionCorrectedProfilerGet', 'GroupPositionCurrentGet', 'GroupPositionPCORawEncoderGet', 'GroupPositionSetpointGet', 'GroupPositionTargetGet', 'GroupReferencingActionExecute', 'GroupReferencingStart', 'GroupReferencingStop', 'GroupStatusGet', 'GroupStatusStringGet', 'GroupVelocityCurrentGet', 'HexapodMoveAbsolute', 'HexapodMoveRelative', 'HexapodPositionCurrentGet', 'KillAll', 'PositionerAnalogTrackingPositionParametersGet', 'PositionerAnalogTrackingPositionParametersSet', 'PositionerAnalogTrackingVelocityParametersGet', 'PositionerAnalogTrackingVelocityParametersSet', 'PositionerBacklashGet', 'PositionerBacklashSet', 'PositionerBacklashEnable', 'PositionerBacklashDisable', 'PositionerCorrectorNotchFiltersSet', 'PositionerCorrectorNotchFiltersGet', 'PositionerCorrectorPIDFFAccelerationSet', 'PositionerCorrectorPIDFFAccelerationGet', 'PositionerCorrectorPIDFFVelocitySet', 'PositionerCorrectorPIDFFVelocityGet', 'PositionerCorrectorPIDDualFFVoltageSet', 'PositionerCorrectorPIDDualFFVoltageGet', 'PositionerCorrectorPIPositionSet', 'PositionerCorrectorPIPositionGet', 'PositionerCorrectorTypeGet', 'PositionerCurrentVelocityAccelerationFiltersGet', 'PositionerCurrentVelocityAccelerationFiltersSet', 'PositionerDriverFiltersGet', 'PositionerDriverFiltersSet', 'PositionerDriverPositionOffsetsGet', 'PositionerDriverStatusGet', 'PositionerDriverStatusStringGet', 'PositionerEncoderAmplitudeValuesGet', 'PositionerEncoderCalibrationParametersGet', 'PositionerErrorGet', 'PositionerErrorRead', 'PositionerErrorStringGet', 'PositionerExcitationSignalGet', 'PositionerExcitationSignalSet', 'PositionerExternalLatchPositionGet', 'PositionerHardwareStatusGet', 'PositionerHardwareStatusStringGet', 'PositionerHardInterpolatorFactorGet', 'PositionerHardInterpolatorFactorSet', 'PositionerMaximumVelocityAndAccelerationGet', 'PositionerMotionDoneGet', 'PositionerMotionDoneSet', 'PositionerPositionCompareAquadBAlwaysEnable', 'PositionerPositionCompareAquadBWindowedGet', 'PositionerPositionCompareAquadBWindowedSet', 'PositionerPositionCompareGet', 'PositionerPositionCompareSet', 'PositionerPositionCompareEnable', 'PositionerPositionCompareDisable', 'PositionerPositionComparePulseParametersGet', 'PositionerPositionComparePulseParametersSet', 'PositionerRawEncoderPositionGet', 'PositionersEncoderIndexDifferenceGet', 'PositionerSGammaExactVelocityAjustedDisplacementGet', 'PositionerSGammaParametersGet', 'PositionerSGammaParametersSet', 'PositionerSGammaPreviousMotionTimesGet', 'PositionerStageParameterGet', 'PositionerStageParameterSet', 'PositionerTimeFlasherGet', 'PositionerTimeFlasherSet', 'PositionerTimeFlasherEnable', 'PositionerTimeFlasherDisable', 'PositionerUserTravelLimitsGet', 'PositionerUserTravelLimitsSet', 'PositionerDACOffsetGet', 'PositionerDACOffsetSet', 'PositionerDACOffsetDualGet', 'PositionerDACOffsetDualSet', 'PositionerCorrectorAutoTuning', 'PositionerAccelerationAutoScaling', 'MultipleAxesPVTVerification', 'MultipleAxesPVTVerificationResultGet', 'MultipleAxesPVTExecution', 'MultipleAxesPVTParametersGet', 'MultipleAxesPVTPulseOutputSet', 'MultipleAxesPVTPulseOutputGet', 'SingleAxisSlaveModeEnable', 'SingleAxisSlaveModeDisable', 'SingleAxisSlaveParametersSet', 'SingleAxisSlaveParametersGet', 'SpindleSlaveModeEnable', 'SpindleSlaveModeDisable', 'SpindleSlaveParametersSet', 'SpindleSlaveParametersGet', 'GroupSpinParametersSet', 'GroupSpinParametersGet', 'GroupSpinCurrentGet', 'GroupSpinModeStop', 'XYLineArcVerification', 'XYLineArcVerificationResultGet', 'XYLineArcExecution', 'XYLineArcParametersGet', 'XYLineArcPulseOutputSet', 'XYLineArcPulseOutputGet', 'XYZGroupPositionCorrectedProfilerGet', 'XYZSplineVerification', 'XYZSplineVerificationResultGet', 'XYZSplineExecution', 'XYZSplineParametersGet', 'OptionalModuleExecute', 'OptionalModuleKill', 'EEPROMCIESet', 'EEPROMDACOffsetCIESet', 'EEPROMDriverSet', 'EEPROMINTSet', 'CPUCoreAndBoardSupplyVoltagesGet', 'CPUTemperatureAndFanSpeedGet', 'ActionListGet', 'ActionExtendedListGet', 'APIExtendedListGet', 'APIListGet', 'ControllerStatusListGet', 'ErrorListGet', 'EventListGet', 'GatheringListGet', 'GatheringExtendedListGet', 'GatheringExternalListGet', 'GroupStatusListGet', 'HardwareInternalListGet', 'HardwareDriverAndStageGet', 'ObjectsListGet', 'PositionerErrorListGet', 'PositionerHardwareStatusListGet', 'PositionerDriverStatusListGet', 'ReferencingActionListGet', 'ReferencingSensorListGet', 'GatheringUserDatasGet', 'ControllerMotionKernelPeriodMinMaxGet', 'ControllerMotionKernelPeriodMinMaxReset', 'SocketsStatusGet', 'TestTCP'], 'action_targets': {}, 'metadata': {'repo': 'biocatiit/beamline-control-user', 'repo_url': 'https://github.com/biocatiit/beamline-control-user', 'brand': 'Agilent', 'model': '1260 (BioCon)', 'device_type_cn': '液相色谱仪', 'device_type_en': 'HPLC', 'source_framework': 'BioCon', 'tag_id': '4418', 'tag_name': '液相色谱质谱联用仪', 'tag_name_en': 'LC-MS', 'candidate_score': 1862, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def withValidSocket(self, **kwargs):
        return self.call('withValidSocket', kwargs=kwargs)

    def Send(self, **kwargs):
        return self.call('Send', kwargs=kwargs)

    def TCP_ConnectToServer(self, **kwargs):
        return self.call('TCP_ConnectToServer', kwargs=kwargs)

    def TCP_SetTimeout(self, **kwargs):
        return self.call('TCP_SetTimeout', kwargs=kwargs)

    def TCP_CloseSocket(self, **kwargs):
        return self.call('TCP_CloseSocket', kwargs=kwargs)

    def GetLibraryVersion(self, **kwargs):
        return self.call('GetLibraryVersion', kwargs=kwargs)

    def ControllerMotionKernelTimeLoadGet(self, **kwargs):
        return self.call('ControllerMotionKernelTimeLoadGet', kwargs=kwargs)

    def ControllerStatusGet(self, **kwargs):
        return self.call('ControllerStatusGet', kwargs=kwargs)

    def ControllerStatusStringGet(self, **kwargs):
        return self.call('ControllerStatusStringGet', kwargs=kwargs)

    def ElapsedTimeGet(self, **kwargs):
        return self.call('ElapsedTimeGet', kwargs=kwargs)

    def ErrorStringGet(self, **kwargs):
        return self.call('ErrorStringGet', kwargs=kwargs)

    def FirmwareVersionGet(self, **kwargs):
        return self.call('FirmwareVersionGet', kwargs=kwargs)

    def TCLScriptExecute(self, **kwargs):
        return self.call('TCLScriptExecute', kwargs=kwargs)

    def TCLScriptExecuteAndWait(self, **kwargs):
        return self.call('TCLScriptExecuteAndWait', kwargs=kwargs)

    def TCLScriptExecuteWithPriority(self, **kwargs):
        return self.call('TCLScriptExecuteWithPriority', kwargs=kwargs)

    def TCLScriptKill(self, **kwargs):
        return self.call('TCLScriptKill', kwargs=kwargs)

    def TimerGet(self, **kwargs):
        return self.call('TimerGet', kwargs=kwargs)

    def TimerSet(self, **kwargs):
        return self.call('TimerSet', kwargs=kwargs)

    def Reboot(self, **kwargs):
        return self.call('Reboot', kwargs=kwargs)

    def Login(self, **kwargs):
        return self.call('Login', kwargs=kwargs)

    def CloseAllOtherSockets(self, **kwargs):
        return self.call('CloseAllOtherSockets', kwargs=kwargs)

    def HardwareDateAndTimeGet(self, **kwargs):
        return self.call('HardwareDateAndTimeGet', kwargs=kwargs)

    def HardwareDateAndTimeSet(self, **kwargs):
        return self.call('HardwareDateAndTimeSet', kwargs=kwargs)

    def EventAdd(self, **kwargs):
        return self.call('EventAdd', kwargs=kwargs)

    def EventGet(self, **kwargs):
        return self.call('EventGet', kwargs=kwargs)

    def EventRemove(self, **kwargs):
        return self.call('EventRemove', kwargs=kwargs)

    def EventWait(self, **kwargs):
        return self.call('EventWait', kwargs=kwargs)

    def EventExtendedConfigurationTriggerSet(self, **kwargs):
        return self.call('EventExtendedConfigurationTriggerSet', kwargs=kwargs)

    def EventExtendedConfigurationTriggerGet(self, **kwargs):
        return self.call('EventExtendedConfigurationTriggerGet', kwargs=kwargs)

    def EventExtendedConfigurationActionSet(self, **kwargs):
        return self.call('EventExtendedConfigurationActionSet', kwargs=kwargs)

    def EventExtendedConfigurationActionGet(self, **kwargs):
        return self.call('EventExtendedConfigurationActionGet', kwargs=kwargs)

    def EventExtendedStart(self, **kwargs):
        return self.call('EventExtendedStart', kwargs=kwargs)

    def EventExtendedAllGet(self, **kwargs):
        return self.call('EventExtendedAllGet', kwargs=kwargs)

    def EventExtendedGet(self, **kwargs):
        return self.call('EventExtendedGet', kwargs=kwargs)

    def EventExtendedRemove(self, **kwargs):
        return self.call('EventExtendedRemove', kwargs=kwargs)

    def EventExtendedWait(self, **kwargs):
        return self.call('EventExtendedWait', kwargs=kwargs)

    def GatheringConfigurationGet(self, **kwargs):
        return self.call('GatheringConfigurationGet', kwargs=kwargs)

    def GatheringConfigurationSet(self, **kwargs):
        return self.call('GatheringConfigurationSet', kwargs=kwargs)

    def GatheringCurrentNumberGet(self, **kwargs):
        return self.call('GatheringCurrentNumberGet', kwargs=kwargs)

    def GatheringStopAndSave(self, **kwargs):
        return self.call('GatheringStopAndSave', kwargs=kwargs)

    def GatheringDataAcquire(self, **kwargs):
        return self.call('GatheringDataAcquire', kwargs=kwargs)

    def GatheringDataGet(self, **kwargs):
        return self.call('GatheringDataGet', kwargs=kwargs)

    def GatheringDataMultipleLinesGet(self, **kwargs):
        return self.call('GatheringDataMultipleLinesGet', kwargs=kwargs)

    def GatheringReset(self, **kwargs):
        return self.call('GatheringReset', kwargs=kwargs)

    def GatheringRun(self, **kwargs):
        return self.call('GatheringRun', kwargs=kwargs)

    def GatheringRunAppend(self, **kwargs):
        return self.call('GatheringRunAppend', kwargs=kwargs)

    def GatheringStop(self, **kwargs):
        return self.call('GatheringStop', kwargs=kwargs)

    def GatheringExternalConfigurationSet(self, **kwargs):
        return self.call('GatheringExternalConfigurationSet', kwargs=kwargs)

    def GatheringExternalConfigurationGet(self, **kwargs):
        return self.call('GatheringExternalConfigurationGet', kwargs=kwargs)

    def GatheringExternalCurrentNumberGet(self, **kwargs):
        return self.call('GatheringExternalCurrentNumberGet', kwargs=kwargs)

    def GatheringExternalDataGet(self, **kwargs):
        return self.call('GatheringExternalDataGet', kwargs=kwargs)

    def GatheringExternalStopAndSave(self, **kwargs):
        return self.call('GatheringExternalStopAndSave', kwargs=kwargs)

    def GlobalArrayGet(self, **kwargs):
        return self.call('GlobalArrayGet', kwargs=kwargs)

    def GlobalArraySet(self, **kwargs):
        return self.call('GlobalArraySet', kwargs=kwargs)

    def DoubleGlobalArrayGet(self, **kwargs):
        return self.call('DoubleGlobalArrayGet', kwargs=kwargs)

    def DoubleGlobalArraySet(self, **kwargs):
        return self.call('DoubleGlobalArraySet', kwargs=kwargs)

    def GPIOAnalogGet(self, **kwargs):
        return self.call('GPIOAnalogGet', kwargs=kwargs)

    def GPIOAnalogSet(self, **kwargs):
        return self.call('GPIOAnalogSet', kwargs=kwargs)

    def GPIOAnalogGainGet(self, **kwargs):
        return self.call('GPIOAnalogGainGet', kwargs=kwargs)

    def GPIOAnalogGainSet(self, **kwargs):
        return self.call('GPIOAnalogGainSet', kwargs=kwargs)

    def GPIODigitalGet(self, **kwargs):
        return self.call('GPIODigitalGet', kwargs=kwargs)

    def GPIODigitalSet(self, **kwargs):
        return self.call('GPIODigitalSet', kwargs=kwargs)

    def GroupAccelerationSetpointGet(self, **kwargs):
        return self.call('GroupAccelerationSetpointGet', kwargs=kwargs)

    def GroupAnalogTrackingModeEnable(self, **kwargs):
        return self.call('GroupAnalogTrackingModeEnable', kwargs=kwargs)

    def GroupAnalogTrackingModeDisable(self, **kwargs):
        return self.call('GroupAnalogTrackingModeDisable', kwargs=kwargs)

    def GroupCorrectorOutputGet(self, **kwargs):
        return self.call('GroupCorrectorOutputGet', kwargs=kwargs)

    def GroupCurrentFollowingErrorGet(self, **kwargs):
        return self.call('GroupCurrentFollowingErrorGet', kwargs=kwargs)

    def GroupHomeSearch(self, **kwargs):
        return self.call('GroupHomeSearch', kwargs=kwargs)

    def GroupHomeSearchAndRelativeMove(self, **kwargs):
        return self.call('GroupHomeSearchAndRelativeMove', kwargs=kwargs)

    def GroupInitialize(self, **kwargs):
        return self.call('GroupInitialize', kwargs=kwargs)

    def GroupInitializeWithEncoderCalibration(self, **kwargs):
        return self.call('GroupInitializeWithEncoderCalibration', kwargs=kwargs)

    def GroupJogParametersSet(self, **kwargs):
        return self.call('GroupJogParametersSet', kwargs=kwargs)

    def GroupJogParametersGet(self, **kwargs):
        return self.call('GroupJogParametersGet', kwargs=kwargs)

    def GroupJogCurrentGet(self, **kwargs):
        return self.call('GroupJogCurrentGet', kwargs=kwargs)

    def GroupJogModeEnable(self, **kwargs):
        return self.call('GroupJogModeEnable', kwargs=kwargs)

    def GroupJogModeDisable(self, **kwargs):
        return self.call('GroupJogModeDisable', kwargs=kwargs)

    def GroupKill(self, **kwargs):
        return self.call('GroupKill', kwargs=kwargs)

    def GroupMoveAbort(self, **kwargs):
        return self.call('GroupMoveAbort', kwargs=kwargs)

    def GroupMoveAbsolute(self, **kwargs):
        return self.call('GroupMoveAbsolute', kwargs=kwargs)

    def GroupMoveRelative(self, **kwargs):
        return self.call('GroupMoveRelative', kwargs=kwargs)

    def GroupMotionDisable(self, **kwargs):
        return self.call('GroupMotionDisable', kwargs=kwargs)

    def GroupMotionEnable(self, **kwargs):
        return self.call('GroupMotionEnable', kwargs=kwargs)

    def GroupPositionCorrectedProfilerGet(self, **kwargs):
        return self.call('GroupPositionCorrectedProfilerGet', kwargs=kwargs)

    def GroupPositionCurrentGet(self, **kwargs):
        return self.call('GroupPositionCurrentGet', kwargs=kwargs)

    def GroupPositionPCORawEncoderGet(self, **kwargs):
        return self.call('GroupPositionPCORawEncoderGet', kwargs=kwargs)

    def GroupPositionSetpointGet(self, **kwargs):
        return self.call('GroupPositionSetpointGet', kwargs=kwargs)

    def GroupPositionTargetGet(self, **kwargs):
        return self.call('GroupPositionTargetGet', kwargs=kwargs)

    def GroupReferencingActionExecute(self, **kwargs):
        return self.call('GroupReferencingActionExecute', kwargs=kwargs)

    def GroupReferencingStart(self, **kwargs):
        return self.call('GroupReferencingStart', kwargs=kwargs)

    def GroupReferencingStop(self, **kwargs):
        return self.call('GroupReferencingStop', kwargs=kwargs)

    def GroupStatusGet(self, **kwargs):
        return self.call('GroupStatusGet', kwargs=kwargs)

    def GroupStatusStringGet(self, **kwargs):
        return self.call('GroupStatusStringGet', kwargs=kwargs)

    def GroupVelocityCurrentGet(self, **kwargs):
        return self.call('GroupVelocityCurrentGet', kwargs=kwargs)

    def HexapodMoveAbsolute(self, **kwargs):
        return self.call('HexapodMoveAbsolute', kwargs=kwargs)

    def HexapodMoveRelative(self, **kwargs):
        return self.call('HexapodMoveRelative', kwargs=kwargs)

    def HexapodPositionCurrentGet(self, **kwargs):
        return self.call('HexapodPositionCurrentGet', kwargs=kwargs)

    def KillAll(self, **kwargs):
        return self.call('KillAll', kwargs=kwargs)

    def PositionerAnalogTrackingPositionParametersGet(self, **kwargs):
        return self.call('PositionerAnalogTrackingPositionParametersGet', kwargs=kwargs)

    def PositionerAnalogTrackingPositionParametersSet(self, **kwargs):
        return self.call('PositionerAnalogTrackingPositionParametersSet', kwargs=kwargs)

    def PositionerAnalogTrackingVelocityParametersGet(self, **kwargs):
        return self.call('PositionerAnalogTrackingVelocityParametersGet', kwargs=kwargs)

    def PositionerAnalogTrackingVelocityParametersSet(self, **kwargs):
        return self.call('PositionerAnalogTrackingVelocityParametersSet', kwargs=kwargs)

    def PositionerBacklashGet(self, **kwargs):
        return self.call('PositionerBacklashGet', kwargs=kwargs)

    def PositionerBacklashSet(self, **kwargs):
        return self.call('PositionerBacklashSet', kwargs=kwargs)

    def PositionerBacklashEnable(self, **kwargs):
        return self.call('PositionerBacklashEnable', kwargs=kwargs)

    def PositionerBacklashDisable(self, **kwargs):
        return self.call('PositionerBacklashDisable', kwargs=kwargs)

    def PositionerCorrectorNotchFiltersSet(self, **kwargs):
        return self.call('PositionerCorrectorNotchFiltersSet', kwargs=kwargs)

    def PositionerCorrectorNotchFiltersGet(self, **kwargs):
        return self.call('PositionerCorrectorNotchFiltersGet', kwargs=kwargs)

    def PositionerCorrectorPIDFFAccelerationSet(self, **kwargs):
        return self.call('PositionerCorrectorPIDFFAccelerationSet', kwargs=kwargs)

    def PositionerCorrectorPIDFFAccelerationGet(self, **kwargs):
        return self.call('PositionerCorrectorPIDFFAccelerationGet', kwargs=kwargs)

    def PositionerCorrectorPIDFFVelocitySet(self, **kwargs):
        return self.call('PositionerCorrectorPIDFFVelocitySet', kwargs=kwargs)

    def PositionerCorrectorPIDFFVelocityGet(self, **kwargs):
        return self.call('PositionerCorrectorPIDFFVelocityGet', kwargs=kwargs)

    def PositionerCorrectorPIDDualFFVoltageSet(self, **kwargs):
        return self.call('PositionerCorrectorPIDDualFFVoltageSet', kwargs=kwargs)

    def PositionerCorrectorPIDDualFFVoltageGet(self, **kwargs):
        return self.call('PositionerCorrectorPIDDualFFVoltageGet', kwargs=kwargs)

    def PositionerCorrectorPIPositionSet(self, **kwargs):
        return self.call('PositionerCorrectorPIPositionSet', kwargs=kwargs)

    def PositionerCorrectorPIPositionGet(self, **kwargs):
        return self.call('PositionerCorrectorPIPositionGet', kwargs=kwargs)

    def PositionerCorrectorTypeGet(self, **kwargs):
        return self.call('PositionerCorrectorTypeGet', kwargs=kwargs)

    def PositionerCurrentVelocityAccelerationFiltersGet(self, **kwargs):
        return self.call('PositionerCurrentVelocityAccelerationFiltersGet', kwargs=kwargs)

    def PositionerCurrentVelocityAccelerationFiltersSet(self, **kwargs):
        return self.call('PositionerCurrentVelocityAccelerationFiltersSet', kwargs=kwargs)

    def PositionerDriverFiltersGet(self, **kwargs):
        return self.call('PositionerDriverFiltersGet', kwargs=kwargs)

    def PositionerDriverFiltersSet(self, **kwargs):
        return self.call('PositionerDriverFiltersSet', kwargs=kwargs)

    def PositionerDriverPositionOffsetsGet(self, **kwargs):
        return self.call('PositionerDriverPositionOffsetsGet', kwargs=kwargs)

    def PositionerDriverStatusGet(self, **kwargs):
        return self.call('PositionerDriverStatusGet', kwargs=kwargs)

    def PositionerDriverStatusStringGet(self, **kwargs):
        return self.call('PositionerDriverStatusStringGet', kwargs=kwargs)

    def PositionerEncoderAmplitudeValuesGet(self, **kwargs):
        return self.call('PositionerEncoderAmplitudeValuesGet', kwargs=kwargs)

    def PositionerEncoderCalibrationParametersGet(self, **kwargs):
        return self.call('PositionerEncoderCalibrationParametersGet', kwargs=kwargs)

    def PositionerErrorGet(self, **kwargs):
        return self.call('PositionerErrorGet', kwargs=kwargs)

    def PositionerErrorRead(self, **kwargs):
        return self.call('PositionerErrorRead', kwargs=kwargs)

    def PositionerErrorStringGet(self, **kwargs):
        return self.call('PositionerErrorStringGet', kwargs=kwargs)

    def PositionerExcitationSignalGet(self, **kwargs):
        return self.call('PositionerExcitationSignalGet', kwargs=kwargs)

    def PositionerExcitationSignalSet(self, **kwargs):
        return self.call('PositionerExcitationSignalSet', kwargs=kwargs)

    def PositionerExternalLatchPositionGet(self, **kwargs):
        return self.call('PositionerExternalLatchPositionGet', kwargs=kwargs)

    def PositionerHardwareStatusGet(self, **kwargs):
        return self.call('PositionerHardwareStatusGet', kwargs=kwargs)

    def PositionerHardwareStatusStringGet(self, **kwargs):
        return self.call('PositionerHardwareStatusStringGet', kwargs=kwargs)

    def PositionerHardInterpolatorFactorGet(self, **kwargs):
        return self.call('PositionerHardInterpolatorFactorGet', kwargs=kwargs)

    def PositionerHardInterpolatorFactorSet(self, **kwargs):
        return self.call('PositionerHardInterpolatorFactorSet', kwargs=kwargs)

    def PositionerMaximumVelocityAndAccelerationGet(self, **kwargs):
        return self.call('PositionerMaximumVelocityAndAccelerationGet', kwargs=kwargs)

    def PositionerMotionDoneGet(self, **kwargs):
        return self.call('PositionerMotionDoneGet', kwargs=kwargs)

    def PositionerMotionDoneSet(self, **kwargs):
        return self.call('PositionerMotionDoneSet', kwargs=kwargs)

    def PositionerPositionCompareAquadBAlwaysEnable(self, **kwargs):
        return self.call('PositionerPositionCompareAquadBAlwaysEnable', kwargs=kwargs)

    def PositionerPositionCompareAquadBWindowedGet(self, **kwargs):
        return self.call('PositionerPositionCompareAquadBWindowedGet', kwargs=kwargs)

    def PositionerPositionCompareAquadBWindowedSet(self, **kwargs):
        return self.call('PositionerPositionCompareAquadBWindowedSet', kwargs=kwargs)

    def PositionerPositionCompareGet(self, **kwargs):
        return self.call('PositionerPositionCompareGet', kwargs=kwargs)

    def PositionerPositionCompareSet(self, **kwargs):
        return self.call('PositionerPositionCompareSet', kwargs=kwargs)

    def PositionerPositionCompareEnable(self, **kwargs):
        return self.call('PositionerPositionCompareEnable', kwargs=kwargs)

    def PositionerPositionCompareDisable(self, **kwargs):
        return self.call('PositionerPositionCompareDisable', kwargs=kwargs)

    def PositionerPositionComparePulseParametersGet(self, **kwargs):
        return self.call('PositionerPositionComparePulseParametersGet', kwargs=kwargs)

    def PositionerPositionComparePulseParametersSet(self, **kwargs):
        return self.call('PositionerPositionComparePulseParametersSet', kwargs=kwargs)

    def PositionerRawEncoderPositionGet(self, **kwargs):
        return self.call('PositionerRawEncoderPositionGet', kwargs=kwargs)

    def PositionersEncoderIndexDifferenceGet(self, **kwargs):
        return self.call('PositionersEncoderIndexDifferenceGet', kwargs=kwargs)

    def PositionerSGammaExactVelocityAjustedDisplacementGet(self, **kwargs):
        return self.call('PositionerSGammaExactVelocityAjustedDisplacementGet', kwargs=kwargs)

    def PositionerSGammaParametersGet(self, **kwargs):
        return self.call('PositionerSGammaParametersGet', kwargs=kwargs)

    def PositionerSGammaParametersSet(self, **kwargs):
        return self.call('PositionerSGammaParametersSet', kwargs=kwargs)

    def PositionerSGammaPreviousMotionTimesGet(self, **kwargs):
        return self.call('PositionerSGammaPreviousMotionTimesGet', kwargs=kwargs)

    def PositionerStageParameterGet(self, **kwargs):
        return self.call('PositionerStageParameterGet', kwargs=kwargs)

    def PositionerStageParameterSet(self, **kwargs):
        return self.call('PositionerStageParameterSet', kwargs=kwargs)

    def PositionerTimeFlasherGet(self, **kwargs):
        return self.call('PositionerTimeFlasherGet', kwargs=kwargs)

    def PositionerTimeFlasherSet(self, **kwargs):
        return self.call('PositionerTimeFlasherSet', kwargs=kwargs)

    def PositionerTimeFlasherEnable(self, **kwargs):
        return self.call('PositionerTimeFlasherEnable', kwargs=kwargs)

    def PositionerTimeFlasherDisable(self, **kwargs):
        return self.call('PositionerTimeFlasherDisable', kwargs=kwargs)

    def PositionerUserTravelLimitsGet(self, **kwargs):
        return self.call('PositionerUserTravelLimitsGet', kwargs=kwargs)

    def PositionerUserTravelLimitsSet(self, **kwargs):
        return self.call('PositionerUserTravelLimitsSet', kwargs=kwargs)

    def PositionerDACOffsetGet(self, **kwargs):
        return self.call('PositionerDACOffsetGet', kwargs=kwargs)

    def PositionerDACOffsetSet(self, **kwargs):
        return self.call('PositionerDACOffsetSet', kwargs=kwargs)

    def PositionerDACOffsetDualGet(self, **kwargs):
        return self.call('PositionerDACOffsetDualGet', kwargs=kwargs)

    def PositionerDACOffsetDualSet(self, **kwargs):
        return self.call('PositionerDACOffsetDualSet', kwargs=kwargs)

    def PositionerCorrectorAutoTuning(self, **kwargs):
        return self.call('PositionerCorrectorAutoTuning', kwargs=kwargs)

    def PositionerAccelerationAutoScaling(self, **kwargs):
        return self.call('PositionerAccelerationAutoScaling', kwargs=kwargs)

    def MultipleAxesPVTVerification(self, **kwargs):
        return self.call('MultipleAxesPVTVerification', kwargs=kwargs)

    def MultipleAxesPVTVerificationResultGet(self, **kwargs):
        return self.call('MultipleAxesPVTVerificationResultGet', kwargs=kwargs)

    def MultipleAxesPVTExecution(self, **kwargs):
        return self.call('MultipleAxesPVTExecution', kwargs=kwargs)

    def MultipleAxesPVTParametersGet(self, **kwargs):
        return self.call('MultipleAxesPVTParametersGet', kwargs=kwargs)

    def MultipleAxesPVTPulseOutputSet(self, **kwargs):
        return self.call('MultipleAxesPVTPulseOutputSet', kwargs=kwargs)

    def MultipleAxesPVTPulseOutputGet(self, **kwargs):
        return self.call('MultipleAxesPVTPulseOutputGet', kwargs=kwargs)

    def SingleAxisSlaveModeEnable(self, **kwargs):
        return self.call('SingleAxisSlaveModeEnable', kwargs=kwargs)

    def SingleAxisSlaveModeDisable(self, **kwargs):
        return self.call('SingleAxisSlaveModeDisable', kwargs=kwargs)

    def SingleAxisSlaveParametersSet(self, **kwargs):
        return self.call('SingleAxisSlaveParametersSet', kwargs=kwargs)

    def SingleAxisSlaveParametersGet(self, **kwargs):
        return self.call('SingleAxisSlaveParametersGet', kwargs=kwargs)

    def SpindleSlaveModeEnable(self, **kwargs):
        return self.call('SpindleSlaveModeEnable', kwargs=kwargs)

    def SpindleSlaveModeDisable(self, **kwargs):
        return self.call('SpindleSlaveModeDisable', kwargs=kwargs)

    def SpindleSlaveParametersSet(self, **kwargs):
        return self.call('SpindleSlaveParametersSet', kwargs=kwargs)

    def SpindleSlaveParametersGet(self, **kwargs):
        return self.call('SpindleSlaveParametersGet', kwargs=kwargs)

    def GroupSpinParametersSet(self, **kwargs):
        return self.call('GroupSpinParametersSet', kwargs=kwargs)

    def GroupSpinParametersGet(self, **kwargs):
        return self.call('GroupSpinParametersGet', kwargs=kwargs)

    def GroupSpinCurrentGet(self, **kwargs):
        return self.call('GroupSpinCurrentGet', kwargs=kwargs)

    def GroupSpinModeStop(self, **kwargs):
        return self.call('GroupSpinModeStop', kwargs=kwargs)

    def XYLineArcVerification(self, **kwargs):
        return self.call('XYLineArcVerification', kwargs=kwargs)

    def XYLineArcVerificationResultGet(self, **kwargs):
        return self.call('XYLineArcVerificationResultGet', kwargs=kwargs)

    def XYLineArcExecution(self, **kwargs):
        return self.call('XYLineArcExecution', kwargs=kwargs)

    def XYLineArcParametersGet(self, **kwargs):
        return self.call('XYLineArcParametersGet', kwargs=kwargs)

    def XYLineArcPulseOutputSet(self, **kwargs):
        return self.call('XYLineArcPulseOutputSet', kwargs=kwargs)

    def XYLineArcPulseOutputGet(self, **kwargs):
        return self.call('XYLineArcPulseOutputGet', kwargs=kwargs)

    def XYZGroupPositionCorrectedProfilerGet(self, **kwargs):
        return self.call('XYZGroupPositionCorrectedProfilerGet', kwargs=kwargs)

    def XYZSplineVerification(self, **kwargs):
        return self.call('XYZSplineVerification', kwargs=kwargs)

    def XYZSplineVerificationResultGet(self, **kwargs):
        return self.call('XYZSplineVerificationResultGet', kwargs=kwargs)

    def XYZSplineExecution(self, **kwargs):
        return self.call('XYZSplineExecution', kwargs=kwargs)

    def XYZSplineParametersGet(self, **kwargs):
        return self.call('XYZSplineParametersGet', kwargs=kwargs)

    def OptionalModuleExecute(self, **kwargs):
        return self.call('OptionalModuleExecute', kwargs=kwargs)

    def OptionalModuleKill(self, **kwargs):
        return self.call('OptionalModuleKill', kwargs=kwargs)

    def EEPROMCIESet(self, **kwargs):
        return self.call('EEPROMCIESet', kwargs=kwargs)

    def EEPROMDACOffsetCIESet(self, **kwargs):
        return self.call('EEPROMDACOffsetCIESet', kwargs=kwargs)

    def EEPROMDriverSet(self, **kwargs):
        return self.call('EEPROMDriverSet', kwargs=kwargs)

    def EEPROMINTSet(self, **kwargs):
        return self.call('EEPROMINTSet', kwargs=kwargs)

    def CPUCoreAndBoardSupplyVoltagesGet(self, **kwargs):
        return self.call('CPUCoreAndBoardSupplyVoltagesGet', kwargs=kwargs)

    def CPUTemperatureAndFanSpeedGet(self, **kwargs):
        return self.call('CPUTemperatureAndFanSpeedGet', kwargs=kwargs)

    def ActionListGet(self, **kwargs):
        return self.call('ActionListGet', kwargs=kwargs)

    def ActionExtendedListGet(self, **kwargs):
        return self.call('ActionExtendedListGet', kwargs=kwargs)

    def APIExtendedListGet(self, **kwargs):
        return self.call('APIExtendedListGet', kwargs=kwargs)

    def APIListGet(self, **kwargs):
        return self.call('APIListGet', kwargs=kwargs)

    def ControllerStatusListGet(self, **kwargs):
        return self.call('ControllerStatusListGet', kwargs=kwargs)

    def ErrorListGet(self, **kwargs):
        return self.call('ErrorListGet', kwargs=kwargs)

    def EventListGet(self, **kwargs):
        return self.call('EventListGet', kwargs=kwargs)

    def GatheringListGet(self, **kwargs):
        return self.call('GatheringListGet', kwargs=kwargs)

    def GatheringExtendedListGet(self, **kwargs):
        return self.call('GatheringExtendedListGet', kwargs=kwargs)

    def GatheringExternalListGet(self, **kwargs):
        return self.call('GatheringExternalListGet', kwargs=kwargs)

    def GroupStatusListGet(self, **kwargs):
        return self.call('GroupStatusListGet', kwargs=kwargs)

    def HardwareInternalListGet(self, **kwargs):
        return self.call('HardwareInternalListGet', kwargs=kwargs)

    def HardwareDriverAndStageGet(self, **kwargs):
        return self.call('HardwareDriverAndStageGet', kwargs=kwargs)

    def ObjectsListGet(self, **kwargs):
        return self.call('ObjectsListGet', kwargs=kwargs)

    def PositionerErrorListGet(self, **kwargs):
        return self.call('PositionerErrorListGet', kwargs=kwargs)

    def PositionerHardwareStatusListGet(self, **kwargs):
        return self.call('PositionerHardwareStatusListGet', kwargs=kwargs)

    def PositionerDriverStatusListGet(self, **kwargs):
        return self.call('PositionerDriverStatusListGet', kwargs=kwargs)

    def ReferencingActionListGet(self, **kwargs):
        return self.call('ReferencingActionListGet', kwargs=kwargs)

    def ReferencingSensorListGet(self, **kwargs):
        return self.call('ReferencingSensorListGet', kwargs=kwargs)

    def GatheringUserDatasGet(self, **kwargs):
        return self.call('GatheringUserDatasGet', kwargs=kwargs)

    def ControllerMotionKernelPeriodMinMaxGet(self, **kwargs):
        return self.call('ControllerMotionKernelPeriodMinMaxGet', kwargs=kwargs)

    def ControllerMotionKernelPeriodMinMaxReset(self, **kwargs):
        return self.call('ControllerMotionKernelPeriodMinMaxReset', kwargs=kwargs)

    def SocketsStatusGet(self, **kwargs):
        return self.call('SocketsStatusGet', kwargs=kwargs)

    def TestTCP(self, **kwargs):
        return self.call('TestTCP', kwargs=kwargs)

