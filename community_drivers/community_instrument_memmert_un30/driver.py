from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMemmertUn30(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/bec4__ovenControl', 'source_file': 'ovenControl.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['getTemperature', 'setTemperature', 'getProgram', 'appendToCSVFile'], 'action_targets': {'getTemperature': 'getTemperature', 'setTemperature': 'setTemperature', 'getProgram': 'getProgram', 'appendToCSVFile': 'appendToCSVFile'}, 'metadata': {'repo': 'bec4/ovenControl', 'repo_url': 'https://github.com/bec4/ovenControl', 'brand': 'Memmert', 'model': 'UN30', 'device_type_cn': '真空干燥箱', 'device_type_en': 'Vacuum Drying Oven', 'source_framework': '专用驱动', 'tag_id': '4430', 'tag_name': '真空干燥箱', 'tag_name_en': 'Vacuum Drying Oven', 'candidate_score': 68, 'parse_status': 'module_selected', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {'getTemperature': 'getTemperature', 'setTemperature': 'setTemperature', 'getProgram': 'getProgram', 'appendToCSVFile': 'appendToCSVFile'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def getTemperature(self, **kwargs):
        return self.call('getTemperature', kwargs=kwargs)

    def setTemperature(self, **kwargs):
        return self.call('setTemperature', kwargs=kwargs)

    def getProgram(self, **kwargs):
        return self.call('getProgram', kwargs=kwargs)

    def appendToCSVFile(self, **kwargs):
        return self.call('appendToCSVFile', kwargs=kwargs)

