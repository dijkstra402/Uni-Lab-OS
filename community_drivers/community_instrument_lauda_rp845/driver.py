from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLaudaRp845(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/geocryology__GeoCryoLabPy', 'source_file': 'equipment/Monitor.py', 'class_name': 'monitorFile', 'import_roots': [], 'candidate_methods': ['setFile', 'set_xcol', 'set_ycol', 'set_xmax', 'readdata', 'simpleXY', 'execute'], 'action_targets': {}, 'metadata': {'repo': 'geocryology/GeoCryoLabPy', 'repo_url': 'https://github.com/geocryology/GeoCryoLabPy', 'brand': 'Lauda', 'model': 'RP845', 'device_type_cn': '冷热水机', 'device_type_en': 'Chiller / Heater Unit', 'source_framework': '专用驱动', 'tag_id': '4369', 'tag_name': '冷热水机', 'tag_name_en': 'Chiller / Heater Unit', 'candidate_score': 86, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def setFile(self, **kwargs):
        return self.call('setFile', kwargs=kwargs)

    def set_xcol(self, **kwargs):
        return self.call('set_xcol', kwargs=kwargs)

    def set_ycol(self, **kwargs):
        return self.call('set_ycol', kwargs=kwargs)

    def set_xmax(self, **kwargs):
        return self.call('set_xmax', kwargs=kwargs)

    def readdata(self, **kwargs):
        return self.call('readdata', kwargs=kwargs)

    def simpleXY(self, **kwargs):
        return self.call('simpleXY', kwargs=kwargs)

    def execute(self, **kwargs):
        return self.call('execute', kwargs=kwargs)

