from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAbbIrb120026006700Irc5(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/rpiRobotics__abb_robot_client', 'source_file': 'src/abb_robot_client/robotraconteur/abb_robotraconteur_rws_driver.py', 'class_name': 'ABBRWSRobotImpl', 'import_roots': ['src'], 'candidate_methods': ['RRServiceObjectInit', 'async_disable', 'async_enable', 'async_reset_errors', 'async_jog_freespace', 'async_jog_joint', 'execute_trajectory', 'jog_cartesian', 'async_home', 'tool_attached', 'tool_detached', 'payload_attached', 'payload_detached', 'getf_execution_state', 'getf_controller_state', 'getf_operation_mode', 'operational_mode', 'controller_state', 'start', 'stop', 'resetpp', 'activate_task', 'deactivate_task', 'getf_tasks', 'getf_digital_io', 'setf_digital_io', 'getf_digital_io2', 'setf_digital_io2', 'getf_analog_io', 'setf_analog_io', 'getf_analog_io2', 'setf_analog_io2', 'getf_rapid_variables', 'getf_rapid_variable', 'setf_rapid_variable', 'getf_ramdisk_path', 'read_file', 'upload_file', 'delete_file', 'list_files', 'read_event_log', 'getf_jointtarget', 'getf_robtarget', 'getf_robtarget2', 'speed_ratio', 'getf_rapid_variable_jointtarget', 'setf_rapid_variable_jointtarget', 'getf_rapid_variable_jointtarget_array', 'setf_rapid_variable_jointtarget_array', 'getf_rapid_variable_num', 'setf_rapid_variable_num', 'getf_rapid_variable_num_array', 'setf_rapid_variable_num_array', 'request_rmmp', 'poll_rmmp'], 'action_targets': {}, 'metadata': {'repo': 'rpiRobotics/abb_robot_client', 'repo_url': 'https://github.com/rpiRobotics/abb_robot_client', 'brand': 'ABB', 'model': 'IRB 1200/2600/6700 (IRC5)', 'device_type_cn': '工业机械臂', 'device_type_en': 'Industrial Robot Arm', 'source_framework': '机器人/运动控制', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 526, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def RRServiceObjectInit(self, **kwargs):
        return self.call('RRServiceObjectInit', kwargs=kwargs)

    def async_disable(self, **kwargs):
        return self.call('async_disable', kwargs=kwargs)

    def async_enable(self, **kwargs):
        return self.call('async_enable', kwargs=kwargs)

    def async_reset_errors(self, **kwargs):
        return self.call('async_reset_errors', kwargs=kwargs)

    def async_jog_freespace(self, **kwargs):
        return self.call('async_jog_freespace', kwargs=kwargs)

    def async_jog_joint(self, **kwargs):
        return self.call('async_jog_joint', kwargs=kwargs)

    def execute_trajectory(self, **kwargs):
        return self.call('execute_trajectory', kwargs=kwargs)

    def jog_cartesian(self, **kwargs):
        return self.call('jog_cartesian', kwargs=kwargs)

    def async_home(self, **kwargs):
        return self.call('async_home', kwargs=kwargs)

    def tool_attached(self, **kwargs):
        return self.call('tool_attached', kwargs=kwargs)

    def tool_detached(self, **kwargs):
        return self.call('tool_detached', kwargs=kwargs)

    def payload_attached(self, **kwargs):
        return self.call('payload_attached', kwargs=kwargs)

    def payload_detached(self, **kwargs):
        return self.call('payload_detached', kwargs=kwargs)

    def getf_execution_state(self, **kwargs):
        return self.call('getf_execution_state', kwargs=kwargs)

    def getf_controller_state(self, **kwargs):
        return self.call('getf_controller_state', kwargs=kwargs)

    def getf_operation_mode(self, **kwargs):
        return self.call('getf_operation_mode', kwargs=kwargs)

    def operational_mode(self, **kwargs):
        return self.call('operational_mode', kwargs=kwargs)

    def controller_state(self, **kwargs):
        return self.call('controller_state', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def resetpp(self, **kwargs):
        return self.call('resetpp', kwargs=kwargs)

    def activate_task(self, **kwargs):
        return self.call('activate_task', kwargs=kwargs)

    def deactivate_task(self, **kwargs):
        return self.call('deactivate_task', kwargs=kwargs)

    def getf_tasks(self, **kwargs):
        return self.call('getf_tasks', kwargs=kwargs)

    def getf_digital_io(self, **kwargs):
        return self.call('getf_digital_io', kwargs=kwargs)

    def setf_digital_io(self, **kwargs):
        return self.call('setf_digital_io', kwargs=kwargs)

    def getf_digital_io2(self, **kwargs):
        return self.call('getf_digital_io2', kwargs=kwargs)

    def setf_digital_io2(self, **kwargs):
        return self.call('setf_digital_io2', kwargs=kwargs)

    def getf_analog_io(self, **kwargs):
        return self.call('getf_analog_io', kwargs=kwargs)

    def setf_analog_io(self, **kwargs):
        return self.call('setf_analog_io', kwargs=kwargs)

    def getf_analog_io2(self, **kwargs):
        return self.call('getf_analog_io2', kwargs=kwargs)

    def setf_analog_io2(self, **kwargs):
        return self.call('setf_analog_io2', kwargs=kwargs)

    def getf_rapid_variables(self, **kwargs):
        return self.call('getf_rapid_variables', kwargs=kwargs)

    def getf_rapid_variable(self, **kwargs):
        return self.call('getf_rapid_variable', kwargs=kwargs)

    def setf_rapid_variable(self, **kwargs):
        return self.call('setf_rapid_variable', kwargs=kwargs)

    def getf_ramdisk_path(self, **kwargs):
        return self.call('getf_ramdisk_path', kwargs=kwargs)

    def read_file(self, **kwargs):
        return self.call('read_file', kwargs=kwargs)

    def upload_file(self, **kwargs):
        return self.call('upload_file', kwargs=kwargs)

    def delete_file(self, **kwargs):
        return self.call('delete_file', kwargs=kwargs)

    def list_files(self, **kwargs):
        return self.call('list_files', kwargs=kwargs)

    def read_event_log(self, **kwargs):
        return self.call('read_event_log', kwargs=kwargs)

    def getf_jointtarget(self, **kwargs):
        return self.call('getf_jointtarget', kwargs=kwargs)

    def getf_robtarget(self, **kwargs):
        return self.call('getf_robtarget', kwargs=kwargs)

    def getf_robtarget2(self, **kwargs):
        return self.call('getf_robtarget2', kwargs=kwargs)

    def speed_ratio(self, **kwargs):
        return self.call('speed_ratio', kwargs=kwargs)

    def getf_rapid_variable_jointtarget(self, **kwargs):
        return self.call('getf_rapid_variable_jointtarget', kwargs=kwargs)

    def setf_rapid_variable_jointtarget(self, **kwargs):
        return self.call('setf_rapid_variable_jointtarget', kwargs=kwargs)

    def getf_rapid_variable_jointtarget_array(self, **kwargs):
        return self.call('getf_rapid_variable_jointtarget_array', kwargs=kwargs)

    def setf_rapid_variable_jointtarget_array(self, **kwargs):
        return self.call('setf_rapid_variable_jointtarget_array', kwargs=kwargs)

    def getf_rapid_variable_num(self, **kwargs):
        return self.call('getf_rapid_variable_num', kwargs=kwargs)

    def setf_rapid_variable_num(self, **kwargs):
        return self.call('setf_rapid_variable_num', kwargs=kwargs)

    def getf_rapid_variable_num_array(self, **kwargs):
        return self.call('getf_rapid_variable_num_array', kwargs=kwargs)

    def setf_rapid_variable_num_array(self, **kwargs):
        return self.call('setf_rapid_variable_num_array', kwargs=kwargs)

    def request_rmmp(self, **kwargs):
        return self.call('request_rmmp', kwargs=kwargs)

    def poll_rmmp(self, **kwargs):
        return self.call('poll_rmmp', kwargs=kwargs)

