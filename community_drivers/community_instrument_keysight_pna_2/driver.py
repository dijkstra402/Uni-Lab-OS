from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeysightPna2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keysight/keysightPNA.py', 'class_name': 'Marker', 'import_roots': [], 'candidate_methods': ['read_buffer', 'x_data', 'y_data', 'y_data_complex', 'initiate', 'single', 'continuous', 'hold', 'update_traces', 'abort', 'load_state', 'update_channels', 'reset'], 'metadata': {'source_file': 'pymeasure/instruments/keysight/keysightPNA.py', 'class_name': 'Marker', 'candidate_score': 0.905, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def read_buffer(self, **kwargs):
            return self.call('read_buffer', kwargs=kwargs)

        def x_data(self, **kwargs):
            return self.call('x_data', kwargs=kwargs)

        def y_data(self, **kwargs):
            return self.call('y_data', kwargs=kwargs)

        def y_data_complex(self, **kwargs):
            return self.call('y_data_complex', kwargs=kwargs)

        def initiate(self, **kwargs):
            return self.call('initiate', kwargs=kwargs)

        def single(self, **kwargs):
            return self.call('single', kwargs=kwargs)

        def continuous(self, **kwargs):
            return self.call('continuous', kwargs=kwargs)

        def hold(self, **kwargs):
            return self.call('hold', kwargs=kwargs)

        def update_traces(self, **kwargs):
            return self.call('update_traces', kwargs=kwargs)

        def abort(self, **kwargs):
            return self.call('abort', kwargs=kwargs)

        def load_state(self, **kwargs):
            return self.call('load_state', kwargs=kwargs)

        def update_channels(self, **kwargs):
            return self.call('update_channels', kwargs=kwargs)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

