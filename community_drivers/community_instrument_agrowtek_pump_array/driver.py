from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgrowtekPumpArray(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/pumps/agrowpumps/agrowdosepump_backend.py', 'class_name': 'AgrowPumpArrayBackend', 'import_roots': [], 'candidate_methods': ['halt', 'run_continuously', 'run_revolutions', 'setup', 'start_keep_alive_thread', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Agrowtek', 'model': 'Pump Array', 'device_type_cn': '泵', 'device_type_en': 'Pump', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/pumps/agrowpumps/agrowdosepump_backend.py', 'class_name': 'AgrowPumpArrayBackend', 'candidate_methods': ['halt', 'run_continuously', 'run_revolutions', 'setup', 'start_keep_alive_thread', 'stop']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def halt(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('halt', kwargs={k: v for k, v in _kw.items() if v is not None})

    def run_continuously(self, speed=None, use_channels=None, **kwargs):
        _kw = {'speed': speed, 'use_channels': use_channels}
        _kw.update(kwargs)
        return self.call('run_continuously', kwargs={k: v for k, v in _kw.items() if v is not None})

    def run_revolutions(self, num_revolutions=None, use_channels=None, **kwargs):
        _kw = {'num_revolutions': num_revolutions, 'use_channels': use_channels}
        _kw.update(kwargs)
        return self.call('run_revolutions', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def start_keep_alive_thread(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('start_keep_alive_thread', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

