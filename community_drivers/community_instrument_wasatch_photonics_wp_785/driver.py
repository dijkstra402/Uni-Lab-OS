from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentWasatchPhotonicsWp785(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/WasatchPhotonics__Wasatch.PY', 'source_file': 'wasatch/FeatureIdentificationDevice.py', 'class_name': 'FeatureIdentificationDevice', 'import_roots': [], 'candidate_methods': ['handle_requests', 'connect', 'reset_area_scan_frame', 'disconnect', 'reset', 'get_upper_code', 'has_linearity_coeffs', 'get_battery_register', 'get_battery_state_raw', 'get_battery_percentage', 'get_battery_charging', 'get_integration_time_ms', 'set_dfu_enable', 'set_detector_offset', 'set_detector_offset_odd', 'get_detector_gain', 'get_detector_gain_odd', 'set_detector_gain', 'set_detector_gain_odd', 'set_area_scan_enable', 'set_area_scan_line_step', 'set_area_scan_line_count', 'set_area_scan_line_interval', 'get_sensor_line_length', 'get_microcontroller_firmware_version', 'get_fpga_firmware_version', 'get_microcontroller_serial_number', 'get_ble_firmware_version', 'apply_edc', 'get_line', 'generate_timeout_ms', 'get_spectrum', 'require_throwaway', 'set_onboard_scans_to_average', 'get_scans_to_average', 'set_integration_time_ms', 'is_sensor_stable', 'get_poll_status', 'i2c_write', 'get_area_scan', 'get_area_scan_xs', 'get_area_scan_hamamatsu', 'get_dac', 'select_adc', 'get_secondary_adc_calibrated', 'get_secondary_adc_raw', 'set_laser_tec_mode', 'get_laser_tec_mode', 'get_laser_temperature_degC', 'get_detector_temperature_raw', 'get_detector_temperature_degC', 'set_detector_tec_setpoint_degC', 'get_detector_tec_setpoint_degC', 'get_detector_tec_setpoint_raw', 'set_tec_enable', 'set_trigger_source', 'set_high_gain_mode_enable', 'get_high_gain_mode_enabled', 'get_opt_laser_control', 'get_opt_has_laser', 'get_laser_temperature_raw', 'set_selected_laser', 'get_selected_laser', 'get_laser_enabled', 'set_laser_enable', 'set_laser_power_mW', 'set_laser_power_high_resolution', 'set_laser_power_require_modulation', 'set_laser_power_perc', 'set_laser_power_perc_immediate', 'get_laser_temperature_setpoint_raw', 'set_laser_temperature_setpoint_raw', 'set_laser_warning_delay_sec', 'get_laser_warning_delay_sec', 'set_laser_power_attenuator', 'get_laser_power_attenuator', 'get_laser_interlock', 'can_laser_fire', 'is_laser_firing', 'reset_fpga', 'get_trigger_source', 'get_raman_mode_enabled_NOT_USED', 'set_raman_mode_enable_NOT_USED', 'get_raman_delay_ms', 'set_raman_delay_ms', 'get_laser_watchdog_sec', 'set_laser_watchdog_sec', 'update_laser_watchdog', 'update_vertical_roi', 'set_vertical_roi', 'set_pixel_mode', 'clear_regions', 'set_single_region', 'set_detector_roi', 'get_fpga_configuration_register', 'set_accessory_enable', 'get_discretes_enabled', 'set_fan_enable', 'get_fan_enabled', 'set_lamp_enable', 'get_lamp_enabled', 'set_shutter_enable', 'get_shutter_enabled', 'set_mod_enable', 'get_mod_enabled', 'set_mod_period_us', 'get_mod_period_us', 'set_mod_width_us', 'get_mod_width_us', 'set_mod_delay_us', 'get_mod_delay_us', 'set_mod_duration_us_NOT_USED', 'get_mod_duration_us', 'set_strobe_enable', 'get_strobe_enabled', 'get_ambient_temperature_degC', 'get_ambient_temperature_degC_arm', 'get_ambient_temperature_degC_gen15', 'get_tec_enabled', 'get_actual_frames', 'get_actual_integration_time_us', 'get_detector_offset', 'get_detector_offset_odd', 'get_ccd_sensing_threshold', 'get_ccd_threshold_sensing_mode', 'get_external_trigger_output', 'set_mod_linked_to_integration', 'get_mod_linked_to_integration', 'get_selected_adc', 'set_trigger_delay', 'get_trigger_delay', 'get_vr_continuous_ccd', 'get_vr_num_frames', 'get_opt_actual_integration_time', 'get_opt_area_scan', 'get_opt_cf_select', 'get_opt_data_header_tab', 'get_opt_horizontal_binning', 'get_opt_integration_time_resolution', 'update_firmware_log', 'set_analog_output_mode', 'set_analog_output_value', 'get_analog_output_state', 'get_analog_input_value', 'update_session_eeprom', 'replace_session_eeprom', 'write_eeprom', 'set_log_level', 'queue_message', 'check_alert', 'refresh_alerts'], 'action_targets': {}, 'metadata': {'repo': 'WasatchPhotonics/Wasatch.PY', 'repo_url': 'https://github.com/WasatchPhotonics/Wasatch.PY', 'brand': 'Wasatch Photonics', 'model': 'WP-785', 'device_type_cn': '拉曼光谱仪', 'device_type_en': 'Raman Spectrometer', 'source_framework': 'Wasatch.PY', 'tag_id': '4392', 'tag_name': '拉曼光谱仪', 'tag_name_en': 'Raman Spectrometer', 'candidate_score': 1254, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def handle_requests(self, **kwargs):
        return self.call('handle_requests', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def reset_area_scan_frame(self, **kwargs):
        return self.call('reset_area_scan_frame', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def get_upper_code(self, **kwargs):
        return self.call('get_upper_code', kwargs=kwargs)

    def has_linearity_coeffs(self, **kwargs):
        return self.call('has_linearity_coeffs', kwargs=kwargs)

    def get_battery_register(self, **kwargs):
        return self.call('get_battery_register', kwargs=kwargs)

    def get_battery_state_raw(self, **kwargs):
        return self.call('get_battery_state_raw', kwargs=kwargs)

    def get_battery_percentage(self, **kwargs):
        return self.call('get_battery_percentage', kwargs=kwargs)

    def get_battery_charging(self, **kwargs):
        return self.call('get_battery_charging', kwargs=kwargs)

    def get_integration_time_ms(self, **kwargs):
        return self.call('get_integration_time_ms', kwargs=kwargs)

    def set_dfu_enable(self, **kwargs):
        return self.call('set_dfu_enable', kwargs=kwargs)

    def set_detector_offset(self, **kwargs):
        return self.call('set_detector_offset', kwargs=kwargs)

    def set_detector_offset_odd(self, **kwargs):
        return self.call('set_detector_offset_odd', kwargs=kwargs)

    def get_detector_gain(self, **kwargs):
        return self.call('get_detector_gain', kwargs=kwargs)

    def get_detector_gain_odd(self, **kwargs):
        return self.call('get_detector_gain_odd', kwargs=kwargs)

    def set_detector_gain(self, **kwargs):
        return self.call('set_detector_gain', kwargs=kwargs)

    def set_detector_gain_odd(self, **kwargs):
        return self.call('set_detector_gain_odd', kwargs=kwargs)

    def set_area_scan_enable(self, **kwargs):
        return self.call('set_area_scan_enable', kwargs=kwargs)

    def set_area_scan_line_step(self, **kwargs):
        return self.call('set_area_scan_line_step', kwargs=kwargs)

    def set_area_scan_line_count(self, **kwargs):
        return self.call('set_area_scan_line_count', kwargs=kwargs)

    def set_area_scan_line_interval(self, **kwargs):
        return self.call('set_area_scan_line_interval', kwargs=kwargs)

    def get_sensor_line_length(self, **kwargs):
        return self.call('get_sensor_line_length', kwargs=kwargs)

    def get_microcontroller_firmware_version(self, **kwargs):
        return self.call('get_microcontroller_firmware_version', kwargs=kwargs)

    def get_fpga_firmware_version(self, **kwargs):
        return self.call('get_fpga_firmware_version', kwargs=kwargs)

    def get_microcontroller_serial_number(self, **kwargs):
        return self.call('get_microcontroller_serial_number', kwargs=kwargs)

    def get_ble_firmware_version(self, **kwargs):
        return self.call('get_ble_firmware_version', kwargs=kwargs)

    def apply_edc(self, **kwargs):
        return self.call('apply_edc', kwargs=kwargs)

    def get_line(self, **kwargs):
        return self.call('get_line', kwargs=kwargs)

    def generate_timeout_ms(self, **kwargs):
        return self.call('generate_timeout_ms', kwargs=kwargs)

    def get_spectrum(self, **kwargs):
        return self.call('get_spectrum', kwargs=kwargs)

    def require_throwaway(self, **kwargs):
        return self.call('require_throwaway', kwargs=kwargs)

    def set_onboard_scans_to_average(self, **kwargs):
        return self.call('set_onboard_scans_to_average', kwargs=kwargs)

    def get_scans_to_average(self, **kwargs):
        return self.call('get_scans_to_average', kwargs=kwargs)

    def set_integration_time_ms(self, **kwargs):
        return self.call('set_integration_time_ms', kwargs=kwargs)

    def is_sensor_stable(self, **kwargs):
        return self.call('is_sensor_stable', kwargs=kwargs)

    def get_poll_status(self, **kwargs):
        return self.call('get_poll_status', kwargs=kwargs)

    def i2c_write(self, **kwargs):
        return self.call('i2c_write', kwargs=kwargs)

    def get_area_scan(self, **kwargs):
        return self.call('get_area_scan', kwargs=kwargs)

    def get_area_scan_xs(self, **kwargs):
        return self.call('get_area_scan_xs', kwargs=kwargs)

    def get_area_scan_hamamatsu(self, **kwargs):
        return self.call('get_area_scan_hamamatsu', kwargs=kwargs)

    def get_dac(self, **kwargs):
        return self.call('get_dac', kwargs=kwargs)

    def select_adc(self, **kwargs):
        return self.call('select_adc', kwargs=kwargs)

    def get_secondary_adc_calibrated(self, **kwargs):
        return self.call('get_secondary_adc_calibrated', kwargs=kwargs)

    def get_secondary_adc_raw(self, **kwargs):
        return self.call('get_secondary_adc_raw', kwargs=kwargs)

    def set_laser_tec_mode(self, **kwargs):
        return self.call('set_laser_tec_mode', kwargs=kwargs)

    def get_laser_tec_mode(self, **kwargs):
        return self.call('get_laser_tec_mode', kwargs=kwargs)

    def get_laser_temperature_degC(self, **kwargs):
        return self.call('get_laser_temperature_degC', kwargs=kwargs)

    def get_detector_temperature_raw(self, **kwargs):
        return self.call('get_detector_temperature_raw', kwargs=kwargs)

    def get_detector_temperature_degC(self, **kwargs):
        return self.call('get_detector_temperature_degC', kwargs=kwargs)

    def set_detector_tec_setpoint_degC(self, **kwargs):
        return self.call('set_detector_tec_setpoint_degC', kwargs=kwargs)

    def get_detector_tec_setpoint_degC(self, **kwargs):
        return self.call('get_detector_tec_setpoint_degC', kwargs=kwargs)

    def get_detector_tec_setpoint_raw(self, **kwargs):
        return self.call('get_detector_tec_setpoint_raw', kwargs=kwargs)

    def set_tec_enable(self, **kwargs):
        return self.call('set_tec_enable', kwargs=kwargs)

    def set_trigger_source(self, **kwargs):
        return self.call('set_trigger_source', kwargs=kwargs)

    def set_high_gain_mode_enable(self, **kwargs):
        return self.call('set_high_gain_mode_enable', kwargs=kwargs)

    def get_high_gain_mode_enabled(self, **kwargs):
        return self.call('get_high_gain_mode_enabled', kwargs=kwargs)

    def get_opt_laser_control(self, **kwargs):
        return self.call('get_opt_laser_control', kwargs=kwargs)

    def get_opt_has_laser(self, **kwargs):
        return self.call('get_opt_has_laser', kwargs=kwargs)

    def get_laser_temperature_raw(self, **kwargs):
        return self.call('get_laser_temperature_raw', kwargs=kwargs)

    def set_selected_laser(self, **kwargs):
        return self.call('set_selected_laser', kwargs=kwargs)

    def get_selected_laser(self, **kwargs):
        return self.call('get_selected_laser', kwargs=kwargs)

    def get_laser_enabled(self, **kwargs):
        return self.call('get_laser_enabled', kwargs=kwargs)

    def set_laser_enable(self, **kwargs):
        return self.call('set_laser_enable', kwargs=kwargs)

    def set_laser_power_mW(self, **kwargs):
        return self.call('set_laser_power_mW', kwargs=kwargs)

    def set_laser_power_high_resolution(self, **kwargs):
        return self.call('set_laser_power_high_resolution', kwargs=kwargs)

    def set_laser_power_require_modulation(self, **kwargs):
        return self.call('set_laser_power_require_modulation', kwargs=kwargs)

    def set_laser_power_perc(self, **kwargs):
        return self.call('set_laser_power_perc', kwargs=kwargs)

    def set_laser_power_perc_immediate(self, **kwargs):
        return self.call('set_laser_power_perc_immediate', kwargs=kwargs)

    def get_laser_temperature_setpoint_raw(self, **kwargs):
        return self.call('get_laser_temperature_setpoint_raw', kwargs=kwargs)

    def set_laser_temperature_setpoint_raw(self, **kwargs):
        return self.call('set_laser_temperature_setpoint_raw', kwargs=kwargs)

    def set_laser_warning_delay_sec(self, **kwargs):
        return self.call('set_laser_warning_delay_sec', kwargs=kwargs)

    def get_laser_warning_delay_sec(self, **kwargs):
        return self.call('get_laser_warning_delay_sec', kwargs=kwargs)

    def set_laser_power_attenuator(self, **kwargs):
        return self.call('set_laser_power_attenuator', kwargs=kwargs)

    def get_laser_power_attenuator(self, **kwargs):
        return self.call('get_laser_power_attenuator', kwargs=kwargs)

    def get_laser_interlock(self, **kwargs):
        return self.call('get_laser_interlock', kwargs=kwargs)

    def can_laser_fire(self, **kwargs):
        return self.call('can_laser_fire', kwargs=kwargs)

    def is_laser_firing(self, **kwargs):
        return self.call('is_laser_firing', kwargs=kwargs)

    def reset_fpga(self, **kwargs):
        return self.call('reset_fpga', kwargs=kwargs)

    def get_trigger_source(self, **kwargs):
        return self.call('get_trigger_source', kwargs=kwargs)

    def get_raman_mode_enabled_NOT_USED(self, **kwargs):
        return self.call('get_raman_mode_enabled_NOT_USED', kwargs=kwargs)

    def set_raman_mode_enable_NOT_USED(self, **kwargs):
        return self.call('set_raman_mode_enable_NOT_USED', kwargs=kwargs)

    def get_raman_delay_ms(self, **kwargs):
        return self.call('get_raman_delay_ms', kwargs=kwargs)

    def set_raman_delay_ms(self, **kwargs):
        return self.call('set_raman_delay_ms', kwargs=kwargs)

    def get_laser_watchdog_sec(self, **kwargs):
        return self.call('get_laser_watchdog_sec', kwargs=kwargs)

    def set_laser_watchdog_sec(self, **kwargs):
        return self.call('set_laser_watchdog_sec', kwargs=kwargs)

    def update_laser_watchdog(self, **kwargs):
        return self.call('update_laser_watchdog', kwargs=kwargs)

    def update_vertical_roi(self, **kwargs):
        return self.call('update_vertical_roi', kwargs=kwargs)

    def set_vertical_roi(self, **kwargs):
        return self.call('set_vertical_roi', kwargs=kwargs)

    def set_pixel_mode(self, **kwargs):
        return self.call('set_pixel_mode', kwargs=kwargs)

    def clear_regions(self, **kwargs):
        return self.call('clear_regions', kwargs=kwargs)

    def set_single_region(self, **kwargs):
        return self.call('set_single_region', kwargs=kwargs)

    def set_detector_roi(self, **kwargs):
        return self.call('set_detector_roi', kwargs=kwargs)

    def get_fpga_configuration_register(self, **kwargs):
        return self.call('get_fpga_configuration_register', kwargs=kwargs)

    def set_accessory_enable(self, **kwargs):
        return self.call('set_accessory_enable', kwargs=kwargs)

    def get_discretes_enabled(self, **kwargs):
        return self.call('get_discretes_enabled', kwargs=kwargs)

    def set_fan_enable(self, **kwargs):
        return self.call('set_fan_enable', kwargs=kwargs)

    def get_fan_enabled(self, **kwargs):
        return self.call('get_fan_enabled', kwargs=kwargs)

    def set_lamp_enable(self, **kwargs):
        return self.call('set_lamp_enable', kwargs=kwargs)

    def get_lamp_enabled(self, **kwargs):
        return self.call('get_lamp_enabled', kwargs=kwargs)

    def set_shutter_enable(self, **kwargs):
        return self.call('set_shutter_enable', kwargs=kwargs)

    def get_shutter_enabled(self, **kwargs):
        return self.call('get_shutter_enabled', kwargs=kwargs)

    def set_mod_enable(self, **kwargs):
        return self.call('set_mod_enable', kwargs=kwargs)

    def get_mod_enabled(self, **kwargs):
        return self.call('get_mod_enabled', kwargs=kwargs)

    def set_mod_period_us(self, **kwargs):
        return self.call('set_mod_period_us', kwargs=kwargs)

    def get_mod_period_us(self, **kwargs):
        return self.call('get_mod_period_us', kwargs=kwargs)

    def set_mod_width_us(self, **kwargs):
        return self.call('set_mod_width_us', kwargs=kwargs)

    def get_mod_width_us(self, **kwargs):
        return self.call('get_mod_width_us', kwargs=kwargs)

    def set_mod_delay_us(self, **kwargs):
        return self.call('set_mod_delay_us', kwargs=kwargs)

    def get_mod_delay_us(self, **kwargs):
        return self.call('get_mod_delay_us', kwargs=kwargs)

    def set_mod_duration_us_NOT_USED(self, **kwargs):
        return self.call('set_mod_duration_us_NOT_USED', kwargs=kwargs)

    def get_mod_duration_us(self, **kwargs):
        return self.call('get_mod_duration_us', kwargs=kwargs)

    def set_strobe_enable(self, **kwargs):
        return self.call('set_strobe_enable', kwargs=kwargs)

    def get_strobe_enabled(self, **kwargs):
        return self.call('get_strobe_enabled', kwargs=kwargs)

    def get_ambient_temperature_degC(self, **kwargs):
        return self.call('get_ambient_temperature_degC', kwargs=kwargs)

    def get_ambient_temperature_degC_arm(self, **kwargs):
        return self.call('get_ambient_temperature_degC_arm', kwargs=kwargs)

    def get_ambient_temperature_degC_gen15(self, **kwargs):
        return self.call('get_ambient_temperature_degC_gen15', kwargs=kwargs)

    def get_tec_enabled(self, **kwargs):
        return self.call('get_tec_enabled', kwargs=kwargs)

    def get_actual_frames(self, **kwargs):
        return self.call('get_actual_frames', kwargs=kwargs)

    def get_actual_integration_time_us(self, **kwargs):
        return self.call('get_actual_integration_time_us', kwargs=kwargs)

    def get_detector_offset(self, **kwargs):
        return self.call('get_detector_offset', kwargs=kwargs)

    def get_detector_offset_odd(self, **kwargs):
        return self.call('get_detector_offset_odd', kwargs=kwargs)

    def get_ccd_sensing_threshold(self, **kwargs):
        return self.call('get_ccd_sensing_threshold', kwargs=kwargs)

    def get_ccd_threshold_sensing_mode(self, **kwargs):
        return self.call('get_ccd_threshold_sensing_mode', kwargs=kwargs)

    def get_external_trigger_output(self, **kwargs):
        return self.call('get_external_trigger_output', kwargs=kwargs)

    def set_mod_linked_to_integration(self, **kwargs):
        return self.call('set_mod_linked_to_integration', kwargs=kwargs)

    def get_mod_linked_to_integration(self, **kwargs):
        return self.call('get_mod_linked_to_integration', kwargs=kwargs)

    def get_selected_adc(self, **kwargs):
        return self.call('get_selected_adc', kwargs=kwargs)

    def set_trigger_delay(self, **kwargs):
        return self.call('set_trigger_delay', kwargs=kwargs)

    def get_trigger_delay(self, **kwargs):
        return self.call('get_trigger_delay', kwargs=kwargs)

    def get_vr_continuous_ccd(self, **kwargs):
        return self.call('get_vr_continuous_ccd', kwargs=kwargs)

    def get_vr_num_frames(self, **kwargs):
        return self.call('get_vr_num_frames', kwargs=kwargs)

    def get_opt_actual_integration_time(self, **kwargs):
        return self.call('get_opt_actual_integration_time', kwargs=kwargs)

    def get_opt_area_scan(self, **kwargs):
        return self.call('get_opt_area_scan', kwargs=kwargs)

    def get_opt_cf_select(self, **kwargs):
        return self.call('get_opt_cf_select', kwargs=kwargs)

    def get_opt_data_header_tab(self, **kwargs):
        return self.call('get_opt_data_header_tab', kwargs=kwargs)

    def get_opt_horizontal_binning(self, **kwargs):
        return self.call('get_opt_horizontal_binning', kwargs=kwargs)

    def get_opt_integration_time_resolution(self, **kwargs):
        return self.call('get_opt_integration_time_resolution', kwargs=kwargs)

    def update_firmware_log(self, **kwargs):
        return self.call('update_firmware_log', kwargs=kwargs)

    def set_analog_output_mode(self, **kwargs):
        return self.call('set_analog_output_mode', kwargs=kwargs)

    def set_analog_output_value(self, **kwargs):
        return self.call('set_analog_output_value', kwargs=kwargs)

    def get_analog_output_state(self, **kwargs):
        return self.call('get_analog_output_state', kwargs=kwargs)

    def get_analog_input_value(self, **kwargs):
        return self.call('get_analog_input_value', kwargs=kwargs)

    def update_session_eeprom(self, **kwargs):
        return self.call('update_session_eeprom', kwargs=kwargs)

    def replace_session_eeprom(self, **kwargs):
        return self.call('replace_session_eeprom', kwargs=kwargs)

    def write_eeprom(self, **kwargs):
        return self.call('write_eeprom', kwargs=kwargs)

    def set_log_level(self, **kwargs):
        return self.call('set_log_level', kwargs=kwargs)

    def queue_message(self, **kwargs):
        return self.call('queue_message', kwargs=kwargs)

    def check_alert(self, **kwargs):
        return self.call('check_alert', kwargs=kwargs)

    def refresh_alerts(self, **kwargs):
        return self.call('refresh_alerts', kwargs=kwargs)

