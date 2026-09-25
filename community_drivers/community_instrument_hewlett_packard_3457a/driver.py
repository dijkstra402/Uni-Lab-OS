from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHewlettPackard3457a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/SweepMe__instrument-drivers', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'SweepMe/instrument-drivers', 'repo_url': 'https://github.com/SweepMe/instrument-drivers', 'brand': 'Hewlett-Packard', 'model': '3457A', 'device_type_cn': '万用表', 'device_type_en': 'Multimeter', 'source_framework': 'SweepMe', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


