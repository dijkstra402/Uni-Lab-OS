from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilentXpeel(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/peeling/xpeel_backend.py', 'class_name': 'XPeelBackend', 'import_roots': [], 'candidate_methods': ['advance_tape', 'describe_error', 'enable_plate_check', 'get_seal_sensor_status', 'get_status', 'get_tape_remaining', 'get_version', 'move_conveyor_in', 'move_conveyor_out', 'move_elevator_down', 'move_elevator_up', 'parse_ready_line', 'peel', 'reset', 'restart', 'seal_check', 'set_seal_threshold_lower', 'set_seal_threshold_upper', 'setup', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Agilent', 'model': 'XPeel', 'device_type_cn': '撕膜仪', 'device_type_en': 'Plate Desealer', 'source_framework': 'PyLabRobot', 'tag_id': '4396', 'tag_name': '撕膜仪', 'tag_name_en': 'Plate Desealer', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/peeling/xpeel_backend.py', 'class_name': 'XPeelBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def advance_tape(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('advance_tape', kwargs={k: v for k, v in _kw.items() if v is not None})

    def describe_error(self, code=None, **kwargs):
        _kw = {'code': code}
        _kw.update(kwargs)
        return self.call('describe_error', kwargs={k: v for k, v in _kw.items() if v is not None})

    def enable_plate_check(self, enabled=None, **kwargs):
        _kw = {'enabled': enabled}
        _kw.update(kwargs)
        return self.call('enable_plate_check', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_seal_sensor_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_seal_sensor_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_tape_remaining(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_tape_remaining', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_version(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_version', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_conveyor_in(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('move_conveyor_in', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_conveyor_out(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('move_conveyor_out', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_elevator_down(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('move_elevator_down', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_elevator_up(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('move_elevator_up', kwargs={k: v for k, v in _kw.items() if v is not None})

    def parse_ready_line(self, line=None, **kwargs):
        _kw = {'line': line}
        _kw.update(kwargs)
        return self.call('parse_ready_line', kwargs={k: v for k, v in _kw.items() if v is not None})

    def peel(self, begin_location=None, fast=None, adhere_time=None, **kwargs):
        _kw = {'begin_location': begin_location, 'fast': fast, 'adhere_time': adhere_time}
        _kw.update(kwargs)
        return self.call('peel', kwargs={k: v for k, v in _kw.items() if v is not None})

    def reset(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('reset', kwargs={k: v for k, v in _kw.items() if v is not None})

    def restart(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('restart', kwargs={k: v for k, v in _kw.items() if v is not None})

    def seal_check(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('seal_check', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_seal_threshold_lower(self, value=None, **kwargs):
        _kw = {'value': value}
        _kw.update(kwargs)
        return self.call('set_seal_threshold_lower', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_seal_threshold_upper(self, value=None, **kwargs):
        _kw = {'value': value}
        _kw.update(kwargs)
        return self.call('set_seal_threshold_upper', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

