from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMetrohmAutolabPgstat302n(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/helgestein__metrohm_autolab_python', 'source_file': 'autolab.py', 'class_name': 'Autolab', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'ismeasuring', 'potential', 'current', 'setCurrentRange', 'setStability', 'time', 'appliedPotential', 'abort', 'loadProcedure', 'setSetpoints', 'whileMeasuring', 'CellOnOff', 'parseNox', 'performMeasurement'], 'action_targets': {}, 'metadata': {'repo': 'helgestein/metrohm_autolab_python', 'repo_url': 'https://github.com/helgestein/metrohm_autolab_python', 'brand': 'Metrohm Autolab', 'model': 'PGSTAT302N', 'device_type_cn': '恒电位仪', 'device_type_en': 'Potentiostat', 'source_framework': '电化学/热分析/天平', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 178, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

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

