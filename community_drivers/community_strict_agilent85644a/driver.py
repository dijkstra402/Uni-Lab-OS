from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictAgilent85644a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/python-ivi__python-ivi', 'source_file': 'ivi/agilent/agilent85644A.py', 'class_name': 'agilent85644A', 'import_roots': [], 'candidate_methods': ['get_rf_frequency', 'set_rf_frequency', 'get_rf_frequency_offset', 'set_rf_frequency_offset', 'get_rf_frequency_mode', 'set_rf_frequency_mode', 'get_rf_level', 'set_rf_level', 'get_rf_attenuation', 'set_rf_attenuation', 'get_rf_attenuation_auto', 'set_rf_attenuation_auto', 'get_rf_output_enabled', 'set_rf_output_enabled', 'get_rf_power_mode', 'set_rf_power_mode', 'get_rf_power_slope', 'set_rf_power_slope', 'get_rf_power_center', 'set_rf_power_center', 'get_rf_power_span', 'set_rf_power_span', 'get_rf_tracking_adjust', 'set_rf_tracking_adjust', 'get_rf_tracking_host', 'set_rf_tracking_host', 'get_rf_tracking_sweeptune', 'set_rf_tracking_sweeptune', 'rf_configure', 'rf_is_unleveled', 'get_alc_enabled', 'set_alc_enabled', 'get_alc_source', 'set_alc_source', 'get_reference_oscillator_source', 'initialize', 'get_initialized', 'close', 'get_driver_operation_cache', 'set_driver_operation_cache', 'get_driver_operation_driver_setup', 'get_driver_operation_interchange_check', 'set_driver_operation_interchange_check', 'get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status', 'get_driver_operation_range_check', 'set_driver_operation_range_check', 'get_driver_operation_record_coercions', 'set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check', 'get_identity_description', 'get_identity_identifier', 'get_identity_revision', 'get_identity_vendor', 'get_identity_instrument_manufacturer', 'get_identity_instrument_model', 'get_identity_instrument_firmware_revision', 'get_identity_specification_major_version', 'get_identity_specification_minor_version', 'get_identity_supported_instrument_models', 'get_identity_group_capabilities', 'identity_get_group_capabilities', 'identity_get_supported_instrument_models', 'utility_disable', 'utility_error_query', 'utility_lock_object', 'utility_reset', 'utility_reset_with_defaults', 'utility_self_test', 'utility_unlock_object', 'memory_save', 'memory_recall'], 'action_targets': {'get_rf_frequency': '_get_rf_frequency', 'set_rf_frequency': '_set_rf_frequency', 'get_rf_frequency_offset': '_get_rf_frequency_offset', 'set_rf_frequency_offset': '_set_rf_frequency_offset', 'get_rf_frequency_mode': '_get_rf_frequency_mode', 'set_rf_frequency_mode': '_set_rf_frequency_mode', 'get_rf_level': '_get_rf_level', 'set_rf_level': '_set_rf_level', 'get_rf_attenuation': '_get_rf_attenuation', 'set_rf_attenuation': '_set_rf_attenuation', 'get_rf_attenuation_auto': '_get_rf_attenuation_auto', 'set_rf_attenuation_auto': '_set_rf_attenuation_auto', 'get_rf_output_enabled': '_get_rf_output_enabled', 'set_rf_output_enabled': '_set_rf_output_enabled', 'get_rf_power_mode': '_get_rf_power_mode', 'set_rf_power_mode': '_set_rf_power_mode', 'get_rf_power_slope': '_get_rf_power_slope', 'set_rf_power_slope': '_set_rf_power_slope', 'get_rf_power_center': '_get_rf_power_center', 'set_rf_power_center': '_set_rf_power_center', 'get_rf_power_span': '_get_rf_power_span', 'set_rf_power_span': '_set_rf_power_span', 'get_rf_tracking_adjust': '_get_rf_tracking_adjust', 'set_rf_tracking_adjust': '_set_rf_tracking_adjust', 'get_rf_tracking_host': '_get_rf_tracking_host', 'set_rf_tracking_host': '_set_rf_tracking_host', 'get_rf_tracking_sweeptune': '_get_rf_tracking_sweeptune', 'set_rf_tracking_sweeptune': '_set_rf_tracking_sweeptune', 'rf_configure': '_rf_configure', 'rf_is_unleveled': '_rf_is_unleveled', 'get_alc_enabled': '_get_alc_enabled', 'set_alc_enabled': '_set_alc_enabled', 'get_alc_source': '_get_alc_source', 'set_alc_source': '_set_alc_source', 'get_reference_oscillator_source': '_get_reference_oscillator_source', 'initialize': '_initialize', 'get_initialized': '_get_initialized', 'close': '_close', 'get_driver_operation_cache': '_get_driver_operation_cache', 'set_driver_operation_cache': '_set_driver_operation_cache', 'get_driver_operation_driver_setup': '_get_driver_operation_driver_setup', 'get_driver_operation_interchange_check': '_get_driver_operation_interchange_check', 'set_driver_operation_interchange_check': '_set_driver_operation_interchange_check', 'get_driver_operation_logical_name': '_get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status': '_get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status': '_set_driver_operation_query_instrument_status', 'get_driver_operation_range_check': '_get_driver_operation_range_check', 'set_driver_operation_range_check': '_set_driver_operation_range_check', 'get_driver_operation_record_coercions': '_get_driver_operation_record_coercions', 'set_driver_operation_record_coercions': '_set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor': '_get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate': '_get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings': '_driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record': '_driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning': '_driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes': '_driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check': '_driver_operation_reset_interchange_check', 'get_identity_description': '_get_identity_description', 'get_identity_identifier': '_get_identity_identifier', 'get_identity_revision': '_get_identity_revision', 'get_identity_vendor': '_get_identity_vendor', 'get_identity_instrument_manufacturer': '_get_identity_instrument_manufacturer', 'get_identity_instrument_model': '_get_identity_instrument_model', 'get_identity_instrument_firmware_revision': '_get_identity_instrument_firmware_revision', 'get_identity_specification_major_version': '_get_identity_specification_major_version', 'get_identity_specification_minor_version': '_get_identity_specification_minor_version', 'get_identity_supported_instrument_models': '_get_identity_supported_instrument_models', 'get_identity_group_capabilities': '_get_identity_group_capabilities', 'identity_get_group_capabilities': '_identity_get_group_capabilities', 'identity_get_supported_instrument_models': '_identity_get_supported_instrument_models', 'utility_disable': '_utility_disable', 'utility_error_query': '_utility_error_query', 'utility_lock_object': '_utility_lock_object', 'utility_reset': '_utility_reset', 'utility_reset_with_defaults': '_utility_reset_with_defaults', 'utility_self_test': '_utility_self_test', 'utility_unlock_object': '_utility_unlock_object', 'memory_save': '_memory_save', 'memory_recall': '_memory_recall'}, 'metadata': {'repo': 'python-ivi/python-ivi', 'repo_url': 'https://github.com/python-ivi/python-ivi', 'source_url': 'https://github.com/python-ivi/python-ivi/blob/main/ivi/agilent/agilent85644A.py', 'confidence': 0.9, 'quality_score': 1.12, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_rf_frequency': '_get_rf_frequency', 'set_rf_frequency': '_set_rf_frequency', 'get_rf_frequency_offset': '_get_rf_frequency_offset', 'set_rf_frequency_offset': '_set_rf_frequency_offset', 'get_rf_frequency_mode': '_get_rf_frequency_mode', 'set_rf_frequency_mode': '_set_rf_frequency_mode', 'get_rf_level': '_get_rf_level', 'set_rf_level': '_set_rf_level', 'get_rf_attenuation': '_get_rf_attenuation', 'set_rf_attenuation': '_set_rf_attenuation', 'get_rf_attenuation_auto': '_get_rf_attenuation_auto', 'set_rf_attenuation_auto': '_set_rf_attenuation_auto', 'get_rf_output_enabled': '_get_rf_output_enabled', 'set_rf_output_enabled': '_set_rf_output_enabled', 'get_rf_power_mode': '_get_rf_power_mode', 'set_rf_power_mode': '_set_rf_power_mode', 'get_rf_power_slope': '_get_rf_power_slope', 'set_rf_power_slope': '_set_rf_power_slope', 'get_rf_power_center': '_get_rf_power_center', 'set_rf_power_center': '_set_rf_power_center', 'get_rf_power_span': '_get_rf_power_span', 'set_rf_power_span': '_set_rf_power_span', 'get_rf_tracking_adjust': '_get_rf_tracking_adjust', 'set_rf_tracking_adjust': '_set_rf_tracking_adjust', 'get_rf_tracking_host': '_get_rf_tracking_host', 'set_rf_tracking_host': '_set_rf_tracking_host', 'get_rf_tracking_sweeptune': '_get_rf_tracking_sweeptune', 'set_rf_tracking_sweeptune': '_set_rf_tracking_sweeptune', 'rf_configure': '_rf_configure', 'rf_is_unleveled': '_rf_is_unleveled', 'get_alc_enabled': '_get_alc_enabled', 'set_alc_enabled': '_set_alc_enabled', 'get_alc_source': '_get_alc_source', 'set_alc_source': '_set_alc_source', 'get_reference_oscillator_source': '_get_reference_oscillator_source', 'initialize': '_initialize', 'get_initialized': '_get_initialized', 'close': '_close', 'get_driver_operation_cache': '_get_driver_operation_cache', 'set_driver_operation_cache': '_set_driver_operation_cache', 'get_driver_operation_driver_setup': '_get_driver_operation_driver_setup', 'get_driver_operation_interchange_check': '_get_driver_operation_interchange_check', 'set_driver_operation_interchange_check': '_set_driver_operation_interchange_check', 'get_driver_operation_logical_name': '_get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status': '_get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status': '_set_driver_operation_query_instrument_status', 'get_driver_operation_range_check': '_get_driver_operation_range_check', 'set_driver_operation_range_check': '_set_driver_operation_range_check', 'get_driver_operation_record_coercions': '_get_driver_operation_record_coercions', 'set_driver_operation_record_coercions': '_set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor': '_get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate': '_get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings': '_driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record': '_driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning': '_driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes': '_driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check': '_driver_operation_reset_interchange_check', 'get_identity_description': '_get_identity_description', 'get_identity_identifier': '_get_identity_identifier', 'get_identity_revision': '_get_identity_revision', 'get_identity_vendor': '_get_identity_vendor', 'get_identity_instrument_manufacturer': '_get_identity_instrument_manufacturer', 'get_identity_instrument_model': '_get_identity_instrument_model', 'get_identity_instrument_firmware_revision': '_get_identity_instrument_firmware_revision', 'get_identity_specification_major_version': '_get_identity_specification_major_version', 'get_identity_specification_minor_version': '_get_identity_specification_minor_version', 'get_identity_supported_instrument_models': '_get_identity_supported_instrument_models', 'get_identity_group_capabilities': '_get_identity_group_capabilities', 'identity_get_group_capabilities': '_identity_get_group_capabilities', 'identity_get_supported_instrument_models': '_identity_get_supported_instrument_models', 'utility_disable': '_utility_disable', 'utility_error_query': '_utility_error_query', 'utility_lock_object': '_utility_lock_object', 'utility_reset': '_utility_reset', 'utility_reset_with_defaults': '_utility_reset_with_defaults', 'utility_self_test': '_utility_self_test', 'utility_unlock_object': '_utility_unlock_object', 'memory_save': '_memory_save', 'memory_recall': '_memory_recall'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_rf_frequency(self, **kwargs):
        return self.call('get_rf_frequency', kwargs=kwargs)

    def set_rf_frequency(self, **kwargs):
        return self.call('set_rf_frequency', kwargs=kwargs)

    def get_rf_frequency_offset(self, **kwargs):
        return self.call('get_rf_frequency_offset', kwargs=kwargs)

    def set_rf_frequency_offset(self, **kwargs):
        return self.call('set_rf_frequency_offset', kwargs=kwargs)

    def get_rf_frequency_mode(self, **kwargs):
        return self.call('get_rf_frequency_mode', kwargs=kwargs)

    def set_rf_frequency_mode(self, **kwargs):
        return self.call('set_rf_frequency_mode', kwargs=kwargs)

    def get_rf_level(self, **kwargs):
        return self.call('get_rf_level', kwargs=kwargs)

    def set_rf_level(self, **kwargs):
        return self.call('set_rf_level', kwargs=kwargs)

    def get_rf_attenuation(self, **kwargs):
        return self.call('get_rf_attenuation', kwargs=kwargs)

    def set_rf_attenuation(self, **kwargs):
        return self.call('set_rf_attenuation', kwargs=kwargs)

    def get_rf_attenuation_auto(self, **kwargs):
        return self.call('get_rf_attenuation_auto', kwargs=kwargs)

    def set_rf_attenuation_auto(self, **kwargs):
        return self.call('set_rf_attenuation_auto', kwargs=kwargs)

    def get_rf_output_enabled(self, **kwargs):
        return self.call('get_rf_output_enabled', kwargs=kwargs)

    def set_rf_output_enabled(self, **kwargs):
        return self.call('set_rf_output_enabled', kwargs=kwargs)

    def get_rf_power_mode(self, **kwargs):
        return self.call('get_rf_power_mode', kwargs=kwargs)

    def set_rf_power_mode(self, **kwargs):
        return self.call('set_rf_power_mode', kwargs=kwargs)

    def get_rf_power_slope(self, **kwargs):
        return self.call('get_rf_power_slope', kwargs=kwargs)

    def set_rf_power_slope(self, **kwargs):
        return self.call('set_rf_power_slope', kwargs=kwargs)

    def get_rf_power_center(self, **kwargs):
        return self.call('get_rf_power_center', kwargs=kwargs)

    def set_rf_power_center(self, **kwargs):
        return self.call('set_rf_power_center', kwargs=kwargs)

    def get_rf_power_span(self, **kwargs):
        return self.call('get_rf_power_span', kwargs=kwargs)

    def set_rf_power_span(self, **kwargs):
        return self.call('set_rf_power_span', kwargs=kwargs)

    def get_rf_tracking_adjust(self, **kwargs):
        return self.call('get_rf_tracking_adjust', kwargs=kwargs)

    def set_rf_tracking_adjust(self, **kwargs):
        return self.call('set_rf_tracking_adjust', kwargs=kwargs)

    def get_rf_tracking_host(self, **kwargs):
        return self.call('get_rf_tracking_host', kwargs=kwargs)

    def set_rf_tracking_host(self, **kwargs):
        return self.call('set_rf_tracking_host', kwargs=kwargs)

    def get_rf_tracking_sweeptune(self, **kwargs):
        return self.call('get_rf_tracking_sweeptune', kwargs=kwargs)

    def set_rf_tracking_sweeptune(self, **kwargs):
        return self.call('set_rf_tracking_sweeptune', kwargs=kwargs)

    def rf_configure(self, **kwargs):
        return self.call('rf_configure', kwargs=kwargs)

    def rf_is_unleveled(self, **kwargs):
        return self.call('rf_is_unleveled', kwargs=kwargs)

    def get_alc_enabled(self, **kwargs):
        return self.call('get_alc_enabled', kwargs=kwargs)

    def set_alc_enabled(self, **kwargs):
        return self.call('set_alc_enabled', kwargs=kwargs)

    def get_alc_source(self, **kwargs):
        return self.call('get_alc_source', kwargs=kwargs)

    def set_alc_source(self, **kwargs):
        return self.call('set_alc_source', kwargs=kwargs)

    def get_reference_oscillator_source(self, **kwargs):
        return self.call('get_reference_oscillator_source', kwargs=kwargs)

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

    def memory_save(self, **kwargs):
        return self.call('memory_save', kwargs=kwargs)

    def memory_recall(self, **kwargs):
        return self.call('memory_recall', kwargs=kwargs)

