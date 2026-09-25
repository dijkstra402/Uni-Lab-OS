from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentDwyer16c(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/yaq-project__yaqd-dwyer', 'source_file': 'yaqd_dwyer/_dwyer_16b.py', 'class_name': 'Dwyer16B', 'import_roots': [], 'candidate_methods': ['direct_serial_write', 'get_derivative_constant', 'get_integral_constant', 'get_integral_offset', 'get_output_1_duty', 'get_output_2_duty', 'get_proportional_constant', 'get_ramp_time', 'get_ramp_time_limits', 'get_ramp_time_units', 'get_temperature_regulation_value', 'set_ramp_time', 'set_derivative_constant', 'set_integral_constant', 'set_integral_offset', 'set_proportional_constant', 'update_state'], 'action_targets': {}, 'metadata': {'repo': 'yaq-project/yaqd-dwyer', 'repo_url': 'https://github.com/yaq-project/yaqd-dwyer', 'brand': 'Dwyer', 'model': '16C', 'device_type_cn': '温控器', 'device_type_en': 'Temperature Controller', 'source_framework': 'yaq', 'tag_id': '4438', 'tag_name': '箱式电阻炉', 'tag_name_en': 'Box Resistance Furnace', 'candidate_score': 202, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def direct_serial_write(self, **kwargs):
        return self.call('direct_serial_write', kwargs=kwargs)

    def get_derivative_constant(self, **kwargs):
        return self.call('get_derivative_constant', kwargs=kwargs)

    def get_integral_constant(self, **kwargs):
        return self.call('get_integral_constant', kwargs=kwargs)

    def get_integral_offset(self, **kwargs):
        return self.call('get_integral_offset', kwargs=kwargs)

    def get_output_1_duty(self, **kwargs):
        return self.call('get_output_1_duty', kwargs=kwargs)

    def get_output_2_duty(self, **kwargs):
        return self.call('get_output_2_duty', kwargs=kwargs)

    def get_proportional_constant(self, **kwargs):
        return self.call('get_proportional_constant', kwargs=kwargs)

    def get_ramp_time(self, **kwargs):
        return self.call('get_ramp_time', kwargs=kwargs)

    def get_ramp_time_limits(self, **kwargs):
        return self.call('get_ramp_time_limits', kwargs=kwargs)

    def get_ramp_time_units(self, **kwargs):
        return self.call('get_ramp_time_units', kwargs=kwargs)

    def get_temperature_regulation_value(self, **kwargs):
        return self.call('get_temperature_regulation_value', kwargs=kwargs)

    def set_ramp_time(self, **kwargs):
        return self.call('set_ramp_time', kwargs=kwargs)

    def set_derivative_constant(self, **kwargs):
        return self.call('set_derivative_constant', kwargs=kwargs)

    def set_integral_constant(self, **kwargs):
        return self.call('set_integral_constant', kwargs=kwargs)

    def set_integral_offset(self, **kwargs):
        return self.call('set_integral_offset', kwargs=kwargs)

    def set_proportional_constant(self, **kwargs):
        return self.call('set_proportional_constant', kwargs=kwargs)

    def update_state(self, **kwargs):
        return self.call('update_state', kwargs=kwargs)

