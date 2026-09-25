from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentByonoyLuminescence96Automate(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/plate_reading/byonoy/byonoy_backend.py', 'class_name': 'ByonoyLuminescence96AutomateBackend', 'import_roots': [], 'candidate_methods': ['close', 'open', 'read_absorbance', 'read_fluorescence', 'read_luminescence', 'setup', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Byonoy', 'model': 'Luminescence 96 Automate', 'device_type_cn': '酶标仪', 'device_type_en': 'Plate Reader', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/plate_reading/byonoy/byonoy_backend.py', 'class_name': 'ByonoyLuminescence96AutomateBackend', 'candidate_methods': ['close', 'open', 'read_absorbance', 'read_fluorescence', 'read_luminescence', 'setup', 'stop']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, plate=None, **kwargs):
        _kw = {'plate': plate}
        _kw.update(kwargs)
        return self.call('close', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_absorbance(self, plate=None, wells=None, wavelength=None, **kwargs):
        _kw = {'plate': plate, 'wells': wells, 'wavelength': wavelength}
        _kw.update(kwargs)
        return self.call('read_absorbance', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_fluorescence(self, plate=None, wells=None, excitation_wavelength=None, emission_wavelength=None, focal_height=None, **kwargs):
        _kw = {'plate': plate, 'wells': wells, 'excitation_wavelength': excitation_wavelength, 'emission_wavelength': emission_wavelength, 'focal_height': focal_height}
        _kw.update(kwargs)
        return self.call('read_fluorescence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_luminescence(self, plate=None, wells=None, focal_height=None, integration_time=None, **kwargs):
        _kw = {'plate': plate, 'wells': wells, 'focal_height': focal_height, 'integration_time': integration_time}
        _kw.update(kwargs)
        return self.call('read_luminescence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

