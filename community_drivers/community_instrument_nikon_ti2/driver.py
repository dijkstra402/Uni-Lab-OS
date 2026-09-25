from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentNikonTi2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/pymmcore-plus__pymmcore-plus', 'source_file': 'src/pymmcore_plus/experimental/unicore/core/_unicore.py', 'class_name': 'UniMMCore', 'import_roots': ['src'], 'candidate_methods': ['loadSystemConfiguration', 'saveSystemConfiguration', 'loadDevice', 'loadPyDevice', 'isPyDevice', 'unloadDevice', 'unloadAllDevices', 'reset', 'initializeDevice', 'initializeAllDevices', 'getDeviceInitializationState', 'getLoadedDevices', 'getLoadedDevicesOfType', 'getDeviceType', 'getDeviceLibrary', 'getDeviceName', 'getDeviceDescription', 'getParentLabel', 'setParentLabel', 'getInstalledDevices', 'getLoadedPeripheralDevices', 'getInstalledDeviceDescription', 'getDevicePropertyNames', 'hasProperty', 'getProperty', 'getPropertyFromCache', 'setProperty', 'getPropertyType', 'hasPropertyLimits', 'getPropertyLowerLimit', 'getPropertyUpperLimit', 'getAllowedPropertyValues', 'isPropertyPreInit', 'isPropertyReadOnly', 'isPropertySequenceable', 'getPropertySequenceMaxLength', 'loadPropertySequence', 'startPropertySequence', 'stopPropertySequence', 'deviceBusy', 'waitForDevice', 'waitForConfig', 'systemBusy', 'waitForSystem', 'waitForDeviceType', 'deviceTypeBusy', 'getDeviceDelayMs', 'setDeviceDelayMs', 'usesDeviceDelay', 'setXYStageDevice', 'getXYStageDevice', 'setXYPosition', 'getXYPosition', 'getXPosition', 'getYPosition', 'getXYStageSequenceMaxLength', 'isXYStageSequenceable', 'loadXYStageSequence', 'setOriginX', 'setOriginY', 'setOriginXY', 'setAdapterOriginXY', 'setRelativeXYPosition', 'startXYStageSequence', 'stopXYStageSequence', 'getFocusDevice', 'setFocusDevice', 'getPosition', 'setPosition', 'setFocusDirection', 'getFocusDirection', 'setOrigin', 'setRelativePosition', 'setAdapterOrigin', 'isStageSequenceable', 'isStageLinearSequenceable', 'getStageSequenceMaxLength', 'loadStageSequence', 'startStageSequence', 'stopStageSequence', 'setStageLinearSequence', 'isContinuousFocusDrive', 'home', 'stop', 'setCameraDevice', 'getCameraDevice', 'getImage', 'isSequenceRunning', 'getRemainingImageCount', 'getLastImage', 'getLastImageMD', 'getNBeforeLastImageMD', 'popNextImage', 'popNextImageMD', 'setCircularBufferMemoryFootprint', 'initializeCircularBuffer', 'getBufferFreeCapacity', 'getBufferTotalCapacity', 'getCircularBufferMemoryFootprint', 'clearCircularBuffer', 'isBufferOverflowed', 'getImageBitDepth', 'getBytesPerPixel', 'getImageBufferSize', 'getImageHeight', 'getImageWidth', 'getNumberOfComponents', 'getNumberOfCameraChannels', 'getCameraChannelName', 'getExposure', 'setExposure', 'getROI', 'clearROI', 'isExposureSequenceable', 'loadExposureSequence', 'getExposureSequenceMaxLength', 'startExposureSequence', 'stopExposureSequence', 'prepareSequenceAcquisition', 'getPixelSizeAffine', 'getPixelSizeUm', 'setSLMDevice', 'getSLMDevice', 'setSLMImage', 'getSLMImage', 'setSLMPixelsTo', 'displaySLMImage', 'setSLMExposure', 'getSLMExposure', 'getSLMWidth', 'getSLMHeight', 'getSLMNumberOfComponents', 'getSLMBytesPerPixel', 'getSLMSequenceMaxLength', 'loadSLMSequence', 'startSLMSequence', 'stopSLMSequence', 'setState', 'getState', 'getNumberOfStates', 'setStateLabel', 'getStateLabel', 'defineStateLabel', 'getStateLabels', 'getStateFromLabel', 'setShutterDevice', 'getShutterDevice', 'getShutterOpen', 'defineConfigGroup', 'deleteConfigGroup', 'renameConfigGroup', 'defineConfig', 'deleteConfig', 'renameConfig', 'getConfigData', 'setConfig', 'getCurrentConfig', 'getCurrentConfigFromCache', 'getConfigState', 'getConfigGroupState', 'getConfigGroupStateFromCache', 'getSystemState', 'getSystemStateCache', 'updateSystemStateCache', 'instance', 'registerCallback', 'events', 'setDeviceAdapterSearchPaths', 'systemConfigurationFile', 'detectDevice', 'getPixelSizeConfigData', 'getLastImageAndMD', 'popNextImageAndMD', 'getNBeforeLastImageAndMD', 'iterDeviceAdapters', 'iterDevices', 'iterProperties', 'getPropertyObject', 'getAdapterObject', 'getDeviceObject', 'getConfigGroupObject', 'iterConfigGroups', 'getCurrentDeviceOfType', 'getDeviceSchema', 'objective_device_pattern', 'channelGroup_pattern', 'guessObjectiveDevices', 'getOrGuessChannelGroup', 'setRelativeXYZPosition', 'getZPosition', 'setZPosition', 'getCameraChannelNames', 'snapImage', 'mda', 'run_mda', 'register_mda_engine', 'fixImage', 'getPhysicalCameraDevice', 'getTaggedImage', 'popNextTaggedImage', 'getTags', 'snap', 'startContinuousSequenceAcquisition', 'startSequenceAcquisition', 'stopSequenceAcquisition', 'setAutoFocusOffset', 'getAutoFocusOffset', 'setAutoShutter', 'setShutterOpen', 'setPixelSizeUm', 'deletePixelSizeConfig', 'definePixelSizeConfig', 'setROI', 'setChannelGroup', 'describe', 'state', 'setContext', 'canSequenceEvents'], 'action_targets': {}, 'metadata': {'repo': 'pymmcore-plus/pymmcore-plus', 'repo_url': 'https://github.com/pymmcore-plus/pymmcore-plus', 'brand': 'Nikon', 'model': 'Ti2', 'device_type_cn': '普通光学显微镜', 'device_type_en': 'Optical Microscope', 'source_framework': 'pymmcore-plus', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 1358, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def loadSystemConfiguration(self, **kwargs):
        return self.call('loadSystemConfiguration', kwargs=kwargs)

    def saveSystemConfiguration(self, **kwargs):
        return self.call('saveSystemConfiguration', kwargs=kwargs)

    def loadDevice(self, **kwargs):
        return self.call('loadDevice', kwargs=kwargs)

    def loadPyDevice(self, **kwargs):
        return self.call('loadPyDevice', kwargs=kwargs)

    def isPyDevice(self, **kwargs):
        return self.call('isPyDevice', kwargs=kwargs)

    def unloadDevice(self, **kwargs):
        return self.call('unloadDevice', kwargs=kwargs)

    def unloadAllDevices(self, **kwargs):
        return self.call('unloadAllDevices', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def initializeDevice(self, **kwargs):
        return self.call('initializeDevice', kwargs=kwargs)

    def initializeAllDevices(self, **kwargs):
        return self.call('initializeAllDevices', kwargs=kwargs)

    def getDeviceInitializationState(self, **kwargs):
        return self.call('getDeviceInitializationState', kwargs=kwargs)

    def getLoadedDevices(self, **kwargs):
        return self.call('getLoadedDevices', kwargs=kwargs)

    def getLoadedDevicesOfType(self, **kwargs):
        return self.call('getLoadedDevicesOfType', kwargs=kwargs)

    def getDeviceType(self, **kwargs):
        return self.call('getDeviceType', kwargs=kwargs)

    def getDeviceLibrary(self, **kwargs):
        return self.call('getDeviceLibrary', kwargs=kwargs)

    def getDeviceName(self, **kwargs):
        return self.call('getDeviceName', kwargs=kwargs)

    def getDeviceDescription(self, **kwargs):
        return self.call('getDeviceDescription', kwargs=kwargs)

    def getParentLabel(self, **kwargs):
        return self.call('getParentLabel', kwargs=kwargs)

    def setParentLabel(self, **kwargs):
        return self.call('setParentLabel', kwargs=kwargs)

    def getInstalledDevices(self, **kwargs):
        return self.call('getInstalledDevices', kwargs=kwargs)

    def getLoadedPeripheralDevices(self, **kwargs):
        return self.call('getLoadedPeripheralDevices', kwargs=kwargs)

    def getInstalledDeviceDescription(self, **kwargs):
        return self.call('getInstalledDeviceDescription', kwargs=kwargs)

    def getDevicePropertyNames(self, **kwargs):
        return self.call('getDevicePropertyNames', kwargs=kwargs)

    def hasProperty(self, **kwargs):
        return self.call('hasProperty', kwargs=kwargs)

    def getProperty(self, **kwargs):
        return self.call('getProperty', kwargs=kwargs)

    def getPropertyFromCache(self, **kwargs):
        return self.call('getPropertyFromCache', kwargs=kwargs)

    def setProperty(self, **kwargs):
        return self.call('setProperty', kwargs=kwargs)

    def getPropertyType(self, **kwargs):
        return self.call('getPropertyType', kwargs=kwargs)

    def hasPropertyLimits(self, **kwargs):
        return self.call('hasPropertyLimits', kwargs=kwargs)

    def getPropertyLowerLimit(self, **kwargs):
        return self.call('getPropertyLowerLimit', kwargs=kwargs)

    def getPropertyUpperLimit(self, **kwargs):
        return self.call('getPropertyUpperLimit', kwargs=kwargs)

    def getAllowedPropertyValues(self, **kwargs):
        return self.call('getAllowedPropertyValues', kwargs=kwargs)

    def isPropertyPreInit(self, **kwargs):
        return self.call('isPropertyPreInit', kwargs=kwargs)

    def isPropertyReadOnly(self, **kwargs):
        return self.call('isPropertyReadOnly', kwargs=kwargs)

    def isPropertySequenceable(self, **kwargs):
        return self.call('isPropertySequenceable', kwargs=kwargs)

    def getPropertySequenceMaxLength(self, **kwargs):
        return self.call('getPropertySequenceMaxLength', kwargs=kwargs)

    def loadPropertySequence(self, **kwargs):
        return self.call('loadPropertySequence', kwargs=kwargs)

    def startPropertySequence(self, **kwargs):
        return self.call('startPropertySequence', kwargs=kwargs)

    def stopPropertySequence(self, **kwargs):
        return self.call('stopPropertySequence', kwargs=kwargs)

    def deviceBusy(self, **kwargs):
        return self.call('deviceBusy', kwargs=kwargs)

    def waitForDevice(self, **kwargs):
        return self.call('waitForDevice', kwargs=kwargs)

    def waitForConfig(self, **kwargs):
        return self.call('waitForConfig', kwargs=kwargs)

    def systemBusy(self, **kwargs):
        return self.call('systemBusy', kwargs=kwargs)

    def waitForSystem(self, **kwargs):
        return self.call('waitForSystem', kwargs=kwargs)

    def waitForDeviceType(self, **kwargs):
        return self.call('waitForDeviceType', kwargs=kwargs)

    def deviceTypeBusy(self, **kwargs):
        return self.call('deviceTypeBusy', kwargs=kwargs)

    def getDeviceDelayMs(self, **kwargs):
        return self.call('getDeviceDelayMs', kwargs=kwargs)

    def setDeviceDelayMs(self, **kwargs):
        return self.call('setDeviceDelayMs', kwargs=kwargs)

    def usesDeviceDelay(self, **kwargs):
        return self.call('usesDeviceDelay', kwargs=kwargs)

    def setXYStageDevice(self, **kwargs):
        return self.call('setXYStageDevice', kwargs=kwargs)

    def getXYStageDevice(self, **kwargs):
        return self.call('getXYStageDevice', kwargs=kwargs)

    def setXYPosition(self, **kwargs):
        return self.call('setXYPosition', kwargs=kwargs)

    def getXYPosition(self, **kwargs):
        return self.call('getXYPosition', kwargs=kwargs)

    def getXPosition(self, **kwargs):
        return self.call('getXPosition', kwargs=kwargs)

    def getYPosition(self, **kwargs):
        return self.call('getYPosition', kwargs=kwargs)

    def getXYStageSequenceMaxLength(self, **kwargs):
        return self.call('getXYStageSequenceMaxLength', kwargs=kwargs)

    def isXYStageSequenceable(self, **kwargs):
        return self.call('isXYStageSequenceable', kwargs=kwargs)

    def loadXYStageSequence(self, **kwargs):
        return self.call('loadXYStageSequence', kwargs=kwargs)

    def setOriginX(self, **kwargs):
        return self.call('setOriginX', kwargs=kwargs)

    def setOriginY(self, **kwargs):
        return self.call('setOriginY', kwargs=kwargs)

    def setOriginXY(self, **kwargs):
        return self.call('setOriginXY', kwargs=kwargs)

    def setAdapterOriginXY(self, **kwargs):
        return self.call('setAdapterOriginXY', kwargs=kwargs)

    def setRelativeXYPosition(self, **kwargs):
        return self.call('setRelativeXYPosition', kwargs=kwargs)

    def startXYStageSequence(self, **kwargs):
        return self.call('startXYStageSequence', kwargs=kwargs)

    def stopXYStageSequence(self, **kwargs):
        return self.call('stopXYStageSequence', kwargs=kwargs)

    def getFocusDevice(self, **kwargs):
        return self.call('getFocusDevice', kwargs=kwargs)

    def setFocusDevice(self, **kwargs):
        return self.call('setFocusDevice', kwargs=kwargs)

    def getPosition(self, **kwargs):
        return self.call('getPosition', kwargs=kwargs)

    def setPosition(self, **kwargs):
        return self.call('setPosition', kwargs=kwargs)

    def setFocusDirection(self, **kwargs):
        return self.call('setFocusDirection', kwargs=kwargs)

    def getFocusDirection(self, **kwargs):
        return self.call('getFocusDirection', kwargs=kwargs)

    def setOrigin(self, **kwargs):
        return self.call('setOrigin', kwargs=kwargs)

    def setRelativePosition(self, **kwargs):
        return self.call('setRelativePosition', kwargs=kwargs)

    def setAdapterOrigin(self, **kwargs):
        return self.call('setAdapterOrigin', kwargs=kwargs)

    def isStageSequenceable(self, **kwargs):
        return self.call('isStageSequenceable', kwargs=kwargs)

    def isStageLinearSequenceable(self, **kwargs):
        return self.call('isStageLinearSequenceable', kwargs=kwargs)

    def getStageSequenceMaxLength(self, **kwargs):
        return self.call('getStageSequenceMaxLength', kwargs=kwargs)

    def loadStageSequence(self, **kwargs):
        return self.call('loadStageSequence', kwargs=kwargs)

    def startStageSequence(self, **kwargs):
        return self.call('startStageSequence', kwargs=kwargs)

    def stopStageSequence(self, **kwargs):
        return self.call('stopStageSequence', kwargs=kwargs)

    def setStageLinearSequence(self, **kwargs):
        return self.call('setStageLinearSequence', kwargs=kwargs)

    def isContinuousFocusDrive(self, **kwargs):
        return self.call('isContinuousFocusDrive', kwargs=kwargs)

    def home(self, **kwargs):
        return self.call('home', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def setCameraDevice(self, **kwargs):
        return self.call('setCameraDevice', kwargs=kwargs)

    def getCameraDevice(self, **kwargs):
        return self.call('getCameraDevice', kwargs=kwargs)

    def getImage(self, **kwargs):
        return self.call('getImage', kwargs=kwargs)

    def isSequenceRunning(self, **kwargs):
        return self.call('isSequenceRunning', kwargs=kwargs)

    def getRemainingImageCount(self, **kwargs):
        return self.call('getRemainingImageCount', kwargs=kwargs)

    def getLastImage(self, **kwargs):
        return self.call('getLastImage', kwargs=kwargs)

    def getLastImageMD(self, **kwargs):
        return self.call('getLastImageMD', kwargs=kwargs)

    def getNBeforeLastImageMD(self, **kwargs):
        return self.call('getNBeforeLastImageMD', kwargs=kwargs)

    def popNextImage(self, **kwargs):
        return self.call('popNextImage', kwargs=kwargs)

    def popNextImageMD(self, **kwargs):
        return self.call('popNextImageMD', kwargs=kwargs)

    def setCircularBufferMemoryFootprint(self, **kwargs):
        return self.call('setCircularBufferMemoryFootprint', kwargs=kwargs)

    def initializeCircularBuffer(self, **kwargs):
        return self.call('initializeCircularBuffer', kwargs=kwargs)

    def getBufferFreeCapacity(self, **kwargs):
        return self.call('getBufferFreeCapacity', kwargs=kwargs)

    def getBufferTotalCapacity(self, **kwargs):
        return self.call('getBufferTotalCapacity', kwargs=kwargs)

    def getCircularBufferMemoryFootprint(self, **kwargs):
        return self.call('getCircularBufferMemoryFootprint', kwargs=kwargs)

    def clearCircularBuffer(self, **kwargs):
        return self.call('clearCircularBuffer', kwargs=kwargs)

    def isBufferOverflowed(self, **kwargs):
        return self.call('isBufferOverflowed', kwargs=kwargs)

    def getImageBitDepth(self, **kwargs):
        return self.call('getImageBitDepth', kwargs=kwargs)

    def getBytesPerPixel(self, **kwargs):
        return self.call('getBytesPerPixel', kwargs=kwargs)

    def getImageBufferSize(self, **kwargs):
        return self.call('getImageBufferSize', kwargs=kwargs)

    def getImageHeight(self, **kwargs):
        return self.call('getImageHeight', kwargs=kwargs)

    def getImageWidth(self, **kwargs):
        return self.call('getImageWidth', kwargs=kwargs)

    def getNumberOfComponents(self, **kwargs):
        return self.call('getNumberOfComponents', kwargs=kwargs)

    def getNumberOfCameraChannels(self, **kwargs):
        return self.call('getNumberOfCameraChannels', kwargs=kwargs)

    def getCameraChannelName(self, **kwargs):
        return self.call('getCameraChannelName', kwargs=kwargs)

    def getExposure(self, **kwargs):
        return self.call('getExposure', kwargs=kwargs)

    def setExposure(self, **kwargs):
        return self.call('setExposure', kwargs=kwargs)

    def getROI(self, **kwargs):
        return self.call('getROI', kwargs=kwargs)

    def clearROI(self, **kwargs):
        return self.call('clearROI', kwargs=kwargs)

    def isExposureSequenceable(self, **kwargs):
        return self.call('isExposureSequenceable', kwargs=kwargs)

    def loadExposureSequence(self, **kwargs):
        return self.call('loadExposureSequence', kwargs=kwargs)

    def getExposureSequenceMaxLength(self, **kwargs):
        return self.call('getExposureSequenceMaxLength', kwargs=kwargs)

    def startExposureSequence(self, **kwargs):
        return self.call('startExposureSequence', kwargs=kwargs)

    def stopExposureSequence(self, **kwargs):
        return self.call('stopExposureSequence', kwargs=kwargs)

    def prepareSequenceAcquisition(self, **kwargs):
        return self.call('prepareSequenceAcquisition', kwargs=kwargs)

    def getPixelSizeAffine(self, **kwargs):
        return self.call('getPixelSizeAffine', kwargs=kwargs)

    def getPixelSizeUm(self, **kwargs):
        return self.call('getPixelSizeUm', kwargs=kwargs)

    def setSLMDevice(self, **kwargs):
        return self.call('setSLMDevice', kwargs=kwargs)

    def getSLMDevice(self, **kwargs):
        return self.call('getSLMDevice', kwargs=kwargs)

    def setSLMImage(self, **kwargs):
        return self.call('setSLMImage', kwargs=kwargs)

    def getSLMImage(self, **kwargs):
        return self.call('getSLMImage', kwargs=kwargs)

    def setSLMPixelsTo(self, **kwargs):
        return self.call('setSLMPixelsTo', kwargs=kwargs)

    def displaySLMImage(self, **kwargs):
        return self.call('displaySLMImage', kwargs=kwargs)

    def setSLMExposure(self, **kwargs):
        return self.call('setSLMExposure', kwargs=kwargs)

    def getSLMExposure(self, **kwargs):
        return self.call('getSLMExposure', kwargs=kwargs)

    def getSLMWidth(self, **kwargs):
        return self.call('getSLMWidth', kwargs=kwargs)

    def getSLMHeight(self, **kwargs):
        return self.call('getSLMHeight', kwargs=kwargs)

    def getSLMNumberOfComponents(self, **kwargs):
        return self.call('getSLMNumberOfComponents', kwargs=kwargs)

    def getSLMBytesPerPixel(self, **kwargs):
        return self.call('getSLMBytesPerPixel', kwargs=kwargs)

    def getSLMSequenceMaxLength(self, **kwargs):
        return self.call('getSLMSequenceMaxLength', kwargs=kwargs)

    def loadSLMSequence(self, **kwargs):
        return self.call('loadSLMSequence', kwargs=kwargs)

    def startSLMSequence(self, **kwargs):
        return self.call('startSLMSequence', kwargs=kwargs)

    def stopSLMSequence(self, **kwargs):
        return self.call('stopSLMSequence', kwargs=kwargs)

    def setState(self, **kwargs):
        return self.call('setState', kwargs=kwargs)

    def getState(self, **kwargs):
        return self.call('getState', kwargs=kwargs)

    def getNumberOfStates(self, **kwargs):
        return self.call('getNumberOfStates', kwargs=kwargs)

    def setStateLabel(self, **kwargs):
        return self.call('setStateLabel', kwargs=kwargs)

    def getStateLabel(self, **kwargs):
        return self.call('getStateLabel', kwargs=kwargs)

    def defineStateLabel(self, **kwargs):
        return self.call('defineStateLabel', kwargs=kwargs)

    def getStateLabels(self, **kwargs):
        return self.call('getStateLabels', kwargs=kwargs)

    def getStateFromLabel(self, **kwargs):
        return self.call('getStateFromLabel', kwargs=kwargs)

    def setShutterDevice(self, **kwargs):
        return self.call('setShutterDevice', kwargs=kwargs)

    def getShutterDevice(self, **kwargs):
        return self.call('getShutterDevice', kwargs=kwargs)

    def getShutterOpen(self, **kwargs):
        return self.call('getShutterOpen', kwargs=kwargs)

    def defineConfigGroup(self, **kwargs):
        return self.call('defineConfigGroup', kwargs=kwargs)

    def deleteConfigGroup(self, **kwargs):
        return self.call('deleteConfigGroup', kwargs=kwargs)

    def renameConfigGroup(self, **kwargs):
        return self.call('renameConfigGroup', kwargs=kwargs)

    def defineConfig(self, **kwargs):
        return self.call('defineConfig', kwargs=kwargs)

    def deleteConfig(self, **kwargs):
        return self.call('deleteConfig', kwargs=kwargs)

    def renameConfig(self, **kwargs):
        return self.call('renameConfig', kwargs=kwargs)

    def getConfigData(self, **kwargs):
        return self.call('getConfigData', kwargs=kwargs)

    def setConfig(self, **kwargs):
        return self.call('setConfig', kwargs=kwargs)

    def getCurrentConfig(self, **kwargs):
        return self.call('getCurrentConfig', kwargs=kwargs)

    def getCurrentConfigFromCache(self, **kwargs):
        return self.call('getCurrentConfigFromCache', kwargs=kwargs)

    def getConfigState(self, **kwargs):
        return self.call('getConfigState', kwargs=kwargs)

    def getConfigGroupState(self, **kwargs):
        return self.call('getConfigGroupState', kwargs=kwargs)

    def getConfigGroupStateFromCache(self, **kwargs):
        return self.call('getConfigGroupStateFromCache', kwargs=kwargs)

    def getSystemState(self, **kwargs):
        return self.call('getSystemState', kwargs=kwargs)

    def getSystemStateCache(self, **kwargs):
        return self.call('getSystemStateCache', kwargs=kwargs)

    def updateSystemStateCache(self, **kwargs):
        return self.call('updateSystemStateCache', kwargs=kwargs)

    def instance(self, **kwargs):
        return self.call('instance', kwargs=kwargs)

    def registerCallback(self, **kwargs):
        return self.call('registerCallback', kwargs=kwargs)

    def events(self, **kwargs):
        return self.call('events', kwargs=kwargs)

    def setDeviceAdapterSearchPaths(self, **kwargs):
        return self.call('setDeviceAdapterSearchPaths', kwargs=kwargs)

    def systemConfigurationFile(self, **kwargs):
        return self.call('systemConfigurationFile', kwargs=kwargs)

    def detectDevice(self, **kwargs):
        return self.call('detectDevice', kwargs=kwargs)

    def getPixelSizeConfigData(self, **kwargs):
        return self.call('getPixelSizeConfigData', kwargs=kwargs)

    def getLastImageAndMD(self, **kwargs):
        return self.call('getLastImageAndMD', kwargs=kwargs)

    def popNextImageAndMD(self, **kwargs):
        return self.call('popNextImageAndMD', kwargs=kwargs)

    def getNBeforeLastImageAndMD(self, **kwargs):
        return self.call('getNBeforeLastImageAndMD', kwargs=kwargs)

    def iterDeviceAdapters(self, **kwargs):
        return self.call('iterDeviceAdapters', kwargs=kwargs)

    def iterDevices(self, **kwargs):
        return self.call('iterDevices', kwargs=kwargs)

    def iterProperties(self, **kwargs):
        return self.call('iterProperties', kwargs=kwargs)

    def getPropertyObject(self, **kwargs):
        return self.call('getPropertyObject', kwargs=kwargs)

    def getAdapterObject(self, **kwargs):
        return self.call('getAdapterObject', kwargs=kwargs)

    def getDeviceObject(self, **kwargs):
        return self.call('getDeviceObject', kwargs=kwargs)

    def getConfigGroupObject(self, **kwargs):
        return self.call('getConfigGroupObject', kwargs=kwargs)

    def iterConfigGroups(self, **kwargs):
        return self.call('iterConfigGroups', kwargs=kwargs)

    def getCurrentDeviceOfType(self, **kwargs):
        return self.call('getCurrentDeviceOfType', kwargs=kwargs)

    def getDeviceSchema(self, **kwargs):
        return self.call('getDeviceSchema', kwargs=kwargs)

    def objective_device_pattern(self, **kwargs):
        return self.call('objective_device_pattern', kwargs=kwargs)

    def channelGroup_pattern(self, **kwargs):
        return self.call('channelGroup_pattern', kwargs=kwargs)

    def guessObjectiveDevices(self, **kwargs):
        return self.call('guessObjectiveDevices', kwargs=kwargs)

    def getOrGuessChannelGroup(self, **kwargs):
        return self.call('getOrGuessChannelGroup', kwargs=kwargs)

    def setRelativeXYZPosition(self, **kwargs):
        return self.call('setRelativeXYZPosition', kwargs=kwargs)

    def getZPosition(self, **kwargs):
        return self.call('getZPosition', kwargs=kwargs)

    def setZPosition(self, **kwargs):
        return self.call('setZPosition', kwargs=kwargs)

    def getCameraChannelNames(self, **kwargs):
        return self.call('getCameraChannelNames', kwargs=kwargs)

    def snapImage(self, **kwargs):
        return self.call('snapImage', kwargs=kwargs)

    def mda(self, **kwargs):
        return self.call('mda', kwargs=kwargs)

    def run_mda(self, **kwargs):
        return self.call('run_mda', kwargs=kwargs)

    def register_mda_engine(self, **kwargs):
        return self.call('register_mda_engine', kwargs=kwargs)

    def fixImage(self, **kwargs):
        return self.call('fixImage', kwargs=kwargs)

    def getPhysicalCameraDevice(self, **kwargs):
        return self.call('getPhysicalCameraDevice', kwargs=kwargs)

    def getTaggedImage(self, **kwargs):
        return self.call('getTaggedImage', kwargs=kwargs)

    def popNextTaggedImage(self, **kwargs):
        return self.call('popNextTaggedImage', kwargs=kwargs)

    def getTags(self, **kwargs):
        return self.call('getTags', kwargs=kwargs)

    def snap(self, **kwargs):
        return self.call('snap', kwargs=kwargs)

    def startContinuousSequenceAcquisition(self, **kwargs):
        return self.call('startContinuousSequenceAcquisition', kwargs=kwargs)

    def startSequenceAcquisition(self, **kwargs):
        return self.call('startSequenceAcquisition', kwargs=kwargs)

    def stopSequenceAcquisition(self, **kwargs):
        return self.call('stopSequenceAcquisition', kwargs=kwargs)

    def setAutoFocusOffset(self, **kwargs):
        return self.call('setAutoFocusOffset', kwargs=kwargs)

    def getAutoFocusOffset(self, **kwargs):
        return self.call('getAutoFocusOffset', kwargs=kwargs)

    def setAutoShutter(self, **kwargs):
        return self.call('setAutoShutter', kwargs=kwargs)

    def setShutterOpen(self, **kwargs):
        return self.call('setShutterOpen', kwargs=kwargs)

    def setPixelSizeUm(self, **kwargs):
        return self.call('setPixelSizeUm', kwargs=kwargs)

    def deletePixelSizeConfig(self, **kwargs):
        return self.call('deletePixelSizeConfig', kwargs=kwargs)

    def definePixelSizeConfig(self, **kwargs):
        return self.call('definePixelSizeConfig', kwargs=kwargs)

    def setROI(self, **kwargs):
        return self.call('setROI', kwargs=kwargs)

    def setChannelGroup(self, **kwargs):
        return self.call('setChannelGroup', kwargs=kwargs)

    def describe(self, **kwargs):
        return self.call('describe', kwargs=kwargs)

    def state(self, **kwargs):
        return self.call('state', kwargs=kwargs)

    def setContext(self, **kwargs):
        return self.call('setContext', kwargs=kwargs)

    def canSequenceEvents(self, **kwargs):
        return self.call('canSequenceEvents', kwargs=kwargs)

