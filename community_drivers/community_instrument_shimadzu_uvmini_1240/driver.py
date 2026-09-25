from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentShimadzuUvmini1240(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/paulbnjl__PySerSpec', 'source_file': 'PySerSpec/data_proc.py', 'class_name': 'DataProcessing', 'import_roots': [], 'candidate_methods': ['data_spectrum', 'data_time_range1', 'data_time_range2', 'data_time_range3', 'data_time_range4', 'data_value', 'data_plot', 'data_save_csv', 'data_save_csv_mono'], 'action_targets': {}, 'metadata': {'repo': 'paulbnjl/PySerSpec', 'repo_url': 'https://github.com/paulbnjl/PySerSpec', 'brand': 'Shimadzu', 'model': 'UVmini-1240', 'device_type_cn': 'UV分光光度计', 'device_type_en': 'UV Spectrophotometer', 'source_framework': '色谱/质谱', 'tag_id': '4439', 'tag_name': '紫外-可见分光光谱仪', 'tag_name_en': 'UV-Vis Spectrophotometer', 'candidate_score': 110, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def data_spectrum(self, **kwargs):
        return self.call('data_spectrum', kwargs=kwargs)

    def data_time_range1(self, **kwargs):
        return self.call('data_time_range1', kwargs=kwargs)

    def data_time_range2(self, **kwargs):
        return self.call('data_time_range2', kwargs=kwargs)

    def data_time_range3(self, **kwargs):
        return self.call('data_time_range3', kwargs=kwargs)

    def data_time_range4(self, **kwargs):
        return self.call('data_time_range4', kwargs=kwargs)

    def data_value(self, **kwargs):
        return self.call('data_value', kwargs=kwargs)

    def data_plot(self, **kwargs):
        return self.call('data_plot', kwargs=kwargs)

    def data_save_csv(self, **kwargs):
        return self.call('data_save_csv', kwargs=kwargs)

    def data_save_csv_mono(self, **kwargs):
        return self.call('data_save_csv_mono', kwargs=kwargs)

