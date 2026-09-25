from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictM3300adig(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Keysight/Keysight_M3300A.py', 'class_name': 'M3300A_DIG', 'import_roots': ['src'], 'candidate_methods': ['daq_read', 'daq_start', 'daq_start_multiple', 'daq_stop', 'daq_stop_multiple', 'daq_trigger', 'daq_trigger_multiple', 'daq_flush', 'daq_flush_multiple', 'set_trigger_io', 'get_trigger_io', 'reset_clock_phase', 'set_clksys_frequency', 'get_prescaler', 'set_prescaler', 'get_full_scale', 'set_full_scale', 'get_impedance', 'set_impedance', 'get_coupling', 'set_coupling', 'set_trigger_mode', 'get_trigger_mode', 'set_trigger_threshold', 'get_trigger_threshold', 'set_points_per_cycle', 'set_n_cycles', 'set_daq_trigger_delay', 'set_daq_trigger_mode', 'set_digital_trigger_mode', 'set_digital_trigger_source', 'set_analog_trigger_mask', 'set_ext_trigger_source', 'set_ext_trigger_behaviour', 'set_n_points', 'set_timeout', 'get_trigger_direction', 'set_trigger_direction', 'get_sys_frequency', 'set_sys_frequency', 'get_sync_frequency', 'get_idn', 'get_module_count', 'get_product_name', 'get_serial_number', 'get_chassis', 'get_slot', 'get_firmware_version', 'get_hardware_version', 'get_type', 'get_open', 'get_pxi_trigger', 'set_pxi_trigger', 'get_fpga_pc_port', 'set_fpga_pc_port', 'load_fpga_image', 'set_hvi_register', 'get_hvi_register', 'get_product_name_by_slot', 'get_product_name_by_index', 'get_serial_number_by_slot', 'get_serial_number_by_index', 'get_type_by_slot', 'get_type_by_index', 'get_temperature', 'close', 'close_soft', 'open_with_serial_number', 'open_with_slot', 'run_self_test', 'get_chassis_number', 'get_slot_number', 'get_instrument_type'], 'action_targets': {'set_trigger_io': '__qcodes_param_set__trigger_io', 'get_trigger_io': '__qcodes_param_get__trigger_io', 'get_trigger_direction': '__qcodes_param_get__trigger_direction', 'set_trigger_direction': '__qcodes_param_set__trigger_direction', 'get_sys_frequency': '__qcodes_param_get__sys_frequency', 'set_sys_frequency': '__qcodes_param_set__sys_frequency', 'get_sync_frequency': '__qcodes_param_get__sync_frequency', 'get_module_count': '__qcodes_param_get__module_count', 'get_product_name': '__qcodes_param_get__product_name', 'get_serial_number': '__qcodes_param_get__serial_number', 'get_firmware_version': '__qcodes_param_get__firmware_version', 'get_hardware_version': '__qcodes_param_get__hardware_version', 'get_open': '__qcodes_param_get__open', 'get_temperature': '__qcodes_param_get__temperature', 'get_chassis_number': '__qcodes_param_get__chassis_number', 'get_slot_number': '__qcodes_param_get__slot_number', 'get_instrument_type': '__qcodes_param_get__instrument_type'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Keysight/Keysight_M3300A.py', 'confidence': 0.9, 'quality_score': 1.06, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'set_trigger_io': '__qcodes_param_set__trigger_io', 'get_trigger_io': '__qcodes_param_get__trigger_io', 'get_trigger_direction': '__qcodes_param_get__trigger_direction', 'set_trigger_direction': '__qcodes_param_set__trigger_direction', 'get_sys_frequency': '__qcodes_param_get__sys_frequency', 'set_sys_frequency': '__qcodes_param_set__sys_frequency', 'get_sync_frequency': '__qcodes_param_get__sync_frequency', 'get_module_count': '__qcodes_param_get__module_count', 'get_product_name': '__qcodes_param_get__product_name', 'get_serial_number': '__qcodes_param_get__serial_number', 'get_firmware_version': '__qcodes_param_get__firmware_version', 'get_hardware_version': '__qcodes_param_get__hardware_version', 'get_open': '__qcodes_param_get__open', 'get_temperature': '__qcodes_param_get__temperature', 'get_chassis_number': '__qcodes_param_get__chassis_number', 'get_slot_number': '__qcodes_param_get__slot_number', 'get_instrument_type': '__qcodes_param_get__instrument_type'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def daq_read(self, **kwargs):
        return self.call('daq_read', kwargs=kwargs)

    def daq_start(self, **kwargs):
        return self.call('daq_start', kwargs=kwargs)

    def daq_start_multiple(self, **kwargs):
        return self.call('daq_start_multiple', kwargs=kwargs)

    def daq_stop(self, **kwargs):
        return self.call('daq_stop', kwargs=kwargs)

    def daq_stop_multiple(self, **kwargs):
        return self.call('daq_stop_multiple', kwargs=kwargs)

    def daq_trigger(self, **kwargs):
        return self.call('daq_trigger', kwargs=kwargs)

    def daq_trigger_multiple(self, **kwargs):
        return self.call('daq_trigger_multiple', kwargs=kwargs)

    def daq_flush(self, **kwargs):
        return self.call('daq_flush', kwargs=kwargs)

    def daq_flush_multiple(self, **kwargs):
        return self.call('daq_flush_multiple', kwargs=kwargs)

    def set_trigger_io(self, **kwargs):
        return self.call('set_trigger_io', kwargs=kwargs)

    def get_trigger_io(self, **kwargs):
        return self.call('get_trigger_io', kwargs=kwargs)

    def reset_clock_phase(self, **kwargs):
        return self.call('reset_clock_phase', kwargs=kwargs)

    def set_clksys_frequency(self, **kwargs):
        return self.call('set_clksys_frequency', kwargs=kwargs)

    def get_prescaler(self, **kwargs):
        return self.call('get_prescaler', kwargs=kwargs)

    def set_prescaler(self, **kwargs):
        return self.call('set_prescaler', kwargs=kwargs)

    def get_full_scale(self, **kwargs):
        return self.call('get_full_scale', kwargs=kwargs)

    def set_full_scale(self, **kwargs):
        return self.call('set_full_scale', kwargs=kwargs)

    def get_impedance(self, **kwargs):
        return self.call('get_impedance', kwargs=kwargs)

    def set_impedance(self, **kwargs):
        return self.call('set_impedance', kwargs=kwargs)

    def get_coupling(self, **kwargs):
        return self.call('get_coupling', kwargs=kwargs)

    def set_coupling(self, **kwargs):
        return self.call('set_coupling', kwargs=kwargs)

    def set_trigger_mode(self, **kwargs):
        return self.call('set_trigger_mode', kwargs=kwargs)

    def get_trigger_mode(self, **kwargs):
        return self.call('get_trigger_mode', kwargs=kwargs)

    def set_trigger_threshold(self, **kwargs):
        return self.call('set_trigger_threshold', kwargs=kwargs)

    def get_trigger_threshold(self, **kwargs):
        return self.call('get_trigger_threshold', kwargs=kwargs)

    def set_points_per_cycle(self, **kwargs):
        return self.call('set_points_per_cycle', kwargs=kwargs)

    def set_n_cycles(self, **kwargs):
        return self.call('set_n_cycles', kwargs=kwargs)

    def set_daq_trigger_delay(self, **kwargs):
        return self.call('set_daq_trigger_delay', kwargs=kwargs)

    def set_daq_trigger_mode(self, **kwargs):
        return self.call('set_daq_trigger_mode', kwargs=kwargs)

    def set_digital_trigger_mode(self, **kwargs):
        return self.call('set_digital_trigger_mode', kwargs=kwargs)

    def set_digital_trigger_source(self, **kwargs):
        return self.call('set_digital_trigger_source', kwargs=kwargs)

    def set_analog_trigger_mask(self, **kwargs):
        return self.call('set_analog_trigger_mask', kwargs=kwargs)

    def set_ext_trigger_source(self, **kwargs):
        return self.call('set_ext_trigger_source', kwargs=kwargs)

    def set_ext_trigger_behaviour(self, **kwargs):
        return self.call('set_ext_trigger_behaviour', kwargs=kwargs)

    def set_n_points(self, **kwargs):
        return self.call('set_n_points', kwargs=kwargs)

    def set_timeout(self, **kwargs):
        return self.call('set_timeout', kwargs=kwargs)

    def get_trigger_direction(self, **kwargs):
        return self.call('get_trigger_direction', kwargs=kwargs)

    def set_trigger_direction(self, **kwargs):
        return self.call('set_trigger_direction', kwargs=kwargs)

    def get_sys_frequency(self, **kwargs):
        return self.call('get_sys_frequency', kwargs=kwargs)

    def set_sys_frequency(self, **kwargs):
        return self.call('set_sys_frequency', kwargs=kwargs)

    def get_sync_frequency(self, **kwargs):
        return self.call('get_sync_frequency', kwargs=kwargs)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def get_module_count(self, **kwargs):
        return self.call('get_module_count', kwargs=kwargs)

    def get_product_name(self, **kwargs):
        return self.call('get_product_name', kwargs=kwargs)

    def get_serial_number(self, **kwargs):
        return self.call('get_serial_number', kwargs=kwargs)

    def get_chassis(self, **kwargs):
        return self.call('get_chassis', kwargs=kwargs)

    def get_slot(self, **kwargs):
        return self.call('get_slot', kwargs=kwargs)

    def get_firmware_version(self, **kwargs):
        return self.call('get_firmware_version', kwargs=kwargs)

    def get_hardware_version(self, **kwargs):
        return self.call('get_hardware_version', kwargs=kwargs)

    def get_type(self, **kwargs):
        return self.call('get_type', kwargs=kwargs)

    def get_open(self, **kwargs):
        return self.call('get_open', kwargs=kwargs)

    def get_pxi_trigger(self, **kwargs):
        return self.call('get_pxi_trigger', kwargs=kwargs)

    def set_pxi_trigger(self, **kwargs):
        return self.call('set_pxi_trigger', kwargs=kwargs)

    def get_fpga_pc_port(self, **kwargs):
        return self.call('get_fpga_pc_port', kwargs=kwargs)

    def set_fpga_pc_port(self, **kwargs):
        return self.call('set_fpga_pc_port', kwargs=kwargs)

    def load_fpga_image(self, **kwargs):
        return self.call('load_fpga_image', kwargs=kwargs)

    def set_hvi_register(self, **kwargs):
        return self.call('set_hvi_register', kwargs=kwargs)

    def get_hvi_register(self, **kwargs):
        return self.call('get_hvi_register', kwargs=kwargs)

    def get_product_name_by_slot(self, **kwargs):
        return self.call('get_product_name_by_slot', kwargs=kwargs)

    def get_product_name_by_index(self, **kwargs):
        return self.call('get_product_name_by_index', kwargs=kwargs)

    def get_serial_number_by_slot(self, **kwargs):
        return self.call('get_serial_number_by_slot', kwargs=kwargs)

    def get_serial_number_by_index(self, **kwargs):
        return self.call('get_serial_number_by_index', kwargs=kwargs)

    def get_type_by_slot(self, **kwargs):
        return self.call('get_type_by_slot', kwargs=kwargs)

    def get_type_by_index(self, **kwargs):
        return self.call('get_type_by_index', kwargs=kwargs)

    def get_temperature(self, **kwargs):
        return self.call('get_temperature', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def close_soft(self, **kwargs):
        return self.call('close_soft', kwargs=kwargs)

    def open_with_serial_number(self, **kwargs):
        return self.call('open_with_serial_number', kwargs=kwargs)

    def open_with_slot(self, **kwargs):
        return self.call('open_with_slot', kwargs=kwargs)

    def run_self_test(self, **kwargs):
        return self.call('run_self_test', kwargs=kwargs)

    def get_chassis_number(self, **kwargs):
        return self.call('get_chassis_number', kwargs=kwargs)

    def get_slot_number(self, **kwargs):
        return self.call('get_slot_number', kwargs=kwargs)

    def get_instrument_type(self, **kwargs):
        return self.call('get_instrument_type', kwargs=kwargs)

