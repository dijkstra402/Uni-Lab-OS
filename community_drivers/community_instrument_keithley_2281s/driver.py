from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley2281s(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithley2281S.py', 'class_name': 'Keithley2281SOperationEventRegister', 'import_roots': [], 'candidate_methods': ['buffer_data', 'set_battery_model_range', 'save_model_to_usb', 'buffer_data', 'load_model_from_usb', 'buffer_data', 'buffer_data', 'measurement_ongoing', 'reading_available'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithley2281S.py', 'class_name': 'Keithley2281SOperationEventRegister', 'candidate_score': 0.963, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def buffer_data(self, **kwargs):
            return self.call('buffer_data', kwargs=kwargs)

        def set_battery_model_range(self, **kwargs):
            return self.call('set_battery_model_range', kwargs=kwargs)

        def save_model_to_usb(self, **kwargs):
            return self.call('save_model_to_usb', kwargs=kwargs)

        def buffer_data(self, **kwargs):
            return self.call('buffer_data', kwargs=kwargs)

        def load_model_from_usb(self, **kwargs):
            return self.call('load_model_from_usb', kwargs=kwargs)

        def buffer_data(self, **kwargs):
            return self.call('buffer_data', kwargs=kwargs)

        def buffer_data(self, **kwargs):
            return self.call('buffer_data', kwargs=kwargs)

        def measurement_ongoing(self, **kwargs):
            return self.call('measurement_ongoing', kwargs=kwargs)

        def reading_available(self, **kwargs):
            return self.call('reading_available', kwargs=kwargs)

