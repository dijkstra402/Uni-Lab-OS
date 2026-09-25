from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentPcoPcoPanda42(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/amsikking__pco_panda42', 'source_file': 'pco_panda42.py', 'class_name': 'Camera', 'import_roots': [], 'candidate_methods': ['apply_settings', 'record_to_memory', 'close'], 'action_targets': {}, 'metadata': {'repo': 'amsikking/pco_panda42', 'repo_url': 'https://github.com/amsikking/pco_panda42', 'brand': 'PCO', 'model': 'pco.panda 4.2', 'device_type_cn': 'sCMOS相机', 'device_type_en': 'sCMOS Camera', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 90, 'parse_status': 'ok', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def apply_settings(self, **kwargs):
        return self.call('apply_settings', kwargs=kwargs)

    def record_to_memory(self, **kwargs):
        return self.call('record_to_memory', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

