from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubIorodeoPotentiostat(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/iorodeo_potentiostat', 'source_file': 'software/python/potentiostat/potentiostat/potentiostat.py', 'class_name': 'Potentiostat', 'import_roots': [], 'candidate_methods': ['get_hardware_variant', 'stop_test', 'get_volt', 'set_volt', 'get_curr', 'get_ref_volt', 'get_param', 'set_param', 'set_volt_range', 'get_volt_range', 'get_all_volt_range', 'set_curr_range', 'get_curr_range', 'get_all_curr_range', 'get_device_id', 'set_device_id', 'set_sample_period', 'get_sample_period', 'set_sample_rate', 'get_sample_rate'], 'metadata': {'repo': 'iorodeo/potentiostat', 'repo_url': 'https://github.com/iorodeo/potentiostat', 'unit_id': 'gh_iorodeo_rodeostat', 'source_file': 'software/python/potentiostat/potentiostat/potentiostat.py', 'candidate_score': 140, 'manufacturer': 'IoRodeo', 'model_name': 'IoRodeo Rodeostat'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def get_hardware_variant(self, **kwargs):
        return self.call('get_hardware_variant', kwargs=kwargs)

    def stop_test(self, **kwargs):
        return self.call('stop_test', kwargs=kwargs)

    def get_volt(self, **kwargs):
        return self.call('get_volt', kwargs=kwargs)

    def set_volt(self, **kwargs):
        return self.call('set_volt', kwargs=kwargs)

    def get_curr(self, **kwargs):
        return self.call('get_curr', kwargs=kwargs)

    def get_ref_volt(self, **kwargs):
        return self.call('get_ref_volt', kwargs=kwargs)

    def get_param(self, **kwargs):
        return self.call('get_param', kwargs=kwargs)

    def set_param(self, **kwargs):
        return self.call('set_param', kwargs=kwargs)

    def set_volt_range(self, **kwargs):
        return self.call('set_volt_range', kwargs=kwargs)

    def get_volt_range(self, **kwargs):
        return self.call('get_volt_range', kwargs=kwargs)

    def get_all_volt_range(self, **kwargs):
        return self.call('get_all_volt_range', kwargs=kwargs)

    def set_curr_range(self, **kwargs):
        return self.call('set_curr_range', kwargs=kwargs)

    def get_curr_range(self, **kwargs):
        return self.call('get_curr_range', kwargs=kwargs)

    def get_all_curr_range(self, **kwargs):
        return self.call('get_all_curr_range', kwargs=kwargs)

    def get_device_id(self, **kwargs):
        return self.call('get_device_id', kwargs=kwargs)

    def set_device_id(self, **kwargs):
        return self.call('set_device_id', kwargs=kwargs)

    def set_sample_period(self, **kwargs):
        return self.call('set_sample_period', kwargs=kwargs)

    def get_sample_period(self, **kwargs):
        return self.call('get_sample_period', kwargs=kwargs)

    def set_sample_rate(self, **kwargs):
        return self.call('set_sample_rate', kwargs=kwargs)

    def get_sample_rate(self, **kwargs):
        return self.call('get_sample_rate', kwargs=kwargs)

