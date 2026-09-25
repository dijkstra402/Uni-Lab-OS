from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentInhecoThermoshake(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AD-SDL__inheco_incubator_module', 'source_file': 'src/inheco_incubator_interface.py', 'class_name': 'Interface', 'import_roots': ['src'], 'candidate_methods': ['open_connection', 'close_connection', 'initialize_device', 'reset_device', 'report_error_flags', 'get_actual_temperature', 'get_target_temperature', 'set_target_temperature', 'start_heater', 'stop_heater', 'is_heater_active', 'open_door', 'close_door', 'report_door_status', 'report_labware', 'start_shaker', 'stop_shaker', 'is_shaker_active', 'set_shaker_parameters', 'send_message', 'format_response', 'is_busy'], 'action_targets': {}, 'metadata': {'repo': 'AD-SDL/inheco_incubator_module', 'repo_url': 'https://github.com/AD-SDL/inheco_incubator_module', 'brand': 'Inheco', 'model': 'ThermoShake', 'device_type_cn': '培养振荡器', 'device_type_en': 'Thermo Shaker', 'source_framework': '生命科学', 'tag_id': '4389', 'tag_name': '恒温摇床', 'tag_name_en': 'Constant Temperature Shaker', 'candidate_score': 222, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def open_connection(self, **kwargs):
        return self.call('open_connection', kwargs=kwargs)

    def close_connection(self, **kwargs):
        return self.call('close_connection', kwargs=kwargs)

    def initialize_device(self, **kwargs):
        return self.call('initialize_device', kwargs=kwargs)

    def reset_device(self, **kwargs):
        return self.call('reset_device', kwargs=kwargs)

    def report_error_flags(self, **kwargs):
        return self.call('report_error_flags', kwargs=kwargs)

    def get_actual_temperature(self, **kwargs):
        return self.call('get_actual_temperature', kwargs=kwargs)

    def get_target_temperature(self, **kwargs):
        return self.call('get_target_temperature', kwargs=kwargs)

    def set_target_temperature(self, **kwargs):
        return self.call('set_target_temperature', kwargs=kwargs)

    def start_heater(self, **kwargs):
        return self.call('start_heater', kwargs=kwargs)

    def stop_heater(self, **kwargs):
        return self.call('stop_heater', kwargs=kwargs)

    def is_heater_active(self, **kwargs):
        return self.call('is_heater_active', kwargs=kwargs)

    def open_door(self, **kwargs):
        return self.call('open_door', kwargs=kwargs)

    def close_door(self, **kwargs):
        return self.call('close_door', kwargs=kwargs)

    def report_door_status(self, **kwargs):
        return self.call('report_door_status', kwargs=kwargs)

    def report_labware(self, **kwargs):
        return self.call('report_labware', kwargs=kwargs)

    def start_shaker(self, **kwargs):
        return self.call('start_shaker', kwargs=kwargs)

    def stop_shaker(self, **kwargs):
        return self.call('stop_shaker', kwargs=kwargs)

    def is_shaker_active(self, **kwargs):
        return self.call('is_shaker_active', kwargs=kwargs)

    def set_shaker_parameters(self, **kwargs):
        return self.call('set_shaker_parameters', kwargs=kwargs)

    def send_message(self, **kwargs):
        return self.call('send_message', kwargs=kwargs)

    def format_response(self, **kwargs):
        return self.call('format_response', kwargs=kwargs)

    def is_busy(self, **kwargs):
        return self.call('is_busy', kwargs=kwargs)

