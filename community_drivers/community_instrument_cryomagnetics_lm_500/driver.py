from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentCryomagneticsLm500(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/QCoDeS__Qcodes_contrib_drivers', 'source_file': 'src/qcodes_contrib_drivers/drivers/Siglent/sdg_channel.py', 'class_name': 'SiglentSDGChannel', 'import_roots': ['src'], 'candidate_methods': ['get_raw_outp', 'set_raw_outp', 'get_enabled', 'set_enabled', 'get_load', 'set_load', 'get_polarity', 'set_polarity', 'get_raw_basic_wave', 'set_raw_basic_wave', 'get_wave_type', 'set_wave_type', 'get_frequency', 'set_frequency', 'get_period', 'set_period', 'get_amplitude', 'set_amplitude', 'get_amplitude_rms', 'set_amplitude_rms', 'get_amplitude_dbm', 'set_amplitude_dbm', 'get_offset', 'set_offset', 'get_common_offset', 'set_common_offset', 'get_ramp_symmetry', 'set_ramp_symmetry', 'get_duty_cycle', 'set_duty_cycle', 'get_phase', 'set_phase', 'get_noise_std_dev', 'set_noise_std_dev', 'get_noise_mean', 'set_noise_mean', 'get_pulse_width', 'set_pulse_width', 'get_rise_time', 'set_rise_time', 'get_fall_time', 'set_fall_time', 'get_delay', 'set_delay', 'get_high_level', 'set_high_level', 'get_low_level', 'set_low_level', 'get_noise_bandwidth_enabled', 'set_noise_bandwidth_enabled', 'get_noise_bandwidth', 'set_noise_bandwidth', 'get_prbs_length', 'set_prbs_length', 'get_prbs_edge_time', 'set_prbs_edge_time', 'get_differential_mode', 'set_differential_mode', 'get_prbs_differential_mode', 'set_prbs_differential_mode', 'get_prbs_bit_rate', 'set_prbs_bit_rate', 'get_prbs_logic_level', 'set_prbs_logic_level', 'get_raw_modulate_wave', 'set_raw_modulate_wave', 'get_modulate_wave', 'set_modulate_wave', 'get_mod_am_src', 'set_mod_am_src', 'get_mod_am_shape', 'set_mod_am_shape', 'get_mod_am_frequency', 'set_mod_am_frequency', 'get_mod_am_depth', 'set_mod_am_depth', 'get_mod_dsb_am_src', 'set_mod_dsb_am_src', 'get_mod_dsb_am_shape', 'set_mod_dsb_am_shape', 'get_mod_dsb_am_frequency', 'set_mod_dsb_am_frequency', 'get_mod_fm_src', 'set_mod_fm_src', 'get_mod_fm_shape', 'set_mod_fm_shape', 'get_mod_fm_frequency', 'set_mod_fm_frequency', 'get_mod_fm_deviation', 'set_mod_fm_deviation', 'get_mod_pm_src', 'set_mod_pm_src', 'get_mod_pm_shape', 'set_mod_pm_shape', 'get_mod_pm_frequency', 'set_mod_pm_frequency', 'get_mod_pm_deviation', 'set_mod_pm_deviation', 'get_mod_pwm_src', 'set_mod_pwm_src', 'get_mod_pwm_frequency', 'set_mod_pwm_frequency', 'get_mod_pwm_width_deviation', 'set_mod_pwm_width_deviation', 'get_mod_pwm_duty_cycle_deviation', 'set_mod_pwm_duty_cycle_deviation', 'get_mod_pwm_shape', 'set_mod_pwm_shape', 'get_mod_ask_src', 'set_mod_ask_src', 'get_mod_ask_key_frequency', 'set_mod_ask_key_frequency', 'get_mod_fsk_src', 'set_mod_fsk_src', 'get_mod_fsk_key_frequency', 'set_mod_fsk_key_frequency', 'get_mod_fsk_hop_frequency', 'set_mod_fsk_hop_frequency', 'get_mod_psk_src', 'set_mod_psk_src', 'get_mod_psk_key_frequency', 'set_mod_psk_key_frequency', 'get_mod_carrier_wave_type', 'set_mod_carrier_wave_type', 'get_mod_carrier_frequency', 'set_mod_carrier_frequency', 'get_mod_carrier_phase', 'set_mod_carrier_phase', 'get_mod_carrier_amplitude', 'set_mod_carrier_amplitude', 'get_mod_carrier_amplitude_rms', 'set_mod_carrier_amplitude_rms', 'get_mod_carrier_offset', 'set_mod_carrier_offset', 'get_mod_carrier_ramp_symmetry', 'set_mod_carrier_ramp_symmetry', 'get_mod_carrier_duty_cycle', 'set_mod_carrier_duty_cycle', 'get_raw_sweep_wave', 'set_raw_sweep_wave', 'get_sweep_wave', 'set_sweep_wave', 'get_sweep_time', 'set_sweep_time', 'get_sweep_start_frequency', 'set_sweep_start_frequency', 'get_sweep_stop_frequency', 'set_sweep_stop_frequency', 'get_sweep_mode', 'set_sweep_mode', 'get_sweep_direction', 'set_sweep_direction', 'get_sweep_symmetry', 'set_sweep_symmetry', 'get_sweep_trigger_source', 'set_sweep_trigger_source', 'get_sweep_carrier_wave_type', 'set_sweep_carrier_wave_type', 'get_sweep_carrier_frequency', 'set_sweep_carrier_frequency', 'get_sweep_carrier_phase', 'set_sweep_carrier_phase', 'get_sweep_carrier_amplitude', 'set_sweep_carrier_amplitude', 'get_sweep_carrier_amplitude_rms', 'set_sweep_carrier_amplitude_rms', 'get_sweep_carrier_offset', 'set_sweep_carrier_offset', 'get_sweep_carrier_ramp_symmetry', 'set_sweep_carrier_ramp_symmetry', 'get_sweep_carrier_duty_cycle', 'set_sweep_carrier_duty_cycle', 'get_sweep_mark', 'set_sweep_mark', 'get_sweep_mark_frequency', 'set_sweep_mark_frequency', 'get_raw_burst_wave', 'set_raw_burst_wave', 'get_burst_wave', 'set_burst_wave', 'get_burst_period', 'set_burst_period', 'get_burst_start_phase', 'set_burst_start_phase', 'get_burst_mode', 'set_burst_mode', 'get_burst_trigger_source', 'set_burst_trigger_source', 'get_burst_trigger_delay', 'set_burst_trigger_delay', 'get_burst_gate_polarity', 'set_burst_gate_polarity', 'get_burst_ncycles', 'set_burst_ncycles', 'get_burst_carrier_wave_type', 'set_burst_carrier_wave_type', 'get_burst_carrier_frequency', 'set_burst_carrier_frequency', 'get_burst_carrier_phase', 'set_burst_carrier_phase', 'get_burst_carrier_amplitude', 'set_burst_carrier_amplitude', 'get_burst_carrier_amplitude_rms', 'set_burst_carrier_amplitude_rms', 'get_burst_carrier_offset', 'set_burst_carrier_offset', 'get_burst_carrier_ramp_symmetry', 'set_burst_carrier_ramp_symmetry', 'get_burst_carrier_duty_cycle', 'set_burst_carrier_duty_cycle', 'get_burst_carrier_noise_std_dev', 'set_burst_carrier_noise_std_dev', 'get_burst_carrier_noise_mean', 'set_burst_carrier_noise_mean', 'get_raw_arbitrary_wave', 'set_raw_arbitrary_wave', 'get_arbitrary_wave_index', 'set_arbitrary_wave_index', 'get_arbitrary_wave_name', 'set_arbitrary_wave_name', 'get_raw_sync', 'set_raw_sync', 'get_sync_enabled', 'set_sync_enabled', 'get_sync_type', 'set_sync_type', 'get_inverted', 'set_inverted', 'get_poweron_state', 'set_poweron_state', 'get_max_output_amp', 'set_max_output_amp', 'get_mod_dsb_sc_src', 'set_mod_dsb_sc_src', 'get_mod_dsb_sc_shape', 'set_mod_dsb_sc_shape', 'get_mod_dsb_sc_frequency', 'set_mod_dsb_sc_frequency', 'get_mod_carrier_rise_time', 'set_mod_carrier_rise_time', 'get_mod_carrier_fall_time', 'set_mod_carrier_fall_time', 'get_mod_carrier_delay', 'set_mod_carrier_delay', 'get_sweep_start_hold_time', 'set_sweep_start_hold_time', 'get_sweep_end_hold_time', 'set_sweep_end_hold_time', 'get_sweep_back_time', 'set_sweep_back_time', 'get_sweep_center_frequency', 'set_sweep_center_frequency', 'get_sweep_frequency_span', 'set_sweep_frequency_span', 'get_sweep_trigger_output', 'set_sweep_trigger_output', 'get_sweep_trigger_edge', 'set_sweep_trigger_edge', 'get_burst_trigger_output_mode', 'set_burst_trigger_output_mode', 'get_burst_trigger_edge', 'set_burst_trigger_edge', 'get_burst_counter', 'set_burst_counter', 'get_burst_carrier_rise_time', 'set_burst_carrier_rise_time', 'get_burst_carrier_fall_time', 'set_burst_carrier_fall_time', 'get_burst_carrier_delay', 'set_burst_carrier_delay', 'channel_number'], 'action_targets': {'get_raw_outp': '__qcodes_param_get__raw_outp', 'set_raw_outp': '__qcodes_param_set__raw_outp', 'get_enabled': '__qcodes_param_get__enabled', 'set_enabled': '__qcodes_param_set__enabled', 'get_load': '__qcodes_param_get__load', 'set_load': '__qcodes_param_set__load', 'get_polarity': '__qcodes_param_get__polarity', 'set_polarity': '__qcodes_param_set__polarity', 'get_raw_basic_wave': '__qcodes_param_get__raw_basic_wave', 'set_raw_basic_wave': '__qcodes_param_set__raw_basic_wave', 'get_wave_type': '__qcodes_param_get__wave_type', 'set_wave_type': '__qcodes_param_set__wave_type', 'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_period': '__qcodes_param_get__period', 'set_period': '__qcodes_param_set__period', 'get_amplitude': '__qcodes_param_get__amplitude', 'set_amplitude': '__qcodes_param_set__amplitude', 'get_amplitude_rms': '__qcodes_param_get__amplitude_rms', 'set_amplitude_rms': '__qcodes_param_set__amplitude_rms', 'get_amplitude_dbm': '__qcodes_param_get__amplitude_dbm', 'set_amplitude_dbm': '__qcodes_param_set__amplitude_dbm', 'get_offset': '__qcodes_param_get__offset', 'set_offset': '__qcodes_param_set__offset', 'get_common_offset': '__qcodes_param_get__common_offset', 'set_common_offset': '__qcodes_param_set__common_offset', 'get_ramp_symmetry': '__qcodes_param_get__ramp_symmetry', 'set_ramp_symmetry': '__qcodes_param_set__ramp_symmetry', 'get_duty_cycle': '__qcodes_param_get__duty_cycle', 'set_duty_cycle': '__qcodes_param_set__duty_cycle', 'get_phase': '__qcodes_param_get__phase', 'set_phase': '__qcodes_param_set__phase', 'get_noise_std_dev': '__qcodes_param_get__noise_std_dev', 'set_noise_std_dev': '__qcodes_param_set__noise_std_dev', 'get_noise_mean': '__qcodes_param_get__noise_mean', 'set_noise_mean': '__qcodes_param_set__noise_mean', 'get_pulse_width': '__qcodes_param_get__pulse_width', 'set_pulse_width': '__qcodes_param_set__pulse_width', 'get_rise_time': '__qcodes_param_get__rise_time', 'set_rise_time': '__qcodes_param_set__rise_time', 'get_fall_time': '__qcodes_param_get__fall_time', 'set_fall_time': '__qcodes_param_set__fall_time', 'get_delay': '__qcodes_param_get__delay', 'set_delay': '__qcodes_param_set__delay', 'get_high_level': '__qcodes_param_get__high_level', 'set_high_level': '__qcodes_param_set__high_level', 'get_low_level': '__qcodes_param_get__low_level', 'set_low_level': '__qcodes_param_set__low_level', 'get_noise_bandwidth_enabled': '__qcodes_param_get__noise_bandwidth_enabled', 'set_noise_bandwidth_enabled': '__qcodes_param_set__noise_bandwidth_enabled', 'get_noise_bandwidth': '__qcodes_param_get__noise_bandwidth', 'set_noise_bandwidth': '__qcodes_param_set__noise_bandwidth', 'get_prbs_length': '__qcodes_param_get__prbs_length', 'set_prbs_length': '__qcodes_param_set__prbs_length', 'get_prbs_edge_time': '__qcodes_param_get__prbs_edge_time', 'set_prbs_edge_time': '__qcodes_param_set__prbs_edge_time', 'get_differential_mode': '__qcodes_param_get__differential_mode', 'set_differential_mode': '__qcodes_param_set__differential_mode', 'get_prbs_differential_mode': '__qcodes_param_get__prbs_differential_mode', 'set_prbs_differential_mode': '__qcodes_param_set__prbs_differential_mode', 'get_prbs_bit_rate': '__qcodes_param_get__prbs_bit_rate', 'set_prbs_bit_rate': '__qcodes_param_set__prbs_bit_rate', 'get_prbs_logic_level': '__qcodes_param_get__prbs_logic_level', 'set_prbs_logic_level': '__qcodes_param_set__prbs_logic_level', 'get_raw_modulate_wave': '__qcodes_param_get__raw_modulate_wave', 'set_raw_modulate_wave': '__qcodes_param_set__raw_modulate_wave', 'get_modulate_wave': '__qcodes_param_get__modulate_wave', 'set_modulate_wave': '__qcodes_param_set__modulate_wave', 'get_mod_am_src': '__qcodes_param_get__mod_am_src', 'set_mod_am_src': '__qcodes_param_set__mod_am_src', 'get_mod_am_shape': '__qcodes_param_get__mod_am_shape', 'set_mod_am_shape': '__qcodes_param_set__mod_am_shape', 'get_mod_am_frequency': '__qcodes_param_get__mod_am_frequency', 'set_mod_am_frequency': '__qcodes_param_set__mod_am_frequency', 'get_mod_am_depth': '__qcodes_param_get__mod_am_depth', 'set_mod_am_depth': '__qcodes_param_set__mod_am_depth', 'get_mod_dsb_am_src': '__qcodes_param_get__mod_dsb_am_src', 'set_mod_dsb_am_src': '__qcodes_param_set__mod_dsb_am_src', 'get_mod_dsb_am_shape': '__qcodes_param_get__mod_dsb_am_shape', 'set_mod_dsb_am_shape': '__qcodes_param_set__mod_dsb_am_shape', 'get_mod_dsb_am_frequency': '__qcodes_param_get__mod_dsb_am_frequency', 'set_mod_dsb_am_frequency': '__qcodes_param_set__mod_dsb_am_frequency', 'get_mod_fm_src': '__qcodes_param_get__mod_fm_src', 'set_mod_fm_src': '__qcodes_param_set__mod_fm_src', 'get_mod_fm_shape': '__qcodes_param_get__mod_fm_shape', 'set_mod_fm_shape': '__qcodes_param_set__mod_fm_shape', 'get_mod_fm_frequency': '__qcodes_param_get__mod_fm_frequency', 'set_mod_fm_frequency': '__qcodes_param_set__mod_fm_frequency', 'get_mod_fm_deviation': '__qcodes_param_get__mod_fm_deviation', 'set_mod_fm_deviation': '__qcodes_param_set__mod_fm_deviation', 'get_mod_pm_src': '__qcodes_param_get__mod_pm_src', 'set_mod_pm_src': '__qcodes_param_set__mod_pm_src', 'get_mod_pm_shape': '__qcodes_param_get__mod_pm_shape', 'set_mod_pm_shape': '__qcodes_param_set__mod_pm_shape', 'get_mod_pm_frequency': '__qcodes_param_get__mod_pm_frequency', 'set_mod_pm_frequency': '__qcodes_param_set__mod_pm_frequency', 'get_mod_pm_deviation': '__qcodes_param_get__mod_pm_deviation', 'set_mod_pm_deviation': '__qcodes_param_set__mod_pm_deviation', 'get_mod_pwm_src': '__qcodes_param_get__mod_pwm_src', 'set_mod_pwm_src': '__qcodes_param_set__mod_pwm_src', 'get_mod_pwm_frequency': '__qcodes_param_get__mod_pwm_frequency', 'set_mod_pwm_frequency': '__qcodes_param_set__mod_pwm_frequency', 'get_mod_pwm_width_deviation': '__qcodes_param_get__mod_pwm_width_deviation', 'set_mod_pwm_width_deviation': '__qcodes_param_set__mod_pwm_width_deviation', 'get_mod_pwm_duty_cycle_deviation': '__qcodes_param_get__mod_pwm_duty_cycle_deviation', 'set_mod_pwm_duty_cycle_deviation': '__qcodes_param_set__mod_pwm_duty_cycle_deviation', 'get_mod_pwm_shape': '__qcodes_param_get__mod_pwm_shape', 'set_mod_pwm_shape': '__qcodes_param_set__mod_pwm_shape', 'get_mod_ask_src': '__qcodes_param_get__mod_ask_src', 'set_mod_ask_src': '__qcodes_param_set__mod_ask_src', 'get_mod_ask_key_frequency': '__qcodes_param_get__mod_ask_key_frequency', 'set_mod_ask_key_frequency': '__qcodes_param_set__mod_ask_key_frequency', 'get_mod_fsk_src': '__qcodes_param_get__mod_fsk_src', 'set_mod_fsk_src': '__qcodes_param_set__mod_fsk_src', 'get_mod_fsk_key_frequency': '__qcodes_param_get__mod_fsk_key_frequency', 'set_mod_fsk_key_frequency': '__qcodes_param_set__mod_fsk_key_frequency', 'get_mod_fsk_hop_frequency': '__qcodes_param_get__mod_fsk_hop_frequency', 'set_mod_fsk_hop_frequency': '__qcodes_param_set__mod_fsk_hop_frequency', 'get_mod_psk_src': '__qcodes_param_get__mod_psk_src', 'set_mod_psk_src': '__qcodes_param_set__mod_psk_src', 'get_mod_psk_key_frequency': '__qcodes_param_get__mod_psk_key_frequency', 'set_mod_psk_key_frequency': '__qcodes_param_set__mod_psk_key_frequency', 'get_mod_carrier_wave_type': '__qcodes_param_get__mod_carrier_wave_type', 'set_mod_carrier_wave_type': '__qcodes_param_set__mod_carrier_wave_type', 'get_mod_carrier_frequency': '__qcodes_param_get__mod_carrier_frequency', 'set_mod_carrier_frequency': '__qcodes_param_set__mod_carrier_frequency', 'get_mod_carrier_phase': '__qcodes_param_get__mod_carrier_phase', 'set_mod_carrier_phase': '__qcodes_param_set__mod_carrier_phase', 'get_mod_carrier_amplitude': '__qcodes_param_get__mod_carrier_amplitude', 'set_mod_carrier_amplitude': '__qcodes_param_set__mod_carrier_amplitude', 'get_mod_carrier_amplitude_rms': '__qcodes_param_get__mod_carrier_amplitude_rms', 'set_mod_carrier_amplitude_rms': '__qcodes_param_set__mod_carrier_amplitude_rms', 'get_mod_carrier_offset': '__qcodes_param_get__mod_carrier_offset', 'set_mod_carrier_offset': '__qcodes_param_set__mod_carrier_offset', 'get_mod_carrier_ramp_symmetry': '__qcodes_param_get__mod_carrier_ramp_symmetry', 'set_mod_carrier_ramp_symmetry': '__qcodes_param_set__mod_carrier_ramp_symmetry', 'get_mod_carrier_duty_cycle': '__qcodes_param_get__mod_carrier_duty_cycle', 'set_mod_carrier_duty_cycle': '__qcodes_param_set__mod_carrier_duty_cycle', 'get_raw_sweep_wave': '__qcodes_param_get__raw_sweep_wave', 'set_raw_sweep_wave': '__qcodes_param_set__raw_sweep_wave', 'get_sweep_wave': '__qcodes_param_get__sweep_wave', 'set_sweep_wave': '__qcodes_param_set__sweep_wave', 'get_sweep_time': '__qcodes_param_get__sweep_time', 'set_sweep_time': '__qcodes_param_set__sweep_time', 'get_sweep_start_frequency': '__qcodes_param_get__sweep_start_frequency', 'set_sweep_start_frequency': '__qcodes_param_set__sweep_start_frequency', 'get_sweep_stop_frequency': '__qcodes_param_get__sweep_stop_frequency', 'set_sweep_stop_frequency': '__qcodes_param_set__sweep_stop_frequency', 'get_sweep_mode': '__qcodes_param_get__sweep_mode', 'set_sweep_mode': '__qcodes_param_set__sweep_mode', 'get_sweep_direction': '__qcodes_param_get__sweep_direction', 'set_sweep_direction': '__qcodes_param_set__sweep_direction', 'get_sweep_symmetry': '__qcodes_param_get__sweep_symmetry', 'set_sweep_symmetry': '__qcodes_param_set__sweep_symmetry', 'get_sweep_trigger_source': '__qcodes_param_get__sweep_trigger_source', 'set_sweep_trigger_source': '__qcodes_param_set__sweep_trigger_source', 'get_sweep_carrier_wave_type': '__qcodes_param_get__sweep_carrier_wave_type', 'set_sweep_carrier_wave_type': '__qcodes_param_set__sweep_carrier_wave_type', 'get_sweep_carrier_frequency': '__qcodes_param_get__sweep_carrier_frequency', 'set_sweep_carrier_frequency': '__qcodes_param_set__sweep_carrier_frequency', 'get_sweep_carrier_phase': '__qcodes_param_get__sweep_carrier_phase', 'set_sweep_carrier_phase': '__qcodes_param_set__sweep_carrier_phase', 'get_sweep_carrier_amplitude': '__qcodes_param_get__sweep_carrier_amplitude', 'set_sweep_carrier_amplitude': '__qcodes_param_set__sweep_carrier_amplitude', 'get_sweep_carrier_amplitude_rms': '__qcodes_param_get__sweep_carrier_amplitude_rms', 'set_sweep_carrier_amplitude_rms': '__qcodes_param_set__sweep_carrier_amplitude_rms', 'get_sweep_carrier_offset': '__qcodes_param_get__sweep_carrier_offset', 'set_sweep_carrier_offset': '__qcodes_param_set__sweep_carrier_offset', 'get_sweep_carrier_ramp_symmetry': '__qcodes_param_get__sweep_carrier_ramp_symmetry', 'set_sweep_carrier_ramp_symmetry': '__qcodes_param_set__sweep_carrier_ramp_symmetry', 'get_sweep_carrier_duty_cycle': '__qcodes_param_get__sweep_carrier_duty_cycle', 'set_sweep_carrier_duty_cycle': '__qcodes_param_set__sweep_carrier_duty_cycle', 'get_sweep_mark': '__qcodes_param_get__sweep_mark', 'set_sweep_mark': '__qcodes_param_set__sweep_mark', 'get_sweep_mark_frequency': '__qcodes_param_get__sweep_mark_frequency', 'set_sweep_mark_frequency': '__qcodes_param_set__sweep_mark_frequency', 'get_raw_burst_wave': '__qcodes_param_get__raw_burst_wave', 'set_raw_burst_wave': '__qcodes_param_set__raw_burst_wave', 'get_burst_wave': '__qcodes_param_get__burst_wave', 'set_burst_wave': '__qcodes_param_set__burst_wave', 'get_burst_period': '__qcodes_param_get__burst_period', 'set_burst_period': '__qcodes_param_set__burst_period', 'get_burst_start_phase': '__qcodes_param_get__burst_start_phase', 'set_burst_start_phase': '__qcodes_param_set__burst_start_phase', 'get_burst_mode': '__qcodes_param_get__burst_mode', 'set_burst_mode': '__qcodes_param_set__burst_mode', 'get_burst_trigger_source': '__qcodes_param_get__burst_trigger_source', 'set_burst_trigger_source': '__qcodes_param_set__burst_trigger_source', 'get_burst_trigger_delay': '__qcodes_param_get__burst_trigger_delay', 'set_burst_trigger_delay': '__qcodes_param_set__burst_trigger_delay', 'get_burst_gate_polarity': '__qcodes_param_get__burst_gate_polarity', 'set_burst_gate_polarity': '__qcodes_param_set__burst_gate_polarity', 'get_burst_ncycles': '__qcodes_param_get__burst_ncycles', 'set_burst_ncycles': '__qcodes_param_set__burst_ncycles', 'get_burst_carrier_wave_type': '__qcodes_param_get__burst_carrier_wave_type', 'set_burst_carrier_wave_type': '__qcodes_param_set__burst_carrier_wave_type', 'get_burst_carrier_frequency': '__qcodes_param_get__burst_carrier_frequency', 'set_burst_carrier_frequency': '__qcodes_param_set__burst_carrier_frequency', 'get_burst_carrier_phase': '__qcodes_param_get__burst_carrier_phase', 'set_burst_carrier_phase': '__qcodes_param_set__burst_carrier_phase', 'get_burst_carrier_amplitude': '__qcodes_param_get__burst_carrier_amplitude', 'set_burst_carrier_amplitude': '__qcodes_param_set__burst_carrier_amplitude', 'get_burst_carrier_amplitude_rms': '__qcodes_param_get__burst_carrier_amplitude_rms', 'set_burst_carrier_amplitude_rms': '__qcodes_param_set__burst_carrier_amplitude_rms', 'get_burst_carrier_offset': '__qcodes_param_get__burst_carrier_offset', 'set_burst_carrier_offset': '__qcodes_param_set__burst_carrier_offset', 'get_burst_carrier_ramp_symmetry': '__qcodes_param_get__burst_carrier_ramp_symmetry', 'set_burst_carrier_ramp_symmetry': '__qcodes_param_set__burst_carrier_ramp_symmetry', 'get_burst_carrier_duty_cycle': '__qcodes_param_get__burst_carrier_duty_cycle', 'set_burst_carrier_duty_cycle': '__qcodes_param_set__burst_carrier_duty_cycle', 'get_burst_carrier_noise_std_dev': '__qcodes_param_get__burst_carrier_noise_std_dev', 'set_burst_carrier_noise_std_dev': '__qcodes_param_set__burst_carrier_noise_std_dev', 'get_burst_carrier_noise_mean': '__qcodes_param_get__burst_carrier_noise_mean', 'set_burst_carrier_noise_mean': '__qcodes_param_set__burst_carrier_noise_mean', 'get_raw_arbitrary_wave': '__qcodes_param_get__raw_arbitrary_wave', 'set_raw_arbitrary_wave': '__qcodes_param_set__raw_arbitrary_wave', 'get_arbitrary_wave_index': '__qcodes_param_get__arbitrary_wave_index', 'set_arbitrary_wave_index': '__qcodes_param_set__arbitrary_wave_index', 'get_arbitrary_wave_name': '__qcodes_param_get__arbitrary_wave_name', 'set_arbitrary_wave_name': '__qcodes_param_set__arbitrary_wave_name', 'get_raw_sync': '__qcodes_param_get__raw_sync', 'set_raw_sync': '__qcodes_param_set__raw_sync', 'get_sync_enabled': '__qcodes_param_get__sync_enabled', 'set_sync_enabled': '__qcodes_param_set__sync_enabled', 'get_sync_type': '__qcodes_param_get__sync_type', 'set_sync_type': '__qcodes_param_set__sync_type', 'get_inverted': '__qcodes_param_get__inverted', 'set_inverted': '__qcodes_param_set__inverted', 'get_poweron_state': '__qcodes_param_get__poweron_state', 'set_poweron_state': '__qcodes_param_set__poweron_state', 'get_max_output_amp': '__qcodes_param_get__max_output_amp', 'set_max_output_amp': '__qcodes_param_set__max_output_amp', 'get_mod_dsb_sc_src': '__qcodes_param_get__mod_dsb_sc_src', 'set_mod_dsb_sc_src': '__qcodes_param_set__mod_dsb_sc_src', 'get_mod_dsb_sc_shape': '__qcodes_param_get__mod_dsb_sc_shape', 'set_mod_dsb_sc_shape': '__qcodes_param_set__mod_dsb_sc_shape', 'get_mod_dsb_sc_frequency': '__qcodes_param_get__mod_dsb_sc_frequency', 'set_mod_dsb_sc_frequency': '__qcodes_param_set__mod_dsb_sc_frequency', 'get_mod_carrier_rise_time': '__qcodes_param_get__mod_carrier_rise_time', 'set_mod_carrier_rise_time': '__qcodes_param_set__mod_carrier_rise_time', 'get_mod_carrier_fall_time': '__qcodes_param_get__mod_carrier_fall_time', 'set_mod_carrier_fall_time': '__qcodes_param_set__mod_carrier_fall_time', 'get_mod_carrier_delay': '__qcodes_param_get__mod_carrier_delay', 'set_mod_carrier_delay': '__qcodes_param_set__mod_carrier_delay', 'get_sweep_start_hold_time': '__qcodes_param_get__sweep_start_hold_time', 'set_sweep_start_hold_time': '__qcodes_param_set__sweep_start_hold_time', 'get_sweep_end_hold_time': '__qcodes_param_get__sweep_end_hold_time', 'set_sweep_end_hold_time': '__qcodes_param_set__sweep_end_hold_time', 'get_sweep_back_time': '__qcodes_param_get__sweep_back_time', 'set_sweep_back_time': '__qcodes_param_set__sweep_back_time', 'get_sweep_center_frequency': '__qcodes_param_get__sweep_center_frequency', 'set_sweep_center_frequency': '__qcodes_param_set__sweep_center_frequency', 'get_sweep_frequency_span': '__qcodes_param_get__sweep_frequency_span', 'set_sweep_frequency_span': '__qcodes_param_set__sweep_frequency_span', 'get_sweep_trigger_output': '__qcodes_param_get__sweep_trigger_output', 'set_sweep_trigger_output': '__qcodes_param_set__sweep_trigger_output', 'get_sweep_trigger_edge': '__qcodes_param_get__sweep_trigger_edge', 'set_sweep_trigger_edge': '__qcodes_param_set__sweep_trigger_edge', 'get_burst_trigger_output_mode': '__qcodes_param_get__burst_trigger_output_mode', 'set_burst_trigger_output_mode': '__qcodes_param_set__burst_trigger_output_mode', 'get_burst_trigger_edge': '__qcodes_param_get__burst_trigger_edge', 'set_burst_trigger_edge': '__qcodes_param_set__burst_trigger_edge', 'get_burst_counter': '__qcodes_param_get__burst_counter', 'set_burst_counter': '__qcodes_param_set__burst_counter', 'get_burst_carrier_rise_time': '__qcodes_param_get__burst_carrier_rise_time', 'set_burst_carrier_rise_time': '__qcodes_param_set__burst_carrier_rise_time', 'get_burst_carrier_fall_time': '__qcodes_param_get__burst_carrier_fall_time', 'set_burst_carrier_fall_time': '__qcodes_param_set__burst_carrier_fall_time', 'get_burst_carrier_delay': '__qcodes_param_get__burst_carrier_delay', 'set_burst_carrier_delay': '__qcodes_param_set__burst_carrier_delay'}, 'metadata': {'repo': 'QCoDeS/Qcodes_contrib_drivers', 'repo_url': 'https://github.com/QCoDeS/Qcodes_contrib_drivers', 'brand': 'Cryomagnetics', 'model': 'LM-500', 'device_type_cn': '液位计', 'device_type_en': 'Level Meter', 'source_framework': 'QCoDeS-Contrib', 'tag_id': '4369', 'tag_name': '冷热水机', 'tag_name_en': 'Chiller / Heater Unit', 'candidate_score': 2214, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_raw_outp': '__qcodes_param_get__raw_outp', 'set_raw_outp': '__qcodes_param_set__raw_outp', 'get_enabled': '__qcodes_param_get__enabled', 'set_enabled': '__qcodes_param_set__enabled', 'get_load': '__qcodes_param_get__load', 'set_load': '__qcodes_param_set__load', 'get_polarity': '__qcodes_param_get__polarity', 'set_polarity': '__qcodes_param_set__polarity', 'get_raw_basic_wave': '__qcodes_param_get__raw_basic_wave', 'set_raw_basic_wave': '__qcodes_param_set__raw_basic_wave', 'get_wave_type': '__qcodes_param_get__wave_type', 'set_wave_type': '__qcodes_param_set__wave_type', 'get_frequency': '__qcodes_param_get__frequency', 'set_frequency': '__qcodes_param_set__frequency', 'get_period': '__qcodes_param_get__period', 'set_period': '__qcodes_param_set__period', 'get_amplitude': '__qcodes_param_get__amplitude', 'set_amplitude': '__qcodes_param_set__amplitude', 'get_amplitude_rms': '__qcodes_param_get__amplitude_rms', 'set_amplitude_rms': '__qcodes_param_set__amplitude_rms', 'get_amplitude_dbm': '__qcodes_param_get__amplitude_dbm', 'set_amplitude_dbm': '__qcodes_param_set__amplitude_dbm', 'get_offset': '__qcodes_param_get__offset', 'set_offset': '__qcodes_param_set__offset', 'get_common_offset': '__qcodes_param_get__common_offset', 'set_common_offset': '__qcodes_param_set__common_offset', 'get_ramp_symmetry': '__qcodes_param_get__ramp_symmetry', 'set_ramp_symmetry': '__qcodes_param_set__ramp_symmetry', 'get_duty_cycle': '__qcodes_param_get__duty_cycle', 'set_duty_cycle': '__qcodes_param_set__duty_cycle', 'get_phase': '__qcodes_param_get__phase', 'set_phase': '__qcodes_param_set__phase', 'get_noise_std_dev': '__qcodes_param_get__noise_std_dev', 'set_noise_std_dev': '__qcodes_param_set__noise_std_dev', 'get_noise_mean': '__qcodes_param_get__noise_mean', 'set_noise_mean': '__qcodes_param_set__noise_mean', 'get_pulse_width': '__qcodes_param_get__pulse_width', 'set_pulse_width': '__qcodes_param_set__pulse_width', 'get_rise_time': '__qcodes_param_get__rise_time', 'set_rise_time': '__qcodes_param_set__rise_time', 'get_fall_time': '__qcodes_param_get__fall_time', 'set_fall_time': '__qcodes_param_set__fall_time', 'get_delay': '__qcodes_param_get__delay', 'set_delay': '__qcodes_param_set__delay', 'get_high_level': '__qcodes_param_get__high_level', 'set_high_level': '__qcodes_param_set__high_level', 'get_low_level': '__qcodes_param_get__low_level', 'set_low_level': '__qcodes_param_set__low_level', 'get_noise_bandwidth_enabled': '__qcodes_param_get__noise_bandwidth_enabled', 'set_noise_bandwidth_enabled': '__qcodes_param_set__noise_bandwidth_enabled', 'get_noise_bandwidth': '__qcodes_param_get__noise_bandwidth', 'set_noise_bandwidth': '__qcodes_param_set__noise_bandwidth', 'get_prbs_length': '__qcodes_param_get__prbs_length', 'set_prbs_length': '__qcodes_param_set__prbs_length', 'get_prbs_edge_time': '__qcodes_param_get__prbs_edge_time', 'set_prbs_edge_time': '__qcodes_param_set__prbs_edge_time', 'get_differential_mode': '__qcodes_param_get__differential_mode', 'set_differential_mode': '__qcodes_param_set__differential_mode', 'get_prbs_differential_mode': '__qcodes_param_get__prbs_differential_mode', 'set_prbs_differential_mode': '__qcodes_param_set__prbs_differential_mode', 'get_prbs_bit_rate': '__qcodes_param_get__prbs_bit_rate', 'set_prbs_bit_rate': '__qcodes_param_set__prbs_bit_rate', 'get_prbs_logic_level': '__qcodes_param_get__prbs_logic_level', 'set_prbs_logic_level': '__qcodes_param_set__prbs_logic_level', 'get_raw_modulate_wave': '__qcodes_param_get__raw_modulate_wave', 'set_raw_modulate_wave': '__qcodes_param_set__raw_modulate_wave', 'get_modulate_wave': '__qcodes_param_get__modulate_wave', 'set_modulate_wave': '__qcodes_param_set__modulate_wave', 'get_mod_am_src': '__qcodes_param_get__mod_am_src', 'set_mod_am_src': '__qcodes_param_set__mod_am_src', 'get_mod_am_shape': '__qcodes_param_get__mod_am_shape', 'set_mod_am_shape': '__qcodes_param_set__mod_am_shape', 'get_mod_am_frequency': '__qcodes_param_get__mod_am_frequency', 'set_mod_am_frequency': '__qcodes_param_set__mod_am_frequency', 'get_mod_am_depth': '__qcodes_param_get__mod_am_depth', 'set_mod_am_depth': '__qcodes_param_set__mod_am_depth', 'get_mod_dsb_am_src': '__qcodes_param_get__mod_dsb_am_src', 'set_mod_dsb_am_src': '__qcodes_param_set__mod_dsb_am_src', 'get_mod_dsb_am_shape': '__qcodes_param_get__mod_dsb_am_shape', 'set_mod_dsb_am_shape': '__qcodes_param_set__mod_dsb_am_shape', 'get_mod_dsb_am_frequency': '__qcodes_param_get__mod_dsb_am_frequency', 'set_mod_dsb_am_frequency': '__qcodes_param_set__mod_dsb_am_frequency', 'get_mod_fm_src': '__qcodes_param_get__mod_fm_src', 'set_mod_fm_src': '__qcodes_param_set__mod_fm_src', 'get_mod_fm_shape': '__qcodes_param_get__mod_fm_shape', 'set_mod_fm_shape': '__qcodes_param_set__mod_fm_shape', 'get_mod_fm_frequency': '__qcodes_param_get__mod_fm_frequency', 'set_mod_fm_frequency': '__qcodes_param_set__mod_fm_frequency', 'get_mod_fm_deviation': '__qcodes_param_get__mod_fm_deviation', 'set_mod_fm_deviation': '__qcodes_param_set__mod_fm_deviation', 'get_mod_pm_src': '__qcodes_param_get__mod_pm_src', 'set_mod_pm_src': '__qcodes_param_set__mod_pm_src', 'get_mod_pm_shape': '__qcodes_param_get__mod_pm_shape', 'set_mod_pm_shape': '__qcodes_param_set__mod_pm_shape', 'get_mod_pm_frequency': '__qcodes_param_get__mod_pm_frequency', 'set_mod_pm_frequency': '__qcodes_param_set__mod_pm_frequency', 'get_mod_pm_deviation': '__qcodes_param_get__mod_pm_deviation', 'set_mod_pm_deviation': '__qcodes_param_set__mod_pm_deviation', 'get_mod_pwm_src': '__qcodes_param_get__mod_pwm_src', 'set_mod_pwm_src': '__qcodes_param_set__mod_pwm_src', 'get_mod_pwm_frequency': '__qcodes_param_get__mod_pwm_frequency', 'set_mod_pwm_frequency': '__qcodes_param_set__mod_pwm_frequency', 'get_mod_pwm_width_deviation': '__qcodes_param_get__mod_pwm_width_deviation', 'set_mod_pwm_width_deviation': '__qcodes_param_set__mod_pwm_width_deviation', 'get_mod_pwm_duty_cycle_deviation': '__qcodes_param_get__mod_pwm_duty_cycle_deviation', 'set_mod_pwm_duty_cycle_deviation': '__qcodes_param_set__mod_pwm_duty_cycle_deviation', 'get_mod_pwm_shape': '__qcodes_param_get__mod_pwm_shape', 'set_mod_pwm_shape': '__qcodes_param_set__mod_pwm_shape', 'get_mod_ask_src': '__qcodes_param_get__mod_ask_src', 'set_mod_ask_src': '__qcodes_param_set__mod_ask_src', 'get_mod_ask_key_frequency': '__qcodes_param_get__mod_ask_key_frequency', 'set_mod_ask_key_frequency': '__qcodes_param_set__mod_ask_key_frequency', 'get_mod_fsk_src': '__qcodes_param_get__mod_fsk_src', 'set_mod_fsk_src': '__qcodes_param_set__mod_fsk_src', 'get_mod_fsk_key_frequency': '__qcodes_param_get__mod_fsk_key_frequency', 'set_mod_fsk_key_frequency': '__qcodes_param_set__mod_fsk_key_frequency', 'get_mod_fsk_hop_frequency': '__qcodes_param_get__mod_fsk_hop_frequency', 'set_mod_fsk_hop_frequency': '__qcodes_param_set__mod_fsk_hop_frequency', 'get_mod_psk_src': '__qcodes_param_get__mod_psk_src', 'set_mod_psk_src': '__qcodes_param_set__mod_psk_src', 'get_mod_psk_key_frequency': '__qcodes_param_get__mod_psk_key_frequency', 'set_mod_psk_key_frequency': '__qcodes_param_set__mod_psk_key_frequency', 'get_mod_carrier_wave_type': '__qcodes_param_get__mod_carrier_wave_type', 'set_mod_carrier_wave_type': '__qcodes_param_set__mod_carrier_wave_type', 'get_mod_carrier_frequency': '__qcodes_param_get__mod_carrier_frequency', 'set_mod_carrier_frequency': '__qcodes_param_set__mod_carrier_frequency', 'get_mod_carrier_phase': '__qcodes_param_get__mod_carrier_phase', 'set_mod_carrier_phase': '__qcodes_param_set__mod_carrier_phase', 'get_mod_carrier_amplitude': '__qcodes_param_get__mod_carrier_amplitude', 'set_mod_carrier_amplitude': '__qcodes_param_set__mod_carrier_amplitude', 'get_mod_carrier_amplitude_rms': '__qcodes_param_get__mod_carrier_amplitude_rms', 'set_mod_carrier_amplitude_rms': '__qcodes_param_set__mod_carrier_amplitude_rms', 'get_mod_carrier_offset': '__qcodes_param_get__mod_carrier_offset', 'set_mod_carrier_offset': '__qcodes_param_set__mod_carrier_offset', 'get_mod_carrier_ramp_symmetry': '__qcodes_param_get__mod_carrier_ramp_symmetry', 'set_mod_carrier_ramp_symmetry': '__qcodes_param_set__mod_carrier_ramp_symmetry', 'get_mod_carrier_duty_cycle': '__qcodes_param_get__mod_carrier_duty_cycle', 'set_mod_carrier_duty_cycle': '__qcodes_param_set__mod_carrier_duty_cycle', 'get_raw_sweep_wave': '__qcodes_param_get__raw_sweep_wave', 'set_raw_sweep_wave': '__qcodes_param_set__raw_sweep_wave', 'get_sweep_wave': '__qcodes_param_get__sweep_wave', 'set_sweep_wave': '__qcodes_param_set__sweep_wave', 'get_sweep_time': '__qcodes_param_get__sweep_time', 'set_sweep_time': '__qcodes_param_set__sweep_time', 'get_sweep_start_frequency': '__qcodes_param_get__sweep_start_frequency', 'set_sweep_start_frequency': '__qcodes_param_set__sweep_start_frequency', 'get_sweep_stop_frequency': '__qcodes_param_get__sweep_stop_frequency', 'set_sweep_stop_frequency': '__qcodes_param_set__sweep_stop_frequency', 'get_sweep_mode': '__qcodes_param_get__sweep_mode', 'set_sweep_mode': '__qcodes_param_set__sweep_mode', 'get_sweep_direction': '__qcodes_param_get__sweep_direction', 'set_sweep_direction': '__qcodes_param_set__sweep_direction', 'get_sweep_symmetry': '__qcodes_param_get__sweep_symmetry', 'set_sweep_symmetry': '__qcodes_param_set__sweep_symmetry', 'get_sweep_trigger_source': '__qcodes_param_get__sweep_trigger_source', 'set_sweep_trigger_source': '__qcodes_param_set__sweep_trigger_source', 'get_sweep_carrier_wave_type': '__qcodes_param_get__sweep_carrier_wave_type', 'set_sweep_carrier_wave_type': '__qcodes_param_set__sweep_carrier_wave_type', 'get_sweep_carrier_frequency': '__qcodes_param_get__sweep_carrier_frequency', 'set_sweep_carrier_frequency': '__qcodes_param_set__sweep_carrier_frequency', 'get_sweep_carrier_phase': '__qcodes_param_get__sweep_carrier_phase', 'set_sweep_carrier_phase': '__qcodes_param_set__sweep_carrier_phase', 'get_sweep_carrier_amplitude': '__qcodes_param_get__sweep_carrier_amplitude', 'set_sweep_carrier_amplitude': '__qcodes_param_set__sweep_carrier_amplitude', 'get_sweep_carrier_amplitude_rms': '__qcodes_param_get__sweep_carrier_amplitude_rms', 'set_sweep_carrier_amplitude_rms': '__qcodes_param_set__sweep_carrier_amplitude_rms', 'get_sweep_carrier_offset': '__qcodes_param_get__sweep_carrier_offset', 'set_sweep_carrier_offset': '__qcodes_param_set__sweep_carrier_offset', 'get_sweep_carrier_ramp_symmetry': '__qcodes_param_get__sweep_carrier_ramp_symmetry', 'set_sweep_carrier_ramp_symmetry': '__qcodes_param_set__sweep_carrier_ramp_symmetry', 'get_sweep_carrier_duty_cycle': '__qcodes_param_get__sweep_carrier_duty_cycle', 'set_sweep_carrier_duty_cycle': '__qcodes_param_set__sweep_carrier_duty_cycle', 'get_sweep_mark': '__qcodes_param_get__sweep_mark', 'set_sweep_mark': '__qcodes_param_set__sweep_mark', 'get_sweep_mark_frequency': '__qcodes_param_get__sweep_mark_frequency', 'set_sweep_mark_frequency': '__qcodes_param_set__sweep_mark_frequency', 'get_raw_burst_wave': '__qcodes_param_get__raw_burst_wave', 'set_raw_burst_wave': '__qcodes_param_set__raw_burst_wave', 'get_burst_wave': '__qcodes_param_get__burst_wave', 'set_burst_wave': '__qcodes_param_set__burst_wave', 'get_burst_period': '__qcodes_param_get__burst_period', 'set_burst_period': '__qcodes_param_set__burst_period', 'get_burst_start_phase': '__qcodes_param_get__burst_start_phase', 'set_burst_start_phase': '__qcodes_param_set__burst_start_phase', 'get_burst_mode': '__qcodes_param_get__burst_mode', 'set_burst_mode': '__qcodes_param_set__burst_mode', 'get_burst_trigger_source': '__qcodes_param_get__burst_trigger_source', 'set_burst_trigger_source': '__qcodes_param_set__burst_trigger_source', 'get_burst_trigger_delay': '__qcodes_param_get__burst_trigger_delay', 'set_burst_trigger_delay': '__qcodes_param_set__burst_trigger_delay', 'get_burst_gate_polarity': '__qcodes_param_get__burst_gate_polarity', 'set_burst_gate_polarity': '__qcodes_param_set__burst_gate_polarity', 'get_burst_ncycles': '__qcodes_param_get__burst_ncycles', 'set_burst_ncycles': '__qcodes_param_set__burst_ncycles', 'get_burst_carrier_wave_type': '__qcodes_param_get__burst_carrier_wave_type', 'set_burst_carrier_wave_type': '__qcodes_param_set__burst_carrier_wave_type', 'get_burst_carrier_frequency': '__qcodes_param_get__burst_carrier_frequency', 'set_burst_carrier_frequency': '__qcodes_param_set__burst_carrier_frequency', 'get_burst_carrier_phase': '__qcodes_param_get__burst_carrier_phase', 'set_burst_carrier_phase': '__qcodes_param_set__burst_carrier_phase', 'get_burst_carrier_amplitude': '__qcodes_param_get__burst_carrier_amplitude', 'set_burst_carrier_amplitude': '__qcodes_param_set__burst_carrier_amplitude', 'get_burst_carrier_amplitude_rms': '__qcodes_param_get__burst_carrier_amplitude_rms', 'set_burst_carrier_amplitude_rms': '__qcodes_param_set__burst_carrier_amplitude_rms', 'get_burst_carrier_offset': '__qcodes_param_get__burst_carrier_offset', 'set_burst_carrier_offset': '__qcodes_param_set__burst_carrier_offset', 'get_burst_carrier_ramp_symmetry': '__qcodes_param_get__burst_carrier_ramp_symmetry', 'set_burst_carrier_ramp_symmetry': '__qcodes_param_set__burst_carrier_ramp_symmetry', 'get_burst_carrier_duty_cycle': '__qcodes_param_get__burst_carrier_duty_cycle', 'set_burst_carrier_duty_cycle': '__qcodes_param_set__burst_carrier_duty_cycle', 'get_burst_carrier_noise_std_dev': '__qcodes_param_get__burst_carrier_noise_std_dev', 'set_burst_carrier_noise_std_dev': '__qcodes_param_set__burst_carrier_noise_std_dev', 'get_burst_carrier_noise_mean': '__qcodes_param_get__burst_carrier_noise_mean', 'set_burst_carrier_noise_mean': '__qcodes_param_set__burst_carrier_noise_mean', 'get_raw_arbitrary_wave': '__qcodes_param_get__raw_arbitrary_wave', 'set_raw_arbitrary_wave': '__qcodes_param_set__raw_arbitrary_wave', 'get_arbitrary_wave_index': '__qcodes_param_get__arbitrary_wave_index', 'set_arbitrary_wave_index': '__qcodes_param_set__arbitrary_wave_index', 'get_arbitrary_wave_name': '__qcodes_param_get__arbitrary_wave_name', 'set_arbitrary_wave_name': '__qcodes_param_set__arbitrary_wave_name', 'get_raw_sync': '__qcodes_param_get__raw_sync', 'set_raw_sync': '__qcodes_param_set__raw_sync', 'get_sync_enabled': '__qcodes_param_get__sync_enabled', 'set_sync_enabled': '__qcodes_param_set__sync_enabled', 'get_sync_type': '__qcodes_param_get__sync_type', 'set_sync_type': '__qcodes_param_set__sync_type', 'get_inverted': '__qcodes_param_get__inverted', 'set_inverted': '__qcodes_param_set__inverted', 'get_poweron_state': '__qcodes_param_get__poweron_state', 'set_poweron_state': '__qcodes_param_set__poweron_state', 'get_max_output_amp': '__qcodes_param_get__max_output_amp', 'set_max_output_amp': '__qcodes_param_set__max_output_amp', 'get_mod_dsb_sc_src': '__qcodes_param_get__mod_dsb_sc_src', 'set_mod_dsb_sc_src': '__qcodes_param_set__mod_dsb_sc_src', 'get_mod_dsb_sc_shape': '__qcodes_param_get__mod_dsb_sc_shape', 'set_mod_dsb_sc_shape': '__qcodes_param_set__mod_dsb_sc_shape', 'get_mod_dsb_sc_frequency': '__qcodes_param_get__mod_dsb_sc_frequency', 'set_mod_dsb_sc_frequency': '__qcodes_param_set__mod_dsb_sc_frequency', 'get_mod_carrier_rise_time': '__qcodes_param_get__mod_carrier_rise_time', 'set_mod_carrier_rise_time': '__qcodes_param_set__mod_carrier_rise_time', 'get_mod_carrier_fall_time': '__qcodes_param_get__mod_carrier_fall_time', 'set_mod_carrier_fall_time': '__qcodes_param_set__mod_carrier_fall_time', 'get_mod_carrier_delay': '__qcodes_param_get__mod_carrier_delay', 'set_mod_carrier_delay': '__qcodes_param_set__mod_carrier_delay', 'get_sweep_start_hold_time': '__qcodes_param_get__sweep_start_hold_time', 'set_sweep_start_hold_time': '__qcodes_param_set__sweep_start_hold_time', 'get_sweep_end_hold_time': '__qcodes_param_get__sweep_end_hold_time', 'set_sweep_end_hold_time': '__qcodes_param_set__sweep_end_hold_time', 'get_sweep_back_time': '__qcodes_param_get__sweep_back_time', 'set_sweep_back_time': '__qcodes_param_set__sweep_back_time', 'get_sweep_center_frequency': '__qcodes_param_get__sweep_center_frequency', 'set_sweep_center_frequency': '__qcodes_param_set__sweep_center_frequency', 'get_sweep_frequency_span': '__qcodes_param_get__sweep_frequency_span', 'set_sweep_frequency_span': '__qcodes_param_set__sweep_frequency_span', 'get_sweep_trigger_output': '__qcodes_param_get__sweep_trigger_output', 'set_sweep_trigger_output': '__qcodes_param_set__sweep_trigger_output', 'get_sweep_trigger_edge': '__qcodes_param_get__sweep_trigger_edge', 'set_sweep_trigger_edge': '__qcodes_param_set__sweep_trigger_edge', 'get_burst_trigger_output_mode': '__qcodes_param_get__burst_trigger_output_mode', 'set_burst_trigger_output_mode': '__qcodes_param_set__burst_trigger_output_mode', 'get_burst_trigger_edge': '__qcodes_param_get__burst_trigger_edge', 'set_burst_trigger_edge': '__qcodes_param_set__burst_trigger_edge', 'get_burst_counter': '__qcodes_param_get__burst_counter', 'set_burst_counter': '__qcodes_param_set__burst_counter', 'get_burst_carrier_rise_time': '__qcodes_param_get__burst_carrier_rise_time', 'set_burst_carrier_rise_time': '__qcodes_param_set__burst_carrier_rise_time', 'get_burst_carrier_fall_time': '__qcodes_param_get__burst_carrier_fall_time', 'set_burst_carrier_fall_time': '__qcodes_param_set__burst_carrier_fall_time', 'get_burst_carrier_delay': '__qcodes_param_get__burst_carrier_delay', 'set_burst_carrier_delay': '__qcodes_param_set__burst_carrier_delay'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_raw_outp(self, **kwargs):
        return self.call('get_raw_outp', kwargs=kwargs)

    def set_raw_outp(self, **kwargs):
        return self.call('set_raw_outp', kwargs=kwargs)

    def get_enabled(self, **kwargs):
        return self.call('get_enabled', kwargs=kwargs)

    def set_enabled(self, **kwargs):
        return self.call('set_enabled', kwargs=kwargs)

    def get_load(self, **kwargs):
        return self.call('get_load', kwargs=kwargs)

    def set_load(self, **kwargs):
        return self.call('set_load', kwargs=kwargs)

    def get_polarity(self, **kwargs):
        return self.call('get_polarity', kwargs=kwargs)

    def set_polarity(self, **kwargs):
        return self.call('set_polarity', kwargs=kwargs)

    def get_raw_basic_wave(self, **kwargs):
        return self.call('get_raw_basic_wave', kwargs=kwargs)

    def set_raw_basic_wave(self, **kwargs):
        return self.call('set_raw_basic_wave', kwargs=kwargs)

    def get_wave_type(self, **kwargs):
        return self.call('get_wave_type', kwargs=kwargs)

    def set_wave_type(self, **kwargs):
        return self.call('set_wave_type', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def get_period(self, **kwargs):
        return self.call('get_period', kwargs=kwargs)

    def set_period(self, **kwargs):
        return self.call('set_period', kwargs=kwargs)

    def get_amplitude(self, **kwargs):
        return self.call('get_amplitude', kwargs=kwargs)

    def set_amplitude(self, **kwargs):
        return self.call('set_amplitude', kwargs=kwargs)

    def get_amplitude_rms(self, **kwargs):
        return self.call('get_amplitude_rms', kwargs=kwargs)

    def set_amplitude_rms(self, **kwargs):
        return self.call('set_amplitude_rms', kwargs=kwargs)

    def get_amplitude_dbm(self, **kwargs):
        return self.call('get_amplitude_dbm', kwargs=kwargs)

    def set_amplitude_dbm(self, **kwargs):
        return self.call('set_amplitude_dbm', kwargs=kwargs)

    def get_offset(self, **kwargs):
        return self.call('get_offset', kwargs=kwargs)

    def set_offset(self, **kwargs):
        return self.call('set_offset', kwargs=kwargs)

    def get_common_offset(self, **kwargs):
        return self.call('get_common_offset', kwargs=kwargs)

    def set_common_offset(self, **kwargs):
        return self.call('set_common_offset', kwargs=kwargs)

    def get_ramp_symmetry(self, **kwargs):
        return self.call('get_ramp_symmetry', kwargs=kwargs)

    def set_ramp_symmetry(self, **kwargs):
        return self.call('set_ramp_symmetry', kwargs=kwargs)

    def get_duty_cycle(self, **kwargs):
        return self.call('get_duty_cycle', kwargs=kwargs)

    def set_duty_cycle(self, **kwargs):
        return self.call('set_duty_cycle', kwargs=kwargs)

    def get_phase(self, **kwargs):
        return self.call('get_phase', kwargs=kwargs)

    def set_phase(self, **kwargs):
        return self.call('set_phase', kwargs=kwargs)

    def get_noise_std_dev(self, **kwargs):
        return self.call('get_noise_std_dev', kwargs=kwargs)

    def set_noise_std_dev(self, **kwargs):
        return self.call('set_noise_std_dev', kwargs=kwargs)

    def get_noise_mean(self, **kwargs):
        return self.call('get_noise_mean', kwargs=kwargs)

    def set_noise_mean(self, **kwargs):
        return self.call('set_noise_mean', kwargs=kwargs)

    def get_pulse_width(self, **kwargs):
        return self.call('get_pulse_width', kwargs=kwargs)

    def set_pulse_width(self, **kwargs):
        return self.call('set_pulse_width', kwargs=kwargs)

    def get_rise_time(self, **kwargs):
        return self.call('get_rise_time', kwargs=kwargs)

    def set_rise_time(self, **kwargs):
        return self.call('set_rise_time', kwargs=kwargs)

    def get_fall_time(self, **kwargs):
        return self.call('get_fall_time', kwargs=kwargs)

    def set_fall_time(self, **kwargs):
        return self.call('set_fall_time', kwargs=kwargs)

    def get_delay(self, **kwargs):
        return self.call('get_delay', kwargs=kwargs)

    def set_delay(self, **kwargs):
        return self.call('set_delay', kwargs=kwargs)

    def get_high_level(self, **kwargs):
        return self.call('get_high_level', kwargs=kwargs)

    def set_high_level(self, **kwargs):
        return self.call('set_high_level', kwargs=kwargs)

    def get_low_level(self, **kwargs):
        return self.call('get_low_level', kwargs=kwargs)

    def set_low_level(self, **kwargs):
        return self.call('set_low_level', kwargs=kwargs)

    def get_noise_bandwidth_enabled(self, **kwargs):
        return self.call('get_noise_bandwidth_enabled', kwargs=kwargs)

    def set_noise_bandwidth_enabled(self, **kwargs):
        return self.call('set_noise_bandwidth_enabled', kwargs=kwargs)

    def get_noise_bandwidth(self, **kwargs):
        return self.call('get_noise_bandwidth', kwargs=kwargs)

    def set_noise_bandwidth(self, **kwargs):
        return self.call('set_noise_bandwidth', kwargs=kwargs)

    def get_prbs_length(self, **kwargs):
        return self.call('get_prbs_length', kwargs=kwargs)

    def set_prbs_length(self, **kwargs):
        return self.call('set_prbs_length', kwargs=kwargs)

    def get_prbs_edge_time(self, **kwargs):
        return self.call('get_prbs_edge_time', kwargs=kwargs)

    def set_prbs_edge_time(self, **kwargs):
        return self.call('set_prbs_edge_time', kwargs=kwargs)

    def get_differential_mode(self, **kwargs):
        return self.call('get_differential_mode', kwargs=kwargs)

    def set_differential_mode(self, **kwargs):
        return self.call('set_differential_mode', kwargs=kwargs)

    def get_prbs_differential_mode(self, **kwargs):
        return self.call('get_prbs_differential_mode', kwargs=kwargs)

    def set_prbs_differential_mode(self, **kwargs):
        return self.call('set_prbs_differential_mode', kwargs=kwargs)

    def get_prbs_bit_rate(self, **kwargs):
        return self.call('get_prbs_bit_rate', kwargs=kwargs)

    def set_prbs_bit_rate(self, **kwargs):
        return self.call('set_prbs_bit_rate', kwargs=kwargs)

    def get_prbs_logic_level(self, **kwargs):
        return self.call('get_prbs_logic_level', kwargs=kwargs)

    def set_prbs_logic_level(self, **kwargs):
        return self.call('set_prbs_logic_level', kwargs=kwargs)

    def get_raw_modulate_wave(self, **kwargs):
        return self.call('get_raw_modulate_wave', kwargs=kwargs)

    def set_raw_modulate_wave(self, **kwargs):
        return self.call('set_raw_modulate_wave', kwargs=kwargs)

    def get_modulate_wave(self, **kwargs):
        return self.call('get_modulate_wave', kwargs=kwargs)

    def set_modulate_wave(self, **kwargs):
        return self.call('set_modulate_wave', kwargs=kwargs)

    def get_mod_am_src(self, **kwargs):
        return self.call('get_mod_am_src', kwargs=kwargs)

    def set_mod_am_src(self, **kwargs):
        return self.call('set_mod_am_src', kwargs=kwargs)

    def get_mod_am_shape(self, **kwargs):
        return self.call('get_mod_am_shape', kwargs=kwargs)

    def set_mod_am_shape(self, **kwargs):
        return self.call('set_mod_am_shape', kwargs=kwargs)

    def get_mod_am_frequency(self, **kwargs):
        return self.call('get_mod_am_frequency', kwargs=kwargs)

    def set_mod_am_frequency(self, **kwargs):
        return self.call('set_mod_am_frequency', kwargs=kwargs)

    def get_mod_am_depth(self, **kwargs):
        return self.call('get_mod_am_depth', kwargs=kwargs)

    def set_mod_am_depth(self, **kwargs):
        return self.call('set_mod_am_depth', kwargs=kwargs)

    def get_mod_dsb_am_src(self, **kwargs):
        return self.call('get_mod_dsb_am_src', kwargs=kwargs)

    def set_mod_dsb_am_src(self, **kwargs):
        return self.call('set_mod_dsb_am_src', kwargs=kwargs)

    def get_mod_dsb_am_shape(self, **kwargs):
        return self.call('get_mod_dsb_am_shape', kwargs=kwargs)

    def set_mod_dsb_am_shape(self, **kwargs):
        return self.call('set_mod_dsb_am_shape', kwargs=kwargs)

    def get_mod_dsb_am_frequency(self, **kwargs):
        return self.call('get_mod_dsb_am_frequency', kwargs=kwargs)

    def set_mod_dsb_am_frequency(self, **kwargs):
        return self.call('set_mod_dsb_am_frequency', kwargs=kwargs)

    def get_mod_fm_src(self, **kwargs):
        return self.call('get_mod_fm_src', kwargs=kwargs)

    def set_mod_fm_src(self, **kwargs):
        return self.call('set_mod_fm_src', kwargs=kwargs)

    def get_mod_fm_shape(self, **kwargs):
        return self.call('get_mod_fm_shape', kwargs=kwargs)

    def set_mod_fm_shape(self, **kwargs):
        return self.call('set_mod_fm_shape', kwargs=kwargs)

    def get_mod_fm_frequency(self, **kwargs):
        return self.call('get_mod_fm_frequency', kwargs=kwargs)

    def set_mod_fm_frequency(self, **kwargs):
        return self.call('set_mod_fm_frequency', kwargs=kwargs)

    def get_mod_fm_deviation(self, **kwargs):
        return self.call('get_mod_fm_deviation', kwargs=kwargs)

    def set_mod_fm_deviation(self, **kwargs):
        return self.call('set_mod_fm_deviation', kwargs=kwargs)

    def get_mod_pm_src(self, **kwargs):
        return self.call('get_mod_pm_src', kwargs=kwargs)

    def set_mod_pm_src(self, **kwargs):
        return self.call('set_mod_pm_src', kwargs=kwargs)

    def get_mod_pm_shape(self, **kwargs):
        return self.call('get_mod_pm_shape', kwargs=kwargs)

    def set_mod_pm_shape(self, **kwargs):
        return self.call('set_mod_pm_shape', kwargs=kwargs)

    def get_mod_pm_frequency(self, **kwargs):
        return self.call('get_mod_pm_frequency', kwargs=kwargs)

    def set_mod_pm_frequency(self, **kwargs):
        return self.call('set_mod_pm_frequency', kwargs=kwargs)

    def get_mod_pm_deviation(self, **kwargs):
        return self.call('get_mod_pm_deviation', kwargs=kwargs)

    def set_mod_pm_deviation(self, **kwargs):
        return self.call('set_mod_pm_deviation', kwargs=kwargs)

    def get_mod_pwm_src(self, **kwargs):
        return self.call('get_mod_pwm_src', kwargs=kwargs)

    def set_mod_pwm_src(self, **kwargs):
        return self.call('set_mod_pwm_src', kwargs=kwargs)

    def get_mod_pwm_frequency(self, **kwargs):
        return self.call('get_mod_pwm_frequency', kwargs=kwargs)

    def set_mod_pwm_frequency(self, **kwargs):
        return self.call('set_mod_pwm_frequency', kwargs=kwargs)

    def get_mod_pwm_width_deviation(self, **kwargs):
        return self.call('get_mod_pwm_width_deviation', kwargs=kwargs)

    def set_mod_pwm_width_deviation(self, **kwargs):
        return self.call('set_mod_pwm_width_deviation', kwargs=kwargs)

    def get_mod_pwm_duty_cycle_deviation(self, **kwargs):
        return self.call('get_mod_pwm_duty_cycle_deviation', kwargs=kwargs)

    def set_mod_pwm_duty_cycle_deviation(self, **kwargs):
        return self.call('set_mod_pwm_duty_cycle_deviation', kwargs=kwargs)

    def get_mod_pwm_shape(self, **kwargs):
        return self.call('get_mod_pwm_shape', kwargs=kwargs)

    def set_mod_pwm_shape(self, **kwargs):
        return self.call('set_mod_pwm_shape', kwargs=kwargs)

    def get_mod_ask_src(self, **kwargs):
        return self.call('get_mod_ask_src', kwargs=kwargs)

    def set_mod_ask_src(self, **kwargs):
        return self.call('set_mod_ask_src', kwargs=kwargs)

    def get_mod_ask_key_frequency(self, **kwargs):
        return self.call('get_mod_ask_key_frequency', kwargs=kwargs)

    def set_mod_ask_key_frequency(self, **kwargs):
        return self.call('set_mod_ask_key_frequency', kwargs=kwargs)

    def get_mod_fsk_src(self, **kwargs):
        return self.call('get_mod_fsk_src', kwargs=kwargs)

    def set_mod_fsk_src(self, **kwargs):
        return self.call('set_mod_fsk_src', kwargs=kwargs)

    def get_mod_fsk_key_frequency(self, **kwargs):
        return self.call('get_mod_fsk_key_frequency', kwargs=kwargs)

    def set_mod_fsk_key_frequency(self, **kwargs):
        return self.call('set_mod_fsk_key_frequency', kwargs=kwargs)

    def get_mod_fsk_hop_frequency(self, **kwargs):
        return self.call('get_mod_fsk_hop_frequency', kwargs=kwargs)

    def set_mod_fsk_hop_frequency(self, **kwargs):
        return self.call('set_mod_fsk_hop_frequency', kwargs=kwargs)

    def get_mod_psk_src(self, **kwargs):
        return self.call('get_mod_psk_src', kwargs=kwargs)

    def set_mod_psk_src(self, **kwargs):
        return self.call('set_mod_psk_src', kwargs=kwargs)

    def get_mod_psk_key_frequency(self, **kwargs):
        return self.call('get_mod_psk_key_frequency', kwargs=kwargs)

    def set_mod_psk_key_frequency(self, **kwargs):
        return self.call('set_mod_psk_key_frequency', kwargs=kwargs)

    def get_mod_carrier_wave_type(self, **kwargs):
        return self.call('get_mod_carrier_wave_type', kwargs=kwargs)

    def set_mod_carrier_wave_type(self, **kwargs):
        return self.call('set_mod_carrier_wave_type', kwargs=kwargs)

    def get_mod_carrier_frequency(self, **kwargs):
        return self.call('get_mod_carrier_frequency', kwargs=kwargs)

    def set_mod_carrier_frequency(self, **kwargs):
        return self.call('set_mod_carrier_frequency', kwargs=kwargs)

    def get_mod_carrier_phase(self, **kwargs):
        return self.call('get_mod_carrier_phase', kwargs=kwargs)

    def set_mod_carrier_phase(self, **kwargs):
        return self.call('set_mod_carrier_phase', kwargs=kwargs)

    def get_mod_carrier_amplitude(self, **kwargs):
        return self.call('get_mod_carrier_amplitude', kwargs=kwargs)

    def set_mod_carrier_amplitude(self, **kwargs):
        return self.call('set_mod_carrier_amplitude', kwargs=kwargs)

    def get_mod_carrier_amplitude_rms(self, **kwargs):
        return self.call('get_mod_carrier_amplitude_rms', kwargs=kwargs)

    def set_mod_carrier_amplitude_rms(self, **kwargs):
        return self.call('set_mod_carrier_amplitude_rms', kwargs=kwargs)

    def get_mod_carrier_offset(self, **kwargs):
        return self.call('get_mod_carrier_offset', kwargs=kwargs)

    def set_mod_carrier_offset(self, **kwargs):
        return self.call('set_mod_carrier_offset', kwargs=kwargs)

    def get_mod_carrier_ramp_symmetry(self, **kwargs):
        return self.call('get_mod_carrier_ramp_symmetry', kwargs=kwargs)

    def set_mod_carrier_ramp_symmetry(self, **kwargs):
        return self.call('set_mod_carrier_ramp_symmetry', kwargs=kwargs)

    def get_mod_carrier_duty_cycle(self, **kwargs):
        return self.call('get_mod_carrier_duty_cycle', kwargs=kwargs)

    def set_mod_carrier_duty_cycle(self, **kwargs):
        return self.call('set_mod_carrier_duty_cycle', kwargs=kwargs)

    def get_raw_sweep_wave(self, **kwargs):
        return self.call('get_raw_sweep_wave', kwargs=kwargs)

    def set_raw_sweep_wave(self, **kwargs):
        return self.call('set_raw_sweep_wave', kwargs=kwargs)

    def get_sweep_wave(self, **kwargs):
        return self.call('get_sweep_wave', kwargs=kwargs)

    def set_sweep_wave(self, **kwargs):
        return self.call('set_sweep_wave', kwargs=kwargs)

    def get_sweep_time(self, **kwargs):
        return self.call('get_sweep_time', kwargs=kwargs)

    def set_sweep_time(self, **kwargs):
        return self.call('set_sweep_time', kwargs=kwargs)

    def get_sweep_start_frequency(self, **kwargs):
        return self.call('get_sweep_start_frequency', kwargs=kwargs)

    def set_sweep_start_frequency(self, **kwargs):
        return self.call('set_sweep_start_frequency', kwargs=kwargs)

    def get_sweep_stop_frequency(self, **kwargs):
        return self.call('get_sweep_stop_frequency', kwargs=kwargs)

    def set_sweep_stop_frequency(self, **kwargs):
        return self.call('set_sweep_stop_frequency', kwargs=kwargs)

    def get_sweep_mode(self, **kwargs):
        return self.call('get_sweep_mode', kwargs=kwargs)

    def set_sweep_mode(self, **kwargs):
        return self.call('set_sweep_mode', kwargs=kwargs)

    def get_sweep_direction(self, **kwargs):
        return self.call('get_sweep_direction', kwargs=kwargs)

    def set_sweep_direction(self, **kwargs):
        return self.call('set_sweep_direction', kwargs=kwargs)

    def get_sweep_symmetry(self, **kwargs):
        return self.call('get_sweep_symmetry', kwargs=kwargs)

    def set_sweep_symmetry(self, **kwargs):
        return self.call('set_sweep_symmetry', kwargs=kwargs)

    def get_sweep_trigger_source(self, **kwargs):
        return self.call('get_sweep_trigger_source', kwargs=kwargs)

    def set_sweep_trigger_source(self, **kwargs):
        return self.call('set_sweep_trigger_source', kwargs=kwargs)

    def get_sweep_carrier_wave_type(self, **kwargs):
        return self.call('get_sweep_carrier_wave_type', kwargs=kwargs)

    def set_sweep_carrier_wave_type(self, **kwargs):
        return self.call('set_sweep_carrier_wave_type', kwargs=kwargs)

    def get_sweep_carrier_frequency(self, **kwargs):
        return self.call('get_sweep_carrier_frequency', kwargs=kwargs)

    def set_sweep_carrier_frequency(self, **kwargs):
        return self.call('set_sweep_carrier_frequency', kwargs=kwargs)

    def get_sweep_carrier_phase(self, **kwargs):
        return self.call('get_sweep_carrier_phase', kwargs=kwargs)

    def set_sweep_carrier_phase(self, **kwargs):
        return self.call('set_sweep_carrier_phase', kwargs=kwargs)

    def get_sweep_carrier_amplitude(self, **kwargs):
        return self.call('get_sweep_carrier_amplitude', kwargs=kwargs)

    def set_sweep_carrier_amplitude(self, **kwargs):
        return self.call('set_sweep_carrier_amplitude', kwargs=kwargs)

    def get_sweep_carrier_amplitude_rms(self, **kwargs):
        return self.call('get_sweep_carrier_amplitude_rms', kwargs=kwargs)

    def set_sweep_carrier_amplitude_rms(self, **kwargs):
        return self.call('set_sweep_carrier_amplitude_rms', kwargs=kwargs)

    def get_sweep_carrier_offset(self, **kwargs):
        return self.call('get_sweep_carrier_offset', kwargs=kwargs)

    def set_sweep_carrier_offset(self, **kwargs):
        return self.call('set_sweep_carrier_offset', kwargs=kwargs)

    def get_sweep_carrier_ramp_symmetry(self, **kwargs):
        return self.call('get_sweep_carrier_ramp_symmetry', kwargs=kwargs)

    def set_sweep_carrier_ramp_symmetry(self, **kwargs):
        return self.call('set_sweep_carrier_ramp_symmetry', kwargs=kwargs)

    def get_sweep_carrier_duty_cycle(self, **kwargs):
        return self.call('get_sweep_carrier_duty_cycle', kwargs=kwargs)

    def set_sweep_carrier_duty_cycle(self, **kwargs):
        return self.call('set_sweep_carrier_duty_cycle', kwargs=kwargs)

    def get_sweep_mark(self, **kwargs):
        return self.call('get_sweep_mark', kwargs=kwargs)

    def set_sweep_mark(self, **kwargs):
        return self.call('set_sweep_mark', kwargs=kwargs)

    def get_sweep_mark_frequency(self, **kwargs):
        return self.call('get_sweep_mark_frequency', kwargs=kwargs)

    def set_sweep_mark_frequency(self, **kwargs):
        return self.call('set_sweep_mark_frequency', kwargs=kwargs)

    def get_raw_burst_wave(self, **kwargs):
        return self.call('get_raw_burst_wave', kwargs=kwargs)

    def set_raw_burst_wave(self, **kwargs):
        return self.call('set_raw_burst_wave', kwargs=kwargs)

    def get_burst_wave(self, **kwargs):
        return self.call('get_burst_wave', kwargs=kwargs)

    def set_burst_wave(self, **kwargs):
        return self.call('set_burst_wave', kwargs=kwargs)

    def get_burst_period(self, **kwargs):
        return self.call('get_burst_period', kwargs=kwargs)

    def set_burst_period(self, **kwargs):
        return self.call('set_burst_period', kwargs=kwargs)

    def get_burst_start_phase(self, **kwargs):
        return self.call('get_burst_start_phase', kwargs=kwargs)

    def set_burst_start_phase(self, **kwargs):
        return self.call('set_burst_start_phase', kwargs=kwargs)

    def get_burst_mode(self, **kwargs):
        return self.call('get_burst_mode', kwargs=kwargs)

    def set_burst_mode(self, **kwargs):
        return self.call('set_burst_mode', kwargs=kwargs)

    def get_burst_trigger_source(self, **kwargs):
        return self.call('get_burst_trigger_source', kwargs=kwargs)

    def set_burst_trigger_source(self, **kwargs):
        return self.call('set_burst_trigger_source', kwargs=kwargs)

    def get_burst_trigger_delay(self, **kwargs):
        return self.call('get_burst_trigger_delay', kwargs=kwargs)

    def set_burst_trigger_delay(self, **kwargs):
        return self.call('set_burst_trigger_delay', kwargs=kwargs)

    def get_burst_gate_polarity(self, **kwargs):
        return self.call('get_burst_gate_polarity', kwargs=kwargs)

    def set_burst_gate_polarity(self, **kwargs):
        return self.call('set_burst_gate_polarity', kwargs=kwargs)

    def get_burst_ncycles(self, **kwargs):
        return self.call('get_burst_ncycles', kwargs=kwargs)

    def set_burst_ncycles(self, **kwargs):
        return self.call('set_burst_ncycles', kwargs=kwargs)

    def get_burst_carrier_wave_type(self, **kwargs):
        return self.call('get_burst_carrier_wave_type', kwargs=kwargs)

    def set_burst_carrier_wave_type(self, **kwargs):
        return self.call('set_burst_carrier_wave_type', kwargs=kwargs)

    def get_burst_carrier_frequency(self, **kwargs):
        return self.call('get_burst_carrier_frequency', kwargs=kwargs)

    def set_burst_carrier_frequency(self, **kwargs):
        return self.call('set_burst_carrier_frequency', kwargs=kwargs)

    def get_burst_carrier_phase(self, **kwargs):
        return self.call('get_burst_carrier_phase', kwargs=kwargs)

    def set_burst_carrier_phase(self, **kwargs):
        return self.call('set_burst_carrier_phase', kwargs=kwargs)

    def get_burst_carrier_amplitude(self, **kwargs):
        return self.call('get_burst_carrier_amplitude', kwargs=kwargs)

    def set_burst_carrier_amplitude(self, **kwargs):
        return self.call('set_burst_carrier_amplitude', kwargs=kwargs)

    def get_burst_carrier_amplitude_rms(self, **kwargs):
        return self.call('get_burst_carrier_amplitude_rms', kwargs=kwargs)

    def set_burst_carrier_amplitude_rms(self, **kwargs):
        return self.call('set_burst_carrier_amplitude_rms', kwargs=kwargs)

    def get_burst_carrier_offset(self, **kwargs):
        return self.call('get_burst_carrier_offset', kwargs=kwargs)

    def set_burst_carrier_offset(self, **kwargs):
        return self.call('set_burst_carrier_offset', kwargs=kwargs)

    def get_burst_carrier_ramp_symmetry(self, **kwargs):
        return self.call('get_burst_carrier_ramp_symmetry', kwargs=kwargs)

    def set_burst_carrier_ramp_symmetry(self, **kwargs):
        return self.call('set_burst_carrier_ramp_symmetry', kwargs=kwargs)

    def get_burst_carrier_duty_cycle(self, **kwargs):
        return self.call('get_burst_carrier_duty_cycle', kwargs=kwargs)

    def set_burst_carrier_duty_cycle(self, **kwargs):
        return self.call('set_burst_carrier_duty_cycle', kwargs=kwargs)

    def get_burst_carrier_noise_std_dev(self, **kwargs):
        return self.call('get_burst_carrier_noise_std_dev', kwargs=kwargs)

    def set_burst_carrier_noise_std_dev(self, **kwargs):
        return self.call('set_burst_carrier_noise_std_dev', kwargs=kwargs)

    def get_burst_carrier_noise_mean(self, **kwargs):
        return self.call('get_burst_carrier_noise_mean', kwargs=kwargs)

    def set_burst_carrier_noise_mean(self, **kwargs):
        return self.call('set_burst_carrier_noise_mean', kwargs=kwargs)

    def get_raw_arbitrary_wave(self, **kwargs):
        return self.call('get_raw_arbitrary_wave', kwargs=kwargs)

    def set_raw_arbitrary_wave(self, **kwargs):
        return self.call('set_raw_arbitrary_wave', kwargs=kwargs)

    def get_arbitrary_wave_index(self, **kwargs):
        return self.call('get_arbitrary_wave_index', kwargs=kwargs)

    def set_arbitrary_wave_index(self, **kwargs):
        return self.call('set_arbitrary_wave_index', kwargs=kwargs)

    def get_arbitrary_wave_name(self, **kwargs):
        return self.call('get_arbitrary_wave_name', kwargs=kwargs)

    def set_arbitrary_wave_name(self, **kwargs):
        return self.call('set_arbitrary_wave_name', kwargs=kwargs)

    def get_raw_sync(self, **kwargs):
        return self.call('get_raw_sync', kwargs=kwargs)

    def set_raw_sync(self, **kwargs):
        return self.call('set_raw_sync', kwargs=kwargs)

    def get_sync_enabled(self, **kwargs):
        return self.call('get_sync_enabled', kwargs=kwargs)

    def set_sync_enabled(self, **kwargs):
        return self.call('set_sync_enabled', kwargs=kwargs)

    def get_sync_type(self, **kwargs):
        return self.call('get_sync_type', kwargs=kwargs)

    def set_sync_type(self, **kwargs):
        return self.call('set_sync_type', kwargs=kwargs)

    def get_inverted(self, **kwargs):
        return self.call('get_inverted', kwargs=kwargs)

    def set_inverted(self, **kwargs):
        return self.call('set_inverted', kwargs=kwargs)

    def get_poweron_state(self, **kwargs):
        return self.call('get_poweron_state', kwargs=kwargs)

    def set_poweron_state(self, **kwargs):
        return self.call('set_poweron_state', kwargs=kwargs)

    def get_max_output_amp(self, **kwargs):
        return self.call('get_max_output_amp', kwargs=kwargs)

    def set_max_output_amp(self, **kwargs):
        return self.call('set_max_output_amp', kwargs=kwargs)

    def get_mod_dsb_sc_src(self, **kwargs):
        return self.call('get_mod_dsb_sc_src', kwargs=kwargs)

    def set_mod_dsb_sc_src(self, **kwargs):
        return self.call('set_mod_dsb_sc_src', kwargs=kwargs)

    def get_mod_dsb_sc_shape(self, **kwargs):
        return self.call('get_mod_dsb_sc_shape', kwargs=kwargs)

    def set_mod_dsb_sc_shape(self, **kwargs):
        return self.call('set_mod_dsb_sc_shape', kwargs=kwargs)

    def get_mod_dsb_sc_frequency(self, **kwargs):
        return self.call('get_mod_dsb_sc_frequency', kwargs=kwargs)

    def set_mod_dsb_sc_frequency(self, **kwargs):
        return self.call('set_mod_dsb_sc_frequency', kwargs=kwargs)

    def get_mod_carrier_rise_time(self, **kwargs):
        return self.call('get_mod_carrier_rise_time', kwargs=kwargs)

    def set_mod_carrier_rise_time(self, **kwargs):
        return self.call('set_mod_carrier_rise_time', kwargs=kwargs)

    def get_mod_carrier_fall_time(self, **kwargs):
        return self.call('get_mod_carrier_fall_time', kwargs=kwargs)

    def set_mod_carrier_fall_time(self, **kwargs):
        return self.call('set_mod_carrier_fall_time', kwargs=kwargs)

    def get_mod_carrier_delay(self, **kwargs):
        return self.call('get_mod_carrier_delay', kwargs=kwargs)

    def set_mod_carrier_delay(self, **kwargs):
        return self.call('set_mod_carrier_delay', kwargs=kwargs)

    def get_sweep_start_hold_time(self, **kwargs):
        return self.call('get_sweep_start_hold_time', kwargs=kwargs)

    def set_sweep_start_hold_time(self, **kwargs):
        return self.call('set_sweep_start_hold_time', kwargs=kwargs)

    def get_sweep_end_hold_time(self, **kwargs):
        return self.call('get_sweep_end_hold_time', kwargs=kwargs)

    def set_sweep_end_hold_time(self, **kwargs):
        return self.call('set_sweep_end_hold_time', kwargs=kwargs)

    def get_sweep_back_time(self, **kwargs):
        return self.call('get_sweep_back_time', kwargs=kwargs)

    def set_sweep_back_time(self, **kwargs):
        return self.call('set_sweep_back_time', kwargs=kwargs)

    def get_sweep_center_frequency(self, **kwargs):
        return self.call('get_sweep_center_frequency', kwargs=kwargs)

    def set_sweep_center_frequency(self, **kwargs):
        return self.call('set_sweep_center_frequency', kwargs=kwargs)

    def get_sweep_frequency_span(self, **kwargs):
        return self.call('get_sweep_frequency_span', kwargs=kwargs)

    def set_sweep_frequency_span(self, **kwargs):
        return self.call('set_sweep_frequency_span', kwargs=kwargs)

    def get_sweep_trigger_output(self, **kwargs):
        return self.call('get_sweep_trigger_output', kwargs=kwargs)

    def set_sweep_trigger_output(self, **kwargs):
        return self.call('set_sweep_trigger_output', kwargs=kwargs)

    def get_sweep_trigger_edge(self, **kwargs):
        return self.call('get_sweep_trigger_edge', kwargs=kwargs)

    def set_sweep_trigger_edge(self, **kwargs):
        return self.call('set_sweep_trigger_edge', kwargs=kwargs)

    def get_burst_trigger_output_mode(self, **kwargs):
        return self.call('get_burst_trigger_output_mode', kwargs=kwargs)

    def set_burst_trigger_output_mode(self, **kwargs):
        return self.call('set_burst_trigger_output_mode', kwargs=kwargs)

    def get_burst_trigger_edge(self, **kwargs):
        return self.call('get_burst_trigger_edge', kwargs=kwargs)

    def set_burst_trigger_edge(self, **kwargs):
        return self.call('set_burst_trigger_edge', kwargs=kwargs)

    def get_burst_counter(self, **kwargs):
        return self.call('get_burst_counter', kwargs=kwargs)

    def set_burst_counter(self, **kwargs):
        return self.call('set_burst_counter', kwargs=kwargs)

    def get_burst_carrier_rise_time(self, **kwargs):
        return self.call('get_burst_carrier_rise_time', kwargs=kwargs)

    def set_burst_carrier_rise_time(self, **kwargs):
        return self.call('set_burst_carrier_rise_time', kwargs=kwargs)

    def get_burst_carrier_fall_time(self, **kwargs):
        return self.call('get_burst_carrier_fall_time', kwargs=kwargs)

    def set_burst_carrier_fall_time(self, **kwargs):
        return self.call('set_burst_carrier_fall_time', kwargs=kwargs)

    def get_burst_carrier_delay(self, **kwargs):
        return self.call('get_burst_carrier_delay', kwargs=kwargs)

    def set_burst_carrier_delay(self, **kwargs):
        return self.call('set_burst_carrier_delay', kwargs=kwargs)

    def channel_number(self, **kwargs):
        return self.call('channel_number', kwargs=kwargs)

