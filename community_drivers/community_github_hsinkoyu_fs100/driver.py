from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubHsinkoyuFs100(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/hsinkoyu_fs100', 'source_file': 'fs100.py', 'class_name': 'FS100', 'import_roots': [], 'candidate_methods': ['switch_power', 'select_cycle', 'mov', 'pmov', 'get_last_alarm', 'read_alarm_info', 'reset_alarm', 'get_status', 'read_executing_job_info', 'play_job', 'select_job', 'delete_file', 'get_file_list', 'send_file', 'recv_file', 'read_axis_name', 'read_position', 'read_position_error', 'read_torque', 'read_variable'], 'metadata': {'repo': 'hsinkoyu/fs100', 'repo_url': 'https://github.com/hsinkoyu/fs100', 'unit_id': 'gh_yaskawa_motoman_fs100', 'source_file': 'fs100.py', 'candidate_score': 137, 'manufacturer': 'Yaskawa', 'model_name': 'Yaskawa Motoman FS100'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def switch_power(self, **kwargs):
        return self.call('switch_power', kwargs=kwargs)

    def select_cycle(self, **kwargs):
        return self.call('select_cycle', kwargs=kwargs)

    def mov(self, **kwargs):
        return self.call('mov', kwargs=kwargs)

    def pmov(self, **kwargs):
        return self.call('pmov', kwargs=kwargs)

    def get_last_alarm(self, **kwargs):
        return self.call('get_last_alarm', kwargs=kwargs)

    def read_alarm_info(self, **kwargs):
        return self.call('read_alarm_info', kwargs=kwargs)

    def reset_alarm(self, **kwargs):
        return self.call('reset_alarm', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def read_executing_job_info(self, **kwargs):
        return self.call('read_executing_job_info', kwargs=kwargs)

    def play_job(self, **kwargs):
        return self.call('play_job', kwargs=kwargs)

    def select_job(self, **kwargs):
        return self.call('select_job', kwargs=kwargs)

    def delete_file(self, **kwargs):
        return self.call('delete_file', kwargs=kwargs)

    def get_file_list(self, **kwargs):
        return self.call('get_file_list', kwargs=kwargs)

    def send_file(self, **kwargs):
        return self.call('send_file', kwargs=kwargs)

    def recv_file(self, **kwargs):
        return self.call('recv_file', kwargs=kwargs)

    def read_axis_name(self, **kwargs):
        return self.call('read_axis_name', kwargs=kwargs)

    def read_position(self, **kwargs):
        return self.call('read_position', kwargs=kwargs)

    def read_position_error(self, **kwargs):
        return self.call('read_position_error', kwargs=kwargs)

    def read_torque(self, **kwargs):
        return self.call('read_torque', kwargs=kwargs)

    def read_variable(self, **kwargs):
        return self.call('read_variable', kwargs=kwargs)

