from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLonger(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Bofeng-DU__Longer_pump', 'source_file': 'modules/serial_labware/IKA_RET_Stirrer/IKA_RET_Control_Visc.py', 'class_name': 'IKARETControlVisc', 'import_roots': [], 'candidate_methods': ['stir_rate_pv', 'stir_rate_sp', 'temperature_pv', 'temperature_sp', 'start_heater', 'stop_heater', 'start_stirrer', 'stop_stirrer', 'start_ph_meter', 'stop_ph_meter', 'start_weighing', 'stop_weighing', 'reset_hot_plate', 'name', 'software_version', 'set_watch_dog_temp', 'set_watch_dog_stir_rate', 'get_hot_plate_temp_current', 'temperature_heat_transfer_medium_sp', 'temperature_hot_plate_pv', 'temperature_hot_plate_sp', 'temperature_hot_plate_safety_pv', 'temperature_hot_plate_safety_sp', 'get_viscosity_trend', 'get_ph', 'get_weight', 'launch_command_handler', 'open_connection', 'close_connection', 'send_message', 'non_blocking_wait', 'keepalive'], 'action_targets': {}, 'metadata': {'repo': 'Bofeng-DU/Longer_pump', 'repo_url': 'https://github.com/Bofeng-DU/Longer_pump', 'brand': 'Longer', 'model': '兰格注射泵', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': '专用驱动', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 238, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def stir_rate_pv(self, **kwargs):
        return self.call('stir_rate_pv', kwargs=kwargs)

    def stir_rate_sp(self, **kwargs):
        return self.call('stir_rate_sp', kwargs=kwargs)

    def temperature_pv(self, **kwargs):
        return self.call('temperature_pv', kwargs=kwargs)

    def temperature_sp(self, **kwargs):
        return self.call('temperature_sp', kwargs=kwargs)

    def start_heater(self, **kwargs):
        return self.call('start_heater', kwargs=kwargs)

    def stop_heater(self, **kwargs):
        return self.call('stop_heater', kwargs=kwargs)

    def start_stirrer(self, **kwargs):
        return self.call('start_stirrer', kwargs=kwargs)

    def stop_stirrer(self, **kwargs):
        return self.call('stop_stirrer', kwargs=kwargs)

    def start_ph_meter(self, **kwargs):
        return self.call('start_ph_meter', kwargs=kwargs)

    def stop_ph_meter(self, **kwargs):
        return self.call('stop_ph_meter', kwargs=kwargs)

    def start_weighing(self, **kwargs):
        return self.call('start_weighing', kwargs=kwargs)

    def stop_weighing(self, **kwargs):
        return self.call('stop_weighing', kwargs=kwargs)

    def reset_hot_plate(self, **kwargs):
        return self.call('reset_hot_plate', kwargs=kwargs)

    def name(self, **kwargs):
        return self.call('name', kwargs=kwargs)

    def software_version(self, **kwargs):
        return self.call('software_version', kwargs=kwargs)

    def set_watch_dog_temp(self, **kwargs):
        return self.call('set_watch_dog_temp', kwargs=kwargs)

    def set_watch_dog_stir_rate(self, **kwargs):
        return self.call('set_watch_dog_stir_rate', kwargs=kwargs)

    def get_hot_plate_temp_current(self, **kwargs):
        return self.call('get_hot_plate_temp_current', kwargs=kwargs)

    def temperature_heat_transfer_medium_sp(self, **kwargs):
        return self.call('temperature_heat_transfer_medium_sp', kwargs=kwargs)

    def temperature_hot_plate_pv(self, **kwargs):
        return self.call('temperature_hot_plate_pv', kwargs=kwargs)

    def temperature_hot_plate_sp(self, **kwargs):
        return self.call('temperature_hot_plate_sp', kwargs=kwargs)

    def temperature_hot_plate_safety_pv(self, **kwargs):
        return self.call('temperature_hot_plate_safety_pv', kwargs=kwargs)

    def temperature_hot_plate_safety_sp(self, **kwargs):
        return self.call('temperature_hot_plate_safety_sp', kwargs=kwargs)

    def get_viscosity_trend(self, **kwargs):
        return self.call('get_viscosity_trend', kwargs=kwargs)

    def get_ph(self, **kwargs):
        return self.call('get_ph', kwargs=kwargs)

    def get_weight(self, **kwargs):
        return self.call('get_weight', kwargs=kwargs)

    def launch_command_handler(self, **kwargs):
        return self.call('launch_command_handler', kwargs=kwargs)

    def open_connection(self, **kwargs):
        return self.call('open_connection', kwargs=kwargs)

    def close_connection(self, **kwargs):
        return self.call('close_connection', kwargs=kwargs)

    def send_message(self, **kwargs):
        return self.call('send_message', kwargs=kwargs)

    def non_blocking_wait(self, **kwargs):
        return self.call('non_blocking_wait', kwargs=kwargs)

    def keepalive(self, **kwargs):
        return self.call('keepalive', kwargs=kwargs)

