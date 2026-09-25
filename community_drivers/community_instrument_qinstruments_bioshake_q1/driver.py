from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentQinstrumentsBioshakeQ1(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/heating_shaking/bioshake_backend.py', 'class_name': 'BioShake', 'import_roots': [], 'candidate_methods': ['deactivate', 'get_current_temperature', 'home', 'lock_plate', 'reset', 'set_temperature', 'setup', 'shake', 'start_shaking', 'stop', 'stop_shaking', 'unlock_plate'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'QInstruments', 'model': 'BioShake Q1', 'device_type_cn': '加热振荡器', 'device_type_en': 'Heater Shaker', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/heating_shaking/bioshake_backend.py', 'class_name': 'BioShake', 'candidate_methods': ['deactivate', 'get_current_temperature', 'home', 'lock_plate', 'reset', 'set_temperature', 'setup', 'shake', 'start_shaking', 'stop', 'stop_shaking', 'unlock_plate']}}

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

    def home(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('home', kwargs={k: v for k, v in _kw.items() if v is not None})

    def lock_plate(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('lock_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def reset(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('reset', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, skip_home=None, **kwargs):
        _kw = {'skip_home': skip_home}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def shake(self, speed=None, acceleration=None, **kwargs):
        _kw = {'speed': speed, 'acceleration': acceleration}
        _kw.update(kwargs)
        return self.call('shake', kwargs={k: v for k, v in _kw.items() if v is not None})

    def start_shaking(self, speed=None, acceleration=None, **kwargs):
        _kw = {'speed': speed, 'acceleration': acceleration}
        _kw.update(kwargs)
        return self.call('start_shaking', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_shaking(self, deceleration=None, **kwargs):
        _kw = {'deceleration': deceleration}
        _kw.update(kwargs)
        return self.call('stop_shaking', kwargs={k: v for k, v in _kw.items() if v is not None})

    def unlock_plate(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('unlock_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

