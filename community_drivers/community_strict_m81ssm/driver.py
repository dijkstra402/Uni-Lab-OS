from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictM81ssm(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Lakeshore/M81_SSM.py', 'class_name': 'M81_SSM', 'import_roots': ['src'], 'candidate_methods': ['show_system_info', 'stream_data', 'close', 'get_keypad_lock', 'set_keypad_lock'], 'action_targets': {'get_keypad_lock': '__qcodes_param_get__keypad_lock', 'set_keypad_lock': '__qcodes_param_set__keypad_lock'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Lakeshore/M81_SSM.py', 'confidence': 0.8, 'quality_score': 0.88, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_keypad_lock': '__qcodes_param_get__keypad_lock', 'set_keypad_lock': '__qcodes_param_set__keypad_lock'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def show_system_info(self, **kwargs):
        return self.call('show_system_info', kwargs=kwargs)

    def stream_data(self, **kwargs):
        return self.call('stream_data', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def get_keypad_lock(self, **kwargs):
        return self.call('get_keypad_lock', kwargs=kwargs)

    def set_keypad_lock(self, **kwargs):
        return self.call('set_keypad_lock', kwargs=kwargs)

