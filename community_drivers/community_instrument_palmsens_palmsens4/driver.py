from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPalmsensPalmsens4(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PalmSens__PalmSens_SDK', 'source_file': 'python/src/pypalmsens/_data/curve.py', 'class_name': 'Curve', 'import_roots': ['python'], 'candidate_methods': ['copy', 'smooth', 'savitsky_golay', 'find_peaks', 'find_peaks_semiderivative', 'max_x', 'max_y', 'min_x', 'min_y', 'mux_channel', 'n_points', 'ocp_value', 'reference_electrode_name', 'reference_electrode_potential', 'x_unit', 'x_label', 'y_unit', 'y_label', 'z_unit', 'z_label', 'title', 'peaks', 'clear_peaks', 'x_array', 'y_array', 'linear_slope', 'plot'], 'action_targets': {}, 'metadata': {'repo': 'PalmSens/PalmSens_SDK', 'repo_url': 'https://github.com/PalmSens/PalmSens_SDK', 'brand': 'PalmSens', 'model': 'PalmSens4', 'device_type_cn': '电化学反应器', 'device_type_en': 'Electrochemical Reactor', 'source_framework': '官方SDK', 'tag_id': '4424', 'tag_name': '电化学反应器', 'tag_name_en': 'Electrochemical Reactor', 'candidate_score': 254, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def copy(self, **kwargs):
        return self.call('copy', kwargs=kwargs)

    def smooth(self, **kwargs):
        return self.call('smooth', kwargs=kwargs)

    def savitsky_golay(self, **kwargs):
        return self.call('savitsky_golay', kwargs=kwargs)

    def find_peaks(self, **kwargs):
        return self.call('find_peaks', kwargs=kwargs)

    def find_peaks_semiderivative(self, **kwargs):
        return self.call('find_peaks_semiderivative', kwargs=kwargs)

    def max_x(self, **kwargs):
        return self.call('max_x', kwargs=kwargs)

    def max_y(self, **kwargs):
        return self.call('max_y', kwargs=kwargs)

    def min_x(self, **kwargs):
        return self.call('min_x', kwargs=kwargs)

    def min_y(self, **kwargs):
        return self.call('min_y', kwargs=kwargs)

    def mux_channel(self, **kwargs):
        return self.call('mux_channel', kwargs=kwargs)

    def n_points(self, **kwargs):
        return self.call('n_points', kwargs=kwargs)

    def ocp_value(self, **kwargs):
        return self.call('ocp_value', kwargs=kwargs)

    def reference_electrode_name(self, **kwargs):
        return self.call('reference_electrode_name', kwargs=kwargs)

    def reference_electrode_potential(self, **kwargs):
        return self.call('reference_electrode_potential', kwargs=kwargs)

    def x_unit(self, **kwargs):
        return self.call('x_unit', kwargs=kwargs)

    def x_label(self, **kwargs):
        return self.call('x_label', kwargs=kwargs)

    def y_unit(self, **kwargs):
        return self.call('y_unit', kwargs=kwargs)

    def y_label(self, **kwargs):
        return self.call('y_label', kwargs=kwargs)

    def z_unit(self, **kwargs):
        return self.call('z_unit', kwargs=kwargs)

    def z_label(self, **kwargs):
        return self.call('z_label', kwargs=kwargs)

    def title(self, **kwargs):
        return self.call('title', kwargs=kwargs)

    def peaks(self, **kwargs):
        return self.call('peaks', kwargs=kwargs)

    def clear_peaks(self, **kwargs):
        return self.call('clear_peaks', kwargs=kwargs)

    def x_array(self, **kwargs):
        return self.call('x_array', kwargs=kwargs)

    def y_array(self, **kwargs):
        return self.call('y_array', kwargs=kwargs)

    def linear_slope(self, **kwargs):
        return self.call('linear_slope', kwargs=kwargs)

    def plot(self, **kwargs):
        return self.call('plot', kwargs=kwargs)

