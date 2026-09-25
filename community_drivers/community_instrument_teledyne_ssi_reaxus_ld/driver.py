from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTeledyneSsiReaxusLd(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/pct-code__py-hplc', 'source_file': 'py_hplc/pump.py', 'class_name': 'NextGenPump', 'import_roots': [], 'candidate_methods': ['run', 'stop', 'keypad_enable', 'keypad_disable', 'clear_faults', 'reset', 'zero_seal', 'current_conditions', 'current_state', 'pump_info', 'read_faults', 'is_running', 'stroke_counter', 'flowrate_compensation', 'flowrate', 'pressure', 'upper_pressure_limit', 'lower_pressure_limit', 'leak_detected', 'set_leak_mode', 'solvent', 'identify', 'command', 'is_open'], 'action_targets': {}, 'metadata': {'repo': 'pct-code/py-hplc', 'repo_url': 'https://github.com/pct-code/py-hplc', 'brand': 'Teledyne SSI', 'model': 'Reaxus LD', 'device_type_cn': 'HPLC泵', 'device_type_en': 'HPLC Pump', 'source_framework': 'py-hplc', 'tag_id': '4370', 'tag_name': '凝胶渗透色谱仪', 'tag_name_en': 'Gel Permeation Chromatograph', 'candidate_score': 234, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def keypad_enable(self, **kwargs):
        return self.call('keypad_enable', kwargs=kwargs)

    def keypad_disable(self, **kwargs):
        return self.call('keypad_disable', kwargs=kwargs)

    def clear_faults(self, **kwargs):
        return self.call('clear_faults', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def zero_seal(self, **kwargs):
        return self.call('zero_seal', kwargs=kwargs)

    def current_conditions(self, **kwargs):
        return self.call('current_conditions', kwargs=kwargs)

    def current_state(self, **kwargs):
        return self.call('current_state', kwargs=kwargs)

    def pump_info(self, **kwargs):
        return self.call('pump_info', kwargs=kwargs)

    def read_faults(self, **kwargs):
        return self.call('read_faults', kwargs=kwargs)

    def is_running(self, **kwargs):
        return self.call('is_running', kwargs=kwargs)

    def stroke_counter(self, **kwargs):
        return self.call('stroke_counter', kwargs=kwargs)

    def flowrate_compensation(self, **kwargs):
        return self.call('flowrate_compensation', kwargs=kwargs)

    def flowrate(self, **kwargs):
        return self.call('flowrate', kwargs=kwargs)

    def pressure(self, **kwargs):
        return self.call('pressure', kwargs=kwargs)

    def upper_pressure_limit(self, **kwargs):
        return self.call('upper_pressure_limit', kwargs=kwargs)

    def lower_pressure_limit(self, **kwargs):
        return self.call('lower_pressure_limit', kwargs=kwargs)

    def leak_detected(self, **kwargs):
        return self.call('leak_detected', kwargs=kwargs)

    def set_leak_mode(self, **kwargs):
        return self.call('set_leak_mode', kwargs=kwargs)

    def solvent(self, **kwargs):
        return self.call('solvent', kwargs=kwargs)

    def identify(self, **kwargs):
        return self.call('identify', kwargs=kwargs)

    def command(self, **kwargs):
        return self.call('command', kwargs=kwargs)

    def is_open(self, **kwargs):
        return self.call('is_open', kwargs=kwargs)

