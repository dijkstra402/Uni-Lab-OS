from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictLakeshore421(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/lakeshore/lakeshore421.py', 'class_name': 'LakeShore421', 'import_roots': [], 'candidate_methods': ['field', 'field_range', 'zero_probe', 'max_hold_field', 'max_hold_reset', 'relative_field', 'relative_setpoint', 'alarm_low', 'alarm_high', 'shutdown', 'delay_write', 'write', 'next_error', 'write_binary_values', 'read_binary_values', 'check_errors'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/lakeshore/lakeshore421.py', 'confidence': 0.75, 'quality_score': 0.89, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def field(self, **kwargs):
        return self.call('field', kwargs=kwargs)

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

    def alarm_low(self, **kwargs):
        return self.call('alarm_low', kwargs=kwargs)

    def alarm_high(self, **kwargs):
        return self.call('alarm_high', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

    def delay_write(self, **kwargs):
        return self.call('delay_write', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

