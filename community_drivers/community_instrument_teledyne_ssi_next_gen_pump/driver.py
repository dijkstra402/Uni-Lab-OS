from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentTeledyneSsiNextGenPump(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/biocatiit__beamline-control-user', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'biocatiit/beamline-control-user', 'repo_url': 'https://github.com/biocatiit/beamline-control-user', 'brand': 'Teledyne SSI', 'model': 'Next Gen Pump', 'device_type_cn': 'HPLC泵', 'device_type_en': 'HPLC Pump', 'source_framework': 'BioCAT', 'tag_id': '4370', 'tag_name': '凝胶渗透色谱仪', 'tag_name_en': 'Gel Permeation Chromatograph', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


