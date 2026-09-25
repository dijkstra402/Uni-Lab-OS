from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentUniversalRobotsUr3e(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/UniversalRobots__RTDE_Python_Client_Library', 'source_file': 'rtde/rtde.py', 'class_name': 'RTDE', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'is_connected', 'get_controller_version', 'negotiate_protocol_version', 'send_input_setup', 'send_output_setup', 'send_start', 'send_pause', 'send', 'receive', 'receive_buffered', 'send_message', 'has_data', 'skipped_package_count'], 'action_targets': {}, 'metadata': {'repo': 'UniversalRobots/RTDE_Python_Client_Library', 'repo_url': 'https://github.com/UniversalRobots/RTDE_Python_Client_Library', 'brand': 'Universal Robots', 'model': 'UR3e', 'device_type_cn': '协作机械臂', 'device_type_en': 'Collaborative Robot', 'source_framework': 'ur_rtde', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 170, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def is_connected(self, **kwargs):
        return self.call('is_connected', kwargs=kwargs)

    def get_controller_version(self, **kwargs):
        return self.call('get_controller_version', kwargs=kwargs)

    def negotiate_protocol_version(self, **kwargs):
        return self.call('negotiate_protocol_version', kwargs=kwargs)

    def send_input_setup(self, **kwargs):
        return self.call('send_input_setup', kwargs=kwargs)

    def send_output_setup(self, **kwargs):
        return self.call('send_output_setup', kwargs=kwargs)

    def send_start(self, **kwargs):
        return self.call('send_start', kwargs=kwargs)

    def send_pause(self, **kwargs):
        return self.call('send_pause', kwargs=kwargs)

    def send(self, **kwargs):
        return self.call('send', kwargs=kwargs)

    def receive(self, **kwargs):
        return self.call('receive', kwargs=kwargs)

    def receive_buffered(self, **kwargs):
        return self.call('receive_buffered', kwargs=kwargs)

    def send_message(self, **kwargs):
        return self.call('send_message', kwargs=kwargs)

    def has_data(self, **kwargs):
        return self.call('has_data', kwargs=kwargs)

    def skipped_package_count(self, **kwargs):
        return self.call('skipped_package_count', kwargs=kwargs)

