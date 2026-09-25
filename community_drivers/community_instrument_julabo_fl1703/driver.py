from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentJulaboFl1703(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/santec/tsl570.py', 'class_name': 'SweepStatus', 'import_roots': [], 'candidate_methods': ['start_sweep', 'start_repeat', 'stop_sweep', 'sweep_pattern', 'sweep_pattern', 'sweep_routing', 'sweep_routing'], 'metadata': {'source_file': 'pymeasure/instruments/santec/tsl570.py', 'class_name': 'SweepStatus', 'candidate_score': 0.5, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def start_sweep(self, **kwargs):
            return self.call('start_sweep', kwargs=kwargs)

        def start_repeat(self, **kwargs):
            return self.call('start_repeat', kwargs=kwargs)

        def stop_sweep(self, **kwargs):
            return self.call('stop_sweep', kwargs=kwargs)

        def sweep_pattern(self, **kwargs):
            return self.call('sweep_pattern', kwargs=kwargs)

        def sweep_pattern(self, **kwargs):
            return self.call('sweep_pattern', kwargs=kwargs)

        def sweep_routing(self, **kwargs):
            return self.call('sweep_routing', kwargs=kwargs)

        def sweep_routing(self, **kwargs):
            return self.call('sweep_routing', kwargs=kwargs)

