from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentNionUltrastem(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/nion-software__nionswift-instrumentation-kit', 'source_file': '', 'class_name': '', 'import_roots': [], 'candidate_methods': [], 'action_targets': {}, 'metadata': {'repo': 'nion-software/nionswift-instrumentation-kit', 'repo_url': 'https://github.com/nion-software/nionswift-instrumentation-kit', 'brand': 'Nion', 'model': 'UltraSTEM', 'device_type_cn': '透射电子显微镜', 'device_type_en': 'TEM', 'source_framework': 'nionswift', 'tag_id': '4456', 'tag_name': '透射电子显微镜', 'tag_name_en': 'Transmission Electron Microscope', 'candidate_score': -999.0, 'parse_status': 'repo_download_failed', 'quality_status': 'broken', 'quality_reasons': ['repo_download_failed'], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


