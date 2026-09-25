from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAgilent4284a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent4284A.py', 'class_name': 'Agilent4284ASpot', 'import_roots': [], 'candidate_methods': ['measure_open', 'measure_short', 'measure_load', 'check_errors', 'measure_voltage', 'measure_current', 'auto_range_source', 'apply_current', 'apply_voltage', 'ramp_to_voltage', 'ramp_to_current'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/agilent/agilent4284A.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def measure_open(self, **kwargs):
        return self.call('measure_open', kwargs=kwargs)

    def measure_short(self, **kwargs):
        return self.call('measure_short', kwargs=kwargs)

    def measure_load(self, **kwargs):
        return self.call('measure_load', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def measure_voltage(self, **kwargs):
        return self.call('measure_voltage', kwargs=kwargs)

    def measure_current(self, **kwargs):
        return self.call('measure_current', kwargs=kwargs)

    def auto_range_source(self, **kwargs):
        return self.call('auto_range_source', kwargs=kwargs)

    def apply_current(self, **kwargs):
        return self.call('apply_current', kwargs=kwargs)

    def apply_voltage(self, **kwargs):
        return self.call('apply_voltage', kwargs=kwargs)

    def ramp_to_voltage(self, **kwargs):
        return self.call('ramp_to_voltage', kwargs=kwargs)

    def ramp_to_current(self, **kwargs):
        return self.call('ramp_to_current', kwargs=kwargs)

