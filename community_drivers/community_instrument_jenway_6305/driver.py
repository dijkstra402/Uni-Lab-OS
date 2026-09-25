from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentJenway6305(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/davidmam__UvSpec', 'source_file': 'J6305.py', 'class_name': 'Spectrometer', 'import_roots': [], 'candidate_methods': ['pause', 'set_shutter', 'printout', 'transmission', 'absorbance', 'concentration', 'voltage', 'calibrate', 'set_wavelength', 'set_conc_factor', 'scan', 'luminosity', 'scan_to_file'], 'action_targets': {}, 'metadata': {'repo': 'davidmam/UvSpec', 'repo_url': 'https://github.com/davidmam/UvSpec', 'brand': 'Jenway', 'model': '6305', 'device_type_cn': 'UV-Vis分光光度计', 'device_type_en': 'UV-Vis Spectrophotometer', 'source_framework': '光谱分析', 'tag_id': '4439', 'tag_name': '紫外-可见分光光谱仪', 'tag_name_en': 'UV-Vis Spectrophotometer', 'candidate_score': 142, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def pause(self, **kwargs):
        return self.call('pause', kwargs=kwargs)

    def set_shutter(self, **kwargs):
        return self.call('set_shutter', kwargs=kwargs)

    def printout(self, **kwargs):
        return self.call('printout', kwargs=kwargs)

    def transmission(self, **kwargs):
        return self.call('transmission', kwargs=kwargs)

    def absorbance(self, **kwargs):
        return self.call('absorbance', kwargs=kwargs)

    def concentration(self, **kwargs):
        return self.call('concentration', kwargs=kwargs)

    def voltage(self, **kwargs):
        return self.call('voltage', kwargs=kwargs)

    def calibrate(self, **kwargs):
        return self.call('calibrate', kwargs=kwargs)

    def set_wavelength(self, **kwargs):
        return self.call('set_wavelength', kwargs=kwargs)

    def set_conc_factor(self, **kwargs):
        return self.call('set_conc_factor', kwargs=kwargs)

    def scan(self, **kwargs):
        return self.call('scan', kwargs=kwargs)

    def luminosity(self, **kwargs):
        return self.call('luminosity', kwargs=kwargs)

    def scan_to_file(self, **kwargs):
        return self.call('scan_to_file', kwargs=kwargs)

