from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithleyDmm6500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithleyDMM6500.py', 'class_name': 'KeithleyDMM6500', 'import_roots': [], 'candidate_methods': ['enable_filter', 'disable_filter', 'write', 'close', 'trigger_single_autozero', 'displayed_text', 'measure_current', 'measure_voltage', 'measure_resistance', 'measure_frequency', 'measure_period', 'measure_temperature', 'measure_capacitance', 'measure_diode', 'measure_continuity', 'scan_channels_list', 'scan_channels_list', 'scanned_data', 'scan_modes', 'scan_modes'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithleyDMM6500.py', 'class_name': 'KeithleyDMM6500', 'candidate_score': 0.968, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def enable_filter(self, **kwargs):
            return self.call('enable_filter', kwargs=kwargs)

        def disable_filter(self, **kwargs):
            return self.call('disable_filter', kwargs=kwargs)

        def write(self, **kwargs):
            return self.call('write', kwargs=kwargs)

        def close(self, **kwargs):
            return self.call('close', kwargs=kwargs)

        def trigger_single_autozero(self, **kwargs):
            return self.call('trigger_single_autozero', kwargs=kwargs)

        def displayed_text(self, **kwargs):
            return self.call('displayed_text', kwargs=kwargs)

        def measure_current(self, **kwargs):
            return self.call('measure_current', kwargs=kwargs)

        def measure_voltage(self, **kwargs):
            return self.call('measure_voltage', kwargs=kwargs)

        def measure_resistance(self, **kwargs):
            return self.call('measure_resistance', kwargs=kwargs)

        def measure_frequency(self, **kwargs):
            return self.call('measure_frequency', kwargs=kwargs)

        def measure_period(self, **kwargs):
            return self.call('measure_period', kwargs=kwargs)

        def measure_temperature(self, **kwargs):
            return self.call('measure_temperature', kwargs=kwargs)

        def measure_capacitance(self, **kwargs):
            return self.call('measure_capacitance', kwargs=kwargs)

        def measure_diode(self, **kwargs):
            return self.call('measure_diode', kwargs=kwargs)

        def measure_continuity(self, **kwargs):
            return self.call('measure_continuity', kwargs=kwargs)

        def scan_channels_list(self, **kwargs):
            return self.call('scan_channels_list', kwargs=kwargs)

        def scan_channels_list(self, **kwargs):
            return self.call('scan_channels_list', kwargs=kwargs)

        def scanned_data(self, **kwargs):
            return self.call('scanned_data', kwargs=kwargs)

        def scan_modes(self, **kwargs):
            return self.call('scan_modes', kwargs=kwargs)

        def scan_modes(self, **kwargs):
            return self.call('scan_modes', kwargs=kwargs)

