from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTecanInfinite200Pro2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/plate_reading/tecan/infinite_backend.py', 'class_name': 'ExperimentalTecanInfinite200ProBackend', 'import_roots': [], 'candidate_methods': ['close', 'open', 'read_absorbance', 'read_fluorescence', 'read_luminescence', 'setup', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Tecan', 'model': 'Infinite 200 PRO', 'device_type_cn': '微生物培养箱/读板器', 'device_type_en': 'Incubator/Reader', 'source_framework': 'PyLabRobot', 'tag_id': '4387', 'tag_name': '微生物培养箱', 'tag_name_en': 'Microbial Incubator', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/plate_reading/tecan/infinite_backend.py', 'class_name': 'ExperimentalTecanInfinite200ProBackend'}}

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

    def read_absorbance(self, plate=None, wells=None, wavelength=None, flashes=None, bandwidth=None, **kwargs):
        _kw = {'plate': plate, 'wells': wells, 'wavelength': wavelength, 'flashes': flashes, 'bandwidth': bandwidth}
        _kw.update(kwargs)
        return self.call('read_absorbance', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_fluorescence(self, plate=None, wells=None, excitation_wavelength=None, emission_wavelength=None, focal_height=None, flashes=None, integration_us=None, gain=None, excitation_bandwidth=None, emission_bandwidth=None, lag_us=None, **kwargs):
        _kw = {'plate': plate, 'wells': wells, 'excitation_wavelength': excitation_wavelength, 'emission_wavelength': emission_wavelength, 'focal_height': focal_height, 'flashes': flashes, 'integration_us': integration_us, 'gain': gain, 'excitation_bandwidth': excitation_bandwidth, 'emission_bandwidth': emission_bandwidth, 'lag_us': lag_us}
        _kw.update(kwargs)
        return self.call('read_fluorescence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_luminescence(self, plate=None, wells=None, focal_height=None, flashes=None, dark_integration_us=None, meas_integration_us=None, **kwargs):
        _kw = {'plate': plate, 'wells': wells, 'focal_height': focal_height, 'flashes': flashes, 'dark_integration_us': dark_integration_us, 'meas_integration_us': meas_integration_us}
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

