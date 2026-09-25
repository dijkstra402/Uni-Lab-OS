from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubAutonomousChemistryLabQuantos(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/autonomous-chemistry-lab_quantos', 'source_file': 'mettler_toledo_quantos/mettler_toledo_quantos.py', 'class_name': 'MettlerToledoDevice', 'import_roots': [], 'candidate_methods': ['close', 'move_frontdoor_open', 'move_frontdoor_close', 'move_to', 'unlock_dosing_pin', 'lock_dosing_pin', 'set_target_value_mg', 'set_tolerance_value_pct', 'start_dosing', 'request_frontdoor_position', 'request_autosampler_position', 'quantos_test'], 'metadata': {'repo': 'autonomous-chemistry-lab/quantos', 'repo_url': 'https://github.com/autonomous-chemistry-lab/quantos', 'unit_id': 'gh_mettler_toledo_quantos', 'source_file': 'mettler_toledo_quantos/mettler_toledo_quantos.py', 'candidate_score': 96, 'manufacturer': 'Mettler Toledo', 'model_name': 'Mettler Toledo Quantos'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def move_frontdoor_open(self, **kwargs):
        return self.call('move_frontdoor_open', kwargs=kwargs)

    def move_frontdoor_close(self, **kwargs):
        return self.call('move_frontdoor_close', kwargs=kwargs)

    def move_to(self, **kwargs):
        return self.call('move_to', kwargs=kwargs)

    def unlock_dosing_pin(self, **kwargs):
        return self.call('unlock_dosing_pin', kwargs=kwargs)

    def lock_dosing_pin(self, **kwargs):
        return self.call('lock_dosing_pin', kwargs=kwargs)

    def set_target_value_mg(self, **kwargs):
        return self.call('set_target_value_mg', kwargs=kwargs)

    def set_tolerance_value_pct(self, **kwargs):
        return self.call('set_tolerance_value_pct', kwargs=kwargs)

    def start_dosing(self, **kwargs):
        return self.call('start_dosing', kwargs=kwargs)

    def request_frontdoor_position(self, **kwargs):
        return self.call('request_frontdoor_position', kwargs=kwargs)

    def request_autosampler_position(self, **kwargs):
        return self.call('request_autosampler_position', kwargs=kwargs)

    def quantos_test(self, **kwargs):
        return self.call('quantos_test', kwargs=kwargs)

