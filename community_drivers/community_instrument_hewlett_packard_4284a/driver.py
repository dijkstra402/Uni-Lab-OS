from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHewlettPackard4284a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/leokogos__hp-4284A-LCR-meter-driver', 'source_file': 'gui_frames/runCVFrameGUI.py', 'class_name': 'RunCVFrame', 'import_roots': [], 'candidate_methods': ['Widgets', 'cb', 'updateInstHandle', 'updateFileName', 'runCVMeasurements'], 'action_targets': {}, 'metadata': {'repo': 'leokogos/hp-4284A-LCR-meter-driver', 'repo_url': 'https://github.com/leokogos/hp-4284A-LCR-meter-driver', 'brand': 'Hewlett-Packard', 'model': '4284A', 'device_type_cn': 'LCR表', 'device_type_en': 'LCR Meter', 'source_framework': '电化学/热分析/天平', 'tag_id': '4365', 'tag_name': '介电常数测定仪', 'tag_name_en': 'Dielectric Constant Meter', 'candidate_score': 70, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def Widgets(self, **kwargs):
        return self.call('Widgets', kwargs=kwargs)

    def cb(self, **kwargs):
        return self.call('cb', kwargs=kwargs)

    def updateInstHandle(self, **kwargs):
        return self.call('updateInstHandle', kwargs=kwargs)

    def updateFileName(self, **kwargs):
        return self.call('updateFileName', kwargs=kwargs)

    def runCVMeasurements(self, **kwargs):
        return self.call('runCVMeasurements', kwargs=kwargs)

