from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentUniversalRobotsUrAdSdl(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AD-SDL__ur_module', 'source_file': 'src/ur_interface/ur_tools/pipette_driver.py', 'class_name': 'PipetteDriver', 'import_roots': ['src'], 'candidate_methods': ['get_step', 'get_step_percent', 'get_volume', 'get_speed_start', 'get_speed_start_percent', 'get_speed', 'get_speed_percent', 'get_speed_stop', 'get_max_homing_steps', 'get_speed_stop_percent', 'get_dead_volume', 'get_backlash', 'get_dead_volume2', 'get_hold_current', 'get_run_current', 'get_parameter', 'initialize', 'set_speed', 'set_motorcurrent', 'set_step', 'dispense', 'aspirate', 'stop', 'move', 'connect', 'reconnect', 'disconnect', 'var_test', 'get_status', 'query', 'send_command'], 'action_targets': {}, 'metadata': {'repo': 'AD-SDL/ur_module', 'repo_url': 'https://github.com/AD-SDL/ur_module', 'brand': 'Universal Robots', 'model': 'UR (AD-SDL)', 'device_type_cn': '协作机械臂', 'device_type_en': 'Collaborative Robot', 'source_framework': 'AD-SDL', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 286, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_step(self, **kwargs):
        return self.call('get_step', kwargs=kwargs)

    def get_step_percent(self, **kwargs):
        return self.call('get_step_percent', kwargs=kwargs)

    def get_volume(self, **kwargs):
        return self.call('get_volume', kwargs=kwargs)

    def get_speed_start(self, **kwargs):
        return self.call('get_speed_start', kwargs=kwargs)

    def get_speed_start_percent(self, **kwargs):
        return self.call('get_speed_start_percent', kwargs=kwargs)

    def get_speed(self, **kwargs):
        return self.call('get_speed', kwargs=kwargs)

    def get_speed_percent(self, **kwargs):
        return self.call('get_speed_percent', kwargs=kwargs)

    def get_speed_stop(self, **kwargs):
        return self.call('get_speed_stop', kwargs=kwargs)

    def get_max_homing_steps(self, **kwargs):
        return self.call('get_max_homing_steps', kwargs=kwargs)

    def get_speed_stop_percent(self, **kwargs):
        return self.call('get_speed_stop_percent', kwargs=kwargs)

    def get_dead_volume(self, **kwargs):
        return self.call('get_dead_volume', kwargs=kwargs)

    def get_backlash(self, **kwargs):
        return self.call('get_backlash', kwargs=kwargs)

    def get_dead_volume2(self, **kwargs):
        return self.call('get_dead_volume2', kwargs=kwargs)

    def get_hold_current(self, **kwargs):
        return self.call('get_hold_current', kwargs=kwargs)

    def get_run_current(self, **kwargs):
        return self.call('get_run_current', kwargs=kwargs)

    def get_parameter(self, **kwargs):
        return self.call('get_parameter', kwargs=kwargs)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

    def set_motorcurrent(self, **kwargs):
        return self.call('set_motorcurrent', kwargs=kwargs)

    def set_step(self, **kwargs):
        return self.call('set_step', kwargs=kwargs)

    def dispense(self, **kwargs):
        return self.call('dispense', kwargs=kwargs)

    def aspirate(self, **kwargs):
        return self.call('aspirate', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def move(self, **kwargs):
        return self.call('move', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def reconnect(self, **kwargs):
        return self.call('reconnect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def var_test(self, **kwargs):
        return self.call('var_test', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def query(self, **kwargs):
        return self.call('query', kwargs=kwargs)

    def send_command(self, **kwargs):
        return self.call('send_command', kwargs=kwargs)

