from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBostonMicromachinesMultiDmKiloC(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/jacopoantonello__devwraps', 'source_file': 'devwraps/dll_finder.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['find_file', 'remove_dlls', 'get_root_folder', 'look_for_dlls', 'dll_lookup_ximea', 'dll_lookup_asdk', 'dll_lookup_mirao52e', 'dll_lookup_bmc', 'dll_lookup_thorcam', 'dll_lookup_ueye', 'dll_lookup_sdk3'], 'action_targets': {'find_file': 'find_file', 'remove_dlls': 'remove_dlls', 'get_root_folder': 'get_root_folder', 'look_for_dlls': 'look_for_dlls', 'dll_lookup_ximea': 'dll_lookup_ximea', 'dll_lookup_asdk': 'dll_lookup_asdk', 'dll_lookup_mirao52e': 'dll_lookup_mirao52e', 'dll_lookup_bmc': 'dll_lookup_bmc', 'dll_lookup_thorcam': 'dll_lookup_thorcam', 'dll_lookup_ueye': 'dll_lookup_ueye', 'dll_lookup_sdk3': 'dll_lookup_sdk3'}, 'metadata': {'repo': 'jacopoantonello/devwraps', 'repo_url': 'https://github.com/jacopoantonello/devwraps', 'brand': 'Boston Micromachines', 'model': 'Multi-DM/Kilo-C', 'device_type_cn': '变形镜', 'device_type_en': 'Deformable Mirror', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 85, 'parse_status': 'module_selected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'find_file': 'find_file', 'remove_dlls': 'remove_dlls', 'get_root_folder': 'get_root_folder', 'look_for_dlls': 'look_for_dlls', 'dll_lookup_ximea': 'dll_lookup_ximea', 'dll_lookup_asdk': 'dll_lookup_asdk', 'dll_lookup_mirao52e': 'dll_lookup_mirao52e', 'dll_lookup_bmc': 'dll_lookup_bmc', 'dll_lookup_thorcam': 'dll_lookup_thorcam', 'dll_lookup_ueye': 'dll_lookup_ueye', 'dll_lookup_sdk3': 'dll_lookup_sdk3'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def find_file(self, **kwargs):
        return self.call('find_file', kwargs=kwargs)

    def remove_dlls(self, **kwargs):
        return self.call('remove_dlls', kwargs=kwargs)

    def get_root_folder(self, **kwargs):
        return self.call('get_root_folder', kwargs=kwargs)

    def look_for_dlls(self, **kwargs):
        return self.call('look_for_dlls', kwargs=kwargs)

    def dll_lookup_ximea(self, **kwargs):
        return self.call('dll_lookup_ximea', kwargs=kwargs)

    def dll_lookup_asdk(self, **kwargs):
        return self.call('dll_lookup_asdk', kwargs=kwargs)

    def dll_lookup_mirao52e(self, **kwargs):
        return self.call('dll_lookup_mirao52e', kwargs=kwargs)

    def dll_lookup_bmc(self, **kwargs):
        return self.call('dll_lookup_bmc', kwargs=kwargs)

    def dll_lookup_thorcam(self, **kwargs):
        return self.call('dll_lookup_thorcam', kwargs=kwargs)

    def dll_lookup_ueye(self, **kwargs):
        return self.call('dll_lookup_ueye', kwargs=kwargs)

    def dll_lookup_sdk3(self, **kwargs):
        return self.call('dll_lookup_sdk3', kwargs=kwargs)

