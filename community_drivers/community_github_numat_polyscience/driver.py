from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubNumatPolyscience(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/numat_polyscience', 'source_file': 'polyscience/udp.py', 'class_name': 'CirculatingBath', 'import_roots': [], 'candidate_methods': ['turn_on', 'turn_off', 'check_fault', 'get', 'get_setpoint', 'get_temperature_units', 'get_internal_temperature', 'get_external_temperature', 'get_operating_status', 'get_pump_speed', 'set_setpoint', 'set_pump_speed', 'close'], 'metadata': {'repo': 'numat/polyscience', 'repo_url': 'https://github.com/numat/polyscience', 'unit_id': 'gh_polyscience_4100', 'source_file': 'polyscience/udp.py', 'candidate_score': 109, 'manufacturer': 'PolyScience', 'model_name': 'PolyScience 4100'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def turn_on(self, **kwargs):
        return self.call('turn_on', kwargs=kwargs)

    def turn_off(self, **kwargs):
        return self.call('turn_off', kwargs=kwargs)

    def check_fault(self, **kwargs):
        return self.call('check_fault', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def get_setpoint(self, **kwargs):
        return self.call('get_setpoint', kwargs=kwargs)

    def get_temperature_units(self, **kwargs):
        return self.call('get_temperature_units', kwargs=kwargs)

    def get_internal_temperature(self, **kwargs):
        return self.call('get_internal_temperature', kwargs=kwargs)

    def get_external_temperature(self, **kwargs):
        return self.call('get_external_temperature', kwargs=kwargs)

    def get_operating_status(self, **kwargs):
        return self.call('get_operating_status', kwargs=kwargs)

    def get_pump_speed(self, **kwargs):
        return self.call('get_pump_speed', kwargs=kwargs)

    def set_setpoint(self, **kwargs):
        return self.call('set_setpoint', kwargs=kwargs)

    def set_pump_speed(self, **kwargs):
        return self.call('set_pump_speed', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

