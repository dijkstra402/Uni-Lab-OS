from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAustraliansynchrotronAspyrobot(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/AustralianSynchrotron_aspyrobot', 'source_file': 'aspyrobot/robot.py', 'class_name': 'Robot', 'import_roots': [], 'candidate_methods': ['snapshot', 'run_task', 'run_background_task'], 'metadata': {'repo': 'australiansynchrotron/aspyrobot', 'repo_url': 'https://github.com/AustralianSynchrotron/aspyrobot', 'unit_id': 'gh_epson_scara_rc90', 'source_file': 'aspyrobot/robot.py', 'candidate_score': 43, 'manufacturer': 'Epson', 'model_name': 'Epson SCARA (RC90/RC700)'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def snapshot(self, **kwargs):
        return self.call('snapshot', kwargs=kwargs)

    def run_task(self, **kwargs):
        return self.call('run_task', kwargs=kwargs)

    def run_background_task(self, **kwargs):
        return self.call('run_background_task', kwargs=kwargs)

