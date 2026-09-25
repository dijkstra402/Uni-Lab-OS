from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentDanfysik8500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/danfysik/danfysik8500.py', 'class_name': 'Danfysik8500', 'import_roots': [], 'candidate_methods': ['read', 'local', 'remote', 'polarity', 'polarity', 'reset_interlocks', 'enable', 'disable', 'is_enabled', 'status_hex', 'current', 'current', 'current_ppm', 'current_ppm', 'current_setpoint', 'slew_rate', 'wait_for_current', 'is_current_stable', 'is_ready', 'wait_for_ready'], 'metadata': {'source_file': 'pymeasure/instruments/danfysik/danfysik8500.py', 'class_name': 'Danfysik8500', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def read(self, **kwargs):
            return self.call('read', kwargs=kwargs)

        def local(self, **kwargs):
            return self.call('local', kwargs=kwargs)

        def remote(self, **kwargs):
            return self.call('remote', kwargs=kwargs)

        def polarity(self, **kwargs):
            return self.call('polarity', kwargs=kwargs)

        def polarity(self, **kwargs):
            return self.call('polarity', kwargs=kwargs)

        def reset_interlocks(self, **kwargs):
            return self.call('reset_interlocks', kwargs=kwargs)

        def enable(self, **kwargs):
            return self.call('enable', kwargs=kwargs)

        def disable(self, **kwargs):
            return self.call('disable', kwargs=kwargs)

        def is_enabled(self, **kwargs):
            return self.call('is_enabled', kwargs=kwargs)

        def status_hex(self, **kwargs):
            return self.call('status_hex', kwargs=kwargs)

        def current(self, **kwargs):
            return self.call('current', kwargs=kwargs)

        def current(self, **kwargs):
            return self.call('current', kwargs=kwargs)

        def current_ppm(self, **kwargs):
            return self.call('current_ppm', kwargs=kwargs)

        def current_ppm(self, **kwargs):
            return self.call('current_ppm', kwargs=kwargs)

        def current_setpoint(self, **kwargs):
            return self.call('current_setpoint', kwargs=kwargs)

        def slew_rate(self, **kwargs):
            return self.call('slew_rate', kwargs=kwargs)

        def wait_for_current(self, **kwargs):
            return self.call('wait_for_current', kwargs=kwargs)

        def is_current_stable(self, **kwargs):
            return self.call('is_current_stable', kwargs=kwargs)

        def is_ready(self, **kwargs):
            return self.call('is_ready', kwargs=kwargs)

        def wait_for_ready(self, **kwargs):
            return self.call('wait_for_ready', kwargs=kwargs)

