from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMetrohmAutolabPgstat(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/shuayliu__pyMetrohmAUTOLAB', 'source_file': 'src/Metrohm/AUTOLAB.py', 'class_name': 'AUTOLAB', 'import_roots': ['src'], 'candidate_methods': ['disconnectAutolab', 'setSDKandADX', 'isMeasuring', 'connectToAutolab', 'measure', 'save', 'saveAs', 'setCellOn', 'setMode', 'setPotential', 'setCurrentRange', 'wait', 'loadData'], 'action_targets': {}, 'metadata': {'repo': 'shuayliu/pyMetrohmAUTOLAB', 'repo_url': 'https://github.com/shuayliu/pyMetrohmAUTOLAB', 'brand': 'Metrohm', 'model': 'Autolab PGSTAT', 'device_type_cn': '电化学反应器', 'device_type_en': 'Electrochemical Reactor', 'source_framework': '专用驱动', 'tag_id': '4424', 'tag_name': '电化学反应器', 'tag_name_en': 'Electrochemical Reactor', 'candidate_score': 162, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

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

