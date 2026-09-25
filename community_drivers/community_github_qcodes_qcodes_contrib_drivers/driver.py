from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubQcodesQcodesContribDrivers(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/QCoDeS_Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/OxfordInstruments/kelvinox.py', 'class_name': 'OxfordInstruments_Kelvinox_IGH', 'import_roots': [], 'candidate_methods': ['get_all', 'identify', 'remote', 'local', 'close', 'get_idn', 'set_mix_chamber_heater_mode', 'set_mix_chamber_heater_power_range', 'rotate_Nvalve'], 'metadata': {'repo': 'qcodes/qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'unit_id': 'gh_lake_shore_m81', 'source_file': 'src/qcodes_contrib_drivers/drivers/OxfordInstruments/kelvinox.py', 'candidate_score': 222, 'manufacturer': 'Lake Shore', 'model_name': 'Lake Shore M81'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def get_all(self, **kwargs):
        return self.call('get_all', kwargs=kwargs)

    def identify(self, **kwargs):
        return self.call('identify', kwargs=kwargs)

    def remote(self, **kwargs):
        return self.call('remote', kwargs=kwargs)

    def local(self, **kwargs):
        return self.call('local', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def set_mix_chamber_heater_mode(self, **kwargs):
        return self.call('set_mix_chamber_heater_mode', kwargs=kwargs)

    def set_mix_chamber_heater_power_range(self, **kwargs):
        return self.call('set_mix_chamber_heater_power_range', kwargs=kwargs)

    def rotate_Nvalve(self, **kwargs):
        return self.call('rotate_Nvalve', kwargs=kwargs)

