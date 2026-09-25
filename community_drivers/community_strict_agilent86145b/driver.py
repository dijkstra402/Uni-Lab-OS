from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAgilent86145b(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/python-ivi__python-ivi', 'source_file': 'ivi/agilent/agilent86145B.py', 'class_name': 'agilent86145B', 'import_roots': [], 'candidate_methods': ['get_level_amplitude_units', 'set_level_amplitude_units', 'get_acquisition_detector_type', 'set_acquisition_detector_type', 'get_acquisition_detector_type_auto', 'set_acquisition_detector_type_auto', 'get_wavelength_start', 'set_wavelength_start', 'get_wavelength_stop', 'set_wavelength_stop', 'get_wavelength_offset', 'set_wavelength_offset', 'get_acquisition_number_of_sweeps', 'set_acquisition_number_of_sweeps', 'get_level_reference', 'set_level_reference', 'get_level_reference_offset', 'set_level_reference_offset', 'get_sweep_coupling_resolution_bandwidth', 'set_sweep_coupling_resolution_bandwidth', 'get_sweep_coupling_resolution_bandwidth_auto', 'set_sweep_coupling_resolution_bandwidth_auto', 'get_acquisition_sweep_mode_continuous', 'set_acquisition_sweep_mode_continuous', 'get_sweep_coupling_sweep_time', 'set_sweep_coupling_sweep_time', 'get_sweep_coupling_sweep_time_auto', 'set_sweep_coupling_sweep_time_auto', 'get_traces_name', 'get_traces_type', 'set_traces_type', 'get_acquisition_vertical_scale', 'set_acquisition_vertical_scale', 'get_sweep_coupling_video_bandwidth', 'set_sweep_coupling_video_bandwidth', 'get_sweep_coupling_video_bandwidth_auto', 'set_sweep_coupling_video_bandwidth_auto', 'acquisition_abort', 'acquisition_status', 'acquisition_configure', 'wavelength_configure_center_span', 'wavelength_configure_start_stop', 'level_configure', 'sweep_coupling_configure', 'traces_fetch_y', 'acquisition_initiate', 'traces_read_y', 'initialize', 'get_initialized', 'close', 'get_driver_operation_cache', 'set_driver_operation_cache', 'get_driver_operation_driver_setup', 'get_driver_operation_interchange_check', 'set_driver_operation_interchange_check', 'get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status', 'get_driver_operation_range_check', 'set_driver_operation_range_check', 'get_driver_operation_record_coercions', 'set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check', 'get_identity_description', 'get_identity_identifier', 'get_identity_revision', 'get_identity_vendor', 'get_identity_instrument_manufacturer', 'get_identity_instrument_model', 'get_identity_instrument_firmware_revision', 'get_identity_specification_major_version', 'get_identity_specification_minor_version', 'get_identity_supported_instrument_models', 'get_identity_group_capabilities', 'identity_get_group_capabilities', 'identity_get_supported_instrument_models', 'utility_disable', 'utility_error_query', 'utility_lock_object', 'utility_reset', 'utility_reset_with_defaults', 'utility_self_test', 'utility_unlock_object', 'display_fetch_screenshot', 'memory_save', 'memory_recall'], 'action_targets': {'get_level_amplitude_units': '_get_level_amplitude_units', 'set_level_amplitude_units': '_set_level_amplitude_units', 'get_acquisition_detector_type': '_get_acquisition_detector_type', 'set_acquisition_detector_type': '_set_acquisition_detector_type', 'get_acquisition_detector_type_auto': '_get_acquisition_detector_type_auto', 'set_acquisition_detector_type_auto': '_set_acquisition_detector_type_auto', 'get_wavelength_start': '_get_wavelength_start', 'set_wavelength_start': '_set_wavelength_start', 'get_wavelength_stop': '_get_wavelength_stop', 'set_wavelength_stop': '_set_wavelength_stop', 'get_wavelength_offset': '_get_wavelength_offset', 'set_wavelength_offset': '_set_wavelength_offset', 'get_acquisition_number_of_sweeps': '_get_acquisition_number_of_sweeps', 'set_acquisition_number_of_sweeps': '_set_acquisition_number_of_sweeps', 'get_level_reference': '_get_level_reference', 'set_level_reference': '_set_level_reference', 'get_level_reference_offset': '_get_level_reference_offset', 'set_level_reference_offset': '_set_level_reference_offset', 'get_sweep_coupling_resolution_bandwidth': '_get_sweep_coupling_resolution_bandwidth', 'set_sweep_coupling_resolution_bandwidth': '_set_sweep_coupling_resolution_bandwidth', 'get_sweep_coupling_resolution_bandwidth_auto': '_get_sweep_coupling_resolution_bandwidth_auto', 'set_sweep_coupling_resolution_bandwidth_auto': '_set_sweep_coupling_resolution_bandwidth_auto', 'get_acquisition_sweep_mode_continuous': '_get_acquisition_sweep_mode_continuous', 'set_acquisition_sweep_mode_continuous': '_set_acquisition_sweep_mode_continuous', 'get_sweep_coupling_sweep_time': '_get_sweep_coupling_sweep_time', 'set_sweep_coupling_sweep_time': '_set_sweep_coupling_sweep_time', 'get_sweep_coupling_sweep_time_auto': '_get_sweep_coupling_sweep_time_auto', 'set_sweep_coupling_sweep_time_auto': '_set_sweep_coupling_sweep_time_auto', 'get_traces_name': '_get_trace_name', 'get_traces_type': '_get_trace_type', 'set_traces_type': '_set_trace_type', 'get_acquisition_vertical_scale': '_get_acquisition_vertical_scale', 'set_acquisition_vertical_scale': '_set_acquisition_vertical_scale', 'get_sweep_coupling_video_bandwidth': '_get_sweep_coupling_video_bandwidth', 'set_sweep_coupling_video_bandwidth': '_set_sweep_coupling_video_bandwidth', 'get_sweep_coupling_video_bandwidth_auto': '_get_sweep_coupling_video_bandwidth_auto', 'set_sweep_coupling_video_bandwidth_auto': '_set_sweep_coupling_video_bandwidth_auto', 'acquisition_abort': '_acquisition_abort', 'acquisition_status': '_acquisition_status', 'acquisition_configure': '_acquisition_configure', 'wavelength_configure_center_span': '_wavelength_configure_center_span', 'wavelength_configure_start_stop': '_wavelength_configure_start_stop', 'level_configure': '_level_configure', 'sweep_coupling_configure': '_sweep_coupling_configure', 'traces_fetch_y': '_trace_fetch_y', 'acquisition_initiate': '_acquisition_initiate', 'traces_read_y': '_trace_read_y', 'initialize': '_initialize', 'get_initialized': '_get_initialized', 'close': '_close', 'get_driver_operation_cache': '_get_driver_operation_cache', 'set_driver_operation_cache': '_set_driver_operation_cache', 'get_driver_operation_driver_setup': '_get_driver_operation_driver_setup', 'get_driver_operation_interchange_check': '_get_driver_operation_interchange_check', 'set_driver_operation_interchange_check': '_set_driver_operation_interchange_check', 'get_driver_operation_logical_name': '_get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status': '_get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status': '_set_driver_operation_query_instrument_status', 'get_driver_operation_range_check': '_get_driver_operation_range_check', 'set_driver_operation_range_check': '_set_driver_operation_range_check', 'get_driver_operation_record_coercions': '_get_driver_operation_record_coercions', 'set_driver_operation_record_coercions': '_set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor': '_get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate': '_get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings': '_driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record': '_driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning': '_driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes': '_driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check': '_driver_operation_reset_interchange_check', 'get_identity_description': '_get_identity_description', 'get_identity_identifier': '_get_identity_identifier', 'get_identity_revision': '_get_identity_revision', 'get_identity_vendor': '_get_identity_vendor', 'get_identity_instrument_manufacturer': '_get_identity_instrument_manufacturer', 'get_identity_instrument_model': '_get_identity_instrument_model', 'get_identity_instrument_firmware_revision': '_get_identity_instrument_firmware_revision', 'get_identity_specification_major_version': '_get_identity_specification_major_version', 'get_identity_specification_minor_version': '_get_identity_specification_minor_version', 'get_identity_supported_instrument_models': '_get_identity_supported_instrument_models', 'get_identity_group_capabilities': '_get_identity_group_capabilities', 'identity_get_group_capabilities': '_identity_get_group_capabilities', 'identity_get_supported_instrument_models': '_identity_get_supported_instrument_models', 'utility_disable': '_utility_disable', 'utility_error_query': '_utility_error_query', 'utility_lock_object': '_utility_lock_object', 'utility_reset': '_utility_reset', 'utility_reset_with_defaults': '_utility_reset_with_defaults', 'utility_self_test': '_utility_self_test', 'utility_unlock_object': '_utility_unlock_object', 'display_fetch_screenshot': '_display_fetch_screenshot', 'memory_save': '_memory_save', 'memory_recall': '_memory_recall'}, 'metadata': {'repo': 'python-ivi/python-ivi', 'repo_url': 'https://github.com/python-ivi/python-ivi', 'source_url': 'https://github.com/python-ivi/python-ivi/blob/main/ivi/agilent/agilent86145B.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_level_amplitude_units': '_get_level_amplitude_units', 'set_level_amplitude_units': '_set_level_amplitude_units', 'get_acquisition_detector_type': '_get_acquisition_detector_type', 'set_acquisition_detector_type': '_set_acquisition_detector_type', 'get_acquisition_detector_type_auto': '_get_acquisition_detector_type_auto', 'set_acquisition_detector_type_auto': '_set_acquisition_detector_type_auto', 'get_wavelength_start': '_get_wavelength_start', 'set_wavelength_start': '_set_wavelength_start', 'get_wavelength_stop': '_get_wavelength_stop', 'set_wavelength_stop': '_set_wavelength_stop', 'get_wavelength_offset': '_get_wavelength_offset', 'set_wavelength_offset': '_set_wavelength_offset', 'get_acquisition_number_of_sweeps': '_get_acquisition_number_of_sweeps', 'set_acquisition_number_of_sweeps': '_set_acquisition_number_of_sweeps', 'get_level_reference': '_get_level_reference', 'set_level_reference': '_set_level_reference', 'get_level_reference_offset': '_get_level_reference_offset', 'set_level_reference_offset': '_set_level_reference_offset', 'get_sweep_coupling_resolution_bandwidth': '_get_sweep_coupling_resolution_bandwidth', 'set_sweep_coupling_resolution_bandwidth': '_set_sweep_coupling_resolution_bandwidth', 'get_sweep_coupling_resolution_bandwidth_auto': '_get_sweep_coupling_resolution_bandwidth_auto', 'set_sweep_coupling_resolution_bandwidth_auto': '_set_sweep_coupling_resolution_bandwidth_auto', 'get_acquisition_sweep_mode_continuous': '_get_acquisition_sweep_mode_continuous', 'set_acquisition_sweep_mode_continuous': '_set_acquisition_sweep_mode_continuous', 'get_sweep_coupling_sweep_time': '_get_sweep_coupling_sweep_time', 'set_sweep_coupling_sweep_time': '_set_sweep_coupling_sweep_time', 'get_sweep_coupling_sweep_time_auto': '_get_sweep_coupling_sweep_time_auto', 'set_sweep_coupling_sweep_time_auto': '_set_sweep_coupling_sweep_time_auto', 'get_traces_name': '_get_trace_name', 'get_traces_type': '_get_trace_type', 'set_traces_type': '_set_trace_type', 'get_acquisition_vertical_scale': '_get_acquisition_vertical_scale', 'set_acquisition_vertical_scale': '_set_acquisition_vertical_scale', 'get_sweep_coupling_video_bandwidth': '_get_sweep_coupling_video_bandwidth', 'set_sweep_coupling_video_bandwidth': '_set_sweep_coupling_video_bandwidth', 'get_sweep_coupling_video_bandwidth_auto': '_get_sweep_coupling_video_bandwidth_auto', 'set_sweep_coupling_video_bandwidth_auto': '_set_sweep_coupling_video_bandwidth_auto', 'acquisition_abort': '_acquisition_abort', 'acquisition_status': '_acquisition_status', 'acquisition_configure': '_acquisition_configure', 'wavelength_configure_center_span': '_wavelength_configure_center_span', 'wavelength_configure_start_stop': '_wavelength_configure_start_stop', 'level_configure': '_level_configure', 'sweep_coupling_configure': '_sweep_coupling_configure', 'traces_fetch_y': '_trace_fetch_y', 'acquisition_initiate': '_acquisition_initiate', 'traces_read_y': '_trace_read_y', 'initialize': '_initialize', 'get_initialized': '_get_initialized', 'close': '_close', 'get_driver_operation_cache': '_get_driver_operation_cache', 'set_driver_operation_cache': '_set_driver_operation_cache', 'get_driver_operation_driver_setup': '_get_driver_operation_driver_setup', 'get_driver_operation_interchange_check': '_get_driver_operation_interchange_check', 'set_driver_operation_interchange_check': '_set_driver_operation_interchange_check', 'get_driver_operation_logical_name': '_get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status': '_get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status': '_set_driver_operation_query_instrument_status', 'get_driver_operation_range_check': '_get_driver_operation_range_check', 'set_driver_operation_range_check': '_set_driver_operation_range_check', 'get_driver_operation_record_coercions': '_get_driver_operation_record_coercions', 'set_driver_operation_record_coercions': '_set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor': '_get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate': '_get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings': '_driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record': '_driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning': '_driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes': '_driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check': '_driver_operation_reset_interchange_check', 'get_identity_description': '_get_identity_description', 'get_identity_identifier': '_get_identity_identifier', 'get_identity_revision': '_get_identity_revision', 'get_identity_vendor': '_get_identity_vendor', 'get_identity_instrument_manufacturer': '_get_identity_instrument_manufacturer', 'get_identity_instrument_model': '_get_identity_instrument_model', 'get_identity_instrument_firmware_revision': '_get_identity_instrument_firmware_revision', 'get_identity_specification_major_version': '_get_identity_specification_major_version', 'get_identity_specification_minor_version': '_get_identity_specification_minor_version', 'get_identity_supported_instrument_models': '_get_identity_supported_instrument_models', 'get_identity_group_capabilities': '_get_identity_group_capabilities', 'identity_get_group_capabilities': '_identity_get_group_capabilities', 'identity_get_supported_instrument_models': '_identity_get_supported_instrument_models', 'utility_disable': '_utility_disable', 'utility_error_query': '_utility_error_query', 'utility_lock_object': '_utility_lock_object', 'utility_reset': '_utility_reset', 'utility_reset_with_defaults': '_utility_reset_with_defaults', 'utility_self_test': '_utility_self_test', 'utility_unlock_object': '_utility_unlock_object', 'display_fetch_screenshot': '_display_fetch_screenshot', 'memory_save': '_memory_save', 'memory_recall': '_memory_recall'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_level_amplitude_units(self, **kwargs):
        return self.call('get_level_amplitude_units', kwargs=kwargs)

    def set_level_amplitude_units(self, **kwargs):
        return self.call('set_level_amplitude_units', kwargs=kwargs)

    def get_acquisition_detector_type(self, **kwargs):
        return self.call('get_acquisition_detector_type', kwargs=kwargs)

    def set_acquisition_detector_type(self, **kwargs):
        return self.call('set_acquisition_detector_type', kwargs=kwargs)

    def get_acquisition_detector_type_auto(self, **kwargs):
        return self.call('get_acquisition_detector_type_auto', kwargs=kwargs)

    def set_acquisition_detector_type_auto(self, **kwargs):
        return self.call('set_acquisition_detector_type_auto', kwargs=kwargs)

    def get_wavelength_start(self, **kwargs):
        return self.call('get_wavelength_start', kwargs=kwargs)

    def set_wavelength_start(self, **kwargs):
        return self.call('set_wavelength_start', kwargs=kwargs)

    def get_wavelength_stop(self, **kwargs):
        return self.call('get_wavelength_stop', kwargs=kwargs)

    def set_wavelength_stop(self, **kwargs):
        return self.call('set_wavelength_stop', kwargs=kwargs)

    def get_wavelength_offset(self, **kwargs):
        return self.call('get_wavelength_offset', kwargs=kwargs)

    def set_wavelength_offset(self, **kwargs):
        return self.call('set_wavelength_offset', kwargs=kwargs)

    def get_acquisition_number_of_sweeps(self, **kwargs):
        return self.call('get_acquisition_number_of_sweeps', kwargs=kwargs)

    def set_acquisition_number_of_sweeps(self, **kwargs):
        return self.call('set_acquisition_number_of_sweeps', kwargs=kwargs)

    def get_level_reference(self, **kwargs):
        return self.call('get_level_reference', kwargs=kwargs)

    def set_level_reference(self, **kwargs):
        return self.call('set_level_reference', kwargs=kwargs)

    def get_level_reference_offset(self, **kwargs):
        return self.call('get_level_reference_offset', kwargs=kwargs)

    def set_level_reference_offset(self, **kwargs):
        return self.call('set_level_reference_offset', kwargs=kwargs)

    def get_sweep_coupling_resolution_bandwidth(self, **kwargs):
        return self.call('get_sweep_coupling_resolution_bandwidth', kwargs=kwargs)

    def set_sweep_coupling_resolution_bandwidth(self, **kwargs):
        return self.call('set_sweep_coupling_resolution_bandwidth', kwargs=kwargs)

    def get_sweep_coupling_resolution_bandwidth_auto(self, **kwargs):
        return self.call('get_sweep_coupling_resolution_bandwidth_auto', kwargs=kwargs)

    def set_sweep_coupling_resolution_bandwidth_auto(self, **kwargs):
        return self.call('set_sweep_coupling_resolution_bandwidth_auto', kwargs=kwargs)

    def get_acquisition_sweep_mode_continuous(self, **kwargs):
        return self.call('get_acquisition_sweep_mode_continuous', kwargs=kwargs)

    def set_acquisition_sweep_mode_continuous(self, **kwargs):
        return self.call('set_acquisition_sweep_mode_continuous', kwargs=kwargs)

    def get_sweep_coupling_sweep_time(self, **kwargs):
        return self.call('get_sweep_coupling_sweep_time', kwargs=kwargs)

    def set_sweep_coupling_sweep_time(self, **kwargs):
        return self.call('set_sweep_coupling_sweep_time', kwargs=kwargs)

    def get_sweep_coupling_sweep_time_auto(self, **kwargs):
        return self.call('get_sweep_coupling_sweep_time_auto', kwargs=kwargs)

    def set_sweep_coupling_sweep_time_auto(self, **kwargs):
        return self.call('set_sweep_coupling_sweep_time_auto', kwargs=kwargs)

    def get_traces_name(self, **kwargs):
        return self.call('get_traces_name', kwargs=kwargs)

    def get_traces_type(self, **kwargs):
        return self.call('get_traces_type', kwargs=kwargs)

    def set_traces_type(self, **kwargs):
        return self.call('set_traces_type', kwargs=kwargs)

    def get_acquisition_vertical_scale(self, **kwargs):
        return self.call('get_acquisition_vertical_scale', kwargs=kwargs)

    def set_acquisition_vertical_scale(self, **kwargs):
        return self.call('set_acquisition_vertical_scale', kwargs=kwargs)

    def get_sweep_coupling_video_bandwidth(self, **kwargs):
        return self.call('get_sweep_coupling_video_bandwidth', kwargs=kwargs)

    def set_sweep_coupling_video_bandwidth(self, **kwargs):
        return self.call('set_sweep_coupling_video_bandwidth', kwargs=kwargs)

    def get_sweep_coupling_video_bandwidth_auto(self, **kwargs):
        return self.call('get_sweep_coupling_video_bandwidth_auto', kwargs=kwargs)

    def set_sweep_coupling_video_bandwidth_auto(self, **kwargs):
        return self.call('set_sweep_coupling_video_bandwidth_auto', kwargs=kwargs)

    def acquisition_abort(self, **kwargs):
        return self.call('acquisition_abort', kwargs=kwargs)

    def acquisition_status(self, **kwargs):
        return self.call('acquisition_status', kwargs=kwargs)

    def acquisition_configure(self, **kwargs):
        return self.call('acquisition_configure', kwargs=kwargs)

    def wavelength_configure_center_span(self, **kwargs):
        return self.call('wavelength_configure_center_span', kwargs=kwargs)

    def wavelength_configure_start_stop(self, **kwargs):
        return self.call('wavelength_configure_start_stop', kwargs=kwargs)

    def level_configure(self, **kwargs):
        return self.call('level_configure', kwargs=kwargs)

    def sweep_coupling_configure(self, **kwargs):
        return self.call('sweep_coupling_configure', kwargs=kwargs)

    def traces_fetch_y(self, **kwargs):
        return self.call('traces_fetch_y', kwargs=kwargs)

    def acquisition_initiate(self, **kwargs):
        return self.call('acquisition_initiate', kwargs=kwargs)

    def traces_read_y(self, **kwargs):
        return self.call('traces_read_y', kwargs=kwargs)

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

    def display_fetch_screenshot(self, **kwargs):
        return self.call('display_fetch_screenshot', kwargs=kwargs)

    def memory_save(self, **kwargs):
        return self.call('memory_save', kwargs=kwargs)

    def memory_recall(self, **kwargs):
        return self.call('memory_recall', kwargs=kwargs)

