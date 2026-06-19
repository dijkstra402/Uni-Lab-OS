from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubMcimechBk891(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/mcimech_bk891', 'source_file': 'bkp891/scpi891.py', 'class_name': 'ScpiConnection', 'import_roots': [], 'candidate_methods': ['close', 'sendcmd', 'calibrate', 'get_calibrate', 'set_displayfont', 'get_displayfont', 'set_displaymode', 'get_displaymode', 'set_displaypage', 'get_displaypage', 'fetch', 'set_format', 'get_format', 'set_frequency', 'get_frequency', 'set_aclevel', 'get_aclevel', 'set_function', 'get_function', 'set_speed'], 'metadata': {'repo': 'mcimech/bk891', 'repo_url': 'https://github.com/mcimech/bk891', 'unit_id': 'gh_bk_precision_891', 'source_file': 'bkp891/scpi891.py', 'candidate_score': 109, 'manufacturer': 'BK Precision', 'model_name': 'BK Precision 891'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def sendcmd(self, **kwargs):
        return self.call('sendcmd', kwargs=kwargs)

    def calibrate(self, **kwargs):
        return self.call('calibrate', kwargs=kwargs)

    def get_calibrate(self, **kwargs):
        return self.call('get_calibrate', kwargs=kwargs)

    def set_displayfont(self, **kwargs):
        return self.call('set_displayfont', kwargs=kwargs)

    def get_displayfont(self, **kwargs):
        return self.call('get_displayfont', kwargs=kwargs)

    def set_displaymode(self, **kwargs):
        return self.call('set_displaymode', kwargs=kwargs)

    def get_displaymode(self, **kwargs):
        return self.call('get_displaymode', kwargs=kwargs)

    def set_displaypage(self, **kwargs):
        return self.call('set_displaypage', kwargs=kwargs)

    def get_displaypage(self, **kwargs):
        return self.call('get_displaypage', kwargs=kwargs)

    def fetch(self, **kwargs):
        return self.call('fetch', kwargs=kwargs)

    def set_format(self, **kwargs):
        return self.call('set_format', kwargs=kwargs)

    def get_format(self, **kwargs):
        return self.call('get_format', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def set_aclevel(self, **kwargs):
        return self.call('set_aclevel', kwargs=kwargs)

    def get_aclevel(self, **kwargs):
        return self.call('get_aclevel', kwargs=kwargs)

    def set_function(self, **kwargs):
        return self.call('set_function', kwargs=kwargs)

    def get_function(self, **kwargs):
        return self.call('get_function', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

