from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubTorayeffFanucpy(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/torayeff_fanucpy', 'source_file': 'src/fanucpy/robot.py', 'class_name': 'Robot', 'import_roots': [], 'candidate_methods': ['handle_response', 'connect', 'disconnect', 'send_cmd', 'call_prog', 'get_ins_power', 'get_curpos', 'get_curjpos', 'move', 'gripper', 'get_rdo', 'set_rdo', 'get_dout', 'set_dout', 'set_sys_var'], 'metadata': {'repo': 'torayeff/fanucpy', 'repo_url': 'https://github.com/torayeff/fanucpy', 'unit_id': 'gh_fanuc_r_30ib', 'source_file': 'src/fanucpy/robot.py', 'candidate_score': 120, 'manufacturer': 'FANUC', 'model_name': 'FANUC R-30iB/R-30iA'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def handle_response(self, **kwargs):
        return self.call('handle_response', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def send_cmd(self, **kwargs):
        return self.call('send_cmd', kwargs=kwargs)

    def call_prog(self, **kwargs):
        return self.call('call_prog', kwargs=kwargs)

    def get_ins_power(self, **kwargs):
        return self.call('get_ins_power', kwargs=kwargs)

    def get_curpos(self, **kwargs):
        return self.call('get_curpos', kwargs=kwargs)

    def get_curjpos(self, **kwargs):
        return self.call('get_curjpos', kwargs=kwargs)

    def move(self, **kwargs):
        return self.call('move', kwargs=kwargs)

    def gripper(self, **kwargs):
        return self.call('gripper', kwargs=kwargs)

    def get_rdo(self, **kwargs):
        return self.call('get_rdo', kwargs=kwargs)

    def set_rdo(self, **kwargs):
        return self.call('set_rdo', kwargs=kwargs)

    def get_dout(self, **kwargs):
        return self.call('get_dout', kwargs=kwargs)

    def set_dout(self, **kwargs):
        return self.call('set_dout', kwargs=kwargs)

    def set_sys_var(self, **kwargs):
        return self.call('set_sys_var', kwargs=kwargs)

