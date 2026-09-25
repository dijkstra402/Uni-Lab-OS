from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBiotekElx405(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/stefangolas__Equipment_Integrations', 'source_file': 'ELx405_Washer.py', 'class_name': 'ELx405_Washer', 'import_roots': [], 'candidate_methods': ['initialize', 'run_protocol', 'load_protocol_from_file', 'load_protocol_from_flash', 'pause_protocol', 'run_verify_manifold_test', 'get_verify_manifold_status'], 'action_targets': {}, 'metadata': {'repo': 'stefangolas/Equipment_Integrations', 'repo_url': 'https://github.com/stefangolas/Equipment_Integrations', 'brand': 'BioTek', 'model': 'ELx405', 'device_type_cn': '洗板机', 'device_type_en': 'Microplate Washer', 'source_framework': '专用驱动', 'tag_id': '4414', 'tag_name': '洗板机', 'tag_name_en': 'Microplate Washer', 'candidate_score': 156, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def run_protocol(self, **kwargs):
        return self.call('run_protocol', kwargs=kwargs)

    def load_protocol_from_file(self, **kwargs):
        return self.call('load_protocol_from_file', kwargs=kwargs)

    def load_protocol_from_flash(self, **kwargs):
        return self.call('load_protocol_from_flash', kwargs=kwargs)

    def pause_protocol(self, **kwargs):
        return self.call('pause_protocol', kwargs=kwargs)

    def run_verify_manifold_test(self, **kwargs):
        return self.call('run_verify_manifold_test', kwargs=kwargs)

    def get_verify_manifold_status(self, **kwargs):
        return self.call('get_verify_manifold_status', kwargs=kwargs)

