from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLumeneraLucam(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/cgohlke__lucam', 'source_file': 'lucam/lucam.py', 'class_name': 'Lucam', 'import_roots': [], 'candidate_methods': ['default_snapshot', 'default_conversion', 'is_little_endian', 'set_properties', 'CameraClose', 'CameraReset', 'QueryVersion', 'QueryExternInterface', 'GetCameraId', 'EnumAvailableFrameRates', 'QueryDisplayFrameRate', 'DisplayPropertyPage', 'DisplayVideoFormatPage', 'CreateDisplayWindow', 'DestroyDisplayWindow', 'AdjustDisplayWindow', 'GetTruePixelDepth', 'GetVideoImageFormat', 'GetLastErrorForCamera', 'SetProperty', 'GetProperty', 'PropertyRange', 'GetFormat', 'SetFormat', 'ReadRegister', 'WriteRegister', 'SetTimeout', 'SetTriggerMode', 'TriggerFastFrame', 'CancelTakeFastFrame', 'EnableFastFrames', 'TakeFastFrame', 'ForceTakeFastFrame', 'TakeFastFrameNoTrigger', 'DisableFastFrames', 'TakeSnapshot', 'SaveImage', 'StreamVideoControl', 'TakeVideo', 'TakeVideoEx', 'CancelTakeVideo', 'StreamVideoControlAVI', 'ConvertRawAVIToStdVideo', 'ConvertFrameToRgb24', 'ConvertFrameToRgb32', 'ConvertFrameToRgb48', 'ConvertFrameToGreyscale8', 'ConvertFrameToGreyscale16', 'Setup8bitsLUT', 'Setup8bitsColorLUT', 'SetupCustomMatrix', 'GetCurrentMatrix', 'AddStreamingCallback', 'RemoveStreamingCallback', 'AddSnapshotCallback', 'RemoveSnapshotCallback', 'AddRgbPreviewCallback', 'RemoveRgbPreviewCallback', 'QueryRgbPreviewPixelFormat', 'OneShotAutoExposure', 'OneShotAutoWhiteBalance', 'OneShotAutoWhiteBalanceEx', 'DigitalWhiteBalance', 'LucamDigitalWhiteBalanceEx', 'AdjustWhiteBalanceFromSnapshot', 'OneShotAutoIris', 'ContinuousAutoExposureEnable', 'ContinuousAutoExposureDisable', 'LucamAutoFocusStart', 'LucamAutoFocusWait', 'LucamAutoFocusStop', 'AutoFocusQueryProgress', 'InitAutoLens', 'PermanentBufferRead', 'PermanentBufferWrite', 'GpioRead', 'GpioWrite', 'GpoSelect', 'GpioConfigure', 'Rs232Transmit', 'Rs232Receive', 'AddRs232Callback', 'RemoveRs232Callback'], 'action_targets': {}, 'metadata': {'repo': 'cgohlke/lucam', 'repo_url': 'https://github.com/cgohlke/lucam', 'brand': 'Lumenera', 'model': 'LuCam', 'device_type_cn': '显微镜相机', 'device_type_en': 'Microscope Camera', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 744, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

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

    def GetProperty(self, **kwargs):
        return self.call('GetProperty', kwargs=kwargs)

    def PropertyRange(self, **kwargs):
        return self.call('PropertyRange', kwargs=kwargs)

    def GetFormat(self, **kwargs):
        return self.call('GetFormat', kwargs=kwargs)

    def SetFormat(self, **kwargs):
        return self.call('SetFormat', kwargs=kwargs)

    def ReadRegister(self, **kwargs):
        return self.call('ReadRegister', kwargs=kwargs)

    def WriteRegister(self, **kwargs):
        return self.call('WriteRegister', kwargs=kwargs)

    def SetTimeout(self, **kwargs):
        return self.call('SetTimeout', kwargs=kwargs)

    def SetTriggerMode(self, **kwargs):
        return self.call('SetTriggerMode', kwargs=kwargs)

    def TriggerFastFrame(self, **kwargs):
        return self.call('TriggerFastFrame', kwargs=kwargs)

    def CancelTakeFastFrame(self, **kwargs):
        return self.call('CancelTakeFastFrame', kwargs=kwargs)

    def EnableFastFrames(self, **kwargs):
        return self.call('EnableFastFrames', kwargs=kwargs)

    def TakeFastFrame(self, **kwargs):
        return self.call('TakeFastFrame', kwargs=kwargs)

    def ForceTakeFastFrame(self, **kwargs):
        return self.call('ForceTakeFastFrame', kwargs=kwargs)

    def TakeFastFrameNoTrigger(self, **kwargs):
        return self.call('TakeFastFrameNoTrigger', kwargs=kwargs)

    def DisableFastFrames(self, **kwargs):
        return self.call('DisableFastFrames', kwargs=kwargs)

    def TakeSnapshot(self, **kwargs):
        return self.call('TakeSnapshot', kwargs=kwargs)

    def SaveImage(self, **kwargs):
        return self.call('SaveImage', kwargs=kwargs)

    def StreamVideoControl(self, **kwargs):
        return self.call('StreamVideoControl', kwargs=kwargs)

    def TakeVideo(self, **kwargs):
        return self.call('TakeVideo', kwargs=kwargs)

    def TakeVideoEx(self, **kwargs):
        return self.call('TakeVideoEx', kwargs=kwargs)

    def CancelTakeVideo(self, **kwargs):
        return self.call('CancelTakeVideo', kwargs=kwargs)

    def StreamVideoControlAVI(self, **kwargs):
        return self.call('StreamVideoControlAVI', kwargs=kwargs)

    def ConvertRawAVIToStdVideo(self, **kwargs):
        return self.call('ConvertRawAVIToStdVideo', kwargs=kwargs)

    def ConvertFrameToRgb24(self, **kwargs):
        return self.call('ConvertFrameToRgb24', kwargs=kwargs)

    def ConvertFrameToRgb32(self, **kwargs):
        return self.call('ConvertFrameToRgb32', kwargs=kwargs)

    def ConvertFrameToRgb48(self, **kwargs):
        return self.call('ConvertFrameToRgb48', kwargs=kwargs)

    def ConvertFrameToGreyscale8(self, **kwargs):
        return self.call('ConvertFrameToGreyscale8', kwargs=kwargs)

    def ConvertFrameToGreyscale16(self, **kwargs):
        return self.call('ConvertFrameToGreyscale16', kwargs=kwargs)

    def Setup8bitsLUT(self, **kwargs):
        return self.call('Setup8bitsLUT', kwargs=kwargs)

    def Setup8bitsColorLUT(self, **kwargs):
        return self.call('Setup8bitsColorLUT', kwargs=kwargs)

    def SetupCustomMatrix(self, **kwargs):
        return self.call('SetupCustomMatrix', kwargs=kwargs)

    def GetCurrentMatrix(self, **kwargs):
        return self.call('GetCurrentMatrix', kwargs=kwargs)

    def AddStreamingCallback(self, **kwargs):
        return self.call('AddStreamingCallback', kwargs=kwargs)

    def RemoveStreamingCallback(self, **kwargs):
        return self.call('RemoveStreamingCallback', kwargs=kwargs)

    def AddSnapshotCallback(self, **kwargs):
        return self.call('AddSnapshotCallback', kwargs=kwargs)

    def RemoveSnapshotCallback(self, **kwargs):
        return self.call('RemoveSnapshotCallback', kwargs=kwargs)

    def AddRgbPreviewCallback(self, **kwargs):
        return self.call('AddRgbPreviewCallback', kwargs=kwargs)

    def RemoveRgbPreviewCallback(self, **kwargs):
        return self.call('RemoveRgbPreviewCallback', kwargs=kwargs)

    def QueryRgbPreviewPixelFormat(self, **kwargs):
        return self.call('QueryRgbPreviewPixelFormat', kwargs=kwargs)

    def OneShotAutoExposure(self, **kwargs):
        return self.call('OneShotAutoExposure', kwargs=kwargs)

    def OneShotAutoWhiteBalance(self, **kwargs):
        return self.call('OneShotAutoWhiteBalance', kwargs=kwargs)

    def OneShotAutoWhiteBalanceEx(self, **kwargs):
        return self.call('OneShotAutoWhiteBalanceEx', kwargs=kwargs)

    def DigitalWhiteBalance(self, **kwargs):
        return self.call('DigitalWhiteBalance', kwargs=kwargs)

    def LucamDigitalWhiteBalanceEx(self, **kwargs):
        return self.call('LucamDigitalWhiteBalanceEx', kwargs=kwargs)

    def AdjustWhiteBalanceFromSnapshot(self, **kwargs):
        return self.call('AdjustWhiteBalanceFromSnapshot', kwargs=kwargs)

    def OneShotAutoIris(self, **kwargs):
        return self.call('OneShotAutoIris', kwargs=kwargs)

    def ContinuousAutoExposureEnable(self, **kwargs):
        return self.call('ContinuousAutoExposureEnable', kwargs=kwargs)

    def ContinuousAutoExposureDisable(self, **kwargs):
        return self.call('ContinuousAutoExposureDisable', kwargs=kwargs)

    def LucamAutoFocusStart(self, **kwargs):
        return self.call('LucamAutoFocusStart', kwargs=kwargs)

    def LucamAutoFocusWait(self, **kwargs):
        return self.call('LucamAutoFocusWait', kwargs=kwargs)

    def LucamAutoFocusStop(self, **kwargs):
        return self.call('LucamAutoFocusStop', kwargs=kwargs)

    def AutoFocusQueryProgress(self, **kwargs):
        return self.call('AutoFocusQueryProgress', kwargs=kwargs)

    def InitAutoLens(self, **kwargs):
        return self.call('InitAutoLens', kwargs=kwargs)

    def PermanentBufferRead(self, **kwargs):
        return self.call('PermanentBufferRead', kwargs=kwargs)

    def PermanentBufferWrite(self, **kwargs):
        return self.call('PermanentBufferWrite', kwargs=kwargs)

    def GpioRead(self, **kwargs):
        return self.call('GpioRead', kwargs=kwargs)

    def GpioWrite(self, **kwargs):
        return self.call('GpioWrite', kwargs=kwargs)

    def GpoSelect(self, **kwargs):
        return self.call('GpoSelect', kwargs=kwargs)

    def GpioConfigure(self, **kwargs):
        return self.call('GpioConfigure', kwargs=kwargs)

    def Rs232Transmit(self, **kwargs):
        return self.call('Rs232Transmit', kwargs=kwargs)

    def Rs232Receive(self, **kwargs):
        return self.call('Rs232Receive', kwargs=kwargs)

    def AddRs232Callback(self, **kwargs):
        return self.call('AddRs232Callback', kwargs=kwargs)

    def RemoveRs232Callback(self, **kwargs):
        return self.call('RemoveRs232Callback', kwargs=kwargs)

