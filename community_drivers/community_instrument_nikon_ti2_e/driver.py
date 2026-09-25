from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentNikonTi2E(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/slietar__nikon', 'source_file': 'nikon/microscope.py', 'class_name': 'MicroscopeDevice', 'import_roots': [], 'candidate_methods': ['get_firmware_cpu_version', 'get_version', 'get_condenser_label', 'get_condenser_labels', 'get_filter_label', 'get_filter_labels', 'get_optical_path_label', 'get_optical_path_labels', 'get_zoom_label', 'get_zoom_labels', 'get_objective_info', 'get_objective_infos', 'get_x_bounds', 'get_y_bounds', 'get_z_bound', 'get_event', 'get_status', 'get_stable_status', 'set_x', 'set_y', 'set_z', 'set_condenser', 'set_dia', 'set_filter', 'set_light', 'set_objective', 'set_optical_path', 'set_shutter', 'set_button_function', 'list'], 'action_targets': {}, 'metadata': {'repo': 'slietar/nikon', 'repo_url': 'https://github.com/slietar/nikon', 'brand': 'Nikon', 'model': 'Ti2-E', 'device_type_cn': '倒置显微镜', 'device_type_en': 'Inverted Microscope', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 306, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

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

    def set_z(self, **kwargs):
        return self.call('set_z', kwargs=kwargs)

    def set_condenser(self, **kwargs):
        return self.call('set_condenser', kwargs=kwargs)

    def set_dia(self, **kwargs):
        return self.call('set_dia', kwargs=kwargs)

    def set_filter(self, **kwargs):
        return self.call('set_filter', kwargs=kwargs)

    def set_light(self, **kwargs):
        return self.call('set_light', kwargs=kwargs)

    def set_objective(self, **kwargs):
        return self.call('set_objective', kwargs=kwargs)

    def set_optical_path(self, **kwargs):
        return self.call('set_optical_path', kwargs=kwargs)

    def set_shutter(self, **kwargs):
        return self.call('set_shutter', kwargs=kwargs)

    def set_button_function(self, **kwargs):
        return self.call('set_button_function', kwargs=kwargs)

    def list(self, **kwargs):
        return self.call('list', kwargs=kwargs)

