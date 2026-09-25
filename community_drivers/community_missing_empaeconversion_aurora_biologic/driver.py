from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingEmpaeconversionAuroraBiologic(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/EmpaEconversion__aurora-biologic', 'source_file': 'aurora_biologic/biologic.py', 'class_name': 'BiologicAPI', 'import_roots': [], 'candidate_methods': ['get_pipelines', 'get_status', 'load_settings', 'run_channel', 'start', 'stop', 'get_experiment_info', 'get_job_id'], 'metadata': {'repo': 'EmpaEconversion/aurora-biologic', 'repo_url': 'https://github.com/EmpaEconversion/aurora-biologic', 'review_status': 'good', 'review_notes': ['业务方法干净，可直接使用。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_pipelines(self, **kwargs):
        return self.call('get_pipelines', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def load_settings(self, **kwargs):
        return self.call('load_settings', kwargs=kwargs)

    def run_channel(self, **kwargs):
        return self.call('run_channel', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def get_experiment_info(self, **kwargs):
        return self.call('get_experiment_info', kwargs=kwargs)

    def get_job_id(self, **kwargs):
        return self.call('get_job_id', kwargs=kwargs)

