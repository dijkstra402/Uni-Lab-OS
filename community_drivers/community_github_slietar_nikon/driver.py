from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubSlietarNikon(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/slietar_nikon', 'source_file': 'nikon/microscope.py', 'class_name': 'MicroscopeDevice', 'import_roots': [], 'candidate_methods': ['get_firmware_cpu_version', 'get_version', 'get_condenser_label', 'get_condenser_labels', 'get_filter_label', 'get_filter_labels', 'get_optical_path_label', 'get_optical_path_labels', 'get_zoom_label', 'get_zoom_labels', 'get_objective_info', 'get_objective_infos', 'get_x_bounds', 'get_y_bounds', 'get_z_bound', 'get_event', 'get_status', 'get_stable_status', 'set_x', 'set_y'], 'metadata': {'repo': 'slietar/nikon', 'repo_url': 'https://github.com/slietar/nikon', 'unit_id': 'gh_nikon_ti2_e', 'source_file': 'nikon/microscope.py', 'candidate_score': 49, 'manufacturer': 'Nikon', 'model_name': 'Nikon Ti2-E'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def get_firmware_cpu_version(self, **kwargs):
        return self.call('get_firmware_cpu_version', kwargs=kwargs)

    def get_version(self, **kwargs):
        return self.call('get_version', kwargs=kwargs)

    def get_condenser_label(self, **kwargs):
        return self.call('get_condenser_label', kwargs=kwargs)

    def get_condenser_labels(self, **kwargs):
        return self.call('get_condenser_labels', kwargs=kwargs)

    def get_filter_label(self, **kwargs):
        return self.call('get_filter_label', kwargs=kwargs)

    def get_filter_labels(self, **kwargs):
        return self.call('get_filter_labels', kwargs=kwargs)

    def get_optical_path_label(self, **kwargs):
        return self.call('get_optical_path_label', kwargs=kwargs)

    def get_optical_path_labels(self, **kwargs):
        return self.call('get_optical_path_labels', kwargs=kwargs)

    def get_zoom_label(self, **kwargs):
        return self.call('get_zoom_label', kwargs=kwargs)

    def get_zoom_labels(self, **kwargs):
        return self.call('get_zoom_labels', kwargs=kwargs)

    def get_objective_info(self, **kwargs):
        return self.call('get_objective_info', kwargs=kwargs)

    def get_objective_infos(self, **kwargs):
        return self.call('get_objective_infos', kwargs=kwargs)

    def get_x_bounds(self, **kwargs):
        return self.call('get_x_bounds', kwargs=kwargs)

    def get_y_bounds(self, **kwargs):
        return self.call('get_y_bounds', kwargs=kwargs)

    def get_z_bound(self, **kwargs):
        return self.call('get_z_bound', kwargs=kwargs)

    def get_event(self, **kwargs):
        return self.call('get_event', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def get_stable_status(self, **kwargs):
        return self.call('get_stable_status', kwargs=kwargs)

    def set_x(self, **kwargs):
        return self.call('set_x', kwargs=kwargs)

    def set_y(self, **kwargs):
        return self.call('set_y', kwargs=kwargs)

