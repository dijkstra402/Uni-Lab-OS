from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubHelgesteinMetrohmAutolabPython(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/helgestein_metrohm_autolab_python', 'source_file': 'autolab.py', 'class_name': 'Autolab', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'ismeasuring', 'potential', 'current', 'setCurrentRange', 'setStability', 'time', 'appliedPotential', 'abort', 'loadProcedure', 'setSetpoints', 'whileMeasuring', 'CellOnOff', 'parseNox', 'performMeasurement'], 'metadata': {'repo': 'helgestein/metrohm_autolab_python', 'repo_url': 'https://github.com/helgestein/metrohm_autolab_python', 'unit_id': 'gh_metrohm_autolab_pgstat302n', 'source_file': 'autolab.py', 'candidate_score': 64, 'manufacturer': 'Metrohm Autolab', 'model_name': 'Metrohm Autolab PGSTAT302N'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def ismeasuring(self, **kwargs):
        return self.call('ismeasuring', kwargs=kwargs)

    def potential(self, **kwargs):
        return self.call('potential', kwargs=kwargs)

    def current(self, **kwargs):
        return self.call('current', kwargs=kwargs)

    def setCurrentRange(self, **kwargs):
        return self.call('setCurrentRange', kwargs=kwargs)

    def setStability(self, **kwargs):
        return self.call('setStability', kwargs=kwargs)

    def time(self, **kwargs):
        return self.call('time', kwargs=kwargs)

    def appliedPotential(self, **kwargs):
        return self.call('appliedPotential', kwargs=kwargs)

    def abort(self, **kwargs):
        return self.call('abort', kwargs=kwargs)

    def loadProcedure(self, **kwargs):
        return self.call('loadProcedure', kwargs=kwargs)

    def setSetpoints(self, **kwargs):
        return self.call('setSetpoints', kwargs=kwargs)

    def whileMeasuring(self, **kwargs):
        return self.call('whileMeasuring', kwargs=kwargs)

    def CellOnOff(self, **kwargs):
        return self.call('CellOnOff', kwargs=kwargs)

    def parseNox(self, **kwargs):
        return self.call('parseNox', kwargs=kwargs)

    def performMeasurement(self, **kwargs):
        return self.call('performMeasurement', kwargs=kwargs)

