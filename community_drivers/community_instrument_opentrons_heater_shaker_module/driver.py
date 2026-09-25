from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOpentronsHeaterShakerModule(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/anuwrag__Opentrons-Tools', 'source_file': 'Run-Module-from-Computer/hs_driver.py', 'class_name': 'HeaterShakerDriver', 'import_roots': [], 'candidate_methods': ['create', 'connect', 'disconnect', 'is_connected', 'open_labware_latch', 'close_labware_latch', 'set_temperature', 'get_temperature', 'set_rpm', 'get_rpm', 'get_labware_latch_status', 'home', 'get_device_info', 'enter_programming_mode', 'deactivate_heater'], 'action_targets': {}, 'metadata': {'repo': 'anuwrag/Opentrons-Tools', 'repo_url': 'https://github.com/anuwrag/Opentrons-Tools', 'brand': 'Opentrons', 'model': 'Heater-Shaker Module', 'device_type_cn': '热混匀仪', 'device_type_en': 'Thermomixer', 'source_framework': '专用驱动', 'tag_id': '4421', 'tag_name': '热混匀仪', 'tag_name_en': 'Thermomixer', 'candidate_score': 190, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def create(self, **kwargs):
        return self.call('create', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def is_connected(self, **kwargs):
        return self.call('is_connected', kwargs=kwargs)

    def open_labware_latch(self, **kwargs):
        return self.call('open_labware_latch', kwargs=kwargs)

    def close_labware_latch(self, **kwargs):
        return self.call('close_labware_latch', kwargs=kwargs)

    def set_temperature(self, **kwargs):
        return self.call('set_temperature', kwargs=kwargs)

    def get_temperature(self, **kwargs):
        return self.call('get_temperature', kwargs=kwargs)

    def set_rpm(self, **kwargs):
        return self.call('set_rpm', kwargs=kwargs)

    def get_rpm(self, **kwargs):
        return self.call('get_rpm', kwargs=kwargs)

    def get_labware_latch_status(self, **kwargs):
        return self.call('get_labware_latch_status', kwargs=kwargs)

    def home(self, **kwargs):
        return self.call('home', kwargs=kwargs)

    def get_device_info(self, **kwargs):
        return self.call('get_device_info', kwargs=kwargs)

    def enter_programming_mode(self, **kwargs):
        return self.call('enter_programming_mode', kwargs=kwargs)

    def deactivate_heater(self, **kwargs):
        return self.call('deactivate_heater', kwargs=kwargs)

