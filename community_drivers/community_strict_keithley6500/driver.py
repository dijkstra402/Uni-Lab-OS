from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictKeithley6500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Tektronix/Keithley_6500.py', 'class_name': 'Keithley_6500', 'import_roots': ['src'], 'candidate_methods': ['get_active_terminal', 'get_resistance', 'get_resistance_4w', 'get_voltage_dc', 'get_current_dc', 'get_temperature'], 'action_targets': {'get_active_terminal': '__qcodes_param_get__active_terminal', 'get_resistance': '__qcodes_param_get__resistance', 'get_resistance_4w': '__qcodes_param_get__resistance_4w', 'get_voltage_dc': '__qcodes_param_get__voltage_dc', 'get_current_dc': '__qcodes_param_get__current_dc', 'get_temperature': '__qcodes_param_get__temperature'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Tektronix/Keithley_6500.py', 'confidence': 0.9, 'quality_score': 1.06, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_active_terminal': '__qcodes_param_get__active_terminal', 'get_resistance': '__qcodes_param_get__resistance', 'get_resistance_4w': '__qcodes_param_get__resistance_4w', 'get_voltage_dc': '__qcodes_param_get__voltage_dc', 'get_current_dc': '__qcodes_param_get__current_dc', 'get_temperature': '__qcodes_param_get__temperature'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_active_terminal(self, **kwargs):
        return self.call('get_active_terminal', kwargs=kwargs)

    def get_resistance(self, **kwargs):
        return self.call('get_resistance', kwargs=kwargs)

    def get_resistance_4w(self, **kwargs):
        return self.call('get_resistance_4w', kwargs=kwargs)

    def get_voltage_dc(self, **kwargs):
        return self.call('get_voltage_dc', kwargs=kwargs)

    def get_current_dc(self, **kwargs):
        return self.call('get_current_dc', kwargs=kwargs)

    def get_temperature(self, **kwargs):
        return self.call('get_temperature', kwargs=kwargs)

