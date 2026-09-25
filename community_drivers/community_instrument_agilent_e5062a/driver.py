from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilentE5062a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilentE5062A.py', 'class_name': 'VNATrace', 'import_roots': [], 'candidate_methods': ['activate', 'restart_averaging', 'activate', 'visible_traces', 'visible_traces', 'attenuation', 'attenuation', 'data', 'frequencies', 'trigger_initiate', 'abort', 'trigger_bus', 'trigger', 'trigger_single', 'wait_for_complete', 'pop_err'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilentE5062A.py', 'class_name': 'VNATrace', 'candidate_score': 0.963, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def activate(self, **kwargs):
            return self.call('activate', kwargs=kwargs)

        def restart_averaging(self, **kwargs):
            return self.call('restart_averaging', kwargs=kwargs)

        def activate(self, **kwargs):
            return self.call('activate', kwargs=kwargs)

        def visible_traces(self, **kwargs):
            return self.call('visible_traces', kwargs=kwargs)

        def visible_traces(self, **kwargs):
            return self.call('visible_traces', kwargs=kwargs)

        def attenuation(self, **kwargs):
            return self.call('attenuation', kwargs=kwargs)

        def attenuation(self, **kwargs):
            return self.call('attenuation', kwargs=kwargs)

        def data(self, **kwargs):
            return self.call('data', kwargs=kwargs)

        def frequencies(self, **kwargs):
            return self.call('frequencies', kwargs=kwargs)

        def trigger_initiate(self, **kwargs):
            return self.call('trigger_initiate', kwargs=kwargs)

        def abort(self, **kwargs):
            return self.call('abort', kwargs=kwargs)

        def trigger_bus(self, **kwargs):
            return self.call('trigger_bus', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def trigger_single(self, **kwargs):
            return self.call('trigger_single', kwargs=kwargs)

        def wait_for_complete(self, **kwargs):
            return self.call('wait_for_complete', kwargs=kwargs)

        def pop_err(self, **kwargs):
            return self.call('pop_err', kwargs=kwargs)

