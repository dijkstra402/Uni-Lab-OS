from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingCroningpPycont(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/croningp__pycont', 'source_file': 'pycont/controller.py', 'class_name': 'C3000Controller', 'import_roots': [], 'candidate_methods': ['initialize', 'smart_initialize', 'is_idle', 'is_busy', 'wait_until_idle', 'get_volume', 'current_volume', 'remaining_volume', 'pump', 'deliver', 'transfer', 'get_valve_position', 'set_valve_position', 'go_to_volume', 'go_to_max_volume'], 'metadata': {'repo': 'croningp/pycont', 'repo_url': 'https://github.com/croningp/pycont', 'source_file': 'pycont/controller.py', 'candidate_score': 152, 'candidate_reason': '', 'manufacturers': ['Tricontinent/Tecan'], 'models': ['C3000系列注射泵'], 'tags': ['柱塞泵'], 'notes': ['Glasgow大学Cronin实验室'], 'comm_protocols': ['RS-485 pyserial 9600'], 'review_status': 'good', 'review_notes': ['改选 C3000Controller，覆盖 Tricontinent C3000 泵完整控制接口。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)


    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def smart_initialize(self, **kwargs):
        return self.call('smart_initialize', kwargs=kwargs)

    def is_idle(self, **kwargs):
        return self.call('is_idle', kwargs=kwargs)

    def is_busy(self, **kwargs):
        return self.call('is_busy', kwargs=kwargs)

    def wait_until_idle(self, **kwargs):
        return self.call('wait_until_idle', kwargs=kwargs)

    def get_volume(self, **kwargs):
        return self.call('get_volume', kwargs=kwargs)

    def current_volume(self, **kwargs):
        return self.call('current_volume', kwargs=kwargs)

    def remaining_volume(self, **kwargs):
        return self.call('remaining_volume', kwargs=kwargs)

    def pump(self, **kwargs):
        return self.call('pump', kwargs=kwargs)

    def deliver(self, **kwargs):
        return self.call('deliver', kwargs=kwargs)

    def transfer(self, **kwargs):
        return self.call('transfer', kwargs=kwargs)

    def get_valve_position(self, **kwargs):
        return self.call('get_valve_position', kwargs=kwargs)

    def set_valve_position(self, **kwargs):
        return self.call('set_valve_position', kwargs=kwargs)

    def go_to_volume(self, **kwargs):
        return self.call('go_to_volume', kwargs=kwargs)

    def go_to_max_volume(self, **kwargs):
        return self.call('go_to_max_volume', kwargs=kwargs)

