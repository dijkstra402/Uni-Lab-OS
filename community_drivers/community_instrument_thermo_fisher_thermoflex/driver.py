from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThermoFisherThermoflex(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Dennis-van-Gils__python-dvg-devices', 'source_file': 'src/dvg_devices/ThermoFlex_chiller_protocol_RS232.py', 'class_name': 'ThermoFlex_chiller', 'import_roots': ['src'], 'candidate_methods': ['query', 'ID_validation_query', 'begin', 'query_data_as_float_and_uom', 'parse_data_bytes', 'parse_status_bits', 'parse_ASCII_bytes', 'turn_off', 'turn_on', 'query_is_on', 'query_Ack', 'query_alarm_values_and_units', 'query_alarm_LO_flow', 'query_alarm_LO_temp', 'query_alarm_LO_pres', 'query_alarm_HI_flow', 'query_alarm_HI_temp', 'query_alarm_HI_pres', 'query_PID_values', 'query_PID_P', 'query_PID_I', 'query_PID_D', 'query_status_bits', 'query_state', 'query_setpoint', 'query_temp', 'query_flow', 'query_supply_pres', 'query_suction_pres', 'query_display_msg', 'send_setpoint', 'set_read_termination', 'set_write_termination', 'set_ID_validation_query', 'readline', 'query_bytes', 'query_ascii_values', 'connect_at_port', 'scan_ports', 'auto_connect'], 'action_targets': {}, 'metadata': {'repo': 'Dennis-van-Gils/python-dvg-devices', 'repo_url': 'https://github.com/Dennis-van-Gils/python-dvg-devices', 'brand': 'Thermo Fisher', 'model': 'ThermoFlex', 'device_type_cn': '冷水机', 'device_type_en': 'Chiller', 'source_framework': '独立仓库', 'tag_id': '4369', 'tag_name': '冷热水机', 'tag_name_en': 'Chiller / Heater Unit', 'candidate_score': 384, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def ID_validation_query(self, **kwargs):
        return self.call('ID_validation_query', kwargs=kwargs)

    def begin(self, **kwargs):
        return self.call('begin', kwargs=kwargs)

    def query_data_as_float_and_uom(self, **kwargs):
        return self.call('query_data_as_float_and_uom', kwargs=kwargs)

    def parse_data_bytes(self, **kwargs):
        return self.call('parse_data_bytes', kwargs=kwargs)

    def parse_status_bits(self, **kwargs):
        return self.call('parse_status_bits', kwargs=kwargs)

    def parse_ASCII_bytes(self, **kwargs):
        return self.call('parse_ASCII_bytes', kwargs=kwargs)

    def turn_off(self, **kwargs):
        return self.call('turn_off', kwargs=kwargs)

    def turn_on(self, **kwargs):
        return self.call('turn_on', kwargs=kwargs)

    def query_is_on(self, **kwargs):
        return self.call('query_is_on', kwargs=kwargs)

    def query_Ack(self, **kwargs):
        return self.call('query_Ack', kwargs=kwargs)

    def query_alarm_values_and_units(self, **kwargs):
        return self.call('query_alarm_values_and_units', kwargs=kwargs)

    def query_alarm_LO_flow(self, **kwargs):
        return self.call('query_alarm_LO_flow', kwargs=kwargs)

    def query_alarm_LO_temp(self, **kwargs):
        return self.call('query_alarm_LO_temp', kwargs=kwargs)

    def query_alarm_LO_pres(self, **kwargs):
        return self.call('query_alarm_LO_pres', kwargs=kwargs)

    def query_alarm_HI_flow(self, **kwargs):
        return self.call('query_alarm_HI_flow', kwargs=kwargs)

    def query_alarm_HI_temp(self, **kwargs):
        return self.call('query_alarm_HI_temp', kwargs=kwargs)

    def query_alarm_HI_pres(self, **kwargs):
        return self.call('query_alarm_HI_pres', kwargs=kwargs)

    def query_PID_values(self, **kwargs):
        return self.call('query_PID_values', kwargs=kwargs)

    def query_PID_P(self, **kwargs):
        return self.call('query_PID_P', kwargs=kwargs)

    def query_PID_I(self, **kwargs):
        return self.call('query_PID_I', kwargs=kwargs)

    def query_PID_D(self, **kwargs):
        return self.call('query_PID_D', kwargs=kwargs)

    def query_status_bits(self, **kwargs):
        return self.call('query_status_bits', kwargs=kwargs)

    def query_state(self, **kwargs):
        return self.call('query_state', kwargs=kwargs)

    def query_setpoint(self, **kwargs):
        return self.call('query_setpoint', kwargs=kwargs)

    def query_temp(self, **kwargs):
        return self.call('query_temp', kwargs=kwargs)

    def query_flow(self, **kwargs):
        return self.call('query_flow', kwargs=kwargs)

    def query_supply_pres(self, **kwargs):
        return self.call('query_supply_pres', kwargs=kwargs)

    def query_suction_pres(self, **kwargs):
        return self.call('query_suction_pres', kwargs=kwargs)

    def query_display_msg(self, **kwargs):
        return self.call('query_display_msg', kwargs=kwargs)

    def send_setpoint(self, **kwargs):
        return self.call('send_setpoint', kwargs=kwargs)

    def set_read_termination(self, **kwargs):
        return self.call('set_read_termination', kwargs=kwargs)

    def set_write_termination(self, **kwargs):
        return self.call('set_write_termination', kwargs=kwargs)

    def set_ID_validation_query(self, **kwargs):
        return self.call('set_ID_validation_query', kwargs=kwargs)

    def readline(self, **kwargs):
        return self.call('readline', kwargs=kwargs)

    def query_bytes(self, **kwargs):
        return self.call('query_bytes', kwargs=kwargs)

    def query_ascii_values(self, **kwargs):
        return self.call('query_ascii_values', kwargs=kwargs)

    def connect_at_port(self, **kwargs):
        return self.call('connect_at_port', kwargs=kwargs)

    def scan_ports(self, **kwargs):
        return self.call('scan_ports', kwargs=kwargs)

    def auto_connect(self, **kwargs):
        return self.call('auto_connect', kwargs=kwargs)

