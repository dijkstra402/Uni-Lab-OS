from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubCgohlkeLucam(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/cgohlke_lucam', 'source_file': 'lucam/lucam.py', 'class_name': 'Lucam', 'import_roots': [], 'candidate_methods': ['default_snapshot', 'default_conversion', 'is_little_endian', 'set_properties', 'CameraClose', 'CameraReset', 'QueryVersion', 'QueryExternInterface', 'GetCameraId', 'EnumAvailableFrameRates', 'QueryDisplayFrameRate', 'DisplayPropertyPage', 'DisplayVideoFormatPage', 'CreateDisplayWindow', 'DestroyDisplayWindow', 'AdjustDisplayWindow', 'GetTruePixelDepth', 'GetVideoImageFormat', 'GetLastErrorForCamera', 'SetProperty'], 'metadata': {'repo': 'cgohlke/lucam', 'repo_url': 'https://github.com/cgohlke/lucam', 'unit_id': 'gh_lumenera_lucam', 'source_file': 'lucam/lucam.py', 'candidate_score': 84, 'manufacturer': 'Lumenera', 'model_name': 'Lumenera LuCam'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def default_snapshot(self, **kwargs):
        return self.call('default_snapshot', kwargs=kwargs)

    def default_conversion(self, **kwargs):
        return self.call('default_conversion', kwargs=kwargs)

    def is_little_endian(self, **kwargs):
        return self.call('is_little_endian', kwargs=kwargs)

    def set_properties(self, **kwargs):
        return self.call('set_properties', kwargs=kwargs)

    def CameraClose(self, **kwargs):
        return self.call('CameraClose', kwargs=kwargs)

    def CameraReset(self, **kwargs):
        return self.call('CameraReset', kwargs=kwargs)

    def QueryVersion(self, **kwargs):
        return self.call('QueryVersion', kwargs=kwargs)

    def QueryExternInterface(self, **kwargs):
        return self.call('QueryExternInterface', kwargs=kwargs)

    def GetCameraId(self, **kwargs):
        return self.call('GetCameraId', kwargs=kwargs)

    def EnumAvailableFrameRates(self, **kwargs):
        return self.call('EnumAvailableFrameRates', kwargs=kwargs)

    def QueryDisplayFrameRate(self, **kwargs):
        return self.call('QueryDisplayFrameRate', kwargs=kwargs)

    def DisplayPropertyPage(self, **kwargs):
        return self.call('DisplayPropertyPage', kwargs=kwargs)

    def DisplayVideoFormatPage(self, **kwargs):
        return self.call('DisplayVideoFormatPage', kwargs=kwargs)

    def CreateDisplayWindow(self, **kwargs):
        return self.call('CreateDisplayWindow', kwargs=kwargs)

    def DestroyDisplayWindow(self, **kwargs):
        return self.call('DestroyDisplayWindow', kwargs=kwargs)

    def AdjustDisplayWindow(self, **kwargs):
        return self.call('AdjustDisplayWindow', kwargs=kwargs)

    def GetTruePixelDepth(self, **kwargs):
        return self.call('GetTruePixelDepth', kwargs=kwargs)

    def GetVideoImageFormat(self, **kwargs):
        return self.call('GetVideoImageFormat', kwargs=kwargs)

    def GetLastErrorForCamera(self, **kwargs):
        return self.call('GetLastErrorForCamera', kwargs=kwargs)

    def SetProperty(self, **kwargs):
        return self.call('SetProperty', kwargs=kwargs)

