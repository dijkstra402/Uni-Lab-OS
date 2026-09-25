from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithleyDaq6510(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithleyDAQ6510.py', 'class_name': 'KeithleyDAQ6510', 'import_roots': [], 'candidate_methods': ['measure_resistance', 'measure_voltage', 'measure_current', 'open_channel', 'close_channel', 'open_channels', 'close_channels', 'beep'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithleyDAQ6510.py', 'class_name': 'KeithleyDAQ6510', 'candidate_score': 0.968, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def measure_resistance(self, **kwargs):
            return self.call('measure_resistance', kwargs=kwargs)

        def measure_voltage(self, **kwargs):
            return self.call('measure_voltage', kwargs=kwargs)

        def measure_current(self, **kwargs):
            return self.call('measure_current', kwargs=kwargs)

        def open_channel(self, **kwargs):
            return self.call('open_channel', kwargs=kwargs)

        def close_channel(self, **kwargs):
            return self.call('close_channel', kwargs=kwargs)

        def open_channels(self, **kwargs):
            return self.call('open_channels', kwargs=kwargs)

        def close_channels(self, **kwargs):
            return self.call('close_channels', kwargs=kwargs)

        def beep(self, **kwargs):
            return self.call('beep', kwargs=kwargs)

