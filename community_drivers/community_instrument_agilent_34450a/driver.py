from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAgilent34450a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/agilent/agilent34450A.py', 'class_name': 'Agilent34450A', 'import_roots': [], 'candidate_methods': ['mode', 'mode', 'configure_voltage', 'configure_current', 'configure_resistance', 'configure_frequency', 'configure_temperature', 'configure_diode', 'configure_capacitance', 'configure_continuity', 'beep'], 'metadata': {'source_file': 'pymeasure/instruments/agilent/agilent34450A.py', 'class_name': 'Agilent34450A', 'candidate_score': 0.963, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def mode(self, **kwargs):
            return self.call('mode', kwargs=kwargs)

        def mode(self, **kwargs):
            return self.call('mode', kwargs=kwargs)

        def configure_voltage(self, **kwargs):
            return self.call('configure_voltage', kwargs=kwargs)

        def configure_current(self, **kwargs):
            return self.call('configure_current', kwargs=kwargs)

        def configure_resistance(self, **kwargs):
            return self.call('configure_resistance', kwargs=kwargs)

        def configure_frequency(self, **kwargs):
            return self.call('configure_frequency', kwargs=kwargs)

        def configure_temperature(self, **kwargs):
            return self.call('configure_temperature', kwargs=kwargs)

        def configure_diode(self, **kwargs):
            return self.call('configure_diode', kwargs=kwargs)

        def configure_capacitance(self, **kwargs):
            return self.call('configure_capacitance', kwargs=kwargs)

        def configure_continuity(self, **kwargs):
            return self.call('configure_continuity', kwargs=kwargs)

        def beep(self, **kwargs):
            return self.call('beep', kwargs=kwargs)

