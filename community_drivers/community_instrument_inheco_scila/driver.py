from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentInhecoScila(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/storage/inheco/scila/scila_backend.py', 'class_name': 'SCILABackend', 'import_roots': [], 'candidate_methods': ['close', 'is_temperature_control_enabled', 'maintenance', 'measure_temperature', 'open', 'request_co2_flow_status', 'request_drawer_status', 'request_drawer_statuses', 'request_liquid_level', 'request_status', 'request_target_temperature', 'request_temperature_information', 'request_valve_status', 'setup', 'start_temperature_control', 'stop', 'stop_temperature_control'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Inheco', 'model': 'SCILA', 'device_type_cn': '存储孵育器', 'device_type_en': 'Storage Incubator', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/storage/inheco/scila/scila_backend.py', 'class_name': 'SCILABackend', 'candidate_methods': ['close', 'is_temperature_control_enabled', 'maintenance', 'measure_temperature', 'open', 'request_co2_flow_status', 'request_drawer_status', 'request_drawer_statuses', 'request_liquid_level', 'request_status', 'request_target_temperature', 'request_temperature_information', 'request_valve_status', 'setup', 'start_temperature_control', 'stop', 'stop_temperature_control']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, drawer_id=None, **kwargs):
        _kw = {'drawer_id': drawer_id}
        _kw.update(kwargs)
        return self.call('close', kwargs={k: v for k, v in _kw.items() if v is not None})

    def is_temperature_control_enabled(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('is_temperature_control_enabled', kwargs={k: v for k, v in _kw.items() if v is not None})

    def maintenance(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('maintenance', kwargs={k: v for k, v in _kw.items() if v is not None})

    def measure_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('measure_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open(self, drawer_id=None, **kwargs):
        _kw = {'drawer_id': drawer_id}
        _kw.update(kwargs)
        return self.call('open', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_co2_flow_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_co2_flow_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_drawer_status(self, drawer_id=None, **kwargs):
        _kw = {'drawer_id': drawer_id}
        _kw.update(kwargs)
        return self.call('request_drawer_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_drawer_statuses(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_drawer_statuses', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_liquid_level(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_liquid_level', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_target_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_target_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_temperature_information(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_temperature_information', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_valve_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_valve_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def start_temperature_control(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
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

