from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPharmbioRobotlab(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pharmbio_robotlab', 'source_file': 'labrobots/labrobots/imx.py', 'class_name': 'IMX', 'import_roots': [], 'candidate_methods': ['send_raw', 'send', 'online', 'status', 'goto', 'goto_loading', 'leave_loading', 'acquire'], 'metadata': {'repo': 'pharmbio/robotlab', 'repo_url': 'https://github.com/pharmbio/robotlab', 'unit_id': 'gh_biotek_el406', 'source_file': 'labrobots/labrobots/imx.py', 'candidate_score': 99, 'manufacturer': 'BioTek', 'model_name': 'BioTek EL406'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def send_raw(self, **kwargs):
        return self.call('send_raw', kwargs=kwargs)

    def send(self, **kwargs):
        return self.call('send', kwargs=kwargs)

    def online(self, **kwargs):
        return self.call('online', kwargs=kwargs)

    def status(self, **kwargs):
        return self.call('status', kwargs=kwargs)

    def goto(self, **kwargs):
        return self.call('goto', kwargs=kwargs)

    def goto_loading(self, **kwargs):
        return self.call('goto_loading', kwargs=kwargs)

    def leave_loading(self, **kwargs):
        return self.call('leave_loading', kwargs=kwargs)

    def acquire(self, **kwargs):
        return self.call('acquire', kwargs=kwargs)

