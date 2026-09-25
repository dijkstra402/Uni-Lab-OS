from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictSim928(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/StanfordResearchSystems/SIM928.py', 'class_name': 'SIM928', 'import_roots': ['src'], 'candidate_methods': ['get_module_idn', 'find_modules', 'ask_module', 'write_module', 'set_voltage', 'get_voltage', 'set_smooth', 'get_module_status', 'reset_module', 'check_module_errors', 'byte_to_bits'], 'action_targets': {}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/StanfordResearchSystems/SIM928.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_module_idn(self, **kwargs):
        return self.call('get_module_idn', kwargs=kwargs)

    def find_modules(self, **kwargs):
        return self.call('find_modules', kwargs=kwargs)

    def ask_module(self, **kwargs):
        return self.call('ask_module', kwargs=kwargs)

    def write_module(self, **kwargs):
        return self.call('write_module', kwargs=kwargs)

    def set_voltage(self, **kwargs):
        return self.call('set_voltage', kwargs=kwargs)

    def get_voltage(self, **kwargs):
        return self.call('get_voltage', kwargs=kwargs)

    def set_smooth(self, **kwargs):
        return self.call('set_smooth', kwargs=kwargs)

    def get_module_status(self, **kwargs):
        return self.call('get_module_status', kwargs=kwargs)

    def reset_module(self, **kwargs):
        return self.call('reset_module', kwargs=kwargs)

    def check_module_errors(self, **kwargs):
        return self.call('check_module_errors', kwargs=kwargs)

    def byte_to_bits(self, **kwargs):
        return self.call('byte_to_bits', kwargs=kwargs)

