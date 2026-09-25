from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentSiglentSds1000xhd(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/siglenttechnologies/siglent_sds1000xhd.py', 'class_name': 'AdvancedMeasurementItem', 'import_roots': [], 'candidate_methods': ['preamble', 'get_data', 'get_simple_value', 'clear_simple', 'clear_advanced', 'reset_statistics', 'force_trigger', 'run', 'stop', 'auto_setup', 'clear_sweeps_acq'], 'metadata': {'source_file': 'pymeasure/instruments/siglenttechnologies/siglent_sds1000xhd.py', 'class_name': 'AdvancedMeasurementItem', 'candidate_score': 1.0, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def preamble(self, **kwargs):
            return self.call('preamble', kwargs=kwargs)

        def get_data(self, **kwargs):
            return self.call('get_data', kwargs=kwargs)

        def get_simple_value(self, **kwargs):
            return self.call('get_simple_value', kwargs=kwargs)

        def clear_simple(self, **kwargs):
            return self.call('clear_simple', kwargs=kwargs)

        def clear_advanced(self, **kwargs):
            return self.call('clear_advanced', kwargs=kwargs)

        def reset_statistics(self, **kwargs):
            return self.call('reset_statistics', kwargs=kwargs)

        def force_trigger(self, **kwargs):
            return self.call('force_trigger', kwargs=kwargs)

        def run(self, **kwargs):
            return self.call('run', kwargs=kwargs)

        def stop(self, **kwargs):
            return self.call('stop', kwargs=kwargs)

        def auto_setup(self, **kwargs):
            return self.call('auto_setup', kwargs=kwargs)

        def clear_sweeps_acq(self, **kwargs):
            return self.call('clear_sweeps_acq', kwargs=kwargs)

