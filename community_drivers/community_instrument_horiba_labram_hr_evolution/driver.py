from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHoribaLabramHrEvolution(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Arcadia-Science__ramanalysis', 'source_file': 'ramanalysis/spectra.py', 'class_name': 'RamanSpectrum', 'import_roots': [], 'candidate_methods': ['from_openraman_csvfiles', 'from_horiba_txtfile', 'from_renishaw_txtfile', 'from_wasatch_csvfile', 'from_generic_csvfile', 'snr', 'between', 'interpolate', 'normalize', 'standardize', 'smooth', 'find_n_most_prominent_wavenumbers', 'find_prominent_wavenumbers'], 'action_targets': {}, 'metadata': {'repo': 'Arcadia-Science/ramanalysis', 'repo_url': 'https://github.com/Arcadia-Science/ramanalysis', 'brand': 'Horiba', 'model': 'LabRAM HR Evolution', 'device_type_cn': '拉曼光谱仪', 'device_type_en': 'Raman Spectrometer', 'source_framework': '光谱分析', 'tag_id': '4392', 'tag_name': '拉曼光谱仪', 'tag_name_en': 'Raman Spectrometer', 'candidate_score': 162, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def from_openraman_csvfiles(self, **kwargs):
        return self.call('from_openraman_csvfiles', kwargs=kwargs)

    def from_horiba_txtfile(self, **kwargs):
        return self.call('from_horiba_txtfile', kwargs=kwargs)

    def from_renishaw_txtfile(self, **kwargs):
        return self.call('from_renishaw_txtfile', kwargs=kwargs)

    def from_wasatch_csvfile(self, **kwargs):
        return self.call('from_wasatch_csvfile', kwargs=kwargs)

    def from_generic_csvfile(self, **kwargs):
        return self.call('from_generic_csvfile', kwargs=kwargs)

    def snr(self, **kwargs):
        return self.call('snr', kwargs=kwargs)

    def between(self, **kwargs):
        return self.call('between', kwargs=kwargs)

    def interpolate(self, **kwargs):
        return self.call('interpolate', kwargs=kwargs)

    def normalize(self, **kwargs):
        return self.call('normalize', kwargs=kwargs)

    def standardize(self, **kwargs):
        return self.call('standardize', kwargs=kwargs)

    def smooth(self, **kwargs):
        return self.call('smooth', kwargs=kwargs)

    def find_n_most_prominent_wavenumbers(self, **kwargs):
        return self.call('find_n_most_prominent_wavenumbers', kwargs=kwargs)

    def find_prominent_wavenumbers(self, **kwargs):
        return self.call('find_prominent_wavenumbers', kwargs=kwargs)

