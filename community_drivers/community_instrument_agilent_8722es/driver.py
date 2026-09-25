from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilent8722es(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent8722ES.py', 'class_name': 'Agilent8722ES', 'import_roots': [], 'candidate_methods': ['set_fixed_frequency', 'parameter', 'parameter', 'scan_points', 'scan_points', 'set_IF_bandwidth', 'set_averaging', 'disable_averaging', 'enable_averaging', 'is_averaging', 'restart_averaging', 'scan', 'scan_single', 'scan_continuous', 'frequencies', 'data_complex', 'data_log_magnitude', 'data_magnitude', 'data_phase', 'data'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilent8722ES.py', 'class_name': 'Agilent8722ES', 'candidate_score': 0.963, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def set_fixed_frequency(self, **kwargs):
            return self.call('set_fixed_frequency', kwargs=kwargs)

        def parameter(self, **kwargs):
            return self.call('parameter', kwargs=kwargs)

        def parameter(self, **kwargs):
            return self.call('parameter', kwargs=kwargs)

        def scan_points(self, **kwargs):
            return self.call('scan_points', kwargs=kwargs)

        def scan_points(self, **kwargs):
            return self.call('scan_points', kwargs=kwargs)

        def set_IF_bandwidth(self, **kwargs):
            return self.call('set_IF_bandwidth', kwargs=kwargs)

        def set_averaging(self, **kwargs):
            return self.call('set_averaging', kwargs=kwargs)

        def disable_averaging(self, **kwargs):
            return self.call('disable_averaging', kwargs=kwargs)

        def enable_averaging(self, **kwargs):
            return self.call('enable_averaging', kwargs=kwargs)

        def is_averaging(self, **kwargs):
            return self.call('is_averaging', kwargs=kwargs)

        def restart_averaging(self, **kwargs):
            return self.call('restart_averaging', kwargs=kwargs)

        def scan(self, **kwargs):
            return self.call('scan', kwargs=kwargs)

        def scan_single(self, **kwargs):
            return self.call('scan_single', kwargs=kwargs)

        def scan_continuous(self, **kwargs):
            return self.call('scan_continuous', kwargs=kwargs)

        def frequencies(self, **kwargs):
            return self.call('frequencies', kwargs=kwargs)

        def data_complex(self, **kwargs):
            return self.call('data_complex', kwargs=kwargs)

        def data_log_magnitude(self, **kwargs):
            return self.call('data_log_magnitude', kwargs=kwargs)

        def data_magnitude(self, **kwargs):
            return self.call('data_magnitude', kwargs=kwargs)

        def data_phase(self, **kwargs):
            return self.call('data_phase', kwargs=kwargs)

        def data(self, **kwargs):
            return self.call('data', kwargs=kwargs)

