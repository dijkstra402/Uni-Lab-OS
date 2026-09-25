from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAgilent34450a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent34450A.py', 'class_name': 'Agilent34450A', 'import_roots': [], 'candidate_methods': ['mode', 'configure_voltage', 'configure_current', 'configure_resistance', 'configure_frequency', 'configure_temperature', 'configure_diode', 'configure_capacitance', 'configure_continuity', 'beep', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/agilent/agilent34450A.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def mode(self, **kwargs):
        return self.call('mode', kwargs=kwargs)

    def configure_voltage(self, **kwargs):
        return self.call('configure_voltage', kwargs=kwargs)

    def configure_current(self, **kwargs):
        return self.call('configure_current', kwargs=kwargs)

    def configure_resistance(self, **kwargs):
        return self.call('configure_resistance', kwargs=kwargs)

    def configure_frequency(self, **kwargs):
        return self.call('configure_frequency', kwargs=kwargs)

    def configure_temperature(self, **kwargs):
        return self.call('configure_temperature', kwargs=kwargs)

    def configure_diode(self, **kwargs):
        return self.call('configure_diode', kwargs=kwargs)

    def configure_capacitance(self, **kwargs):
        return self.call('configure_capacitance', kwargs=kwargs)

    def configure_continuity(self, **kwargs):
        return self.call('configure_continuity', kwargs=kwargs)

    def beep(self, **kwargs):
        return self.call('beep', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

