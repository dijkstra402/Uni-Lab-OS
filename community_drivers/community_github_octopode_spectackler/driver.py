from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubOctopodeSpectackler(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/octopode_spectackler', 'source_file': 'rf5301.py', 'class_name': 'RF5301', 'import_roots': [], 'candidate_methods': ['disconnect', 'post', 'ser_num', 'rom_ver', 'mem_chk', 'opt_chk', 'xen_hrs', 'shutter', 'zero', 'slit_ex', 'slit_em', 'wl_ex', 'wl_em', 'wl_set_nadh', 'wl_set_dph', 'wl_set_340_440', 'wl_set_340_490', 'wl_set_410_440', 'wl_set_410_490', 'fluor_get'], 'metadata': {'repo': 'octopode/spectackler', 'repo_url': 'https://github.com/octopode/spectackler', 'unit_id': 'gh_teledyne_isco_260d', 'source_file': 'rf5301.py', 'candidate_score': 117, 'manufacturer': 'Teledyne Isco', 'model_name': 'Teledyne Isco 260D'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def post(self, **kwargs):
        return self.call('post', kwargs=kwargs)

    def ser_num(self, **kwargs):
        return self.call('ser_num', kwargs=kwargs)

    def rom_ver(self, **kwargs):
        return self.call('rom_ver', kwargs=kwargs)

    def mem_chk(self, **kwargs):
        return self.call('mem_chk', kwargs=kwargs)

    def opt_chk(self, **kwargs):
        return self.call('opt_chk', kwargs=kwargs)

    def xen_hrs(self, **kwargs):
        return self.call('xen_hrs', kwargs=kwargs)

    def shutter(self, **kwargs):
        return self.call('shutter', kwargs=kwargs)

    def zero(self, **kwargs):
        return self.call('zero', kwargs=kwargs)

    def slit_ex(self, **kwargs):
        return self.call('slit_ex', kwargs=kwargs)

    def slit_em(self, **kwargs):
        return self.call('slit_em', kwargs=kwargs)

    def wl_ex(self, **kwargs):
        return self.call('wl_ex', kwargs=kwargs)

    def wl_em(self, **kwargs):
        return self.call('wl_em', kwargs=kwargs)

    def wl_set_nadh(self, **kwargs):
        return self.call('wl_set_nadh', kwargs=kwargs)

    def wl_set_dph(self, **kwargs):
        return self.call('wl_set_dph', kwargs=kwargs)

    def wl_set_340_440(self, **kwargs):
        return self.call('wl_set_340_440', kwargs=kwargs)

    def wl_set_340_490(self, **kwargs):
        return self.call('wl_set_340_490', kwargs=kwargs)

    def wl_set_410_440(self, **kwargs):
        return self.call('wl_set_410_440', kwargs=kwargs)

    def wl_set_410_490(self, **kwargs):
        return self.call('wl_set_410_490', kwargs=kwargs)

    def fluor_get(self, **kwargs):
        return self.call('fluor_get', kwargs=kwargs)

