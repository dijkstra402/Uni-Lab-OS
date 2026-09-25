from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentChemspeedFlexIsynth2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AccelerationConsortium__ac-training-lab', 'source_file': 'src/ac_training_lab/picow/fan-control/lib/EMC2101.py', 'class_name': 'EMC2101', 'import_roots': ['src'], 'candidate_methods': ['enable_tach_input', 'invert_fan_speed', 'config_pwm_clock', 'config_fan_spinup', 'get_lut_hysteresis', 'set_lut_hysteresis', 'set_lut', 'get_lut', 'get_duty_cycle', 'set_duty_cycle', 'set_lut_enabled', 'get_lut_enabled', 'get_fan_min_rpm', 'set_fan_min_rpm', 'get_external_temp', 'get_internal_temp', 'get_fan_rpm', 'get_data_rate', 'set_data_rate', 'set_dac_out_enabled', 'get_dac_out_enabled', 'get_pwm_frequency', 'set_pwm_frequency', 'get_pwm_divisor', 'set_pwm_divisor', 'set_enable_forced_temp', 'get_enable_forced_temp', 'set_forced_temp', 'get_forced_temp', 'make_interpolator', 'read_byte', 'read_bit', 'write_byte', 'write_bit'], 'action_targets': {}, 'metadata': {'repo': 'AccelerationConsortium/ac-training-lab', 'repo_url': 'https://github.com/AccelerationConsortium/ac-training-lab', 'brand': 'Chemspeed', 'model': 'Flex Isynth', 'device_type_cn': '配粉配液站', 'device_type_en': 'Powder & Liquid Dispensing', 'source_framework': '独立驱动', 'tag_id': '4363', 'tag_name': '一体化配粉配液站', 'tag_name_en': 'Integrated Powder & Liquid Dispensing Station', 'candidate_score': 318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def enable_tach_input(self, **kwargs):
        return self.call('enable_tach_input', kwargs=kwargs)

    def invert_fan_speed(self, **kwargs):
        return self.call('invert_fan_speed', kwargs=kwargs)

    def config_pwm_clock(self, **kwargs):
        return self.call('config_pwm_clock', kwargs=kwargs)

    def config_fan_spinup(self, **kwargs):
        return self.call('config_fan_spinup', kwargs=kwargs)

    def get_lut_hysteresis(self, **kwargs):
        return self.call('get_lut_hysteresis', kwargs=kwargs)

    def set_lut_hysteresis(self, **kwargs):
        return self.call('set_lut_hysteresis', kwargs=kwargs)

    def set_lut(self, **kwargs):
        return self.call('set_lut', kwargs=kwargs)

    def get_lut(self, **kwargs):
        return self.call('get_lut', kwargs=kwargs)

    def get_duty_cycle(self, **kwargs):
        return self.call('get_duty_cycle', kwargs=kwargs)

    def set_duty_cycle(self, **kwargs):
        return self.call('set_duty_cycle', kwargs=kwargs)

    def set_lut_enabled(self, **kwargs):
        return self.call('set_lut_enabled', kwargs=kwargs)

    def get_lut_enabled(self, **kwargs):
        return self.call('get_lut_enabled', kwargs=kwargs)

    def get_fan_min_rpm(self, **kwargs):
        return self.call('get_fan_min_rpm', kwargs=kwargs)

    def set_fan_min_rpm(self, **kwargs):
        return self.call('set_fan_min_rpm', kwargs=kwargs)

    def get_external_temp(self, **kwargs):
        return self.call('get_external_temp', kwargs=kwargs)

    def get_internal_temp(self, **kwargs):
        return self.call('get_internal_temp', kwargs=kwargs)

    def get_fan_rpm(self, **kwargs):
        return self.call('get_fan_rpm', kwargs=kwargs)

    def get_data_rate(self, **kwargs):
        return self.call('get_data_rate', kwargs=kwargs)

    def set_data_rate(self, **kwargs):
        return self.call('set_data_rate', kwargs=kwargs)

    def set_dac_out_enabled(self, **kwargs):
        return self.call('set_dac_out_enabled', kwargs=kwargs)

    def get_dac_out_enabled(self, **kwargs):
        return self.call('get_dac_out_enabled', kwargs=kwargs)

    def get_pwm_frequency(self, **kwargs):
        return self.call('get_pwm_frequency', kwargs=kwargs)

    def set_pwm_frequency(self, **kwargs):
        return self.call('set_pwm_frequency', kwargs=kwargs)

    def get_pwm_divisor(self, **kwargs):
        return self.call('get_pwm_divisor', kwargs=kwargs)

    def set_pwm_divisor(self, **kwargs):
        return self.call('set_pwm_divisor', kwargs=kwargs)

    def set_enable_forced_temp(self, **kwargs):
        return self.call('set_enable_forced_temp', kwargs=kwargs)

    def get_enable_forced_temp(self, **kwargs):
        return self.call('get_enable_forced_temp', kwargs=kwargs)

    def set_forced_temp(self, **kwargs):
        return self.call('set_forced_temp', kwargs=kwargs)

    def get_forced_temp(self, **kwargs):
        return self.call('get_forced_temp', kwargs=kwargs)

    def make_interpolator(self, **kwargs):
        return self.call('make_interpolator', kwargs=kwargs)

    def read_byte(self, **kwargs):
        return self.call('read_byte', kwargs=kwargs)

    def read_bit(self, **kwargs):
        return self.call('read_bit', kwargs=kwargs)

    def write_byte(self, **kwargs):
        return self.call('write_byte', kwargs=kwargs)

    def write_bit(self, **kwargs):
        return self.call('write_bit', kwargs=kwargs)

