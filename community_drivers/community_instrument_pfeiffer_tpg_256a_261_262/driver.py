from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPfeifferTpg256a261262(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/buffer.py', 'class_name': 'KeithleyBuffer', 'import_roots': [], 'candidate_methods': ['config_buffer', 'is_buffer_full', 'wait_for_buffer', 'buffer_data', 'start_buffer', 'reset_buffer', 'stop_buffer', 'disable_buffer'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/buffer.py', 'class_name': 'KeithleyBuffer', 'candidate_score': 0.571, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def config_buffer(self, **kwargs):
            return self.call('config_buffer', kwargs=kwargs)

        def is_buffer_full(self, **kwargs):
            return self.call('is_buffer_full', kwargs=kwargs)

        def wait_for_buffer(self, **kwargs):
            return self.call('wait_for_buffer', kwargs=kwargs)

        def buffer_data(self, **kwargs):
            return self.call('buffer_data', kwargs=kwargs)

        def start_buffer(self, **kwargs):
            return self.call('start_buffer', kwargs=kwargs)

        def reset_buffer(self, **kwargs):
            return self.call('reset_buffer', kwargs=kwargs)

        def stop_buffer(self, **kwargs):
            return self.call('stop_buffer', kwargs=kwargs)

        def disable_buffer(self, **kwargs):
            return self.call('disable_buffer', kwargs=kwargs)

