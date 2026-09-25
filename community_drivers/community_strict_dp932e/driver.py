from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictDp932e(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Rigol/Rigol_DP932.py', 'class_name': 'RigolDP932E', 'import_roots': ['src'], 'candidate_methods': ['reset', 'enable_output', 'disable_output', 'measure_voltage', 'measure_current', 'set_voltage', 'set_current', 'set_output_state', 'measure_power'], 'action_targets': {}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Rigol/Rigol_DP932.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def enable_output(self, **kwargs):
        return self.call('enable_output', kwargs=kwargs)

    def disable_output(self, **kwargs):
        return self.call('disable_output', kwargs=kwargs)

    def measure_voltage(self, **kwargs):
        return self.call('measure_voltage', kwargs=kwargs)

    def measure_current(self, **kwargs):
        return self.call('measure_current', kwargs=kwargs)

    def set_voltage(self, **kwargs):
        return self.call('set_voltage', kwargs=kwargs)

    def set_current(self, **kwargs):
        return self.call('set_current', kwargs=kwargs)

    def set_output_state(self, **kwargs):
        return self.call('set_output_state', kwargs=kwargs)

    def measure_power(self, **kwargs):
        return self.call('measure_power', kwargs=kwargs)

