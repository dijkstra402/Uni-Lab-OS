from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentNewportEsp3002(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/newport/esp300.py', 'class_name': 'Axis', 'import_roots': [], 'candidate_methods': ['ask', 'write', 'values', 'enable', 'disable', 'home', 'define_position', 'zero', 'wait_for_stop', 'clear_errors', 'errors', 'axes', 'enable', 'disable', 'shutdown'], 'metadata': {'source_file': 'pymeasure/instruments/newport/esp300.py', 'class_name': 'Axis', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def ask(self, **kwargs):
            return self.call('ask', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def values(self, **kwargs):
            return self.call('values', kwargs=kwargs)

        def enable(self, **kwargs):
            return self.call('enable', kwargs=kwargs)

        def disable(self, **kwargs):
            return self.call('disable', kwargs=kwargs)

        def home(self, **kwargs):
            return self.call('home', kwargs=kwargs)

        def define_position(self, **kwargs):
            return self.call('define_position', kwargs=kwargs)

        def zero(self, **kwargs):
            return self.call('zero', kwargs=kwargs)

        def wait_for_stop(self, **kwargs):
            return self.call('wait_for_stop', kwargs=kwargs)

        def clear_errors(self, **kwargs):
            return self.call('clear_errors', kwargs=kwargs)

        def errors(self, **kwargs):
            return self.call('errors', kwargs=kwargs)

        def axes(self, **kwargs):
            return self.call('axes', kwargs=kwargs)

        def enable(self, **kwargs):
            return self.call('enable', kwargs=kwargs)

        def disable(self, **kwargs):
            return self.call('disable', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

