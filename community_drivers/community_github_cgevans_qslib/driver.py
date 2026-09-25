from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubCgevansQslib(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/cgevans_qslib', 'source_file': 'python/qslib/machine.py', 'class_name': 'Machine', 'import_roots': [], 'candidate_methods': ['asdict', 'connection', 'connection', 'max_access_level', 'max_access_level', 'connect', 'connected', 'run_command', 'run_command_to_bytes', 'run_command_to_ack', 'run_command_bytes', 'define_protocol', 'read_dir_as_zip', 'list_files', 'list_files', 'list_files', 'list_files', 'read_file', 'write_file', 'list_runs_in_storage'], 'metadata': {'repo': 'cgevans/qslib', 'repo_url': 'https://github.com/cgevans/qslib', 'unit_id': 'gh_applied_biosystems_quantstudio_5', 'source_file': 'python/qslib/machine.py', 'candidate_score': 120, 'manufacturer': 'Applied Biosystems', 'model_name': 'Applied Biosystems QuantStudio 5'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def asdict(self, **kwargs):
        return self.call('asdict', kwargs=kwargs)

    def connection(self, **kwargs):
        return self.call('connection', kwargs=kwargs)

    def connection(self, **kwargs):
        return self.call('connection', kwargs=kwargs)

    def max_access_level(self, **kwargs):
        return self.call('max_access_level', kwargs=kwargs)

    def max_access_level(self, **kwargs):
        return self.call('max_access_level', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def connected(self, **kwargs):
        return self.call('connected', kwargs=kwargs)

    def run_command(self, **kwargs):
        return self.call('run_command', kwargs=kwargs)

    def run_command_to_bytes(self, **kwargs):
        return self.call('run_command_to_bytes', kwargs=kwargs)

    def run_command_to_ack(self, **kwargs):
        return self.call('run_command_to_ack', kwargs=kwargs)

    def run_command_bytes(self, **kwargs):
        return self.call('run_command_bytes', kwargs=kwargs)

    def define_protocol(self, **kwargs):
        return self.call('define_protocol', kwargs=kwargs)

    def read_dir_as_zip(self, **kwargs):
        return self.call('read_dir_as_zip', kwargs=kwargs)

    def list_files(self, **kwargs):
        return self.call('list_files', kwargs=kwargs)

    def list_files(self, **kwargs):
        return self.call('list_files', kwargs=kwargs)

    def list_files(self, **kwargs):
        return self.call('list_files', kwargs=kwargs)

    def list_files(self, **kwargs):
        return self.call('list_files', kwargs=kwargs)

    def read_file(self, **kwargs):
        return self.call('read_file', kwargs=kwargs)

    def write_file(self, **kwargs):
        return self.call('write_file', kwargs=kwargs)

    def list_runs_in_storage(self, **kwargs):
        return self.call('list_runs_in_storage', kwargs=kwargs)

