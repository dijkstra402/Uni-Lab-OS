from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentRocheLightcycler480Ii(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Koeng101__lightcycler-demo', 'source_file': 'server/generated/lightcycler_connect.py', 'class_name': 'LightCyclerService', 'import_roots': [], 'candidate_methods': ['get_state', 'get_logs', 'run_experiment', 'get_experiment', 'list_experiments', 'open_door', 'close_door', 'get_door_status'], 'action_targets': {}, 'metadata': {'repo': 'Koeng101/lightcycler-demo', 'repo_url': 'https://github.com/Koeng101/lightcycler-demo', 'brand': 'Roche', 'model': 'LightCycler 480 II', 'device_type_cn': '实时定量PCR仪', 'device_type_en': 'Real-Time qPCR', 'source_framework': '独立驱动', 'tag_id': '4383', 'tag_name': '实时定量PCR仪', 'tag_name_en': 'Real-Time Quantitative PCR', 'candidate_score': 114, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_state(self, **kwargs):
        return self.call('get_state', kwargs=kwargs)

    def get_logs(self, **kwargs):
        return self.call('get_logs', kwargs=kwargs)

    def run_experiment(self, **kwargs):
        return self.call('run_experiment', kwargs=kwargs)

    def get_experiment(self, **kwargs):
        return self.call('get_experiment', kwargs=kwargs)

    def list_experiments(self, **kwargs):
        return self.call('list_experiments', kwargs=kwargs)

    def open_door(self, **kwargs):
        return self.call('open_door', kwargs=kwargs)

    def close_door(self, **kwargs):
        return self.call('close_door', kwargs=kwargs)

    def get_door_status(self, **kwargs):
        return self.call('get_door_status', kwargs=kwargs)

