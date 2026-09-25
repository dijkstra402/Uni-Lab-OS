from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBiotekCytation1(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/plate_reading/agilent/biotek_cytation_backend.py', 'class_name': 'CytationBackend', 'import_roots': [], 'candidate_methods': ['capture', 'close', 'get_current_temperature', 'get_firmware_version', 'get_serial_number', 'home', 'led_off', 'led_on', 'open', 'read_absorbance', 'read_fluorescence', 'read_luminescence', 'select', 'set_auto_exposure', 'set_exposure', 'set_focus', 'set_gain', 'set_imaging_mode', 'set_objective', 'set_plate', 'set_position', 'set_temperature', 'setup', 'shake', 'start_acquisition', 'stop', 'stop_acquisition', 'stop_heating_or_cooling', 'stop_shaking'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Agilent (BioTek)', 'model': 'Cytation 1', 'device_type_cn': '酶标仪', 'device_type_en': 'Plate Reader', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/plate_reading/agilent/biotek_cytation_backend.py', 'class_name': 'CytationBackend', 'candidate_methods': ['capture', 'close', 'get_current_temperature', 'get_firmware_version', 'get_serial_number', 'home', 'led_off', 'led_on', 'open', 'read_absorbance', 'read_fluorescence', 'read_luminescence', 'select', 'set_auto_exposure', 'set_exposure', 'set_focus', 'set_gain', 'set_imaging_mode', 'set_objective', 'set_plate', 'set_position', 'set_temperature', 'setup', 'shake', 'start_acquisition', 'stop', 'stop_acquisition', 'stop_heating_or_cooling', 'stop_shaking']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def capture(self, row=None, column=None, mode=None, objective=None, exposure_time=None, focal_height=None, gain=None, plate=None, led_intensity=None, coverage=None, center_position=None, overlap=None, color_processing_algorithm=None, pixel_format=None, auto_stop_acquisition=None, **kwargs):
        _kw = {'row': row, 'column': column, 'mode': mode, 'objective': objective, 'exposure_time': exposure_time, 'focal_height': focal_height, 'gain': gain, 'plate': plate, 'led_intensity': led_intensity, 'coverage': coverage, 'center_position': center_position, 'overlap': overlap, 'color_processing_algorithm': color_processing_algorithm, 'pixel_format': pixel_format, 'auto_stop_acquisition': auto_stop_acquisition}
        _kw.update(kwargs)
        return self.call('capture', kwargs={k: v for k, v in _kw.items() if v is not None})

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

    def led_off(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('led_off', kwargs={k: v for k, v in _kw.items() if v is not None})

    def led_on(self, intensity=None, **kwargs):
        _kw = {'intensity': intensity}
        _kw.update(kwargs)
        return self.call('led_on', kwargs={k: v for k, v in _kw.items() if v is not None})

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

    def select(self, row=None, column=None, **kwargs):
        _kw = {'row': row, 'column': column}
        _kw.update(kwargs)
        return self.call('select', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_auto_exposure(self, auto_exposure=None, **kwargs):
        _kw = {'auto_exposure': auto_exposure}
        _kw.update(kwargs)
        return self.call('set_auto_exposure', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_exposure(self, exposure=None, **kwargs):
        _kw = {'exposure': exposure}
        _kw.update(kwargs)
        return self.call('set_exposure', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_focus(self, focal_position=None, **kwargs):
        _kw = {'focal_position': focal_position}
        _kw.update(kwargs)
        return self.call('set_focus', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_gain(self, gain=None, **kwargs):
        _kw = {'gain': gain}
        _kw.update(kwargs)
        return self.call('set_gain', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_imaging_mode(self, mode=None, led_intensity=None, **kwargs):
        _kw = {'mode': mode, 'led_intensity': led_intensity}
        _kw.update(kwargs)
        return self.call('set_imaging_mode', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_objective(self, objective=None, **kwargs):
        _kw = {'objective': objective}
        _kw.update(kwargs)
        return self.call('set_objective', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_plate(self, plate=None, **kwargs):
        _kw = {'plate': plate}
        _kw.update(kwargs)
        return self.call('set_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_position(self, x=None, y=None, **kwargs):
        _kw = {'x': x, 'y': y}
        _kw.update(kwargs)
        return self.call('set_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, use_cam=None, **kwargs):
        _kw = {'use_cam': use_cam}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def shake(self, shake_type=None, frequency=None, **kwargs):
        _kw = {'shake_type': shake_type, 'frequency': frequency}
        _kw.update(kwargs)
        return self.call('shake', kwargs={k: v for k, v in _kw.items() if v is not None})

    def start_acquisition(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('start_acquisition', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_acquisition(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop_acquisition', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_heating_or_cooling(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop_heating_or_cooling', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_shaking(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop_shaking', kwargs={k: v for k, v in _kw.items() if v is not None})

