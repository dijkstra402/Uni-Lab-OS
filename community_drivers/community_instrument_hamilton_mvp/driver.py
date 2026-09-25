from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHamiltonMvp(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/ZhuangLab__storm-control', 'source_file': 'storm_control/sc_hardware/andor/andorcontroller.py', 'class_name': 'AndorCamera', 'import_roots': [], 'candidate_methods': ['closeShutter', 'coolerOff', 'coolerOn', 'getAcquisitionTimings', 'getCameraSize', 'getCurrentSetup', 'getDimensions', 'getHeadModel', 'getHSSpeeds', 'getEMAdvanced', 'getEMGainRange', 'getFrames', 'getImages16', 'getMaxBinning', 'getMaxExposure', 'getMaxIntensity', 'getNumberADChannels', 'getNumberEMGainModes', 'getOldestImage16', 'getPreampGains', 'getProperties', 'getTemperature', 'getTemperatureRange', 'getVSSpeeds', 'goToTemperature', 'openShutter', 'setACQMode', 'setADChannel', 'setBaselineClamp', 'setEMAdvanced', 'setEMCCDGain', 'setEMGainMode', 'setExposureTime', 'setFanMode', 'setFastExtTrigger', 'setFrameTransferMode', 'setHSSpeed', 'setIsolatedCropMode', 'setKineticCycleTime', 'setPreAmpGain', 'setReadMode', 'setROIAndBinning', 'setTriggerMode', 'setTemperature', 'setVSAmplitude', 'setVSSpeed', 'shutdown', 'startAcquisition', 'stopAcquisition'], 'action_targets': {}, 'metadata': {'repo': 'ZhuangLab/storm-control', 'repo_url': 'https://github.com/ZhuangLab/storm-control', 'brand': 'Hamilton', 'model': 'MVP', 'device_type_cn': '多通阀', 'device_type_en': 'Multi-Port Valve', 'source_framework': 'storm-control', 'tag_id': '4382', 'tag_name': '多通阀', 'tag_name_en': 'Multi-Port Valve', 'candidate_score': 438, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def closeShutter(self, **kwargs):
        return self.call('closeShutter', kwargs=kwargs)

    def coolerOff(self, **kwargs):
        return self.call('coolerOff', kwargs=kwargs)

    def coolerOn(self, **kwargs):
        return self.call('coolerOn', kwargs=kwargs)

    def getAcquisitionTimings(self, **kwargs):
        return self.call('getAcquisitionTimings', kwargs=kwargs)

    def getCameraSize(self, **kwargs):
        return self.call('getCameraSize', kwargs=kwargs)

    def getCurrentSetup(self, **kwargs):
        return self.call('getCurrentSetup', kwargs=kwargs)

    def getDimensions(self, **kwargs):
        return self.call('getDimensions', kwargs=kwargs)

    def getHeadModel(self, **kwargs):
        return self.call('getHeadModel', kwargs=kwargs)

    def getHSSpeeds(self, **kwargs):
        return self.call('getHSSpeeds', kwargs=kwargs)

    def getEMAdvanced(self, **kwargs):
        return self.call('getEMAdvanced', kwargs=kwargs)

    def getEMGainRange(self, **kwargs):
        return self.call('getEMGainRange', kwargs=kwargs)

    def getFrames(self, **kwargs):
        return self.call('getFrames', kwargs=kwargs)

    def getImages16(self, **kwargs):
        return self.call('getImages16', kwargs=kwargs)

    def getMaxBinning(self, **kwargs):
        return self.call('getMaxBinning', kwargs=kwargs)

    def getMaxExposure(self, **kwargs):
        return self.call('getMaxExposure', kwargs=kwargs)

    def getMaxIntensity(self, **kwargs):
        return self.call('getMaxIntensity', kwargs=kwargs)

    def getNumberADChannels(self, **kwargs):
        return self.call('getNumberADChannels', kwargs=kwargs)

    def getNumberEMGainModes(self, **kwargs):
        return self.call('getNumberEMGainModes', kwargs=kwargs)

    def getOldestImage16(self, **kwargs):
        return self.call('getOldestImage16', kwargs=kwargs)

    def getPreampGains(self, **kwargs):
        return self.call('getPreampGains', kwargs=kwargs)

    def getProperties(self, **kwargs):
        return self.call('getProperties', kwargs=kwargs)

    def getTemperature(self, **kwargs):
        return self.call('getTemperature', kwargs=kwargs)

    def getTemperatureRange(self, **kwargs):
        return self.call('getTemperatureRange', kwargs=kwargs)

    def getVSSpeeds(self, **kwargs):
        return self.call('getVSSpeeds', kwargs=kwargs)

    def goToTemperature(self, **kwargs):
        return self.call('goToTemperature', kwargs=kwargs)

    def openShutter(self, **kwargs):
        return self.call('openShutter', kwargs=kwargs)

    def setACQMode(self, **kwargs):
        return self.call('setACQMode', kwargs=kwargs)

    def setADChannel(self, **kwargs):
        return self.call('setADChannel', kwargs=kwargs)

    def setBaselineClamp(self, **kwargs):
        return self.call('setBaselineClamp', kwargs=kwargs)

    def setEMAdvanced(self, **kwargs):
        return self.call('setEMAdvanced', kwargs=kwargs)

    def setEMCCDGain(self, **kwargs):
        return self.call('setEMCCDGain', kwargs=kwargs)

    def setEMGainMode(self, **kwargs):
        return self.call('setEMGainMode', kwargs=kwargs)

    def setExposureTime(self, **kwargs):
        return self.call('setExposureTime', kwargs=kwargs)

    def setFanMode(self, **kwargs):
        return self.call('setFanMode', kwargs=kwargs)

    def setFastExtTrigger(self, **kwargs):
        return self.call('setFastExtTrigger', kwargs=kwargs)

    def setFrameTransferMode(self, **kwargs):
        return self.call('setFrameTransferMode', kwargs=kwargs)

    def setHSSpeed(self, **kwargs):
        return self.call('setHSSpeed', kwargs=kwargs)

    def setIsolatedCropMode(self, **kwargs):
        return self.call('setIsolatedCropMode', kwargs=kwargs)

    def setKineticCycleTime(self, **kwargs):
        return self.call('setKineticCycleTime', kwargs=kwargs)

    def setPreAmpGain(self, **kwargs):
        return self.call('setPreAmpGain', kwargs=kwargs)

    def setReadMode(self, **kwargs):
        return self.call('setReadMode', kwargs=kwargs)

    def setROIAndBinning(self, **kwargs):
        return self.call('setROIAndBinning', kwargs=kwargs)

    def setTriggerMode(self, **kwargs):
        return self.call('setTriggerMode', kwargs=kwargs)

    def setTemperature(self, **kwargs):
        return self.call('setTemperature', kwargs=kwargs)

    def setVSAmplitude(self, **kwargs):
        return self.call('setVSAmplitude', kwargs=kwargs)

    def setVSSpeed(self, **kwargs):
        return self.call('setVSSpeed', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

    def startAcquisition(self, **kwargs):
        return self.call('startAcquisition', kwargs=kwargs)

    def stopAcquisition(self, **kwargs):
        return self.call('stopAcquisition', kwargs=kwargs)

