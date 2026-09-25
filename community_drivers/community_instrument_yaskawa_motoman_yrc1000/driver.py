from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentYaskawaMotomanYrc1000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/underautomation__Yaskawa.py', 'source_file': 'underautomation/yaskawa/high_speed_e_server/internal/high_speed_e_server_client_base.py', 'class_name': 'HighSpeedEServerClientBase', 'import_roots': [], 'candidate_methods': ['close', 'get_alarm', 'get_status_information', 'get_executing_job_information', 'get_job_stack', 'get_configuration_information', 'get_robot_cartesian_position', 'get_robot_joint_position', 'get_robot_position', 'get_position_error', 'get_torque', 'alarm_reset', 'servo_command', 'switching_command', 'display', 'start_job', 'select_job', 'get_management_time', 'get_system_information', 'get_system_parameter', 'read_io', 'write_io', 'write_io_network_input', 'read_register', 'write_register', 'read_byte', 'write_byte', 'read_integer', 'write_integer', 'read_double_integer', 'write_double_integer', 'read_real', 'write_real', 'read16_bytes_char', 'write16_bytes_char', 'read_position_variable', 'write_position_variable', 'read_base_position', 'write_base_position', 'read_external_position', 'write_external_position', 'get_alarm_extended', 'move_cartesian', 'move_joints', 'read32_bytes_char', 'write32_bytes_char', 'delete_file', 'load_file', 'get_file_list', 'get_file', 'batch_data_backup', 'ip', 'connected'], 'action_targets': {}, 'metadata': {'repo': 'underautomation/Yaskawa.py', 'repo_url': 'https://github.com/underautomation/Yaskawa.py', 'brand': 'Yaskawa', 'model': 'Motoman YRC1000', 'device_type_cn': '工业机械臂', 'device_type_en': 'Industrial Robot Arm', 'source_framework': '机器人/运动控制', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 445, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def get_alarm(self, **kwargs):
        return self.call('get_alarm', kwargs=kwargs)

    def get_status_information(self, **kwargs):
        return self.call('get_status_information', kwargs=kwargs)

    def get_executing_job_information(self, **kwargs):
        return self.call('get_executing_job_information', kwargs=kwargs)

    def get_job_stack(self, **kwargs):
        return self.call('get_job_stack', kwargs=kwargs)

    def get_configuration_information(self, **kwargs):
        return self.call('get_configuration_information', kwargs=kwargs)

    def get_robot_cartesian_position(self, **kwargs):
        return self.call('get_robot_cartesian_position', kwargs=kwargs)

    def get_robot_joint_position(self, **kwargs):
        return self.call('get_robot_joint_position', kwargs=kwargs)

    def get_robot_position(self, **kwargs):
        return self.call('get_robot_position', kwargs=kwargs)

    def get_position_error(self, **kwargs):
        return self.call('get_position_error', kwargs=kwargs)

    def get_torque(self, **kwargs):
        return self.call('get_torque', kwargs=kwargs)

    def alarm_reset(self, **kwargs):
        return self.call('alarm_reset', kwargs=kwargs)

    def servo_command(self, **kwargs):
        return self.call('servo_command', kwargs=kwargs)

    def switching_command(self, **kwargs):
        return self.call('switching_command', kwargs=kwargs)

    def display(self, **kwargs):
        return self.call('display', kwargs=kwargs)

    def start_job(self, **kwargs):
        return self.call('start_job', kwargs=kwargs)

    def select_job(self, **kwargs):
        return self.call('select_job', kwargs=kwargs)

    def get_management_time(self, **kwargs):
        return self.call('get_management_time', kwargs=kwargs)

    def get_system_information(self, **kwargs):
        return self.call('get_system_information', kwargs=kwargs)

    def get_system_parameter(self, **kwargs):
        return self.call('get_system_parameter', kwargs=kwargs)

    def read_io(self, **kwargs):
        return self.call('read_io', kwargs=kwargs)

    def write_io(self, **kwargs):
        return self.call('write_io', kwargs=kwargs)

    def write_io_network_input(self, **kwargs):
        return self.call('write_io_network_input', kwargs=kwargs)

    def read_register(self, **kwargs):
        return self.call('read_register', kwargs=kwargs)

    def write_register(self, **kwargs):
        return self.call('write_register', kwargs=kwargs)

    def read_byte(self, **kwargs):
        return self.call('read_byte', kwargs=kwargs)

    def write_byte(self, **kwargs):
        return self.call('write_byte', kwargs=kwargs)

    def read_integer(self, **kwargs):
        return self.call('read_integer', kwargs=kwargs)

    def write_integer(self, **kwargs):
        return self.call('write_integer', kwargs=kwargs)

    def read_double_integer(self, **kwargs):
        return self.call('read_double_integer', kwargs=kwargs)

    def write_double_integer(self, **kwargs):
        return self.call('write_double_integer', kwargs=kwargs)

    def read_real(self, **kwargs):
        return self.call('read_real', kwargs=kwargs)

    def write_real(self, **kwargs):
        return self.call('write_real', kwargs=kwargs)

    def read16_bytes_char(self, **kwargs):
        return self.call('read16_bytes_char', kwargs=kwargs)

    def write16_bytes_char(self, **kwargs):
        return self.call('write16_bytes_char', kwargs=kwargs)

    def read_position_variable(self, **kwargs):
        return self.call('read_position_variable', kwargs=kwargs)

    def write_position_variable(self, **kwargs):
        return self.call('write_position_variable', kwargs=kwargs)

    def read_base_position(self, **kwargs):
        return self.call('read_base_position', kwargs=kwargs)

    def write_base_position(self, **kwargs):
        return self.call('write_base_position', kwargs=kwargs)

    def read_external_position(self, **kwargs):
        return self.call('read_external_position', kwargs=kwargs)

    def write_external_position(self, **kwargs):
        return self.call('write_external_position', kwargs=kwargs)

    def get_alarm_extended(self, **kwargs):
        return self.call('get_alarm_extended', kwargs=kwargs)

    def move_cartesian(self, **kwargs):
        return self.call('move_cartesian', kwargs=kwargs)

    def move_joints(self, **kwargs):
        return self.call('move_joints', kwargs=kwargs)

    def read32_bytes_char(self, **kwargs):
        return self.call('read32_bytes_char', kwargs=kwargs)

    def write32_bytes_char(self, **kwargs):
        return self.call('write32_bytes_char', kwargs=kwargs)

    def delete_file(self, **kwargs):
        return self.call('delete_file', kwargs=kwargs)

    def load_file(self, **kwargs):
        return self.call('load_file', kwargs=kwargs)

    def get_file_list(self, **kwargs):
        return self.call('get_file_list', kwargs=kwargs)

    def get_file(self, **kwargs):
        return self.call('get_file', kwargs=kwargs)

    def batch_data_backup(self, **kwargs):
        return self.call('batch_data_backup', kwargs=kwargs)

    def ip(self, **kwargs):
        return self.call('ip', kwargs=kwargs)

    def connected(self, **kwargs):
        return self.call('connected', kwargs=kwargs)

