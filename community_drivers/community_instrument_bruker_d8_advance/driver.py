from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBrukerD8Advance(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/bluesky__hklpy', 'source_file': 'hkl/calc.py', 'class_name': 'CalcRecip', 'import_roots': [], 'candidate_methods': ['Position', 'wavelength', 'energy', 'engine_locked', 'engine', 'axes_r', 'axes_w', 'axes_c', 'geometry_name', 'geometry_table', 'sample_name', 'sample', 'add_sample', 'new_sample', 'engines', 'parameters', 'physical_axis_names', 'inverted_axes', 'physical_positions', 'physical_axes', 'pseudo_axis_names', 'pseudo_positions', 'pseudo_axes', 'update', 'units', 'forward_iter', 'forward', 'inverse', 'calc_linear_path', 'get_path'], 'action_targets': {}, 'metadata': {'repo': 'bluesky/hklpy', 'repo_url': 'https://github.com/bluesky/hklpy', 'brand': 'Bruker', 'model': 'D8 Advance', 'device_type_cn': 'X射线衍射仪', 'device_type_en': 'X-Ray Diffractometer', 'source_framework': 'hklpy/bluesky', 'tag_id': '4362', 'tag_name': 'X射线衍射仪', 'tag_name_en': 'X-Ray Diffractometer', 'candidate_score': 270, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def Position(self, **kwargs):
        return self.call('Position', kwargs=kwargs)

    def wavelength(self, **kwargs):
        return self.call('wavelength', kwargs=kwargs)

    def energy(self, **kwargs):
        return self.call('energy', kwargs=kwargs)

    def engine_locked(self, **kwargs):
        return self.call('engine_locked', kwargs=kwargs)

    def engine(self, **kwargs):
        return self.call('engine', kwargs=kwargs)

    def axes_r(self, **kwargs):
        return self.call('axes_r', kwargs=kwargs)

    def axes_w(self, **kwargs):
        return self.call('axes_w', kwargs=kwargs)

    def axes_c(self, **kwargs):
        return self.call('axes_c', kwargs=kwargs)

    def geometry_name(self, **kwargs):
        return self.call('geometry_name', kwargs=kwargs)

    def geometry_table(self, **kwargs):
        return self.call('geometry_table', kwargs=kwargs)

    def sample_name(self, **kwargs):
        return self.call('sample_name', kwargs=kwargs)

    def sample(self, **kwargs):
        return self.call('sample', kwargs=kwargs)

    def add_sample(self, **kwargs):
        return self.call('add_sample', kwargs=kwargs)

    def new_sample(self, **kwargs):
        return self.call('new_sample', kwargs=kwargs)

    def engines(self, **kwargs):
        return self.call('engines', kwargs=kwargs)

    def parameters(self, **kwargs):
        return self.call('parameters', kwargs=kwargs)

    def physical_axis_names(self, **kwargs):
        return self.call('physical_axis_names', kwargs=kwargs)

    def inverted_axes(self, **kwargs):
        return self.call('inverted_axes', kwargs=kwargs)

    def physical_positions(self, **kwargs):
        return self.call('physical_positions', kwargs=kwargs)

    def physical_axes(self, **kwargs):
        return self.call('physical_axes', kwargs=kwargs)

    def pseudo_axis_names(self, **kwargs):
        return self.call('pseudo_axis_names', kwargs=kwargs)

    def pseudo_positions(self, **kwargs):
        return self.call('pseudo_positions', kwargs=kwargs)

    def pseudo_axes(self, **kwargs):
        return self.call('pseudo_axes', kwargs=kwargs)

    def update(self, **kwargs):
        return self.call('update', kwargs=kwargs)

    def units(self, **kwargs):
        return self.call('units', kwargs=kwargs)

    def forward_iter(self, **kwargs):
        return self.call('forward_iter', kwargs=kwargs)

    def forward(self, **kwargs):
        return self.call('forward', kwargs=kwargs)

    def inverse(self, **kwargs):
        return self.call('inverse', kwargs=kwargs)

    def calc_linear_path(self, **kwargs):
        return self.call('calc_linear_path', kwargs=kwargs)

    def get_path(self, **kwargs):
        return self.call('get_path', kwargs=kwargs)

