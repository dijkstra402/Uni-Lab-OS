from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentChemspeedFlexIsynth(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/aspuru-guzik-group__chemspyd', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'aspuru-guzik-group/chemspyd', 'repo_url': 'https://github.com/aspuru-guzik-group/chemspyd', 'brand': 'Chemspeed', 'model': 'FLEX/iSynth', 'device_type_cn': '并行反应仪', 'device_type_en': 'Parallel Reactor', 'source_framework': 'Chemspyd', 'tag_id': '4385', 'tag_name': '并行反应仪', 'tag_name_en': 'Parallel Reactor', 'candidate_score': -999, 'parse_status': 'class_not_found', 'quality_status': 'broken', 'quality_reasons': ['no_class_found'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


