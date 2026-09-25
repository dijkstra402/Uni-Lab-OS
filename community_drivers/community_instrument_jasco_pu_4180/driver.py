from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentJascoPu4180(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/ISISComputingGroup__IBEX', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'ISISComputingGroup/IBEX', 'repo_url': 'https://github.com/ISISComputingGroup/IBEX', 'brand': 'JASCO', 'model': 'PU-4180', 'device_type_cn': 'HPLC泵', 'device_type_en': 'HPLC Pump', 'source_framework': '色谱/质谱', 'tag_id': '4403', 'tag_name': '柱塞泵', 'tag_name_en': 'Plunger Pump', 'candidate_score': -999, 'parse_status': 'class_not_found', 'quality_status': 'broken', 'quality_reasons': ['no_class_found'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


