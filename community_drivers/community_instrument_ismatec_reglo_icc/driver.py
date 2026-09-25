from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIsmatecRegloIcc(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/numat__ismatec', 'source_file': 'ismatec/driver.py', 'class_name': 'Pump', 'import_roots': [], 'candidate_methods': ['get_pump_version', 'get_serial_protocol_version', 'set_flow_rate', 'get_flow_rate', 'is_running', 'get_mode', 'set_mode', 'get_channels', 'get_tubing_inner_diameter', 'set_tubing_inner_diameter', 'get_speed', 'set_speed', 'get_runtime', 'set_runtime', 'get_volume_setpoint', 'set_volume_setpoint', 'get_rotation', 'set_rotation', 'get_setpoint_type', 'set_setpoint_type', 'get_max_flow_rate', 'get_run_failure_reason', 'has_channel_addressing', 'set_channel_addressing', 'has_event_messaging', 'set_event_messaging', 'reset_default_settings', 'continuous_flow', 'dispense_vol_at_rate', 'dispense_vol_over_time', 'dispense_flow_over_time', 'start', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'numat/ismatec', 'repo_url': 'https://github.com/numat/ismatec', 'brand': 'Ismatec', 'model': 'Reglo ICC', 'device_type_cn': '蠕动泵', 'device_type_en': 'Peristaltic Pump', 'source_framework': '泵阀/液体处理', 'tag_id': '4451', 'tag_name': '蠕动泵', 'tag_name_en': 'Peristaltic Pump', 'candidate_score': 322, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_pump_version(self, **kwargs):
        return self.call('get_pump_version', kwargs=kwargs)

    def get_serial_protocol_version(self, **kwargs):
        return self.call('get_serial_protocol_version', kwargs=kwargs)

    def set_flow_rate(self, **kwargs):
        return self.call('set_flow_rate', kwargs=kwargs)

    def get_flow_rate(self, **kwargs):
        return self.call('get_flow_rate', kwargs=kwargs)

    def is_running(self, **kwargs):
        return self.call('is_running', kwargs=kwargs)

    def get_mode(self, **kwargs):
        return self.call('get_mode', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def get_channels(self, **kwargs):
        return self.call('get_channels', kwargs=kwargs)

    def get_tubing_inner_diameter(self, **kwargs):
        return self.call('get_tubing_inner_diameter', kwargs=kwargs)

    def set_tubing_inner_diameter(self, **kwargs):
        return self.call('set_tubing_inner_diameter', kwargs=kwargs)

    def get_speed(self, **kwargs):
        return self.call('get_speed', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

    def get_runtime(self, **kwargs):
        return self.call('get_runtime', kwargs=kwargs)

    def set_runtime(self, **kwargs):
        return self.call('set_runtime', kwargs=kwargs)

    def get_volume_setpoint(self, **kwargs):
        return self.call('get_volume_setpoint', kwargs=kwargs)

    def set_volume_setpoint(self, **kwargs):
        return self.call('set_volume_setpoint', kwargs=kwargs)

    def get_rotation(self, **kwargs):
        return self.call('get_rotation', kwargs=kwargs)

    def set_rotation(self, **kwargs):
        return self.call('set_rotation', kwargs=kwargs)

    def get_setpoint_type(self, **kwargs):
        return self.call('get_setpoint_type', kwargs=kwargs)

    def set_setpoint_type(self, **kwargs):
        return self.call('set_setpoint_type', kwargs=kwargs)

    def get_max_flow_rate(self, **kwargs):
        return self.call('get_max_flow_rate', kwargs=kwargs)

    def get_run_failure_reason(self, **kwargs):
        return self.call('get_run_failure_reason', kwargs=kwargs)

    def has_channel_addressing(self, **kwargs):
        return self.call('has_channel_addressing', kwargs=kwargs)

    def set_channel_addressing(self, **kwargs):
        return self.call('set_channel_addressing', kwargs=kwargs)

    def has_event_messaging(self, **kwargs):
        return self.call('has_event_messaging', kwargs=kwargs)

    def set_event_messaging(self, **kwargs):
        return self.call('set_event_messaging', kwargs=kwargs)

    def reset_default_settings(self, **kwargs):
        return self.call('reset_default_settings', kwargs=kwargs)

    def continuous_flow(self, **kwargs):
        return self.call('continuous_flow', kwargs=kwargs)

    def dispense_vol_at_rate(self, **kwargs):
        return self.call('dispense_vol_at_rate', kwargs=kwargs)

    def dispense_vol_over_time(self, **kwargs):
        return self.call('dispense_vol_over_time', kwargs=kwargs)

    def dispense_flow_over_time(self, **kwargs):
        return self.call('dispense_flow_over_time', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

