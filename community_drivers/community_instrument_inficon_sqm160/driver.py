from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentInficonSqm160(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/inficon/sqm160.py', 'class_name': 'SQM160', 'import_roots': [], 'candidate_methods': ['read', 'write', 'check_set_errors', 'reset_system_parameters', 'reset_thickness_rate', 'reset_time'], 'metadata': {'source_file': 'pymeasure/instruments/inficon/sqm160.py', 'class_name': 'SQM160', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def check_set_errors(self, **kwargs):
            return self.call('check_set_errors', kwargs=kwargs)

        def reset_system_parameters(self, **kwargs):
            return self.call('reset_system_parameters', kwargs=kwargs)

        def reset_thickness_rate(self, **kwargs):
            return self.call('reset_thickness_rate', kwargs=kwargs)

        def reset_time(self, **kwargs):
            return self.call('reset_time', kwargs=kwargs)

