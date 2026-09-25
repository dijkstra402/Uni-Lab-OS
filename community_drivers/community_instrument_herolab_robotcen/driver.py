from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHerolabRobotcen(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/BAMresearch__MAPz_at_BAM', 'source_file': 'Minerva/Releases/Version_1.0.0/Hardware/Centrifuges/Herolab.py', 'class_name': 'RobotCen', 'import_roots': [], 'candidate_methods': ['rotor_homing', 'start_centrifugation', 'stop', 'get_current_speed', 'get_speed_setpoint', 'set_speed', 'get_current_time', 'get_time_setpoint', 'set_time', 'get_current_temperature', 'get_temperature_setpoint', 'set_temperature', 'open_lid', 'close_lid', 'set_position_relative', 'set_position_absolute', 'set_position_relative2', 'set_position_absolute2', 'get_rotor_position', 'rotor_detection', 'enable_and_get_rotor_id', 'get_rotor_id', 'rpm_to_rcf', 'rcf_to_rpm', 'parent_hardware', 'dump_configuration', 'post_load_from_config'], 'action_targets': {}, 'metadata': {'repo': 'BAMresearch/MAPz_at_BAM', 'repo_url': 'https://github.com/BAMresearch/MAPz_at_BAM', 'brand': 'Herolab', 'model': 'RobotCen', 'device_type_cn': '离心机', 'device_type_en': 'Centrifuge', 'source_framework': '反应器/合成设备', 'tag_id': '4434', 'tag_name': '离心机', 'tag_name_en': 'Centrifuge', 'candidate_score': 288, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def rotor_homing(self, **kwargs):
        return self.call('rotor_homing', kwargs=kwargs)

    def start_centrifugation(self, **kwargs):
        return self.call('start_centrifugation', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def get_current_speed(self, **kwargs):
        return self.call('get_current_speed', kwargs=kwargs)

    def get_speed_setpoint(self, **kwargs):
        return self.call('get_speed_setpoint', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

    def get_current_time(self, **kwargs):
        return self.call('get_current_time', kwargs=kwargs)

    def get_time_setpoint(self, **kwargs):
        return self.call('get_time_setpoint', kwargs=kwargs)

    def set_time(self, **kwargs):
        return self.call('set_time', kwargs=kwargs)

    def get_current_temperature(self, **kwargs):
        return self.call('get_current_temperature', kwargs=kwargs)

    def get_temperature_setpoint(self, **kwargs):
        return self.call('get_temperature_setpoint', kwargs=kwargs)

    def set_temperature(self, **kwargs):
        return self.call('set_temperature', kwargs=kwargs)

    def open_lid(self, **kwargs):
        return self.call('open_lid', kwargs=kwargs)

    def close_lid(self, **kwargs):
        return self.call('close_lid', kwargs=kwargs)

    def set_position_relative(self, **kwargs):
        return self.call('set_position_relative', kwargs=kwargs)

    def set_position_absolute(self, **kwargs):
        return self.call('set_position_absolute', kwargs=kwargs)

    def set_position_relative2(self, **kwargs):
        return self.call('set_position_relative2', kwargs=kwargs)

    def set_position_absolute2(self, **kwargs):
        return self.call('set_position_absolute2', kwargs=kwargs)

    def get_rotor_position(self, **kwargs):
        return self.call('get_rotor_position', kwargs=kwargs)

    def rotor_detection(self, **kwargs):
        return self.call('rotor_detection', kwargs=kwargs)

    def enable_and_get_rotor_id(self, **kwargs):
        return self.call('enable_and_get_rotor_id', kwargs=kwargs)

    def get_rotor_id(self, **kwargs):
        return self.call('get_rotor_id', kwargs=kwargs)

    def rpm_to_rcf(self, **kwargs):
        return self.call('rpm_to_rcf', kwargs=kwargs)

    def rcf_to_rpm(self, **kwargs):
        return self.call('rcf_to_rpm', kwargs=kwargs)

    def parent_hardware(self, **kwargs):
        return self.call('parent_hardware', kwargs=kwargs)

    def dump_configuration(self, **kwargs):
        return self.call('dump_configuration', kwargs=kwargs)

    def post_load_from_config(self, **kwargs):
        return self.call('post_load_from_config', kwargs=kwargs)

