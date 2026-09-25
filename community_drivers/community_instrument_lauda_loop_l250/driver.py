from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLaudaLoopL250(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/turbocasino__LOOP-L250-Chiller', 'source_file': 'chiller.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['write_cmd', 'check_dec', 'power', 'temperature', 'read_cmd', 'read_set_temp', 'read_inside_temp', 'read_set_temp_hi', 'read_set_temp_lo', 'naming', 'logging', 'sampling'], 'action_targets': {'write_cmd': 'write_cmd', 'check_dec': 'check_dec', 'power': 'power', 'temperature': 'temperature', 'read_cmd': 'read_cmd', 'read_set_temp': 'read_set_temp', 'read_inside_temp': 'read_inside_temp', 'read_set_temp_hi': 'read_set_temp_hi', 'read_set_temp_lo': 'read_set_temp_lo', 'naming': 'naming', 'logging': 'logging', 'sampling': 'sampling'}, 'metadata': {'repo': 'turbocasino/LOOP-L250-Chiller', 'repo_url': 'https://github.com/turbocasino/LOOP-L250-Chiller', 'brand': 'Lauda', 'model': 'LOOP L250', 'device_type_cn': '冷热水机', 'device_type_en': 'Chiller / Heater Unit', 'source_framework': '专用驱动', 'tag_id': '4369', 'tag_name': '冷热水机', 'tag_name_en': 'Chiller / Heater Unit', 'candidate_score': 104, 'parse_status': 'module_selected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'write_cmd': 'write_cmd', 'check_dec': 'check_dec', 'power': 'power', 'temperature': 'temperature', 'read_cmd': 'read_cmd', 'read_set_temp': 'read_set_temp', 'read_inside_temp': 'read_inside_temp', 'read_set_temp_hi': 'read_set_temp_hi', 'read_set_temp_lo': 'read_set_temp_lo', 'naming': 'naming', 'logging': 'logging', 'sampling': 'sampling'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def write_cmd(self, **kwargs):
        return self.call('write_cmd', kwargs=kwargs)

    def check_dec(self, **kwargs):
        return self.call('check_dec', kwargs=kwargs)

    def power(self, **kwargs):
        return self.call('power', kwargs=kwargs)

    def temperature(self, **kwargs):
        return self.call('temperature', kwargs=kwargs)

    def read_cmd(self, **kwargs):
        return self.call('read_cmd', kwargs=kwargs)

    def read_set_temp(self, **kwargs):
        return self.call('read_set_temp', kwargs=kwargs)

    def read_inside_temp(self, **kwargs):
        return self.call('read_inside_temp', kwargs=kwargs)

    def read_set_temp_hi(self, **kwargs):
        return self.call('read_set_temp_hi', kwargs=kwargs)

    def read_set_temp_lo(self, **kwargs):
        return self.call('read_set_temp_lo', kwargs=kwargs)

    def naming(self, **kwargs):
        return self.call('naming', kwargs=kwargs)

    def logging(self, **kwargs):
        return self.call('logging', kwargs=kwargs)

    def sampling(self, **kwargs):
        return self.call('sampling', kwargs=kwargs)

