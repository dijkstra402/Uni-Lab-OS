from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBrukerVeecoDimensionNanoscope(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/jmarini__nanoscope', 'source_file': 'nanoscope/image.py', 'class_name': 'NanoscopeImage', 'import_roots': [], 'candidate_methods': ['data', 'process', 'flatten', 'convert', 'colorize', 'reset_height_scale', 'mean_height', 'mean_roughness', 'rms_roughness', 'total_roughness', 'max_valley', 'max_peak', 'mean_valley', 'mean_peak', 'mean_total_roughness', 'min_height', 'max_height', 'n_point_roughness', 'peak_count', 'peak_density', 'high_spot_count', 'low_spot_count'], 'action_targets': {}, 'metadata': {'repo': 'jmarini/nanoscope', 'repo_url': 'https://github.com/jmarini/nanoscope', 'brand': 'Bruker/Veeco', 'model': 'Dimension (NanoScope)', 'device_type_cn': 'AFM', 'device_type_en': 'Atomic Force Microscope', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 234, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def data(self, **kwargs):
        return self.call('data', kwargs=kwargs)

    def process(self, **kwargs):
        return self.call('process', kwargs=kwargs)

    def flatten(self, **kwargs):
        return self.call('flatten', kwargs=kwargs)

    def convert(self, **kwargs):
        return self.call('convert', kwargs=kwargs)

    def colorize(self, **kwargs):
        return self.call('colorize', kwargs=kwargs)

    def reset_height_scale(self, **kwargs):
        return self.call('reset_height_scale', kwargs=kwargs)

    def mean_height(self, **kwargs):
        return self.call('mean_height', kwargs=kwargs)

    def mean_roughness(self, **kwargs):
        return self.call('mean_roughness', kwargs=kwargs)

    def rms_roughness(self, **kwargs):
        return self.call('rms_roughness', kwargs=kwargs)

    def total_roughness(self, **kwargs):
        return self.call('total_roughness', kwargs=kwargs)

    def max_valley(self, **kwargs):
        return self.call('max_valley', kwargs=kwargs)

    def max_peak(self, **kwargs):
        return self.call('max_peak', kwargs=kwargs)

    def mean_valley(self, **kwargs):
        return self.call('mean_valley', kwargs=kwargs)

    def mean_peak(self, **kwargs):
        return self.call('mean_peak', kwargs=kwargs)

    def mean_total_roughness(self, **kwargs):
        return self.call('mean_total_roughness', kwargs=kwargs)

    def min_height(self, **kwargs):
        return self.call('min_height', kwargs=kwargs)

    def max_height(self, **kwargs):
        return self.call('max_height', kwargs=kwargs)

    def n_point_roughness(self, **kwargs):
        return self.call('n_point_roughness', kwargs=kwargs)

    def peak_count(self, **kwargs):
        return self.call('peak_count', kwargs=kwargs)

    def peak_density(self, **kwargs):
        return self.call('peak_density', kwargs=kwargs)

    def high_spot_count(self, **kwargs):
        return self.call('high_spot_count', kwargs=kwargs)

    def low_spot_count(self, **kwargs):
        return self.call('low_spot_count', kwargs=kwargs)

