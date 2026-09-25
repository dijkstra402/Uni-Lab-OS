from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIdsUeyeUeye(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/samhitech__microEye', 'source_file': 'src/microEye/hardware/pycromanager/core.py', 'class_name': 'PycroCore', 'import_roots': ['src'], 'candidate_methods': ['instance', 'get_camera_list', 'start', 'close', 'reconnect', 'is_connected', 'add_galvo_polygon_vertex', 'add_search_path', 'clear_circular_buffer', 'clear_roi', 'debug_log_enabled', 'define_config', 'define_config_group', 'define_pixel_size_config', 'define_property_block', 'define_state_label', 'delete', 'delete_config', 'delete_config_group', 'delete_galvo_polygons', 'delete_pixel_size_config', 'detect_device', 'device_busy', 'device_type_busy', 'display_slm_image', 'enable_continuous_focus', 'enable_debug_log', 'enable_stderr_log', 'full_focus', 'get_allowed_property_values', 'get_api_version_info', 'get_auto_focus_device', 'get_auto_focus_offset', 'get_auto_shutter', 'get_available_config_groups', 'get_available_configs', 'get_available_device_descriptions', 'get_available_devices', 'get_available_device_types', 'get_available_pixel_size_configs', 'get_buffer_free_capacity', 'get_buffer_total_capacity', 'get_bytes_per_pixel', 'get_camera_channel_name', 'get_camera_device', 'get_channel_group', 'get_circular_buffer_memory_footprint', 'get_config_data', 'get_config_group_state', 'get_config_group_state_from_cache', 'get_config_state', 'get_core_error_text', 'get_current_config', 'get_current_config_from_cache', 'get_current_focus_score', 'get_current_pixel_size_config', 'get_data', 'get_device_adapter_names', 'get_device_adapter_search_paths', 'get_device_delay_ms', 'get_device_description', 'get_device_name', 'get_device_property_names', 'get_device_type', 'get_exposure', 'get_exposure_sequence_max_length', 'get_focus_device', 'get_focus_direction', 'get_galvo_channel', 'get_galvo_device', 'get_galvo_position', 'get_galvo_x_minimum', 'get_galvo_x_range', 'get_galvo_y_minimum', 'get_galvo_y_range', 'get_image', 'get_image_bit_depth', 'get_image_buffer_size', 'get_image_height', 'get_image_processor_device', 'get_image_width', 'get_installed_device_description', 'get_installed_devices', 'get_last_focus_score', 'get_last_image', 'get_last_image_md', 'get_last_tagged_image', 'get_loaded_devices', 'get_loaded_devices_of_type', 'get_loaded_peripheral_devices', 'get_magnification_factor', 'get_multi_roi', 'get_n_before_last_image_md', 'get_n_before_last_tagged_image', 'get_number_of_camera_channels', 'get_number_of_components', 'get_number_of_galvo_polygons', 'get_number_of_states', 'get_parent_label', 'get_pixel_size_affine', 'get_pixel_size_affine_as_string', 'get_pixel_size_affine_by_id', 'get_pixel_size_config_data', 'get_pixel_size_um', 'get_pixel_size_um_by_id', 'get_position', 'get_primary_log_file', 'get_property', 'get_property_from_cache', 'get_property_lower_limit', 'get_property_sequence_max_length', 'get_property_type', 'get_property_upper_limit', 'get_property_limits', 'get_remaining_image_count', 'get_roi', 'get_serial_port_answer', 'get_shutter_device', 'get_shutter_open', 'get_slm_bytes_per_pixel', 'get_slm_device', 'get_slm_exposure', 'get_slm_height', 'get_slm_number_of_components', 'get_slm_sequence_max_length', 'get_slm_width', 'get_stage_sequence_max_length', 'get_state', 'get_state_from_label', 'get_state_label', 'get_state_labels', 'get_system_state', 'get_system_state_cache', 'get_tagged_image', 'get_timeout_ms', 'get_version_info', 'get_x_position', 'get_xy_position', 'get_xy_stage_device', 'get_xy_stage_position', 'get_xy_stage_sequence_max_length', 'get_y_position', 'has_property', 'has_property_limits', 'home', 'incremental_focus', 'initialize_all_devices', 'initialize_circular_buffer', 'initialize_device', 'is_buffer_overflowed', 'is_config_defined', 'is_continuous_focus_drive', 'is_continuous_focus_enabled', 'is_continuous_focus_locked', 'is_exposure_sequenceable', 'is_group_defined', 'is_multi_roi_enabled', 'is_multi_roi_supported', 'is_pixel_size_config_defined', 'is_property_pre_init', 'is_property_read_only', 'is_property_sequenceable', 'is_sequence_running', 'is_stage_linear_sequenceable', 'is_stage_sequenceable', 'is_xy_stage_sequenceable', 'load_device', 'load_exposure_sequence', 'load_galvo_polygons', 'load_property_sequence', 'load_slm_sequence', 'load_stage_sequence', 'load_system_configuration', 'load_system_state', 'load_xy_stage_sequence', 'log_message', 'point_galvo_and_fire', 'pop_next_image', 'pop_next_image_md', 'pop_next_tagged_image', 'prepare_sequence_acquisition', 'read_from_serial_port', 'register_callback', 'rename_config', 'rename_config_group', 'rename_pixel_size_config', 'reset', 'run_galvo_polygons', 'run_galvo_sequence', 'save_system_configuration', 'save_system_state', 'set_adapter_origin', 'set_adapter_origin_xy', 'set_auto_focus_device', 'set_auto_focus_offset', 'set_auto_shutter', 'set_camera_device', 'set_channel_group', 'set_circular_buffer_memory_footprint', 'set_config', 'set_device_adapter_search_paths', 'set_device_delay_ms', 'set_exposure', 'set_focus_device', 'set_focus_direction', 'set_galvo_device', 'set_galvo_illumination_state', 'set_galvo_polygon_repetitions', 'set_galvo_position', 'set_galvo_spot_interval', 'set_image_processor_device', 'set_metadata_profile', 'set_multi_roi', 'set_origin', 'set_origin_x', 'set_origin_xy', 'set_origin_y', 'set_parent_label', 'set_pixel_size_affine', 'set_pixel_size_config', 'set_pixel_size_um', 'set_position', 'set_primary_log_file', 'set_property', 'set_relative_position', 'set_relative_xy_position', 'set_roi', 'set_shutter_device', 'set_shutter_open', 'set_slm_device', 'set_slm_exposure', 'set_slm_image', 'set_slm_pixels_to', 'set_stage_linear_sequence', 'set_state', 'set_state_label', 'set_system_state', 'set_timeout_ms', 'set_xy_position', 'set_xy_stage_device', 'sleep', 'snap_image', 'start_continuous_sequence_acquisition', 'start_exposure_sequence', 'start_property_sequence', 'start_secondary_log_file', 'start_sequence_acquisition', 'start_slm_sequence', 'start_stage_sequence', 'start_xy_stage_sequence', 'stderr_log_enabled', 'stop', 'stop_exposure_sequence', 'stop_property_sequence', 'stop_secondary_log_file', 'stop_sequence_acquisition', 'stop_slm_sequence', 'stop_stage_sequence', 'stop_xy_stage_sequence', 'supports_device_detection', 'system_busy', 'unload_all_devices', 'unload_device', 'unload_library', 'update_core_properties', 'update_system_state_cache', 'uses_device_delay', 'wait_for_config', 'wait_for_device', 'wait_for_device_type', 'wait_for_system'], 'action_targets': {}, 'metadata': {'repo': 'samhitech/microEye', 'repo_url': 'https://github.com/samhitech/microEye', 'brand': 'IDS', 'model': 'uEye/uEye+', 'device_type_cn': '工业相机', 'device_type_en': 'Industrial Camera', 'source_framework': '显微镜/成像', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 2206, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def instance(self, **kwargs):
        return self.call('instance', kwargs=kwargs)

    def get_camera_list(self, **kwargs):
        return self.call('get_camera_list', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def reconnect(self, **kwargs):
        return self.call('reconnect', kwargs=kwargs)

    def is_connected(self, **kwargs):
        return self.call('is_connected', kwargs=kwargs)

    def add_galvo_polygon_vertex(self, **kwargs):
        return self.call('add_galvo_polygon_vertex', kwargs=kwargs)

    def add_search_path(self, **kwargs):
        return self.call('add_search_path', kwargs=kwargs)

    def clear_circular_buffer(self, **kwargs):
        return self.call('clear_circular_buffer', kwargs=kwargs)

    def clear_roi(self, **kwargs):
        return self.call('clear_roi', kwargs=kwargs)

    def debug_log_enabled(self, **kwargs):
        return self.call('debug_log_enabled', kwargs=kwargs)

    def define_config(self, **kwargs):
        return self.call('define_config', kwargs=kwargs)

    def define_config_group(self, **kwargs):
        return self.call('define_config_group', kwargs=kwargs)

    def define_pixel_size_config(self, **kwargs):
        return self.call('define_pixel_size_config', kwargs=kwargs)

    def define_property_block(self, **kwargs):
        return self.call('define_property_block', kwargs=kwargs)

    def define_state_label(self, **kwargs):
        return self.call('define_state_label', kwargs=kwargs)

    def delete(self, **kwargs):
        return self.call('delete', kwargs=kwargs)

    def delete_config(self, **kwargs):
        return self.call('delete_config', kwargs=kwargs)

    def delete_config_group(self, **kwargs):
        return self.call('delete_config_group', kwargs=kwargs)

    def delete_galvo_polygons(self, **kwargs):
        return self.call('delete_galvo_polygons', kwargs=kwargs)

    def delete_pixel_size_config(self, **kwargs):
        return self.call('delete_pixel_size_config', kwargs=kwargs)

    def detect_device(self, **kwargs):
        return self.call('detect_device', kwargs=kwargs)

    def device_busy(self, **kwargs):
        return self.call('device_busy', kwargs=kwargs)

    def device_type_busy(self, **kwargs):
        return self.call('device_type_busy', kwargs=kwargs)

    def display_slm_image(self, **kwargs):
        return self.call('display_slm_image', kwargs=kwargs)

    def enable_continuous_focus(self, **kwargs):
        return self.call('enable_continuous_focus', kwargs=kwargs)

    def enable_debug_log(self, **kwargs):
        return self.call('enable_debug_log', kwargs=kwargs)

    def enable_stderr_log(self, **kwargs):
        return self.call('enable_stderr_log', kwargs=kwargs)

    def full_focus(self, **kwargs):
        return self.call('full_focus', kwargs=kwargs)

    def get_allowed_property_values(self, **kwargs):
        return self.call('get_allowed_property_values', kwargs=kwargs)

    def get_api_version_info(self, **kwargs):
        return self.call('get_api_version_info', kwargs=kwargs)

    def get_auto_focus_device(self, **kwargs):
        return self.call('get_auto_focus_device', kwargs=kwargs)

    def get_auto_focus_offset(self, **kwargs):
        return self.call('get_auto_focus_offset', kwargs=kwargs)

    def get_auto_shutter(self, **kwargs):
        return self.call('get_auto_shutter', kwargs=kwargs)

    def get_available_config_groups(self, **kwargs):
        return self.call('get_available_config_groups', kwargs=kwargs)

    def get_available_configs(self, **kwargs):
        return self.call('get_available_configs', kwargs=kwargs)

    def get_available_device_descriptions(self, **kwargs):
        return self.call('get_available_device_descriptions', kwargs=kwargs)

    def get_available_devices(self, **kwargs):
        return self.call('get_available_devices', kwargs=kwargs)

    def get_available_device_types(self, **kwargs):
        return self.call('get_available_device_types', kwargs=kwargs)

    def get_available_pixel_size_configs(self, **kwargs):
        return self.call('get_available_pixel_size_configs', kwargs=kwargs)

    def get_buffer_free_capacity(self, **kwargs):
        return self.call('get_buffer_free_capacity', kwargs=kwargs)

    def get_buffer_total_capacity(self, **kwargs):
        return self.call('get_buffer_total_capacity', kwargs=kwargs)

    def get_bytes_per_pixel(self, **kwargs):
        return self.call('get_bytes_per_pixel', kwargs=kwargs)

    def get_camera_channel_name(self, **kwargs):
        return self.call('get_camera_channel_name', kwargs=kwargs)

    def get_camera_device(self, **kwargs):
        return self.call('get_camera_device', kwargs=kwargs)

    def get_channel_group(self, **kwargs):
        return self.call('get_channel_group', kwargs=kwargs)

    def get_circular_buffer_memory_footprint(self, **kwargs):
        return self.call('get_circular_buffer_memory_footprint', kwargs=kwargs)

    def get_config_data(self, **kwargs):
        return self.call('get_config_data', kwargs=kwargs)

    def get_config_group_state(self, **kwargs):
        return self.call('get_config_group_state', kwargs=kwargs)

    def get_config_group_state_from_cache(self, **kwargs):
        return self.call('get_config_group_state_from_cache', kwargs=kwargs)

    def get_config_state(self, **kwargs):
        return self.call('get_config_state', kwargs=kwargs)

    def get_core_error_text(self, **kwargs):
        return self.call('get_core_error_text', kwargs=kwargs)

    def get_current_config(self, **kwargs):
        return self.call('get_current_config', kwargs=kwargs)

    def get_current_config_from_cache(self, **kwargs):
        return self.call('get_current_config_from_cache', kwargs=kwargs)

    def get_current_focus_score(self, **kwargs):
        return self.call('get_current_focus_score', kwargs=kwargs)

    def get_current_pixel_size_config(self, **kwargs):
        return self.call('get_current_pixel_size_config', kwargs=kwargs)

    def get_data(self, **kwargs):
        return self.call('get_data', kwargs=kwargs)

    def get_device_adapter_names(self, **kwargs):
        return self.call('get_device_adapter_names', kwargs=kwargs)

    def get_device_adapter_search_paths(self, **kwargs):
        return self.call('get_device_adapter_search_paths', kwargs=kwargs)

    def get_device_delay_ms(self, **kwargs):
        return self.call('get_device_delay_ms', kwargs=kwargs)

    def get_device_description(self, **kwargs):
        return self.call('get_device_description', kwargs=kwargs)

    def get_device_name(self, **kwargs):
        return self.call('get_device_name', kwargs=kwargs)

    def get_device_property_names(self, **kwargs):
        return self.call('get_device_property_names', kwargs=kwargs)

    def get_device_type(self, **kwargs):
        return self.call('get_device_type', kwargs=kwargs)

    def get_exposure(self, **kwargs):
        return self.call('get_exposure', kwargs=kwargs)

    def get_exposure_sequence_max_length(self, **kwargs):
        return self.call('get_exposure_sequence_max_length', kwargs=kwargs)

    def get_focus_device(self, **kwargs):
        return self.call('get_focus_device', kwargs=kwargs)

    def get_focus_direction(self, **kwargs):
        return self.call('get_focus_direction', kwargs=kwargs)

    def get_galvo_channel(self, **kwargs):
        return self.call('get_galvo_channel', kwargs=kwargs)

    def get_galvo_device(self, **kwargs):
        return self.call('get_galvo_device', kwargs=kwargs)

    def get_galvo_position(self, **kwargs):
        return self.call('get_galvo_position', kwargs=kwargs)

    def get_galvo_x_minimum(self, **kwargs):
        return self.call('get_galvo_x_minimum', kwargs=kwargs)

    def get_galvo_x_range(self, **kwargs):
        return self.call('get_galvo_x_range', kwargs=kwargs)

    def get_galvo_y_minimum(self, **kwargs):
        return self.call('get_galvo_y_minimum', kwargs=kwargs)

    def get_galvo_y_range(self, **kwargs):
        return self.call('get_galvo_y_range', kwargs=kwargs)

    def get_image(self, **kwargs):
        return self.call('get_image', kwargs=kwargs)

    def get_image_bit_depth(self, **kwargs):
        return self.call('get_image_bit_depth', kwargs=kwargs)

    def get_image_buffer_size(self, **kwargs):
        return self.call('get_image_buffer_size', kwargs=kwargs)

    def get_image_height(self, **kwargs):
        return self.call('get_image_height', kwargs=kwargs)

    def get_image_processor_device(self, **kwargs):
        return self.call('get_image_processor_device', kwargs=kwargs)

    def get_image_width(self, **kwargs):
        return self.call('get_image_width', kwargs=kwargs)

    def get_installed_device_description(self, **kwargs):
        return self.call('get_installed_device_description', kwargs=kwargs)

    def get_installed_devices(self, **kwargs):
        return self.call('get_installed_devices', kwargs=kwargs)

    def get_last_focus_score(self, **kwargs):
        return self.call('get_last_focus_score', kwargs=kwargs)

    def get_last_image(self, **kwargs):
        return self.call('get_last_image', kwargs=kwargs)

    def get_last_image_md(self, **kwargs):
        return self.call('get_last_image_md', kwargs=kwargs)

    def get_last_tagged_image(self, **kwargs):
        return self.call('get_last_tagged_image', kwargs=kwargs)

    def get_loaded_devices(self, **kwargs):
        return self.call('get_loaded_devices', kwargs=kwargs)

    def get_loaded_devices_of_type(self, **kwargs):
        return self.call('get_loaded_devices_of_type', kwargs=kwargs)

    def get_loaded_peripheral_devices(self, **kwargs):
        return self.call('get_loaded_peripheral_devices', kwargs=kwargs)

    def get_magnification_factor(self, **kwargs):
        return self.call('get_magnification_factor', kwargs=kwargs)

    def get_multi_roi(self, **kwargs):
        return self.call('get_multi_roi', kwargs=kwargs)

    def get_n_before_last_image_md(self, **kwargs):
        return self.call('get_n_before_last_image_md', kwargs=kwargs)

    def get_n_before_last_tagged_image(self, **kwargs):
        return self.call('get_n_before_last_tagged_image', kwargs=kwargs)

    def get_number_of_camera_channels(self, **kwargs):
        return self.call('get_number_of_camera_channels', kwargs=kwargs)

    def get_number_of_components(self, **kwargs):
        return self.call('get_number_of_components', kwargs=kwargs)

    def get_number_of_galvo_polygons(self, **kwargs):
        return self.call('get_number_of_galvo_polygons', kwargs=kwargs)

    def get_number_of_states(self, **kwargs):
        return self.call('get_number_of_states', kwargs=kwargs)

    def get_parent_label(self, **kwargs):
        return self.call('get_parent_label', kwargs=kwargs)

    def get_pixel_size_affine(self, **kwargs):
        return self.call('get_pixel_size_affine', kwargs=kwargs)

    def get_pixel_size_affine_as_string(self, **kwargs):
        return self.call('get_pixel_size_affine_as_string', kwargs=kwargs)

    def get_pixel_size_affine_by_id(self, **kwargs):
        return self.call('get_pixel_size_affine_by_id', kwargs=kwargs)

    def get_pixel_size_config_data(self, **kwargs):
        return self.call('get_pixel_size_config_data', kwargs=kwargs)

    def get_pixel_size_um(self, **kwargs):
        return self.call('get_pixel_size_um', kwargs=kwargs)

    def get_pixel_size_um_by_id(self, **kwargs):
        return self.call('get_pixel_size_um_by_id', kwargs=kwargs)

    def get_position(self, **kwargs):
        return self.call('get_position', kwargs=kwargs)

    def get_primary_log_file(self, **kwargs):
        return self.call('get_primary_log_file', kwargs=kwargs)

    def get_property(self, **kwargs):
        return self.call('get_property', kwargs=kwargs)

    def get_property_from_cache(self, **kwargs):
        return self.call('get_property_from_cache', kwargs=kwargs)

    def get_property_lower_limit(self, **kwargs):
        return self.call('get_property_lower_limit', kwargs=kwargs)

    def get_property_sequence_max_length(self, **kwargs):
        return self.call('get_property_sequence_max_length', kwargs=kwargs)

    def get_property_type(self, **kwargs):
        return self.call('get_property_type', kwargs=kwargs)

    def get_property_upper_limit(self, **kwargs):
        return self.call('get_property_upper_limit', kwargs=kwargs)

    def get_property_limits(self, **kwargs):
        return self.call('get_property_limits', kwargs=kwargs)

    def get_remaining_image_count(self, **kwargs):
        return self.call('get_remaining_image_count', kwargs=kwargs)

    def get_roi(self, **kwargs):
        return self.call('get_roi', kwargs=kwargs)

    def get_serial_port_answer(self, **kwargs):
        return self.call('get_serial_port_answer', kwargs=kwargs)

    def get_shutter_device(self, **kwargs):
        return self.call('get_shutter_device', kwargs=kwargs)

    def get_shutter_open(self, **kwargs):
        return self.call('get_shutter_open', kwargs=kwargs)

    def get_slm_bytes_per_pixel(self, **kwargs):
        return self.call('get_slm_bytes_per_pixel', kwargs=kwargs)

    def get_slm_device(self, **kwargs):
        return self.call('get_slm_device', kwargs=kwargs)

    def get_slm_exposure(self, **kwargs):
        return self.call('get_slm_exposure', kwargs=kwargs)

    def get_slm_height(self, **kwargs):
        return self.call('get_slm_height', kwargs=kwargs)

    def get_slm_number_of_components(self, **kwargs):
        return self.call('get_slm_number_of_components', kwargs=kwargs)

    def get_slm_sequence_max_length(self, **kwargs):
        return self.call('get_slm_sequence_max_length', kwargs=kwargs)

    def get_slm_width(self, **kwargs):
        return self.call('get_slm_width', kwargs=kwargs)

    def get_stage_sequence_max_length(self, **kwargs):
        return self.call('get_stage_sequence_max_length', kwargs=kwargs)

    def get_state(self, **kwargs):
        return self.call('get_state', kwargs=kwargs)

    def get_state_from_label(self, **kwargs):
        return self.call('get_state_from_label', kwargs=kwargs)

    def get_state_label(self, **kwargs):
        return self.call('get_state_label', kwargs=kwargs)

    def get_state_labels(self, **kwargs):
        return self.call('get_state_labels', kwargs=kwargs)

    def get_system_state(self, **kwargs):
        return self.call('get_system_state', kwargs=kwargs)

    def get_system_state_cache(self, **kwargs):
        return self.call('get_system_state_cache', kwargs=kwargs)

    def get_tagged_image(self, **kwargs):
        return self.call('get_tagged_image', kwargs=kwargs)

    def get_timeout_ms(self, **kwargs):
        return self.call('get_timeout_ms', kwargs=kwargs)

    def get_version_info(self, **kwargs):
        return self.call('get_version_info', kwargs=kwargs)

    def get_x_position(self, **kwargs):
        return self.call('get_x_position', kwargs=kwargs)

    def get_xy_position(self, **kwargs):
        return self.call('get_xy_position', kwargs=kwargs)

    def get_xy_stage_device(self, **kwargs):
        return self.call('get_xy_stage_device', kwargs=kwargs)

    def get_xy_stage_position(self, **kwargs):
        return self.call('get_xy_stage_position', kwargs=kwargs)

    def get_xy_stage_sequence_max_length(self, **kwargs):
        return self.call('get_xy_stage_sequence_max_length', kwargs=kwargs)

    def get_y_position(self, **kwargs):
        return self.call('get_y_position', kwargs=kwargs)

    def has_property(self, **kwargs):
        return self.call('has_property', kwargs=kwargs)

    def has_property_limits(self, **kwargs):
        return self.call('has_property_limits', kwargs=kwargs)

    def home(self, **kwargs):
        return self.call('home', kwargs=kwargs)

    def incremental_focus(self, **kwargs):
        return self.call('incremental_focus', kwargs=kwargs)

    def initialize_all_devices(self, **kwargs):
        return self.call('initialize_all_devices', kwargs=kwargs)

    def initialize_circular_buffer(self, **kwargs):
        return self.call('initialize_circular_buffer', kwargs=kwargs)

    def initialize_device(self, **kwargs):
        return self.call('initialize_device', kwargs=kwargs)

    def is_buffer_overflowed(self, **kwargs):
        return self.call('is_buffer_overflowed', kwargs=kwargs)

    def is_config_defined(self, **kwargs):
        return self.call('is_config_defined', kwargs=kwargs)

    def is_continuous_focus_drive(self, **kwargs):
        return self.call('is_continuous_focus_drive', kwargs=kwargs)

    def is_continuous_focus_enabled(self, **kwargs):
        return self.call('is_continuous_focus_enabled', kwargs=kwargs)

    def is_continuous_focus_locked(self, **kwargs):
        return self.call('is_continuous_focus_locked', kwargs=kwargs)

    def is_exposure_sequenceable(self, **kwargs):
        return self.call('is_exposure_sequenceable', kwargs=kwargs)

    def is_group_defined(self, **kwargs):
        return self.call('is_group_defined', kwargs=kwargs)

    def is_multi_roi_enabled(self, **kwargs):
        return self.call('is_multi_roi_enabled', kwargs=kwargs)

    def is_multi_roi_supported(self, **kwargs):
        return self.call('is_multi_roi_supported', kwargs=kwargs)

    def is_pixel_size_config_defined(self, **kwargs):
        return self.call('is_pixel_size_config_defined', kwargs=kwargs)

    def is_property_pre_init(self, **kwargs):
        return self.call('is_property_pre_init', kwargs=kwargs)

    def is_property_read_only(self, **kwargs):
        return self.call('is_property_read_only', kwargs=kwargs)

    def is_property_sequenceable(self, **kwargs):
        return self.call('is_property_sequenceable', kwargs=kwargs)

    def is_sequence_running(self, **kwargs):
        return self.call('is_sequence_running', kwargs=kwargs)

    def is_stage_linear_sequenceable(self, **kwargs):
        return self.call('is_stage_linear_sequenceable', kwargs=kwargs)

    def is_stage_sequenceable(self, **kwargs):
        return self.call('is_stage_sequenceable', kwargs=kwargs)

    def is_xy_stage_sequenceable(self, **kwargs):
        return self.call('is_xy_stage_sequenceable', kwargs=kwargs)

    def load_device(self, **kwargs):
        return self.call('load_device', kwargs=kwargs)

    def load_exposure_sequence(self, **kwargs):
        return self.call('load_exposure_sequence', kwargs=kwargs)

    def load_galvo_polygons(self, **kwargs):
        return self.call('load_galvo_polygons', kwargs=kwargs)

    def load_property_sequence(self, **kwargs):
        return self.call('load_property_sequence', kwargs=kwargs)

    def load_slm_sequence(self, **kwargs):
        return self.call('load_slm_sequence', kwargs=kwargs)

    def load_stage_sequence(self, **kwargs):
        return self.call('load_stage_sequence', kwargs=kwargs)

    def load_system_configuration(self, **kwargs):
        return self.call('load_system_configuration', kwargs=kwargs)

    def load_system_state(self, **kwargs):
        return self.call('load_system_state', kwargs=kwargs)

    def load_xy_stage_sequence(self, **kwargs):
        return self.call('load_xy_stage_sequence', kwargs=kwargs)

    def log_message(self, **kwargs):
        return self.call('log_message', kwargs=kwargs)

    def point_galvo_and_fire(self, **kwargs):
        return self.call('point_galvo_and_fire', kwargs=kwargs)

    def pop_next_image(self, **kwargs):
        return self.call('pop_next_image', kwargs=kwargs)

    def pop_next_image_md(self, **kwargs):
        return self.call('pop_next_image_md', kwargs=kwargs)

    def pop_next_tagged_image(self, **kwargs):
        return self.call('pop_next_tagged_image', kwargs=kwargs)

    def prepare_sequence_acquisition(self, **kwargs):
        return self.call('prepare_sequence_acquisition', kwargs=kwargs)

    def read_from_serial_port(self, **kwargs):
        return self.call('read_from_serial_port', kwargs=kwargs)

    def register_callback(self, **kwargs):
        return self.call('register_callback', kwargs=kwargs)

    def rename_config(self, **kwargs):
        return self.call('rename_config', kwargs=kwargs)

    def rename_config_group(self, **kwargs):
        return self.call('rename_config_group', kwargs=kwargs)

    def rename_pixel_size_config(self, **kwargs):
        return self.call('rename_pixel_size_config', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def run_galvo_polygons(self, **kwargs):
        return self.call('run_galvo_polygons', kwargs=kwargs)

    def run_galvo_sequence(self, **kwargs):
        return self.call('run_galvo_sequence', kwargs=kwargs)

    def save_system_configuration(self, **kwargs):
        return self.call('save_system_configuration', kwargs=kwargs)

    def save_system_state(self, **kwargs):
        return self.call('save_system_state', kwargs=kwargs)

    def set_adapter_origin(self, **kwargs):
        return self.call('set_adapter_origin', kwargs=kwargs)

    def set_adapter_origin_xy(self, **kwargs):
        return self.call('set_adapter_origin_xy', kwargs=kwargs)

    def set_auto_focus_device(self, **kwargs):
        return self.call('set_auto_focus_device', kwargs=kwargs)

    def set_auto_focus_offset(self, **kwargs):
        return self.call('set_auto_focus_offset', kwargs=kwargs)

    def set_auto_shutter(self, **kwargs):
        return self.call('set_auto_shutter', kwargs=kwargs)

    def set_camera_device(self, **kwargs):
        return self.call('set_camera_device', kwargs=kwargs)

    def set_channel_group(self, **kwargs):
        return self.call('set_channel_group', kwargs=kwargs)

    def set_circular_buffer_memory_footprint(self, **kwargs):
        return self.call('set_circular_buffer_memory_footprint', kwargs=kwargs)

    def set_config(self, **kwargs):
        return self.call('set_config', kwargs=kwargs)

    def set_device_adapter_search_paths(self, **kwargs):
        return self.call('set_device_adapter_search_paths', kwargs=kwargs)

    def set_device_delay_ms(self, **kwargs):
        return self.call('set_device_delay_ms', kwargs=kwargs)

    def set_exposure(self, **kwargs):
        return self.call('set_exposure', kwargs=kwargs)

    def set_focus_device(self, **kwargs):
        return self.call('set_focus_device', kwargs=kwargs)

    def set_focus_direction(self, **kwargs):
        return self.call('set_focus_direction', kwargs=kwargs)

    def set_galvo_device(self, **kwargs):
        return self.call('set_galvo_device', kwargs=kwargs)

    def set_galvo_illumination_state(self, **kwargs):
        return self.call('set_galvo_illumination_state', kwargs=kwargs)

    def set_galvo_polygon_repetitions(self, **kwargs):
        return self.call('set_galvo_polygon_repetitions', kwargs=kwargs)

    def set_galvo_position(self, **kwargs):
        return self.call('set_galvo_position', kwargs=kwargs)

    def set_galvo_spot_interval(self, **kwargs):
        return self.call('set_galvo_spot_interval', kwargs=kwargs)

    def set_image_processor_device(self, **kwargs):
        return self.call('set_image_processor_device', kwargs=kwargs)

    def set_metadata_profile(self, **kwargs):
        return self.call('set_metadata_profile', kwargs=kwargs)

    def set_multi_roi(self, **kwargs):
        return self.call('set_multi_roi', kwargs=kwargs)

    def set_origin(self, **kwargs):
        return self.call('set_origin', kwargs=kwargs)

    def set_origin_x(self, **kwargs):
        return self.call('set_origin_x', kwargs=kwargs)

    def set_origin_xy(self, **kwargs):
        return self.call('set_origin_xy', kwargs=kwargs)

    def set_origin_y(self, **kwargs):
        return self.call('set_origin_y', kwargs=kwargs)

    def set_parent_label(self, **kwargs):
        return self.call('set_parent_label', kwargs=kwargs)

    def set_pixel_size_affine(self, **kwargs):
        return self.call('set_pixel_size_affine', kwargs=kwargs)

    def set_pixel_size_config(self, **kwargs):
        return self.call('set_pixel_size_config', kwargs=kwargs)

    def set_pixel_size_um(self, **kwargs):
        return self.call('set_pixel_size_um', kwargs=kwargs)

    def set_position(self, **kwargs):
        return self.call('set_position', kwargs=kwargs)

    def set_primary_log_file(self, **kwargs):
        return self.call('set_primary_log_file', kwargs=kwargs)

    def set_property(self, **kwargs):
        return self.call('set_property', kwargs=kwargs)

    def set_relative_position(self, **kwargs):
        return self.call('set_relative_position', kwargs=kwargs)

    def set_relative_xy_position(self, **kwargs):
        return self.call('set_relative_xy_position', kwargs=kwargs)

    def set_roi(self, **kwargs):
        return self.call('set_roi', kwargs=kwargs)

    def set_shutter_device(self, **kwargs):
        return self.call('set_shutter_device', kwargs=kwargs)

    def set_shutter_open(self, **kwargs):
        return self.call('set_shutter_open', kwargs=kwargs)

    def set_slm_device(self, **kwargs):
        return self.call('set_slm_device', kwargs=kwargs)

    def set_slm_exposure(self, **kwargs):
        return self.call('set_slm_exposure', kwargs=kwargs)

    def set_slm_image(self, **kwargs):
        return self.call('set_slm_image', kwargs=kwargs)

    def set_slm_pixels_to(self, **kwargs):
        return self.call('set_slm_pixels_to', kwargs=kwargs)

    def set_stage_linear_sequence(self, **kwargs):
        return self.call('set_stage_linear_sequence', kwargs=kwargs)

    def set_state(self, **kwargs):
        return self.call('set_state', kwargs=kwargs)

    def set_state_label(self, **kwargs):
        return self.call('set_state_label', kwargs=kwargs)

    def set_system_state(self, **kwargs):
        return self.call('set_system_state', kwargs=kwargs)

    def set_timeout_ms(self, **kwargs):
        return self.call('set_timeout_ms', kwargs=kwargs)

    def set_xy_position(self, **kwargs):
        return self.call('set_xy_position', kwargs=kwargs)

    def set_xy_stage_device(self, **kwargs):
        return self.call('set_xy_stage_device', kwargs=kwargs)

    def sleep(self, **kwargs):
        return self.call('sleep', kwargs=kwargs)

    def snap_image(self, **kwargs):
        return self.call('snap_image', kwargs=kwargs)

    def start_continuous_sequence_acquisition(self, **kwargs):
        return self.call('start_continuous_sequence_acquisition', kwargs=kwargs)

    def start_exposure_sequence(self, **kwargs):
        return self.call('start_exposure_sequence', kwargs=kwargs)

    def start_property_sequence(self, **kwargs):
        return self.call('start_property_sequence', kwargs=kwargs)

    def start_secondary_log_file(self, **kwargs):
        return self.call('start_secondary_log_file', kwargs=kwargs)

    def start_sequence_acquisition(self, **kwargs):
        return self.call('start_sequence_acquisition', kwargs=kwargs)

    def start_slm_sequence(self, **kwargs):
        return self.call('start_slm_sequence', kwargs=kwargs)

    def start_stage_sequence(self, **kwargs):
        return self.call('start_stage_sequence', kwargs=kwargs)

    def start_xy_stage_sequence(self, **kwargs):
        return self.call('start_xy_stage_sequence', kwargs=kwargs)

    def stderr_log_enabled(self, **kwargs):
        return self.call('stderr_log_enabled', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def stop_exposure_sequence(self, **kwargs):
        return self.call('stop_exposure_sequence', kwargs=kwargs)

    def stop_property_sequence(self, **kwargs):
        return self.call('stop_property_sequence', kwargs=kwargs)

    def stop_secondary_log_file(self, **kwargs):
        return self.call('stop_secondary_log_file', kwargs=kwargs)

    def stop_sequence_acquisition(self, **kwargs):
        return self.call('stop_sequence_acquisition', kwargs=kwargs)

    def stop_slm_sequence(self, **kwargs):
        return self.call('stop_slm_sequence', kwargs=kwargs)

    def stop_stage_sequence(self, **kwargs):
        return self.call('stop_stage_sequence', kwargs=kwargs)

    def stop_xy_stage_sequence(self, **kwargs):
        return self.call('stop_xy_stage_sequence', kwargs=kwargs)

    def supports_device_detection(self, **kwargs):
        return self.call('supports_device_detection', kwargs=kwargs)

    def system_busy(self, **kwargs):
        return self.call('system_busy', kwargs=kwargs)

    def unload_all_devices(self, **kwargs):
        return self.call('unload_all_devices', kwargs=kwargs)

    def unload_device(self, **kwargs):
        return self.call('unload_device', kwargs=kwargs)

    def unload_library(self, **kwargs):
        return self.call('unload_library', kwargs=kwargs)

    def update_core_properties(self, **kwargs):
        return self.call('update_core_properties', kwargs=kwargs)

    def update_system_state_cache(self, **kwargs):
        return self.call('update_system_state_cache', kwargs=kwargs)

    def uses_device_delay(self, **kwargs):
        return self.call('uses_device_delay', kwargs=kwargs)

    def wait_for_config(self, **kwargs):
        return self.call('wait_for_config', kwargs=kwargs)

    def wait_for_device(self, **kwargs):
        return self.call('wait_for_device', kwargs=kwargs)

    def wait_for_device_type(self, **kwargs):
        return self.call('wait_for_device_type', kwargs=kwargs)

    def wait_for_system(self, **kwargs):
        return self.call('wait_for_system', kwargs=kwargs)

