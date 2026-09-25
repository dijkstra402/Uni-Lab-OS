from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThermoFisherFeiTecnai(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/instamatic-dev__instamatic', 'source_file': 'src/instamatic/microscope/interface/jeol_microscope.py', 'class_name': 'JeolMicroscope', 'import_roots': ['src'], 'candidate_methods': ['setNeutral', 'getHTValue', 'getHTRange', 'getCurrentDensity', 'setBeamValve', 'getBeamValve', 'getCL1', 'getCL2', 'getBrightness', 'setBrightness', 'getMagnification', 'setMagnification', 'getMagnificationIndex', 'getMagnificationAbsoluteIndex', 'setMagnificationIndex', 'increaseMagnificationIndex', 'decreaseMagnificationIndex', 'getMagnificationRanges', 'getGunShift', 'setGunShift', 'getGunTilt', 'setGunTilt', 'getBeamShift', 'setBeamShift', 'getBeamTilt', 'setBeamTilt', 'getImageShift1', 'setImageShift1', 'getImageShift2', 'setImageShift2', 'getStagePosition', 'isStageMoving', 'waitForStage', 'setStageX', 'setStageY', 'setStageZ', 'setStageA', 'setStageB', 'setStageXY', 'stopStage', 'setStagePosition', 'is_goniotool_available', 'getRotationSpeed', 'setRotationSpeed', 'resetStage', 'stopStageMV', 'getFunctionMode', 'setFunctionMode', 'getDiffFocus', 'setDiffFocus', 'setIntermediateLens1', 'getIntermediateLens1', 'getDiffShift', 'setDiffShift', 'release_connection', 'isBeamBlanked', 'setBeamBlank', 'getCondensorLensStigmator', 'setCondensorLensStigmator', 'getIntermediateLensStigmator', 'setIntermediateLensStigmator', 'getObjectiveLensStigmator', 'setObjectiveLensStigmator', 'getSpotSize', 'setSpotSize', 'setProbeMode', 'getProbeMode', 'getScreenPosition', 'setScreenPosition', 'getCondensorLens1', 'getCondensorLens2', 'getCondensorMiniLens', 'getObjectiveLenseCoarse', 'setObjectiveLenseCoarse', 'getObjectiveLenseFine', 'setObjectiveLenseFine', 'getObjectiveMiniLens', 'getAll'], 'action_targets': {}, 'metadata': {'repo': 'instamatic-dev/instamatic', 'repo_url': 'https://github.com/instamatic-dev/instamatic', 'brand': 'Thermo Fisher/FEI', 'model': 'Tecnai', 'device_type_cn': 'TEM', 'device_type_en': 'Transmission Electron Microscope', 'source_framework': '显微镜/成像', 'tag_id': '4456', 'tag_name': '透射电子显微镜', 'tag_name_en': 'Transmission Electron Microscope', 'candidate_score': 690, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def setNeutral(self, **kwargs):
        return self.call('setNeutral', kwargs=kwargs)

    def getHTValue(self, **kwargs):
        return self.call('getHTValue', kwargs=kwargs)

    def getHTRange(self, **kwargs):
        return self.call('getHTRange', kwargs=kwargs)

    def getCurrentDensity(self, **kwargs):
        return self.call('getCurrentDensity', kwargs=kwargs)

    def setBeamValve(self, **kwargs):
        return self.call('setBeamValve', kwargs=kwargs)

    def getBeamValve(self, **kwargs):
        return self.call('getBeamValve', kwargs=kwargs)

    def getCL1(self, **kwargs):
        return self.call('getCL1', kwargs=kwargs)

    def getCL2(self, **kwargs):
        return self.call('getCL2', kwargs=kwargs)

    def getBrightness(self, **kwargs):
        return self.call('getBrightness', kwargs=kwargs)

    def setBrightness(self, **kwargs):
        return self.call('setBrightness', kwargs=kwargs)

    def getMagnification(self, **kwargs):
        return self.call('getMagnification', kwargs=kwargs)

    def setMagnification(self, **kwargs):
        return self.call('setMagnification', kwargs=kwargs)

    def getMagnificationIndex(self, **kwargs):
        return self.call('getMagnificationIndex', kwargs=kwargs)

    def getMagnificationAbsoluteIndex(self, **kwargs):
        return self.call('getMagnificationAbsoluteIndex', kwargs=kwargs)

    def setMagnificationIndex(self, **kwargs):
        return self.call('setMagnificationIndex', kwargs=kwargs)

    def increaseMagnificationIndex(self, **kwargs):
        return self.call('increaseMagnificationIndex', kwargs=kwargs)

    def decreaseMagnificationIndex(self, **kwargs):
        return self.call('decreaseMagnificationIndex', kwargs=kwargs)

    def getMagnificationRanges(self, **kwargs):
        return self.call('getMagnificationRanges', kwargs=kwargs)

    def getGunShift(self, **kwargs):
        return self.call('getGunShift', kwargs=kwargs)

    def setGunShift(self, **kwargs):
        return self.call('setGunShift', kwargs=kwargs)

    def getGunTilt(self, **kwargs):
        return self.call('getGunTilt', kwargs=kwargs)

    def setGunTilt(self, **kwargs):
        return self.call('setGunTilt', kwargs=kwargs)

    def getBeamShift(self, **kwargs):
        return self.call('getBeamShift', kwargs=kwargs)

    def setBeamShift(self, **kwargs):
        return self.call('setBeamShift', kwargs=kwargs)

    def getBeamTilt(self, **kwargs):
        return self.call('getBeamTilt', kwargs=kwargs)

    def setBeamTilt(self, **kwargs):
        return self.call('setBeamTilt', kwargs=kwargs)

    def getImageShift1(self, **kwargs):
        return self.call('getImageShift1', kwargs=kwargs)

    def setImageShift1(self, **kwargs):
        return self.call('setImageShift1', kwargs=kwargs)

    def getImageShift2(self, **kwargs):
        return self.call('getImageShift2', kwargs=kwargs)

    def setImageShift2(self, **kwargs):
        return self.call('setImageShift2', kwargs=kwargs)

    def getStagePosition(self, **kwargs):
        return self.call('getStagePosition', kwargs=kwargs)

    def isStageMoving(self, **kwargs):
        return self.call('isStageMoving', kwargs=kwargs)

    def waitForStage(self, **kwargs):
        return self.call('waitForStage', kwargs=kwargs)

    def setStageX(self, **kwargs):
        return self.call('setStageX', kwargs=kwargs)

    def setStageY(self, **kwargs):
        return self.call('setStageY', kwargs=kwargs)

    def setStageZ(self, **kwargs):
        return self.call('setStageZ', kwargs=kwargs)

    def setStageA(self, **kwargs):
        return self.call('setStageA', kwargs=kwargs)

    def setStageB(self, **kwargs):
        return self.call('setStageB', kwargs=kwargs)

    def setStageXY(self, **kwargs):
        return self.call('setStageXY', kwargs=kwargs)

    def stopStage(self, **kwargs):
        return self.call('stopStage', kwargs=kwargs)

    def setStagePosition(self, **kwargs):
        return self.call('setStagePosition', kwargs=kwargs)

    def is_goniotool_available(self, **kwargs):
        return self.call('is_goniotool_available', kwargs=kwargs)

    def getRotationSpeed(self, **kwargs):
        return self.call('getRotationSpeed', kwargs=kwargs)

    def setRotationSpeed(self, **kwargs):
        return self.call('setRotationSpeed', kwargs=kwargs)

    def resetStage(self, **kwargs):
        return self.call('resetStage', kwargs=kwargs)

    def stopStageMV(self, **kwargs):
        return self.call('stopStageMV', kwargs=kwargs)

    def getFunctionMode(self, **kwargs):
        return self.call('getFunctionMode', kwargs=kwargs)

    def setFunctionMode(self, **kwargs):
        return self.call('setFunctionMode', kwargs=kwargs)

    def getDiffFocus(self, **kwargs):
        return self.call('getDiffFocus', kwargs=kwargs)

    def setDiffFocus(self, **kwargs):
        return self.call('setDiffFocus', kwargs=kwargs)

    def setIntermediateLens1(self, **kwargs):
        return self.call('setIntermediateLens1', kwargs=kwargs)

    def getIntermediateLens1(self, **kwargs):
        return self.call('getIntermediateLens1', kwargs=kwargs)

    def getDiffShift(self, **kwargs):
        return self.call('getDiffShift', kwargs=kwargs)

    def setDiffShift(self, **kwargs):
        return self.call('setDiffShift', kwargs=kwargs)

    def release_connection(self, **kwargs):
        return self.call('release_connection', kwargs=kwargs)

    def isBeamBlanked(self, **kwargs):
        return self.call('isBeamBlanked', kwargs=kwargs)

    def setBeamBlank(self, **kwargs):
        return self.call('setBeamBlank', kwargs=kwargs)

    def getCondensorLensStigmator(self, **kwargs):
        return self.call('getCondensorLensStigmator', kwargs=kwargs)

    def setCondensorLensStigmator(self, **kwargs):
        return self.call('setCondensorLensStigmator', kwargs=kwargs)

    def getIntermediateLensStigmator(self, **kwargs):
        return self.call('getIntermediateLensStigmator', kwargs=kwargs)

    def setIntermediateLensStigmator(self, **kwargs):
        return self.call('setIntermediateLensStigmator', kwargs=kwargs)

    def getObjectiveLensStigmator(self, **kwargs):
        return self.call('getObjectiveLensStigmator', kwargs=kwargs)

    def setObjectiveLensStigmator(self, **kwargs):
        return self.call('setObjectiveLensStigmator', kwargs=kwargs)

    def getSpotSize(self, **kwargs):
        return self.call('getSpotSize', kwargs=kwargs)

    def setSpotSize(self, **kwargs):
        return self.call('setSpotSize', kwargs=kwargs)

    def setProbeMode(self, **kwargs):
        return self.call('setProbeMode', kwargs=kwargs)

    def getProbeMode(self, **kwargs):
        return self.call('getProbeMode', kwargs=kwargs)

    def getScreenPosition(self, **kwargs):
        return self.call('getScreenPosition', kwargs=kwargs)

    def setScreenPosition(self, **kwargs):
        return self.call('setScreenPosition', kwargs=kwargs)

    def getCondensorLens1(self, **kwargs):
        return self.call('getCondensorLens1', kwargs=kwargs)

    def getCondensorLens2(self, **kwargs):
        return self.call('getCondensorLens2', kwargs=kwargs)

    def getCondensorMiniLens(self, **kwargs):
        return self.call('getCondensorMiniLens', kwargs=kwargs)

    def getObjectiveLenseCoarse(self, **kwargs):
        return self.call('getObjectiveLenseCoarse', kwargs=kwargs)

    def setObjectiveLenseCoarse(self, **kwargs):
        return self.call('setObjectiveLenseCoarse', kwargs=kwargs)

    def getObjectiveLenseFine(self, **kwargs):
        return self.call('getObjectiveLenseFine', kwargs=kwargs)

    def setObjectiveLenseFine(self, **kwargs):
        return self.call('setObjectiveLenseFine', kwargs=kwargs)

    def getObjectiveMiniLens(self, **kwargs):
        return self.call('getObjectiveMiniLens', kwargs=kwargs)

    def getAll(self, **kwargs):
        return self.call('getAll', kwargs=kwargs)

