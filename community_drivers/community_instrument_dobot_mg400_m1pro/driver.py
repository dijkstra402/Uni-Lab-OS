from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentDobotMg400M1pro(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Dobot-Arm__TCP-IP-4Axis-Python', 'source_file': 'dobot_api.py', 'class_name': 'DobotApiDashboard', 'import_roots': [], 'candidate_methods': ['EnableRobot', 'DisableRobot', 'ClearError', 'ResetRobot', 'SpeedFactor', 'User', 'Tool', 'RobotMode', 'PayLoad', 'DO', 'AccJ', 'AccL', 'SpeedJ', 'SpeedL', 'Arch', 'CP', 'LimZ', 'RunScript', 'StopScript', 'PauseScript', 'ContinueScript', 'GetHoldRegs', 'SetHoldRegs', 'GetErrorID', 'DOExecute', 'ToolDO', 'ToolDOExecute', 'SetArmOrientation', 'SetPayload', 'PositiveSolution', 'InverseSolution', 'SetCollisionLevel', 'GetAngle', 'GetPose', 'EmergencyStop', 'ModbusCreate', 'ModbusClose', 'GetInBits', 'GetInRegs', 'GetCoils', 'SetCoils', 'DI', 'ToolDI', 'DOGroup', 'BrakeControl', 'StartDrag', 'StopDrag', 'LoadSwitch', 'wait', 'pause', 'Continue', 'log', 'send_data', 'wait_reply', 'sendRecvMsg'], 'action_targets': {}, 'metadata': {'repo': 'Dobot-Arm/TCP-IP-4Axis-Python', 'repo_url': 'https://github.com/Dobot-Arm/TCP-IP-4Axis-Python', 'brand': 'Dobot', 'model': 'MG400 / M1Pro', 'device_type_cn': '桌面协作机械臂', 'device_type_en': 'Desktop Collaborative Robot', 'source_framework': '机器人/运动控制', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 458, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def EnableRobot(self, **kwargs):
        return self.call('EnableRobot', kwargs=kwargs)

    def DisableRobot(self, **kwargs):
        return self.call('DisableRobot', kwargs=kwargs)

    def ClearError(self, **kwargs):
        return self.call('ClearError', kwargs=kwargs)

    def ResetRobot(self, **kwargs):
        return self.call('ResetRobot', kwargs=kwargs)

    def SpeedFactor(self, **kwargs):
        return self.call('SpeedFactor', kwargs=kwargs)

    def User(self, **kwargs):
        return self.call('User', kwargs=kwargs)

    def Tool(self, **kwargs):
        return self.call('Tool', kwargs=kwargs)

    def RobotMode(self, **kwargs):
        return self.call('RobotMode', kwargs=kwargs)

    def PayLoad(self, **kwargs):
        return self.call('PayLoad', kwargs=kwargs)

    def DO(self, **kwargs):
        return self.call('DO', kwargs=kwargs)

    def AccJ(self, **kwargs):
        return self.call('AccJ', kwargs=kwargs)

    def AccL(self, **kwargs):
        return self.call('AccL', kwargs=kwargs)

    def SpeedJ(self, **kwargs):
        return self.call('SpeedJ', kwargs=kwargs)

    def SpeedL(self, **kwargs):
        return self.call('SpeedL', kwargs=kwargs)

    def Arch(self, **kwargs):
        return self.call('Arch', kwargs=kwargs)

    def CP(self, **kwargs):
        return self.call('CP', kwargs=kwargs)

    def LimZ(self, **kwargs):
        return self.call('LimZ', kwargs=kwargs)

    def RunScript(self, **kwargs):
        return self.call('RunScript', kwargs=kwargs)

    def StopScript(self, **kwargs):
        return self.call('StopScript', kwargs=kwargs)

    def PauseScript(self, **kwargs):
        return self.call('PauseScript', kwargs=kwargs)

    def ContinueScript(self, **kwargs):
        return self.call('ContinueScript', kwargs=kwargs)

    def GetHoldRegs(self, **kwargs):
        return self.call('GetHoldRegs', kwargs=kwargs)

    def SetHoldRegs(self, **kwargs):
        return self.call('SetHoldRegs', kwargs=kwargs)

    def GetErrorID(self, **kwargs):
        return self.call('GetErrorID', kwargs=kwargs)

    def DOExecute(self, **kwargs):
        return self.call('DOExecute', kwargs=kwargs)

    def ToolDO(self, **kwargs):
        return self.call('ToolDO', kwargs=kwargs)

    def ToolDOExecute(self, **kwargs):
        return self.call('ToolDOExecute', kwargs=kwargs)

    def SetArmOrientation(self, **kwargs):
        return self.call('SetArmOrientation', kwargs=kwargs)

    def SetPayload(self, **kwargs):
        return self.call('SetPayload', kwargs=kwargs)

    def PositiveSolution(self, **kwargs):
        return self.call('PositiveSolution', kwargs=kwargs)

    def InverseSolution(self, **kwargs):
        return self.call('InverseSolution', kwargs=kwargs)

    def SetCollisionLevel(self, **kwargs):
        return self.call('SetCollisionLevel', kwargs=kwargs)

    def GetAngle(self, **kwargs):
        return self.call('GetAngle', kwargs=kwargs)

    def GetPose(self, **kwargs):
        return self.call('GetPose', kwargs=kwargs)

    def EmergencyStop(self, **kwargs):
        return self.call('EmergencyStop', kwargs=kwargs)

    def ModbusCreate(self, **kwargs):
        return self.call('ModbusCreate', kwargs=kwargs)

    def ModbusClose(self, **kwargs):
        return self.call('ModbusClose', kwargs=kwargs)

    def GetInBits(self, **kwargs):
        return self.call('GetInBits', kwargs=kwargs)

    def GetInRegs(self, **kwargs):
        return self.call('GetInRegs', kwargs=kwargs)

    def GetCoils(self, **kwargs):
        return self.call('GetCoils', kwargs=kwargs)

    def SetCoils(self, **kwargs):
        return self.call('SetCoils', kwargs=kwargs)

    def DI(self, **kwargs):
        return self.call('DI', kwargs=kwargs)

    def ToolDI(self, **kwargs):
        return self.call('ToolDI', kwargs=kwargs)

    def DOGroup(self, **kwargs):
        return self.call('DOGroup', kwargs=kwargs)

    def BrakeControl(self, **kwargs):
        return self.call('BrakeControl', kwargs=kwargs)

    def StartDrag(self, **kwargs):
        return self.call('StartDrag', kwargs=kwargs)

    def StopDrag(self, **kwargs):
        return self.call('StopDrag', kwargs=kwargs)

    def LoadSwitch(self, **kwargs):
        return self.call('LoadSwitch', kwargs=kwargs)

    def wait(self, **kwargs):
        return self.call('wait', kwargs=kwargs)

    def pause(self, **kwargs):
        return self.call('pause', kwargs=kwargs)

    def Continue(self, **kwargs):
        return self.call('Continue', kwargs=kwargs)

    def log(self, **kwargs):
        return self.call('log', kwargs=kwargs)

    def send_data(self, **kwargs):
        return self.call('send_data', kwargs=kwargs)

    def wait_reply(self, **kwargs):
        return self.call('wait_reply', kwargs=kwargs)

    def sendRecvMsg(self, **kwargs):
        return self.call('sendRecvMsg', kwargs=kwargs)

