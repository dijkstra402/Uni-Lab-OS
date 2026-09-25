from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAgilentmsox92504a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/python-ivi__python-ivi', 'source_file': 'ivi/agilent/agilentMSOX92504A.py', 'class_name': 'agilentMSOX92504A', 'import_roots': [], 'candidate_methods': ['get_channels_common_mode', 'set_channels_common_mode', 'get_channels_differential', 'set_channels_differential', 'get_channels_differential_skew', 'set_channels_differential_skew', 'get_channels_display_auto', 'set_channels_display_auto', 'get_channels_display_offset', 'set_channels_display_offset', 'get_channels_display_range', 'set_channels_display_range', 'get_channels_display_scale', 'set_channels_display_scale', 'get_display_color_grade', 'set_display_color_grade', 'display_fetch_color_grade_levels', 'acquisition_segmented_analyze', 'get_acquisition_segmented_count', 'set_acquisition_segmented_count', 'get_acquisition_segmented_index', 'set_acquisition_segmented_index', 'get_acquisition_segmented_acquired_count', 'get_acquisition_segmented_time_tag', 'get_channels_bw_limit', 'set_channels_bw_limit', 'get_channels_invert', 'set_channels_invert', 'get_channels_label', 'set_channels_label', 'get_channels_probe_id', 'get_channels_probe_skew', 'set_channels_probe_skew', 'get_channels_scale', 'set_channels_scale', 'get_channels_trigger_level', 'set_channels_trigger_level', 'get_timebase_mode', 'set_timebase_mode', 'get_timebase_reference', 'set_timebase_reference', 'get_timebase_position', 'set_timebase_position', 'get_timebase_range', 'set_timebase_range', 'get_timebase_scale', 'set_timebase_scale', 'get_timebase_window_position', 'set_timebase_window_position', 'get_timebase_window_range', 'set_timebase_window_range', 'get_timebase_window_scale', 'set_timebase_window_scale', 'get_display_vectors', 'set_display_vectors', 'get_display_labels', 'set_display_labels', 'display_clear', 'system_display_string', 'get_identity_instrument_serial_number', 'memory_save', 'memory_recall', 'get_measurement_function', 'set_measurement_function', 'get_channels_name', 'get_channels_impedance', 'set_channels_impedance', 'get_channels_coupling', 'set_channels_coupling', 'get_channels_attenuation', 'set_channels_attenuation', 'get_channels_level', 'set_channels_level', 'get_channels_hysteresis', 'set_channels_hysteresis', 'get_channels_slope', 'set_channels_slope', 'get_channels_filter_enabled', 'set_channels_filter_enabled', 'get_frequency_channel', 'set_frequency_channel', 'get_frequency_estimate', 'set_frequency_estimate', 'get_frequency_resolution', 'set_frequency_resolution', 'get_frequency_aperture_time', 'set_frequency_aperture_time', 'get_frequency_estimate_auto', 'set_frequency_estimate_auto', 'get_frequency_resolution_auto', 'set_frequency_resolution_auto', 'get_period_channel', 'set_period_channel', 'get_period_estimate', 'set_period_estimate', 'get_period_resolution', 'set_period_resolution', 'get_period_aperture_time', 'set_period_aperture_time', 'get_pulse_width_channel', 'set_pulse_width_channel', 'get_pulse_width_estimate', 'set_pulse_width_estimate', 'get_pulse_width_resolution', 'set_pulse_width_resolution', 'get_duty_cycle_channel', 'set_duty_cycle_channel', 'get_duty_cycle_frequency_estimate', 'set_duty_cycle_frequency_estimate', 'get_duty_cycle_resolution', 'set_duty_cycle_resolution', 'get_edge_time_channel', 'set_edge_time_channel', 'get_edge_time_reference_type', 'set_edge_time_reference_type', 'get_edge_time_estimate', 'set_edge_time_estimate', 'get_edge_time_resolution', 'set_edge_time_resolution', 'get_edge_time_high_reference', 'set_edge_time_high_reference', 'get_edge_time_low_reference', 'set_edge_time_low_reference', 'get_frequency_ratio_numerator_channel', 'set_frequency_ratio_numerator_channel', 'get_frequency_ratio_denominator_channel', 'set_frequency_ratio_denominator_channel', 'get_frequency_ratio_numerator_frequency_estimate', 'set_frequency_ratio_numerator_frequency_estimate', 'get_frequency_ratio_estimate', 'set_frequency_ratio_estimate', 'get_frequency_ratio_resolution', 'set_frequency_ratio_resolution', 'get_time_interval_start_channel', 'set_time_interval_start_channel', 'get_time_interval_stop_channel', 'set_time_interval_stop_channel', 'get_time_interval_estimate', 'set_time_interval_estimate', 'get_time_interval_resolution', 'set_time_interval_resolution', 'get_phase_input_channel', 'set_phase_input_channel', 'get_phase_reference_channel', 'set_phase_reference_channel', 'get_phase_frequency_estimate', 'set_phase_frequency_estimate', 'get_phase_resolution', 'set_phase_resolution', 'get_totalize_continuous_channel', 'set_totalize_continuous_channel', 'get_totalize_gated_channel', 'set_totalize_gated_channel', 'get_totalize_gated_gate_source', 'set_totalize_gated_gate_source', 'get_totalize_gated_gate_slope', 'set_totalize_gated_gate_slope', 'get_totalize_timed_channel', 'set_totalize_timed_channel', 'get_totalize_timed_gate_time', 'set_totalize_timed_gate_time', 'get_arm_start_type', 'set_arm_start_type', 'get_arm_start_external_source', 'set_arm_start_external_source', 'get_arm_start_external_level', 'set_arm_start_external_level', 'get_arm_start_external_slope', 'set_arm_start_external_slope', 'get_arm_start_external_delay', 'set_arm_start_external_delay', 'get_arm_stop_type', 'set_arm_stop_type', 'get_arm_stop_external_source', 'set_arm_stop_external_source', 'get_arm_stop_external_level', 'set_arm_stop_external_level', 'get_arm_stop_external_slope', 'set_arm_stop_external_slope', 'get_arm_stop_external_delay', 'set_arm_stop_external_delay', 'measurement_abort', 'measurement_is_measurement_complete', 'channels_configure', 'channels_configure_level', 'frequency_configure', 'frequency_configure_manual', 'frequency_configure_with_aperture', 'period_configure', 'period_configure_with_aperture', 'pulse_width_configure', 'duty_cycle_configure', 'edge_time_configure', 'frequency_ratio_configure', 'time_interval_configure', 'phase_configure', 'totalize_continuous_configure', 'totalize_continuous_start', 'totalize_continuous_stop', 'totalize_continuous_fetch_count', 'totalize_gated_configure', 'totalize_timed_configure', 'arm_start_external_configure', 'arm_stop_external_configure', 'measurement_fetch', 'measurement_initiate', 'measurement_read', 'get_trigger_tv_trigger_event', 'set_trigger_tv_trigger_event', 'get_trigger_tv_line_number', 'set_trigger_tv_line_number', 'get_trigger_tv_polarity', 'set_trigger_tv_polarity', 'get_trigger_tv_signal_format', 'set_trigger_tv_signal_format', 'trigger_tv_configure', 'get_trigger_glitch_condition', 'set_trigger_glitch_condition', 'get_trigger_glitch_polarity', 'set_trigger_glitch_polarity', 'get_trigger_glitch_width', 'set_trigger_glitch_width', 'trigger_glitch_configure', 'get_trigger_width_condition', 'set_trigger_width_condition', 'get_trigger_width_threshold_high', 'set_trigger_width_threshold_high', 'get_trigger_width_threshold_low', 'set_trigger_width_threshold_low', 'get_trigger_width_polarity', 'set_trigger_width_polarity', 'trigger_width_configure', 'get_trigger_ac_line_slope', 'set_trigger_ac_line_slope', 'get_reference_level_high', 'set_reference_level_high', 'get_reference_level_middle', 'set_reference_level_middle', 'get_reference_level_low', 'set_reference_level_low', 'reference_level_configure', 'channels_measurement_fetch_waveform_measurement', 'channels_measurement_read_waveform_measurement', 'get_acquisition_number_of_envelopes', 'set_acquisition_number_of_envelopes', 'channels_measurement_fetch_waveform_min_max', 'channels_measurement_read_waveform_min_max', 'get_trigger_continuous', 'set_trigger_continuous', 'get_acquisition_number_of_averages', 'set_acquisition_number_of_averages', 'get_acquisition_sample_mode', 'set_acquisition_sample_mode', 'get_trigger_modifier', 'set_trigger_modifier', 'measurement_auto_setup', 'system_fetch_setup', 'system_load_setup', 'display_fetch_screenshot', 'initialize', 'get_initialized', 'close', 'get_driver_operation_cache', 'set_driver_operation_cache', 'get_driver_operation_driver_setup', 'get_driver_operation_interchange_check', 'set_driver_operation_interchange_check', 'get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status', 'get_driver_operation_range_check', 'set_driver_operation_range_check', 'get_driver_operation_record_coercions', 'set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check', 'get_identity_description', 'get_identity_identifier', 'get_identity_revision', 'get_identity_vendor', 'get_identity_instrument_manufacturer', 'get_identity_instrument_model', 'get_identity_instrument_firmware_revision', 'get_identity_specification_major_version', 'get_identity_specification_minor_version', 'get_identity_supported_instrument_models', 'get_identity_group_capabilities', 'identity_get_group_capabilities', 'identity_get_supported_instrument_models', 'utility_disable', 'utility_error_query', 'utility_lock_object', 'utility_reset', 'utility_reset_with_defaults', 'utility_self_test', 'utility_unlock_object'], 'action_targets': {'get_channels_common_mode': '_get_channel_common_mode', 'set_channels_common_mode': '_set_channel_common_mode', 'get_channels_differential': '_get_channel_differential', 'set_channels_differential': '_set_channel_differential', 'get_channels_differential_skew': '_get_channel_differential_skew', 'set_channels_differential_skew': '_set_channel_differential_skew', 'get_channels_display_auto': '_get_channel_display_auto', 'set_channels_display_auto': '_set_channel_display_auto', 'get_channels_display_offset': '_get_channel_display_offset', 'set_channels_display_offset': '_set_channel_display_offset', 'get_channels_display_range': '_get_channel_display_range', 'set_channels_display_range': '_set_channel_display_range', 'get_channels_display_scale': '_get_channel_display_scale', 'set_channels_display_scale': '_set_channel_display_scale', 'get_display_color_grade': '_get_display_color_grade', 'set_display_color_grade': '_set_display_color_grade', 'display_fetch_color_grade_levels': '_fetch_display_color_grade_levels', 'acquisition_segmented_analyze': '_acquisition_segmented_analyze', 'get_acquisition_segmented_count': '_get_acquisition_segmented_count', 'set_acquisition_segmented_count': '_set_acquisition_segmented_count', 'get_acquisition_segmented_index': '_get_acquisition_segmented_index', 'set_acquisition_segmented_index': '_set_acquisition_segmented_index', 'get_acquisition_segmented_acquired_count': '_get_acquisition_segmented_acquired_count', 'get_acquisition_segmented_time_tag': '_get_acquisition_segmented_time_tag', 'get_channels_bw_limit': '_get_channel_bw_limit', 'set_channels_bw_limit': '_set_channel_bw_limit', 'get_channels_invert': '_get_channel_invert', 'set_channels_invert': '_set_channel_invert', 'get_channels_label': '_get_channel_label', 'set_channels_label': '_set_channel_label', 'get_channels_probe_id': '_get_channel_probe_id', 'get_channels_probe_skew': '_get_channel_probe_skew', 'set_channels_probe_skew': '_set_channel_probe_skew', 'get_channels_scale': '_get_channel_scale', 'set_channels_scale': '_set_channel_scale', 'get_channels_trigger_level': '_get_channel_trigger_level', 'set_channels_trigger_level': '_set_channel_trigger_level', 'get_timebase_mode': '_get_timebase_mode', 'set_timebase_mode': '_set_timebase_mode', 'get_timebase_reference': '_get_timebase_reference', 'set_timebase_reference': '_set_timebase_reference', 'get_timebase_position': '_get_timebase_position', 'set_timebase_position': '_set_timebase_position', 'get_timebase_range': '_get_timebase_range', 'set_timebase_range': '_set_timebase_range', 'get_timebase_scale': '_get_timebase_scale', 'set_timebase_scale': '_set_timebase_scale', 'get_timebase_window_position': '_get_timebase_window_position', 'set_timebase_window_position': '_set_timebase_window_position', 'get_timebase_window_range': '_get_timebase_window_range', 'set_timebase_window_range': '_set_timebase_window_range', 'get_timebase_window_scale': '_get_timebase_window_scale', 'set_timebase_window_scale': '_set_timebase_window_scale', 'get_display_vectors': '_get_display_vectors', 'set_display_vectors': '_set_display_vectors', 'get_display_labels': '_get_display_labels', 'set_display_labels': '_set_display_labels', 'display_clear': '_display_clear', 'system_display_string': '_system_display_string', 'get_identity_instrument_serial_number': '_get_identity_instrument_serial_number', 'memory_save': '_memory_save', 'memory_recall': '_memory_recall', 'get_measurement_function': '_get_measurement_function', 'set_measurement_function': '_set_measurement_function', 'get_channels_name': '_get_channel_name', 'get_channels_impedance': '_get_channel_impedance', 'set_channels_impedance': '_set_channel_impedance', 'get_channels_coupling': '_get_channel_coupling', 'set_channels_coupling': '_set_channel_coupling', 'get_channels_attenuation': '_get_channel_attenuation', 'set_channels_attenuation': '_set_channel_attenuation', 'get_channels_level': '_get_channel_level', 'set_channels_level': '_set_channel_level', 'get_channels_hysteresis': '_get_channel_hysteresis', 'set_channels_hysteresis': '_set_channel_hysteresis', 'get_channels_slope': '_get_channel_slope', 'set_channels_slope': '_set_channel_slope', 'get_channels_filter_enabled': '_get_channel_filter_enabled', 'set_channels_filter_enabled': '_set_channel_filter_enabled', 'get_frequency_channel': '_get_frequency_channel', 'set_frequency_channel': '_set_frequency_channel', 'get_frequency_estimate': '_get_frequency_estimate', 'set_frequency_estimate': '_set_frequency_estimate', 'get_frequency_resolution': '_get_frequency_resolution', 'set_frequency_resolution': '_set_frequency_resolution', 'get_frequency_aperture_time': '_get_frequency_aperture_time', 'set_frequency_aperture_time': '_set_frequency_aperture_time', 'get_frequency_estimate_auto': '_get_frequency_estimate_auto', 'set_frequency_estimate_auto': '_set_frequency_estimate_auto', 'get_frequency_resolution_auto': '_get_frequency_resolution_auto', 'set_frequency_resolution_auto': '_set_frequency_resolution_auto', 'get_period_channel': '_get_period_channel', 'set_period_channel': '_set_period_channel', 'get_period_estimate': '_get_period_estimate', 'set_period_estimate': '_set_period_estimate', 'get_period_resolution': '_get_period_resolution', 'set_period_resolution': '_set_period_resolution', 'get_period_aperture_time': '_get_period_aperture_time', 'set_period_aperture_time': '_set_period_aperture_time', 'get_pulse_width_channel': '_get_pulse_width_channel', 'set_pulse_width_channel': '_set_pulse_width_channel', 'get_pulse_width_estimate': '_get_pulse_width_estimate', 'set_pulse_width_estimate': '_set_pulse_width_estimate', 'get_pulse_width_resolution': '_get_pulse_width_resolution', 'set_pulse_width_resolution': '_set_pulse_width_resolution', 'get_duty_cycle_channel': '_get_duty_cycle_channel', 'set_duty_cycle_channel': '_set_duty_cycle_channel', 'get_duty_cycle_frequency_estimate': '_get_duty_cycle_frequency_estimate', 'set_duty_cycle_frequency_estimate': '_set_duty_cycle_frequency_estimate', 'get_duty_cycle_resolution': '_get_duty_cycle_resolution', 'set_duty_cycle_resolution': '_set_duty_cycle_resolution', 'get_edge_time_channel': '_get_edge_time_channel', 'set_edge_time_channel': '_set_edge_time_channel', 'get_edge_time_reference_type': '_get_edge_time_reference_type', 'set_edge_time_reference_type': '_set_edge_time_reference_type', 'get_edge_time_estimate': '_get_edge_time_estimate', 'set_edge_time_estimate': '_set_edge_time_estimate', 'get_edge_time_resolution': '_get_edge_time_resolution', 'set_edge_time_resolution': '_set_edge_time_resolution', 'get_edge_time_high_reference': '_get_edge_time_high_reference', 'set_edge_time_high_reference': '_set_edge_time_high_reference', 'get_edge_time_low_reference': '_get_edge_time_low_reference', 'set_edge_time_low_reference': '_set_edge_time_low_reference', 'get_frequency_ratio_numerator_channel': '_get_frequency_ratio_numerator_channel', 'set_frequency_ratio_numerator_channel': '_set_frequency_ratio_numerator_channel', 'get_frequency_ratio_denominator_channel': '_get_frequency_ratio_denominator_channel', 'set_frequency_ratio_denominator_channel': '_set_frequency_ratio_denominator_channel', 'get_frequency_ratio_numerator_frequency_estimate': '_get_frequency_ratio_numerator_frequency_estimate', 'set_frequency_ratio_numerator_frequency_estimate': '_set_frequency_ratio_numerator_frequency_estimate', 'get_frequency_ratio_estimate': '_get_frequency_ratio_estimate', 'set_frequency_ratio_estimate': '_set_frequency_ratio_estimate', 'get_frequency_ratio_resolution': '_get_frequency_ratio_resolution', 'set_frequency_ratio_resolution': '_set_frequency_ratio_resolution', 'get_time_interval_start_channel': '_get_time_interval_start_channel', 'set_time_interval_start_channel': '_set_time_interval_start_channel', 'get_time_interval_stop_channel': '_get_time_interval_stop_channel', 'set_time_interval_stop_channel': '_set_time_interval_stop_channel', 'get_time_interval_estimate': '_get_time_interval_estimate', 'set_time_interval_estimate': '_set_time_interval_estimate', 'get_time_interval_resolution': '_get_time_interval_resolution', 'set_time_interval_resolution': '_set_time_interval_resolution', 'get_phase_input_channel': '_get_phase_input_channel', 'set_phase_input_channel': '_set_phase_input_channel', 'get_phase_reference_channel': '_get_phase_reference_channel', 'set_phase_reference_channel': '_set_phase_reference_channel', 'get_phase_frequency_estimate': '_get_phase_frequency_estimate', 'set_phase_frequency_estimate': '_set_phase_frequency_estimate', 'get_phase_resolution': '_get_phase_resolution', 'set_phase_resolution': '_set_phase_resolution', 'get_totalize_continuous_channel': '_get_totalize_continuous_channel', 'set_totalize_continuous_channel': '_set_totalize_continuous_channel', 'get_totalize_gated_channel': '_get_totalize_gated_channel', 'set_totalize_gated_channel': '_set_totalize_gated_channel', 'get_totalize_gated_gate_source': '_get_totalize_gated_gate_source', 'set_totalize_gated_gate_source': '_set_totalize_gated_gate_source', 'get_totalize_gated_gate_slope': '_get_totalize_gated_gate_slope', 'set_totalize_gated_gate_slope': '_set_totalize_gated_gate_slope', 'get_totalize_timed_channel': '_get_totalize_timed_channel', 'set_totalize_timed_channel': '_set_totalize_timed_channel', 'get_totalize_timed_gate_time': '_get_totalize_timed_gate_time', 'set_totalize_timed_gate_time': '_set_totalize_timed_gate_time', 'get_arm_start_type': '_get_arm_start_type', 'set_arm_start_type': '_set_arm_start_type', 'get_arm_start_external_source': '_get_arm_start_external_source', 'set_arm_start_external_source': '_set_arm_start_external_source', 'get_arm_start_external_level': '_get_arm_start_external_level', 'set_arm_start_external_level': '_set_arm_start_external_level', 'get_arm_start_external_slope': '_get_arm_start_external_slope', 'set_arm_start_external_slope': '_set_arm_start_external_slope', 'get_arm_start_external_delay': '_get_arm_start_external_delay', 'set_arm_start_external_delay': '_set_arm_start_external_delay', 'get_arm_stop_type': '_get_arm_stop_type', 'set_arm_stop_type': '_set_arm_stop_type', 'get_arm_stop_external_source': '_get_arm_stop_external_source', 'set_arm_stop_external_source': '_set_arm_stop_external_source', 'get_arm_stop_external_level': '_get_arm_stop_external_level', 'set_arm_stop_external_level': '_set_arm_stop_external_level', 'get_arm_stop_external_slope': '_get_arm_stop_external_slope', 'set_arm_stop_external_slope': '_set_arm_stop_external_slope', 'get_arm_stop_external_delay': '_get_arm_stop_external_delay', 'set_arm_stop_external_delay': '_set_arm_stop_external_delay', 'measurement_abort': '_measurement_abort', 'measurement_is_measurement_complete': '_measurement_is_measurement_complete', 'channels_configure': '_channel_configure', 'channels_configure_level': '_channel_configure_level', 'frequency_configure': '_frequency_configure', 'frequency_configure_manual': '_frequency_configure_manual', 'frequency_configure_with_aperture': '_frequency_configure_with_aperture', 'period_configure': '_period_configure', 'period_configure_with_aperture': '_period_configure_with_aperture', 'pulse_width_configure': '_pulse_width_configure', 'duty_cycle_configure': '_duty_cycle_configure', 'edge_time_configure': '_edge_time_configure_reference_levels', 'frequency_ratio_configure': '_frequency_ratio_configure', 'time_interval_configure': '_time_interval_configure', 'phase_configure': '_phase_configure', 'totalize_continuous_configure': '_totalize_continuous_configure', 'totalize_continuous_start': '_totalize_continuous_start', 'totalize_continuous_stop': '_totalize_continuous_stop', 'totalize_continuous_fetch_count': '_totalize_continuous_fetch_count', 'totalize_gated_configure': '_totalize_gated_configure', 'totalize_timed_configure': '_totalize_timed_configure', 'arm_start_external_configure': '_arm_start_external_configure', 'arm_stop_external_configure': '_arm_stop_external_configure', 'measurement_fetch': '_measurement_fetch', 'measurement_initiate': '_measurement_initiate', 'measurement_read': '_measurement_read', 'get_trigger_tv_trigger_event': '_get_trigger_tv_trigger_event', 'set_trigger_tv_trigger_event': '_set_trigger_tv_trigger_event', 'get_trigger_tv_line_number': '_get_trigger_tv_line_number', 'set_trigger_tv_line_number': '_set_trigger_tv_line_number', 'get_trigger_tv_polarity': '_get_trigger_tv_polarity', 'set_trigger_tv_polarity': '_set_trigger_tv_polarity', 'get_trigger_tv_signal_format': '_get_trigger_tv_signal_format', 'set_trigger_tv_signal_format': '_set_trigger_tv_signal_format', 'trigger_tv_configure': '_trigger_tv_configure', 'get_trigger_glitch_condition': '_get_trigger_glitch_condition', 'set_trigger_glitch_condition': '_set_trigger_glitch_condition', 'get_trigger_glitch_polarity': '_get_trigger_glitch_polarity', 'set_trigger_glitch_polarity': '_set_trigger_glitch_polarity', 'get_trigger_glitch_width': '_get_trigger_glitch_width', 'set_trigger_glitch_width': '_set_trigger_glitch_width', 'trigger_glitch_configure': '_trigger_glitch_configure', 'get_trigger_width_condition': '_get_trigger_width_condition', 'set_trigger_width_condition': '_set_trigger_width_condition', 'get_trigger_width_threshold_high': '_get_trigger_width_threshold_high', 'set_trigger_width_threshold_high': '_set_trigger_width_threshold_high', 'get_trigger_width_threshold_low': '_get_trigger_width_threshold_low', 'set_trigger_width_threshold_low': '_set_trigger_width_threshold_low', 'get_trigger_width_polarity': '_get_trigger_width_polarity', 'set_trigger_width_polarity': '_set_trigger_width_polarity', 'trigger_width_configure': '_trigger_width_configure', 'get_trigger_ac_line_slope': '_get_trigger_ac_line_slope', 'set_trigger_ac_line_slope': '_set_trigger_ac_line_slope', 'get_reference_level_high': '_get_reference_level_high', 'set_reference_level_high': '_set_reference_level_high', 'get_reference_level_middle': '_get_reference_level_middle', 'set_reference_level_middle': '_set_reference_level_middle', 'get_reference_level_low': '_get_reference_level_low', 'set_reference_level_low': '_set_reference_level_low', 'reference_level_configure': '_reference_level_configure', 'channels_measurement_fetch_waveform_measurement': '_measurement_fetch_waveform_measurement', 'channels_measurement_read_waveform_measurement': '_measurement_read_waveform_measurement', 'get_acquisition_number_of_envelopes': '_get_acquisition_number_of_envelopes', 'set_acquisition_number_of_envelopes': '_set_acquisition_number_of_envelopes', 'channels_measurement_fetch_waveform_min_max': '_measurement_fetch_waveform_min_max', 'channels_measurement_read_waveform_min_max': '_measurement_read_waveform_min_max', 'get_trigger_continuous': '_get_trigger_continuous', 'set_trigger_continuous': '_set_trigger_continuous', 'get_acquisition_number_of_averages': '_get_acquisition_number_of_averages', 'set_acquisition_number_of_averages': '_set_acquisition_number_of_averages', 'get_acquisition_sample_mode': '_get_acquisition_sample_mode', 'set_acquisition_sample_mode': '_set_acquisition_sample_mode', 'get_trigger_modifier': '_get_trigger_modifier', 'set_trigger_modifier': '_set_trigger_modifier', 'measurement_auto_setup': '_measurement_auto_setup', 'system_fetch_setup': '_system_fetch_setup', 'system_load_setup': '_system_load_setup', 'display_fetch_screenshot': '_display_fetch_screenshot', 'initialize': '_initialize', 'get_initialized': '_get_initialized', 'close': '_close', 'get_driver_operation_cache': '_get_driver_operation_cache', 'set_driver_operation_cache': '_set_driver_operation_cache', 'get_driver_operation_driver_setup': '_get_driver_operation_driver_setup', 'get_driver_operation_interchange_check': '_get_driver_operation_interchange_check', 'set_driver_operation_interchange_check': '_set_driver_operation_interchange_check', 'get_driver_operation_logical_name': '_get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status': '_get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status': '_set_driver_operation_query_instrument_status', 'get_driver_operation_range_check': '_get_driver_operation_range_check', 'set_driver_operation_range_check': '_set_driver_operation_range_check', 'get_driver_operation_record_coercions': '_get_driver_operation_record_coercions', 'set_driver_operation_record_coercions': '_set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor': '_get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate': '_get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings': '_driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record': '_driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning': '_driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes': '_driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check': '_driver_operation_reset_interchange_check', 'get_identity_description': '_get_identity_description', 'get_identity_identifier': '_get_identity_identifier', 'get_identity_revision': '_get_identity_revision', 'get_identity_vendor': '_get_identity_vendor', 'get_identity_instrument_manufacturer': '_get_identity_instrument_manufacturer', 'get_identity_instrument_model': '_get_identity_instrument_model', 'get_identity_instrument_firmware_revision': '_get_identity_instrument_firmware_revision', 'get_identity_specification_major_version': '_get_identity_specification_major_version', 'get_identity_specification_minor_version': '_get_identity_specification_minor_version', 'get_identity_supported_instrument_models': '_get_identity_supported_instrument_models', 'get_identity_group_capabilities': '_get_identity_group_capabilities', 'identity_get_group_capabilities': '_identity_get_group_capabilities', 'identity_get_supported_instrument_models': '_identity_get_supported_instrument_models', 'utility_disable': '_utility_disable', 'utility_error_query': '_utility_error_query', 'utility_lock_object': '_utility_lock_object', 'utility_reset': '_utility_reset', 'utility_reset_with_defaults': '_utility_reset_with_defaults', 'utility_self_test': '_utility_self_test', 'utility_unlock_object': '_utility_unlock_object'}, 'metadata': {'repo': 'python-ivi/python-ivi', 'repo_url': 'https://github.com/python-ivi/python-ivi', 'source_url': 'https://github.com/python-ivi/python-ivi/blob/main/ivi/agilent/agilentMSOX92504A.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_channels_common_mode': '_get_channel_common_mode', 'set_channels_common_mode': '_set_channel_common_mode', 'get_channels_differential': '_get_channel_differential', 'set_channels_differential': '_set_channel_differential', 'get_channels_differential_skew': '_get_channel_differential_skew', 'set_channels_differential_skew': '_set_channel_differential_skew', 'get_channels_display_auto': '_get_channel_display_auto', 'set_channels_display_auto': '_set_channel_display_auto', 'get_channels_display_offset': '_get_channel_display_offset', 'set_channels_display_offset': '_set_channel_display_offset', 'get_channels_display_range': '_get_channel_display_range', 'set_channels_display_range': '_set_channel_display_range', 'get_channels_display_scale': '_get_channel_display_scale', 'set_channels_display_scale': '_set_channel_display_scale', 'get_display_color_grade': '_get_display_color_grade', 'set_display_color_grade': '_set_display_color_grade', 'display_fetch_color_grade_levels': '_fetch_display_color_grade_levels', 'acquisition_segmented_analyze': '_acquisition_segmented_analyze', 'get_acquisition_segmented_count': '_get_acquisition_segmented_count', 'set_acquisition_segmented_count': '_set_acquisition_segmented_count', 'get_acquisition_segmented_index': '_get_acquisition_segmented_index', 'set_acquisition_segmented_index': '_set_acquisition_segmented_index', 'get_acquisition_segmented_acquired_count': '_get_acquisition_segmented_acquired_count', 'get_acquisition_segmented_time_tag': '_get_acquisition_segmented_time_tag', 'get_channels_bw_limit': '_get_channel_bw_limit', 'set_channels_bw_limit': '_set_channel_bw_limit', 'get_channels_invert': '_get_channel_invert', 'set_channels_invert': '_set_channel_invert', 'get_channels_label': '_get_channel_label', 'set_channels_label': '_set_channel_label', 'get_channels_probe_id': '_get_channel_probe_id', 'get_channels_probe_skew': '_get_channel_probe_skew', 'set_channels_probe_skew': '_set_channel_probe_skew', 'get_channels_scale': '_get_channel_scale', 'set_channels_scale': '_set_channel_scale', 'get_channels_trigger_level': '_get_channel_trigger_level', 'set_channels_trigger_level': '_set_channel_trigger_level', 'get_timebase_mode': '_get_timebase_mode', 'set_timebase_mode': '_set_timebase_mode', 'get_timebase_reference': '_get_timebase_reference', 'set_timebase_reference': '_set_timebase_reference', 'get_timebase_position': '_get_timebase_position', 'set_timebase_position': '_set_timebase_position', 'get_timebase_range': '_get_timebase_range', 'set_timebase_range': '_set_timebase_range', 'get_timebase_scale': '_get_timebase_scale', 'set_timebase_scale': '_set_timebase_scale', 'get_timebase_window_position': '_get_timebase_window_position', 'set_timebase_window_position': '_set_timebase_window_position', 'get_timebase_window_range': '_get_timebase_window_range', 'set_timebase_window_range': '_set_timebase_window_range', 'get_timebase_window_scale': '_get_timebase_window_scale', 'set_timebase_window_scale': '_set_timebase_window_scale', 'get_display_vectors': '_get_display_vectors', 'set_display_vectors': '_set_display_vectors', 'get_display_labels': '_get_display_labels', 'set_display_labels': '_set_display_labels', 'display_clear': '_display_clear', 'system_display_string': '_system_display_string', 'get_identity_instrument_serial_number': '_get_identity_instrument_serial_number', 'memory_save': '_memory_save', 'memory_recall': '_memory_recall', 'get_measurement_function': '_get_measurement_function', 'set_measurement_function': '_set_measurement_function', 'get_channels_name': '_get_channel_name', 'get_channels_impedance': '_get_channel_impedance', 'set_channels_impedance': '_set_channel_impedance', 'get_channels_coupling': '_get_channel_coupling', 'set_channels_coupling': '_set_channel_coupling', 'get_channels_attenuation': '_get_channel_attenuation', 'set_channels_attenuation': '_set_channel_attenuation', 'get_channels_level': '_get_channel_level', 'set_channels_level': '_set_channel_level', 'get_channels_hysteresis': '_get_channel_hysteresis', 'set_channels_hysteresis': '_set_channel_hysteresis', 'get_channels_slope': '_get_channel_slope', 'set_channels_slope': '_set_channel_slope', 'get_channels_filter_enabled': '_get_channel_filter_enabled', 'set_channels_filter_enabled': '_set_channel_filter_enabled', 'get_frequency_channel': '_get_frequency_channel', 'set_frequency_channel': '_set_frequency_channel', 'get_frequency_estimate': '_get_frequency_estimate', 'set_frequency_estimate': '_set_frequency_estimate', 'get_frequency_resolution': '_get_frequency_resolution', 'set_frequency_resolution': '_set_frequency_resolution', 'get_frequency_aperture_time': '_get_frequency_aperture_time', 'set_frequency_aperture_time': '_set_frequency_aperture_time', 'get_frequency_estimate_auto': '_get_frequency_estimate_auto', 'set_frequency_estimate_auto': '_set_frequency_estimate_auto', 'get_frequency_resolution_auto': '_get_frequency_resolution_auto', 'set_frequency_resolution_auto': '_set_frequency_resolution_auto', 'get_period_channel': '_get_period_channel', 'set_period_channel': '_set_period_channel', 'get_period_estimate': '_get_period_estimate', 'set_period_estimate': '_set_period_estimate', 'get_period_resolution': '_get_period_resolution', 'set_period_resolution': '_set_period_resolution', 'get_period_aperture_time': '_get_period_aperture_time', 'set_period_aperture_time': '_set_period_aperture_time', 'get_pulse_width_channel': '_get_pulse_width_channel', 'set_pulse_width_channel': '_set_pulse_width_channel', 'get_pulse_width_estimate': '_get_pulse_width_estimate', 'set_pulse_width_estimate': '_set_pulse_width_estimate', 'get_pulse_width_resolution': '_get_pulse_width_resolution', 'set_pulse_width_resolution': '_set_pulse_width_resolution', 'get_duty_cycle_channel': '_get_duty_cycle_channel', 'set_duty_cycle_channel': '_set_duty_cycle_channel', 'get_duty_cycle_frequency_estimate': '_get_duty_cycle_frequency_estimate', 'set_duty_cycle_frequency_estimate': '_set_duty_cycle_frequency_estimate', 'get_duty_cycle_resolution': '_get_duty_cycle_resolution', 'set_duty_cycle_resolution': '_set_duty_cycle_resolution', 'get_edge_time_channel': '_get_edge_time_channel', 'set_edge_time_channel': '_set_edge_time_channel', 'get_edge_time_reference_type': '_get_edge_time_reference_type', 'set_edge_time_reference_type': '_set_edge_time_reference_type', 'get_edge_time_estimate': '_get_edge_time_estimate', 'set_edge_time_estimate': '_set_edge_time_estimate', 'get_edge_time_resolution': '_get_edge_time_resolution', 'set_edge_time_resolution': '_set_edge_time_resolution', 'get_edge_time_high_reference': '_get_edge_time_high_reference', 'set_edge_time_high_reference': '_set_edge_time_high_reference', 'get_edge_time_low_reference': '_get_edge_time_low_reference', 'set_edge_time_low_reference': '_set_edge_time_low_reference', 'get_frequency_ratio_numerator_channel': '_get_frequency_ratio_numerator_channel', 'set_frequency_ratio_numerator_channel': '_set_frequency_ratio_numerator_channel', 'get_frequency_ratio_denominator_channel': '_get_frequency_ratio_denominator_channel', 'set_frequency_ratio_denominator_channel': '_set_frequency_ratio_denominator_channel', 'get_frequency_ratio_numerator_frequency_estimate': '_get_frequency_ratio_numerator_frequency_estimate', 'set_frequency_ratio_numerator_frequency_estimate': '_set_frequency_ratio_numerator_frequency_estimate', 'get_frequency_ratio_estimate': '_get_frequency_ratio_estimate', 'set_frequency_ratio_estimate': '_set_frequency_ratio_estimate', 'get_frequency_ratio_resolution': '_get_frequency_ratio_resolution', 'set_frequency_ratio_resolution': '_set_frequency_ratio_resolution', 'get_time_interval_start_channel': '_get_time_interval_start_channel', 'set_time_interval_start_channel': '_set_time_interval_start_channel', 'get_time_interval_stop_channel': '_get_time_interval_stop_channel', 'set_time_interval_stop_channel': '_set_time_interval_stop_channel', 'get_time_interval_estimate': '_get_time_interval_estimate', 'set_time_interval_estimate': '_set_time_interval_estimate', 'get_time_interval_resolution': '_get_time_interval_resolution', 'set_time_interval_resolution': '_set_time_interval_resolution', 'get_phase_input_channel': '_get_phase_input_channel', 'set_phase_input_channel': '_set_phase_input_channel', 'get_phase_reference_channel': '_get_phase_reference_channel', 'set_phase_reference_channel': '_set_phase_reference_channel', 'get_phase_frequency_estimate': '_get_phase_frequency_estimate', 'set_phase_frequency_estimate': '_set_phase_frequency_estimate', 'get_phase_resolution': '_get_phase_resolution', 'set_phase_resolution': '_set_phase_resolution', 'get_totalize_continuous_channel': '_get_totalize_continuous_channel', 'set_totalize_continuous_channel': '_set_totalize_continuous_channel', 'get_totalize_gated_channel': '_get_totalize_gated_channel', 'set_totalize_gated_channel': '_set_totalize_gated_channel', 'get_totalize_gated_gate_source': '_get_totalize_gated_gate_source', 'set_totalize_gated_gate_source': '_set_totalize_gated_gate_source', 'get_totalize_gated_gate_slope': '_get_totalize_gated_gate_slope', 'set_totalize_gated_gate_slope': '_set_totalize_gated_gate_slope', 'get_totalize_timed_channel': '_get_totalize_timed_channel', 'set_totalize_timed_channel': '_set_totalize_timed_channel', 'get_totalize_timed_gate_time': '_get_totalize_timed_gate_time', 'set_totalize_timed_gate_time': '_set_totalize_timed_gate_time', 'get_arm_start_type': '_get_arm_start_type', 'set_arm_start_type': '_set_arm_start_type', 'get_arm_start_external_source': '_get_arm_start_external_source', 'set_arm_start_external_source': '_set_arm_start_external_source', 'get_arm_start_external_level': '_get_arm_start_external_level', 'set_arm_start_external_level': '_set_arm_start_external_level', 'get_arm_start_external_slope': '_get_arm_start_external_slope', 'set_arm_start_external_slope': '_set_arm_start_external_slope', 'get_arm_start_external_delay': '_get_arm_start_external_delay', 'set_arm_start_external_delay': '_set_arm_start_external_delay', 'get_arm_stop_type': '_get_arm_stop_type', 'set_arm_stop_type': '_set_arm_stop_type', 'get_arm_stop_external_source': '_get_arm_stop_external_source', 'set_arm_stop_external_source': '_set_arm_stop_external_source', 'get_arm_stop_external_level': '_get_arm_stop_external_level', 'set_arm_stop_external_level': '_set_arm_stop_external_level', 'get_arm_stop_external_slope': '_get_arm_stop_external_slope', 'set_arm_stop_external_slope': '_set_arm_stop_external_slope', 'get_arm_stop_external_delay': '_get_arm_stop_external_delay', 'set_arm_stop_external_delay': '_set_arm_stop_external_delay', 'measurement_abort': '_measurement_abort', 'measurement_is_measurement_complete': '_measurement_is_measurement_complete', 'channels_configure': '_channel_configure', 'channels_configure_level': '_channel_configure_level', 'frequency_configure': '_frequency_configure', 'frequency_configure_manual': '_frequency_configure_manual', 'frequency_configure_with_aperture': '_frequency_configure_with_aperture', 'period_configure': '_period_configure', 'period_configure_with_aperture': '_period_configure_with_aperture', 'pulse_width_configure': '_pulse_width_configure', 'duty_cycle_configure': '_duty_cycle_configure', 'edge_time_configure': '_edge_time_configure_reference_levels', 'frequency_ratio_configure': '_frequency_ratio_configure', 'time_interval_configure': '_time_interval_configure', 'phase_configure': '_phase_configure', 'totalize_continuous_configure': '_totalize_continuous_configure', 'totalize_continuous_start': '_totalize_continuous_start', 'totalize_continuous_stop': '_totalize_continuous_stop', 'totalize_continuous_fetch_count': '_totalize_continuous_fetch_count', 'totalize_gated_configure': '_totalize_gated_configure', 'totalize_timed_configure': '_totalize_timed_configure', 'arm_start_external_configure': '_arm_start_external_configure', 'arm_stop_external_configure': '_arm_stop_external_configure', 'measurement_fetch': '_measurement_fetch', 'measurement_initiate': '_measurement_initiate', 'measurement_read': '_measurement_read', 'get_trigger_tv_trigger_event': '_get_trigger_tv_trigger_event', 'set_trigger_tv_trigger_event': '_set_trigger_tv_trigger_event', 'get_trigger_tv_line_number': '_get_trigger_tv_line_number', 'set_trigger_tv_line_number': '_set_trigger_tv_line_number', 'get_trigger_tv_polarity': '_get_trigger_tv_polarity', 'set_trigger_tv_polarity': '_set_trigger_tv_polarity', 'get_trigger_tv_signal_format': '_get_trigger_tv_signal_format', 'set_trigger_tv_signal_format': '_set_trigger_tv_signal_format', 'trigger_tv_configure': '_trigger_tv_configure', 'get_trigger_glitch_condition': '_get_trigger_glitch_condition', 'set_trigger_glitch_condition': '_set_trigger_glitch_condition', 'get_trigger_glitch_polarity': '_get_trigger_glitch_polarity', 'set_trigger_glitch_polarity': '_set_trigger_glitch_polarity', 'get_trigger_glitch_width': '_get_trigger_glitch_width', 'set_trigger_glitch_width': '_set_trigger_glitch_width', 'trigger_glitch_configure': '_trigger_glitch_configure', 'get_trigger_width_condition': '_get_trigger_width_condition', 'set_trigger_width_condition': '_set_trigger_width_condition', 'get_trigger_width_threshold_high': '_get_trigger_width_threshold_high', 'set_trigger_width_threshold_high': '_set_trigger_width_threshold_high', 'get_trigger_width_threshold_low': '_get_trigger_width_threshold_low', 'set_trigger_width_threshold_low': '_set_trigger_width_threshold_low', 'get_trigger_width_polarity': '_get_trigger_width_polarity', 'set_trigger_width_polarity': '_set_trigger_width_polarity', 'trigger_width_configure': '_trigger_width_configure', 'get_trigger_ac_line_slope': '_get_trigger_ac_line_slope', 'set_trigger_ac_line_slope': '_set_trigger_ac_line_slope', 'get_reference_level_high': '_get_reference_level_high', 'set_reference_level_high': '_set_reference_level_high', 'get_reference_level_middle': '_get_reference_level_middle', 'set_reference_level_middle': '_set_reference_level_middle', 'get_reference_level_low': '_get_reference_level_low', 'set_reference_level_low': '_set_reference_level_low', 'reference_level_configure': '_reference_level_configure', 'channels_measurement_fetch_waveform_measurement': '_measurement_fetch_waveform_measurement', 'channels_measurement_read_waveform_measurement': '_measurement_read_waveform_measurement', 'get_acquisition_number_of_envelopes': '_get_acquisition_number_of_envelopes', 'set_acquisition_number_of_envelopes': '_set_acquisition_number_of_envelopes', 'channels_measurement_fetch_waveform_min_max': '_measurement_fetch_waveform_min_max', 'channels_measurement_read_waveform_min_max': '_measurement_read_waveform_min_max', 'get_trigger_continuous': '_get_trigger_continuous', 'set_trigger_continuous': '_set_trigger_continuous', 'get_acquisition_number_of_averages': '_get_acquisition_number_of_averages', 'set_acquisition_number_of_averages': '_set_acquisition_number_of_averages', 'get_acquisition_sample_mode': '_get_acquisition_sample_mode', 'set_acquisition_sample_mode': '_set_acquisition_sample_mode', 'get_trigger_modifier': '_get_trigger_modifier', 'set_trigger_modifier': '_set_trigger_modifier', 'measurement_auto_setup': '_measurement_auto_setup', 'system_fetch_setup': '_system_fetch_setup', 'system_load_setup': '_system_load_setup', 'display_fetch_screenshot': '_display_fetch_screenshot', 'initialize': '_initialize', 'get_initialized': '_get_initialized', 'close': '_close', 'get_driver_operation_cache': '_get_driver_operation_cache', 'set_driver_operation_cache': '_set_driver_operation_cache', 'get_driver_operation_driver_setup': '_get_driver_operation_driver_setup', 'get_driver_operation_interchange_check': '_get_driver_operation_interchange_check', 'set_driver_operation_interchange_check': '_set_driver_operation_interchange_check', 'get_driver_operation_logical_name': '_get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status': '_get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status': '_set_driver_operation_query_instrument_status', 'get_driver_operation_range_check': '_get_driver_operation_range_check', 'set_driver_operation_range_check': '_set_driver_operation_range_check', 'get_driver_operation_record_coercions': '_get_driver_operation_record_coercions', 'set_driver_operation_record_coercions': '_set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor': '_get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate': '_get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings': '_driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record': '_driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning': '_driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes': '_driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check': '_driver_operation_reset_interchange_check', 'get_identity_description': '_get_identity_description', 'get_identity_identifier': '_get_identity_identifier', 'get_identity_revision': '_get_identity_revision', 'get_identity_vendor': '_get_identity_vendor', 'get_identity_instrument_manufacturer': '_get_identity_instrument_manufacturer', 'get_identity_instrument_model': '_get_identity_instrument_model', 'get_identity_instrument_firmware_revision': '_get_identity_instrument_firmware_revision', 'get_identity_specification_major_version': '_get_identity_specification_major_version', 'get_identity_specification_minor_version': '_get_identity_specification_minor_version', 'get_identity_supported_instrument_models': '_get_identity_supported_instrument_models', 'get_identity_group_capabilities': '_get_identity_group_capabilities', 'identity_get_group_capabilities': '_identity_get_group_capabilities', 'identity_get_supported_instrument_models': '_identity_get_supported_instrument_models', 'utility_disable': '_utility_disable', 'utility_error_query': '_utility_error_query', 'utility_lock_object': '_utility_lock_object', 'utility_reset': '_utility_reset', 'utility_reset_with_defaults': '_utility_reset_with_defaults', 'utility_self_test': '_utility_self_test', 'utility_unlock_object': '_utility_unlock_object'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_channels_common_mode(self, **kwargs):
        return self.call('get_channels_common_mode', kwargs=kwargs)

    def set_channels_common_mode(self, **kwargs):
        return self.call('set_channels_common_mode', kwargs=kwargs)

    def get_channels_differential(self, **kwargs):
        return self.call('get_channels_differential', kwargs=kwargs)

    def set_channels_differential(self, **kwargs):
        return self.call('set_channels_differential', kwargs=kwargs)

    def get_channels_differential_skew(self, **kwargs):
        return self.call('get_channels_differential_skew', kwargs=kwargs)

    def set_channels_differential_skew(self, **kwargs):
        return self.call('set_channels_differential_skew', kwargs=kwargs)

    def get_channels_display_auto(self, **kwargs):
        return self.call('get_channels_display_auto', kwargs=kwargs)

    def set_channels_display_auto(self, **kwargs):
        return self.call('set_channels_display_auto', kwargs=kwargs)

    def get_channels_display_offset(self, **kwargs):
        return self.call('get_channels_display_offset', kwargs=kwargs)

    def set_channels_display_offset(self, **kwargs):
        return self.call('set_channels_display_offset', kwargs=kwargs)

    def get_channels_display_range(self, **kwargs):
        return self.call('get_channels_display_range', kwargs=kwargs)

    def set_channels_display_range(self, **kwargs):
        return self.call('set_channels_display_range', kwargs=kwargs)

    def get_channels_display_scale(self, **kwargs):
        return self.call('get_channels_display_scale', kwargs=kwargs)

    def set_channels_display_scale(self, **kwargs):
        return self.call('set_channels_display_scale', kwargs=kwargs)

    def get_display_color_grade(self, **kwargs):
        return self.call('get_display_color_grade', kwargs=kwargs)

    def set_display_color_grade(self, **kwargs):
        return self.call('set_display_color_grade', kwargs=kwargs)

    def display_fetch_color_grade_levels(self, **kwargs):
        return self.call('display_fetch_color_grade_levels', kwargs=kwargs)

    def acquisition_segmented_analyze(self, **kwargs):
        return self.call('acquisition_segmented_analyze', kwargs=kwargs)

    def get_acquisition_segmented_count(self, **kwargs):
        return self.call('get_acquisition_segmented_count', kwargs=kwargs)

    def set_acquisition_segmented_count(self, **kwargs):
        return self.call('set_acquisition_segmented_count', kwargs=kwargs)

    def get_acquisition_segmented_index(self, **kwargs):
        return self.call('get_acquisition_segmented_index', kwargs=kwargs)

    def set_acquisition_segmented_index(self, **kwargs):
        return self.call('set_acquisition_segmented_index', kwargs=kwargs)

    def get_acquisition_segmented_acquired_count(self, **kwargs):
        return self.call('get_acquisition_segmented_acquired_count', kwargs=kwargs)

    def get_acquisition_segmented_time_tag(self, **kwargs):
        return self.call('get_acquisition_segmented_time_tag', kwargs=kwargs)

    def get_channels_bw_limit(self, **kwargs):
        return self.call('get_channels_bw_limit', kwargs=kwargs)

    def set_channels_bw_limit(self, **kwargs):
        return self.call('set_channels_bw_limit', kwargs=kwargs)

    def get_channels_invert(self, **kwargs):
        return self.call('get_channels_invert', kwargs=kwargs)

    def set_channels_invert(self, **kwargs):
        return self.call('set_channels_invert', kwargs=kwargs)

    def get_channels_label(self, **kwargs):
        return self.call('get_channels_label', kwargs=kwargs)

    def set_channels_label(self, **kwargs):
        return self.call('set_channels_label', kwargs=kwargs)

    def get_channels_probe_id(self, **kwargs):
        return self.call('get_channels_probe_id', kwargs=kwargs)

    def get_channels_probe_skew(self, **kwargs):
        return self.call('get_channels_probe_skew', kwargs=kwargs)

    def set_channels_probe_skew(self, **kwargs):
        return self.call('set_channels_probe_skew', kwargs=kwargs)

    def get_channels_scale(self, **kwargs):
        return self.call('get_channels_scale', kwargs=kwargs)

    def set_channels_scale(self, **kwargs):
        return self.call('set_channels_scale', kwargs=kwargs)

    def get_channels_trigger_level(self, **kwargs):
        return self.call('get_channels_trigger_level', kwargs=kwargs)

    def set_channels_trigger_level(self, **kwargs):
        return self.call('set_channels_trigger_level', kwargs=kwargs)

    def get_timebase_mode(self, **kwargs):
        return self.call('get_timebase_mode', kwargs=kwargs)

    def set_timebase_mode(self, **kwargs):
        return self.call('set_timebase_mode', kwargs=kwargs)

    def get_timebase_reference(self, **kwargs):
        return self.call('get_timebase_reference', kwargs=kwargs)

    def set_timebase_reference(self, **kwargs):
        return self.call('set_timebase_reference', kwargs=kwargs)

    def get_timebase_position(self, **kwargs):
        return self.call('get_timebase_position', kwargs=kwargs)

    def set_timebase_position(self, **kwargs):
        return self.call('set_timebase_position', kwargs=kwargs)

    def get_timebase_range(self, **kwargs):
        return self.call('get_timebase_range', kwargs=kwargs)

    def set_timebase_range(self, **kwargs):
        return self.call('set_timebase_range', kwargs=kwargs)

    def get_timebase_scale(self, **kwargs):
        return self.call('get_timebase_scale', kwargs=kwargs)

    def set_timebase_scale(self, **kwargs):
        return self.call('set_timebase_scale', kwargs=kwargs)

    def get_timebase_window_position(self, **kwargs):
        return self.call('get_timebase_window_position', kwargs=kwargs)

    def set_timebase_window_position(self, **kwargs):
        return self.call('set_timebase_window_position', kwargs=kwargs)

    def get_timebase_window_range(self, **kwargs):
        return self.call('get_timebase_window_range', kwargs=kwargs)

    def set_timebase_window_range(self, **kwargs):
        return self.call('set_timebase_window_range', kwargs=kwargs)

    def get_timebase_window_scale(self, **kwargs):
        return self.call('get_timebase_window_scale', kwargs=kwargs)

    def set_timebase_window_scale(self, **kwargs):
        return self.call('set_timebase_window_scale', kwargs=kwargs)

    def get_display_vectors(self, **kwargs):
        return self.call('get_display_vectors', kwargs=kwargs)

    def set_display_vectors(self, **kwargs):
        return self.call('set_display_vectors', kwargs=kwargs)

    def get_display_labels(self, **kwargs):
        return self.call('get_display_labels', kwargs=kwargs)

    def set_display_labels(self, **kwargs):
        return self.call('set_display_labels', kwargs=kwargs)

    def display_clear(self, **kwargs):
        return self.call('display_clear', kwargs=kwargs)

    def system_display_string(self, **kwargs):
        return self.call('system_display_string', kwargs=kwargs)

    def get_identity_instrument_serial_number(self, **kwargs):
        return self.call('get_identity_instrument_serial_number', kwargs=kwargs)

    def memory_save(self, **kwargs):
        return self.call('memory_save', kwargs=kwargs)

    def memory_recall(self, **kwargs):
        return self.call('memory_recall', kwargs=kwargs)

    def get_measurement_function(self, **kwargs):
        return self.call('get_measurement_function', kwargs=kwargs)

    def set_measurement_function(self, **kwargs):
        return self.call('set_measurement_function', kwargs=kwargs)

    def get_channels_name(self, **kwargs):
        return self.call('get_channels_name', kwargs=kwargs)

    def get_channels_impedance(self, **kwargs):
        return self.call('get_channels_impedance', kwargs=kwargs)

    def set_channels_impedance(self, **kwargs):
        return self.call('set_channels_impedance', kwargs=kwargs)

    def get_channels_coupling(self, **kwargs):
        return self.call('get_channels_coupling', kwargs=kwargs)

    def set_channels_coupling(self, **kwargs):
        return self.call('set_channels_coupling', kwargs=kwargs)

    def get_channels_attenuation(self, **kwargs):
        return self.call('get_channels_attenuation', kwargs=kwargs)

    def set_channels_attenuation(self, **kwargs):
        return self.call('set_channels_attenuation', kwargs=kwargs)

    def get_channels_level(self, **kwargs):
        return self.call('get_channels_level', kwargs=kwargs)

    def set_channels_level(self, **kwargs):
        return self.call('set_channels_level', kwargs=kwargs)

    def get_channels_hysteresis(self, **kwargs):
        return self.call('get_channels_hysteresis', kwargs=kwargs)

    def set_channels_hysteresis(self, **kwargs):
        return self.call('set_channels_hysteresis', kwargs=kwargs)

    def get_channels_slope(self, **kwargs):
        return self.call('get_channels_slope', kwargs=kwargs)

    def set_channels_slope(self, **kwargs):
        return self.call('set_channels_slope', kwargs=kwargs)

    def get_channels_filter_enabled(self, **kwargs):
        return self.call('get_channels_filter_enabled', kwargs=kwargs)

    def set_channels_filter_enabled(self, **kwargs):
        return self.call('set_channels_filter_enabled', kwargs=kwargs)

    def get_frequency_channel(self, **kwargs):
        return self.call('get_frequency_channel', kwargs=kwargs)

    def set_frequency_channel(self, **kwargs):
        return self.call('set_frequency_channel', kwargs=kwargs)

    def get_frequency_estimate(self, **kwargs):
        return self.call('get_frequency_estimate', kwargs=kwargs)

    def set_frequency_estimate(self, **kwargs):
        return self.call('set_frequency_estimate', kwargs=kwargs)

    def get_frequency_resolution(self, **kwargs):
        return self.call('get_frequency_resolution', kwargs=kwargs)

    def set_frequency_resolution(self, **kwargs):
        return self.call('set_frequency_resolution', kwargs=kwargs)

    def get_frequency_aperture_time(self, **kwargs):
        return self.call('get_frequency_aperture_time', kwargs=kwargs)

    def set_frequency_aperture_time(self, **kwargs):
        return self.call('set_frequency_aperture_time', kwargs=kwargs)

    def get_frequency_estimate_auto(self, **kwargs):
        return self.call('get_frequency_estimate_auto', kwargs=kwargs)

    def set_frequency_estimate_auto(self, **kwargs):
        return self.call('set_frequency_estimate_auto', kwargs=kwargs)

    def get_frequency_resolution_auto(self, **kwargs):
        return self.call('get_frequency_resolution_auto', kwargs=kwargs)

    def set_frequency_resolution_auto(self, **kwargs):
        return self.call('set_frequency_resolution_auto', kwargs=kwargs)

    def get_period_channel(self, **kwargs):
        return self.call('get_period_channel', kwargs=kwargs)

    def set_period_channel(self, **kwargs):
        return self.call('set_period_channel', kwargs=kwargs)

    def get_period_estimate(self, **kwargs):
        return self.call('get_period_estimate', kwargs=kwargs)

    def set_period_estimate(self, **kwargs):
        return self.call('set_period_estimate', kwargs=kwargs)

    def get_period_resolution(self, **kwargs):
        return self.call('get_period_resolution', kwargs=kwargs)

    def set_period_resolution(self, **kwargs):
        return self.call('set_period_resolution', kwargs=kwargs)

    def get_period_aperture_time(self, **kwargs):
        return self.call('get_period_aperture_time', kwargs=kwargs)

    def set_period_aperture_time(self, **kwargs):
        return self.call('set_period_aperture_time', kwargs=kwargs)

    def get_pulse_width_channel(self, **kwargs):
        return self.call('get_pulse_width_channel', kwargs=kwargs)

    def set_pulse_width_channel(self, **kwargs):
        return self.call('set_pulse_width_channel', kwargs=kwargs)

    def get_pulse_width_estimate(self, **kwargs):
        return self.call('get_pulse_width_estimate', kwargs=kwargs)

    def set_pulse_width_estimate(self, **kwargs):
        return self.call('set_pulse_width_estimate', kwargs=kwargs)

    def get_pulse_width_resolution(self, **kwargs):
        return self.call('get_pulse_width_resolution', kwargs=kwargs)

    def set_pulse_width_resolution(self, **kwargs):
        return self.call('set_pulse_width_resolution', kwargs=kwargs)

    def get_duty_cycle_channel(self, **kwargs):
        return self.call('get_duty_cycle_channel', kwargs=kwargs)

    def set_duty_cycle_channel(self, **kwargs):
        return self.call('set_duty_cycle_channel', kwargs=kwargs)

    def get_duty_cycle_frequency_estimate(self, **kwargs):
        return self.call('get_duty_cycle_frequency_estimate', kwargs=kwargs)

    def set_duty_cycle_frequency_estimate(self, **kwargs):
        return self.call('set_duty_cycle_frequency_estimate', kwargs=kwargs)

    def get_duty_cycle_resolution(self, **kwargs):
        return self.call('get_duty_cycle_resolution', kwargs=kwargs)

    def set_duty_cycle_resolution(self, **kwargs):
        return self.call('set_duty_cycle_resolution', kwargs=kwargs)

    def get_edge_time_channel(self, **kwargs):
        return self.call('get_edge_time_channel', kwargs=kwargs)

    def set_edge_time_channel(self, **kwargs):
        return self.call('set_edge_time_channel', kwargs=kwargs)

    def get_edge_time_reference_type(self, **kwargs):
        return self.call('get_edge_time_reference_type', kwargs=kwargs)

    def set_edge_time_reference_type(self, **kwargs):
        return self.call('set_edge_time_reference_type', kwargs=kwargs)

    def get_edge_time_estimate(self, **kwargs):
        return self.call('get_edge_time_estimate', kwargs=kwargs)

    def set_edge_time_estimate(self, **kwargs):
        return self.call('set_edge_time_estimate', kwargs=kwargs)

    def get_edge_time_resolution(self, **kwargs):
        return self.call('get_edge_time_resolution', kwargs=kwargs)

    def set_edge_time_resolution(self, **kwargs):
        return self.call('set_edge_time_resolution', kwargs=kwargs)

    def get_edge_time_high_reference(self, **kwargs):
        return self.call('get_edge_time_high_reference', kwargs=kwargs)

    def set_edge_time_high_reference(self, **kwargs):
        return self.call('set_edge_time_high_reference', kwargs=kwargs)

    def get_edge_time_low_reference(self, **kwargs):
        return self.call('get_edge_time_low_reference', kwargs=kwargs)

    def set_edge_time_low_reference(self, **kwargs):
        return self.call('set_edge_time_low_reference', kwargs=kwargs)

    def get_frequency_ratio_numerator_channel(self, **kwargs):
        return self.call('get_frequency_ratio_numerator_channel', kwargs=kwargs)

    def set_frequency_ratio_numerator_channel(self, **kwargs):
        return self.call('set_frequency_ratio_numerator_channel', kwargs=kwargs)

    def get_frequency_ratio_denominator_channel(self, **kwargs):
        return self.call('get_frequency_ratio_denominator_channel', kwargs=kwargs)

    def set_frequency_ratio_denominator_channel(self, **kwargs):
        return self.call('set_frequency_ratio_denominator_channel', kwargs=kwargs)

    def get_frequency_ratio_numerator_frequency_estimate(self, **kwargs):
        return self.call('get_frequency_ratio_numerator_frequency_estimate', kwargs=kwargs)

    def set_frequency_ratio_numerator_frequency_estimate(self, **kwargs):
        return self.call('set_frequency_ratio_numerator_frequency_estimate', kwargs=kwargs)

    def get_frequency_ratio_estimate(self, **kwargs):
        return self.call('get_frequency_ratio_estimate', kwargs=kwargs)

    def set_frequency_ratio_estimate(self, **kwargs):
        return self.call('set_frequency_ratio_estimate', kwargs=kwargs)

    def get_frequency_ratio_resolution(self, **kwargs):
        return self.call('get_frequency_ratio_resolution', kwargs=kwargs)

    def set_frequency_ratio_resolution(self, **kwargs):
        return self.call('set_frequency_ratio_resolution', kwargs=kwargs)

    def get_time_interval_start_channel(self, **kwargs):
        return self.call('get_time_interval_start_channel', kwargs=kwargs)

    def set_time_interval_start_channel(self, **kwargs):
        return self.call('set_time_interval_start_channel', kwargs=kwargs)

    def get_time_interval_stop_channel(self, **kwargs):
        return self.call('get_time_interval_stop_channel', kwargs=kwargs)

    def set_time_interval_stop_channel(self, **kwargs):
        return self.call('set_time_interval_stop_channel', kwargs=kwargs)

    def get_time_interval_estimate(self, **kwargs):
        return self.call('get_time_interval_estimate', kwargs=kwargs)

    def set_time_interval_estimate(self, **kwargs):
        return self.call('set_time_interval_estimate', kwargs=kwargs)

    def get_time_interval_resolution(self, **kwargs):
        return self.call('get_time_interval_resolution', kwargs=kwargs)

    def set_time_interval_resolution(self, **kwargs):
        return self.call('set_time_interval_resolution', kwargs=kwargs)

    def get_phase_input_channel(self, **kwargs):
        return self.call('get_phase_input_channel', kwargs=kwargs)

    def set_phase_input_channel(self, **kwargs):
        return self.call('set_phase_input_channel', kwargs=kwargs)

    def get_phase_reference_channel(self, **kwargs):
        return self.call('get_phase_reference_channel', kwargs=kwargs)

    def set_phase_reference_channel(self, **kwargs):
        return self.call('set_phase_reference_channel', kwargs=kwargs)

    def get_phase_frequency_estimate(self, **kwargs):
        return self.call('get_phase_frequency_estimate', kwargs=kwargs)

    def set_phase_frequency_estimate(self, **kwargs):
        return self.call('set_phase_frequency_estimate', kwargs=kwargs)

    def get_phase_resolution(self, **kwargs):
        return self.call('get_phase_resolution', kwargs=kwargs)

    def set_phase_resolution(self, **kwargs):
        return self.call('set_phase_resolution', kwargs=kwargs)

    def get_totalize_continuous_channel(self, **kwargs):
        return self.call('get_totalize_continuous_channel', kwargs=kwargs)

    def set_totalize_continuous_channel(self, **kwargs):
        return self.call('set_totalize_continuous_channel', kwargs=kwargs)

    def get_totalize_gated_channel(self, **kwargs):
        return self.call('get_totalize_gated_channel', kwargs=kwargs)

    def set_totalize_gated_channel(self, **kwargs):
        return self.call('set_totalize_gated_channel', kwargs=kwargs)

    def get_totalize_gated_gate_source(self, **kwargs):
        return self.call('get_totalize_gated_gate_source', kwargs=kwargs)

    def set_totalize_gated_gate_source(self, **kwargs):
        return self.call('set_totalize_gated_gate_source', kwargs=kwargs)

    def get_totalize_gated_gate_slope(self, **kwargs):
        return self.call('get_totalize_gated_gate_slope', kwargs=kwargs)

    def set_totalize_gated_gate_slope(self, **kwargs):
        return self.call('set_totalize_gated_gate_slope', kwargs=kwargs)

    def get_totalize_timed_channel(self, **kwargs):
        return self.call('get_totalize_timed_channel', kwargs=kwargs)

    def set_totalize_timed_channel(self, **kwargs):
        return self.call('set_totalize_timed_channel', kwargs=kwargs)

    def get_totalize_timed_gate_time(self, **kwargs):
        return self.call('get_totalize_timed_gate_time', kwargs=kwargs)

    def set_totalize_timed_gate_time(self, **kwargs):
        return self.call('set_totalize_timed_gate_time', kwargs=kwargs)

    def get_arm_start_type(self, **kwargs):
        return self.call('get_arm_start_type', kwargs=kwargs)

    def set_arm_start_type(self, **kwargs):
        return self.call('set_arm_start_type', kwargs=kwargs)

    def get_arm_start_external_source(self, **kwargs):
        return self.call('get_arm_start_external_source', kwargs=kwargs)

    def set_arm_start_external_source(self, **kwargs):
        return self.call('set_arm_start_external_source', kwargs=kwargs)

    def get_arm_start_external_level(self, **kwargs):
        return self.call('get_arm_start_external_level', kwargs=kwargs)

    def set_arm_start_external_level(self, **kwargs):
        return self.call('set_arm_start_external_level', kwargs=kwargs)

    def get_arm_start_external_slope(self, **kwargs):
        return self.call('get_arm_start_external_slope', kwargs=kwargs)

    def set_arm_start_external_slope(self, **kwargs):
        return self.call('set_arm_start_external_slope', kwargs=kwargs)

    def get_arm_start_external_delay(self, **kwargs):
        return self.call('get_arm_start_external_delay', kwargs=kwargs)

    def set_arm_start_external_delay(self, **kwargs):
        return self.call('set_arm_start_external_delay', kwargs=kwargs)

    def get_arm_stop_type(self, **kwargs):
        return self.call('get_arm_stop_type', kwargs=kwargs)

    def set_arm_stop_type(self, **kwargs):
        return self.call('set_arm_stop_type', kwargs=kwargs)

    def get_arm_stop_external_source(self, **kwargs):
        return self.call('get_arm_stop_external_source', kwargs=kwargs)

    def set_arm_stop_external_source(self, **kwargs):
        return self.call('set_arm_stop_external_source', kwargs=kwargs)

    def get_arm_stop_external_level(self, **kwargs):
        return self.call('get_arm_stop_external_level', kwargs=kwargs)

    def set_arm_stop_external_level(self, **kwargs):
        return self.call('set_arm_stop_external_level', kwargs=kwargs)

    def get_arm_stop_external_slope(self, **kwargs):
        return self.call('get_arm_stop_external_slope', kwargs=kwargs)

    def set_arm_stop_external_slope(self, **kwargs):
        return self.call('set_arm_stop_external_slope', kwargs=kwargs)

    def get_arm_stop_external_delay(self, **kwargs):
        return self.call('get_arm_stop_external_delay', kwargs=kwargs)

    def set_arm_stop_external_delay(self, **kwargs):
        return self.call('set_arm_stop_external_delay', kwargs=kwargs)

    def measurement_abort(self, **kwargs):
        return self.call('measurement_abort', kwargs=kwargs)

    def measurement_is_measurement_complete(self, **kwargs):
        return self.call('measurement_is_measurement_complete', kwargs=kwargs)

    def channels_configure(self, **kwargs):
        return self.call('channels_configure', kwargs=kwargs)

    def channels_configure_level(self, **kwargs):
        return self.call('channels_configure_level', kwargs=kwargs)

    def frequency_configure(self, **kwargs):
        return self.call('frequency_configure', kwargs=kwargs)

    def frequency_configure_manual(self, **kwargs):
        return self.call('frequency_configure_manual', kwargs=kwargs)

    def frequency_configure_with_aperture(self, **kwargs):
        return self.call('frequency_configure_with_aperture', kwargs=kwargs)

    def period_configure(self, **kwargs):
        return self.call('period_configure', kwargs=kwargs)

    def period_configure_with_aperture(self, **kwargs):
        return self.call('period_configure_with_aperture', kwargs=kwargs)

    def pulse_width_configure(self, **kwargs):
        return self.call('pulse_width_configure', kwargs=kwargs)

    def duty_cycle_configure(self, **kwargs):
        return self.call('duty_cycle_configure', kwargs=kwargs)

    def edge_time_configure(self, **kwargs):
        return self.call('edge_time_configure', kwargs=kwargs)

    def frequency_ratio_configure(self, **kwargs):
        return self.call('frequency_ratio_configure', kwargs=kwargs)

    def time_interval_configure(self, **kwargs):
        return self.call('time_interval_configure', kwargs=kwargs)

    def phase_configure(self, **kwargs):
        return self.call('phase_configure', kwargs=kwargs)

    def totalize_continuous_configure(self, **kwargs):
        return self.call('totalize_continuous_configure', kwargs=kwargs)

    def totalize_continuous_start(self, **kwargs):
        return self.call('totalize_continuous_start', kwargs=kwargs)

    def totalize_continuous_stop(self, **kwargs):
        return self.call('totalize_continuous_stop', kwargs=kwargs)

    def totalize_continuous_fetch_count(self, **kwargs):
        return self.call('totalize_continuous_fetch_count', kwargs=kwargs)

    def totalize_gated_configure(self, **kwargs):
        return self.call('totalize_gated_configure', kwargs=kwargs)

    def totalize_timed_configure(self, **kwargs):
        return self.call('totalize_timed_configure', kwargs=kwargs)

    def arm_start_external_configure(self, **kwargs):
        return self.call('arm_start_external_configure', kwargs=kwargs)

    def arm_stop_external_configure(self, **kwargs):
        return self.call('arm_stop_external_configure', kwargs=kwargs)

    def measurement_fetch(self, **kwargs):
        return self.call('measurement_fetch', kwargs=kwargs)

    def measurement_initiate(self, **kwargs):
        return self.call('measurement_initiate', kwargs=kwargs)

    def measurement_read(self, **kwargs):
        return self.call('measurement_read', kwargs=kwargs)

    def get_trigger_tv_trigger_event(self, **kwargs):
        return self.call('get_trigger_tv_trigger_event', kwargs=kwargs)

    def set_trigger_tv_trigger_event(self, **kwargs):
        return self.call('set_trigger_tv_trigger_event', kwargs=kwargs)

    def get_trigger_tv_line_number(self, **kwargs):
        return self.call('get_trigger_tv_line_number', kwargs=kwargs)

    def set_trigger_tv_line_number(self, **kwargs):
        return self.call('set_trigger_tv_line_number', kwargs=kwargs)

    def get_trigger_tv_polarity(self, **kwargs):
        return self.call('get_trigger_tv_polarity', kwargs=kwargs)

    def set_trigger_tv_polarity(self, **kwargs):
        return self.call('set_trigger_tv_polarity', kwargs=kwargs)

    def get_trigger_tv_signal_format(self, **kwargs):
        return self.call('get_trigger_tv_signal_format', kwargs=kwargs)

    def set_trigger_tv_signal_format(self, **kwargs):
        return self.call('set_trigger_tv_signal_format', kwargs=kwargs)

    def trigger_tv_configure(self, **kwargs):
        return self.call('trigger_tv_configure', kwargs=kwargs)

    def get_trigger_glitch_condition(self, **kwargs):
        return self.call('get_trigger_glitch_condition', kwargs=kwargs)

    def set_trigger_glitch_condition(self, **kwargs):
        return self.call('set_trigger_glitch_condition', kwargs=kwargs)

    def get_trigger_glitch_polarity(self, **kwargs):
        return self.call('get_trigger_glitch_polarity', kwargs=kwargs)

    def set_trigger_glitch_polarity(self, **kwargs):
        return self.call('set_trigger_glitch_polarity', kwargs=kwargs)

    def get_trigger_glitch_width(self, **kwargs):
        return self.call('get_trigger_glitch_width', kwargs=kwargs)

    def set_trigger_glitch_width(self, **kwargs):
        return self.call('set_trigger_glitch_width', kwargs=kwargs)

    def trigger_glitch_configure(self, **kwargs):
        return self.call('trigger_glitch_configure', kwargs=kwargs)

    def get_trigger_width_condition(self, **kwargs):
        return self.call('get_trigger_width_condition', kwargs=kwargs)

    def set_trigger_width_condition(self, **kwargs):
        return self.call('set_trigger_width_condition', kwargs=kwargs)

    def get_trigger_width_threshold_high(self, **kwargs):
        return self.call('get_trigger_width_threshold_high', kwargs=kwargs)

    def set_trigger_width_threshold_high(self, **kwargs):
        return self.call('set_trigger_width_threshold_high', kwargs=kwargs)

    def get_trigger_width_threshold_low(self, **kwargs):
        return self.call('get_trigger_width_threshold_low', kwargs=kwargs)

    def set_trigger_width_threshold_low(self, **kwargs):
        return self.call('set_trigger_width_threshold_low', kwargs=kwargs)

    def get_trigger_width_polarity(self, **kwargs):
        return self.call('get_trigger_width_polarity', kwargs=kwargs)

    def set_trigger_width_polarity(self, **kwargs):
        return self.call('set_trigger_width_polarity', kwargs=kwargs)

    def trigger_width_configure(self, **kwargs):
        return self.call('trigger_width_configure', kwargs=kwargs)

    def get_trigger_ac_line_slope(self, **kwargs):
        return self.call('get_trigger_ac_line_slope', kwargs=kwargs)

    def set_trigger_ac_line_slope(self, **kwargs):
        return self.call('set_trigger_ac_line_slope', kwargs=kwargs)

    def get_reference_level_high(self, **kwargs):
        return self.call('get_reference_level_high', kwargs=kwargs)

    def set_reference_level_high(self, **kwargs):
        return self.call('set_reference_level_high', kwargs=kwargs)

    def get_reference_level_middle(self, **kwargs):
        return self.call('get_reference_level_middle', kwargs=kwargs)

    def set_reference_level_middle(self, **kwargs):
        return self.call('set_reference_level_middle', kwargs=kwargs)

    def get_reference_level_low(self, **kwargs):
        return self.call('get_reference_level_low', kwargs=kwargs)

    def set_reference_level_low(self, **kwargs):
        return self.call('set_reference_level_low', kwargs=kwargs)

    def reference_level_configure(self, **kwargs):
        return self.call('reference_level_configure', kwargs=kwargs)

    def channels_measurement_fetch_waveform_measurement(self, **kwargs):
        return self.call('channels_measurement_fetch_waveform_measurement', kwargs=kwargs)

    def channels_measurement_read_waveform_measurement(self, **kwargs):
        return self.call('channels_measurement_read_waveform_measurement', kwargs=kwargs)

    def get_acquisition_number_of_envelopes(self, **kwargs):
        return self.call('get_acquisition_number_of_envelopes', kwargs=kwargs)

    def set_acquisition_number_of_envelopes(self, **kwargs):
        return self.call('set_acquisition_number_of_envelopes', kwargs=kwargs)

    def channels_measurement_fetch_waveform_min_max(self, **kwargs):
        return self.call('channels_measurement_fetch_waveform_min_max', kwargs=kwargs)

    def channels_measurement_read_waveform_min_max(self, **kwargs):
        return self.call('channels_measurement_read_waveform_min_max', kwargs=kwargs)

    def get_trigger_continuous(self, **kwargs):
        return self.call('get_trigger_continuous', kwargs=kwargs)

    def set_trigger_continuous(self, **kwargs):
        return self.call('set_trigger_continuous', kwargs=kwargs)

    def get_acquisition_number_of_averages(self, **kwargs):
        return self.call('get_acquisition_number_of_averages', kwargs=kwargs)

    def set_acquisition_number_of_averages(self, **kwargs):
        return self.call('set_acquisition_number_of_averages', kwargs=kwargs)

    def get_acquisition_sample_mode(self, **kwargs):
        return self.call('get_acquisition_sample_mode', kwargs=kwargs)

    def set_acquisition_sample_mode(self, **kwargs):
        return self.call('set_acquisition_sample_mode', kwargs=kwargs)

    def get_trigger_modifier(self, **kwargs):
        return self.call('get_trigger_modifier', kwargs=kwargs)

    def set_trigger_modifier(self, **kwargs):
        return self.call('set_trigger_modifier', kwargs=kwargs)

    def measurement_auto_setup(self, **kwargs):
        return self.call('measurement_auto_setup', kwargs=kwargs)

    def system_fetch_setup(self, **kwargs):
        return self.call('system_fetch_setup', kwargs=kwargs)

    def system_load_setup(self, **kwargs):
        return self.call('system_load_setup', kwargs=kwargs)

    def display_fetch_screenshot(self, **kwargs):
        return self.call('display_fetch_screenshot', kwargs=kwargs)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def get_initialized(self, **kwargs):
        return self.call('get_initialized', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def get_driver_operation_cache(self, **kwargs):
        return self.call('get_driver_operation_cache', kwargs=kwargs)

    def set_driver_operation_cache(self, **kwargs):
        return self.call('set_driver_operation_cache', kwargs=kwargs)

    def get_driver_operation_driver_setup(self, **kwargs):
        return self.call('get_driver_operation_driver_setup', kwargs=kwargs)

    def get_driver_operation_interchange_check(self, **kwargs):
        return self.call('get_driver_operation_interchange_check', kwargs=kwargs)

    def set_driver_operation_interchange_check(self, **kwargs):
        return self.call('set_driver_operation_interchange_check', kwargs=kwargs)

    def get_driver_operation_logical_name(self, **kwargs):
        return self.call('get_driver_operation_logical_name', kwargs=kwargs)

    def get_driver_operation_query_instrument_status(self, **kwargs):
        return self.call('get_driver_operation_query_instrument_status', kwargs=kwargs)

    def set_driver_operation_query_instrument_status(self, **kwargs):
        return self.call('set_driver_operation_query_instrument_status', kwargs=kwargs)

    def get_driver_operation_range_check(self, **kwargs):
        return self.call('get_driver_operation_range_check', kwargs=kwargs)

    def set_driver_operation_range_check(self, **kwargs):
        return self.call('set_driver_operation_range_check', kwargs=kwargs)

    def get_driver_operation_record_coercions(self, **kwargs):
        return self.call('get_driver_operation_record_coercions', kwargs=kwargs)

    def set_driver_operation_record_coercions(self, **kwargs):
        return self.call('set_driver_operation_record_coercions', kwargs=kwargs)

    def get_driver_operation_io_resource_descriptor(self, **kwargs):
        return self.call('get_driver_operation_io_resource_descriptor', kwargs=kwargs)

    def get_driver_operation_simulate(self, **kwargs):
        return self.call('get_driver_operation_simulate', kwargs=kwargs)

    def driver_operation_clear_interchange_warnings(self, **kwargs):
        return self.call('driver_operation_clear_interchange_warnings', kwargs=kwargs)

    def driver_operation_get_next_coercion_record(self, **kwargs):
        return self.call('driver_operation_get_next_coercion_record', kwargs=kwargs)

    def driver_operation_get_next_interchange_warning(self, **kwargs):
        return self.call('driver_operation_get_next_interchange_warning', kwargs=kwargs)

    def driver_operation_invalidate_all_attributes(self, **kwargs):
        return self.call('driver_operation_invalidate_all_attributes', kwargs=kwargs)

    def driver_operation_reset_interchange_check(self, **kwargs):
        return self.call('driver_operation_reset_interchange_check', kwargs=kwargs)

    def get_identity_description(self, **kwargs):
        return self.call('get_identity_description', kwargs=kwargs)

    def get_identity_identifier(self, **kwargs):
        return self.call('get_identity_identifier', kwargs=kwargs)

    def get_identity_revision(self, **kwargs):
        return self.call('get_identity_revision', kwargs=kwargs)

    def get_identity_vendor(self, **kwargs):
        return self.call('get_identity_vendor', kwargs=kwargs)

    def get_identity_instrument_manufacturer(self, **kwargs):
        return self.call('get_identity_instrument_manufacturer', kwargs=kwargs)

    def get_identity_instrument_model(self, **kwargs):
        return self.call('get_identity_instrument_model', kwargs=kwargs)

    def get_identity_instrument_firmware_revision(self, **kwargs):
        return self.call('get_identity_instrument_firmware_revision', kwargs=kwargs)

    def get_identity_specification_major_version(self, **kwargs):
        return self.call('get_identity_specification_major_version', kwargs=kwargs)

    def get_identity_specification_minor_version(self, **kwargs):
        return self.call('get_identity_specification_minor_version', kwargs=kwargs)

    def get_identity_supported_instrument_models(self, **kwargs):
        return self.call('get_identity_supported_instrument_models', kwargs=kwargs)

    def get_identity_group_capabilities(self, **kwargs):
        return self.call('get_identity_group_capabilities', kwargs=kwargs)

    def identity_get_group_capabilities(self, **kwargs):
        return self.call('identity_get_group_capabilities', kwargs=kwargs)

    def identity_get_supported_instrument_models(self, **kwargs):
        return self.call('identity_get_supported_instrument_models', kwargs=kwargs)

    def utility_disable(self, **kwargs):
        return self.call('utility_disable', kwargs=kwargs)

    def utility_error_query(self, **kwargs):
        return self.call('utility_error_query', kwargs=kwargs)

    def utility_lock_object(self, **kwargs):
        return self.call('utility_lock_object', kwargs=kwargs)

    def utility_reset(self, **kwargs):
        return self.call('utility_reset', kwargs=kwargs)

    def utility_reset_with_defaults(self, **kwargs):
        return self.call('utility_reset_with_defaults', kwargs=kwargs)

    def utility_self_test(self, **kwargs):
        return self.call('utility_self_test', kwargs=kwargs)

    def utility_unlock_object(self, **kwargs):
        return self.call('utility_unlock_object', kwargs=kwargs)

