from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLakeShore421(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/lakeshore/lakeshore421.py', 'class_name': 'LakeShore421', 'import_roots': [], 'candidate_methods': ['field', 'field_range', 'field_range', 'zero_probe', 'max_hold_field', 'max_hold_reset', 'relative_field', 'relative_setpoint', 'relative_setpoint', 'alarm_low', 'alarm_low', 'alarm_high', 'alarm_high', 'shutdown', 'delay_write', 'write'], 'metadata': {'source_file': 'pymeasure/instruments/lakeshore/lakeshore421.py', 'class_name': 'LakeShore421', 'candidate_score': 0.923, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def field(self, **kwargs):
            return self.call('field', kwargs=kwargs)

        def field_range(self, **kwargs):
            return self.call('field_range', kwargs=kwargs)

        def field_range(self, **kwargs):
            return self.call('field_range', kwargs=kwargs)

        def zero_probe(self, **kwargs):
            return self.call('zero_probe', kwargs=kwargs)

        def max_hold_field(self, **kwargs):
            return self.call('max_hold_field', kwargs=kwargs)

        def max_hold_reset(self, **kwargs):
            return self.call('max_hold_reset', kwargs=kwargs)

        def relative_field(self, **kwargs):
            return self.call('relative_field', kwargs=kwargs)

        def relative_setpoint(self, **kwargs):
            return self.call('relative_setpoint', kwargs=kwargs)

        def relative_setpoint(self, **kwargs):
            return self.call('relative_setpoint', kwargs=kwargs)

        def alarm_low(self, **kwargs):
            return self.call('alarm_low', kwargs=kwargs)

        def alarm_low(self, **kwargs):
            return self.call('alarm_low', kwargs=kwargs)

        def alarm_high(self, **kwargs):
            return self.call('alarm_high', kwargs=kwargs)

        def alarm_high(self, **kwargs):
            return self.call('alarm_high', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

        def delay_write(self, **kwargs):
            return self.call('delay_write', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

