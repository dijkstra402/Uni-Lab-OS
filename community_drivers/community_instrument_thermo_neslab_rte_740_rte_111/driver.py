from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThermoNeslabRte740Rte111(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/octopode__bathtime', 'source_file': 'neslabrte.py', 'class_name': 'NeslabController', 'import_roots': [], 'candidate_methods': ['query', 'disconnect', 'status_set', 'status_get', 'on', 'probe_ext', 'temp_set', 'fault_lo', 'fault_hi', 'pid', 'temp_get_int', 'temp_get_ext', 'temp_get_act', 'ref2act', 'act2ref'], 'action_targets': {}, 'metadata': {'repo': 'octopode/bathtime', 'repo_url': 'https://github.com/octopode/bathtime', 'brand': 'Thermo NESLAB', 'model': 'RTE-740/RTE-111', 'device_type_cn': '冷热水机', 'device_type_en': 'Chiller / Heater Unit', 'source_framework': '专用驱动', 'tag_id': '4369', 'tag_name': '冷热水机', 'tag_name_en': 'Chiller / Heater Unit', 'candidate_score': 170, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def status_set(self, **kwargs):
        return self.call('status_set', kwargs=kwargs)

    def status_get(self, **kwargs):
        return self.call('status_get', kwargs=kwargs)

    def on(self, **kwargs):
        return self.call('on', kwargs=kwargs)

    def probe_ext(self, **kwargs):
        return self.call('probe_ext', kwargs=kwargs)

    def temp_set(self, **kwargs):
        return self.call('temp_set', kwargs=kwargs)

    def fault_lo(self, **kwargs):
        return self.call('fault_lo', kwargs=kwargs)

    def fault_hi(self, **kwargs):
        return self.call('fault_hi', kwargs=kwargs)

    def pid(self, **kwargs):
        return self.call('pid', kwargs=kwargs)

    def temp_get_int(self, **kwargs):
        return self.call('temp_get_int', kwargs=kwargs)

    def temp_get_ext(self, **kwargs):
        return self.call('temp_get_ext', kwargs=kwargs)

    def temp_get_act(self, **kwargs):
        return self.call('temp_get_act', kwargs=kwargs)

    def ref2act(self, **kwargs):
        return self.call('ref2act', kwargs=kwargs)

    def act2ref(self, **kwargs):
        return self.call('act2ref', kwargs=kwargs)

