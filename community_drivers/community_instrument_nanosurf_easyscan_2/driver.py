from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentNanosurfEasyscan2(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/levylabpitt__NanosurfES2Py', 'source_file': 'nid_analyze/nid_analyze.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['load_nid_image', 'plane_level_image'], 'action_targets': {'load_nid_image': 'load_nid_image', 'plane_level_image': 'plane_level_image'}, 'metadata': {'repo': 'levylabpitt/NanosurfES2Py', 'repo_url': 'https://github.com/levylabpitt/NanosurfES2Py', 'brand': 'Nanosurf', 'model': 'EasyScan 2', 'device_type_cn': 'AFM', 'device_type_en': 'Atomic Force Microscope', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 14, 'parse_status': 'module_selected', 'quality_status': 'thin', 'quality_reasons': [], 'action_targets': {'load_nid_image': 'load_nid_image', 'plane_level_image': 'plane_level_image'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def load_nid_image(self, **kwargs):
        return self.call('load_nid_image', kwargs=kwargs)

    def plane_level_image(self, **kwargs):
        return self.call('plane_level_image', kwargs=kwargs)

