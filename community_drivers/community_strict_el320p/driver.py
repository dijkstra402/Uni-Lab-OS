from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictEl320p(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/AimTTi/EL320P.py', 'class_name': 'EL320P', 'import_roots': ['src'], 'candidate_methods': ['get_voltage_set', 'set_voltage_set', 'get_voltage_out', 'get_current_set', 'set_current_set', 'get_current_out', 'get_mode', 'get_output', 'set_output', 'get_error'], 'action_targets': {'get_voltage_set': '__qcodes_param_get__voltage_set', 'set_voltage_set': '__qcodes_param_set__voltage_set', 'get_voltage_out': '__qcodes_param_get__voltage_out', 'get_current_set': '__qcodes_param_get__current_set', 'set_current_set': '__qcodes_param_set__current_set', 'get_current_out': '__qcodes_param_get__current_out', 'get_mode': '__qcodes_param_get__mode', 'get_output': '__qcodes_param_get__output', 'set_output': '__qcodes_param_set__output', 'get_error': '__qcodes_param_get__error'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/AimTTi/EL320P.py', 'confidence': 0.8, 'quality_score': 0.88, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_voltage_set': '__qcodes_param_get__voltage_set', 'set_voltage_set': '__qcodes_param_set__voltage_set', 'get_voltage_out': '__qcodes_param_get__voltage_out', 'get_current_set': '__qcodes_param_get__current_set', 'set_current_set': '__qcodes_param_set__current_set', 'get_current_out': '__qcodes_param_get__current_out', 'get_mode': '__qcodes_param_get__mode', 'get_output': '__qcodes_param_get__output', 'set_output': '__qcodes_param_set__output', 'get_error': '__qcodes_param_get__error'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_voltage_set(self, **kwargs):
        return self.call('get_voltage_set', kwargs=kwargs)

    def set_voltage_set(self, **kwargs):
        return self.call('set_voltage_set', kwargs=kwargs)

    def get_voltage_out(self, **kwargs):
        return self.call('get_voltage_out', kwargs=kwargs)

    def get_current_set(self, **kwargs):
        return self.call('get_current_set', kwargs=kwargs)

    def set_current_set(self, **kwargs):
        return self.call('set_current_set', kwargs=kwargs)

    def get_current_out(self, **kwargs):
        return self.call('get_current_out', kwargs=kwargs)

    def get_mode(self, **kwargs):
        return self.call('get_mode', kwargs=kwargs)

    def get_output(self, **kwargs):
        return self.call('get_output', kwargs=kwargs)

    def set_output(self, **kwargs):
        return self.call('set_output', kwargs=kwargs)

    def get_error(self, **kwargs):
        return self.call('get_error', kwargs=kwargs)

