from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubSamhitechMicroeye(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/samhitech_microEye', 'source_file': 'src/microEye/hardware/lasers/io_single_laser.py', 'class_name': 'io_single_laser', 'import_roots': [], 'candidate_methods': ['isOpen', 'setPortName', 'portName', 'setBaudRate', 'baudRate', 'SendCommand', 'OpenCOM', 'CloseCOM', 'GetMaxPower', 'GetReadings', 'GetSettings', 'SetPower', 'GetInfo'], 'metadata': {'repo': 'samhitech/microeye', 'repo_url': 'https://github.com/samhitech/microEye', 'unit_id': 'gh_ids_ueye', 'source_file': 'src/microEye/hardware/lasers/io_single_laser.py', 'candidate_score': 115, 'manufacturer': 'IDS', 'model_name': 'IDS uEye/uEye+'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def isOpen(self, **kwargs):
        return self.call('isOpen', kwargs=kwargs)

    def setPortName(self, **kwargs):
        return self.call('setPortName', kwargs=kwargs)

    def portName(self, **kwargs):
        return self.call('portName', kwargs=kwargs)

    def setBaudRate(self, **kwargs):
        return self.call('setBaudRate', kwargs=kwargs)

    def baudRate(self, **kwargs):
        return self.call('baudRate', kwargs=kwargs)

    def SendCommand(self, **kwargs):
        return self.call('SendCommand', kwargs=kwargs)

    def OpenCOM(self, **kwargs):
        return self.call('OpenCOM', kwargs=kwargs)

    def CloseCOM(self, **kwargs):
        return self.call('CloseCOM', kwargs=kwargs)

    def GetMaxPower(self, **kwargs):
        return self.call('GetMaxPower', kwargs=kwargs)

    def GetReadings(self, **kwargs):
        return self.call('GetReadings', kwargs=kwargs)

    def GetSettings(self, **kwargs):
        return self.call('GetSettings', kwargs=kwargs)

    def SetPower(self, **kwargs):
        return self.call('SetPower', kwargs=kwargs)

    def GetInfo(self, **kwargs):
        return self.call('GetInfo', kwargs=kwargs)

