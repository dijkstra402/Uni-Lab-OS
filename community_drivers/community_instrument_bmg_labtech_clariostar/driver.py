from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBmgLabtechClariostar(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/plate_reading/bmg_labtech/clario_star_backend.py', 'class_name': 'CLARIOstarBackend', 'import_roots': [], 'candidate_methods': ['close', 'get_stat', 'initialize', 'open', 'read_absorbance', 'read_command_status', 'read_fluorescence', 'read_luminescence', 'read_resp', 'request_eeprom_data', 'send', 'setup', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'BMG LABTECH', 'model': 'CLARIOstar', 'device_type_cn': '酶标仪', 'device_type_en': 'Microplate Reader', 'source_framework': 'PyLabRobot', 'tag_id': '4457', 'tag_name': '酶标仪', 'tag_name_en': 'Microplate Reader', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/plate_reading/bmg_labtech/clario_star_backend.py', 'class_name': 'CLARIOstarBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, plate=None, **kwargs):
        _kw = {'plate': plate}
        _kw.update(kwargs)
        return self.call('close', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_stat(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_stat', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_absorbance(self, plate=None, wells=None, wavelength=None, report=None, **kwargs):
        _kw = {'plate': plate, 'wells': wells, 'wavelength': wavelength, 'report': report}
        _kw.update(kwargs)
        return self.call('read_absorbance', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_command_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('read_command_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_fluorescence(self, plate=None, wells=None, excitation_wavelength=None, emission_wavelength=None, focal_height=None, **kwargs):
        _kw = {'plate': plate, 'wells': wells, 'excitation_wavelength': excitation_wavelength, 'emission_wavelength': emission_wavelength, 'focal_height': focal_height}
        _kw.update(kwargs)
        return self.call('read_fluorescence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_luminescence(self, plate=None, wells=None, focal_height=None, **kwargs):
        _kw = {'plate': plate, 'wells': wells, 'focal_height': focal_height}
        _kw.update(kwargs)
        return self.call('read_luminescence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_resp(self, timeout=None, **kwargs):
        _kw = {'timeout': timeout}
        _kw.update(kwargs)
        return self.call('read_resp', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_eeprom_data(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_eeprom_data', kwargs={k: v for k, v in _kw.items() if v is not None})

    def send(self, cmd=None, read_timeout=None, **kwargs):
        _kw = {'cmd': cmd, 'read_timeout': read_timeout}
        _kw.update(kwargs)
        return self.call('send', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

