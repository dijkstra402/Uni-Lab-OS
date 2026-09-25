from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHewlettPackard3478a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/hp/hp3478A.py', 'class_name': 'SRQ', 'import_roots': [], 'candidate_methods': ['active_connectors', 'auto_range_enabled', 'auto_zero_enabled', 'auto_zero_enabled', 'calibration_enabled', 'check_errors', 'display_reset', 'mode', 'mode', 'range', 'range', 'resolution', 'resolution', 'SRQ_mask', 'SRQ_mask', 'trigger', 'trigger', 'calibration_data', 'calibration_data', 'write_calibration_data'], 'metadata': {'source_file': 'pymeasure/instruments/hp/hp3478A.py', 'class_name': 'SRQ', 'candidate_score': 0.833, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def active_connectors(self, **kwargs):
            return self.call('active_connectors', kwargs=kwargs)

        def auto_range_enabled(self, **kwargs):
            return self.call('auto_range_enabled', kwargs=kwargs)

        def auto_zero_enabled(self, **kwargs):
            return self.call('auto_zero_enabled', kwargs=kwargs)

        def auto_zero_enabled(self, **kwargs):
            return self.call('auto_zero_enabled', kwargs=kwargs)

        def calibration_enabled(self, **kwargs):
            return self.call('calibration_enabled', kwargs=kwargs)

        def check_errors(self, **kwargs):
            return self.call('check_errors', kwargs=kwargs)

        def display_reset(self, **kwargs):
            return self.call('display_reset', kwargs=kwargs)

        def mode(self, **kwargs):
            return self.call('mode', kwargs=kwargs)

        def mode(self, **kwargs):
            return self.call('mode', kwargs=kwargs)

        def range(self, **kwargs):
            return self.call('range', kwargs=kwargs)

        def range(self, **kwargs):
            return self.call('range', kwargs=kwargs)

        def resolution(self, **kwargs):
            return self.call('resolution', kwargs=kwargs)

        def resolution(self, **kwargs):
            return self.call('resolution', kwargs=kwargs)

        def SRQ_mask(self, **kwargs):
            return self.call('SRQ_mask', kwargs=kwargs)

        def SRQ_mask(self, **kwargs):
            return self.call('SRQ_mask', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def calibration_data(self, **kwargs):
            return self.call('calibration_data', kwargs=kwargs)

        def calibration_data(self, **kwargs):
            return self.call('calibration_data', kwargs=kwargs)

        def write_calibration_data(self, **kwargs):
            return self.call('write_calibration_data', kwargs=kwargs)

