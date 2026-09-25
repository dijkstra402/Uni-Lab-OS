from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBiotekSynergyH1m(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/bowmanlab__plate_reader', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'bowmanlab/plate_reader', 'repo_url': 'https://github.com/bowmanlab/plate_reader', 'brand': 'BioTek', 'model': 'Synergy H1M', 'device_type_cn': '酶标仪', 'device_type_en': 'Plate Reader', 'source_framework': '生命科学', 'tag_id': '4457', 'tag_name': '酶标仪', 'tag_name_en': 'Microplate Reader', 'candidate_score': -999, 'parse_status': 'class_not_found', 'quality_status': 'broken', 'quality_reasons': ['no_class_found'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


