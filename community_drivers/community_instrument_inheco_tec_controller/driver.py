from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentInhecoTecController(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/temperature_controlling/inheco/temperature_controller.py', 'class_name': 'InhecoTemperatureControllerBackend', 'import_roots': [], 'candidate_methods': ['deactivate', 'get_current_temperature', 'get_device_info', 'set_target_temperature', 'set_temperature', 'setup', 'start_temperature_control', 'stop', 'stop_temperature_control'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Inheco', 'model': 'TEC Controller', 'device_type_cn': '高低温金属浴', 'device_type_en': 'Temperature Controller', 'source_framework': 'PyLabRobot', 'tag_id': '4459', 'tag_name': '高低温金属浴', 'tag_name_en': 'High/Low Temperature Metal Bath', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/temperature_controlling/inheco/temperature_controller.py', 'class_name': 'InhecoTemperatureControllerBackend'}}

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

    def start_temperature_control(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('start_temperature_control', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_temperature_control(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop_temperature_control', kwargs={k: v for k, v in _kw.items() if v is not None})

