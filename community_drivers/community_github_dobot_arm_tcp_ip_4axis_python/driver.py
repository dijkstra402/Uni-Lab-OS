from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubDobotArmTcpIp4axisPython(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/Dobot-Arm_TCP-IP-4Axis-Python', 'source_file': 'dobot_api.py', 'class_name': 'DobotApiDashboard', 'import_roots': [], 'candidate_methods': ['EnableRobot', 'DisableRobot', 'ClearError', 'ResetRobot', 'SpeedFactor', 'User', 'Tool', 'RobotMode', 'PayLoad', 'DO', 'AccJ', 'AccL', 'SpeedJ', 'SpeedL', 'Arch', 'CP', 'LimZ', 'RunScript', 'StopScript', 'PauseScript'], 'metadata': {'repo': 'dobot-arm/tcp-ip-4axis-python', 'repo_url': 'https://github.com/Dobot-Arm/TCP-IP-4Axis-Python', 'unit_id': 'gh_dobot_mg400', 'source_file': 'dobot_api.py', 'candidate_score': 21, 'manufacturer': 'Dobot', 'model_name': 'Dobot MG400 / M1Pro'}}

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

