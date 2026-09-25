from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAzentaA4s(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/sealing/a4s_backend.py', 'class_name': 'A4SBackend', 'import_roots': [], 'candidate_methods': ['close', 'get_remaining_time', 'get_status', 'get_temperature', 'open', 'seal', 'set_heater', 'set_temperature', 'set_time', 'setup', 'stop', 'system_reset'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Azenta', 'model': 'a4S', 'device_type_cn': '封膜机', 'device_type_en': 'Plate Sealer', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/sealing/a4s_backend.py', 'class_name': 'A4SBackend', 'candidate_methods': ['close', 'get_remaining_time', 'get_status', 'get_temperature', 'open', 'seal', 'set_heater', 'set_temperature', 'set_time', 'setup', 'stop', 'system_reset']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('close', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_remaining_time(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_remaining_time', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open', kwargs={k: v for k, v in _kw.items() if v is not None})

    def seal(self, temperature=None, duration=None, **kwargs):
        _kw = {'temperature': temperature, 'duration': duration}
        _kw.update(kwargs)
        return self.call('seal', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_heater(self, on=None, **kwargs):
        _kw = {'on': on}
        _kw.update(kwargs)
        return self.call('set_heater', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_time(self, seconds=None, **kwargs):
        _kw = {'seconds': seconds}
        _kw.update(kwargs)
        return self.call('set_time', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def system_reset(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('system_reset', kwargs={k: v for k, v in _kw.items() if v is not None})

