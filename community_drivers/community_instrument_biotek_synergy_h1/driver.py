from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBiotekSynergyH1(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/plate_reading/agilent/biotek_synergyh1_backend.py', 'class_name': 'SynergyH1Backend', 'import_roots': [], 'candidate_methods': ['close', 'get_current_temperature', 'get_firmware_version', 'get_serial_number', 'home', 'open', 'read_absorbance', 'read_fluorescence', 'read_luminescence', 'set_plate', 'set_temperature', 'setup', 'shake', 'stop', 'stop_heating_or_cooling', 'stop_shaking'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Agilent (BioTek)', 'model': 'Synergy H1', 'device_type_cn': '酶标仪', 'device_type_en': 'Plate Reader', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/plate_reading/agilent/biotek_synergyh1_backend.py', 'class_name': 'SynergyH1Backend', 'candidate_methods': ['close', 'get_current_temperature', 'get_firmware_version', 'get_serial_number', 'home', 'open', 'read_absorbance', 'read_fluorescence', 'read_luminescence', 'set_plate', 'set_temperature', 'setup', 'shake', 'stop', 'stop_heating_or_cooling', 'stop_shaking']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, plate=None, slow=None, **kwargs):
        _kw = {'plate': plate, 'slow': slow}
        _kw.update(kwargs)
        return self.call('close', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_current_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_current_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_firmware_version(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_firmware_version', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_serial_number(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_serial_number', kwargs={k: v for k, v in _kw.items() if v is not None})

    def home(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('home', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open(self, slow=None, **kwargs):
        _kw = {'slow': slow}
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

    def set_plate(self, plate=None, **kwargs):
        _kw = {'plate': plate}
        _kw.update(kwargs)
        return self.call('set_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def shake(self, shake_type=None, frequency=None, **kwargs):
        _kw = {'shake_type': shake_type, 'frequency': frequency}
        _kw.update(kwargs)
        return self.call('shake', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_heating_or_cooling(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop_heating_or_cooling', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_shaking(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop_shaking', kwargs={k: v for k, v in _kw.items() if v is not None})

