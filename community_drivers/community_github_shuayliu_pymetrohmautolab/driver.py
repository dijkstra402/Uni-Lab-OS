from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubShuayliuPymetrohmautolab(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/shuayliu_pyMetrohmAUTOLAB', 'source_file': 'src/Metrohm/AUTOLAB.py', 'class_name': 'AUTOLAB', 'import_roots': [], 'candidate_methods': ['disconnectAutolab', 'setSDKandADX', 'isMeasuring', 'connectToAutolab', 'measure', 'save', 'saveAs', 'setCellOn', 'setMode', 'setPotential', 'setCurrentRange', 'wait', 'loadData'], 'metadata': {'repo': 'shuayliu/pymetrohmautolab', 'repo_url': 'https://github.com/shuayliu/pyMetrohmAUTOLAB', 'unit_id': 'gh_metrohm_autolab_pgstat', 'source_file': 'src/Metrohm/AUTOLAB.py', 'candidate_score': 48, 'manufacturer': 'Metrohm', 'model_name': 'Metrohm Autolab PGSTAT'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def disconnectAutolab(self, **kwargs):
        return self.call('disconnectAutolab', kwargs=kwargs)

    def setSDKandADX(self, **kwargs):
        return self.call('setSDKandADX', kwargs=kwargs)

    def isMeasuring(self, **kwargs):
        return self.call('isMeasuring', kwargs=kwargs)

    def connectToAutolab(self, **kwargs):
        return self.call('connectToAutolab', kwargs=kwargs)

    def measure(self, **kwargs):
        return self.call('measure', kwargs=kwargs)

    def save(self, **kwargs):
        return self.call('save', kwargs=kwargs)

    def saveAs(self, **kwargs):
        return self.call('saveAs', kwargs=kwargs)

    def setCellOn(self, **kwargs):
        return self.call('setCellOn', kwargs=kwargs)

    def setMode(self, **kwargs):
        return self.call('setMode', kwargs=kwargs)

    def setPotential(self, **kwargs):
        return self.call('setPotential', kwargs=kwargs)

    def setCurrentRange(self, **kwargs):
        return self.call('setCurrentRange', kwargs=kwargs)

    def wait(self, **kwargs):
        return self.call('wait', kwargs=kwargs)

    def loadData(self, **kwargs):
        return self.call('loadData', kwargs=kwargs)

