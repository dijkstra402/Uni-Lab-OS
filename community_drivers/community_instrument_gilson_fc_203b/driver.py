from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentGilsonFc203b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/MechWolf__MechWolf', 'source_file': 'mechwolf/core/protocol.py', 'class_name': 'Protocol', 'import_roots': [], 'candidate_methods': ['add', 'to_dict', 'to_list', 'yaml', 'json', 'visualize', 'execute'], 'action_targets': {}, 'metadata': {'repo': 'MechWolf/MechWolf', 'repo_url': 'https://github.com/MechWolf/MechWolf', 'brand': 'Gilson', 'model': 'FC 203B', 'device_type_cn': '馏分收集器', 'device_type_en': 'Fraction Collector', 'source_framework': 'MechWolf', 'tag_id': '4371', 'tag_name': '制备色谱仪', 'tag_name_en': 'Preparative Chromatograph', 'candidate_score': 94, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def add(self, **kwargs):
        return self.call('add', kwargs=kwargs)

    def to_dict(self, **kwargs):
        return self.call('to_dict', kwargs=kwargs)

    def to_list(self, **kwargs):
        return self.call('to_list', kwargs=kwargs)

    def yaml(self, **kwargs):
        return self.call('yaml', kwargs=kwargs)

    def json(self, **kwargs):
        return self.call('json', kwargs=kwargs)

    def visualize(self, **kwargs):
        return self.call('visualize', kwargs=kwargs)

    def execute(self, **kwargs):
        return self.call('execute', kwargs=kwargs)

