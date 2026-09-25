from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictKeysightdsox1102g(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/keysight/keysightDSOX1102G.py', 'class_name': 'KeysightDSOX1102G', 'import_roots': [], 'candidate_methods': ['autoscale', 'timebase', 'run', 'stop', 'single', 'digitize', 'waveform_preamble', 'waveform_data', 'system_setup', 'ch', 'clear_status', 'factory_reset', 'default_setup', 'timebase_setup', 'download_image', 'download_data', 'check_errors', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/keysight/keysightDSOX1102G.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def autoscale(self, **kwargs):
        return self.call('autoscale', kwargs=kwargs)

    def timebase(self, **kwargs):
        return self.call('timebase', kwargs=kwargs)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def single(self, **kwargs):
        return self.call('single', kwargs=kwargs)

    def digitize(self, **kwargs):
        return self.call('digitize', kwargs=kwargs)

    def waveform_preamble(self, **kwargs):
        return self.call('waveform_preamble', kwargs=kwargs)

    def waveform_data(self, **kwargs):
        return self.call('waveform_data', kwargs=kwargs)

    def system_setup(self, **kwargs):
        return self.call('system_setup', kwargs=kwargs)

    def ch(self, **kwargs):
        return self.call('ch', kwargs=kwargs)

    def clear_status(self, **kwargs):
        return self.call('clear_status', kwargs=kwargs)

    def factory_reset(self, **kwargs):
        return self.call('factory_reset', kwargs=kwargs)

    def default_setup(self, **kwargs):
        return self.call('default_setup', kwargs=kwargs)

    def timebase_setup(self, **kwargs):
        return self.call('timebase_setup', kwargs=kwargs)

    def download_image(self, **kwargs):
        return self.call('download_image', kwargs=kwargs)

    def download_data(self, **kwargs):
        return self.call('download_data', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

