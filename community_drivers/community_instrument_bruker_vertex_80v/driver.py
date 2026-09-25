from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBrukerVertex80v(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/joshduran__brukeropus', 'source_file': 'brukeropus/control/opus.py', 'class_name': 'Opus', 'import_roots': [], 'candidate_methods': ['connect', 'disconnect', 'raw_query', 'parse_response', 'query', 'close_opus', 'get_param_label', 'get_param_options', 'get_version', 'get_opus_path', 'send_command', 'evacuate_sample', 'vent_sample', 'close_flaps', 'open_flaps', 'unload_file', 'unload_all', 'measure_ref', 'measure_sample', 'check_signal', 'save_ref'], 'action_targets': {}, 'metadata': {'repo': 'joshduran/brukeropus', 'repo_url': 'https://github.com/joshduran/brukeropus', 'brand': 'Bruker', 'model': 'Vertex 80V', 'device_type_cn': 'FTIR光谱仪', 'device_type_en': 'FTIR Spectrometer', 'source_framework': '光谱分析', 'tag_id': '4440', 'tag_name': '红外光谱仪', 'tag_name_en': 'Infrared Spectrometer', 'candidate_score': 214, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

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

