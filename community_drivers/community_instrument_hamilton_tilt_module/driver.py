from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHamiltonTiltModule(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/tilting/hamilton_backend.py', 'class_name': 'HamiltonTiltModuleBackend', 'import_roots': [], 'candidate_methods': ['set_angle', 'setup', 'stop', 'tilt_go_to_position', 'tilt_initial_offset', 'tilt_initialize', 'tilt_move_to_absolute_step_position', 'tilt_move_to_relative_step_position', 'tilt_port_clear_open_collector', 'tilt_port_set_open_collector', 'tilt_power_off', 'tilt_request_error', 'tilt_request_offset_between_light_barrier_and_init_position', 'tilt_request_sensor', 'tilt_set_drain_time', 'tilt_set_name', 'tilt_set_speed', 'tilt_set_temperature', 'tilt_set_waste_pump_off', 'tilt_set_waste_pump_on', 'tilt_switch_encoder', 'tilt_switch_off_temperature_controller'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Hamilton', 'model': 'Tilt Module', 'device_type_cn': '倾斜模块', 'device_type_en': 'Tilt Module', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/tilting/hamilton_backend.py', 'class_name': 'HamiltonTiltModuleBackend', 'candidate_methods': ['set_angle', 'setup', 'stop', 'tilt_go_to_position', 'tilt_initial_offset', 'tilt_initialize', 'tilt_move_to_absolute_step_position', 'tilt_move_to_relative_step_position', 'tilt_port_clear_open_collector', 'tilt_port_set_open_collector', 'tilt_power_off', 'tilt_request_error', 'tilt_request_offset_between_light_barrier_and_init_position', 'tilt_request_sensor', 'tilt_set_drain_time', 'tilt_set_name', 'tilt_set_speed', 'tilt_set_temperature', 'tilt_set_waste_pump_off', 'tilt_set_waste_pump_on', 'tilt_switch_encoder', 'tilt_switch_off_temperature_controller']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def set_angle(self, angle=None, **kwargs):
        _kw = {'angle': angle}
        _kw.update(kwargs)
        return self.call('set_angle', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, initial_offset=None, **kwargs):
        _kw = {'initial_offset': initial_offset}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_go_to_position(self, position=None, **kwargs):
        _kw = {'position': position}
        _kw.update(kwargs)
        return self.call('tilt_go_to_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_initial_offset(self, offset=None, **kwargs):
        _kw = {'offset': offset}
        _kw.update(kwargs)
        return self.call('tilt_initial_offset', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_initialize(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('tilt_initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_move_to_absolute_step_position(self, position=None, **kwargs):
        _kw = {'position': position}
        _kw.update(kwargs)
        return self.call('tilt_move_to_absolute_step_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_move_to_relative_step_position(self, steps=None, **kwargs):
        _kw = {'steps': steps}
        _kw.update(kwargs)
        return self.call('tilt_move_to_relative_step_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_port_clear_open_collector(self, open_collector=None, **kwargs):
        _kw = {'open_collector': open_collector}
        _kw.update(kwargs)
        return self.call('tilt_port_clear_open_collector', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_port_set_open_collector(self, open_collector=None, **kwargs):
        _kw = {'open_collector': open_collector}
        _kw.update(kwargs)
        return self.call('tilt_port_set_open_collector', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_power_off(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('tilt_power_off', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_request_error(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('tilt_request_error', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_request_offset_between_light_barrier_and_init_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('tilt_request_offset_between_light_barrier_and_init_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_request_sensor(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('tilt_request_sensor', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_set_drain_time(self, drain_time=None, **kwargs):
        _kw = {'drain_time': drain_time}
        _kw.update(kwargs)
        return self.call('tilt_set_drain_time', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_set_name(self, name=None, **kwargs):
        _kw = {'name': name}
        _kw.update(kwargs)
        return self.call('tilt_set_name', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_set_speed(self, speed=None, **kwargs):
        _kw = {'speed': speed}
        _kw.update(kwargs)
        return self.call('tilt_set_speed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_set_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('tilt_set_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_set_waste_pump_off(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('tilt_set_waste_pump_off', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_set_waste_pump_on(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('tilt_set_waste_pump_on', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_switch_encoder(self, on=None, **kwargs):
        _kw = {'on': on}
        _kw.update(kwargs)
        return self.call('tilt_switch_encoder', kwargs={k: v for k, v in _kw.items() if v is not None})

    def tilt_switch_off_temperature_controller(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('tilt_switch_off_temperature_controller', kwargs={k: v for k, v in _kw.items() if v is not None})

