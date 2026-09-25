from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentRunzeFluidAuroraPro(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AllenNeuralDynamics__runze-control', 'source_file': 'src/runze_control/syringe_pump.py', 'class_name': 'SyringePump', 'import_roots': ['src'], 'candidate_methods': ['reset_syringe_position', 'get_position_steps', 'get_position_ul', 'get_position_percent', 'aspirate', 'withdraw', 'dispense', 'aspirate_steps', 'withdraw_steps', 'dispense_steps', 'force_stop', 'halt', 'get_motor_status', 'is_busy', 'set_speed_percent', 'get_speed_percent', 'get_remaining_capacity_ul', 'move_absolute_in_steps', 'move_absolute_in_percent', 'get_firmware_version', 'get_protocol', 'set_address', 'get_address', 'get_serial_number', 'set_multicast_address', 'get_rs232_baudrate', 'get_rs485_baudrate', 'get_can_baudrate', 'wait_for_reply'], 'action_targets': {}, 'metadata': {'repo': 'AllenNeuralDynamics/runze-control', 'repo_url': 'https://github.com/AllenNeuralDynamics/runze-control', 'brand': 'Runze Fluid', 'model': 'Aurora Pro', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': '专用驱动', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 246, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def reset_syringe_position(self, **kwargs):
        return self.call('reset_syringe_position', kwargs=kwargs)

    def get_position_steps(self, **kwargs):
        return self.call('get_position_steps', kwargs=kwargs)

    def get_position_ul(self, **kwargs):
        return self.call('get_position_ul', kwargs=kwargs)

    def get_position_percent(self, **kwargs):
        return self.call('get_position_percent', kwargs=kwargs)

    def aspirate(self, **kwargs):
        return self.call('aspirate', kwargs=kwargs)

    def withdraw(self, **kwargs):
        return self.call('withdraw', kwargs=kwargs)

    def dispense(self, **kwargs):
        return self.call('dispense', kwargs=kwargs)

    def aspirate_steps(self, **kwargs):
        return self.call('aspirate_steps', kwargs=kwargs)

    def withdraw_steps(self, **kwargs):
        return self.call('withdraw_steps', kwargs=kwargs)

    def dispense_steps(self, **kwargs):
        return self.call('dispense_steps', kwargs=kwargs)

    def force_stop(self, **kwargs):
        return self.call('force_stop', kwargs=kwargs)

    def halt(self, **kwargs):
        return self.call('halt', kwargs=kwargs)

    def get_motor_status(self, **kwargs):
        return self.call('get_motor_status', kwargs=kwargs)

    def is_busy(self, **kwargs):
        return self.call('is_busy', kwargs=kwargs)

    def set_speed_percent(self, **kwargs):
        return self.call('set_speed_percent', kwargs=kwargs)

    def get_speed_percent(self, **kwargs):
        return self.call('get_speed_percent', kwargs=kwargs)

    def get_remaining_capacity_ul(self, **kwargs):
        return self.call('get_remaining_capacity_ul', kwargs=kwargs)

    def move_absolute_in_steps(self, **kwargs):
        return self.call('move_absolute_in_steps', kwargs=kwargs)

    def move_absolute_in_percent(self, **kwargs):
        return self.call('move_absolute_in_percent', kwargs=kwargs)

    def get_firmware_version(self, **kwargs):
        return self.call('get_firmware_version', kwargs=kwargs)

    def get_protocol(self, **kwargs):
        return self.call('get_protocol', kwargs=kwargs)

    def set_address(self, **kwargs):
        return self.call('set_address', kwargs=kwargs)

    def get_address(self, **kwargs):
        return self.call('get_address', kwargs=kwargs)

    def get_serial_number(self, **kwargs):
        return self.call('get_serial_number', kwargs=kwargs)

    def set_multicast_address(self, **kwargs):
        return self.call('set_multicast_address', kwargs=kwargs)

    def get_rs232_baudrate(self, **kwargs):
        return self.call('get_rs232_baudrate', kwargs=kwargs)

    def get_rs485_baudrate(self, **kwargs):
        return self.call('get_rs485_baudrate', kwargs=kwargs)

    def get_can_baudrate(self, **kwargs):
        return self.call('get_can_baudrate', kwargs=kwargs)

    def wait_for_reply(self, **kwargs):
        return self.call('wait_for_reply', kwargs=kwargs)

