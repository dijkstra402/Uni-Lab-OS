from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIkaPlateRctDigital(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/cooper-group-uol-robotics__ika_plate_rct_digital', 'source_file': 'ika_plate_rct_digital_driver/src/ika_plate_rct_digital_driver/ika_serial_driver.py', 'class_name': 'IKADriver', 'import_roots': [], 'candidate_methods': ['startHeat', 'stopHeat', 'startStir', 'stopStir', 'setHeat', 'setStir', 'getHotplateTemp', 'getExternalTemp', 'getStirringSpeed', 'getViscosityTrend'], 'action_targets': {}, 'metadata': {'repo': 'cooper-group-uol-robotics/ika_plate_rct_digital', 'repo_url': 'https://github.com/cooper-group-uol-robotics/ika_plate_rct_digital', 'brand': 'IKA', 'model': 'Plate RCT Digital', 'device_type_cn': '磁力加热搅拌器', 'device_type_en': 'Magnetic Stirrer Hot Plate', 'source_framework': '反应器/合成设备', 'tag_id': '4395', 'tag_name': '控温磁力搅拌器', 'tag_name_en': 'Temperature-Controlled Magnetic Stirrer', 'candidate_score': 162, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def startHeat(self, **kwargs):
        return self.call('startHeat', kwargs=kwargs)

    def stopHeat(self, **kwargs):
        return self.call('stopHeat', kwargs=kwargs)

    def startStir(self, **kwargs):
        return self.call('startStir', kwargs=kwargs)

    def stopStir(self, **kwargs):
        return self.call('stopStir', kwargs=kwargs)

    def setHeat(self, **kwargs):
        return self.call('setHeat', kwargs=kwargs)

    def setStir(self, **kwargs):
        return self.call('setStir', kwargs=kwargs)

    def getHotplateTemp(self, **kwargs):
        return self.call('getHotplateTemp', kwargs=kwargs)

    def getExternalTemp(self, **kwargs):
        return self.call('getExternalTemp', kwargs=kwargs)

    def getStirringSpeed(self, **kwargs):
        return self.call('getStirringSpeed', kwargs=kwargs)

    def getViscosityTrend(self, **kwargs):
        return self.call('getViscosityTrend', kwargs=kwargs)

