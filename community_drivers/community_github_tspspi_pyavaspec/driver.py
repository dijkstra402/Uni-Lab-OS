from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubTspspiPyavaspec(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/tspspi_pyavaspec', 'source_file': 'src/pyavaspec/pyavaspec.py', 'class_name': 'PyAvaSpec_2048_2', 'import_roots': [], 'candidate_methods': ['writeDevice', 'readDevice', 'close', 'cmdMeasure', 'cmdMeasureSoftAverages', 'loadData', 'dumpData', 'plotData', 'indexToWavelength', 'applyMovingAverage', 'searchPeaks', 'getVersionInformation', 'getDeviceConfig'], 'metadata': {'repo': 'tspspi/pyavaspec', 'repo_url': 'https://github.com/tspspi/pyavaspec', 'unit_id': 'gh_avantes_avaspec_2048_2', 'source_file': 'src/pyavaspec/pyavaspec.py', 'candidate_score': 87, 'manufacturer': 'Avantes', 'model_name': 'Avantes AvaSpec-2048-2'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def writeDevice(self, **kwargs):
        return self.call('writeDevice', kwargs=kwargs)

    def readDevice(self, **kwargs):
        return self.call('readDevice', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def cmdMeasure(self, **kwargs):
        return self.call('cmdMeasure', kwargs=kwargs)

    def cmdMeasureSoftAverages(self, **kwargs):
        return self.call('cmdMeasureSoftAverages', kwargs=kwargs)

    def loadData(self, **kwargs):
        return self.call('loadData', kwargs=kwargs)

    def dumpData(self, **kwargs):
        return self.call('dumpData', kwargs=kwargs)

    def plotData(self, **kwargs):
        return self.call('plotData', kwargs=kwargs)

    def indexToWavelength(self, **kwargs):
        return self.call('indexToWavelength', kwargs=kwargs)

    def applyMovingAverage(self, **kwargs):
        return self.call('applyMovingAverage', kwargs=kwargs)

    def searchPeaks(self, **kwargs):
        return self.call('searchPeaks', kwargs=kwargs)

    def getVersionInformation(self, **kwargs):
        return self.call('getVersionInformation', kwargs=kwargs)

    def getDeviceConfig(self, **kwargs):
        return self.call('getDeviceConfig', kwargs=kwargs)

