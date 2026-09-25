from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityStrictColbypdl10a(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/strict_candidates_repos/python-ivi__python-ivi', 'source_file': 'ivi/colby/colbyPDL10A.py', 'class_name': 'colbyPDL10A', 'import_roots': [], 'candidate_methods': ['get_delay', 'set_delay', 'get_mode', 'set_mode', 'get_identity_instrument_serial_number', 'initialize', 'get_initialized', 'close', 'get_driver_operation_cache', 'set_driver_operation_cache', 'get_driver_operation_driver_setup', 'get_driver_operation_interchange_check', 'set_driver_operation_interchange_check', 'get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status', 'get_driver_operation_range_check', 'set_driver_operation_range_check', 'get_driver_operation_record_coercions', 'set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check', 'get_identity_description', 'get_identity_identifier', 'get_identity_revision', 'get_identity_vendor', 'get_identity_instrument_manufacturer', 'get_identity_instrument_model', 'get_identity_instrument_firmware_revision', 'get_identity_specification_major_version', 'get_identity_specification_minor_version', 'get_identity_supported_instrument_models', 'get_identity_group_capabilities', 'identity_get_group_capabilities', 'identity_get_supported_instrument_models', 'utility_disable', 'utility_error_query', 'utility_lock_object', 'utility_reset', 'utility_reset_with_defaults', 'utility_self_test', 'utility_unlock_object'], 'action_targets': {'get_delay': '_get_delay', 'set_delay': '_set_delay', 'get_mode': '_get_mode', 'set_mode': '_set_mode', 'get_identity_instrument_serial_number': '_get_identity_instrument_serial_number', 'initialize': '_initialize', 'get_initialized': '_get_initialized', 'close': '_close', 'get_driver_operation_cache': '_get_driver_operation_cache', 'set_driver_operation_cache': '_set_driver_operation_cache', 'get_driver_operation_driver_setup': '_get_driver_operation_driver_setup', 'get_driver_operation_interchange_check': '_get_driver_operation_interchange_check', 'set_driver_operation_interchange_check': '_set_driver_operation_interchange_check', 'get_driver_operation_logical_name': '_get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status': '_get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status': '_set_driver_operation_query_instrument_status', 'get_driver_operation_range_check': '_get_driver_operation_range_check', 'set_driver_operation_range_check': '_set_driver_operation_range_check', 'get_driver_operation_record_coercions': '_get_driver_operation_record_coercions', 'set_driver_operation_record_coercions': '_set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor': '_get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate': '_get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings': '_driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record': '_driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning': '_driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes': '_driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check': '_driver_operation_reset_interchange_check', 'get_identity_description': '_get_identity_description', 'get_identity_identifier': '_get_identity_identifier', 'get_identity_revision': '_get_identity_revision', 'get_identity_vendor': '_get_identity_vendor', 'get_identity_instrument_manufacturer': '_get_identity_instrument_manufacturer', 'get_identity_instrument_model': '_get_identity_instrument_model', 'get_identity_instrument_firmware_revision': '_get_identity_instrument_firmware_revision', 'get_identity_specification_major_version': '_get_identity_specification_major_version', 'get_identity_specification_minor_version': '_get_identity_specification_minor_version', 'get_identity_supported_instrument_models': '_get_identity_supported_instrument_models', 'get_identity_group_capabilities': '_get_identity_group_capabilities', 'identity_get_group_capabilities': '_identity_get_group_capabilities', 'identity_get_supported_instrument_models': '_identity_get_supported_instrument_models', 'utility_disable': '_utility_disable', 'utility_error_query': '_utility_error_query', 'utility_lock_object': '_utility_lock_object', 'utility_reset': '_utility_reset', 'utility_reset_with_defaults': '_utility_reset_with_defaults', 'utility_self_test': '_utility_self_test', 'utility_unlock_object': '_utility_unlock_object'}, 'metadata': {'repo': 'python-ivi/python-ivi', 'repo_url': 'https://github.com/python-ivi/python-ivi', 'source_url': 'https://github.com/python-ivi/python-ivi/blob/main/ivi/colby/colbyPDL10A.py', 'confidence': 0.75, 'quality_score': 0.89, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'get_delay': '_get_delay', 'set_delay': '_set_delay', 'get_mode': '_get_mode', 'set_mode': '_set_mode', 'get_identity_instrument_serial_number': '_get_identity_instrument_serial_number', 'initialize': '_initialize', 'get_initialized': '_get_initialized', 'close': '_close', 'get_driver_operation_cache': '_get_driver_operation_cache', 'set_driver_operation_cache': '_set_driver_operation_cache', 'get_driver_operation_driver_setup': '_get_driver_operation_driver_setup', 'get_driver_operation_interchange_check': '_get_driver_operation_interchange_check', 'set_driver_operation_interchange_check': '_set_driver_operation_interchange_check', 'get_driver_operation_logical_name': '_get_driver_operation_logical_name', 'get_driver_operation_query_instrument_status': '_get_driver_operation_query_instrument_status', 'set_driver_operation_query_instrument_status': '_set_driver_operation_query_instrument_status', 'get_driver_operation_range_check': '_get_driver_operation_range_check', 'set_driver_operation_range_check': '_set_driver_operation_range_check', 'get_driver_operation_record_coercions': '_get_driver_operation_record_coercions', 'set_driver_operation_record_coercions': '_set_driver_operation_record_coercions', 'get_driver_operation_io_resource_descriptor': '_get_driver_operation_io_resource_descriptor', 'get_driver_operation_simulate': '_get_driver_operation_simulate', 'driver_operation_clear_interchange_warnings': '_driver_operation_clear_interchange_warnings', 'driver_operation_get_next_coercion_record': '_driver_operation_get_next_coercion_record', 'driver_operation_get_next_interchange_warning': '_driver_operation_get_next_interchange_warning', 'driver_operation_invalidate_all_attributes': '_driver_operation_invalidate_all_attributes', 'driver_operation_reset_interchange_check': '_driver_operation_reset_interchange_check', 'get_identity_description': '_get_identity_description', 'get_identity_identifier': '_get_identity_identifier', 'get_identity_revision': '_get_identity_revision', 'get_identity_vendor': '_get_identity_vendor', 'get_identity_instrument_manufacturer': '_get_identity_instrument_manufacturer', 'get_identity_instrument_model': '_get_identity_instrument_model', 'get_identity_instrument_firmware_revision': '_get_identity_instrument_firmware_revision', 'get_identity_specification_major_version': '_get_identity_specification_major_version', 'get_identity_specification_minor_version': '_get_identity_specification_minor_version', 'get_identity_supported_instrument_models': '_get_identity_supported_instrument_models', 'get_identity_group_capabilities': '_get_identity_group_capabilities', 'identity_get_group_capabilities': '_identity_get_group_capabilities', 'identity_get_supported_instrument_models': '_identity_get_supported_instrument_models', 'utility_disable': '_utility_disable', 'utility_error_query': '_utility_error_query', 'utility_lock_object': '_utility_lock_object', 'utility_reset': '_utility_reset', 'utility_reset_with_defaults': '_utility_reset_with_defaults', 'utility_self_test': '_utility_self_test', 'utility_unlock_object': '_utility_unlock_object'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_delay(self, **kwargs):
        return self.call('get_delay', kwargs=kwargs)

    def set_delay(self, **kwargs):
        return self.call('set_delay', kwargs=kwargs)

    def get_mode(self, **kwargs):
        return self.call('get_mode', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def get_identity_instrument_serial_number(self, **kwargs):
        return self.call('get_identity_instrument_serial_number', kwargs=kwargs)

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

