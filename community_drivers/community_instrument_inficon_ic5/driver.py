from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentInficonIc5(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/MChenFK__Inficon-IC5', 'source_file': 'virtual_serial_test/command_test.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['send_command', 'send_command_2'], 'action_targets': {'send_command': 'send_command', 'send_command_2': 'send_command_2'}, 'metadata': {'repo': 'MChenFK/Inficon-IC5', 'repo_url': 'https://github.com/MChenFK/Inficon-IC5', 'brand': 'Inficon', 'model': 'IC5', 'device_type_cn': '蒸镀仪', 'device_type_en': 'Evaporation Coater', 'source_framework': '专用驱动', 'tag_id': '4449', 'tag_name': '蒸镀仪', 'tag_name_en': 'Evaporation Coater', 'candidate_score': 14, 'parse_status': 'module_selected', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {'send_command': 'send_command', 'send_command_2': 'send_command_2'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

    def send_command_2(self, **kwargs):
        return self.call('send_command_2', kwargs=kwargs)

