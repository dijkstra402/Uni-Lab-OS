from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentVapourtecR2Uv150(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/automatedchemistry__flowchem', 'source_file': 'src/flowchem/devices/knauer/azura_compact.py', 'class_name': 'AzuraCompact', 'import_roots': ['src'], 'candidate_methods': ['initialize', 'error_present', 'create_and_send_command', 'get_headtype', 'set_headtype', 'get_flow_rate', 'set_flow_rate', 'get_minimum_pressure', 'set_minimum_pressure', 'get_maximum_pressure', 'set_maximum_pressure', 'set_minimum_motor_current', 'is_start_in_required', 'require_start_in', 'is_autostart_enabled', 'enable_autostart', 'get_adjusting_factor', 'set_adjusting_factor', 'get_correction_factor', 'set_correction_factor', 'read_pressure', 'read_extflow', 'read_errors', 'read_motor_current', 'infuse', 'stop', 'is_running', 'set_local', 'remote_control', 'is_analog_control_enabled', 'enable_analog_control', 'repeated_task', 'get_device_info'], 'action_targets': {}, 'metadata': {'repo': 'automatedchemistry/flowchem', 'repo_url': 'https://github.com/automatedchemistry/flowchem', 'brand': 'Vapourtec', 'model': 'R2 UV150模块', 'device_type_cn': '光化学反应器', 'device_type_en': 'Photochemical Reactor', 'source_framework': 'flowchem', 'tag_id': '4368', 'tag_name': '光化学反应器', 'tag_name_en': 'Photochemical Reactor', 'candidate_score': 286, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def error_present(self, **kwargs):
        return self.call('error_present', kwargs=kwargs)

    def create_and_send_command(self, **kwargs):
        return self.call('create_and_send_command', kwargs=kwargs)

    def get_headtype(self, **kwargs):
        return self.call('get_headtype', kwargs=kwargs)

    def set_headtype(self, **kwargs):
        return self.call('set_headtype', kwargs=kwargs)

    def get_flow_rate(self, **kwargs):
        return self.call('get_flow_rate', kwargs=kwargs)

    def set_flow_rate(self, **kwargs):
        return self.call('set_flow_rate', kwargs=kwargs)

    def get_minimum_pressure(self, **kwargs):
        return self.call('get_minimum_pressure', kwargs=kwargs)

    def set_minimum_pressure(self, **kwargs):
        return self.call('set_minimum_pressure', kwargs=kwargs)

    def get_maximum_pressure(self, **kwargs):
        return self.call('get_maximum_pressure', kwargs=kwargs)

    def set_maximum_pressure(self, **kwargs):
        return self.call('set_maximum_pressure', kwargs=kwargs)

    def set_minimum_motor_current(self, **kwargs):
        return self.call('set_minimum_motor_current', kwargs=kwargs)

    def is_start_in_required(self, **kwargs):
        return self.call('is_start_in_required', kwargs=kwargs)

    def require_start_in(self, **kwargs):
        return self.call('require_start_in', kwargs=kwargs)

    def is_autostart_enabled(self, **kwargs):
        return self.call('is_autostart_enabled', kwargs=kwargs)

    def enable_autostart(self, **kwargs):
        return self.call('enable_autostart', kwargs=kwargs)

    def get_adjusting_factor(self, **kwargs):
        return self.call('get_adjusting_factor', kwargs=kwargs)

    def set_adjusting_factor(self, **kwargs):
        return self.call('set_adjusting_factor', kwargs=kwargs)

    def get_correction_factor(self, **kwargs):
        return self.call('get_correction_factor', kwargs=kwargs)

    def set_correction_factor(self, **kwargs):
        return self.call('set_correction_factor', kwargs=kwargs)

    def read_pressure(self, **kwargs):
        return self.call('read_pressure', kwargs=kwargs)

    def read_extflow(self, **kwargs):
        return self.call('read_extflow', kwargs=kwargs)

    def read_errors(self, **kwargs):
        return self.call('read_errors', kwargs=kwargs)

    def read_motor_current(self, **kwargs):
        return self.call('read_motor_current', kwargs=kwargs)

    def infuse(self, **kwargs):
        return self.call('infuse', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def is_running(self, **kwargs):
        return self.call('is_running', kwargs=kwargs)

    def set_local(self, **kwargs):
        return self.call('set_local', kwargs=kwargs)

    def remote_control(self, **kwargs):
        return self.call('remote_control', kwargs=kwargs)

    def is_analog_control_enabled(self, **kwargs):
        return self.call('is_analog_control_enabled', kwargs=kwargs)

    def enable_analog_control(self, **kwargs):
        return self.call('enable_analog_control', kwargs=kwargs)

    def repeated_task(self, **kwargs):
        return self.call('repeated_task', kwargs=kwargs)

    def get_device_info(self, **kwargs):
        return self.call('get_device_info', kwargs=kwargs)

