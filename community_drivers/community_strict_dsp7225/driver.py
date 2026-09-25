from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictDsp7225(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/signalrecovery/dsp7225.py', 'class_name': 'DSP7225', 'import_roots': [], 'candidate_methods': ['gain', 'sensitivity', 'auto_gain', 'set_voltage_mode', 'setDifferentialMode', 'setChannelAMode', 'auto_sensitivity', 'auto_phase', 'init_curve_buffer', 'set_buffer', 'start_buffer', 'wait_for_buffer', 'get_buffer', 'buffer_to_float', 'next_error', 'write_binary_values', 'read_binary_values', 'check_errors'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/signalrecovery/dsp7225.py', 'confidence': 0.75, 'quality_score': 0.89, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def gain(self, **kwargs):
        return self.call('gain', kwargs=kwargs)

    def sensitivity(self, **kwargs):
        return self.call('sensitivity', kwargs=kwargs)

    def auto_gain(self, **kwargs):
        return self.call('auto_gain', kwargs=kwargs)

    def set_voltage_mode(self, **kwargs):
        return self.call('set_voltage_mode', kwargs=kwargs)

    def setDifferentialMode(self, **kwargs):
        return self.call('setDifferentialMode', kwargs=kwargs)

    def setChannelAMode(self, **kwargs):
        return self.call('setChannelAMode', kwargs=kwargs)

    def auto_sensitivity(self, **kwargs):
        return self.call('auto_sensitivity', kwargs=kwargs)

    def auto_phase(self, **kwargs):
        return self.call('auto_phase', kwargs=kwargs)

    def init_curve_buffer(self, **kwargs):
        return self.call('init_curve_buffer', kwargs=kwargs)

    def set_buffer(self, **kwargs):
        return self.call('set_buffer', kwargs=kwargs)

    def start_buffer(self, **kwargs):
        return self.call('start_buffer', kwargs=kwargs)

    def wait_for_buffer(self, **kwargs):
        return self.call('wait_for_buffer', kwargs=kwargs)

    def get_buffer(self, **kwargs):
        return self.call('get_buffer', kwargs=kwargs)

    def buffer_to_float(self, **kwargs):
        return self.call('buffer_to_float', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

