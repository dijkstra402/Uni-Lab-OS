from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIlluminaHiseq2500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/nygctech__PySeq2500', 'source_file': 'pyseq/dcam.py', 'class_name': 'HamamatsuCamera', 'import_roots': [], 'candidate_methods': ['message', 'captureSetup', 'checkStatus', 'getCameraProperties', 'getFrames', 'saveImage', 'getFocusStack', 'getModelInfo', 'getProperties', 'getPropertyAttribute', 'getPropertyText', 'getPropertyRange', 'getPropertyRW', 'getPropertyValue', 'isCameraProperty', 'newFrames', 'setPropertyValue', 'setTriggerMode', 'setLineBundleHeight', 'setSubArrayMode', 'allocFrame', 'startAcquisition', 'stopAcquisition', 'freeFrames', 'shutdown', 'getFrameCount', 'getFrameInterval', 'get_status', 'startSequence', 'setTriggerModeProperty', 'wait', 'getCapability', 'setTDI', 'setAREA'], 'action_targets': {}, 'metadata': {'repo': 'nygctech/PySeq2500', 'repo_url': 'https://github.com/nygctech/PySeq2500', 'brand': 'Illumina', 'model': 'HiSeq 2500', 'device_type_cn': 'DNA测序仪', 'device_type_en': 'DNA Sequencer', 'source_framework': '生命科学', 'tag_id': '4361', 'tag_name': 'DNA测序仪', 'tag_name_en': 'DNA Sequencer', 'candidate_score': 302, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def message(self, **kwargs):
        return self.call('message', kwargs=kwargs)

    def captureSetup(self, **kwargs):
        return self.call('captureSetup', kwargs=kwargs)

    def checkStatus(self, **kwargs):
        return self.call('checkStatus', kwargs=kwargs)

    def getCameraProperties(self, **kwargs):
        return self.call('getCameraProperties', kwargs=kwargs)

    def getFrames(self, **kwargs):
        return self.call('getFrames', kwargs=kwargs)

    def saveImage(self, **kwargs):
        return self.call('saveImage', kwargs=kwargs)

    def getFocusStack(self, **kwargs):
        return self.call('getFocusStack', kwargs=kwargs)

    def getModelInfo(self, **kwargs):
        return self.call('getModelInfo', kwargs=kwargs)

    def getProperties(self, **kwargs):
        return self.call('getProperties', kwargs=kwargs)

    def getPropertyAttribute(self, **kwargs):
        return self.call('getPropertyAttribute', kwargs=kwargs)

    def getPropertyText(self, **kwargs):
        return self.call('getPropertyText', kwargs=kwargs)

    def getPropertyRange(self, **kwargs):
        return self.call('getPropertyRange', kwargs=kwargs)

    def getPropertyRW(self, **kwargs):
        return self.call('getPropertyRW', kwargs=kwargs)

    def getPropertyValue(self, **kwargs):
        return self.call('getPropertyValue', kwargs=kwargs)

    def isCameraProperty(self, **kwargs):
        return self.call('isCameraProperty', kwargs=kwargs)

    def newFrames(self, **kwargs):
        return self.call('newFrames', kwargs=kwargs)

    def setPropertyValue(self, **kwargs):
        return self.call('setPropertyValue', kwargs=kwargs)

    def setTriggerMode(self, **kwargs):
        return self.call('setTriggerMode', kwargs=kwargs)

    def setLineBundleHeight(self, **kwargs):
        return self.call('setLineBundleHeight', kwargs=kwargs)

    def setSubArrayMode(self, **kwargs):
        return self.call('setSubArrayMode', kwargs=kwargs)

    def allocFrame(self, **kwargs):
        return self.call('allocFrame', kwargs=kwargs)

    def startAcquisition(self, **kwargs):
        return self.call('startAcquisition', kwargs=kwargs)

    def stopAcquisition(self, **kwargs):
        return self.call('stopAcquisition', kwargs=kwargs)

    def freeFrames(self, **kwargs):
        return self.call('freeFrames', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

    def getFrameCount(self, **kwargs):
        return self.call('getFrameCount', kwargs=kwargs)

    def getFrameInterval(self, **kwargs):
        return self.call('getFrameInterval', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def startSequence(self, **kwargs):
        return self.call('startSequence', kwargs=kwargs)

    def setTriggerModeProperty(self, **kwargs):
        return self.call('setTriggerModeProperty', kwargs=kwargs)

    def wait(self, **kwargs):
        return self.call('wait', kwargs=kwargs)

    def getCapability(self, **kwargs):
        return self.call('getCapability', kwargs=kwargs)

    def setTDI(self, **kwargs):
        return self.call('setTDI', kwargs=kwargs)

    def setAREA(self, **kwargs):
        return self.call('setAREA', kwargs=kwargs)

