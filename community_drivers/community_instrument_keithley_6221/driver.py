from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeithley6221(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pymeasure_pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithley6221.py', 'class_name': 'Keithley6221', 'import_roots': [], 'candidate_methods': ['delta_arm', 'delta_start', 'delta_abort', 'waveform_duration_set_infinity', 'waveform_arm', 'waveform_start', 'waveform_abort', 'define_arbitary_waveform', 'enable_source', 'disable_source', 'beep', 'triad', 'error', 'reset', 'trigger', 'trigger_immediately', 'trigger_on_bus', 'set_timed_arm', 'trigger_on_external', 'output_trigger_on_external'], 'metadata': {'source_file': 'pymeasure/instruments/keithley/keithley6221.py', 'class_name': 'Keithley6221', 'candidate_score': 0.96, 'fix_note': 'reselected from tests->instruments'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

        def delta_arm(self, **kwargs):
            return self.call('delta_arm', kwargs=kwargs)

        def delta_start(self, **kwargs):
            return self.call('delta_start', kwargs=kwargs)

        def delta_abort(self, **kwargs):
            return self.call('delta_abort', kwargs=kwargs)

        def waveform_duration_set_infinity(self, **kwargs):
            return self.call('waveform_duration_set_infinity', kwargs=kwargs)

        def waveform_arm(self, **kwargs):
            return self.call('waveform_arm', kwargs=kwargs)

        def waveform_start(self, **kwargs):
            return self.call('waveform_start', kwargs=kwargs)

        def waveform_abort(self, **kwargs):
            return self.call('waveform_abort', kwargs=kwargs)

        def define_arbitary_waveform(self, **kwargs):
            return self.call('define_arbitary_waveform', kwargs=kwargs)

        def enable_source(self, **kwargs):
            return self.call('enable_source', kwargs=kwargs)

        def disable_source(self, **kwargs):
            return self.call('disable_source', kwargs=kwargs)

        def beep(self, **kwargs):
            return self.call('beep', kwargs=kwargs)

        def triad(self, **kwargs):
            return self.call('triad', kwargs=kwargs)

        def error(self, **kwargs):
            return self.call('error', kwargs=kwargs)

        def reset(self, **kwargs):
            return self.call('reset', kwargs=kwargs)

        def trigger(self, **kwargs):
            return self.call('trigger', kwargs=kwargs)

        def trigger_immediately(self, **kwargs):
            return self.call('trigger_immediately', kwargs=kwargs)

        def trigger_on_bus(self, **kwargs):
            return self.call('trigger_on_bus', kwargs=kwargs)

        def set_timed_arm(self, **kwargs):
            return self.call('set_timed_arm', kwargs=kwargs)

        def trigger_on_external(self, **kwargs):
            return self.call('trigger_on_external', kwargs=kwargs)

        def output_trigger_on_external(self, **kwargs):
            return self.call('output_trigger_on_external', kwargs=kwargs)

