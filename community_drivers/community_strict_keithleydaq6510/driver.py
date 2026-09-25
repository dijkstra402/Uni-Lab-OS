from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictKeithleydaq6510(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/keithley/keithleyDAQ6510.py', 'class_name': 'KeithleyDAQ6510', 'import_roots': [], 'candidate_methods': ['measure_resistance', 'measure_voltage', 'measure_current', 'open_channel', 'close_channel', 'open_channels', 'close_channels', 'beep', 'config_buffer', 'is_buffer_full', 'wait_for_buffer', 'buffer_data', 'start_buffer', 'reset_buffer', 'stop_buffer', 'disable_buffer', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/keithley/keithleyDAQ6510.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

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

    def config_buffer(self, **kwargs):
        return self.call('config_buffer', kwargs=kwargs)

    def is_buffer_full(self, **kwargs):
        return self.call('is_buffer_full', kwargs=kwargs)

    def wait_for_buffer(self, **kwargs):
        return self.call('wait_for_buffer', kwargs=kwargs)

    def buffer_data(self, **kwargs):
        return self.call('buffer_data', kwargs=kwargs)

    def start_buffer(self, **kwargs):
        return self.call('start_buffer', kwargs=kwargs)

    def reset_buffer(self, **kwargs):
        return self.call('reset_buffer', kwargs=kwargs)

    def stop_buffer(self, **kwargs):
        return self.call('stop_buffer', kwargs=kwargs)

    def disable_buffer(self, **kwargs):
        return self.call('disable_buffer', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

