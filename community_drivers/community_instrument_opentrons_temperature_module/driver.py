from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOpentronsTemperatureModule(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/temperature_controlling/opentrons_backend.py', 'class_name': 'OpentronsTemperatureModuleBackend', 'import_roots': [], 'candidate_methods': ['deactivate', 'get_current_temperature', 'set_temperature', 'setup', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Opentrons', 'model': 'Temperature Module', 'device_type_cn': '温度控制器', 'device_type_en': 'Temperature Controller', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/temperature_controlling/opentrons_backend.py', 'class_name': 'OpentronsTemperatureModuleBackend', 'candidate_methods': ['deactivate', 'get_current_temperature', 'set_temperature', 'setup', 'stop']}}

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

    def set_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

