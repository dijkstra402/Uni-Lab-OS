from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPyhysMinimalmodbus(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pyhys_minimalmodbus', 'source_file': 'minimalmodbus.py', 'class_name': 'Instrument', 'import_roots': [], 'candidate_methods': ['roundtrip_time', 'read_bit', 'write_bit', 'read_bits', 'write_bits', 'read_register', 'write_register', 'read_long', 'write_long', 'read_float', 'write_float', 'read_string', 'write_string', 'read_registers', 'write_registers'], 'metadata': {'repo': 'pyhys/minimalmodbus', 'repo_url': 'https://github.com/pyhys/minimalmodbus', 'unit_id': 'gh_eurotherm_3500', 'source_file': 'minimalmodbus.py', 'candidate_score': 125, 'manufacturer': 'Eurotherm', 'model_name': 'Eurotherm 3500/3504'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def roundtrip_time(self, **kwargs):
        return self.call('roundtrip_time', kwargs=kwargs)

    def read_bit(self, **kwargs):
        return self.call('read_bit', kwargs=kwargs)

    def write_bit(self, **kwargs):
        return self.call('write_bit', kwargs=kwargs)

    def read_bits(self, **kwargs):
        return self.call('read_bits', kwargs=kwargs)

    def write_bits(self, **kwargs):
        return self.call('write_bits', kwargs=kwargs)

    def read_register(self, **kwargs):
        return self.call('read_register', kwargs=kwargs)

    def write_register(self, **kwargs):
        return self.call('write_register', kwargs=kwargs)

    def read_long(self, **kwargs):
        return self.call('read_long', kwargs=kwargs)

    def write_long(self, **kwargs):
        return self.call('write_long', kwargs=kwargs)

    def read_float(self, **kwargs):
        return self.call('read_float', kwargs=kwargs)

    def write_float(self, **kwargs):
        return self.call('write_float', kwargs=kwargs)

    def read_string(self, **kwargs):
        return self.call('read_string', kwargs=kwargs)

    def write_string(self, **kwargs):
        return self.call('write_string', kwargs=kwargs)

    def read_registers(self, **kwargs):
        return self.call('read_registers', kwargs=kwargs)

    def write_registers(self, **kwargs):
        return self.call('write_registers', kwargs=kwargs)

