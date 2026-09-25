from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubEspecnorthamericaChamberconnectlibrary(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/EspecNorthAmerica_ChamberConnectLibrary', 'source_file': 'chamberconnectlibrary/watlowf4.py', 'class_name': 'WatlowF4', 'import_roots': [], 'candidate_methods': ['connect', 'close', 'raw', 'get_datetime', 'set_datetime', 'get_refrig', 'set_refrig', 'get_loop_sp', 'set_loop_sp', 'get_loop_pv', 'get_loop_range', 'set_loop_range', 'get_loop_en', 'set_loop_en', 'get_loop_units', 'get_loop_mode', 'get_loop_modes', 'set_loop_mode', 'get_loop_power', 'set_loop_power'], 'metadata': {'repo': 'especnorthamerica/chamberconnectlibrary', 'repo_url': 'https://github.com/EspecNorthAmerica/ChamberConnectLibrary', 'unit_id': 'gh_espec_p300', 'source_file': 'chamberconnectlibrary/watlowf4.py', 'candidate_score': 44, 'manufacturer': 'Espec', 'model_name': 'Espec P300/SCP-220控制器'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def raw(self, **kwargs):
        return self.call('raw', kwargs=kwargs)

    def get_datetime(self, **kwargs):
        return self.call('get_datetime', kwargs=kwargs)

    def set_datetime(self, **kwargs):
        return self.call('set_datetime', kwargs=kwargs)

    def get_refrig(self, **kwargs):
        return self.call('get_refrig', kwargs=kwargs)

    def set_refrig(self, **kwargs):
        return self.call('set_refrig', kwargs=kwargs)

    def get_loop_sp(self, **kwargs):
        return self.call('get_loop_sp', kwargs=kwargs)

    def set_loop_sp(self, **kwargs):
        return self.call('set_loop_sp', kwargs=kwargs)

    def get_loop_pv(self, **kwargs):
        return self.call('get_loop_pv', kwargs=kwargs)

    def get_loop_range(self, **kwargs):
        return self.call('get_loop_range', kwargs=kwargs)

    def set_loop_range(self, **kwargs):
        return self.call('set_loop_range', kwargs=kwargs)

    def get_loop_en(self, **kwargs):
        return self.call('get_loop_en', kwargs=kwargs)

    def set_loop_en(self, **kwargs):
        return self.call('set_loop_en', kwargs=kwargs)

    def get_loop_units(self, **kwargs):
        return self.call('get_loop_units', kwargs=kwargs)

    def get_loop_mode(self, **kwargs):
        return self.call('get_loop_mode', kwargs=kwargs)

    def get_loop_modes(self, **kwargs):
        return self.call('get_loop_modes', kwargs=kwargs)

    def set_loop_mode(self, **kwargs):
        return self.call('set_loop_mode', kwargs=kwargs)

    def get_loop_power(self, **kwargs):
        return self.call('get_loop_power', kwargs=kwargs)

    def set_loop_power(self, **kwargs):
        return self.call('set_loop_power', kwargs=kwargs)

