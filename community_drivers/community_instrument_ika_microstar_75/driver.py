from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIkaMicrostar75(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/croningp__pylabware', 'source_file': 'PyLabware/devices/buchi_r300.py', 'class_name': 'R300Rotovap', 'import_roots': [], 'candidate_methods': ['prepare_message', 'parse_reply', 'initialize_device', 'is_connected', 'is_idle', 'check_errors', 'clear_errors', 'get_status', 'get_systemclass', 'get_systemname', 'get_mode', 'set_mode', 'set_timer_time', 'get_timer_set_time', 'get_timer_remaining_time', 'set_solvent_name', 'get_solvent_name', 'set_method_name', 'get_method_name', 'set_clouddest_mode', 'get_clouddest_mode', 'set_clouddest_flask_size', 'get_clouddest_flask_size', 'start', 'stop', 'start_bath', 'stop_bath', 'is_heating_running', 'set_temperature', 'get_temperature', 'get_temperature_setpoint', 'start_chiller', 'stop_chiller', 'is_chiller_running', 'set_chiller_temperature', 'get_chiller_temperature', 'get_chiller_temperature_setpoint', 'start_rotation', 'stop_rotation', 'is_rotation_running', 'set_speed', 'get_speed', 'get_speed_setpoint', 'set_lift_pos', 'get_lift_position', 'lift_up', 'lift_down', 'get_lift_limit', 'get_lift_set', 'start_pressure_regulation', 'stop_pressure_regulation', 'set_pressure', 'get_pressure', 'get_pressure_setpoint', 'vent_on', 'vent_off', 'vent_pulse', 'get_vapor_temperature', 'get_water_in_temperature', 'get_water_out_temperature', 'get_vacuum_aeratevalveopen', 'get_vacuum_vacuumvalveopen', 'get_vacuum_powerpercentact', 'get_globalstatus_onhold', 'get_globalstatus_foamactive', 'set_globalstatus_onhold', 'get_network_dhcp', 'get_network_ip', 'get_network_subnet', 'get_network_gateway', 'get_network_dns', 'get_network_cloudip', 'get_network_cloudenabled', 'get_display_language', 'get_display_brightness', 'get_display_units_temperature', 'get_display_units_pressure', 'get_sounds_buttontone', 'get_sounds_playsoundonfinish', 'get_vacuum_pressurehysteresis', 'get_vacuum_altitude', 'get_vacuum_maxpermpressure', 'get_vacuum_maxpumpoutput', 'get_vacuum_ventonfinish', 'get_rotation_startrotationonstart', 'get_rotation_stoprotationonfinish', 'get_heating_maxtemperature', 'get_heating_stopheatingonfinish', 'get_cooling_stopcoolingonfinish', 'get_lift_depthstop', 'get_lift_immerseonstart', 'get_lift_liftoutflaskonfinish', 'get_program_eco_isenabled', 'get_program_eco_activationaftermins', 'get_program_eco_heatingbathtemperature', 'get_program_eco_coolanttemperature', 'set_display_language', 'set_display_brightness', 'set_display_units_temperature', 'set_display_units_pressure', 'set_sounds_buttontone', 'set_sounds_playsoundonfinish', 'set_vacuum_pressurehysteresis', 'set_vacuum_altitude', 'set_vacuum_maxpermpressure', 'set_vacuum_maxpumpoutput', 'set_vacuum_ventonfinish', 'set_rotation_startrotationonstart', 'set_rotation_stoprotationonfinish', 'set_heating_stopheatingonfinish', 'set_cooling_stopcoolingonfinish', 'set_lift_immerseonstart', 'set_lift_liftoutflaskonfinish', 'set_program_eco_isenabled', 'set_program_eco_activationaftermins', 'set_program_eco_heatingbathtemperature', 'set_program_eco_coolanttemperature', 'get_leaktests', 'start_stirring', 'stop_stirring', 'start_temperature_regulation', 'stop_temperature_regulation', 'simulation', 'connect', 'disconnect', 'send', 'check_value', 'cast_reply_type', 'wait_until_ready', 'execute_when_ready', 'start_task', 'stop_task', 'stop_all_tasks', 'get_all_tasks'], 'action_targets': {}, 'metadata': {'repo': 'croningp/pylabware', 'repo_url': 'https://github.com/croningp/pylabware', 'brand': 'IKA', 'model': 'Microstar 75', 'device_type_cn': '顶置式搅拌器', 'device_type_en': 'Overhead Stirrer', 'source_framework': '反应器/合成设备', 'tag_id': '4401', 'tag_name': '机械搅拌反应釜', 'tag_name_en': 'Mechanical Stirring Reactor', 'candidate_score': 982, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def prepare_message(self, **kwargs):
        return self.call('prepare_message', kwargs=kwargs)

    def parse_reply(self, **kwargs):
        return self.call('parse_reply', kwargs=kwargs)

    def initialize_device(self, **kwargs):
        return self.call('initialize_device', kwargs=kwargs)

    def is_connected(self, **kwargs):
        return self.call('is_connected', kwargs=kwargs)

    def is_idle(self, **kwargs):
        return self.call('is_idle', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def clear_errors(self, **kwargs):
        return self.call('clear_errors', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def get_systemclass(self, **kwargs):
        return self.call('get_systemclass', kwargs=kwargs)

    def get_systemname(self, **kwargs):
        return self.call('get_systemname', kwargs=kwargs)

    def get_mode(self, **kwargs):
        return self.call('get_mode', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def set_timer_time(self, **kwargs):
        return self.call('set_timer_time', kwargs=kwargs)

    def get_timer_set_time(self, **kwargs):
        return self.call('get_timer_set_time', kwargs=kwargs)

    def get_timer_remaining_time(self, **kwargs):
        return self.call('get_timer_remaining_time', kwargs=kwargs)

    def set_solvent_name(self, **kwargs):
        return self.call('set_solvent_name', kwargs=kwargs)

    def get_solvent_name(self, **kwargs):
        return self.call('get_solvent_name', kwargs=kwargs)

    def set_method_name(self, **kwargs):
        return self.call('set_method_name', kwargs=kwargs)

    def get_method_name(self, **kwargs):
        return self.call('get_method_name', kwargs=kwargs)

    def set_clouddest_mode(self, **kwargs):
        return self.call('set_clouddest_mode', kwargs=kwargs)

    def get_clouddest_mode(self, **kwargs):
        return self.call('get_clouddest_mode', kwargs=kwargs)

    def set_clouddest_flask_size(self, **kwargs):
        return self.call('set_clouddest_flask_size', kwargs=kwargs)

    def get_clouddest_flask_size(self, **kwargs):
        return self.call('get_clouddest_flask_size', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def start_bath(self, **kwargs):
        return self.call('start_bath', kwargs=kwargs)

    def stop_bath(self, **kwargs):
        return self.call('stop_bath', kwargs=kwargs)

    def is_heating_running(self, **kwargs):
        return self.call('is_heating_running', kwargs=kwargs)

    def set_temperature(self, **kwargs):
        return self.call('set_temperature', kwargs=kwargs)

    def get_temperature(self, **kwargs):
        return self.call('get_temperature', kwargs=kwargs)

    def get_temperature_setpoint(self, **kwargs):
        return self.call('get_temperature_setpoint', kwargs=kwargs)

    def start_chiller(self, **kwargs):
        return self.call('start_chiller', kwargs=kwargs)

    def stop_chiller(self, **kwargs):
        return self.call('stop_chiller', kwargs=kwargs)

    def is_chiller_running(self, **kwargs):
        return self.call('is_chiller_running', kwargs=kwargs)

    def set_chiller_temperature(self, **kwargs):
        return self.call('set_chiller_temperature', kwargs=kwargs)

    def get_chiller_temperature(self, **kwargs):
        return self.call('get_chiller_temperature', kwargs=kwargs)

    def get_chiller_temperature_setpoint(self, **kwargs):
        return self.call('get_chiller_temperature_setpoint', kwargs=kwargs)

    def start_rotation(self, **kwargs):
        return self.call('start_rotation', kwargs=kwargs)

    def stop_rotation(self, **kwargs):
        return self.call('stop_rotation', kwargs=kwargs)

    def is_rotation_running(self, **kwargs):
        return self.call('is_rotation_running', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

    def get_speed(self, **kwargs):
        return self.call('get_speed', kwargs=kwargs)

    def get_speed_setpoint(self, **kwargs):
        return self.call('get_speed_setpoint', kwargs=kwargs)

    def set_lift_pos(self, **kwargs):
        return self.call('set_lift_pos', kwargs=kwargs)

    def get_lift_position(self, **kwargs):
        return self.call('get_lift_position', kwargs=kwargs)

    def lift_up(self, **kwargs):
        return self.call('lift_up', kwargs=kwargs)

    def lift_down(self, **kwargs):
        return self.call('lift_down', kwargs=kwargs)

    def get_lift_limit(self, **kwargs):
        return self.call('get_lift_limit', kwargs=kwargs)

    def get_lift_set(self, **kwargs):
        return self.call('get_lift_set', kwargs=kwargs)

    def start_pressure_regulation(self, **kwargs):
        return self.call('start_pressure_regulation', kwargs=kwargs)

    def stop_pressure_regulation(self, **kwargs):
        return self.call('stop_pressure_regulation', kwargs=kwargs)

    def set_pressure(self, **kwargs):
        return self.call('set_pressure', kwargs=kwargs)

    def get_pressure(self, **kwargs):
        return self.call('get_pressure', kwargs=kwargs)

    def get_pressure_setpoint(self, **kwargs):
        return self.call('get_pressure_setpoint', kwargs=kwargs)

    def vent_on(self, **kwargs):
        return self.call('vent_on', kwargs=kwargs)

    def vent_off(self, **kwargs):
        return self.call('vent_off', kwargs=kwargs)

    def vent_pulse(self, **kwargs):
        return self.call('vent_pulse', kwargs=kwargs)

    def get_vapor_temperature(self, **kwargs):
        return self.call('get_vapor_temperature', kwargs=kwargs)

    def get_water_in_temperature(self, **kwargs):
        return self.call('get_water_in_temperature', kwargs=kwargs)

    def get_water_out_temperature(self, **kwargs):
        return self.call('get_water_out_temperature', kwargs=kwargs)

    def get_vacuum_aeratevalveopen(self, **kwargs):
        return self.call('get_vacuum_aeratevalveopen', kwargs=kwargs)

    def get_vacuum_vacuumvalveopen(self, **kwargs):
        return self.call('get_vacuum_vacuumvalveopen', kwargs=kwargs)

    def get_vacuum_powerpercentact(self, **kwargs):
        return self.call('get_vacuum_powerpercentact', kwargs=kwargs)

    def get_globalstatus_onhold(self, **kwargs):
        return self.call('get_globalstatus_onhold', kwargs=kwargs)

    def get_globalstatus_foamactive(self, **kwargs):
        return self.call('get_globalstatus_foamactive', kwargs=kwargs)

    def set_globalstatus_onhold(self, **kwargs):
        return self.call('set_globalstatus_onhold', kwargs=kwargs)

    def get_network_dhcp(self, **kwargs):
        return self.call('get_network_dhcp', kwargs=kwargs)

    def get_network_ip(self, **kwargs):
        return self.call('get_network_ip', kwargs=kwargs)

    def get_network_subnet(self, **kwargs):
        return self.call('get_network_subnet', kwargs=kwargs)

    def get_network_gateway(self, **kwargs):
        return self.call('get_network_gateway', kwargs=kwargs)

    def get_network_dns(self, **kwargs):
        return self.call('get_network_dns', kwargs=kwargs)

    def get_network_cloudip(self, **kwargs):
        return self.call('get_network_cloudip', kwargs=kwargs)

    def get_network_cloudenabled(self, **kwargs):
        return self.call('get_network_cloudenabled', kwargs=kwargs)

    def get_display_language(self, **kwargs):
        return self.call('get_display_language', kwargs=kwargs)

    def get_display_brightness(self, **kwargs):
        return self.call('get_display_brightness', kwargs=kwargs)

    def get_display_units_temperature(self, **kwargs):
        return self.call('get_display_units_temperature', kwargs=kwargs)

    def get_display_units_pressure(self, **kwargs):
        return self.call('get_display_units_pressure', kwargs=kwargs)

    def get_sounds_buttontone(self, **kwargs):
        return self.call('get_sounds_buttontone', kwargs=kwargs)

    def get_sounds_playsoundonfinish(self, **kwargs):
        return self.call('get_sounds_playsoundonfinish', kwargs=kwargs)

    def get_vacuum_pressurehysteresis(self, **kwargs):
        return self.call('get_vacuum_pressurehysteresis', kwargs=kwargs)

    def get_vacuum_altitude(self, **kwargs):
        return self.call('get_vacuum_altitude', kwargs=kwargs)

    def get_vacuum_maxpermpressure(self, **kwargs):
        return self.call('get_vacuum_maxpermpressure', kwargs=kwargs)

    def get_vacuum_maxpumpoutput(self, **kwargs):
        return self.call('get_vacuum_maxpumpoutput', kwargs=kwargs)

    def get_vacuum_ventonfinish(self, **kwargs):
        return self.call('get_vacuum_ventonfinish', kwargs=kwargs)

    def get_rotation_startrotationonstart(self, **kwargs):
        return self.call('get_rotation_startrotationonstart', kwargs=kwargs)

    def get_rotation_stoprotationonfinish(self, **kwargs):
        return self.call('get_rotation_stoprotationonfinish', kwargs=kwargs)

    def get_heating_maxtemperature(self, **kwargs):
        return self.call('get_heating_maxtemperature', kwargs=kwargs)

    def get_heating_stopheatingonfinish(self, **kwargs):
        return self.call('get_heating_stopheatingonfinish', kwargs=kwargs)

    def get_cooling_stopcoolingonfinish(self, **kwargs):
        return self.call('get_cooling_stopcoolingonfinish', kwargs=kwargs)

    def get_lift_depthstop(self, **kwargs):
        return self.call('get_lift_depthstop', kwargs=kwargs)

    def get_lift_immerseonstart(self, **kwargs):
        return self.call('get_lift_immerseonstart', kwargs=kwargs)

    def get_lift_liftoutflaskonfinish(self, **kwargs):
        return self.call('get_lift_liftoutflaskonfinish', kwargs=kwargs)

    def get_program_eco_isenabled(self, **kwargs):
        return self.call('get_program_eco_isenabled', kwargs=kwargs)

    def get_program_eco_activationaftermins(self, **kwargs):
        return self.call('get_program_eco_activationaftermins', kwargs=kwargs)

    def get_program_eco_heatingbathtemperature(self, **kwargs):
        return self.call('get_program_eco_heatingbathtemperature', kwargs=kwargs)

    def get_program_eco_coolanttemperature(self, **kwargs):
        return self.call('get_program_eco_coolanttemperature', kwargs=kwargs)

    def set_display_language(self, **kwargs):
        return self.call('set_display_language', kwargs=kwargs)

    def set_display_brightness(self, **kwargs):
        return self.call('set_display_brightness', kwargs=kwargs)

    def set_display_units_temperature(self, **kwargs):
        return self.call('set_display_units_temperature', kwargs=kwargs)

    def set_display_units_pressure(self, **kwargs):
        return self.call('set_display_units_pressure', kwargs=kwargs)

    def set_sounds_buttontone(self, **kwargs):
        return self.call('set_sounds_buttontone', kwargs=kwargs)

    def set_sounds_playsoundonfinish(self, **kwargs):
        return self.call('set_sounds_playsoundonfinish', kwargs=kwargs)

    def set_vacuum_pressurehysteresis(self, **kwargs):
        return self.call('set_vacuum_pressurehysteresis', kwargs=kwargs)

    def set_vacuum_altitude(self, **kwargs):
        return self.call('set_vacuum_altitude', kwargs=kwargs)

    def set_vacuum_maxpermpressure(self, **kwargs):
        return self.call('set_vacuum_maxpermpressure', kwargs=kwargs)

    def set_vacuum_maxpumpoutput(self, **kwargs):
        return self.call('set_vacuum_maxpumpoutput', kwargs=kwargs)

    def set_vacuum_ventonfinish(self, **kwargs):
        return self.call('set_vacuum_ventonfinish', kwargs=kwargs)

    def set_rotation_startrotationonstart(self, **kwargs):
        return self.call('set_rotation_startrotationonstart', kwargs=kwargs)

    def set_rotation_stoprotationonfinish(self, **kwargs):
        return self.call('set_rotation_stoprotationonfinish', kwargs=kwargs)

    def set_heating_stopheatingonfinish(self, **kwargs):
        return self.call('set_heating_stopheatingonfinish', kwargs=kwargs)

    def set_cooling_stopcoolingonfinish(self, **kwargs):
        return self.call('set_cooling_stopcoolingonfinish', kwargs=kwargs)

    def set_lift_immerseonstart(self, **kwargs):
        return self.call('set_lift_immerseonstart', kwargs=kwargs)

    def set_lift_liftoutflaskonfinish(self, **kwargs):
        return self.call('set_lift_liftoutflaskonfinish', kwargs=kwargs)

    def set_program_eco_isenabled(self, **kwargs):
        return self.call('set_program_eco_isenabled', kwargs=kwargs)

    def set_program_eco_activationaftermins(self, **kwargs):
        return self.call('set_program_eco_activationaftermins', kwargs=kwargs)

    def set_program_eco_heatingbathtemperature(self, **kwargs):
        return self.call('set_program_eco_heatingbathtemperature', kwargs=kwargs)

    def set_program_eco_coolanttemperature(self, **kwargs):
        return self.call('set_program_eco_coolanttemperature', kwargs=kwargs)

    def get_leaktests(self, **kwargs):
        return self.call('get_leaktests', kwargs=kwargs)

    def start_stirring(self, **kwargs):
        return self.call('start_stirring', kwargs=kwargs)

    def stop_stirring(self, **kwargs):
        return self.call('stop_stirring', kwargs=kwargs)

    def start_temperature_regulation(self, **kwargs):
        return self.call('start_temperature_regulation', kwargs=kwargs)

    def stop_temperature_regulation(self, **kwargs):
        return self.call('stop_temperature_regulation', kwargs=kwargs)

    def simulation(self, **kwargs):
        return self.call('simulation', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def send(self, **kwargs):
        return self.call('send', kwargs=kwargs)

    def check_value(self, **kwargs):
        return self.call('check_value', kwargs=kwargs)

    def cast_reply_type(self, **kwargs):
        return self.call('cast_reply_type', kwargs=kwargs)

    def wait_until_ready(self, **kwargs):
        return self.call('wait_until_ready', kwargs=kwargs)

    def execute_when_ready(self, **kwargs):
        return self.call('execute_when_ready', kwargs=kwargs)

    def start_task(self, **kwargs):
        return self.call('start_task', kwargs=kwargs)

    def stop_task(self, **kwargs):
        return self.call('stop_task', kwargs=kwargs)

    def stop_all_tasks(self, **kwargs):
        return self.call('stop_all_tasks', kwargs=kwargs)

    def get_all_tasks(self, **kwargs):
        return self.call('get_all_tasks', kwargs=kwargs)

