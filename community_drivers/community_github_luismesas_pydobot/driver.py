from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubLuismesasPydobot(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/luismesas_pydobot', 'source_file': 'pydobot/dobot.py', 'class_name': 'Dobot', 'import_roots': [], 'candidate_methods': ['get_eio', 'set_eio', 'close', 'go', 'move_to', 'suck', 'grip', 'speed', 'wait', 'pose'], 'metadata': {'repo': 'luismesas/pydobot', 'repo_url': 'https://github.com/luismesas/pydobot', 'unit_id': 'gh_dobot_magician', 'source_file': 'pydobot/dobot.py', 'candidate_score': 95, 'manufacturer': 'Dobot', 'model_name': 'Dobot Magician'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def get_eio(self, **kwargs):
        return self.call('get_eio', kwargs=kwargs)

    def set_eio(self, **kwargs):
        return self.call('set_eio', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def go(self, **kwargs):
        return self.call('go', kwargs=kwargs)

    def move_to(self, **kwargs):
        return self.call('move_to', kwargs=kwargs)

    def suck(self, **kwargs):
        return self.call('suck', kwargs=kwargs)

    def grip(self, **kwargs):
        return self.call('grip', kwargs=kwargs)

    def speed(self, **kwargs):
        return self.call('speed', kwargs=kwargs)

    def wait(self, **kwargs):
        return self.call('wait', kwargs=kwargs)

    def pose(self, **kwargs):
        return self.call('pose', kwargs=kwargs)

