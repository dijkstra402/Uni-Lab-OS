from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHamiltonMl6002(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/automatedchemistry__flowchem', 'source_file': 'src/flowchem/devices/hamilton/ml600.py', 'class_name': 'ML600', 'import_roots': ['src'], 'candidate_methods': ['inspect_valve_argument', 'from_config', 'get_return_steps', 'set_return_steps', 'initialize', 'send_command_and_read_reply', 'initialize_valve', 'initialize_syringe', 'get_current_volume', 'set_to_volume', 'pause', 'resume', 'stop', 'get_pump_status', 'get_valve_status', 'system_status', 'general_status_info', 'wait_until_idle', 'is_idle', 'is_single_syringe', 'version', 'get_valve_angle', 'set_valve_angle', 'get_valve_position_by_name', 'set_valve_position_by_name', 'get_raw_position', 'set_raw_position', 'send_multiple_commands', 'set_to_volume_dual_syringes', 'repeated_task', 'get_device_info'], 'action_targets': {}, 'metadata': {'repo': 'automatedchemistry/flowchem', 'repo_url': 'https://github.com/automatedchemistry/flowchem', 'brand': 'Hamilton', 'model': 'ML600', 'device_type_cn': '移液工作站', 'device_type_en': 'Liquid Handling Workstation', 'source_framework': 'flowchem', 'tag_id': '4436', 'tag_name': '移液工作站', 'tag_name_en': 'Liquid Handling Workstation', 'candidate_score': 328, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def inspect_valve_argument(self, **kwargs):
        return self.call('inspect_valve_argument', kwargs=kwargs)

    def from_config(self, **kwargs):
        return self.call('from_config', kwargs=kwargs)

    def get_return_steps(self, **kwargs):
        return self.call('get_return_steps', kwargs=kwargs)

    def set_return_steps(self, **kwargs):
        return self.call('set_return_steps', kwargs=kwargs)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def send_command_and_read_reply(self, **kwargs):
        return self.call('send_command_and_read_reply', kwargs=kwargs)

    def initialize_valve(self, **kwargs):
        return self.call('initialize_valve', kwargs=kwargs)

    def initialize_syringe(self, **kwargs):
        return self.call('initialize_syringe', kwargs=kwargs)

    def get_current_volume(self, **kwargs):
        return self.call('get_current_volume', kwargs=kwargs)

    def set_to_volume(self, **kwargs):
        return self.call('set_to_volume', kwargs=kwargs)

    def pause(self, **kwargs):
        return self.call('pause', kwargs=kwargs)

    def resume(self, **kwargs):
        return self.call('resume', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def get_pump_status(self, **kwargs):
        return self.call('get_pump_status', kwargs=kwargs)

    def get_valve_status(self, **kwargs):
        return self.call('get_valve_status', kwargs=kwargs)

    def system_status(self, **kwargs):
        return self.call('system_status', kwargs=kwargs)

    def general_status_info(self, **kwargs):
        return self.call('general_status_info', kwargs=kwargs)

    def wait_until_idle(self, **kwargs):
        return self.call('wait_until_idle', kwargs=kwargs)

    def is_idle(self, **kwargs):
        return self.call('is_idle', kwargs=kwargs)

    def is_single_syringe(self, **kwargs):
        return self.call('is_single_syringe', kwargs=kwargs)

    def version(self, **kwargs):
        return self.call('version', kwargs=kwargs)

    def get_valve_angle(self, **kwargs):
        return self.call('get_valve_angle', kwargs=kwargs)

    def set_valve_angle(self, **kwargs):
        return self.call('set_valve_angle', kwargs=kwargs)

    def get_valve_position_by_name(self, **kwargs):
        return self.call('get_valve_position_by_name', kwargs=kwargs)

    def set_valve_position_by_name(self, **kwargs):
        return self.call('set_valve_position_by_name', kwargs=kwargs)

    def get_raw_position(self, **kwargs):
        return self.call('get_raw_position', kwargs=kwargs)

    def set_raw_position(self, **kwargs):
        return self.call('set_raw_position', kwargs=kwargs)

    def send_multiple_commands(self, **kwargs):
        return self.call('send_multiple_commands', kwargs=kwargs)

    def set_to_volume_dual_syringes(self, **kwargs):
        return self.call('set_to_volume_dual_syringes', kwargs=kwargs)

    def repeated_task(self, **kwargs):
        return self.call('repeated_task', kwargs=kwargs)

    def get_device_info(self, **kwargs):
        return self.call('get_device_info', kwargs=kwargs)

