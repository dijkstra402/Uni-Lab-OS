from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAnritsums464xb(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/pymeasure__pymeasure', 'source_file': 'pymeasure/instruments/anritsu/anritsuMS464xB.py', 'class_name': 'AnritsuMS464xB', 'import_roots': [], 'candidate_methods': ['update_channels', 'check_errors', 'query_event_status_register', 'return_to_local', 'trigger', 'trigger_single', 'trigger_continuous', 'load_data_file', 'delete_data_file', 'copy_data_file', 'load_data_file_to_memory', 'create_directory', 'delete_directory', 'store_image', 'read_datafile', 'next_error', 'write_binary_values', 'read_binary_values'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'source_url': 'https://github.com/pymeasure/pymeasure/blob/main/pymeasure/instruments/anritsu/anritsuMS464xB.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def update_channels(self, **kwargs):
        return self.call('update_channels', kwargs=kwargs)

    def check_errors(self, **kwargs):
        return self.call('check_errors', kwargs=kwargs)

    def query_event_status_register(self, **kwargs):
        return self.call('query_event_status_register', kwargs=kwargs)

    def return_to_local(self, **kwargs):
        return self.call('return_to_local', kwargs=kwargs)

    def trigger(self, **kwargs):
        return self.call('trigger', kwargs=kwargs)

    def trigger_single(self, **kwargs):
        return self.call('trigger_single', kwargs=kwargs)

    def trigger_continuous(self, **kwargs):
        return self.call('trigger_continuous', kwargs=kwargs)

    def load_data_file(self, **kwargs):
        return self.call('load_data_file', kwargs=kwargs)

    def delete_data_file(self, **kwargs):
        return self.call('delete_data_file', kwargs=kwargs)

    def copy_data_file(self, **kwargs):
        return self.call('copy_data_file', kwargs=kwargs)

    def load_data_file_to_memory(self, **kwargs):
        return self.call('load_data_file_to_memory', kwargs=kwargs)

    def create_directory(self, **kwargs):
        return self.call('create_directory', kwargs=kwargs)

    def delete_directory(self, **kwargs):
        return self.call('delete_directory', kwargs=kwargs)

    def store_image(self, **kwargs):
        return self.call('store_image', kwargs=kwargs)

    def read_datafile(self, **kwargs):
        return self.call('read_datafile', kwargs=kwargs)

    def next_error(self, **kwargs):
        return self.call('next_error', kwargs=kwargs)

    def write_binary_values(self, **kwargs):
        return self.call('write_binary_values', kwargs=kwargs)

    def read_binary_values(self, **kwargs):
        return self.call('read_binary_values', kwargs=kwargs)

