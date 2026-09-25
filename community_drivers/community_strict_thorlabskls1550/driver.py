from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictThorlabskls1550(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Thorlabs/KLS1550.py', 'class_name': 'Thorlabs_KLS1550', 'import_roots': ['src'], 'candidate_methods': ['identify', 'get_idn', 'enable_output', 'disable_output', 'close', 'get_output_enabled', 'set_output_enabled', 'get_power', 'set_power', 'enable_simulation', 'disable_simulation'], 'action_targets': {'get_output_enabled': '__qcodes_param_get__output_enabled', 'set_output_enabled': '__qcodes_param_set__output_enabled', 'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Thorlabs/KLS1550.py', 'confidence': 0.9, 'quality_score': 1.06, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_output_enabled': '__qcodes_param_get__output_enabled', 'set_output_enabled': '__qcodes_param_set__output_enabled', 'get_power': '__qcodes_param_get__power', 'set_power': '__qcodes_param_set__power'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def identify(self, **kwargs):
        return self.call('identify', kwargs=kwargs)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def enable_output(self, **kwargs):
        return self.call('enable_output', kwargs=kwargs)

    def disable_output(self, **kwargs):
        return self.call('disable_output', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def get_output_enabled(self, **kwargs):
        return self.call('get_output_enabled', kwargs=kwargs)

    def set_output_enabled(self, **kwargs):
        return self.call('set_output_enabled', kwargs=kwargs)

    def get_power(self, **kwargs):
        return self.call('get_power', kwargs=kwargs)

    def set_power(self, **kwargs):
        return self.call('set_power', kwargs=kwargs)

    def enable_simulation(self, **kwargs):
        return self.call('enable_simulation', kwargs=kwargs)

    def disable_simulation(self, **kwargs):
        return self.call('disable_simulation', kwargs=kwargs)

