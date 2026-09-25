from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLinkamTms94(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AndreEbel__PyLinkam', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'AndreEbel/PyLinkam', 'repo_url': 'https://github.com/AndreEbel/PyLinkam', 'brand': 'Linkam', 'model': 'TMS94', 'device_type_cn': '温度控制台(DSC联用)', 'device_type_en': 'Temperature Controller (DSC)', 'source_framework': 'PyLinkam', 'tag_id': '4433', 'tag_name': '示差扫描量热仪', 'tag_name_en': 'Differential Scanning Calorimeter', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


