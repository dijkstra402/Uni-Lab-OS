from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMecademicMeca500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Mecademic__mecademicpy', 'source_file': 'mecademicpy/robot.py', 'class_name': 'Robot', 'import_roots': [], 'candidate_methods': ['RegisterCallbacks', 'RegisterCallback', 'UnregisterCallbacks', 'UnregisterCallback', 'RunCallbacks', 'Connect', 'Disconnect', 'IsConnected', 'IsControlling', 'IsSynchronousMode', 'IsAllowedToMove', 'SetSynchronousMode', 'Sync', 'SyncCmdQueue', 'ConnectionWatchdog', 'AutoConnectionWatchdog', 'ActivateRobot', 'DeactivateRobot', 'RebootRobot', 'Home', 'ActivateAndHome', 'PauseMotion', 'ResumeMotion', 'ClearMotion', 'MoveJoints', 'MoveJointsRel', 'MoveJointsVel', 'MovePose', 'MoveJump', 'MoveLin', 'MoveLinRelTrf', 'MoveLinRelTRF', 'MoveLinRelWrf', 'MoveLinRelWRF', 'MoveLinVelTrf', 'MoveLinVelTRF', 'MoveLinVelWrf', 'MoveLinVelWRF', 'SetVelTimeout', 'SetConf', 'SetAutoConf', 'SetConfTurn', 'SetAutoConfTurn', 'SetBlending', 'SetCartAcc', 'SetCartAngVel', 'SetCartLinVel', 'SetJointAcc', 'SetJointVel', 'SetJointVelLimit', 'SetMoveMode', 'SetMoveDurationCfg', 'SetMoveDuration', 'SetMoveJumpHeight', 'SetMoveJumpApproachVel', 'SetTrf', 'SetTRF', 'SetWrf', 'SetWRF', 'SetCheckpoint', 'ExpectExternalCheckpoint', 'WaitGripperMoveCompletion', 'GripperOpen', 'GripperClose', 'MoveGripper', 'SetGripperForce', 'SetGripperVel', 'SetGripperRange', 'SetValveState', 'VacuumGrip', 'VacuumGrip_Immediate', 'VacuumRelease', 'VacuumRelease_Immediate', 'VacuumPurge', 'VacuumPurge_Immediate', 'WaitHoldingPart', 'WaitReleasedPart', 'WaitPurgeDone', 'SetVacuumThreshold', 'SetVacuumThreshold_Immediate', 'SetVacuumPurgeDuration', 'SetVacuumPurgeDuration_Immediate', 'SetOutputState', 'SetOutputState_Immediate', 'WaitForAnyCheckpoint', 'WaitConnected', 'WaitDisconnected', 'WaitActivated', 'WaitDeactivated', 'WaitHomed', 'WaitSimActivated', 'WaitSimDeactivated', 'WaitExtToolSimActivated', 'WaitExtToolSimDeactivated', 'WaitIoSimEnabled', 'WaitIoSimDisabled', 'IsDesiredOutputState', 'WaitOutputState', 'IsDesiredInputState', 'WaitInputState', 'WaitRecoveryMode', 'WaitForError', 'WaitErrorReset', 'WaitPStop2Reset', 'WaitPStop2Resettable', 'WaitEStopReset', 'WaitEStopResettable', 'WaitEstopResettable', 'WaitSafetyStopReset', 'WaitSafetyStopResettable', 'WaitSafetyStopStateChange', 'WaitMotionResumed', 'WaitMotionPaused', 'WaitMotionCleared', 'WaitEndOfCycle', 'WaitIdle', 'ResetError', 'ResetPStop', 'ResetPStop2', 'Delay', 'sleep', 'SendCustomCommand', 'GetInterruptableEvent', 'StartProgram', 'StartOfflineProgram', 'StopProgram', 'ListFiles', 'ListPrograms', 'LoadFile', 'LoadProgram', 'SaveFile', 'SaveProgram', 'DeleteFile', 'DeleteProgram', 'SetLoadedPrograms', 'WaitProgramsLoaded', 'WaitMecaScriptEngineReady', 'GetNetworkCfg', 'GetNetworkConfig', 'SetNetworkOptions', 'GetNetworkOptions', 'GetRobotRtData', 'GetRtAccelerometer', 'GetRtExtToolStatus', 'GetRtIoStatus', 'GetRtGripperForce', 'GetRtGripperPos', 'GetRtGripperState', 'GetRtValveState', 'GetRtOutputState', 'GetRtInputState', 'GetRtVacuumState', 'GetRtVacuumPressure', 'GetRtTargetJointPos', 'GetJoints', 'GetRtJointPos', 'GetRtTargetJointTorq', 'GetRtJointTorq', 'GetRtTargetJointVel', 'GetRtJointVel', 'GetRtTargetCartPos', 'GetPose', 'GetRtCartPos', 'GetRtTargetCartVel', 'GetRtCartVel', 'GetRtTargetConf', 'GetRtConf', 'GetRtTargetConfTurn', 'GetRtConfTurn', 'GetRtTrf', 'GetTrf', 'GetRtWrf', 'GetWrf', 'GetRtTemperature', 'GetRtI2t', 'SetEob', 'SetEom', 'SetMonitoringInterval', 'SetRealTimeMonitoring', 'ForceRealTimeMonitoring', 'SetRtc', 'SetRTC', 'ActivateSim', 'DeactivateSim', 'SetExtToolSim', 'SetIoSim', 'SetRecoveryMode', 'SetTimeScaling', 'SetJointLimitsCfg', 'SetJointLimits', 'SetWorkZoneCfg', 'SetWorkZoneLimits', 'SetCollisionCfg', 'SetToolSphere', 'SetTorqueLimitsCfg', 'SetTorqueLimits', 'SetPayload', 'SetCalibrationCfg', 'SetPStop2Cfg', 'SetSimModeCfg', 'SetMecaScriptCfg', 'SetRobotName', 'ActivateBrakes', 'BrakesOn', 'BrakesOff', 'WaitProgramDone', 'GetPowerSupplyInputs', 'GetAutoConf', 'GetAutoConfTurn', 'GetBlending', 'GetBrakesState', 'GetCalibrationCfg', 'GetCartAcc', 'GetCartAngVel', 'GetCartLinVel', 'GetCheckpoint', 'GetCheckpointDiscarded', 'GetCmdPendingCount', 'GetCollisionCfg', 'GetCollisionStatus', 'GetConf', 'GetConfTurn', 'GetEtherNetIpEnabled', 'GetExtToolFwVersion', 'GetExtToolSim', 'GetFwVersion', 'GetGripperForce', 'GetGripperRange', 'GetGripperVel', 'GetIoSim', 'GetJointAcc', 'GetJointLimits', 'GetJointLimitsCfg', 'GetJointVel', 'GetJointVelLimit', 'GetModelJointLimits', 'GetMonitoringInterval', 'GetMoveDuration', 'GetMoveDurationCfg', 'GetMoveJumpApproachVel', 'GetMoveJumpHeight', 'GetMoveMode', 'GetOperationMode', 'GetPStop2Cfg', 'GetPayload', 'GetProductType', 'GetProfinetEnabled', 'GetRealTimeMonitoring', 'GetRecoveryMode', 'GetRobotCalibrated', 'GetRobotInfo', 'GetRobotName', 'GetRobotSerial', 'GetRtc', 'GetStatusRobot', 'GetSafetyStatus', 'GetSafetyStopStatus', 'GetLoadedPrograms', 'GetProgramExecutionStatus', 'GetMecaScriptEngineStatus', 'GetSimModeCfg', 'GetMecaScriptCfg', 'GetTimeScaling', 'GetToolSphere', 'GetTorqueLimits', 'GetTorqueLimitsCfg', 'GetTorqueLimitsStatus', 'GetVacuumPurgeDuration', 'GetVacuumThreshold', 'GetVelTimeout', 'GetWorkZoneCfg', 'GetWorkZoneLimits', 'GetWorkZoneStatus', 'LogTrace', 'LogUserCommands', 'SetSilentApiMode', 'StartLogging', 'EndLogging', 'GetCapturedTrajectory', 'GetCapturedTrajectoryPath', 'FileLogger', 'TcpDump', 'TcpDumpStop', 'UpdateRobot', 'CreateVariable', 'CreateRegisteredVariable', 'DeleteVariable', 'SetVariable', 'GetVariable', 'GetVariableByCyclicId', 'ListVariables', 'EnableEtherNetIp', 'EnableProfinet', 'SwitchToEtherCAT', 'SetApiLock', 'ApiUnlock', 'GetStatusGripper', 'IsDesiredIoState', 'WaitIOState', 'WaitPStop2ResetDeprecated', 'WaitPStop2ResettableDeprecated', 'WaitEStopResetDeprecated', 'WaitEStopResettableDeprecated', 'ResetPStop2Deprecated', 'VacuumGripReleaseImmediate', 'DeleteAllVariables'], 'action_targets': {}, 'metadata': {'repo': 'Mecademic/mecademicpy', 'repo_url': 'https://github.com/Mecademic/mecademicpy', 'brand': 'Mecademic', 'model': 'Meca500', 'device_type_cn': '桌面机械臂', 'device_type_en': 'Desktop Robot', 'source_framework': 'mecademicpy', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 2426, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def RegisterCallbacks(self, **kwargs):
        return self.call('RegisterCallbacks', kwargs=kwargs)

    def RegisterCallback(self, **kwargs):
        return self.call('RegisterCallback', kwargs=kwargs)

    def UnregisterCallbacks(self, **kwargs):
        return self.call('UnregisterCallbacks', kwargs=kwargs)

    def UnregisterCallback(self, **kwargs):
        return self.call('UnregisterCallback', kwargs=kwargs)

    def RunCallbacks(self, **kwargs):
        return self.call('RunCallbacks', kwargs=kwargs)

    def Connect(self, **kwargs):
        return self.call('Connect', kwargs=kwargs)

    def Disconnect(self, **kwargs):
        return self.call('Disconnect', kwargs=kwargs)

    def IsConnected(self, **kwargs):
        return self.call('IsConnected', kwargs=kwargs)

    def IsControlling(self, **kwargs):
        return self.call('IsControlling', kwargs=kwargs)

    def IsSynchronousMode(self, **kwargs):
        return self.call('IsSynchronousMode', kwargs=kwargs)

    def IsAllowedToMove(self, **kwargs):
        return self.call('IsAllowedToMove', kwargs=kwargs)

    def SetSynchronousMode(self, **kwargs):
        return self.call('SetSynchronousMode', kwargs=kwargs)

    def Sync(self, **kwargs):
        return self.call('Sync', kwargs=kwargs)

    def SyncCmdQueue(self, **kwargs):
        return self.call('SyncCmdQueue', kwargs=kwargs)

    def ConnectionWatchdog(self, **kwargs):
        return self.call('ConnectionWatchdog', kwargs=kwargs)

    def AutoConnectionWatchdog(self, **kwargs):
        return self.call('AutoConnectionWatchdog', kwargs=kwargs)

    def ActivateRobot(self, **kwargs):
        return self.call('ActivateRobot', kwargs=kwargs)

    def DeactivateRobot(self, **kwargs):
        return self.call('DeactivateRobot', kwargs=kwargs)

    def RebootRobot(self, **kwargs):
        return self.call('RebootRobot', kwargs=kwargs)

    def Home(self, **kwargs):
        return self.call('Home', kwargs=kwargs)

    def ActivateAndHome(self, **kwargs):
        return self.call('ActivateAndHome', kwargs=kwargs)

    def PauseMotion(self, **kwargs):
        return self.call('PauseMotion', kwargs=kwargs)

    def ResumeMotion(self, **kwargs):
        return self.call('ResumeMotion', kwargs=kwargs)

    def ClearMotion(self, **kwargs):
        return self.call('ClearMotion', kwargs=kwargs)

    def MoveJoints(self, **kwargs):
        return self.call('MoveJoints', kwargs=kwargs)

    def MoveJointsRel(self, **kwargs):
        return self.call('MoveJointsRel', kwargs=kwargs)

    def MoveJointsVel(self, **kwargs):
        return self.call('MoveJointsVel', kwargs=kwargs)

    def MovePose(self, **kwargs):
        return self.call('MovePose', kwargs=kwargs)

    def MoveJump(self, **kwargs):
        return self.call('MoveJump', kwargs=kwargs)

    def MoveLin(self, **kwargs):
        return self.call('MoveLin', kwargs=kwargs)

    def MoveLinRelTrf(self, **kwargs):
        return self.call('MoveLinRelTrf', kwargs=kwargs)

    def MoveLinRelTRF(self, **kwargs):
        return self.call('MoveLinRelTRF', kwargs=kwargs)

    def MoveLinRelWrf(self, **kwargs):
        return self.call('MoveLinRelWrf', kwargs=kwargs)

    def MoveLinRelWRF(self, **kwargs):
        return self.call('MoveLinRelWRF', kwargs=kwargs)

    def MoveLinVelTrf(self, **kwargs):
        return self.call('MoveLinVelTrf', kwargs=kwargs)

    def MoveLinVelTRF(self, **kwargs):
        return self.call('MoveLinVelTRF', kwargs=kwargs)

    def MoveLinVelWrf(self, **kwargs):
        return self.call('MoveLinVelWrf', kwargs=kwargs)

    def MoveLinVelWRF(self, **kwargs):
        return self.call('MoveLinVelWRF', kwargs=kwargs)

    def SetVelTimeout(self, **kwargs):
        return self.call('SetVelTimeout', kwargs=kwargs)

    def SetConf(self, **kwargs):
        return self.call('SetConf', kwargs=kwargs)

    def SetAutoConf(self, **kwargs):
        return self.call('SetAutoConf', kwargs=kwargs)

    def SetConfTurn(self, **kwargs):
        return self.call('SetConfTurn', kwargs=kwargs)

    def SetAutoConfTurn(self, **kwargs):
        return self.call('SetAutoConfTurn', kwargs=kwargs)

    def SetBlending(self, **kwargs):
        return self.call('SetBlending', kwargs=kwargs)

    def SetCartAcc(self, **kwargs):
        return self.call('SetCartAcc', kwargs=kwargs)

    def SetCartAngVel(self, **kwargs):
        return self.call('SetCartAngVel', kwargs=kwargs)

    def SetCartLinVel(self, **kwargs):
        return self.call('SetCartLinVel', kwargs=kwargs)

    def SetJointAcc(self, **kwargs):
        return self.call('SetJointAcc', kwargs=kwargs)

    def SetJointVel(self, **kwargs):
        return self.call('SetJointVel', kwargs=kwargs)

    def SetJointVelLimit(self, **kwargs):
        return self.call('SetJointVelLimit', kwargs=kwargs)

    def SetMoveMode(self, **kwargs):
        return self.call('SetMoveMode', kwargs=kwargs)

    def SetMoveDurationCfg(self, **kwargs):
        return self.call('SetMoveDurationCfg', kwargs=kwargs)

    def SetMoveDuration(self, **kwargs):
        return self.call('SetMoveDuration', kwargs=kwargs)

    def SetMoveJumpHeight(self, **kwargs):
        return self.call('SetMoveJumpHeight', kwargs=kwargs)

    def SetMoveJumpApproachVel(self, **kwargs):
        return self.call('SetMoveJumpApproachVel', kwargs=kwargs)

    def SetTrf(self, **kwargs):
        return self.call('SetTrf', kwargs=kwargs)

    def SetTRF(self, **kwargs):
        return self.call('SetTRF', kwargs=kwargs)

    def SetWrf(self, **kwargs):
        return self.call('SetWrf', kwargs=kwargs)

    def SetWRF(self, **kwargs):
        return self.call('SetWRF', kwargs=kwargs)

    def SetCheckpoint(self, **kwargs):
        return self.call('SetCheckpoint', kwargs=kwargs)

    def ExpectExternalCheckpoint(self, **kwargs):
        return self.call('ExpectExternalCheckpoint', kwargs=kwargs)

    def WaitGripperMoveCompletion(self, **kwargs):
        return self.call('WaitGripperMoveCompletion', kwargs=kwargs)

    def GripperOpen(self, **kwargs):
        return self.call('GripperOpen', kwargs=kwargs)

    def GripperClose(self, **kwargs):
        return self.call('GripperClose', kwargs=kwargs)

    def MoveGripper(self, **kwargs):
        return self.call('MoveGripper', kwargs=kwargs)

    def SetGripperForce(self, **kwargs):
        return self.call('SetGripperForce', kwargs=kwargs)

    def SetGripperVel(self, **kwargs):
        return self.call('SetGripperVel', kwargs=kwargs)

    def SetGripperRange(self, **kwargs):
        return self.call('SetGripperRange', kwargs=kwargs)

    def SetValveState(self, **kwargs):
        return self.call('SetValveState', kwargs=kwargs)

    def VacuumGrip(self, **kwargs):
        return self.call('VacuumGrip', kwargs=kwargs)

    def VacuumGrip_Immediate(self, **kwargs):
        return self.call('VacuumGrip_Immediate', kwargs=kwargs)

    def VacuumRelease(self, **kwargs):
        return self.call('VacuumRelease', kwargs=kwargs)

    def VacuumRelease_Immediate(self, **kwargs):
        return self.call('VacuumRelease_Immediate', kwargs=kwargs)

    def VacuumPurge(self, **kwargs):
        return self.call('VacuumPurge', kwargs=kwargs)

    def VacuumPurge_Immediate(self, **kwargs):
        return self.call('VacuumPurge_Immediate', kwargs=kwargs)

    def WaitHoldingPart(self, **kwargs):
        return self.call('WaitHoldingPart', kwargs=kwargs)

    def WaitReleasedPart(self, **kwargs):
        return self.call('WaitReleasedPart', kwargs=kwargs)

    def WaitPurgeDone(self, **kwargs):
        return self.call('WaitPurgeDone', kwargs=kwargs)

    def SetVacuumThreshold(self, **kwargs):
        return self.call('SetVacuumThreshold', kwargs=kwargs)

    def SetVacuumThreshold_Immediate(self, **kwargs):
        return self.call('SetVacuumThreshold_Immediate', kwargs=kwargs)

    def SetVacuumPurgeDuration(self, **kwargs):
        return self.call('SetVacuumPurgeDuration', kwargs=kwargs)

    def SetVacuumPurgeDuration_Immediate(self, **kwargs):
        return self.call('SetVacuumPurgeDuration_Immediate', kwargs=kwargs)

    def SetOutputState(self, **kwargs):
        return self.call('SetOutputState', kwargs=kwargs)

    def SetOutputState_Immediate(self, **kwargs):
        return self.call('SetOutputState_Immediate', kwargs=kwargs)

    def WaitForAnyCheckpoint(self, **kwargs):
        return self.call('WaitForAnyCheckpoint', kwargs=kwargs)

    def WaitConnected(self, **kwargs):
        return self.call('WaitConnected', kwargs=kwargs)

    def WaitDisconnected(self, **kwargs):
        return self.call('WaitDisconnected', kwargs=kwargs)

    def WaitActivated(self, **kwargs):
        return self.call('WaitActivated', kwargs=kwargs)

    def WaitDeactivated(self, **kwargs):
        return self.call('WaitDeactivated', kwargs=kwargs)

    def WaitHomed(self, **kwargs):
        return self.call('WaitHomed', kwargs=kwargs)

    def WaitSimActivated(self, **kwargs):
        return self.call('WaitSimActivated', kwargs=kwargs)

    def WaitSimDeactivated(self, **kwargs):
        return self.call('WaitSimDeactivated', kwargs=kwargs)

    def WaitExtToolSimActivated(self, **kwargs):
        return self.call('WaitExtToolSimActivated', kwargs=kwargs)

    def WaitExtToolSimDeactivated(self, **kwargs):
        return self.call('WaitExtToolSimDeactivated', kwargs=kwargs)

    def WaitIoSimEnabled(self, **kwargs):
        return self.call('WaitIoSimEnabled', kwargs=kwargs)

    def WaitIoSimDisabled(self, **kwargs):
        return self.call('WaitIoSimDisabled', kwargs=kwargs)

    def IsDesiredOutputState(self, **kwargs):
        return self.call('IsDesiredOutputState', kwargs=kwargs)

    def WaitOutputState(self, **kwargs):
        return self.call('WaitOutputState', kwargs=kwargs)

    def IsDesiredInputState(self, **kwargs):
        return self.call('IsDesiredInputState', kwargs=kwargs)

    def WaitInputState(self, **kwargs):
        return self.call('WaitInputState', kwargs=kwargs)

    def WaitRecoveryMode(self, **kwargs):
        return self.call('WaitRecoveryMode', kwargs=kwargs)

    def WaitForError(self, **kwargs):
        return self.call('WaitForError', kwargs=kwargs)

    def WaitErrorReset(self, **kwargs):
        return self.call('WaitErrorReset', kwargs=kwargs)

    def WaitPStop2Reset(self, **kwargs):
        return self.call('WaitPStop2Reset', kwargs=kwargs)

    def WaitPStop2Resettable(self, **kwargs):
        return self.call('WaitPStop2Resettable', kwargs=kwargs)

    def WaitEStopReset(self, **kwargs):
        return self.call('WaitEStopReset', kwargs=kwargs)

    def WaitEStopResettable(self, **kwargs):
        return self.call('WaitEStopResettable', kwargs=kwargs)

    def WaitEstopResettable(self, **kwargs):
        return self.call('WaitEstopResettable', kwargs=kwargs)

    def WaitSafetyStopReset(self, **kwargs):
        return self.call('WaitSafetyStopReset', kwargs=kwargs)

    def WaitSafetyStopResettable(self, **kwargs):
        return self.call('WaitSafetyStopResettable', kwargs=kwargs)

    def WaitSafetyStopStateChange(self, **kwargs):
        return self.call('WaitSafetyStopStateChange', kwargs=kwargs)

    def WaitMotionResumed(self, **kwargs):
        return self.call('WaitMotionResumed', kwargs=kwargs)

    def WaitMotionPaused(self, **kwargs):
        return self.call('WaitMotionPaused', kwargs=kwargs)

    def WaitMotionCleared(self, **kwargs):
        return self.call('WaitMotionCleared', kwargs=kwargs)

    def WaitEndOfCycle(self, **kwargs):
        return self.call('WaitEndOfCycle', kwargs=kwargs)

    def WaitIdle(self, **kwargs):
        return self.call('WaitIdle', kwargs=kwargs)

    def ResetError(self, **kwargs):
        return self.call('ResetError', kwargs=kwargs)

    def ResetPStop(self, **kwargs):
        return self.call('ResetPStop', kwargs=kwargs)

    def ResetPStop2(self, **kwargs):
        return self.call('ResetPStop2', kwargs=kwargs)

    def Delay(self, **kwargs):
        return self.call('Delay', kwargs=kwargs)

    def sleep(self, **kwargs):
        return self.call('sleep', kwargs=kwargs)

    def SendCustomCommand(self, **kwargs):
        return self.call('SendCustomCommand', kwargs=kwargs)

    def GetInterruptableEvent(self, **kwargs):
        return self.call('GetInterruptableEvent', kwargs=kwargs)

    def StartProgram(self, **kwargs):
        return self.call('StartProgram', kwargs=kwargs)

    def StartOfflineProgram(self, **kwargs):
        return self.call('StartOfflineProgram', kwargs=kwargs)

    def StopProgram(self, **kwargs):
        return self.call('StopProgram', kwargs=kwargs)

    def ListFiles(self, **kwargs):
        return self.call('ListFiles', kwargs=kwargs)

    def ListPrograms(self, **kwargs):
        return self.call('ListPrograms', kwargs=kwargs)

    def LoadFile(self, **kwargs):
        return self.call('LoadFile', kwargs=kwargs)

    def LoadProgram(self, **kwargs):
        return self.call('LoadProgram', kwargs=kwargs)

    def SaveFile(self, **kwargs):
        return self.call('SaveFile', kwargs=kwargs)

    def SaveProgram(self, **kwargs):
        return self.call('SaveProgram', kwargs=kwargs)

    def DeleteFile(self, **kwargs):
        return self.call('DeleteFile', kwargs=kwargs)

    def DeleteProgram(self, **kwargs):
        return self.call('DeleteProgram', kwargs=kwargs)

    def SetLoadedPrograms(self, **kwargs):
        return self.call('SetLoadedPrograms', kwargs=kwargs)

    def WaitProgramsLoaded(self, **kwargs):
        return self.call('WaitProgramsLoaded', kwargs=kwargs)

    def WaitMecaScriptEngineReady(self, **kwargs):
        return self.call('WaitMecaScriptEngineReady', kwargs=kwargs)

    def GetNetworkCfg(self, **kwargs):
        return self.call('GetNetworkCfg', kwargs=kwargs)

    def GetNetworkConfig(self, **kwargs):
        return self.call('GetNetworkConfig', kwargs=kwargs)

    def SetNetworkOptions(self, **kwargs):
        return self.call('SetNetworkOptions', kwargs=kwargs)

    def GetNetworkOptions(self, **kwargs):
        return self.call('GetNetworkOptions', kwargs=kwargs)

    def GetRobotRtData(self, **kwargs):
        return self.call('GetRobotRtData', kwargs=kwargs)

    def GetRtAccelerometer(self, **kwargs):
        return self.call('GetRtAccelerometer', kwargs=kwargs)

    def GetRtExtToolStatus(self, **kwargs):
        return self.call('GetRtExtToolStatus', kwargs=kwargs)

    def GetRtIoStatus(self, **kwargs):
        return self.call('GetRtIoStatus', kwargs=kwargs)

    def GetRtGripperForce(self, **kwargs):
        return self.call('GetRtGripperForce', kwargs=kwargs)

    def GetRtGripperPos(self, **kwargs):
        return self.call('GetRtGripperPos', kwargs=kwargs)

    def GetRtGripperState(self, **kwargs):
        return self.call('GetRtGripperState', kwargs=kwargs)

    def GetRtValveState(self, **kwargs):
        return self.call('GetRtValveState', kwargs=kwargs)

    def GetRtOutputState(self, **kwargs):
        return self.call('GetRtOutputState', kwargs=kwargs)

    def GetRtInputState(self, **kwargs):
        return self.call('GetRtInputState', kwargs=kwargs)

    def GetRtVacuumState(self, **kwargs):
        return self.call('GetRtVacuumState', kwargs=kwargs)

    def GetRtVacuumPressure(self, **kwargs):
        return self.call('GetRtVacuumPressure', kwargs=kwargs)

    def GetRtTargetJointPos(self, **kwargs):
        return self.call('GetRtTargetJointPos', kwargs=kwargs)

    def GetJoints(self, **kwargs):
        return self.call('GetJoints', kwargs=kwargs)

    def GetRtJointPos(self, **kwargs):
        return self.call('GetRtJointPos', kwargs=kwargs)

    def GetRtTargetJointTorq(self, **kwargs):
        return self.call('GetRtTargetJointTorq', kwargs=kwargs)

    def GetRtJointTorq(self, **kwargs):
        return self.call('GetRtJointTorq', kwargs=kwargs)

    def GetRtTargetJointVel(self, **kwargs):
        return self.call('GetRtTargetJointVel', kwargs=kwargs)

    def GetRtJointVel(self, **kwargs):
        return self.call('GetRtJointVel', kwargs=kwargs)

    def GetRtTargetCartPos(self, **kwargs):
        return self.call('GetRtTargetCartPos', kwargs=kwargs)

    def GetPose(self, **kwargs):
        return self.call('GetPose', kwargs=kwargs)

    def GetRtCartPos(self, **kwargs):
        return self.call('GetRtCartPos', kwargs=kwargs)

    def GetRtTargetCartVel(self, **kwargs):
        return self.call('GetRtTargetCartVel', kwargs=kwargs)

    def GetRtCartVel(self, **kwargs):
        return self.call('GetRtCartVel', kwargs=kwargs)

    def GetRtTargetConf(self, **kwargs):
        return self.call('GetRtTargetConf', kwargs=kwargs)

    def GetRtConf(self, **kwargs):
        return self.call('GetRtConf', kwargs=kwargs)

    def GetRtTargetConfTurn(self, **kwargs):
        return self.call('GetRtTargetConfTurn', kwargs=kwargs)

    def GetRtConfTurn(self, **kwargs):
        return self.call('GetRtConfTurn', kwargs=kwargs)

    def GetRtTrf(self, **kwargs):
        return self.call('GetRtTrf', kwargs=kwargs)

    def GetTrf(self, **kwargs):
        return self.call('GetTrf', kwargs=kwargs)

    def GetRtWrf(self, **kwargs):
        return self.call('GetRtWrf', kwargs=kwargs)

    def GetWrf(self, **kwargs):
        return self.call('GetWrf', kwargs=kwargs)

    def GetRtTemperature(self, **kwargs):
        return self.call('GetRtTemperature', kwargs=kwargs)

    def GetRtI2t(self, **kwargs):
        return self.call('GetRtI2t', kwargs=kwargs)

    def SetEob(self, **kwargs):
        return self.call('SetEob', kwargs=kwargs)

    def SetEom(self, **kwargs):
        return self.call('SetEom', kwargs=kwargs)

    def SetMonitoringInterval(self, **kwargs):
        return self.call('SetMonitoringInterval', kwargs=kwargs)

    def SetRealTimeMonitoring(self, **kwargs):
        return self.call('SetRealTimeMonitoring', kwargs=kwargs)

    def ForceRealTimeMonitoring(self, **kwargs):
        return self.call('ForceRealTimeMonitoring', kwargs=kwargs)

    def SetRtc(self, **kwargs):
        return self.call('SetRtc', kwargs=kwargs)

    def SetRTC(self, **kwargs):
        return self.call('SetRTC', kwargs=kwargs)

    def ActivateSim(self, **kwargs):
        return self.call('ActivateSim', kwargs=kwargs)

    def DeactivateSim(self, **kwargs):
        return self.call('DeactivateSim', kwargs=kwargs)

    def SetExtToolSim(self, **kwargs):
        return self.call('SetExtToolSim', kwargs=kwargs)

    def SetIoSim(self, **kwargs):
        return self.call('SetIoSim', kwargs=kwargs)

    def SetRecoveryMode(self, **kwargs):
        return self.call('SetRecoveryMode', kwargs=kwargs)

    def SetTimeScaling(self, **kwargs):
        return self.call('SetTimeScaling', kwargs=kwargs)

    def SetJointLimitsCfg(self, **kwargs):
        return self.call('SetJointLimitsCfg', kwargs=kwargs)

    def SetJointLimits(self, **kwargs):
        return self.call('SetJointLimits', kwargs=kwargs)

    def SetWorkZoneCfg(self, **kwargs):
        return self.call('SetWorkZoneCfg', kwargs=kwargs)

    def SetWorkZoneLimits(self, **kwargs):
        return self.call('SetWorkZoneLimits', kwargs=kwargs)

    def SetCollisionCfg(self, **kwargs):
        return self.call('SetCollisionCfg', kwargs=kwargs)

    def SetToolSphere(self, **kwargs):
        return self.call('SetToolSphere', kwargs=kwargs)

    def SetTorqueLimitsCfg(self, **kwargs):
        return self.call('SetTorqueLimitsCfg', kwargs=kwargs)

    def SetTorqueLimits(self, **kwargs):
        return self.call('SetTorqueLimits', kwargs=kwargs)

    def SetPayload(self, **kwargs):
        return self.call('SetPayload', kwargs=kwargs)

    def SetCalibrationCfg(self, **kwargs):
        return self.call('SetCalibrationCfg', kwargs=kwargs)

    def SetPStop2Cfg(self, **kwargs):
        return self.call('SetPStop2Cfg', kwargs=kwargs)

    def SetSimModeCfg(self, **kwargs):
        return self.call('SetSimModeCfg', kwargs=kwargs)

    def SetMecaScriptCfg(self, **kwargs):
        return self.call('SetMecaScriptCfg', kwargs=kwargs)

    def SetRobotName(self, **kwargs):
        return self.call('SetRobotName', kwargs=kwargs)

    def ActivateBrakes(self, **kwargs):
        return self.call('ActivateBrakes', kwargs=kwargs)

    def BrakesOn(self, **kwargs):
        return self.call('BrakesOn', kwargs=kwargs)

    def BrakesOff(self, **kwargs):
        return self.call('BrakesOff', kwargs=kwargs)

    def WaitProgramDone(self, **kwargs):
        return self.call('WaitProgramDone', kwargs=kwargs)

    def GetPowerSupplyInputs(self, **kwargs):
        return self.call('GetPowerSupplyInputs', kwargs=kwargs)

    def GetAutoConf(self, **kwargs):
        return self.call('GetAutoConf', kwargs=kwargs)

    def GetAutoConfTurn(self, **kwargs):
        return self.call('GetAutoConfTurn', kwargs=kwargs)

    def GetBlending(self, **kwargs):
        return self.call('GetBlending', kwargs=kwargs)

    def GetBrakesState(self, **kwargs):
        return self.call('GetBrakesState', kwargs=kwargs)

    def GetCalibrationCfg(self, **kwargs):
        return self.call('GetCalibrationCfg', kwargs=kwargs)

    def GetCartAcc(self, **kwargs):
        return self.call('GetCartAcc', kwargs=kwargs)

    def GetCartAngVel(self, **kwargs):
        return self.call('GetCartAngVel', kwargs=kwargs)

    def GetCartLinVel(self, **kwargs):
        return self.call('GetCartLinVel', kwargs=kwargs)

    def GetCheckpoint(self, **kwargs):
        return self.call('GetCheckpoint', kwargs=kwargs)

    def GetCheckpointDiscarded(self, **kwargs):
        return self.call('GetCheckpointDiscarded', kwargs=kwargs)

    def GetCmdPendingCount(self, **kwargs):
        return self.call('GetCmdPendingCount', kwargs=kwargs)

    def GetCollisionCfg(self, **kwargs):
        return self.call('GetCollisionCfg', kwargs=kwargs)

    def GetCollisionStatus(self, **kwargs):
        return self.call('GetCollisionStatus', kwargs=kwargs)

    def GetConf(self, **kwargs):
        return self.call('GetConf', kwargs=kwargs)

    def GetConfTurn(self, **kwargs):
        return self.call('GetConfTurn', kwargs=kwargs)

    def GetEtherNetIpEnabled(self, **kwargs):
        return self.call('GetEtherNetIpEnabled', kwargs=kwargs)

    def GetExtToolFwVersion(self, **kwargs):
        return self.call('GetExtToolFwVersion', kwargs=kwargs)

    def GetExtToolSim(self, **kwargs):
        return self.call('GetExtToolSim', kwargs=kwargs)

    def GetFwVersion(self, **kwargs):
        return self.call('GetFwVersion', kwargs=kwargs)

    def GetGripperForce(self, **kwargs):
        return self.call('GetGripperForce', kwargs=kwargs)

    def GetGripperRange(self, **kwargs):
        return self.call('GetGripperRange', kwargs=kwargs)

    def GetGripperVel(self, **kwargs):
        return self.call('GetGripperVel', kwargs=kwargs)

    def GetIoSim(self, **kwargs):
        return self.call('GetIoSim', kwargs=kwargs)

    def GetJointAcc(self, **kwargs):
        return self.call('GetJointAcc', kwargs=kwargs)

    def GetJointLimits(self, **kwargs):
        return self.call('GetJointLimits', kwargs=kwargs)

    def GetJointLimitsCfg(self, **kwargs):
        return self.call('GetJointLimitsCfg', kwargs=kwargs)

    def GetJointVel(self, **kwargs):
        return self.call('GetJointVel', kwargs=kwargs)

    def GetJointVelLimit(self, **kwargs):
        return self.call('GetJointVelLimit', kwargs=kwargs)

    def GetModelJointLimits(self, **kwargs):
        return self.call('GetModelJointLimits', kwargs=kwargs)

    def GetMonitoringInterval(self, **kwargs):
        return self.call('GetMonitoringInterval', kwargs=kwargs)

    def GetMoveDuration(self, **kwargs):
        return self.call('GetMoveDuration', kwargs=kwargs)

    def GetMoveDurationCfg(self, **kwargs):
        return self.call('GetMoveDurationCfg', kwargs=kwargs)

    def GetMoveJumpApproachVel(self, **kwargs):
        return self.call('GetMoveJumpApproachVel', kwargs=kwargs)

    def GetMoveJumpHeight(self, **kwargs):
        return self.call('GetMoveJumpHeight', kwargs=kwargs)

    def GetMoveMode(self, **kwargs):
        return self.call('GetMoveMode', kwargs=kwargs)

    def GetOperationMode(self, **kwargs):
        return self.call('GetOperationMode', kwargs=kwargs)

    def GetPStop2Cfg(self, **kwargs):
        return self.call('GetPStop2Cfg', kwargs=kwargs)

    def GetPayload(self, **kwargs):
        return self.call('GetPayload', kwargs=kwargs)

    def GetProductType(self, **kwargs):
        return self.call('GetProductType', kwargs=kwargs)

    def GetProfinetEnabled(self, **kwargs):
        return self.call('GetProfinetEnabled', kwargs=kwargs)

    def GetRealTimeMonitoring(self, **kwargs):
        return self.call('GetRealTimeMonitoring', kwargs=kwargs)

    def GetRecoveryMode(self, **kwargs):
        return self.call('GetRecoveryMode', kwargs=kwargs)

    def GetRobotCalibrated(self, **kwargs):
        return self.call('GetRobotCalibrated', kwargs=kwargs)

    def GetRobotInfo(self, **kwargs):
        return self.call('GetRobotInfo', kwargs=kwargs)

    def GetRobotName(self, **kwargs):
        return self.call('GetRobotName', kwargs=kwargs)

    def GetRobotSerial(self, **kwargs):
        return self.call('GetRobotSerial', kwargs=kwargs)

    def GetRtc(self, **kwargs):
        return self.call('GetRtc', kwargs=kwargs)

    def GetStatusRobot(self, **kwargs):
        return self.call('GetStatusRobot', kwargs=kwargs)

    def GetSafetyStatus(self, **kwargs):
        return self.call('GetSafetyStatus', kwargs=kwargs)

    def GetSafetyStopStatus(self, **kwargs):
        return self.call('GetSafetyStopStatus', kwargs=kwargs)

    def GetLoadedPrograms(self, **kwargs):
        return self.call('GetLoadedPrograms', kwargs=kwargs)

    def GetProgramExecutionStatus(self, **kwargs):
        return self.call('GetProgramExecutionStatus', kwargs=kwargs)

    def GetMecaScriptEngineStatus(self, **kwargs):
        return self.call('GetMecaScriptEngineStatus', kwargs=kwargs)

    def GetSimModeCfg(self, **kwargs):
        return self.call('GetSimModeCfg', kwargs=kwargs)

    def GetMecaScriptCfg(self, **kwargs):
        return self.call('GetMecaScriptCfg', kwargs=kwargs)

    def GetTimeScaling(self, **kwargs):
        return self.call('GetTimeScaling', kwargs=kwargs)

    def GetToolSphere(self, **kwargs):
        return self.call('GetToolSphere', kwargs=kwargs)

    def GetTorqueLimits(self, **kwargs):
        return self.call('GetTorqueLimits', kwargs=kwargs)

    def GetTorqueLimitsCfg(self, **kwargs):
        return self.call('GetTorqueLimitsCfg', kwargs=kwargs)

    def GetTorqueLimitsStatus(self, **kwargs):
        return self.call('GetTorqueLimitsStatus', kwargs=kwargs)

    def GetVacuumPurgeDuration(self, **kwargs):
        return self.call('GetVacuumPurgeDuration', kwargs=kwargs)

    def GetVacuumThreshold(self, **kwargs):
        return self.call('GetVacuumThreshold', kwargs=kwargs)

    def GetVelTimeout(self, **kwargs):
        return self.call('GetVelTimeout', kwargs=kwargs)

    def GetWorkZoneCfg(self, **kwargs):
        return self.call('GetWorkZoneCfg', kwargs=kwargs)

    def GetWorkZoneLimits(self, **kwargs):
        return self.call('GetWorkZoneLimits', kwargs=kwargs)

    def GetWorkZoneStatus(self, **kwargs):
        return self.call('GetWorkZoneStatus', kwargs=kwargs)

    def LogTrace(self, **kwargs):
        return self.call('LogTrace', kwargs=kwargs)

    def LogUserCommands(self, **kwargs):
        return self.call('LogUserCommands', kwargs=kwargs)

    def SetSilentApiMode(self, **kwargs):
        return self.call('SetSilentApiMode', kwargs=kwargs)

    def StartLogging(self, **kwargs):
        return self.call('StartLogging', kwargs=kwargs)

    def EndLogging(self, **kwargs):
        return self.call('EndLogging', kwargs=kwargs)

    def GetCapturedTrajectory(self, **kwargs):
        return self.call('GetCapturedTrajectory', kwargs=kwargs)

    def GetCapturedTrajectoryPath(self, **kwargs):
        return self.call('GetCapturedTrajectoryPath', kwargs=kwargs)

    def FileLogger(self, **kwargs):
        return self.call('FileLogger', kwargs=kwargs)

    def TcpDump(self, **kwargs):
        return self.call('TcpDump', kwargs=kwargs)

    def TcpDumpStop(self, **kwargs):
        return self.call('TcpDumpStop', kwargs=kwargs)

    def UpdateRobot(self, **kwargs):
        return self.call('UpdateRobot', kwargs=kwargs)

    def CreateVariable(self, **kwargs):
        return self.call('CreateVariable', kwargs=kwargs)

    def CreateRegisteredVariable(self, **kwargs):
        return self.call('CreateRegisteredVariable', kwargs=kwargs)

    def DeleteVariable(self, **kwargs):
        return self.call('DeleteVariable', kwargs=kwargs)

    def SetVariable(self, **kwargs):
        return self.call('SetVariable', kwargs=kwargs)

    def GetVariable(self, **kwargs):
        return self.call('GetVariable', kwargs=kwargs)

    def GetVariableByCyclicId(self, **kwargs):
        return self.call('GetVariableByCyclicId', kwargs=kwargs)

    def ListVariables(self, **kwargs):
        return self.call('ListVariables', kwargs=kwargs)

    def EnableEtherNetIp(self, **kwargs):
        return self.call('EnableEtherNetIp', kwargs=kwargs)

    def EnableProfinet(self, **kwargs):
        return self.call('EnableProfinet', kwargs=kwargs)

    def SwitchToEtherCAT(self, **kwargs):
        return self.call('SwitchToEtherCAT', kwargs=kwargs)

    def SetApiLock(self, **kwargs):
        return self.call('SetApiLock', kwargs=kwargs)

    def ApiUnlock(self, **kwargs):
        return self.call('ApiUnlock', kwargs=kwargs)

    def GetStatusGripper(self, **kwargs):
        return self.call('GetStatusGripper', kwargs=kwargs)

    def IsDesiredIoState(self, **kwargs):
        return self.call('IsDesiredIoState', kwargs=kwargs)

    def WaitIOState(self, **kwargs):
        return self.call('WaitIOState', kwargs=kwargs)

    def WaitPStop2ResetDeprecated(self, **kwargs):
        return self.call('WaitPStop2ResetDeprecated', kwargs=kwargs)

    def WaitPStop2ResettableDeprecated(self, **kwargs):
        return self.call('WaitPStop2ResettableDeprecated', kwargs=kwargs)

    def WaitEStopResetDeprecated(self, **kwargs):
        return self.call('WaitEStopResetDeprecated', kwargs=kwargs)

    def WaitEStopResettableDeprecated(self, **kwargs):
        return self.call('WaitEStopResettableDeprecated', kwargs=kwargs)

    def ResetPStop2Deprecated(self, **kwargs):
        return self.call('ResetPStop2Deprecated', kwargs=kwargs)

    def VacuumGripReleaseImmediate(self, **kwargs):
        return self.call('VacuumGripReleaseImmediate', kwargs=kwargs)

    def DeleteAllVariables(self, **kwargs):
        return self.call('DeleteAllVariables', kwargs=kwargs)

