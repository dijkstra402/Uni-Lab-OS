from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHewlettPackard6633a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/hp/hp3437A.py', 'class_name': 'Status', 'import_roots': [], 'candidate_methods': ['read_data', 'check_errors', 'talk_ascii', 'talk_ascii', 'delay', 'delay', 'number_readings', 'number_readings', 'range', 'range', 'SRQ_mask', 'SRQ_mask', 'trigger', 'trigger'], 'metadata': {'source_file': 'pymeasure/instruments/hp/hp3437A.py', 'class_name': 'Status', 'candidate_score': 0.5, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def read_data(self, **kwargs):
            return self.call('read_data', kwargs=kwargs)

        def check_errors(self, **kwargs):
            return self.call('check_errors', kwargs=kwargs)

        def talk_ascii(self, **kwargs):
            return self.call('talk_ascii', kwargs=kwargs)

        def talk_ascii(self, **kwargs):
            return self.call('talk_ascii', kwargs=kwargs)

        def delay(self, **kwargs):
            return self.call('delay', kwargs=kwargs)

        def delay(self, **kwargs):
            return self.call('delay', kwargs=kwargs)

        def number_readings(self, **kwargs):
            return self.call('number_readings', kwargs=kwargs)

        def number_readings(self, **kwargs):
            return self.call('number_readings', kwargs=kwargs)

        def range(self, **kwargs):
            return self.call('range', kwargs=kwargs)

        def range(self, **kwargs):
            return self.call('range', kwargs=kwargs)

        def SRQ_mask(self, **kwargs):
            return self.call('SRQ_mask', kwargs=kwargs)

        def SRQ_mask(self, **kwargs):
            return self.call('SRQ_mask', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

