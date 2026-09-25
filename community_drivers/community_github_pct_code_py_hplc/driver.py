from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityGithubPctCodePyHplc(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/private/tmp/github_drivers_clone/pct-code_py-hplc', 'source_file': 'py_hplc/pump.py', 'class_name': 'NextGenPump', 'import_roots': [], 'candidate_methods': ['run', 'stop', 'keypad_enable', 'keypad_disable', 'clear_faults', 'reset', 'zero_seal', 'current_conditions', 'current_state', 'pump_info', 'read_faults', 'is_running', 'stroke_counter', 'flowrate_compensation', 'flowrate_compensation', 'flowrate', 'flowrate', 'pressure', 'upper_pressure_limit', 'upper_pressure_limit'], 'metadata': {'repo': 'pct-code/py-hplc', 'repo_url': 'https://github.com/pct-code/py-hplc', 'unit_id': 'gh_ssi_teledyne_next_generation', 'source_file': 'py_hplc/pump.py', 'candidate_score': 51, 'manufacturer': 'SSI-Teledyne', 'model_name': 'SSI-Teledyne Next Generation'}}

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

    def flowrate_compensation(self, **kwargs):
        return self.call('flowrate_compensation', kwargs=kwargs)

    def flowrate(self, **kwargs):
        return self.call('flowrate', kwargs=kwargs)

    def flowrate(self, **kwargs):
        return self.call('flowrate', kwargs=kwargs)

    def pressure(self, **kwargs):
        return self.call('pressure', kwargs=kwargs)

    def upper_pressure_limit(self, **kwargs):
        return self.call('upper_pressure_limit', kwargs=kwargs)

    def upper_pressure_limit(self, **kwargs):
        return self.call('upper_pressure_limit', kwargs=kwargs)

