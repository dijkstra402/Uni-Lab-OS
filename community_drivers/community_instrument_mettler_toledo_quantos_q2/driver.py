from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMettlerToledoQuantosQ2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/cooper-group-uol-robotics__mettler_toledo_quantos_q2', 'source_file': 'mettler_toledo_quantos_q2_driver/src/mettler_toledo_quantos_q2_driver/quantos_serial_driver.py', 'class_name': 'QuantosDriverSerial', 'import_roots': [], 'candidate_methods': ['setTimeout', 'catchResponse', 'startDosing', 'stopDosing', 'getFrontDoorPos', 'getSamplerPos', 'getHeadData', 'getSampleData', 'moveDosingHeadPin', 'moveFrontDoor', 'moveSampler', 'setTappingBeforeDosing', 'setTappingWhileDosing', 'setTapperIntensity', 'setTapperDuration', 'setTargetValue', 'setTolerance', 'setToleranceMode', 'setSampleID', 'setValuePan', 'setAlgorithm', 'setAntiStatic'], 'action_targets': {}, 'metadata': {'repo': 'cooper-group-uol-robotics/mettler_toledo_quantos_q2', 'repo_url': 'https://github.com/cooper-group-uol-robotics/mettler_toledo_quantos_q2', 'brand': 'Mettler Toledo', 'model': 'Quantos Q2', 'device_type_cn': '自动称量', 'device_type_en': 'Automated Weighing', 'source_framework': '反应器/合成设备', 'tag_id': '4426', 'tag_name': '电子天平', 'tag_name_en': 'Electronic Balance', 'candidate_score': 250, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def setTimeout(self, **kwargs):
        return self.call('setTimeout', kwargs=kwargs)

    def catchResponse(self, **kwargs):
        return self.call('catchResponse', kwargs=kwargs)

    def startDosing(self, **kwargs):
        return self.call('startDosing', kwargs=kwargs)

    def stopDosing(self, **kwargs):
        return self.call('stopDosing', kwargs=kwargs)

    def getFrontDoorPos(self, **kwargs):
        return self.call('getFrontDoorPos', kwargs=kwargs)

    def getSamplerPos(self, **kwargs):
        return self.call('getSamplerPos', kwargs=kwargs)

    def getHeadData(self, **kwargs):
        return self.call('getHeadData', kwargs=kwargs)

    def getSampleData(self, **kwargs):
        return self.call('getSampleData', kwargs=kwargs)

    def moveDosingHeadPin(self, **kwargs):
        return self.call('moveDosingHeadPin', kwargs=kwargs)

    def moveFrontDoor(self, **kwargs):
        return self.call('moveFrontDoor', kwargs=kwargs)

    def moveSampler(self, **kwargs):
        return self.call('moveSampler', kwargs=kwargs)

    def setTappingBeforeDosing(self, **kwargs):
        return self.call('setTappingBeforeDosing', kwargs=kwargs)

    def setTappingWhileDosing(self, **kwargs):
        return self.call('setTappingWhileDosing', kwargs=kwargs)

    def setTapperIntensity(self, **kwargs):
        return self.call('setTapperIntensity', kwargs=kwargs)

    def setTapperDuration(self, **kwargs):
        return self.call('setTapperDuration', kwargs=kwargs)

    def setTargetValue(self, **kwargs):
        return self.call('setTargetValue', kwargs=kwargs)

    def setTolerance(self, **kwargs):
        return self.call('setTolerance', kwargs=kwargs)

    def setToleranceMode(self, **kwargs):
        return self.call('setToleranceMode', kwargs=kwargs)

    def setSampleID(self, **kwargs):
        return self.call('setSampleID', kwargs=kwargs)

    def setValuePan(self, **kwargs):
        return self.call('setValuePan', kwargs=kwargs)

    def setAlgorithm(self, **kwargs):
        return self.call('setAlgorithm', kwargs=kwargs)

    def setAntiStatic(self, **kwargs):
        return self.call('setAntiStatic', kwargs=kwargs)

