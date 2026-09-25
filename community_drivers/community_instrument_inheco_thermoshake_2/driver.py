from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentInhecoThermoshake2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/heating_shaking/inheco/thermoshake_backend.py', 'class_name': 'InhecoThermoshakeBackend', 'import_roots': [], 'candidate_methods': ['deactivate', 'get_current_temperature', 'get_device_info', 'lock_plate', 'set_shaker_shape', 'set_shaker_speed', 'set_target_temperature', 'set_temperature', 'setup', 'shake', 'start_shaking', 'start_temperature_control', 'stop', 'stop_shaking', 'stop_temperature_control', 'unlock_plate'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Inheco', 'model': 'ThermoShake', 'device_type_cn': '热混匀仪', 'device_type_en': 'Thermomixer', 'source_framework': 'PyLabRobot', 'tag_id': '4421', 'tag_name': '热混匀仪', 'tag_name_en': 'Thermomixer', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/heating_shaking/inheco/thermoshake_backend.py', 'class_name': 'InhecoThermoshakeBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def deactivate(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('deactivate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_current_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_current_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_device_info(self, info_type=None, **kwargs):
        _kw = {'info_type': info_type}
        _kw.update(kwargs)
        return self.call('get_device_info', kwargs={k: v for k, v in _kw.items() if v is not None})

    def lock_plate(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('lock_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_shaker_shape(self, shape=None, **kwargs):
        _kw = {'shape': shape}
        _kw.update(kwargs)
        return self.call('set_shaker_shape', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_shaker_speed(self, speed=None, **kwargs):
        _kw = {'speed': speed}
        _kw.update(kwargs)
        return self.call('set_shaker_speed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_target_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_target_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def shake(self, speed=None, shape=None, **kwargs):
        _kw = {'speed': speed, 'shape': shape}
        _kw.update(kwargs)
        return self.call('shake', kwargs={k: v for k, v in _kw.items() if v is not None})

    def start_shaking(self, speed=None, shape=None, **kwargs):
        _kw = {'speed': speed, 'shape': shape}
        _kw.update(kwargs)
        return self.call('start_shaking', kwargs={k: v for k, v in _kw.items() if v is not None})

    def start_temperature_control(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('start_temperature_control', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_shaking(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop_shaking', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_temperature_control(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop_temperature_control', kwargs={k: v for k, v in _kw.items() if v is not None})

    def unlock_plate(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('unlock_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

