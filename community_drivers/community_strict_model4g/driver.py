from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictModel4g(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Cryomagnetics/Model_4G.py', 'class_name': 'Model_4G', 'import_roots': ['src'], 'candidate_methods': ['get_units', 'set_units', 'get_b', 'set_b', 'get_b_go', 'set_b_go', 'get_field', 'get_field_supply', 'get_sweep', 'set_sweep', 'get_hilim', 'set_hilim', 'get_lolim', 'set_lolim', 'get_rate_0', 'set_rate_0', 'get_rate_1', 'set_rate_1', 'get_rate_2', 'set_rate_2', 'get_rate_3', 'set_rate_3', 'get_rate_4', 'set_rate_4', 'get_persistance_heater', 'set_persistance_heater'], 'action_targets': {'get_units': '__qcodes_param_get__units', 'set_units': '__qcodes_param_set__units', 'get_b': '__qcodes_param_get__b', 'set_b': '__qcodes_param_set__b', 'get_b_go': '__qcodes_param_get__b_go', 'set_b_go': '__qcodes_param_set__b_go', 'get_field': '__qcodes_param_get__field', 'get_field_supply': '__qcodes_param_get__field_supply', 'get_sweep': '__qcodes_param_get__sweep', 'set_sweep': '__qcodes_param_set__sweep', 'get_hilim': '__qcodes_param_get__hilim', 'set_hilim': '__qcodes_param_set__hilim', 'get_lolim': '__qcodes_param_get__lolim', 'set_lolim': '__qcodes_param_set__lolim', 'get_rate_0': '__qcodes_param_get__rate_0', 'set_rate_0': '__qcodes_param_set__rate_0', 'get_rate_1': '__qcodes_param_get__rate_1', 'set_rate_1': '__qcodes_param_set__rate_1', 'get_rate_2': '__qcodes_param_get__rate_2', 'set_rate_2': '__qcodes_param_set__rate_2', 'get_rate_3': '__qcodes_param_get__rate_3', 'set_rate_3': '__qcodes_param_set__rate_3', 'get_rate_4': '__qcodes_param_get__rate_4', 'set_rate_4': '__qcodes_param_set__rate_4', 'get_persistance_heater': '__qcodes_param_get__persistance_heater', 'set_persistance_heater': '__qcodes_param_set__persistance_heater'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Cryomagnetics/Model_4G.py', 'confidence': 0.8, 'quality_score': 0.88, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_units': '__qcodes_param_get__units', 'set_units': '__qcodes_param_set__units', 'get_b': '__qcodes_param_get__b', 'set_b': '__qcodes_param_set__b', 'get_b_go': '__qcodes_param_get__b_go', 'set_b_go': '__qcodes_param_set__b_go', 'get_field': '__qcodes_param_get__field', 'get_field_supply': '__qcodes_param_get__field_supply', 'get_sweep': '__qcodes_param_get__sweep', 'set_sweep': '__qcodes_param_set__sweep', 'get_hilim': '__qcodes_param_get__hilim', 'set_hilim': '__qcodes_param_set__hilim', 'get_lolim': '__qcodes_param_get__lolim', 'set_lolim': '__qcodes_param_set__lolim', 'get_rate_0': '__qcodes_param_get__rate_0', 'set_rate_0': '__qcodes_param_set__rate_0', 'get_rate_1': '__qcodes_param_get__rate_1', 'set_rate_1': '__qcodes_param_set__rate_1', 'get_rate_2': '__qcodes_param_get__rate_2', 'set_rate_2': '__qcodes_param_set__rate_2', 'get_rate_3': '__qcodes_param_get__rate_3', 'set_rate_3': '__qcodes_param_set__rate_3', 'get_rate_4': '__qcodes_param_get__rate_4', 'set_rate_4': '__qcodes_param_set__rate_4', 'get_persistance_heater': '__qcodes_param_get__persistance_heater', 'set_persistance_heater': '__qcodes_param_set__persistance_heater'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_units(self, **kwargs):
        return self.call('get_units', kwargs=kwargs)

    def set_units(self, **kwargs):
        return self.call('set_units', kwargs=kwargs)

    def get_b(self, **kwargs):
        return self.call('get_b', kwargs=kwargs)

    def set_b(self, **kwargs):
        return self.call('set_b', kwargs=kwargs)

    def get_b_go(self, **kwargs):
        return self.call('get_b_go', kwargs=kwargs)

    def set_b_go(self, **kwargs):
        return self.call('set_b_go', kwargs=kwargs)

    def get_field(self, **kwargs):
        return self.call('get_field', kwargs=kwargs)

    def get_field_supply(self, **kwargs):
        return self.call('get_field_supply', kwargs=kwargs)

    def get_sweep(self, **kwargs):
        return self.call('get_sweep', kwargs=kwargs)

    def set_sweep(self, **kwargs):
        return self.call('set_sweep', kwargs=kwargs)

    def get_hilim(self, **kwargs):
        return self.call('get_hilim', kwargs=kwargs)

    def set_hilim(self, **kwargs):
        return self.call('set_hilim', kwargs=kwargs)

    def get_lolim(self, **kwargs):
        return self.call('get_lolim', kwargs=kwargs)

    def set_lolim(self, **kwargs):
        return self.call('set_lolim', kwargs=kwargs)

    def get_rate_0(self, **kwargs):
        return self.call('get_rate_0', kwargs=kwargs)

    def set_rate_0(self, **kwargs):
        return self.call('set_rate_0', kwargs=kwargs)

    def get_rate_1(self, **kwargs):
        return self.call('get_rate_1', kwargs=kwargs)

    def set_rate_1(self, **kwargs):
        return self.call('set_rate_1', kwargs=kwargs)

    def get_rate_2(self, **kwargs):
        return self.call('get_rate_2', kwargs=kwargs)

    def set_rate_2(self, **kwargs):
        return self.call('set_rate_2', kwargs=kwargs)

    def get_rate_3(self, **kwargs):
        return self.call('get_rate_3', kwargs=kwargs)

    def set_rate_3(self, **kwargs):
        return self.call('set_rate_3', kwargs=kwargs)

    def get_rate_4(self, **kwargs):
        return self.call('get_rate_4', kwargs=kwargs)

    def set_rate_4(self, **kwargs):
        return self.call('set_rate_4', kwargs=kwargs)

    def get_persistance_heater(self, **kwargs):
        return self.call('get_persistance_heater', kwargs=kwargs)

    def set_persistance_heater(self, **kwargs):
        return self.call('set_persistance_heater', kwargs=kwargs)

