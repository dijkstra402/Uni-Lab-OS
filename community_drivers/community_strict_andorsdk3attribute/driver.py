from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAndorsdk3attribute(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/AlexShkarin__pyLabLib', 'source_file': 'pylablib/devices/Andor/AndorSDK3.py', 'class_name': 'AndorSDK3Attribute', 'import_roots': [], 'candidate_methods': ['update_properties', 'get_value', 'set_value', 'call_command', 'get_range', 'update_limits', 'truncate_value'], 'action_targets': {}, 'metadata': {'repo': 'AlexShkarin/pyLabLib', 'repo_url': 'https://github.com/AlexShkarin/pyLabLib', 'source_url': 'https://github.com/AlexShkarin/pyLabLib/blob/main/pylablib/devices/Andor/AndorSDK3.py', 'confidence': 0.75, 'quality_score': 0.83, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def update_properties(self, **kwargs):
        return self.call('update_properties', kwargs=kwargs)

    def get_value(self, **kwargs):
        return self.call('get_value', kwargs=kwargs)

    def set_value(self, **kwargs):
        return self.call('set_value', kwargs=kwargs)

    def call_command(self, **kwargs):
        return self.call('call_command', kwargs=kwargs)

    def get_range(self, **kwargs):
        return self.call('get_range', kwargs=kwargs)

    def update_limits(self, **kwargs):
        return self.call('update_limits', kwargs=kwargs)

    def truncate_value(self, **kwargs):
        return self.call('truncate_value', kwargs=kwargs)

