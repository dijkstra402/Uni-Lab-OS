from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictK10cr1(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/mabuchilab__Instrumental', 'source_file': 'src/instrumental/drivers/motion/_kinesis/isc.py', 'class_name': 'K10CR1', 'import_roots': ['src'], 'candidate_methods': ['close', 'get_info', 'move_to', 'move_relative', 'stop', 'wait_for_move', 'move_finished', 'home', 'wait_for_home', 'homing_finished', 'needs_homing', 'offset', 'backlash', 'position', 'is_homing', 'is_moving', 'get_next_message', 'get_messages', 'get', 'save_instrument', 'observe'], 'action_targets': {}, 'metadata': {'repo': 'mabuchilab/Instrumental', 'repo_url': 'https://github.com/mabuchilab/Instrumental', 'source_url': 'https://github.com/mabuchilab/Instrumental/blob/main/src/instrumental/drivers/motion/_kinesis/isc.py', 'confidence': 0.95, 'quality_score': 1.11, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def get_info(self, **kwargs):
        return self.call('get_info', kwargs=kwargs)

    def move_to(self, **kwargs):
        return self.call('move_to', kwargs=kwargs)

    def move_relative(self, **kwargs):
        return self.call('move_relative', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def wait_for_move(self, **kwargs):
        return self.call('wait_for_move', kwargs=kwargs)

    def move_finished(self, **kwargs):
        return self.call('move_finished', kwargs=kwargs)

    def home(self, **kwargs):
        return self.call('home', kwargs=kwargs)

    def wait_for_home(self, **kwargs):
        return self.call('wait_for_home', kwargs=kwargs)

    def homing_finished(self, **kwargs):
        return self.call('homing_finished', kwargs=kwargs)

    def needs_homing(self, **kwargs):
        return self.call('needs_homing', kwargs=kwargs)

    def offset(self, **kwargs):
        return self.call('offset', kwargs=kwargs)

    def backlash(self, **kwargs):
        return self.call('backlash', kwargs=kwargs)

    def position(self, **kwargs):
        return self.call('position', kwargs=kwargs)

    def is_homing(self, **kwargs):
        return self.call('is_homing', kwargs=kwargs)

    def is_moving(self, **kwargs):
        return self.call('is_moving', kwargs=kwargs)

    def get_next_message(self, **kwargs):
        return self.call('get_next_message', kwargs=kwargs)

    def get_messages(self, **kwargs):
        return self.call('get_messages', kwargs=kwargs)

    def get(self, **kwargs):
        return self.call('get', kwargs=kwargs)

    def save_instrument(self, **kwargs):
        return self.call('save_instrument', kwargs=kwargs)

    def observe(self, **kwargs):
        return self.call('observe', kwargs=kwargs)

