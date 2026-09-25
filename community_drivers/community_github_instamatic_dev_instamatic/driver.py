from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubInstamaticDevInstamatic(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/instamatic-dev_instamatic', 'source_file': 'src/instamatic/camera/gatansocket3.py', 'class_name': 'GatanSocket', 'import_roots': [], 'candidate_methods': ['hasScriptFunction', 'connect', 'disconnect', 'reconnect', 'send_data', 'recv_data', 'ExchangeMessages', 'GetLong', 'SendLongGetLong', 'GetDMVersion', 'GetNumberOfCameras', 'GetPluginVersion', 'IsCameraInserted', 'InsertCamera', 'SetReadMode', 'SetShutterNormallyClosed', 'SetK2Parameters', 'setNumGrabSum', 'getNumGrabSum', 'SetupFileSaving'], 'metadata': {'repo': 'instamatic-dev/instamatic', 'repo_url': 'https://github.com/instamatic-dev/instamatic', 'unit_id': 'gh_jeol_jem_2100', 'source_file': 'src/instamatic/camera/gatansocket3.py', 'candidate_score': 138, 'manufacturer': 'JEOL', 'model_name': 'JEOL JEM-2100'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def hasScriptFunction(self, **kwargs):
        return self.call('hasScriptFunction', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def reconnect(self, **kwargs):
        return self.call('reconnect', kwargs=kwargs)

    def send_data(self, **kwargs):
        return self.call('send_data', kwargs=kwargs)

    def recv_data(self, **kwargs):
        return self.call('recv_data', kwargs=kwargs)

    def ExchangeMessages(self, **kwargs):
        return self.call('ExchangeMessages', kwargs=kwargs)

    def GetLong(self, **kwargs):
        return self.call('GetLong', kwargs=kwargs)

    def SendLongGetLong(self, **kwargs):
        return self.call('SendLongGetLong', kwargs=kwargs)

    def GetDMVersion(self, **kwargs):
        return self.call('GetDMVersion', kwargs=kwargs)

    def GetNumberOfCameras(self, **kwargs):
        return self.call('GetNumberOfCameras', kwargs=kwargs)

    def GetPluginVersion(self, **kwargs):
        return self.call('GetPluginVersion', kwargs=kwargs)

    def IsCameraInserted(self, **kwargs):
        return self.call('IsCameraInserted', kwargs=kwargs)

    def InsertCamera(self, **kwargs):
        return self.call('InsertCamera', kwargs=kwargs)

    def SetReadMode(self, **kwargs):
        return self.call('SetReadMode', kwargs=kwargs)

    def SetShutterNormallyClosed(self, **kwargs):
        return self.call('SetShutterNormallyClosed', kwargs=kwargs)

    def SetK2Parameters(self, **kwargs):
        return self.call('SetK2Parameters', kwargs=kwargs)

    def setNumGrabSum(self, **kwargs):
        return self.call('setNumGrabSum', kwargs=kwargs)

    def getNumGrabSum(self, **kwargs):
        return self.call('getNumGrabSum', kwargs=kwargs)

    def SetupFileSaving(self, **kwargs):
        return self.call('SetupFileSaving', kwargs=kwargs)

