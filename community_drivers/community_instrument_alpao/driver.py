from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAlpao(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/python-microscope__microscope', 'source_file': 'microscope/controllers/asi.py', 'class_name': 'ASIMS2000', 'import_roots': [], 'candidate_methods': ['devices', 'get_is_enabled', 'disable', 'enable', 'initialize', 'shutdown', 'add_setting', 'get_setting', 'get_all_settings', 'set_setting', 'describe_setting', 'describe_settings', 'update_settings'], 'action_targets': {}, 'metadata': {'repo': 'python-microscope/microscope', 'repo_url': 'https://github.com/python-microscope/microscope', 'brand': 'ALPAO', 'model': '变形镜', 'device_type_cn': '变形镜', 'device_type_en': 'Deformable Mirror', 'source_framework': 'python-microscope', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 201, 'parse_status': 'class_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def devices(self, **kwargs):
        return self.call('devices', kwargs=kwargs)

    def get_is_enabled(self, **kwargs):
        return self.call('get_is_enabled', kwargs=kwargs)

    def disable(self, **kwargs):
        return self.call('disable', kwargs=kwargs)

    def enable(self, **kwargs):
        return self.call('enable', kwargs=kwargs)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

    def add_setting(self, **kwargs):
        return self.call('add_setting', kwargs=kwargs)

    def get_setting(self, **kwargs):
        return self.call('get_setting', kwargs=kwargs)

    def get_all_settings(self, **kwargs):
        return self.call('get_all_settings', kwargs=kwargs)

    def set_setting(self, **kwargs):
        return self.call('set_setting', kwargs=kwargs)

    def describe_setting(self, **kwargs):
        return self.call('describe_setting', kwargs=kwargs)

    def describe_settings(self, **kwargs):
        return self.call('describe_settings', kwargs=kwargs)

    def update_settings(self, **kwargs):
        return self.call('update_settings', kwargs=kwargs)

