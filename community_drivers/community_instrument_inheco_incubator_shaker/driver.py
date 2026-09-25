from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentInhecoIncubatorShaker(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/storage/inheco/incubator_shaker_backend.py', 'class_name': 'InhecoIncubatorShakerStackBackend', 'import_roots': [], 'candidate_methods': ['close', 'delete_counter', 'get_temperature', 'initialize', 'is_shaking_enabled', 'is_temperature_control_enabled', 'open', 'perform_self_test', 'read_whole_shaker_calibration_data', 'request_calibration_high', 'request_calibration_low', 'request_delta_temperature', 'request_drawer_cycles_performed', 'request_drawer_status', 'request_firmware_version', 'request_incubator_type', 'request_is_initialized', 'request_labware_detection_threshold', 'request_last_calibration_date', 'request_machine_allocation', 'request_maximum_allowed_temperature', 'request_motor_current_limit_anticlockwise', 'request_motor_current_limit_clockwise', 'request_motor_power_anticlockwise', 'request_motor_power_clockwise', 'request_number_of_connected_machines', 'request_operation_time_in_hours', 'request_pid_controller_coefficients', 'request_plate_in_incubator', 'request_plate_status_known', 'request_proportionality_factor', 'request_serial_number', 'request_shaker_amplitude_x', 'request_shaker_amplitude_y', 'request_shaker_calibration_value', 'request_shaker_frequency_x', 'request_shaker_frequency_y', 'request_shaker_phase_shift', 'request_target_temperature', 'request_thermal_calibration_date', 'request_whole_calibration_data', 'reset_calibration_data', 'set_boost_offset', 'set_boost_time', 'set_calibration_high', 'set_calibration_low', 'set_cooldown_time_factor', 'set_heatup_offset', 'set_heatup_time_factor', 'set_max_allowed_device_temperature', 'set_motor_current_limit_anticlockwise', 'set_motor_current_limit_clockwise', 'set_motor_power_anticlockwise', 'set_motor_power_clockwise', 'set_pid_integration_value', 'set_pid_proportional_gain', 'set_proportionality_factor', 'set_shaker_calibration_value', 'set_shaker_parameters', 'set_shaker_pattern', 'set_shaker_status', 'setup', 'shake', 'start_temperature_control', 'stop', 'stop_shaking', 'stop_temperature_control', 'wait_for_temperature'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Inheco', 'model': 'Incubator Shaker', 'device_type_cn': '组织培养试验箱', 'device_type_en': 'Tissue Culture Chamber', 'source_framework': 'PyLabRobot', 'tag_id': '4442', 'tag_name': '组织培养试验箱', 'tag_name_en': 'Tissue Culture Chamber', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/storage/inheco/incubator_shaker_backend.py', 'class_name': 'InhecoIncubatorShakerStackBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('close', kwargs={k: v for k, v in _kw.items() if v is not None})

    def delete_counter(self, key=None, selector=None, **kwargs):
        _kw = {'key': key, 'selector': selector}
        _kw.update(kwargs)
        return self.call('delete_counter', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_temperature(self, stack_index=None, sensor=None, read_timeout=None, **kwargs):
        _kw = {'stack_index': stack_index, 'sensor': sensor, 'read_timeout': read_timeout}
        _kw.update(kwargs)
        return self.call('get_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def is_shaking_enabled(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('is_shaking_enabled', kwargs={k: v for k, v in _kw.items() if v is not None})

    def is_temperature_control_enabled(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('is_temperature_control_enabled', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('open', kwargs={k: v for k, v in _kw.items() if v is not None})

    def perform_self_test(self, stack_index=None, read_timeout=None, **kwargs):
        _kw = {'stack_index': stack_index, 'read_timeout': read_timeout}
        _kw.update(kwargs)
        return self.call('perform_self_test', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_whole_shaker_calibration_data(self, key=None, **kwargs):
        _kw = {'key': key}
        _kw.update(kwargs)
        return self.call('read_whole_shaker_calibration_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_calibration_high(self, sensor=None, format=None, **kwargs):
        _kw = {'sensor': sensor, 'format': format}
        _kw.update(kwargs)
        return self.call('request_calibration_high', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_calibration_low(self, sensor=None, format=None, **kwargs):
        _kw = {'sensor': sensor, 'format': format}
        _kw.update(kwargs)
        return self.call('request_calibration_low', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_delta_temperature(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_delta_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_drawer_cycles_performed(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_drawer_cycles_performed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_drawer_status(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_drawer_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_firmware_version(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_firmware_version', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_incubator_type(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_incubator_type', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_is_initialized(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_is_initialized', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_labware_detection_threshold(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_labware_detection_threshold', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_last_calibration_date(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_last_calibration_date', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_machine_allocation(self, layer=None, stack_index=None, **kwargs):
        _kw = {'layer': layer, 'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_machine_allocation', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_maximum_allowed_temperature(self, stack_index=None, measured=None, **kwargs):
        _kw = {'stack_index': stack_index, 'measured': measured}
        _kw.update(kwargs)
        return self.call('request_maximum_allowed_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_motor_current_limit_anticlockwise(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_motor_current_limit_anticlockwise', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_motor_current_limit_clockwise(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_motor_current_limit_clockwise', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_motor_power_anticlockwise(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_motor_power_anticlockwise', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_motor_power_clockwise(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_motor_power_clockwise', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_number_of_connected_machines(self, layer=None, stack_index=None, **kwargs):
        _kw = {'layer': layer, 'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_number_of_connected_machines', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_operation_time_in_hours(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_operation_time_in_hours', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_pid_controller_coefficients(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_pid_controller_coefficients', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_plate_in_incubator(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_plate_in_incubator', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_plate_status_known(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_plate_status_known', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_proportionality_factor(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_proportionality_factor', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_serial_number(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_serial_number', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_shaker_amplitude_x(self, stack_index=None, selector=None, **kwargs):
        _kw = {'stack_index': stack_index, 'selector': selector}
        _kw.update(kwargs)
        return self.call('request_shaker_amplitude_x', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_shaker_amplitude_y(self, stack_index=None, selector=None, **kwargs):
        _kw = {'stack_index': stack_index, 'selector': selector}
        _kw.update(kwargs)
        return self.call('request_shaker_amplitude_y', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_shaker_calibration_value(self, position=None, selector=None, **kwargs):
        _kw = {'position': position, 'selector': selector}
        _kw.update(kwargs)
        return self.call('request_shaker_calibration_value', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_shaker_frequency_x(self, stack_index=None, selector=None, **kwargs):
        _kw = {'stack_index': stack_index, 'selector': selector}
        _kw.update(kwargs)
        return self.call('request_shaker_frequency_x', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_shaker_frequency_y(self, stack_index=None, selector=None, **kwargs):
        _kw = {'stack_index': stack_index, 'selector': selector}
        _kw.update(kwargs)
        return self.call('request_shaker_frequency_y', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_shaker_phase_shift(self, stack_index=None, selector=None, **kwargs):
        _kw = {'stack_index': stack_index, 'selector': selector}
        _kw.update(kwargs)
        return self.call('request_shaker_phase_shift', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_target_temperature(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_target_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_thermal_calibration_date(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('request_thermal_calibration_date', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_whole_calibration_data(self, key=None, **kwargs):
        _kw = {'key': key}
        _kw.update(kwargs)
        return self.call('request_whole_calibration_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def reset_calibration_data(self, key=None, **kwargs):
        _kw = {'key': key}
        _kw.update(kwargs)
        return self.call('reset_calibration_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_boost_offset(self, offset=None, **kwargs):
        _kw = {'offset': offset}
        _kw.update(kwargs)
        return self.call('set_boost_offset', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_boost_time(self, time_s=None, **kwargs):
        _kw = {'time_s': time_s}
        _kw.update(kwargs)
        return self.call('set_boost_time', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_calibration_high(self, key=None, sensor1=None, sensor2=None, sensor3=None, date=None, **kwargs):
        _kw = {'key': key, 'sensor1': sensor1, 'sensor2': sensor2, 'sensor3': sensor3, 'date': date}
        _kw.update(kwargs)
        return self.call('set_calibration_high', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_calibration_low(self, key=None, sensor1=None, sensor2=None, sensor3=None, **kwargs):
        _kw = {'key': key, 'sensor1': sensor1, 'sensor2': sensor2, 'sensor3': sensor3}
        _kw.update(kwargs)
        return self.call('set_calibration_low', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_cooldown_time_factor(self, value=None, **kwargs):
        _kw = {'value': value}
        _kw.update(kwargs)
        return self.call('set_cooldown_time_factor', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_heatup_offset(self, offset=None, **kwargs):
        _kw = {'offset': offset}
        _kw.update(kwargs)
        return self.call('set_heatup_offset', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_heatup_time_factor(self, value=None, **kwargs):
        _kw = {'value': value}
        _kw.update(kwargs)
        return self.call('set_heatup_time_factor', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_max_allowed_device_temperature(self, key=None, temperature=None, **kwargs):
        _kw = {'key': key, 'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_max_allowed_device_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_motor_current_limit_anticlockwise(self, key=None, current=None, **kwargs):
        _kw = {'key': key, 'current': current}
        _kw.update(kwargs)
        return self.call('set_motor_current_limit_anticlockwise', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_motor_current_limit_clockwise(self, key=None, current=None, **kwargs):
        _kw = {'key': key, 'current': current}
        _kw.update(kwargs)
        return self.call('set_motor_current_limit_clockwise', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_motor_power_anticlockwise(self, key=None, power=None, **kwargs):
        _kw = {'key': key, 'power': power}
        _kw.update(kwargs)
        return self.call('set_motor_power_anticlockwise', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_motor_power_clockwise(self, key=None, power=None, **kwargs):
        _kw = {'key': key, 'power': power}
        _kw.update(kwargs)
        return self.call('set_motor_power_clockwise', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_pid_integration_value(self, key=None, value=None, **kwargs):
        _kw = {'key': key, 'value': value}
        _kw.update(kwargs)
        return self.call('set_pid_integration_value', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_pid_proportional_gain(self, key=None, value=None, **kwargs):
        _kw = {'key': key, 'value': value}
        _kw.update(kwargs)
        return self.call('set_pid_proportional_gain', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_proportionality_factor(self, value=None, **kwargs):
        _kw = {'value': value}
        _kw.update(kwargs)
        return self.call('set_proportionality_factor', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_shaker_calibration_value(self, key=None, position=None, value=None, **kwargs):
        _kw = {'key': key, 'position': position, 'value': value}
        _kw.update(kwargs)
        return self.call('set_shaker_calibration_value', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_shaker_parameters(self, amplitude_x=None, amplitude_y=None, frequency_x=None, frequency_y=None, phase_shift=None, stack_index=None, **kwargs):
        _kw = {'amplitude_x': amplitude_x, 'amplitude_y': amplitude_y, 'frequency_x': frequency_x, 'frequency_y': frequency_y, 'phase_shift': phase_shift, 'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('set_shaker_parameters', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_shaker_pattern(self, pattern=None, stack_index=None, frequency_hz=None, rpm=None, amplitude_x_mm=None, amplitude_y_mm=None, phase_deg=None, **kwargs):
        _kw = {'pattern': pattern, 'stack_index': stack_index, 'frequency_hz': frequency_hz, 'rpm': rpm, 'amplitude_x_mm': amplitude_x_mm, 'amplitude_y_mm': amplitude_y_mm, 'phase_deg': phase_deg}
        _kw.update(kwargs)
        return self.call('set_shaker_pattern', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_shaker_status(self, enabled=None, stack_index=None, **kwargs):
        _kw = {'enabled': enabled, 'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('set_shaker_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, port=None, **kwargs):
        _kw = {'port': port}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def shake(self, stack_index=None, pattern=None, rpm=None, frequency_hz=None, amplitude_x_mm=None, amplitude_y_mm=None, phase_deg=None, **kwargs):
        _kw = {'stack_index': stack_index, 'pattern': pattern, 'rpm': rpm, 'frequency_hz': frequency_hz, 'amplitude_x_mm': amplitude_x_mm, 'amplitude_y_mm': amplitude_y_mm, 'phase_deg': phase_deg}
        _kw.update(kwargs)
        return self.call('shake', kwargs={k: v for k, v in _kw.items() if v is not None})

    def start_temperature_control(self, temperature=None, stack_index=None, **kwargs):
        _kw = {'temperature': temperature, 'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('start_temperature_control', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_shaking(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('stop_shaking', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_temperature_control(self, stack_index=None, **kwargs):
        _kw = {'stack_index': stack_index}
        _kw.update(kwargs)
        return self.call('stop_temperature_control', kwargs={k: v for k, v in _kw.items() if v is not None})

    def wait_for_temperature(self, stack_index=None, sensor=None, tolerance=None, interval_s=None, timeout_s=None, show_progress_bar=None, **kwargs):
        _kw = {'stack_index': stack_index, 'sensor': sensor, 'tolerance': tolerance, 'interval_s': interval_s, 'timeout_s': timeout_s, 'show_progress_bar': show_progress_bar}
        _kw.update(kwargs)
        return self.call('wait_for_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

