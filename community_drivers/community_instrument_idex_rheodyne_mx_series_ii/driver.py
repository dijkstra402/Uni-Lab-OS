from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIdexRheodyneMxSeriesIi(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/linnarsson-lab__MXII-valve', 'source_file': 'MXII_valve.py', 'class_name': 'MX_valve', 'import_roots': [], 'candidate_methods': ['stripped_hex', 'wait_ready', 'message_builder', 'read_message', 'write_message', 'response_interpret', 'get_port', 'change_port'], 'action_targets': {}, 'metadata': {'repo': 'linnarsson-lab/MXII-valve', 'repo_url': 'https://github.com/linnarsson-lab/MXII-valve', 'brand': 'IDEX (Rheodyne)', 'model': 'MX Series II', 'device_type_cn': '电动多位阀', 'device_type_en': 'Motorized Multi-Position Valve', 'source_framework': '泵阀/液体处理', 'tag_id': '4382', 'tag_name': '多通阀', 'tag_name_en': 'Multi-Port Valve', 'candidate_score': 122, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def stripped_hex(self, **kwargs):
        return self.call('stripped_hex', kwargs=kwargs)

    def wait_ready(self, **kwargs):
        return self.call('wait_ready', kwargs=kwargs)

    def message_builder(self, **kwargs):
        return self.call('message_builder', kwargs=kwargs)

    def read_message(self, **kwargs):
        return self.call('read_message', kwargs=kwargs)

    def write_message(self, **kwargs):
        return self.call('write_message', kwargs=kwargs)

    def response_interpret(self, **kwargs):
        return self.call('response_interpret', kwargs=kwargs)

    def get_port(self, **kwargs):
        return self.call('get_port', kwargs=kwargs)

    def change_port(self, **kwargs):
        return self.call('change_port', kwargs=kwargs)

