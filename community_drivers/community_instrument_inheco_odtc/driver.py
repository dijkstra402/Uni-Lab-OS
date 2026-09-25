from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentInhecoOdtc(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/thermocycling/inheco/odtc_backend.py', 'class_name': 'ExperimentalODTCBackend', 'import_roots': [], 'candidate_methods': ['close_lid', 'deactivate_block', 'deactivate_lid', 'get_block_current_temperature', 'get_block_status', 'get_block_target_temperature', 'get_current_cycle_index', 'get_current_step_index', 'get_hold_time', 'get_lid_current_temperature', 'get_lid_open', 'get_lid_status', 'get_lid_target_temperature', 'get_sensor_data', 'get_total_cycle_count', 'get_total_step_count', 'open_lid', 'run_protocol', 'set_block_temperature', 'set_lid_temperature', 'setup', 'stop', 'stop_method'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Inheco', 'model': 'ODTC', 'device_type_cn': '恒温摇床', 'device_type_en': 'Thermoshaker', 'source_framework': 'PyLabRobot', 'tag_id': '4389', 'tag_name': '恒温摇床', 'tag_name_en': 'Constant Temperature Shaker', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/thermocycling/inheco/odtc_backend.py', 'class_name': 'ExperimentalODTCBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close_lid(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('close_lid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def deactivate_block(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('deactivate_block', kwargs={k: v for k, v in _kw.items() if v is not None})

    def deactivate_lid(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('deactivate_lid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_block_current_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_block_current_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_block_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_block_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_block_target_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_block_target_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_current_cycle_index(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_current_cycle_index', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_current_step_index(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_current_step_index', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_hold_time(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_hold_time', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_current_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_lid_current_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_open(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_lid_open', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_lid_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_target_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_lid_target_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_sensor_data(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_sensor_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_total_cycle_count(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_total_cycle_count', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_total_step_count(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_total_step_count', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open_lid(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open_lid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def run_protocol(self, protocol=None, block_max_volume=None, start_block_temperature=None, start_lid_temperature=None, post_heating=None, method_name=None, **kwargs):
        _kw = {'protocol': protocol, 'block_max_volume': block_max_volume, 'start_block_temperature': start_block_temperature, 'start_lid_temperature': start_lid_temperature, 'post_heating': post_heating, 'method_name': method_name}
        _kw.update(kwargs)
        return self.call('run_protocol', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_block_temperature(self, temperature=None, dynamic_time=None, **kwargs):
        _kw = {'temperature': temperature, 'dynamic_time': dynamic_time}
        _kw.update(kwargs)
        return self.call('set_block_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_lid_temperature(self, temperature=None, dynamic_time=None, **kwargs):
        _kw = {'temperature': temperature, 'dynamic_time': dynamic_time}
        _kw.update(kwargs)
        return self.call('set_lid_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_method(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop_method', kwargs={k: v for k, v in _kw.items() if v is not None})

