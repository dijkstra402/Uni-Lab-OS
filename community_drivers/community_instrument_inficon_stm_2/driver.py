from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentInficonStm2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Mizuho-NAGATA__STM2-remote', 'source_file': 'STM2-remote-monitor.py', 'class_name': 'STM2LoggerGUI', 'import_roots': [], 'candidate_methods': ['build_gui', 'update_material_fields', 'browse_file', 'drop_file', 'start_logging', 'stop_logging', 'update_status', 'run'], 'action_targets': {}, 'metadata': {'repo': 'Mizuho-NAGATA/STM2-remote', 'repo_url': 'https://github.com/Mizuho-NAGATA/STM2-remote', 'brand': 'Inficon', 'model': 'STM-2', 'device_type_cn': '蒸镀仪', 'device_type_en': 'Evaporation Coater', 'source_framework': '专用驱动', 'tag_id': '4449', 'tag_name': '蒸镀仪', 'tag_name_en': 'Evaporation Coater', 'candidate_score': 142, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def build_gui(self, **kwargs):
        return self.call('build_gui', kwargs=kwargs)

    def update_material_fields(self, **kwargs):
        return self.call('update_material_fields', kwargs=kwargs)

    def browse_file(self, **kwargs):
        return self.call('browse_file', kwargs=kwargs)

    def drop_file(self, **kwargs):
        return self.call('drop_file', kwargs=kwargs)

    def start_logging(self, **kwargs):
        return self.call('start_logging', kwargs=kwargs)

    def stop_logging(self, **kwargs):
        return self.call('stop_logging', kwargs=kwargs)

    def update_status(self, **kwargs):
        return self.call('update_status', kwargs=kwargs)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

