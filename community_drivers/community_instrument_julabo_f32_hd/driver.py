from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentJulaboF32Hd(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/SiLab-Bonn__basil', 'source_file': 'basil/HL/iseg_hv.py', 'class_name': 'IsegHV', 'import_roots': [], 'candidate_methods': ['init', 'set_high_voltage', 'get_high_voltage', 'get_current', 'get_voltage', 'set_voltage', 'get_source_voltage', 'get_hardware_voltage_limit', 'get_voltage_limit', 'set_voltage_limit', 'get_current_limit', 'get_current_trip', 'set_current_trip', 'start_voltage_ramp', 'get_current_channel', 'set_current_channel', 'get_identifier', 'get_ramp_speed', 'set_ramp_speed', 'get_answer_delay', 'set_answer_delay', 'get_autostart', 'set_autostart', 'get_polarity', 'get_status_word', 'get_status_description', 'get_module_status', 'get_module_description', 'read', 'write', 'query', 'on', 'off', 'get_on', 'set_voltage_range', 'set_current', 'source_current', 'soruce_volt', 'UNIT_NUMBER', 'SOFTWARE_REL', 'V_MAX', 'I_MAX', 'hv_on', 'hv_off', 'polarity', 'autostart', 'answer_delay', 'ramp_speed', 'channel', 'current_trip', 'voltage', 'current', 'voltage_target', 'v_lim', 'voltage_limit', 'identifier', 'status_word', 'module_status', 'module_description', 'status_description', 'is_ready', 'wait_for_ready', 'is_initialized', 'set_configuration', 'get_configuration'], 'action_targets': {}, 'metadata': {'repo': 'SiLab-Bonn/basil', 'repo_url': 'https://github.com/SiLab-Bonn/basil', 'brand': 'Julabo', 'model': 'F32-HD', 'device_type_cn': '冷热水机', 'device_type_en': 'Chiller / Heater Unit', 'source_framework': 'basil', 'tag_id': '4369', 'tag_name': '冷热水机', 'tag_name_en': 'Chiller / Heater Unit', 'candidate_score': 518, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def init(self, **kwargs):
        return self.call('init', kwargs=kwargs)

    def set_high_voltage(self, **kwargs):
        return self.call('set_high_voltage', kwargs=kwargs)

    def get_high_voltage(self, **kwargs):
        return self.call('get_high_voltage', kwargs=kwargs)

    def get_current(self, **kwargs):
        return self.call('get_current', kwargs=kwargs)

    def get_voltage(self, **kwargs):
        return self.call('get_voltage', kwargs=kwargs)

    def set_voltage(self, **kwargs):
        return self.call('set_voltage', kwargs=kwargs)

    def get_source_voltage(self, **kwargs):
        return self.call('get_source_voltage', kwargs=kwargs)

    def get_hardware_voltage_limit(self, **kwargs):
        return self.call('get_hardware_voltage_limit', kwargs=kwargs)

    def get_voltage_limit(self, **kwargs):
        return self.call('get_voltage_limit', kwargs=kwargs)

    def set_voltage_limit(self, **kwargs):
        return self.call('set_voltage_limit', kwargs=kwargs)

    def get_current_limit(self, **kwargs):
        return self.call('get_current_limit', kwargs=kwargs)

    def get_current_trip(self, **kwargs):
        return self.call('get_current_trip', kwargs=kwargs)

    def set_current_trip(self, **kwargs):
        return self.call('set_current_trip', kwargs=kwargs)

    def start_voltage_ramp(self, **kwargs):
        return self.call('start_voltage_ramp', kwargs=kwargs)

    def get_current_channel(self, **kwargs):
        return self.call('get_current_channel', kwargs=kwargs)

    def set_current_channel(self, **kwargs):
        return self.call('set_current_channel', kwargs=kwargs)

    def get_identifier(self, **kwargs):
        return self.call('get_identifier', kwargs=kwargs)

    def get_ramp_speed(self, **kwargs):
        return self.call('get_ramp_speed', kwargs=kwargs)

    def set_ramp_speed(self, **kwargs):
        return self.call('set_ramp_speed', kwargs=kwargs)

    def get_answer_delay(self, **kwargs):
        return self.call('get_answer_delay', kwargs=kwargs)

    def set_answer_delay(self, **kwargs):
        return self.call('set_answer_delay', kwargs=kwargs)

    def get_autostart(self, **kwargs):
        return self.call('get_autostart', kwargs=kwargs)

    def set_autostart(self, **kwargs):
        return self.call('set_autostart', kwargs=kwargs)

    def get_polarity(self, **kwargs):
        return self.call('get_polarity', kwargs=kwargs)

    def get_status_word(self, **kwargs):
        return self.call('get_status_word', kwargs=kwargs)

    def get_status_description(self, **kwargs):
        return self.call('get_status_description', kwargs=kwargs)

    def get_module_status(self, **kwargs):
        return self.call('get_module_status', kwargs=kwargs)

    def get_module_description(self, **kwargs):
        return self.call('get_module_description', kwargs=kwargs)

    def read(self, **kwargs):
        return self.call('read', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def on(self, **kwargs):
        return self.call('on', kwargs=kwargs)

    def off(self, **kwargs):
        return self.call('off', kwargs=kwargs)

    def get_on(self, **kwargs):
        return self.call('get_on', kwargs=kwargs)

    def set_voltage_range(self, **kwargs):
        return self.call('set_voltage_range', kwargs=kwargs)

    def set_current(self, **kwargs):
        return self.call('set_current', kwargs=kwargs)

    def source_current(self, **kwargs):
        return self.call('source_current', kwargs=kwargs)

    def soruce_volt(self, **kwargs):
        return self.call('soruce_volt', kwargs=kwargs)

    def UNIT_NUMBER(self, **kwargs):
        return self.call('UNIT_NUMBER', kwargs=kwargs)

    def SOFTWARE_REL(self, **kwargs):
        return self.call('SOFTWARE_REL', kwargs=kwargs)

    def V_MAX(self, **kwargs):
        return self.call('V_MAX', kwargs=kwargs)

    def I_MAX(self, **kwargs):
        return self.call('I_MAX', kwargs=kwargs)

    def hv_on(self, **kwargs):
        return self.call('hv_on', kwargs=kwargs)

    def hv_off(self, **kwargs):
        return self.call('hv_off', kwargs=kwargs)

    def polarity(self, **kwargs):
        return self.call('polarity', kwargs=kwargs)

    def autostart(self, **kwargs):
        return self.call('autostart', kwargs=kwargs)

    def answer_delay(self, **kwargs):
        return self.call('answer_delay', kwargs=kwargs)

    def ramp_speed(self, **kwargs):
        return self.call('ramp_speed', kwargs=kwargs)

    def channel(self, **kwargs):
        return self.call('channel', kwargs=kwargs)

    def current_trip(self, **kwargs):
        return self.call('current_trip', kwargs=kwargs)

    def voltage(self, **kwargs):
        return self.call('voltage', kwargs=kwargs)

    def current(self, **kwargs):
        return self.call('current', kwargs=kwargs)

    def voltage_target(self, **kwargs):
        return self.call('voltage_target', kwargs=kwargs)

    def v_lim(self, **kwargs):
        return self.call('v_lim', kwargs=kwargs)

    def voltage_limit(self, **kwargs):
        return self.call('voltage_limit', kwargs=kwargs)

    def identifier(self, **kwargs):
        return self.call('identifier', kwargs=kwargs)

    def status_word(self, **kwargs):
        return self.call('status_word', kwargs=kwargs)

    def module_status(self, **kwargs):
        return self.call('module_status', kwargs=kwargs)

    def module_description(self, **kwargs):
        return self.call('module_description', kwargs=kwargs)

    def status_description(self, **kwargs):
        return self.call('status_description', kwargs=kwargs)

    def is_ready(self, **kwargs):
        return self.call('is_ready', kwargs=kwargs)

    def wait_for_ready(self, **kwargs):
        return self.call('wait_for_ready', kwargs=kwargs)

    def is_initialized(self, **kwargs):
        return self.call('is_initialized', kwargs=kwargs)

    def set_configuration(self, **kwargs):
        return self.call('set_configuration', kwargs=kwargs)

    def get_configuration(self, **kwargs):
        return self.call('get_configuration', kwargs=kwargs)

