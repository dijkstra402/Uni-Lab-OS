from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAmi430(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/ami/ami430.py', 'class_name': 'AMI430', 'import_roots': [], 'candidate_methods': ['zero', 'pause', 'ramp', 'has_persistent_switch_enabled', 'enable_persistent_switch', 'disable_persistent_switch', 'magnet_status', 'ramp_to_current', 'ramp_to_field', 'wait_for_holding', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/ami/ami430.py', 'class_name': 'AMI430', 'candidate_score': 0.923, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def zero(self, **kwargs):
            return self.call('zero', kwargs=kwargs)

        def pause(self, **kwargs):
            return self.call('pause', kwargs=kwargs)

        def ramp(self, **kwargs):
            return self.call('ramp', kwargs=kwargs)

        def has_persistent_switch_enabled(self, **kwargs):
            return self.call('has_persistent_switch_enabled', kwargs=kwargs)

        def enable_persistent_switch(self, **kwargs):
            return self.call('enable_persistent_switch', kwargs=kwargs)

        def disable_persistent_switch(self, **kwargs):
            return self.call('disable_persistent_switch', kwargs=kwargs)

        def magnet_status(self, **kwargs):
            return self.call('magnet_status', kwargs=kwargs)

        def ramp_to_current(self, **kwargs):
            return self.call('ramp_to_current', kwargs=kwargs)

        def ramp_to_field(self, **kwargs):
            return self.call('ramp_to_field', kwargs=kwargs)

        def wait_for_holding(self, **kwargs):
            return self.call('wait_for_holding', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

