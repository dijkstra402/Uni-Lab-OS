from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentJulaboCf31Hl4Ms1000f(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/tiagocoutinho__julabo', 'source_file': 'julabo/tango/server/device.py', 'class_name': 'BaseJulaboCirculator', 'import_roots': [], 'candidate_methods': ['bath_temperature', 'heating_power', 'external_temperature', 'safety_temperature', 'set_point_1', 'set_point_2', 'set_point_3', 'high_temperature', 'low_temperature', 'active_set_point_channel', 'self_tunning', 'external_input', 'temperature_control', 'init_device', 'delete_device', 'dev_state', 'dev_status', 'identification', 'is_started', 'start', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'tiagocoutinho/julabo', 'repo_url': 'https://github.com/tiagocoutinho/julabo', 'brand': 'Julabo', 'model': 'CF31/HL-4/MS-1000f', 'device_type_cn': '循环浴/恒温器', 'device_type_en': 'Circulating Bath', 'source_framework': '独立仓库', 'tag_id': '4369', 'tag_name': '冷热水机', 'tag_name_en': 'Chiller / Heater Unit', 'candidate_score': 129, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def bath_temperature(self, **kwargs):
        return self.call('bath_temperature', kwargs=kwargs)

    def heating_power(self, **kwargs):
        return self.call('heating_power', kwargs=kwargs)

    def external_temperature(self, **kwargs):
        return self.call('external_temperature', kwargs=kwargs)

    def safety_temperature(self, **kwargs):
        return self.call('safety_temperature', kwargs=kwargs)

    def set_point_1(self, **kwargs):
        return self.call('set_point_1', kwargs=kwargs)

    def set_point_2(self, **kwargs):
        return self.call('set_point_2', kwargs=kwargs)

    def set_point_3(self, **kwargs):
        return self.call('set_point_3', kwargs=kwargs)

    def high_temperature(self, **kwargs):
        return self.call('high_temperature', kwargs=kwargs)

    def low_temperature(self, **kwargs):
        return self.call('low_temperature', kwargs=kwargs)

    def active_set_point_channel(self, **kwargs):
        return self.call('active_set_point_channel', kwargs=kwargs)

    def self_tunning(self, **kwargs):
        return self.call('self_tunning', kwargs=kwargs)

    def external_input(self, **kwargs):
        return self.call('external_input', kwargs=kwargs)

    def temperature_control(self, **kwargs):
        return self.call('temperature_control', kwargs=kwargs)

    def init_device(self, **kwargs):
        return self.call('init_device', kwargs=kwargs)

    def delete_device(self, **kwargs):
        return self.call('delete_device', kwargs=kwargs)

    def dev_state(self, **kwargs):
        return self.call('dev_state', kwargs=kwargs)

    def dev_status(self, **kwargs):
        return self.call('dev_status', kwargs=kwargs)

    def identification(self, **kwargs):
        return self.call('identification', kwargs=kwargs)

    def is_started(self, **kwargs):
        return self.call('is_started', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

