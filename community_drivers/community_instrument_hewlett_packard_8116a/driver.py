from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHewlettPackard8116a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/hp/hp8116a.py', 'class_name': 'Status', 'import_roots': [], 'candidate_methods': ['write', 'ask', 'status', 'complete', 'options', 'start_autovernier', 'GPIB_trigger', 'reset', 'shutdown', 'check_errors'], 'metadata': {'source_file': 'pymeasure/instruments/hp/hp8116a.py', 'class_name': 'Status', 'candidate_score': 0.833, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def ask(self, **kwargs):
            return self.call('ask', kwargs=kwargs)

        def status(self, **kwargs):
            return self.call('status', kwargs=kwargs)

        def complete(self, **kwargs):
            return self.call('complete', kwargs=kwargs)

        def options(self, **kwargs):
            return self.call('options', kwargs=kwargs)

        def start_autovernier(self, **kwargs):
            return self.call('start_autovernier', kwargs=kwargs)

        def GPIB_trigger(self, **kwargs):
            return self.call('GPIB_trigger', kwargs=kwargs)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

        def shutdown(self, **kwargs):
            return self.call('shutdown', kwargs=kwargs)

        def check_errors(self, **kwargs):
            return self.call('check_errors', kwargs=kwargs)

