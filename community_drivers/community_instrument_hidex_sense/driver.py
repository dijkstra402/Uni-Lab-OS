from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHidexSense(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AD-SDL__hidex_module', 'source_file': 'src/hidex_rest_node.py', 'class_name': '', 'import_roots': ['src'], 'candidate_methods': ['test_node_startup', 'state_handler', 'run_assay', 'cancel', 'shutdown'], 'action_targets': {'test_node_startup': 'test_node_startup', 'state_handler': 'state_handler', 'run_assay': 'run_assay', 'cancel': 'cancel', 'shutdown': 'shutdown'}, 'metadata': {'repo': 'AD-SDL/hidex_module', 'repo_url': 'https://github.com/AD-SDL/hidex_module', 'brand': 'Hidex', 'model': 'Sense', 'device_type_cn': '酶标仪', 'device_type_en': 'Plate Reader', 'source_framework': '生命科学', 'tag_id': '4457', 'tag_name': '酶标仪', 'tag_name_en': 'Microplate Reader', 'candidate_score': 55, 'parse_status': 'module_selected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'test_node_startup': 'test_node_startup', 'state_handler': 'state_handler', 'run_assay': 'run_assay', 'cancel': 'cancel', 'shutdown': 'shutdown'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def test_node_startup(self, **kwargs):
        return self.call('test_node_startup', kwargs=kwargs)

    def state_handler(self, **kwargs):
        return self.call('state_handler', kwargs=kwargs)

    def run_assay(self, **kwargs):
        return self.call('run_assay', kwargs=kwargs)

    def cancel(self, **kwargs):
        return self.call('cancel', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

