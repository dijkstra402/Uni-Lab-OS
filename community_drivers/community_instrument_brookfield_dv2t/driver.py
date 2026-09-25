from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBrookfieldDv2t(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/pymeasure__pymeasure', 'source_file': 'tests/instruments/hp/test_hp856Xx.py', 'class_name': 'TestHP856Xx', 'import_roots': [], 'candidate_methods': ['test_id', 'test_attenuation', 'test_attenuation_string_parameters', 'test_attenuation_truncation', 'test_amplitude_units', 'test_primitive_commands', 'test_blank_trace', 'test_blank_trace_exceptions', 'test_frequencies', 'test_clear_write_trace', 'test_clear_write_trace_exceptions', 'test_coupling', 'test_demodulation_mode', 'test_demodulation_agc_enabled', 'test_demodulation_time', 'test_detector_mode', 'test_display_line_enabled', 'test_check_done', 'test_errors', 'test_empty_errors', 'test_elapsed_time', 'test_fdiag_frequencies', 'test_sampler_harmonic_number', 'test_frequency_display_enabled', 'test_fft', 'test_fft_exceptions', 'test_frequency_reference_source', 'test_on_off_commands', 'test_adjust_if', 'test_logarithmic_scale', 'test_hold', 'test_hold_exceptions', 'test_marker_amplitude', 'test_marker_delta', 'test_marker_frequency', 'test_frequency_counter_mode_enabled', 'test_frequency_counter_resolution', 'test_deactivate_marker', 'test_minimum_hold', 'test_marker_threshold', 'test_peak_excursion', 'test_marker_time', 'test_mixer_level', 'test_normalized_reference_level', 'test_normalized_reference_position', 'test_display_parameters', 'test_plot', 'test_power_bandwidth', 'test_resolution_bandwidth', 'test_resolution_bandwidth_to_span_ratio', 'test_recall_state', 'test_recall_trace', 'test_firmware_revision', 'test_reference_level', 'test_reference_level_calibration', 'test_request_service_conditions', 'test_save_state', 'test_save_trace', 'test_span_string_params', 'test_squelch', 'test_service_request', 'test_sweep_time', 'test_sweep_couple', 'test_sweep_output', 'test_trace_data_format', 'test_threshold', 'test_threshold_enabled', 'test_title', 'test_trigger_mode', 'test_trace_data', 'test_fft_trace_window', 'test_video_average_enabled', 'test_video_bandwidth', 'test_video_bandwidth_string_parameters', 'test_video_bandwidth_to_resolution_bandwidth', 'test_view_trace', 'test_video_trigger_level'], 'action_targets': {}, 'metadata': {'repo': 'pymeasure/pymeasure', 'repo_url': 'https://github.com/pymeasure/pymeasure', 'brand': 'Brookfield', 'model': 'DV2T', 'device_type_cn': '旋转黏度计', 'device_type_en': 'Rotational Viscometer', 'source_framework': 'PyMeasure', 'tag_id': '4398', 'tag_name': '旋转黏度计', 'tag_name_en': 'Rotational Viscometer', 'candidate_score': 646, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def test_id(self, **kwargs):
        return self.call('test_id', kwargs=kwargs)

    def test_attenuation(self, **kwargs):
        return self.call('test_attenuation', kwargs=kwargs)

    def test_attenuation_string_parameters(self, **kwargs):
        return self.call('test_attenuation_string_parameters', kwargs=kwargs)

    def test_attenuation_truncation(self, **kwargs):
        return self.call('test_attenuation_truncation', kwargs=kwargs)

    def test_amplitude_units(self, **kwargs):
        return self.call('test_amplitude_units', kwargs=kwargs)

    def test_primitive_commands(self, **kwargs):
        return self.call('test_primitive_commands', kwargs=kwargs)

    def test_blank_trace(self, **kwargs):
        return self.call('test_blank_trace', kwargs=kwargs)

    def test_blank_trace_exceptions(self, **kwargs):
        return self.call('test_blank_trace_exceptions', kwargs=kwargs)

    def test_frequencies(self, **kwargs):
        return self.call('test_frequencies', kwargs=kwargs)

    def test_clear_write_trace(self, **kwargs):
        return self.call('test_clear_write_trace', kwargs=kwargs)

    def test_clear_write_trace_exceptions(self, **kwargs):
        return self.call('test_clear_write_trace_exceptions', kwargs=kwargs)

    def test_coupling(self, **kwargs):
        return self.call('test_coupling', kwargs=kwargs)

    def test_demodulation_mode(self, **kwargs):
        return self.call('test_demodulation_mode', kwargs=kwargs)

    def test_demodulation_agc_enabled(self, **kwargs):
        return self.call('test_demodulation_agc_enabled', kwargs=kwargs)

    def test_demodulation_time(self, **kwargs):
        return self.call('test_demodulation_time', kwargs=kwargs)

    def test_detector_mode(self, **kwargs):
        return self.call('test_detector_mode', kwargs=kwargs)

    def test_display_line_enabled(self, **kwargs):
        return self.call('test_display_line_enabled', kwargs=kwargs)

    def test_check_done(self, **kwargs):
        return self.call('test_check_done', kwargs=kwargs)

    def test_errors(self, **kwargs):
        return self.call('test_errors', kwargs=kwargs)

    def test_empty_errors(self, **kwargs):
        return self.call('test_empty_errors', kwargs=kwargs)

    def test_elapsed_time(self, **kwargs):
        return self.call('test_elapsed_time', kwargs=kwargs)

    def test_fdiag_frequencies(self, **kwargs):
        return self.call('test_fdiag_frequencies', kwargs=kwargs)

    def test_sampler_harmonic_number(self, **kwargs):
        return self.call('test_sampler_harmonic_number', kwargs=kwargs)

    def test_frequency_display_enabled(self, **kwargs):
        return self.call('test_frequency_display_enabled', kwargs=kwargs)

    def test_fft(self, **kwargs):
        return self.call('test_fft', kwargs=kwargs)

    def test_fft_exceptions(self, **kwargs):
        return self.call('test_fft_exceptions', kwargs=kwargs)

    def test_frequency_reference_source(self, **kwargs):
        return self.call('test_frequency_reference_source', kwargs=kwargs)

    def test_on_off_commands(self, **kwargs):
        return self.call('test_on_off_commands', kwargs=kwargs)

    def test_adjust_if(self, **kwargs):
        return self.call('test_adjust_if', kwargs=kwargs)

    def test_logarithmic_scale(self, **kwargs):
        return self.call('test_logarithmic_scale', kwargs=kwargs)

    def test_hold(self, **kwargs):
        return self.call('test_hold', kwargs=kwargs)

    def test_hold_exceptions(self, **kwargs):
        return self.call('test_hold_exceptions', kwargs=kwargs)

    def test_marker_amplitude(self, **kwargs):
        return self.call('test_marker_amplitude', kwargs=kwargs)

    def test_marker_delta(self, **kwargs):
        return self.call('test_marker_delta', kwargs=kwargs)

    def test_marker_frequency(self, **kwargs):
        return self.call('test_marker_frequency', kwargs=kwargs)

    def test_frequency_counter_mode_enabled(self, **kwargs):
        return self.call('test_frequency_counter_mode_enabled', kwargs=kwargs)

    def test_frequency_counter_resolution(self, **kwargs):
        return self.call('test_frequency_counter_resolution', kwargs=kwargs)

    def test_deactivate_marker(self, **kwargs):
        return self.call('test_deactivate_marker', kwargs=kwargs)

    def test_minimum_hold(self, **kwargs):
        return self.call('test_minimum_hold', kwargs=kwargs)

    def test_marker_threshold(self, **kwargs):
        return self.call('test_marker_threshold', kwargs=kwargs)

    def test_peak_excursion(self, **kwargs):
        return self.call('test_peak_excursion', kwargs=kwargs)

    def test_marker_time(self, **kwargs):
        return self.call('test_marker_time', kwargs=kwargs)

    def test_mixer_level(self, **kwargs):
        return self.call('test_mixer_level', kwargs=kwargs)

    def test_normalized_reference_level(self, **kwargs):
        return self.call('test_normalized_reference_level', kwargs=kwargs)

    def test_normalized_reference_position(self, **kwargs):
        return self.call('test_normalized_reference_position', kwargs=kwargs)

    def test_display_parameters(self, **kwargs):
        return self.call('test_display_parameters', kwargs=kwargs)

    def test_plot(self, **kwargs):
        return self.call('test_plot', kwargs=kwargs)

    def test_power_bandwidth(self, **kwargs):
        return self.call('test_power_bandwidth', kwargs=kwargs)

    def test_resolution_bandwidth(self, **kwargs):
        return self.call('test_resolution_bandwidth', kwargs=kwargs)

    def test_resolution_bandwidth_to_span_ratio(self, **kwargs):
        return self.call('test_resolution_bandwidth_to_span_ratio', kwargs=kwargs)

    def test_recall_state(self, **kwargs):
        return self.call('test_recall_state', kwargs=kwargs)

    def test_recall_trace(self, **kwargs):
        return self.call('test_recall_trace', kwargs=kwargs)

    def test_firmware_revision(self, **kwargs):
        return self.call('test_firmware_revision', kwargs=kwargs)

    def test_reference_level(self, **kwargs):
        return self.call('test_reference_level', kwargs=kwargs)

    def test_reference_level_calibration(self, **kwargs):
        return self.call('test_reference_level_calibration', kwargs=kwargs)

    def test_request_service_conditions(self, **kwargs):
        return self.call('test_request_service_conditions', kwargs=kwargs)

    def test_save_state(self, **kwargs):
        return self.call('test_save_state', kwargs=kwargs)

    def test_save_trace(self, **kwargs):
        return self.call('test_save_trace', kwargs=kwargs)

    def test_span_string_params(self, **kwargs):
        return self.call('test_span_string_params', kwargs=kwargs)

    def test_squelch(self, **kwargs):
        return self.call('test_squelch', kwargs=kwargs)

    def test_service_request(self, **kwargs):
        return self.call('test_service_request', kwargs=kwargs)

    def test_sweep_time(self, **kwargs):
        return self.call('test_sweep_time', kwargs=kwargs)

    def test_sweep_couple(self, **kwargs):
        return self.call('test_sweep_couple', kwargs=kwargs)

    def test_sweep_output(self, **kwargs):
        return self.call('test_sweep_output', kwargs=kwargs)

    def test_trace_data_format(self, **kwargs):
        return self.call('test_trace_data_format', kwargs=kwargs)

    def test_threshold(self, **kwargs):
        return self.call('test_threshold', kwargs=kwargs)

    def test_threshold_enabled(self, **kwargs):
        return self.call('test_threshold_enabled', kwargs=kwargs)

    def test_title(self, **kwargs):
        return self.call('test_title', kwargs=kwargs)

    def test_trigger_mode(self, **kwargs):
        return self.call('test_trigger_mode', kwargs=kwargs)

    def test_trace_data(self, **kwargs):
        return self.call('test_trace_data', kwargs=kwargs)

    def test_fft_trace_window(self, **kwargs):
        return self.call('test_fft_trace_window', kwargs=kwargs)

    def test_video_average_enabled(self, **kwargs):
        return self.call('test_video_average_enabled', kwargs=kwargs)

    def test_video_bandwidth(self, **kwargs):
        return self.call('test_video_bandwidth', kwargs=kwargs)

    def test_video_bandwidth_string_parameters(self, **kwargs):
        return self.call('test_video_bandwidth_string_parameters', kwargs=kwargs)

    def test_video_bandwidth_to_resolution_bandwidth(self, **kwargs):
        return self.call('test_video_bandwidth_to_resolution_bandwidth', kwargs=kwargs)

    def test_view_trace(self, **kwargs):
        return self.call('test_view_trace', kwargs=kwargs)

    def test_video_trigger_level(self, **kwargs):
        return self.call('test_video_trigger_level', kwargs=kwargs)

