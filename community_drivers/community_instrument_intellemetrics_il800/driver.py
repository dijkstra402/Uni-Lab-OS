from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIntellemetricsIl800(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/CINF__PyExpLabSys', 'source_file': 'PyExpLabSys/apps/Stepper_motor_control/Modbus_comm_commands.py', 'class_name': 'Motor', 'import_roots': [], 'candidate_methods': ['get_status', 'get_home_end', 'get_move', 'get_alarm', 'reset_alarm', 'get_alarm_record', 'clear_alarm_record', 'get_alarm_status', 'clear_ETO', 'save_RAM_to_non_volatile', 'load_non_volatile_to_RAM', 'load_RAM_to_direct', 'get_operation_data_number', 'get_operation_trigger', 'get_operation_type', 'get_operating_speed', 'get_starting_changing_rate', 'get_stopping_deceleration', 'get_operating_current', 'get_position', 'get_command_position', 'get_group_id', 'set_operation_data_number', 'set_operation_trigger', 'set_operation_type', 'set_position', 'set_operating_speed', 'set_starting_changing_rate', 'set_stopping_deceleration', 'set_operating_current', 'set_group_id', 'home', 'stop', 'get_initial_group_id', 'get_initial_position', 'get_initial_operating_speed', 'get_initial_starting_speed', 'get_initial_starting_changing_rate', 'get_initial_stopping_deceleration', 'get_initial_operating_current', 'get_initial_operation_type', 'get_initial_positive_software_limit', 'get_initial_negative_software_limit', 'get_initial_electronic_gear_A', 'get_initial_electronic_gear_B', 'get_initial_zhome_operating_speed', 'get_initial_zhome_starting_speed', 'get_initial_zhome_acceleration_deceleration', 'get_Home_location', 'get_ISS_location', 'get_Mg_XPS_location', 'get_Al_XPS_location', 'get_SIG_location', 'get_HPC_location', 'get_Baking_location', 'set_initial_position', 'set_initial_operating_speed', 'set_initial_starting_speed', 'set_initial_starting_changing_rate', 'set_initial_stopping_deceleration', 'set_initial_operating_current', 'set_initial_operation_type', 'set_initial_group_id', 'set_initial_positive_software_limit', 'set_initial_negative_software_limit', 'set_initial_electronic_gear_A', 'set_initial_electronic_gear_B', 'set_initial_zhome_operating_speed', 'set_initial_zhome_starting_speed', 'set_initial_zhome_acceleration_deceleration', 'set_ISS_location', 'set_Mg_XPS_location', 'set_Al_XPS_location', 'set_SIG_location', 'set_HPC_location', 'set_Baking_location'], 'action_targets': {}, 'metadata': {'repo': 'CINF/PyExpLabSys', 'repo_url': 'https://github.com/CINF/PyExpLabSys', 'brand': 'Intellemetrics', 'model': 'IL800', 'device_type_cn': '蒸镀控制器', 'device_type_en': 'Evaporation Controller', 'source_framework': '反应器/合成设备', 'tag_id': '4449', 'tag_name': '蒸镀仪', 'tag_name_en': 'Evaporation Coater', 'candidate_score': 646, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def get_home_end(self, **kwargs):
        return self.call('get_home_end', kwargs=kwargs)

    def get_move(self, **kwargs):
        return self.call('get_move', kwargs=kwargs)

    def get_alarm(self, **kwargs):
        return self.call('get_alarm', kwargs=kwargs)

    def reset_alarm(self, **kwargs):
        return self.call('reset_alarm', kwargs=kwargs)

    def get_alarm_record(self, **kwargs):
        return self.call('get_alarm_record', kwargs=kwargs)

    def clear_alarm_record(self, **kwargs):
        return self.call('clear_alarm_record', kwargs=kwargs)

    def get_alarm_status(self, **kwargs):
        return self.call('get_alarm_status', kwargs=kwargs)

    def clear_ETO(self, **kwargs):
        return self.call('clear_ETO', kwargs=kwargs)

    def save_RAM_to_non_volatile(self, **kwargs):
        return self.call('save_RAM_to_non_volatile', kwargs=kwargs)

    def load_non_volatile_to_RAM(self, **kwargs):
        return self.call('load_non_volatile_to_RAM', kwargs=kwargs)

    def load_RAM_to_direct(self, **kwargs):
        return self.call('load_RAM_to_direct', kwargs=kwargs)

    def get_operation_data_number(self, **kwargs):
        return self.call('get_operation_data_number', kwargs=kwargs)

    def get_operation_trigger(self, **kwargs):
        return self.call('get_operation_trigger', kwargs=kwargs)

    def get_operation_type(self, **kwargs):
        return self.call('get_operation_type', kwargs=kwargs)

    def get_operating_speed(self, **kwargs):
        return self.call('get_operating_speed', kwargs=kwargs)

    def get_starting_changing_rate(self, **kwargs):
        return self.call('get_starting_changing_rate', kwargs=kwargs)

    def get_stopping_deceleration(self, **kwargs):
        return self.call('get_stopping_deceleration', kwargs=kwargs)

    def get_operating_current(self, **kwargs):
        return self.call('get_operating_current', kwargs=kwargs)

    def get_position(self, **kwargs):
        return self.call('get_position', kwargs=kwargs)

    def get_command_position(self, **kwargs):
        return self.call('get_command_position', kwargs=kwargs)

    def get_group_id(self, **kwargs):
        return self.call('get_group_id', kwargs=kwargs)

    def set_operation_data_number(self, **kwargs):
        return self.call('set_operation_data_number', kwargs=kwargs)

    def set_operation_trigger(self, **kwargs):
        return self.call('set_operation_trigger', kwargs=kwargs)

    def set_operation_type(self, **kwargs):
        return self.call('set_operation_type', kwargs=kwargs)

    def set_position(self, **kwargs):
        return self.call('set_position', kwargs=kwargs)

    def set_operating_speed(self, **kwargs):
        return self.call('set_operating_speed', kwargs=kwargs)

    def set_starting_changing_rate(self, **kwargs):
        return self.call('set_starting_changing_rate', kwargs=kwargs)

    def set_stopping_deceleration(self, **kwargs):
        return self.call('set_stopping_deceleration', kwargs=kwargs)

    def set_operating_current(self, **kwargs):
        return self.call('set_operating_current', kwargs=kwargs)

    def set_group_id(self, **kwargs):
        return self.call('set_group_id', kwargs=kwargs)

    def home(self, **kwargs):
        return self.call('home', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def get_initial_group_id(self, **kwargs):
        return self.call('get_initial_group_id', kwargs=kwargs)

    def get_initial_position(self, **kwargs):
        return self.call('get_initial_position', kwargs=kwargs)

    def get_initial_operating_speed(self, **kwargs):
        return self.call('get_initial_operating_speed', kwargs=kwargs)

    def get_initial_starting_speed(self, **kwargs):
        return self.call('get_initial_starting_speed', kwargs=kwargs)

    def get_initial_starting_changing_rate(self, **kwargs):
        return self.call('get_initial_starting_changing_rate', kwargs=kwargs)

    def get_initial_stopping_deceleration(self, **kwargs):
        return self.call('get_initial_stopping_deceleration', kwargs=kwargs)

    def get_initial_operating_current(self, **kwargs):
        return self.call('get_initial_operating_current', kwargs=kwargs)

    def get_initial_operation_type(self, **kwargs):
        return self.call('get_initial_operation_type', kwargs=kwargs)

    def get_initial_positive_software_limit(self, **kwargs):
        return self.call('get_initial_positive_software_limit', kwargs=kwargs)

    def get_initial_negative_software_limit(self, **kwargs):
        return self.call('get_initial_negative_software_limit', kwargs=kwargs)

    def get_initial_electronic_gear_A(self, **kwargs):
        return self.call('get_initial_electronic_gear_A', kwargs=kwargs)

    def get_initial_electronic_gear_B(self, **kwargs):
        return self.call('get_initial_electronic_gear_B', kwargs=kwargs)

    def get_initial_zhome_operating_speed(self, **kwargs):
        return self.call('get_initial_zhome_operating_speed', kwargs=kwargs)

    def get_initial_zhome_starting_speed(self, **kwargs):
        return self.call('get_initial_zhome_starting_speed', kwargs=kwargs)

    def get_initial_zhome_acceleration_deceleration(self, **kwargs):
        return self.call('get_initial_zhome_acceleration_deceleration', kwargs=kwargs)

    def get_Home_location(self, **kwargs):
        return self.call('get_Home_location', kwargs=kwargs)

    def get_ISS_location(self, **kwargs):
        return self.call('get_ISS_location', kwargs=kwargs)

    def get_Mg_XPS_location(self, **kwargs):
        return self.call('get_Mg_XPS_location', kwargs=kwargs)

    def get_Al_XPS_location(self, **kwargs):
        return self.call('get_Al_XPS_location', kwargs=kwargs)

    def get_SIG_location(self, **kwargs):
        return self.call('get_SIG_location', kwargs=kwargs)

    def get_HPC_location(self, **kwargs):
        return self.call('get_HPC_location', kwargs=kwargs)

    def get_Baking_location(self, **kwargs):
        return self.call('get_Baking_location', kwargs=kwargs)

    def set_initial_position(self, **kwargs):
        return self.call('set_initial_position', kwargs=kwargs)

    def set_initial_operating_speed(self, **kwargs):
        return self.call('set_initial_operating_speed', kwargs=kwargs)

    def set_initial_starting_speed(self, **kwargs):
        return self.call('set_initial_starting_speed', kwargs=kwargs)

    def set_initial_starting_changing_rate(self, **kwargs):
        return self.call('set_initial_starting_changing_rate', kwargs=kwargs)

    def set_initial_stopping_deceleration(self, **kwargs):
        return self.call('set_initial_stopping_deceleration', kwargs=kwargs)

    def set_initial_operating_current(self, **kwargs):
        return self.call('set_initial_operating_current', kwargs=kwargs)

    def set_initial_operation_type(self, **kwargs):
        return self.call('set_initial_operation_type', kwargs=kwargs)

    def set_initial_group_id(self, **kwargs):
        return self.call('set_initial_group_id', kwargs=kwargs)

    def set_initial_positive_software_limit(self, **kwargs):
        return self.call('set_initial_positive_software_limit', kwargs=kwargs)

    def set_initial_negative_software_limit(self, **kwargs):
        return self.call('set_initial_negative_software_limit', kwargs=kwargs)

    def set_initial_electronic_gear_A(self, **kwargs):
        return self.call('set_initial_electronic_gear_A', kwargs=kwargs)

    def set_initial_electronic_gear_B(self, **kwargs):
        return self.call('set_initial_electronic_gear_B', kwargs=kwargs)

    def set_initial_zhome_operating_speed(self, **kwargs):
        return self.call('set_initial_zhome_operating_speed', kwargs=kwargs)

    def set_initial_zhome_starting_speed(self, **kwargs):
        return self.call('set_initial_zhome_starting_speed', kwargs=kwargs)

    def set_initial_zhome_acceleration_deceleration(self, **kwargs):
        return self.call('set_initial_zhome_acceleration_deceleration', kwargs=kwargs)

    def set_ISS_location(self, **kwargs):
        return self.call('set_ISS_location', kwargs=kwargs)

    def set_Mg_XPS_location(self, **kwargs):
        return self.call('set_Mg_XPS_location', kwargs=kwargs)

    def set_Al_XPS_location(self, **kwargs):
        return self.call('set_Al_XPS_location', kwargs=kwargs)

    def set_SIG_location(self, **kwargs):
        return self.call('set_SIG_location', kwargs=kwargs)

    def set_HPC_location(self, **kwargs):
        return self.call('set_HPC_location', kwargs=kwargs)

    def set_Baking_location(self, **kwargs):
        return self.call('set_Baking_location', kwargs=kwargs)

