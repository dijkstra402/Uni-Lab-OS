from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentStanfordResearchSystemsLdc500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/srs/ldc500series.py', 'class_name': 'LDC500Series', 'import_roots': [], 'candidate_methods': ['calibrate', 'temperature_limits', 'temperature_limits', 'resistance_limits', 'resistance_limits', 'check_temperature_stability', 'options', 'next_error', 'check_errors', 'check_set_errors'], 'metadata': {'repo': 'pymeasure/pymeasure', 'source_file': 'pymeasure/instruments/srs/ldc500series.py', 'class_name': 'LDC500Series', 'fix_note': 'manually corrected SRS LDC500'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def calibrate(self, **kwargs):
        return self.call('calibrate', kwargs=kwargs)

    def temperature_limits(self, **kwargs):
        return self.call('temperature_limits', kwargs=kwargs)

    def temperature_limits(self, **kwargs):
        return self.call('temperature_limits', kwargs=kwargs)

    def resistance_limits(self, **kwargs):
        return self.call('resistance_limits', kwargs=kwargs)

    def resistance_limits(self, **kwargs):
        return self.call('resistance_limits', kwargs=kwargs)

    def check_temperature_stability(self, **kwargs):
        return self.call('check_temperature_stability', kwargs=kwargs)

    def options(self, **kwargs):
        return self.call('options', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def check_set_errors(self, **kwargs):
        return self.call('check_set_errors', kwargs=kwargs)

