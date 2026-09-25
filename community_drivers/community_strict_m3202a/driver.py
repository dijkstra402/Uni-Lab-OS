from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictM3202a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Keysight/M3202A.py', 'class_name': 'M3202A', 'import_roots': ['src'], 'candidate_methods': ['asynchronous', 'set_asynchronous', 'load_waveform', 'load_waveform_int16', 'reload_waveform', 'reload_waveform_int16', 'flush_waveform', 'awg_from_file', 'awg_from_array', 'awg_flush', 'uploader_ready', 'awg_queue_waveform', 'set_waveform_limit', 'upload_waveform', 'release_waveform_memory', 'close', 'get_trigger_io', 'get_clock_frequency', 'get_clock_sync_frequency', 'set_clock_frequency', 'set_channel_frequency', 'set_channel_phase', 'set_channel_amplitude', 'set_channel_offset', 'set_channel_wave_shape', 'set_digital_filter_mode', 'set_trigger_io', 'set_marker_config', 'off', 'reset_clock_phase', 'reset_channel_phase', 'reset_multiple_channel_phase', 'config_angle_modulation', 'config_amplitude_modulation', 'set_iq_modulation', 'config_clock_io', 'config_trigger_io', 'awg_queue_config', 'awg_start', 'awg_start_multiple', 'awg_pause', 'awg_pause_multiple', 'awg_resume', 'awg_resume_multiple', 'awg_stop', 'awg_stop_multiple', 'awg_jump_next_waveform', 'awg_config_external_trigger', 'awg_trigger', 'awg_trigger_multiple', 'awg_is_running', 'new_waveform_from_file', 'new_waveform_from_double', 'new_waveform_from_int', 'get_waveform_status', 'get_waveform_type', 'load_fpga_image', 'write_fpga', 'read_fpga', 'write_fpga_array', 'read_fpga_array', 'config_fpga_trigger', 'convert_sample_rate_to_prescaler', 'convert_prescaler_to_sample_rate', 'get_idn', 'get_module_count', 'get_product_name', 'get_serial_number', 'get_chassis', 'get_slot', 'get_firmware_version', 'get_hardware_version', 'get_type', 'get_open', 'get_pxi_trigger', 'set_pxi_trigger', 'get_fpga_pc_port', 'set_fpga_pc_port', 'set_hvi_register', 'get_hvi_register', 'get_product_name_by_slot', 'get_product_name_by_index', 'get_serial_number_by_slot', 'get_serial_number_by_index', 'get_type_by_slot', 'get_type_by_index', 'get_temperature', 'close_soft', 'open_with_serial_number', 'open_with_slot', 'run_self_test', 'get_chassis_number', 'get_slot_number', 'get_instrument_type'], 'action_targets': {'get_trigger_io': '__qcodes_param_get__trigger_io', 'get_clock_frequency': '__qcodes_param_get__clock_frequency', 'get_clock_sync_frequency': '__qcodes_param_get__clock_sync_frequency', 'set_clock_frequency': '__qcodes_param_set__clock_frequency', 'set_trigger_io': '__qcodes_param_set__trigger_io', 'get_module_count': '__qcodes_param_get__module_count', 'get_product_name': '__qcodes_param_get__product_name', 'get_serial_number': '__qcodes_param_get__serial_number', 'get_firmware_version': '__qcodes_param_get__firmware_version', 'get_hardware_version': '__qcodes_param_get__hardware_version', 'get_open': '__qcodes_param_get__open', 'get_temperature': '__qcodes_param_get__temperature', 'get_chassis_number': '__qcodes_param_get__chassis_number', 'get_slot_number': '__qcodes_param_get__slot_number', 'get_instrument_type': '__qcodes_param_get__instrument_type'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'source_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers/blob/main/src/qcodes_contrib_drivers/drivers/Keysight/M3202A.py', 'confidence': 0.9, 'quality_score': 1.06, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_trigger_io': '__qcodes_param_get__trigger_io', 'get_clock_frequency': '__qcodes_param_get__clock_frequency', 'get_clock_sync_frequency': '__qcodes_param_get__clock_sync_frequency', 'set_clock_frequency': '__qcodes_param_set__clock_frequency', 'set_trigger_io': '__qcodes_param_set__trigger_io', 'get_module_count': '__qcodes_param_get__module_count', 'get_product_name': '__qcodes_param_get__product_name', 'get_serial_number': '__qcodes_param_get__serial_number', 'get_firmware_version': '__qcodes_param_get__firmware_version', 'get_hardware_version': '__qcodes_param_get__hardware_version', 'get_open': '__qcodes_param_get__open', 'get_temperature': '__qcodes_param_get__temperature', 'get_chassis_number': '__qcodes_param_get__chassis_number', 'get_slot_number': '__qcodes_param_get__slot_number', 'get_instrument_type': '__qcodes_param_get__instrument_type'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def asynchronous(self, **kwargs):
        return self.call('asynchronous', kwargs=kwargs)

    def set_asynchronous(self, **kwargs):
        return self.call('set_asynchronous', kwargs=kwargs)

    def load_waveform(self, **kwargs):
        return self.call('load_waveform', kwargs=kwargs)

    def load_waveform_int16(self, **kwargs):
        return self.call('load_waveform_int16', kwargs=kwargs)

    def reload_waveform(self, **kwargs):
        return self.call('reload_waveform', kwargs=kwargs)

    def reload_waveform_int16(self, **kwargs):
        return self.call('reload_waveform_int16', kwargs=kwargs)

    def flush_waveform(self, **kwargs):
        return self.call('flush_waveform', kwargs=kwargs)

    def awg_from_file(self, **kwargs):
        return self.call('awg_from_file', kwargs=kwargs)

    def awg_from_array(self, **kwargs):
        return self.call('awg_from_array', kwargs=kwargs)

    def awg_flush(self, **kwargs):
        return self.call('awg_flush', kwargs=kwargs)

    def uploader_ready(self, **kwargs):
        return self.call('uploader_ready', kwargs=kwargs)

    def awg_queue_waveform(self, **kwargs):
        return self.call('awg_queue_waveform', kwargs=kwargs)

    def set_waveform_limit(self, **kwargs):
        return self.call('set_waveform_limit', kwargs=kwargs)

    def upload_waveform(self, **kwargs):
        return self.call('upload_waveform', kwargs=kwargs)

    def release_waveform_memory(self, **kwargs):
        return self.call('release_waveform_memory', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def get_trigger_io(self, **kwargs):
        return self.call('get_trigger_io', kwargs=kwargs)

    def get_clock_frequency(self, **kwargs):
        return self.call('get_clock_frequency', kwargs=kwargs)

    def get_clock_sync_frequency(self, **kwargs):
        return self.call('get_clock_sync_frequency', kwargs=kwargs)

    def set_clock_frequency(self, **kwargs):
        return self.call('set_clock_frequency', kwargs=kwargs)

    def set_channel_frequency(self, **kwargs):
        return self.call('set_channel_frequency', kwargs=kwargs)

    def set_channel_phase(self, **kwargs):
        return self.call('set_channel_phase', kwargs=kwargs)

    def set_channel_amplitude(self, **kwargs):
        return self.call('set_channel_amplitude', kwargs=kwargs)

    def set_channel_offset(self, **kwargs):
        return self.call('set_channel_offset', kwargs=kwargs)

    def set_channel_wave_shape(self, **kwargs):
        return self.call('set_channel_wave_shape', kwargs=kwargs)

    def set_digital_filter_mode(self, **kwargs):
        return self.call('set_digital_filter_mode', kwargs=kwargs)

    def set_trigger_io(self, **kwargs):
        return self.call('set_trigger_io', kwargs=kwargs)

    def set_marker_config(self, **kwargs):
        return self.call('set_marker_config', kwargs=kwargs)

    def off(self, **kwargs):
        return self.call('off', kwargs=kwargs)

    def reset_clock_phase(self, **kwargs):
        return self.call('reset_clock_phase', kwargs=kwargs)

    def reset_channel_phase(self, **kwargs):
        return self.call('reset_channel_phase', kwargs=kwargs)

    def reset_multiple_channel_phase(self, **kwargs):
        return self.call('reset_multiple_channel_phase', kwargs=kwargs)

    def config_angle_modulation(self, **kwargs):
        return self.call('config_angle_modulation', kwargs=kwargs)

    def config_amplitude_modulation(self, **kwargs):
        return self.call('config_amplitude_modulation', kwargs=kwargs)

    def set_iq_modulation(self, **kwargs):
        return self.call('set_iq_modulation', kwargs=kwargs)

    def config_clock_io(self, **kwargs):
        return self.call('config_clock_io', kwargs=kwargs)

    def config_trigger_io(self, **kwargs):
        return self.call('config_trigger_io', kwargs=kwargs)

    def awg_queue_config(self, **kwargs):
        return self.call('awg_queue_config', kwargs=kwargs)

    def awg_start(self, **kwargs):
        return self.call('awg_start', kwargs=kwargs)

    def awg_start_multiple(self, **kwargs):
        return self.call('awg_start_multiple', kwargs=kwargs)

    def awg_pause(self, **kwargs):
        return self.call('awg_pause', kwargs=kwargs)

    def awg_pause_multiple(self, **kwargs):
        return self.call('awg_pause_multiple', kwargs=kwargs)

    def awg_resume(self, **kwargs):
        return self.call('awg_resume', kwargs=kwargs)

    def awg_resume_multiple(self, **kwargs):
        return self.call('awg_resume_multiple', kwargs=kwargs)

    def awg_stop(self, **kwargs):
        return self.call('awg_stop', kwargs=kwargs)

    def awg_stop_multiple(self, **kwargs):
        return self.call('awg_stop_multiple', kwargs=kwargs)

    def awg_jump_next_waveform(self, **kwargs):
        return self.call('awg_jump_next_waveform', kwargs=kwargs)

    def awg_config_external_trigger(self, **kwargs):
        return self.call('awg_config_external_trigger', kwargs=kwargs)

    def awg_trigger(self, **kwargs):
        return self.call('awg_trigger', kwargs=kwargs)

    def awg_trigger_multiple(self, **kwargs):
        return self.call('awg_trigger_multiple', kwargs=kwargs)

    def awg_is_running(self, **kwargs):
        return self.call('awg_is_running', kwargs=kwargs)

    def new_waveform_from_file(self, **kwargs):
        return self.call('new_waveform_from_file', kwargs=kwargs)

    def new_waveform_from_double(self, **kwargs):
        return self.call('new_waveform_from_double', kwargs=kwargs)

    def new_waveform_from_int(self, **kwargs):
        return self.call('new_waveform_from_int', kwargs=kwargs)

    def get_waveform_status(self, **kwargs):
        return self.call('get_waveform_status', kwargs=kwargs)

    def get_waveform_type(self, **kwargs):
        return self.call('get_waveform_type', kwargs=kwargs)

    def load_fpga_image(self, **kwargs):
        return self.call('load_fpga_image', kwargs=kwargs)

    def write_fpga(self, **kwargs):
        return self.call('write_fpga', kwargs=kwargs)

    def read_fpga(self, **kwargs):
        return self.call('read_fpga', kwargs=kwargs)

    def write_fpga_array(self, **kwargs):
        return self.call('write_fpga_array', kwargs=kwargs)

    def read_fpga_array(self, **kwargs):
        return self.call('read_fpga_array', kwargs=kwargs)

    def config_fpga_trigger(self, **kwargs):
        return self.call('config_fpga_trigger', kwargs=kwargs)

    def convert_sample_rate_to_prescaler(self, **kwargs):
        return self.call('convert_sample_rate_to_prescaler', kwargs=kwargs)

    def convert_prescaler_to_sample_rate(self, **kwargs):
        return self.call('convert_prescaler_to_sample_rate', kwargs=kwargs)

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

