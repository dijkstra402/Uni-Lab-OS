from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAppliedBiosystemsQuantstudio5(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/cgevans__qslib', 'source_file': 'python/qslib/machine.py', 'class_name': 'Machine', 'import_roots': ['src', 'python'], 'candidate_methods': ['asdict', 'connection', 'max_access_level', 'connect', 'connected', 'run_command', 'run_command_to_bytes', 'run_command_to_ack', 'run_command_bytes', 'define_protocol', 'read_dir_as_zip', 'list_files', 'read_file', 'write_file', 'list_runs_in_storage', 'load_run_from_storage', 'save_run_from_storage', 'run_status', 'machine_status', 'get_running_protocol', 'set_access_level', 'get_access_level', 'authenticate', 'access_level', 'drawer_open', 'drawer_close', 'block', 'status', 'drawer_position', 'cover_position', 'cover_lower', 'disconnect', 'abort_current_run', 'stop_current_run', 'pause_current_run', 'pause_current_run_at_temperature', 'resume_current_run', 'power', 'current_run_name', 'restart_system', 'at_access', 'ensured_connection', 'compile_eds', 'get_exp_file', 'get_sds_file', 'get_run_start_time', 'get_filterdata_one', 'get_all_filterdata', 'get_expfile_list', 'get_run_title'], 'action_targets': {}, 'metadata': {'repo': 'cgevans/qslib', 'repo_url': 'https://github.com/cgevans/qslib', 'brand': 'Applied Biosystems', 'model': 'QuantStudio 5', 'device_type_cn': '实时定量PCR仪', 'device_type_en': 'Real-Time qPCR', 'source_framework': '生命科学', 'tag_id': '4383', 'tag_name': '实时定量PCR仪', 'tag_name_en': 'Real-Time Quantitative PCR', 'candidate_score': 438, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def asdict(self, **kwargs):
        return self.call('asdict', kwargs=kwargs)

    def connection(self, **kwargs):
        return self.call('connection', kwargs=kwargs)

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

    def read_file(self, **kwargs):
        return self.call('read_file', kwargs=kwargs)

    def write_file(self, **kwargs):
        return self.call('write_file', kwargs=kwargs)

    def list_runs_in_storage(self, **kwargs):
        return self.call('list_runs_in_storage', kwargs=kwargs)

    def load_run_from_storage(self, **kwargs):
        return self.call('load_run_from_storage', kwargs=kwargs)

    def save_run_from_storage(self, **kwargs):
        return self.call('save_run_from_storage', kwargs=kwargs)

    def run_status(self, **kwargs):
        return self.call('run_status', kwargs=kwargs)

    def machine_status(self, **kwargs):
        return self.call('machine_status', kwargs=kwargs)

    def get_running_protocol(self, **kwargs):
        return self.call('get_running_protocol', kwargs=kwargs)

    def set_access_level(self, **kwargs):
        return self.call('set_access_level', kwargs=kwargs)

    def get_access_level(self, **kwargs):
        return self.call('get_access_level', kwargs=kwargs)

    def authenticate(self, **kwargs):
        return self.call('authenticate', kwargs=kwargs)

    def access_level(self, **kwargs):
        return self.call('access_level', kwargs=kwargs)

    def drawer_open(self, **kwargs):
        return self.call('drawer_open', kwargs=kwargs)

    def drawer_close(self, **kwargs):
        return self.call('drawer_close', kwargs=kwargs)

    def block(self, **kwargs):
        return self.call('block', kwargs=kwargs)

    def status(self, **kwargs):
        return self.call('status', kwargs=kwargs)

    def drawer_position(self, **kwargs):
        return self.call('drawer_position', kwargs=kwargs)

    def cover_position(self, **kwargs):
        return self.call('cover_position', kwargs=kwargs)

    def cover_lower(self, **kwargs):
        return self.call('cover_lower', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def abort_current_run(self, **kwargs):
        return self.call('abort_current_run', kwargs=kwargs)

    def stop_current_run(self, **kwargs):
        return self.call('stop_current_run', kwargs=kwargs)

    def pause_current_run(self, **kwargs):
        return self.call('pause_current_run', kwargs=kwargs)

    def pause_current_run_at_temperature(self, **kwargs):
        return self.call('pause_current_run_at_temperature', kwargs=kwargs)

    def resume_current_run(self, **kwargs):
        return self.call('resume_current_run', kwargs=kwargs)

    def power(self, **kwargs):
        return self.call('power', kwargs=kwargs)

    def current_run_name(self, **kwargs):
        return self.call('current_run_name', kwargs=kwargs)

    def restart_system(self, **kwargs):
        return self.call('restart_system', kwargs=kwargs)

    def at_access(self, **kwargs):
        return self.call('at_access', kwargs=kwargs)

    def ensured_connection(self, **kwargs):
        return self.call('ensured_connection', kwargs=kwargs)

    def compile_eds(self, **kwargs):
        return self.call('compile_eds', kwargs=kwargs)

    def get_exp_file(self, **kwargs):
        return self.call('get_exp_file', kwargs=kwargs)

    def get_sds_file(self, **kwargs):
        return self.call('get_sds_file', kwargs=kwargs)

    def get_run_start_time(self, **kwargs):
        return self.call('get_run_start_time', kwargs=kwargs)

    def get_filterdata_one(self, **kwargs):
        return self.call('get_filterdata_one', kwargs=kwargs)

    def get_all_filterdata(self, **kwargs):
        return self.call('get_all_filterdata', kwargs=kwargs)

    def get_expfile_list(self, **kwargs):
        return self.call('get_expfile_list', kwargs=kwargs)

    def get_run_title(self, **kwargs):
        return self.call('get_run_title', kwargs=kwargs)

