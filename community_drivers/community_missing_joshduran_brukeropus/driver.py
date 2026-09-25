from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingJoshduranBrukeropus(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/joshduran__brukeropus', 'source_file': 'brukeropus/control/opus.py', 'class_name': 'Opus', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'raw_query', 'parse_response', '_parse_error', 'query', 'close_opus', 'get_param_label', 'get_param_options', 'get_version', 'get_opus_path', 'send_command', 'evacuate_sample', 'vent_sample', 'close_flaps', 'open_flaps', 'unload_file', 'unload_all', 'measure_ref', 'measure_sample', 'check_signal', 'save_ref', '_param_str', '__bool__', '__init__'], 'metadata': {'repo': 'joshduran/brukeropus', 'repo_url': 'https://github.com/joshduran/brukeropus', 'review_status': 'good', 'review_notes': ['测量流程方法完整。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def raw_query(self, **kwargs):
        return self.call('raw_query', kwargs=kwargs)

    def parse_response(self, **kwargs):
        return self.call('parse_response', kwargs=kwargs)

    def parse_error(self, **kwargs):
        return self.call('_parse_error', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def close_opus(self, **kwargs):
        return self.call('close_opus', kwargs=kwargs)

    def get_param_label(self, **kwargs):
        return self.call('get_param_label', kwargs=kwargs)

    def get_param_options(self, **kwargs):
        return self.call('get_param_options', kwargs=kwargs)

    def get_version(self, **kwargs):
        return self.call('get_version', kwargs=kwargs)

    def get_opus_path(self, **kwargs):
        return self.call('get_opus_path', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def evacuate_sample(self, **kwargs):
        return self.call('evacuate_sample', kwargs=kwargs)

    def vent_sample(self, **kwargs):
        return self.call('vent_sample', kwargs=kwargs)

    def close_flaps(self, **kwargs):
        return self.call('close_flaps', kwargs=kwargs)

    def open_flaps(self, **kwargs):
        return self.call('open_flaps', kwargs=kwargs)

    def unload_file(self, **kwargs):
        return self.call('unload_file', kwargs=kwargs)

    def unload_all(self, **kwargs):
        return self.call('unload_all', kwargs=kwargs)

    def measure_ref(self, **kwargs):
        return self.call('measure_ref', kwargs=kwargs)

    def measure_sample(self, **kwargs):
        return self.call('measure_sample', kwargs=kwargs)

    def check_signal(self, **kwargs):
        return self.call('check_signal', kwargs=kwargs)

    def save_ref(self, **kwargs):
        return self.call('save_ref', kwargs=kwargs)

    def param_str(self, **kwargs):
        return self.call('_param_str', kwargs=kwargs)

    def bool(self, **kwargs):
        return self.call('__bool__', kwargs=kwargs)

    def init(self, **kwargs):
        return self.call('__init__', kwargs=kwargs)

