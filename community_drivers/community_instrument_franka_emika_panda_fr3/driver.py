from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentFrankaEmikaPandaFr3(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/JeanElsner__panda-py', 'source_file': 'src/panda_py/__init__.py', 'class_name': 'Desk', 'import_roots': ['src'], 'candidate_methods': ['lock', 'unlock', 'reboot', 'activate_fci', 'deactivate_fci', 'take_control', 'release_control', 'encode_password', 'login', 'logout', 'has_control', 'listen', 'stop_listen'], 'action_targets': {}, 'metadata': {'repo': 'JeanElsner/panda-py', 'repo_url': 'https://github.com/JeanElsner/panda-py', 'brand': 'Franka Emika', 'model': 'Panda / FR3', 'device_type_cn': '协作机械臂', 'device_type_en': 'Collaborative Robot', 'source_framework': '机器人/运动控制', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 142, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def lock(self, **kwargs):
        return self.call('lock', kwargs=kwargs)

    def unlock(self, **kwargs):
        return self.call('unlock', kwargs=kwargs)

    def reboot(self, **kwargs):
        return self.call('reboot', kwargs=kwargs)

    def activate_fci(self, **kwargs):
        return self.call('activate_fci', kwargs=kwargs)

    def deactivate_fci(self, **kwargs):
        return self.call('deactivate_fci', kwargs=kwargs)

    def take_control(self, **kwargs):
        return self.call('take_control', kwargs=kwargs)

    def release_control(self, **kwargs):
        return self.call('release_control', kwargs=kwargs)

    def encode_password(self, **kwargs):
        return self.call('encode_password', kwargs=kwargs)

    def login(self, **kwargs):
        return self.call('login', kwargs=kwargs)

    def logout(self, **kwargs):
        return self.call('logout', kwargs=kwargs)

    def has_control(self, **kwargs):
        return self.call('has_control', kwargs=kwargs)

    def listen(self, **kwargs):
        return self.call('listen', kwargs=kwargs)

    def stop_listen(self, **kwargs):
        return self.call('stop_listen', kwargs=kwargs)

