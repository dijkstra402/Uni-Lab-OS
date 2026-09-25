from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubHailegroupNupylab(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/hailegroup_nupylab', 'source_file': 'nupylab/drivers/eurotherm2400.py', 'class_name': 'Eurotherm2400', 'import_roots': [], 'candidate_methods': ['read_float', 'write_float', 'read_time', 'write_time', 'process_value', 'output_level', 'target_setpoint', 'target_setpoint', 'operating_mode', 'operating_mode', 'working_setpoint', 'current_program', 'current_program', 'program_status', 'program_status', 'programmer_setpoint', 'programmer_cycles', 'current_segment_number', 'current_segment_type', 'segment_time_remaining'], 'metadata': {'repo': 'hailegroup/nupylab', 'repo_url': 'https://github.com/hailegroup/nupylab', 'unit_id': 'gh_eurotherm_3216', 'source_file': 'nupylab/drivers/eurotherm2400.py', 'candidate_score': 179, 'manufacturer': 'Eurotherm', 'model_name': 'Eurotherm 3216'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def read_float(self, **kwargs):
        return self.call('read_float', kwargs=kwargs)

    def write_float(self, **kwargs):
        return self.call('write_float', kwargs=kwargs)

    def read_time(self, **kwargs):
        return self.call('read_time', kwargs=kwargs)

    def write_time(self, **kwargs):
        return self.call('write_time', kwargs=kwargs)

    def process_value(self, **kwargs):
        return self.call('process_value', kwargs=kwargs)

    def output_level(self, **kwargs):
        return self.call('output_level', kwargs=kwargs)

    def target_setpoint(self, **kwargs):
        return self.call('target_setpoint', kwargs=kwargs)

    def target_setpoint(self, **kwargs):
        return self.call('target_setpoint', kwargs=kwargs)

    def operating_mode(self, **kwargs):
        return self.call('operating_mode', kwargs=kwargs)

    def operating_mode(self, **kwargs):
        return self.call('operating_mode', kwargs=kwargs)

    def working_setpoint(self, **kwargs):
        return self.call('working_setpoint', kwargs=kwargs)

    def current_program(self, **kwargs):
        return self.call('current_program', kwargs=kwargs)

    def current_program(self, **kwargs):
        return self.call('current_program', kwargs=kwargs)

    def program_status(self, **kwargs):
        return self.call('program_status', kwargs=kwargs)

    def program_status(self, **kwargs):
        return self.call('program_status', kwargs=kwargs)

    def programmer_setpoint(self, **kwargs):
        return self.call('programmer_setpoint', kwargs=kwargs)

    def programmer_cycles(self, **kwargs):
        return self.call('programmer_cycles', kwargs=kwargs)

    def current_segment_number(self, **kwargs):
        return self.call('current_segment_number', kwargs=kwargs)

    def current_segment_type(self, **kwargs):
        return self.call('current_segment_type', kwargs=kwargs)

    def segment_time_remaining(self, **kwargs):
        return self.call('segment_time_remaining', kwargs=kwargs)

