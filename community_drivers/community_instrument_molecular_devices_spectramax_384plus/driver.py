from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMolecularDevicesSpectramax384plus(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/plate_reading/molecular_devices/spectramax_384_plus_backend.py', 'class_name': 'MolecularDevicesSpectraMax384PlusBackend', 'import_roots': [], 'candidate_methods': ['clear_error_log', 'close', 'get_firmware_version', 'get_status', 'get_temperature', 'open', 'read_absorbance', 'read_error_log', 'read_fluorescence', 'read_fluorescence_polarization', 'read_luminescence', 'read_time_resolved_fluorescence', 'set_temperature', 'setup', 'start_shake', 'stop', 'stop_shake'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Molecular Devices', 'model': 'SpectraMax 384plus', 'device_type_cn': '酶标仪', 'device_type_en': 'Plate Reader', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/plate_reading/molecular_devices/spectramax_384_plus_backend.py', 'class_name': 'MolecularDevicesSpectraMax384PlusBackend', 'candidate_methods': ['clear_error_log', 'close', 'get_firmware_version', 'get_status', 'get_temperature', 'open', 'read_absorbance', 'read_error_log', 'read_fluorescence', 'read_fluorescence_polarization', 'read_luminescence', 'read_time_resolved_fluorescence', 'set_temperature', 'setup', 'start_shake', 'stop', 'stop_shake']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def clear_error_log(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('clear_error_log', kwargs={k: v for k, v in _kw.items() if v is not None})

    def close(self, plate=None, **kwargs):
        _kw = {'plate': plate}
        _kw.update(kwargs)
        return self.call('close', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_firmware_version(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_firmware_version', kwargs={k: v for k, v in _kw.items() if v is not None})

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

    def read_absorbance(self, plate=None, wavelengths=None, read_type=None, read_order=None, calibrate=None, shake_settings=None, carriage_speed=None, speed_read=None, path_check=None, kinetic_settings=None, spectrum_settings=None, cuvette=None, settling_time=None, timeout=None, **kwargs):
        _kw = {'plate': plate, 'wavelengths': wavelengths, 'read_type': read_type, 'read_order': read_order, 'calibrate': calibrate, 'shake_settings': shake_settings, 'carriage_speed': carriage_speed, 'speed_read': speed_read, 'path_check': path_check, 'kinetic_settings': kinetic_settings, 'spectrum_settings': spectrum_settings, 'cuvette': cuvette, 'settling_time': settling_time, 'timeout': timeout}
        _kw.update(kwargs)
        return self.call('read_absorbance', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_error_log(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('read_error_log', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_fluorescence(self, plate=None, excitation_wavelengths=None, emission_wavelengths=None, cutoff_filters=None, read_type=None, read_order=None, calibrate=None, shake_settings=None, carriage_speed=None, read_from_bottom=None, pmt_gain=None, flashes_per_well=None, kinetic_settings=None, spectrum_settings=None, cuvette=None, settling_time=None, timeout=None, **kwargs):
        _kw = {'plate': plate, 'excitation_wavelengths': excitation_wavelengths, 'emission_wavelengths': emission_wavelengths, 'cutoff_filters': cutoff_filters, 'read_type': read_type, 'read_order': read_order, 'calibrate': calibrate, 'shake_settings': shake_settings, 'carriage_speed': carriage_speed, 'read_from_bottom': read_from_bottom, 'pmt_gain': pmt_gain, 'flashes_per_well': flashes_per_well, 'kinetic_settings': kinetic_settings, 'spectrum_settings': spectrum_settings, 'cuvette': cuvette, 'settling_time': settling_time, 'timeout': timeout}
        _kw.update(kwargs)
        return self.call('read_fluorescence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_fluorescence_polarization(self, plate=None, excitation_wavelengths=None, emission_wavelengths=None, cutoff_filters=None, read_type=None, read_order=None, calibrate=None, shake_settings=None, carriage_speed=None, read_from_bottom=None, pmt_gain=None, flashes_per_well=None, kinetic_settings=None, spectrum_settings=None, cuvette=None, settling_time=None, timeout=None, **kwargs):
        _kw = {'plate': plate, 'excitation_wavelengths': excitation_wavelengths, 'emission_wavelengths': emission_wavelengths, 'cutoff_filters': cutoff_filters, 'read_type': read_type, 'read_order': read_order, 'calibrate': calibrate, 'shake_settings': shake_settings, 'carriage_speed': carriage_speed, 'read_from_bottom': read_from_bottom, 'pmt_gain': pmt_gain, 'flashes_per_well': flashes_per_well, 'kinetic_settings': kinetic_settings, 'spectrum_settings': spectrum_settings, 'cuvette': cuvette, 'settling_time': settling_time, 'timeout': timeout}
        _kw.update(kwargs)
        return self.call('read_fluorescence_polarization', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_luminescence(self, plate=None, emission_wavelengths=None, read_type=None, read_order=None, calibrate=None, shake_settings=None, carriage_speed=None, read_from_bottom=None, pmt_gain=None, flashes_per_well=None, kinetic_settings=None, spectrum_settings=None, cuvette=None, settling_time=None, timeout=None, **kwargs):
        _kw = {'plate': plate, 'emission_wavelengths': emission_wavelengths, 'read_type': read_type, 'read_order': read_order, 'calibrate': calibrate, 'shake_settings': shake_settings, 'carriage_speed': carriage_speed, 'read_from_bottom': read_from_bottom, 'pmt_gain': pmt_gain, 'flashes_per_well': flashes_per_well, 'kinetic_settings': kinetic_settings, 'spectrum_settings': spectrum_settings, 'cuvette': cuvette, 'settling_time': settling_time, 'timeout': timeout}
        _kw.update(kwargs)
        return self.call('read_luminescence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_time_resolved_fluorescence(self, plate=None, excitation_wavelengths=None, emission_wavelengths=None, cutoff_filters=None, delay_time=None, integration_time=None, read_type=None, read_order=None, calibrate=None, shake_settings=None, carriage_speed=None, read_from_bottom=None, pmt_gain=None, flashes_per_well=None, kinetic_settings=None, spectrum_settings=None, cuvette=None, settling_time=None, timeout=None, **kwargs):
        _kw = {'plate': plate, 'excitation_wavelengths': excitation_wavelengths, 'emission_wavelengths': emission_wavelengths, 'cutoff_filters': cutoff_filters, 'delay_time': delay_time, 'integration_time': integration_time, 'read_type': read_type, 'read_order': read_order, 'calibrate': calibrate, 'shake_settings': shake_settings, 'carriage_speed': carriage_speed, 'read_from_bottom': read_from_bottom, 'pmt_gain': pmt_gain, 'flashes_per_well': flashes_per_well, 'kinetic_settings': kinetic_settings, 'spectrum_settings': spectrum_settings, 'cuvette': cuvette, 'settling_time': settling_time, 'timeout': timeout}
        _kw.update(kwargs)
        return self.call('read_time_resolved_fluorescence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def start_shake(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('start_shake', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_shake(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop_shake', kwargs={k: v for k, v in _kw.items() if v is not None})

