from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilentVspin2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/centrifuge/vspin_backend.py', 'class_name': 'VSpinBackend', 'import_roots': [], 'candidate_methods': ['close_door', 'configure_and_initialize', 'g_to_rpm', 'get_bucket_1_position', 'get_bucket_locked', 'get_door_locked', 'get_door_open', 'get_home_position', 'get_position', 'get_tachometer', 'go_to_bucket1', 'go_to_bucket2', 'go_to_position', 'initialize', 'lock_bucket', 'lock_door', 'open_door', 'set_bucket_1_position_to_current', 'set_configuration_data', 'setup', 'spin', 'stop', 'unlock_bucket', 'unlock_door'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Agilent', 'model': 'VSpin', 'device_type_cn': '低温/冷冻离心机', 'device_type_en': 'Refrigerated Centrifuge', 'source_framework': 'PyLabRobot', 'tag_id': '4366', 'tag_name': '低温/冷冻离心机', 'tag_name_en': 'Refrigerated Centrifuge', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/centrifuge/vspin_backend.py', 'class_name': 'VSpinBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('close_door', kwargs={k: v for k, v in _kw.items() if v is not None})

    def configure_and_initialize(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('configure_and_initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def g_to_rpm(self, g=None, **kwargs):
        _kw = {'g': g}
        _kw.update(kwargs)
        return self.call('g_to_rpm', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_bucket_1_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_bucket_1_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_bucket_locked(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_bucket_locked', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_door_locked(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_door_locked', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_door_open(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_door_open', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_home_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_home_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_position(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_tachometer(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_tachometer', kwargs={k: v for k, v in _kw.items() if v is not None})

    def go_to_bucket1(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('go_to_bucket1', kwargs={k: v for k, v in _kw.items() if v is not None})

    def go_to_bucket2(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('go_to_bucket2', kwargs={k: v for k, v in _kw.items() if v is not None})

    def go_to_position(self, position=None, **kwargs):
        _kw = {'position': position}
        _kw.update(kwargs)
        return self.call('go_to_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def lock_bucket(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('lock_bucket', kwargs={k: v for k, v in _kw.items() if v is not None})

    def lock_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('lock_door', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open_door', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_bucket_1_position_to_current(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('set_bucket_1_position_to_current', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_configuration_data(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('set_configuration_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def spin(self, g=None, duration=None, acceleration=None, deceleration=None, **kwargs):
        _kw = {'g': g, 'duration': duration, 'acceleration': acceleration, 'deceleration': deceleration}
        _kw.update(kwargs)
        return self.call('spin', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def unlock_bucket(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('unlock_bucket', kwargs={k: v for k, v in _kw.items() if v is not None})

    def unlock_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('unlock_door', kwargs={k: v for k, v in _kw.items() if v is not None})

