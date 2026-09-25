from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentUniversalRobotsUr10(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/SintefManufacturing__python-urx', 'source_file': 'urx/urrobot.py', 'class_name': 'URRobot', 'import_roots': [], 'candidate_methods': ['is_running', 'is_program_running', 'send_program', 'get_tcp_force', 'get_force', 'get_joint_temperature', 'get_joint_voltage', 'get_joint_current', 'get_main_voltage', 'get_robot_voltage', 'get_robot_current', 'get_all_rt_data', 'set_tcp', 'set_payload', 'set_gravity', 'send_message', 'set_digital_out', 'get_analog_inputs', 'get_analog_in', 'get_digital_in_bits', 'get_digital_in', 'get_digital_out', 'get_digital_out_bits', 'set_analog_out', 'set_tool_voltage', 'getj', 'speedx', 'movej', 'movel', 'movep', 'servoc', 'servoj', 'movex', 'getl', 'movec', 'movejs', 'movels', 'movexs', 'stopl', 'stopj', 'stop', 'close', 'set_freedrive', 'set_simulation', 'get_realtime_monitor', 'translate', 'up', 'down'], 'action_targets': {}, 'metadata': {'repo': 'SintefManufacturing/python-urx', 'repo_url': 'https://github.com/SintefManufacturing/python-urx', 'brand': 'Universal Robots', 'model': 'UR10', 'device_type_cn': '工业机械臂', 'device_type_en': 'Industrial Robot', 'source_framework': 'python-urx', 'tag_id': '4402', 'tag_name': '机械臂', 'tag_name_en': 'Robotic Arm', 'candidate_score': 450, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def is_running(self, **kwargs):
        return self.call('is_running', kwargs=kwargs)

    def is_program_running(self, **kwargs):
        return self.call('is_program_running', kwargs=kwargs)

    def send_program(self, **kwargs):
        return self.call('send_program', kwargs=kwargs)

    def get_tcp_force(self, **kwargs):
        return self.call('get_tcp_force', kwargs=kwargs)

    def get_force(self, **kwargs):
        return self.call('get_force', kwargs=kwargs)

    def get_joint_temperature(self, **kwargs):
        return self.call('get_joint_temperature', kwargs=kwargs)

    def get_joint_voltage(self, **kwargs):
        return self.call('get_joint_voltage', kwargs=kwargs)

    def get_joint_current(self, **kwargs):
        return self.call('get_joint_current', kwargs=kwargs)

    def get_main_voltage(self, **kwargs):
        return self.call('get_main_voltage', kwargs=kwargs)

    def get_robot_voltage(self, **kwargs):
        return self.call('get_robot_voltage', kwargs=kwargs)

    def get_robot_current(self, **kwargs):
        return self.call('get_robot_current', kwargs=kwargs)

    def get_all_rt_data(self, **kwargs):
        return self.call('get_all_rt_data', kwargs=kwargs)

    def set_tcp(self, **kwargs):
        return self.call('set_tcp', kwargs=kwargs)

    def set_payload(self, **kwargs):
        return self.call('set_payload', kwargs=kwargs)

    def set_gravity(self, **kwargs):
        return self.call('set_gravity', kwargs=kwargs)

    def send_message(self, **kwargs):
        return self.call('send_message', kwargs=kwargs)

    def set_digital_out(self, **kwargs):
        return self.call('set_digital_out', kwargs=kwargs)

    def get_analog_inputs(self, **kwargs):
        return self.call('get_analog_inputs', kwargs=kwargs)

    def get_analog_in(self, **kwargs):
        return self.call('get_analog_in', kwargs=kwargs)

    def get_digital_in_bits(self, **kwargs):
        return self.call('get_digital_in_bits', kwargs=kwargs)

    def get_digital_in(self, **kwargs):
        return self.call('get_digital_in', kwargs=kwargs)

    def get_digital_out(self, **kwargs):
        return self.call('get_digital_out', kwargs=kwargs)

    def get_digital_out_bits(self, **kwargs):
        return self.call('get_digital_out_bits', kwargs=kwargs)

    def set_analog_out(self, **kwargs):
        return self.call('set_analog_out', kwargs=kwargs)

    def set_tool_voltage(self, **kwargs):
        return self.call('set_tool_voltage', kwargs=kwargs)

    def getj(self, **kwargs):
        return self.call('getj', kwargs=kwargs)

    def speedx(self, **kwargs):
        return self.call('speedx', kwargs=kwargs)

    def movej(self, **kwargs):
        return self.call('movej', kwargs=kwargs)

    def movel(self, **kwargs):
        return self.call('movel', kwargs=kwargs)

    def movep(self, **kwargs):
        return self.call('movep', kwargs=kwargs)

    def servoc(self, **kwargs):
        return self.call('servoc', kwargs=kwargs)

    def servoj(self, **kwargs):
        return self.call('servoj', kwargs=kwargs)

    def movex(self, **kwargs):
        return self.call('movex', kwargs=kwargs)

    def getl(self, **kwargs):
        return self.call('getl', kwargs=kwargs)

    def movec(self, **kwargs):
        return self.call('movec', kwargs=kwargs)

    def movejs(self, **kwargs):
        return self.call('movejs', kwargs=kwargs)

    def movels(self, **kwargs):
        return self.call('movels', kwargs=kwargs)

    def movexs(self, **kwargs):
        return self.call('movexs', kwargs=kwargs)

    def stopl(self, **kwargs):
        return self.call('stopl', kwargs=kwargs)

    def stopj(self, **kwargs):
        return self.call('stopj', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def set_freedrive(self, **kwargs):
        return self.call('set_freedrive', kwargs=kwargs)

    def set_simulation(self, **kwargs):
        return self.call('set_simulation', kwargs=kwargs)

    def get_realtime_monitor(self, **kwargs):
        return self.call('get_realtime_monitor', kwargs=kwargs)

    def translate(self, **kwargs):
        return self.call('translate', kwargs=kwargs)

    def up(self, **kwargs):
        return self.call('up', kwargs=kwargs)

    def down(self, **kwargs):
        return self.call('down', kwargs=kwargs)

