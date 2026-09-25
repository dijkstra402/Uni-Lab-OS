from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPerkinelmerLambda750(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Cambridge-PAM__spectroscopy', 'source_file': 'spectroscopy/plotting.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['create_figure', 'plot_series', 'plot_dataframe_columns', 'finalize_axis', 'add_vertical_markers', 'save_figure', 'plot_perkin_data_overview', 'plot_fluorolog_overview'], 'action_targets': {'create_figure': 'create_figure', 'plot_series': 'plot_series', 'plot_dataframe_columns': 'plot_dataframe_columns', 'finalize_axis': 'finalize_axis', 'add_vertical_markers': 'add_vertical_markers', 'save_figure': 'save_figure', 'plot_perkin_data_overview': 'plot_perkin_data_overview', 'plot_fluorolog_overview': 'plot_fluorolog_overview'}, 'metadata': {'repo': 'Cambridge-PAM/spectroscopy', 'repo_url': 'https://github.com/Cambridge-PAM/spectroscopy', 'brand': 'PerkinElmer', 'model': 'Lambda 750', 'device_type_cn': 'UV-Vis/NIR分光光度计', 'device_type_en': 'UV-Vis/NIR Spectrophotometer', 'source_framework': '光谱分析', 'tag_id': '4439', 'tag_name': '紫外-可见分光光谱仪', 'tag_name_en': 'UV-Vis Spectrophotometer', 'candidate_score': 64, 'parse_status': 'module_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'create_figure': 'create_figure', 'plot_series': 'plot_series', 'plot_dataframe_columns': 'plot_dataframe_columns', 'finalize_axis': 'finalize_axis', 'add_vertical_markers': 'add_vertical_markers', 'save_figure': 'save_figure', 'plot_perkin_data_overview': 'plot_perkin_data_overview', 'plot_fluorolog_overview': 'plot_fluorolog_overview'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def create_figure(self, **kwargs):
        return self.call('create_figure', kwargs=kwargs)

    def plot_series(self, **kwargs):
        return self.call('plot_series', kwargs=kwargs)

    def plot_dataframe_columns(self, **kwargs):
        return self.call('plot_dataframe_columns', kwargs=kwargs)

    def finalize_axis(self, **kwargs):
        return self.call('finalize_axis', kwargs=kwargs)

    def add_vertical_markers(self, **kwargs):
        return self.call('add_vertical_markers', kwargs=kwargs)

    def save_figure(self, **kwargs):
        return self.call('save_figure', kwargs=kwargs)

    def plot_perkin_data_overview(self, **kwargs):
        return self.call('plot_perkin_data_overview', kwargs=kwargs)

    def plot_fluorolog_overview(self, **kwargs):
        return self.call('plot_fluorolog_overview', kwargs=kwargs)

