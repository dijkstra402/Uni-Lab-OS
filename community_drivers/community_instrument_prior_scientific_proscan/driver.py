from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPriorScientificProscan(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/kleinlabphys__autoflakedet', 'source_file': 'nikon_automation/PlatformOperator.py', 'class_name': 'PlatformOperator', 'import_roots': [], 'candidate_methods': ['get_stage_xy', 'get_stage_x', 'get_stage_y', 'get_stage_z', 'get_stage_xyz', 'wait_for_platform', 'synch_go_to_xyz', 'send_prior_cmd', 'connect_to_device', 'disconnect_and_close_session'], 'action_targets': {}, 'metadata': {'repo': 'kleinlabphys/autoflakedet', 'repo_url': 'https://github.com/kleinlabphys/autoflakedet', 'brand': 'Prior Scientific', 'model': 'ProScan', 'device_type_cn': '普通光学显微镜', 'device_type_en': 'Optical Microscope', 'source_framework': '专用驱动', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 86, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_stage_xy(self, **kwargs):
        return self.call('get_stage_xy', kwargs=kwargs)

    def get_stage_x(self, **kwargs):
        return self.call('get_stage_x', kwargs=kwargs)

    def get_stage_y(self, **kwargs):
        return self.call('get_stage_y', kwargs=kwargs)

    def get_stage_z(self, **kwargs):
        return self.call('get_stage_z', kwargs=kwargs)

    def get_stage_xyz(self, **kwargs):
        return self.call('get_stage_xyz', kwargs=kwargs)

    def wait_for_platform(self, **kwargs):
        return self.call('wait_for_platform', kwargs=kwargs)

    def synch_go_to_xyz(self, **kwargs):
        return self.call('synch_go_to_xyz', kwargs=kwargs)

    def send_prior_cmd(self, **kwargs):
        return self.call('send_prior_cmd', kwargs=kwargs)

    def connect_to_device(self, **kwargs):
        return self.call('connect_to_device', kwargs=kwargs)

    def disconnect_and_close_session(self, **kwargs):
        return self.call('disconnect_and_close_session', kwargs=kwargs)

