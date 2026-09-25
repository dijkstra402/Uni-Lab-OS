from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOceanOpticsHr4000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/ap--__python-seabreeze', 'source_file': 'src/seabreeze/spectrometers.py', 'class_name': 'Spectrometer', 'import_roots': ['src'], 'candidate_methods': ['from_first_available', 'from_serial_number', 'wavelengths', 'intensities', 'max_intensity', 'spectrum', 'integration_time_micros', 'integration_time_micros_limits', 'trigger_mode', 'serial_number', 'model', 'pixels', 'features', 'f', 'open', 'close'], 'action_targets': {}, 'metadata': {'repo': 'ap--/python-seabreeze', 'repo_url': 'https://github.com/ap--/python-seabreeze', 'brand': 'Ocean Optics', 'model': 'HR4000', 'device_type_cn': '紫外-可见分光光谱仪', 'device_type_en': 'UV-Vis Spectrophotometer', 'source_framework': 'python-seabreeze', 'tag_id': '4439', 'tag_name': '紫外-可见分光光谱仪', 'tag_name_en': 'UV-Vis Spectrophotometer', 'candidate_score': 166, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def from_first_available(self, **kwargs):
        return self.call('from_first_available', kwargs=kwargs)

    def from_serial_number(self, **kwargs):
        return self.call('from_serial_number', kwargs=kwargs)

    def wavelengths(self, **kwargs):
        return self.call('wavelengths', kwargs=kwargs)

    def intensities(self, **kwargs):
        return self.call('intensities', kwargs=kwargs)

    def max_intensity(self, **kwargs):
        return self.call('max_intensity', kwargs=kwargs)

    def spectrum(self, **kwargs):
        return self.call('spectrum', kwargs=kwargs)

    def integration_time_micros(self, **kwargs):
        return self.call('integration_time_micros', kwargs=kwargs)

    def integration_time_micros_limits(self, **kwargs):
        return self.call('integration_time_micros_limits', kwargs=kwargs)

    def trigger_mode(self, **kwargs):
        return self.call('trigger_mode', kwargs=kwargs)

    def serial_number(self, **kwargs):
        return self.call('serial_number', kwargs=kwargs)

    def model(self, **kwargs):
        return self.call('model', kwargs=kwargs)

    def pixels(self, **kwargs):
        return self.call('pixels', kwargs=kwargs)

    def features(self, **kwargs):
        return self.call('features', kwargs=kwargs)

    def f(self, **kwargs):
        return self.call('f', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

