from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHarvardApparatusPhdUltra(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Fluids-and-Surfaces-Group__Harvard-Apparatus-PHD-Ultra-Syringe-pump-control', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'Fluids-and-Surfaces-Group/Harvard-Apparatus-PHD-Ultra-Syringe-pump-control', 'repo_url': 'https://github.com/Fluids-and-Surfaces-Group/Harvard-Apparatus-PHD-Ultra-Syringe-pump-control', 'brand': 'Harvard Apparatus', 'model': 'PHD Ultra', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': '专用驱动', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': -999, 'parse_status': 'class_not_found', 'quality_status': 'broken', 'quality_reasons': ['no_class_found'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


