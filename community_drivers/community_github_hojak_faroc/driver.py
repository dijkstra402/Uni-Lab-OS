from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubHojakFaroc(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/hojak_faroc', 'source_file': 'src/faroc/faroc.py', 'class_name': 'FaRoC_Reader', 'import_roots': [], 'candidate_methods': ['status', 'connect', 'disconnect', 'send_cmd', 'handle_response', 'ping', 'error_detail', 'get_curpos', 'get_curjpos', 'get_rdo', 'get_rdi', 'get_flag', 'get_var', 'get_var_list', 'get_ins_power', 'get_mch_pos', 'get_rem_ofs', 'get_app_ofs', 'get_var_type', 'sort_var_list'], 'metadata': {'repo': 'hojak/faroc', 'repo_url': 'https://github.com/hojak/faroc', 'unit_id': '', 'source_file': 'src/faroc/faroc.py', 'candidate_score': 147, 'manufacturer': '', 'model_name': ''}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def status(self, **kwargs):
        return self.call('status', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def send_cmd(self, **kwargs):
        return self.call('send_cmd', kwargs=kwargs)

    def handle_response(self, **kwargs):
        return self.call('handle_response', kwargs=kwargs)

    def ping(self, **kwargs):
        return self.call('ping', kwargs=kwargs)

    def error_detail(self, **kwargs):
        return self.call('error_detail', kwargs=kwargs)

    def get_curpos(self, **kwargs):
        return self.call('get_curpos', kwargs=kwargs)

    def get_curjpos(self, **kwargs):
        return self.call('get_curjpos', kwargs=kwargs)

    def get_rdo(self, **kwargs):
        return self.call('get_rdo', kwargs=kwargs)

    def get_rdi(self, **kwargs):
        return self.call('get_rdi', kwargs=kwargs)

    def get_flag(self, **kwargs):
        return self.call('get_flag', kwargs=kwargs)

    def get_var(self, **kwargs):
        return self.call('get_var', kwargs=kwargs)

    def get_var_list(self, **kwargs):
        return self.call('get_var_list', kwargs=kwargs)

    def get_ins_power(self, **kwargs):
        return self.call('get_ins_power', kwargs=kwargs)

    def get_mch_pos(self, **kwargs):
        return self.call('get_mch_pos', kwargs=kwargs)

    def get_rem_ofs(self, **kwargs):
        return self.call('get_rem_ofs', kwargs=kwargs)

    def get_app_ofs(self, **kwargs):
        return self.call('get_app_ofs', kwargs=kwargs)

    def get_var_type(self, **kwargs):
        return self.call('get_var_type', kwargs=kwargs)

    def sort_var_list(self, **kwargs):
        return self.call('sort_var_list', kwargs=kwargs)

