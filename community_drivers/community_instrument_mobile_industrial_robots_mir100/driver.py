from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMobileIndustrialRobotsMir100(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/osrf__mir100-client', 'source_file': 'mir100_client/api/default_api.py', 'class_name': 'DefaultApi', 'import_roots': [], 'candidate_methods': ['actions_action_type_get', 'actions_action_type_get_with_http_info', 'actions_action_type_post', 'actions_action_type_post_with_http_info', 'actions_get', 'actions_get_with_http_info', 'area_events_action_definitions_action_type_get', 'area_events_action_definitions_action_type_get_with_http_info', 'area_events_action_definitions_get', 'area_events_action_definitions_get_with_http_info', 'area_events_definitions_get', 'area_events_definitions_get_with_http_info', 'area_events_get', 'area_events_get_with_http_info', 'area_events_guid_delete', 'area_events_guid_delete_with_http_info', 'area_events_guid_get', 'area_events_guid_get_with_http_info', 'area_events_guid_put', 'area_events_guid_put_with_http_info', 'area_events_post', 'area_events_post_with_http_info', 'bluetooth_delete', 'bluetooth_delete_with_http_info', 'bluetooth_get', 'bluetooth_get_with_http_info', 'bluetooth_post', 'bluetooth_post_with_http_info', 'bluetooth_put', 'bluetooth_put_with_http_info', 'bluetooth_relays_get', 'bluetooth_relays_get_with_http_info', 'bluetooth_relays_guid_delete', 'bluetooth_relays_guid_delete_with_http_info', 'bluetooth_relays_guid_get', 'bluetooth_relays_guid_get_with_http_info', 'bluetooth_relays_guid_put', 'bluetooth_relays_guid_put_with_http_info', 'bluetooth_relays_post', 'bluetooth_relays_post_with_http_info', 'bluetooth_scan_get', 'bluetooth_scan_get_with_http_info', 'bluetooth_scan_post', 'bluetooth_scan_post_with_http_info', 'cart_calibrations_get', 'cart_calibrations_get_with_http_info', 'cart_calibrations_guid_delete', 'cart_calibrations_guid_delete_with_http_info', 'cart_calibrations_guid_get', 'cart_calibrations_guid_get_with_http_info', 'cart_calibrations_guid_put', 'cart_calibrations_guid_put_with_http_info', 'cart_calibrations_post', 'cart_calibrations_post_with_http_info', 'cart_types_get', 'cart_types_get_with_http_info', 'cart_types_guid_delete', 'cart_types_guid_delete_with_http_info', 'cart_types_guid_get', 'cart_types_guid_get_with_http_info', 'cart_types_guid_put', 'cart_types_guid_put_with_http_info', 'cart_types_post', 'cart_types_post_with_http_info', 'carts_get', 'carts_get_with_http_info', 'carts_guid_delete', 'carts_guid_delete_with_http_info', 'carts_guid_get', 'carts_guid_get_with_http_info', 'carts_guid_put', 'carts_guid_put_with_http_info', 'carts_post', 'carts_post_with_http_info', 'changes_me_delete', 'changes_me_delete_with_http_info', 'changes_me_get', 'changes_me_get_with_http_info', 'dashboards_dashboard_id_widgets_get', 'dashboards_dashboard_id_widgets_get_with_http_info', 'dashboards_dashboard_id_widgets_guid_delete', 'dashboards_dashboard_id_widgets_guid_delete_with_http_info', 'dashboards_dashboard_id_widgets_guid_get', 'dashboards_dashboard_id_widgets_guid_get_with_http_info', 'dashboards_dashboard_id_widgets_guid_put', 'dashboards_dashboard_id_widgets_guid_put_with_http_info', 'dashboards_dashboard_id_widgets_post', 'dashboards_dashboard_id_widgets_post_with_http_info', 'dashboards_get', 'dashboards_get_with_http_info', 'dashboards_guid_delete', 'dashboards_guid_delete_with_http_info', 'dashboards_guid_get', 'dashboards_guid_get_with_http_info', 'dashboards_guid_put', 'dashboards_guid_put_with_http_info', 'dashboards_post', 'dashboards_post_with_http_info', 'docking_offsets_get', 'docking_offsets_get_with_http_info', 'docking_offsets_guid_delete', 'docking_offsets_guid_delete_with_http_info', 'docking_offsets_guid_get', 'docking_offsets_guid_get_with_http_info', 'docking_offsets_guid_put', 'docking_offsets_guid_put_with_http_info', 'docking_offsets_post', 'docking_offsets_post_with_http_info', 'factory_reset_post', 'factory_reset_post_with_http_info', 'hook_brake_get', 'hook_brake_get_with_http_info', 'hook_brake_put', 'hook_brake_put_with_http_info', 'hook_gripper_get', 'hook_gripper_get_with_http_info', 'hook_gripper_put', 'hook_gripper_put_with_http_info', 'hook_height_get', 'hook_height_get_with_http_info', 'hook_height_put', 'hook_height_put_with_http_info', 'hook_status_get', 'hook_status_get_with_http_info', 'hw_export_get', 'hw_export_get_with_http_info', 'hw_import_post', 'hw_import_post_with_http_info', 'io_modules_get', 'io_modules_get_with_http_info', 'io_modules_guid_delete', 'io_modules_guid_delete_with_http_info', 'io_modules_guid_get', 'io_modules_guid_get_with_http_info', 'io_modules_guid_put', 'io_modules_guid_put_with_http_info', 'io_modules_guid_status_delete', 'io_modules_guid_status_delete_with_http_info', 'io_modules_guid_status_get', 'io_modules_guid_status_get_with_http_info', 'io_modules_guid_status_post', 'io_modules_guid_status_post_with_http_info', 'io_modules_guid_status_put', 'io_modules_guid_status_put_with_http_info', 'io_modules_post', 'io_modules_post_with_http_info', 'log_error_reports_delete', 'log_error_reports_delete_with_http_info', 'log_error_reports_get', 'log_error_reports_get_with_http_info', 'log_error_reports_id_delete', 'log_error_reports_id_delete_with_http_info', 'log_error_reports_id_download_get', 'log_error_reports_id_download_get_with_http_info', 'log_error_reports_id_get', 'log_error_reports_id_get_with_http_info', 'log_error_reports_post', 'log_error_reports_post_with_http_info', 'maps_get', 'maps_get_with_http_info', 'maps_guid_delete', 'maps_guid_delete_with_http_info', 'maps_guid_get', 'maps_guid_get_with_http_info', 'maps_guid_put', 'maps_guid_put_with_http_info', 'maps_map_id_area_events_get', 'maps_map_id_area_events_get_with_http_info', 'maps_map_id_path_guides_get', 'maps_map_id_path_guides_get_with_http_info', 'maps_map_id_paths_get', 'maps_map_id_paths_get_with_http_info', 'maps_map_id_positions_get', 'maps_map_id_positions_get_with_http_info', 'maps_post', 'maps_post_with_http_info', 'mission_groups_get', 'mission_groups_get_with_http_info', 'mission_groups_group_id_missions_get', 'mission_groups_group_id_missions_get_with_http_info', 'mission_groups_guid_delete', 'mission_groups_guid_delete_with_http_info', 'mission_groups_guid_get', 'mission_groups_guid_get_with_http_info', 'mission_groups_guid_put', 'mission_groups_guid_put_with_http_info', 'mission_groups_mission_group_id_actions_get', 'mission_groups_mission_group_id_actions_get_with_http_info', 'mission_groups_post', 'mission_groups_post_with_http_info', 'mission_queue_delete', 'mission_queue_delete_with_http_info', 'mission_queue_get', 'mission_queue_get_with_http_info', 'mission_queue_id_delete', 'mission_queue_id_delete_with_http_info', 'mission_queue_id_get', 'mission_queue_id_get_with_http_info', 'mission_queue_id_put', 'mission_queue_id_put_with_http_info', 'mission_queue_mission_queue_id_actions_get', 'mission_queue_mission_queue_id_actions_get_with_http_info', 'mission_queue_mission_queue_id_actions_id_get', 'mission_queue_mission_queue_id_actions_id_get_with_http_info', 'mission_queue_post', 'mission_queue_post_with_http_info', 'missions_get', 'missions_get_with_http_info', 'missions_guid_definition_get', 'missions_guid_definition_get_with_http_info', 'missions_guid_delete', 'missions_guid_delete_with_http_info', 'missions_guid_get', 'missions_guid_get_with_http_info', 'missions_guid_put', 'missions_guid_put_with_http_info', 'missions_mission_id_actions_get', 'missions_mission_id_actions_get_with_http_info', 'missions_mission_id_actions_guid_delete', 'missions_mission_id_actions_guid_delete_with_http_info', 'missions_mission_id_actions_guid_get', 'missions_mission_id_actions_guid_get_with_http_info', 'missions_mission_id_actions_guid_put', 'missions_mission_id_actions_guid_put_with_http_info', 'missions_mission_id_actions_post', 'missions_mission_id_actions_post_with_http_info', 'missions_post', 'missions_post_with_http_info', 'modbus_get', 'modbus_get_with_http_info', 'modbus_id_get', 'modbus_id_get_with_http_info', 'modbus_missions_get', 'modbus_missions_get_with_http_info', 'modbus_missions_guid_delete', 'modbus_missions_guid_delete_with_http_info', 'modbus_missions_guid_get', 'modbus_missions_guid_get_with_http_info', 'modbus_missions_guid_put', 'modbus_missions_guid_put_with_http_info', 'modbus_missions_post', 'modbus_missions_post_with_http_info', 'path_guides_get', 'path_guides_get_with_http_info', 'path_guides_guid_delete', 'path_guides_guid_delete_with_http_info', 'path_guides_guid_get', 'path_guides_guid_get_with_http_info', 'path_guides_guid_put', 'path_guides_guid_put_with_http_info', 'path_guides_path_guide_guid_options_get', 'path_guides_path_guide_guid_options_get_with_http_info', 'path_guides_path_guide_guid_positions_get', 'path_guides_path_guide_guid_positions_get_with_http_info', 'path_guides_path_guide_guid_positions_guid_delete', 'path_guides_path_guide_guid_positions_guid_delete_with_http_info', 'path_guides_path_guide_guid_positions_guid_get', 'path_guides_path_guide_guid_positions_guid_get_with_http_info', 'path_guides_path_guide_guid_positions_guid_put', 'path_guides_path_guide_guid_positions_guid_put_with_http_info', 'path_guides_path_guide_guid_positions_post', 'path_guides_path_guide_guid_positions_post_with_http_info', 'path_guides_positions_get', 'path_guides_positions_get_with_http_info', 'path_guides_positions_guid_delete', 'path_guides_positions_guid_delete_with_http_info', 'path_guides_positions_guid_get', 'path_guides_positions_guid_get_with_http_info', 'path_guides_positions_guid_put', 'path_guides_positions_guid_put_with_http_info', 'path_guides_positions_post', 'path_guides_positions_post_with_http_info', 'path_guides_post', 'path_guides_post_with_http_info', 'path_guides_precalc_get', 'path_guides_precalc_get_with_http_info', 'path_guides_precalc_post', 'path_guides_precalc_post_with_http_info', 'paths_get', 'paths_get_with_http_info', 'paths_guid_delete', 'paths_guid_delete_with_http_info', 'paths_guid_get', 'paths_guid_get_with_http_info', 'paths_guid_put', 'paths_guid_put_with_http_info', 'paths_post', 'paths_post_with_http_info', 'permissions_guid_delete', 'permissions_guid_delete_with_http_info', 'permissions_guid_get', 'permissions_guid_get_with_http_info', 'permissions_guid_put', 'permissions_guid_put_with_http_info', 'position_transition_lists_get', 'position_transition_lists_get_with_http_info', 'position_transition_lists_guid_delete', 'position_transition_lists_guid_delete_with_http_info', 'position_transition_lists_guid_get', 'position_transition_lists_guid_get_with_http_info', 'position_transition_lists_guid_put', 'position_transition_lists_guid_put_with_http_info', 'position_transition_lists_post', 'position_transition_lists_post_with_http_info', 'position_types_get', 'position_types_get_with_http_info', 'position_types_id_get', 'position_types_id_get_with_http_info', 'positions_get', 'positions_get_with_http_info', 'positions_guid_delete', 'positions_guid_delete_with_http_info', 'positions_guid_get', 'positions_guid_get_with_http_info', 'positions_guid_put', 'positions_guid_put_with_http_info', 'positions_parent_guid_helper_positions_get', 'positions_parent_guid_helper_positions_get_with_http_info', 'positions_pos_id_docking_offsets_get', 'positions_pos_id_docking_offsets_get_with_http_info', 'positions_post', 'positions_post_with_http_info', 'registers_get', 'registers_get_with_http_info', 'registers_id_get', 'registers_id_get_with_http_info', 'registers_id_post', 'registers_id_post_with_http_info', 'registers_id_put', 'registers_id_put_with_http_info', 'remote_support_get', 'remote_support_get_with_http_info', 'remote_support_log_get', 'remote_support_log_get_with_http_info', 'remote_support_put', 'remote_support_put_with_http_info', 'robots_post', 'robots_post_with_http_info', 'service_book_get', 'service_book_get_with_http_info', 'service_book_guid_delete', 'service_book_guid_delete_with_http_info', 'service_book_guid_get', 'service_book_guid_get_with_http_info', 'service_book_post', 'service_book_post_with_http_info', 'sessions_get', 'sessions_get_with_http_info', 'sessions_guid_delete', 'sessions_guid_delete_with_http_info', 'sessions_guid_export_get', 'sessions_guid_export_get_with_http_info', 'sessions_guid_get', 'sessions_guid_get_with_http_info', 'sessions_guid_put', 'sessions_guid_put_with_http_info', 'sessions_import_delete', 'sessions_import_delete_with_http_info', 'sessions_import_get', 'sessions_import_get_with_http_info', 'sessions_import_post', 'sessions_import_post_with_http_info', 'sessions_post', 'sessions_post_with_http_info', 'sessions_session_id_maps_get', 'sessions_session_id_maps_get_with_http_info', 'sessions_session_id_missions_get', 'sessions_session_id_missions_get_with_http_info', 'sessions_session_id_position_transition_lists_get', 'sessions_session_id_position_transition_lists_get_with_http_info', 'setting_groups_get', 'setting_groups_get_with_http_info', 'setting_groups_id_get', 'setting_groups_id_get_with_http_info', 'setting_groups_settings_group_id_settings_advanced_get', 'setting_groups_settings_group_id_settings_advanced_get_with_http_info', 'setting_groups_settings_group_id_settings_get', 'setting_groups_settings_group_id_settings_get_with_http_info', 'settings_advanced_get', 'settings_advanced_get_with_http_info', 'settings_advanced_id_get', 'settings_advanced_id_get_with_http_info', 'settings_advanced_id_put', 'settings_advanced_id_put_with_http_info', 'settings_get', 'settings_get_with_http_info', 'settings_id_get', 'settings_id_get_with_http_info', 'settings_id_put', 'settings_id_put_with_http_info', 'shelf_types_get', 'shelf_types_get_with_http_info', 'shelf_types_guid_delete', 'shelf_types_guid_delete_with_http_info', 'shelf_types_guid_get', 'shelf_types_guid_get_with_http_info', 'shelf_types_guid_put', 'shelf_types_guid_put_with_http_info', 'shelf_types_post', 'shelf_types_post_with_http_info', 'software_backups_get', 'software_backups_get_with_http_info', 'software_backups_guid_delete', 'software_backups_guid_delete_with_http_info', 'software_backups_guid_get', 'software_backups_guid_get_with_http_info', 'software_backups_guid_post', 'software_backups_guid_post_with_http_info', 'software_backups_post', 'software_backups_post_with_http_info', 'software_lock_get', 'software_lock_get_with_http_info', 'software_lock_put', 'software_lock_put_with_http_info', 'software_logs_get', 'software_logs_get_with_http_info', 'software_logs_guid_get', 'software_logs_guid_get_with_http_info', 'software_upgrades_get', 'software_upgrades_get_with_http_info', 'software_upgrades_guid_delete', 'software_upgrades_guid_delete_with_http_info', 'software_upgrades_guid_get', 'software_upgrades_guid_get_with_http_info', 'software_upgrades_guid_post', 'software_upgrades_guid_post_with_http_info', 'software_upgrades_post', 'software_upgrades_post_with_http_info', 'sounds_get', 'sounds_get_with_http_info', 'sounds_guid_delete', 'sounds_guid_delete_with_http_info', 'sounds_guid_get', 'sounds_guid_get_with_http_info', 'sounds_guid_put', 'sounds_guid_put_with_http_info', 'sounds_guid_stream_get', 'sounds_guid_stream_get_with_http_info', 'sounds_post', 'sounds_post_with_http_info', 'statistics_distance_get', 'statistics_distance_get_with_http_info', 'status_get', 'status_get_with_http_info', 'status_put', 'status_put_with_http_info', 'system_info_get', 'system_info_get_with_http_info', 'user_groups_get', 'user_groups_get_with_http_info', 'user_groups_guid_delete', 'user_groups_guid_delete_with_http_info', 'user_groups_guid_get', 'user_groups_guid_get_with_http_info', 'user_groups_guid_put', 'user_groups_guid_put_with_http_info', 'user_groups_post', 'user_groups_post_with_http_info', 'user_groups_user_group_guid_permissions_get', 'user_groups_user_group_guid_permissions_get_with_http_info', 'user_groups_user_group_guid_permissions_post', 'user_groups_user_group_guid_permissions_post_with_http_info', 'users_auth_delete', 'users_auth_delete_with_http_info', 'users_auth_post', 'users_auth_post_with_http_info', 'users_get', 'users_get_with_http_info', 'users_guid_delete', 'users_guid_delete_with_http_info', 'users_guid_get', 'users_guid_get_with_http_info', 'users_guid_put', 'users_guid_put_with_http_info', 'users_me_get', 'users_me_get_with_http_info', 'users_me_permissions_get', 'users_me_permissions_get_with_http_info', 'users_me_put', 'users_me_put_with_http_info', 'users_post', 'users_post_with_http_info', 'wifi_connections_get', 'wifi_connections_get_with_http_info', 'wifi_connections_post', 'wifi_connections_post_with_http_info', 'wifi_connections_uuid_delete', 'wifi_connections_uuid_delete_with_http_info', 'wifi_connections_uuid_get', 'wifi_connections_uuid_get_with_http_info', 'wifi_connections_uuid_post', 'wifi_connections_uuid_post_with_http_info', 'wifi_get', 'wifi_get_with_http_info', 'wifi_networks_get', 'wifi_networks_get_with_http_info', 'wifi_networks_guid_get', 'wifi_networks_guid_get_with_http_info', 'world_model_get', 'world_model_get_with_http_info', 'world_model_post', 'world_model_post_with_http_info'], 'action_targets': {}, 'metadata': {'repo': 'osrf/mir100-client', 'repo_url': 'https://github.com/osrf/mir100-client', 'brand': 'Mobile Industrial Robots', 'model': 'MiR100', 'device_type_cn': 'AGV自动导引车', 'device_type_en': 'AGV', 'source_framework': 'ROS/REST API', 'tag_id': '4360', 'tag_name': 'AGV', 'tag_name_en': 'AGV', 'candidate_score': 4082, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def actions_action_type_get(self, **kwargs):
        return self.call('actions_action_type_get', kwargs=kwargs)

    def actions_action_type_get_with_http_info(self, **kwargs):
        return self.call('actions_action_type_get_with_http_info', kwargs=kwargs)

    def actions_action_type_post(self, **kwargs):
        return self.call('actions_action_type_post', kwargs=kwargs)

    def actions_action_type_post_with_http_info(self, **kwargs):
        return self.call('actions_action_type_post_with_http_info', kwargs=kwargs)

    def actions_get(self, **kwargs):
        return self.call('actions_get', kwargs=kwargs)

    def actions_get_with_http_info(self, **kwargs):
        return self.call('actions_get_with_http_info', kwargs=kwargs)

    def area_events_action_definitions_action_type_get(self, **kwargs):
        return self.call('area_events_action_definitions_action_type_get', kwargs=kwargs)

    def area_events_action_definitions_action_type_get_with_http_info(self, **kwargs):
        return self.call('area_events_action_definitions_action_type_get_with_http_info', kwargs=kwargs)

    def area_events_action_definitions_get(self, **kwargs):
        return self.call('area_events_action_definitions_get', kwargs=kwargs)

    def area_events_action_definitions_get_with_http_info(self, **kwargs):
        return self.call('area_events_action_definitions_get_with_http_info', kwargs=kwargs)

    def area_events_definitions_get(self, **kwargs):
        return self.call('area_events_definitions_get', kwargs=kwargs)

    def area_events_definitions_get_with_http_info(self, **kwargs):
        return self.call('area_events_definitions_get_with_http_info', kwargs=kwargs)

    def area_events_get(self, **kwargs):
        return self.call('area_events_get', kwargs=kwargs)

    def area_events_get_with_http_info(self, **kwargs):
        return self.call('area_events_get_with_http_info', kwargs=kwargs)

    def area_events_guid_delete(self, **kwargs):
        return self.call('area_events_guid_delete', kwargs=kwargs)

    def area_events_guid_delete_with_http_info(self, **kwargs):
        return self.call('area_events_guid_delete_with_http_info', kwargs=kwargs)

    def area_events_guid_get(self, **kwargs):
        return self.call('area_events_guid_get', kwargs=kwargs)

    def area_events_guid_get_with_http_info(self, **kwargs):
        return self.call('area_events_guid_get_with_http_info', kwargs=kwargs)

    def area_events_guid_put(self, **kwargs):
        return self.call('area_events_guid_put', kwargs=kwargs)

    def area_events_guid_put_with_http_info(self, **kwargs):
        return self.call('area_events_guid_put_with_http_info', kwargs=kwargs)

    def area_events_post(self, **kwargs):
        return self.call('area_events_post', kwargs=kwargs)

    def area_events_post_with_http_info(self, **kwargs):
        return self.call('area_events_post_with_http_info', kwargs=kwargs)

    def bluetooth_delete(self, **kwargs):
        return self.call('bluetooth_delete', kwargs=kwargs)

    def bluetooth_delete_with_http_info(self, **kwargs):
        return self.call('bluetooth_delete_with_http_info', kwargs=kwargs)

    def bluetooth_get(self, **kwargs):
        return self.call('bluetooth_get', kwargs=kwargs)

    def bluetooth_get_with_http_info(self, **kwargs):
        return self.call('bluetooth_get_with_http_info', kwargs=kwargs)

    def bluetooth_post(self, **kwargs):
        return self.call('bluetooth_post', kwargs=kwargs)

    def bluetooth_post_with_http_info(self, **kwargs):
        return self.call('bluetooth_post_with_http_info', kwargs=kwargs)

    def bluetooth_put(self, **kwargs):
        return self.call('bluetooth_put', kwargs=kwargs)

    def bluetooth_put_with_http_info(self, **kwargs):
        return self.call('bluetooth_put_with_http_info', kwargs=kwargs)

    def bluetooth_relays_get(self, **kwargs):
        return self.call('bluetooth_relays_get', kwargs=kwargs)

    def bluetooth_relays_get_with_http_info(self, **kwargs):
        return self.call('bluetooth_relays_get_with_http_info', kwargs=kwargs)

    def bluetooth_relays_guid_delete(self, **kwargs):
        return self.call('bluetooth_relays_guid_delete', kwargs=kwargs)

    def bluetooth_relays_guid_delete_with_http_info(self, **kwargs):
        return self.call('bluetooth_relays_guid_delete_with_http_info', kwargs=kwargs)

    def bluetooth_relays_guid_get(self, **kwargs):
        return self.call('bluetooth_relays_guid_get', kwargs=kwargs)

    def bluetooth_relays_guid_get_with_http_info(self, **kwargs):
        return self.call('bluetooth_relays_guid_get_with_http_info', kwargs=kwargs)

    def bluetooth_relays_guid_put(self, **kwargs):
        return self.call('bluetooth_relays_guid_put', kwargs=kwargs)

    def bluetooth_relays_guid_put_with_http_info(self, **kwargs):
        return self.call('bluetooth_relays_guid_put_with_http_info', kwargs=kwargs)

    def bluetooth_relays_post(self, **kwargs):
        return self.call('bluetooth_relays_post', kwargs=kwargs)

    def bluetooth_relays_post_with_http_info(self, **kwargs):
        return self.call('bluetooth_relays_post_with_http_info', kwargs=kwargs)

    def bluetooth_scan_get(self, **kwargs):
        return self.call('bluetooth_scan_get', kwargs=kwargs)

    def bluetooth_scan_get_with_http_info(self, **kwargs):
        return self.call('bluetooth_scan_get_with_http_info', kwargs=kwargs)

    def bluetooth_scan_post(self, **kwargs):
        return self.call('bluetooth_scan_post', kwargs=kwargs)

    def bluetooth_scan_post_with_http_info(self, **kwargs):
        return self.call('bluetooth_scan_post_with_http_info', kwargs=kwargs)

    def cart_calibrations_get(self, **kwargs):
        return self.call('cart_calibrations_get', kwargs=kwargs)

    def cart_calibrations_get_with_http_info(self, **kwargs):
        return self.call('cart_calibrations_get_with_http_info', kwargs=kwargs)

    def cart_calibrations_guid_delete(self, **kwargs):
        return self.call('cart_calibrations_guid_delete', kwargs=kwargs)

    def cart_calibrations_guid_delete_with_http_info(self, **kwargs):
        return self.call('cart_calibrations_guid_delete_with_http_info', kwargs=kwargs)

    def cart_calibrations_guid_get(self, **kwargs):
        return self.call('cart_calibrations_guid_get', kwargs=kwargs)

    def cart_calibrations_guid_get_with_http_info(self, **kwargs):
        return self.call('cart_calibrations_guid_get_with_http_info', kwargs=kwargs)

    def cart_calibrations_guid_put(self, **kwargs):
        return self.call('cart_calibrations_guid_put', kwargs=kwargs)

    def cart_calibrations_guid_put_with_http_info(self, **kwargs):
        return self.call('cart_calibrations_guid_put_with_http_info', kwargs=kwargs)

    def cart_calibrations_post(self, **kwargs):
        return self.call('cart_calibrations_post', kwargs=kwargs)

    def cart_calibrations_post_with_http_info(self, **kwargs):
        return self.call('cart_calibrations_post_with_http_info', kwargs=kwargs)

    def cart_types_get(self, **kwargs):
        return self.call('cart_types_get', kwargs=kwargs)

    def cart_types_get_with_http_info(self, **kwargs):
        return self.call('cart_types_get_with_http_info', kwargs=kwargs)

    def cart_types_guid_delete(self, **kwargs):
        return self.call('cart_types_guid_delete', kwargs=kwargs)

    def cart_types_guid_delete_with_http_info(self, **kwargs):
        return self.call('cart_types_guid_delete_with_http_info', kwargs=kwargs)

    def cart_types_guid_get(self, **kwargs):
        return self.call('cart_types_guid_get', kwargs=kwargs)

    def cart_types_guid_get_with_http_info(self, **kwargs):
        return self.call('cart_types_guid_get_with_http_info', kwargs=kwargs)

    def cart_types_guid_put(self, **kwargs):
        return self.call('cart_types_guid_put', kwargs=kwargs)

    def cart_types_guid_put_with_http_info(self, **kwargs):
        return self.call('cart_types_guid_put_with_http_info', kwargs=kwargs)

    def cart_types_post(self, **kwargs):
        return self.call('cart_types_post', kwargs=kwargs)

    def cart_types_post_with_http_info(self, **kwargs):
        return self.call('cart_types_post_with_http_info', kwargs=kwargs)

    def carts_get(self, **kwargs):
        return self.call('carts_get', kwargs=kwargs)

    def carts_get_with_http_info(self, **kwargs):
        return self.call('carts_get_with_http_info', kwargs=kwargs)

    def carts_guid_delete(self, **kwargs):
        return self.call('carts_guid_delete', kwargs=kwargs)

    def carts_guid_delete_with_http_info(self, **kwargs):
        return self.call('carts_guid_delete_with_http_info', kwargs=kwargs)

    def carts_guid_get(self, **kwargs):
        return self.call('carts_guid_get', kwargs=kwargs)

    def carts_guid_get_with_http_info(self, **kwargs):
        return self.call('carts_guid_get_with_http_info', kwargs=kwargs)

    def carts_guid_put(self, **kwargs):
        return self.call('carts_guid_put', kwargs=kwargs)

    def carts_guid_put_with_http_info(self, **kwargs):
        return self.call('carts_guid_put_with_http_info', kwargs=kwargs)

    def carts_post(self, **kwargs):
        return self.call('carts_post', kwargs=kwargs)

    def carts_post_with_http_info(self, **kwargs):
        return self.call('carts_post_with_http_info', kwargs=kwargs)

    def changes_me_delete(self, **kwargs):
        return self.call('changes_me_delete', kwargs=kwargs)

    def changes_me_delete_with_http_info(self, **kwargs):
        return self.call('changes_me_delete_with_http_info', kwargs=kwargs)

    def changes_me_get(self, **kwargs):
        return self.call('changes_me_get', kwargs=kwargs)

    def changes_me_get_with_http_info(self, **kwargs):
        return self.call('changes_me_get_with_http_info', kwargs=kwargs)

    def dashboards_dashboard_id_widgets_get(self, **kwargs):
        return self.call('dashboards_dashboard_id_widgets_get', kwargs=kwargs)

    def dashboards_dashboard_id_widgets_get_with_http_info(self, **kwargs):
        return self.call('dashboards_dashboard_id_widgets_get_with_http_info', kwargs=kwargs)

    def dashboards_dashboard_id_widgets_guid_delete(self, **kwargs):
        return self.call('dashboards_dashboard_id_widgets_guid_delete', kwargs=kwargs)

    def dashboards_dashboard_id_widgets_guid_delete_with_http_info(self, **kwargs):
        return self.call('dashboards_dashboard_id_widgets_guid_delete_with_http_info', kwargs=kwargs)

    def dashboards_dashboard_id_widgets_guid_get(self, **kwargs):
        return self.call('dashboards_dashboard_id_widgets_guid_get', kwargs=kwargs)

    def dashboards_dashboard_id_widgets_guid_get_with_http_info(self, **kwargs):
        return self.call('dashboards_dashboard_id_widgets_guid_get_with_http_info', kwargs=kwargs)

    def dashboards_dashboard_id_widgets_guid_put(self, **kwargs):
        return self.call('dashboards_dashboard_id_widgets_guid_put', kwargs=kwargs)

    def dashboards_dashboard_id_widgets_guid_put_with_http_info(self, **kwargs):
        return self.call('dashboards_dashboard_id_widgets_guid_put_with_http_info', kwargs=kwargs)

    def dashboards_dashboard_id_widgets_post(self, **kwargs):
        return self.call('dashboards_dashboard_id_widgets_post', kwargs=kwargs)

    def dashboards_dashboard_id_widgets_post_with_http_info(self, **kwargs):
        return self.call('dashboards_dashboard_id_widgets_post_with_http_info', kwargs=kwargs)

    def dashboards_get(self, **kwargs):
        return self.call('dashboards_get', kwargs=kwargs)

    def dashboards_get_with_http_info(self, **kwargs):
        return self.call('dashboards_get_with_http_info', kwargs=kwargs)

    def dashboards_guid_delete(self, **kwargs):
        return self.call('dashboards_guid_delete', kwargs=kwargs)

    def dashboards_guid_delete_with_http_info(self, **kwargs):
        return self.call('dashboards_guid_delete_with_http_info', kwargs=kwargs)

    def dashboards_guid_get(self, **kwargs):
        return self.call('dashboards_guid_get', kwargs=kwargs)

    def dashboards_guid_get_with_http_info(self, **kwargs):
        return self.call('dashboards_guid_get_with_http_info', kwargs=kwargs)

    def dashboards_guid_put(self, **kwargs):
        return self.call('dashboards_guid_put', kwargs=kwargs)

    def dashboards_guid_put_with_http_info(self, **kwargs):
        return self.call('dashboards_guid_put_with_http_info', kwargs=kwargs)

    def dashboards_post(self, **kwargs):
        return self.call('dashboards_post', kwargs=kwargs)

    def dashboards_post_with_http_info(self, **kwargs):
        return self.call('dashboards_post_with_http_info', kwargs=kwargs)

    def docking_offsets_get(self, **kwargs):
        return self.call('docking_offsets_get', kwargs=kwargs)

    def docking_offsets_get_with_http_info(self, **kwargs):
        return self.call('docking_offsets_get_with_http_info', kwargs=kwargs)

    def docking_offsets_guid_delete(self, **kwargs):
        return self.call('docking_offsets_guid_delete', kwargs=kwargs)

    def docking_offsets_guid_delete_with_http_info(self, **kwargs):
        return self.call('docking_offsets_guid_delete_with_http_info', kwargs=kwargs)

    def docking_offsets_guid_get(self, **kwargs):
        return self.call('docking_offsets_guid_get', kwargs=kwargs)

    def docking_offsets_guid_get_with_http_info(self, **kwargs):
        return self.call('docking_offsets_guid_get_with_http_info', kwargs=kwargs)

    def docking_offsets_guid_put(self, **kwargs):
        return self.call('docking_offsets_guid_put', kwargs=kwargs)

    def docking_offsets_guid_put_with_http_info(self, **kwargs):
        return self.call('docking_offsets_guid_put_with_http_info', kwargs=kwargs)

    def docking_offsets_post(self, **kwargs):
        return self.call('docking_offsets_post', kwargs=kwargs)

    def docking_offsets_post_with_http_info(self, **kwargs):
        return self.call('docking_offsets_post_with_http_info', kwargs=kwargs)

    def factory_reset_post(self, **kwargs):
        return self.call('factory_reset_post', kwargs=kwargs)

    def factory_reset_post_with_http_info(self, **kwargs):
        return self.call('factory_reset_post_with_http_info', kwargs=kwargs)

    def hook_brake_get(self, **kwargs):
        return self.call('hook_brake_get', kwargs=kwargs)

    def hook_brake_get_with_http_info(self, **kwargs):
        return self.call('hook_brake_get_with_http_info', kwargs=kwargs)

    def hook_brake_put(self, **kwargs):
        return self.call('hook_brake_put', kwargs=kwargs)

    def hook_brake_put_with_http_info(self, **kwargs):
        return self.call('hook_brake_put_with_http_info', kwargs=kwargs)

    def hook_gripper_get(self, **kwargs):
        return self.call('hook_gripper_get', kwargs=kwargs)

    def hook_gripper_get_with_http_info(self, **kwargs):
        return self.call('hook_gripper_get_with_http_info', kwargs=kwargs)

    def hook_gripper_put(self, **kwargs):
        return self.call('hook_gripper_put', kwargs=kwargs)

    def hook_gripper_put_with_http_info(self, **kwargs):
        return self.call('hook_gripper_put_with_http_info', kwargs=kwargs)

    def hook_height_get(self, **kwargs):
        return self.call('hook_height_get', kwargs=kwargs)

    def hook_height_get_with_http_info(self, **kwargs):
        return self.call('hook_height_get_with_http_info', kwargs=kwargs)

    def hook_height_put(self, **kwargs):
        return self.call('hook_height_put', kwargs=kwargs)

    def hook_height_put_with_http_info(self, **kwargs):
        return self.call('hook_height_put_with_http_info', kwargs=kwargs)

    def hook_status_get(self, **kwargs):
        return self.call('hook_status_get', kwargs=kwargs)

    def hook_status_get_with_http_info(self, **kwargs):
        return self.call('hook_status_get_with_http_info', kwargs=kwargs)

    def hw_export_get(self, **kwargs):
        return self.call('hw_export_get', kwargs=kwargs)

    def hw_export_get_with_http_info(self, **kwargs):
        return self.call('hw_export_get_with_http_info', kwargs=kwargs)

    def hw_import_post(self, **kwargs):
        return self.call('hw_import_post', kwargs=kwargs)

    def hw_import_post_with_http_info(self, **kwargs):
        return self.call('hw_import_post_with_http_info', kwargs=kwargs)

    def io_modules_get(self, **kwargs):
        return self.call('io_modules_get', kwargs=kwargs)

    def io_modules_get_with_http_info(self, **kwargs):
        return self.call('io_modules_get_with_http_info', kwargs=kwargs)

    def io_modules_guid_delete(self, **kwargs):
        return self.call('io_modules_guid_delete', kwargs=kwargs)

    def io_modules_guid_delete_with_http_info(self, **kwargs):
        return self.call('io_modules_guid_delete_with_http_info', kwargs=kwargs)

    def io_modules_guid_get(self, **kwargs):
        return self.call('io_modules_guid_get', kwargs=kwargs)

    def io_modules_guid_get_with_http_info(self, **kwargs):
        return self.call('io_modules_guid_get_with_http_info', kwargs=kwargs)

    def io_modules_guid_put(self, **kwargs):
        return self.call('io_modules_guid_put', kwargs=kwargs)

    def io_modules_guid_put_with_http_info(self, **kwargs):
        return self.call('io_modules_guid_put_with_http_info', kwargs=kwargs)

    def io_modules_guid_status_delete(self, **kwargs):
        return self.call('io_modules_guid_status_delete', kwargs=kwargs)

    def io_modules_guid_status_delete_with_http_info(self, **kwargs):
        return self.call('io_modules_guid_status_delete_with_http_info', kwargs=kwargs)

    def io_modules_guid_status_get(self, **kwargs):
        return self.call('io_modules_guid_status_get', kwargs=kwargs)

    def io_modules_guid_status_get_with_http_info(self, **kwargs):
        return self.call('io_modules_guid_status_get_with_http_info', kwargs=kwargs)

    def io_modules_guid_status_post(self, **kwargs):
        return self.call('io_modules_guid_status_post', kwargs=kwargs)

    def io_modules_guid_status_post_with_http_info(self, **kwargs):
        return self.call('io_modules_guid_status_post_with_http_info', kwargs=kwargs)

    def io_modules_guid_status_put(self, **kwargs):
        return self.call('io_modules_guid_status_put', kwargs=kwargs)

    def io_modules_guid_status_put_with_http_info(self, **kwargs):
        return self.call('io_modules_guid_status_put_with_http_info', kwargs=kwargs)

    def io_modules_post(self, **kwargs):
        return self.call('io_modules_post', kwargs=kwargs)

    def io_modules_post_with_http_info(self, **kwargs):
        return self.call('io_modules_post_with_http_info', kwargs=kwargs)

    def log_error_reports_delete(self, **kwargs):
        return self.call('log_error_reports_delete', kwargs=kwargs)

    def log_error_reports_delete_with_http_info(self, **kwargs):
        return self.call('log_error_reports_delete_with_http_info', kwargs=kwargs)

    def log_error_reports_get(self, **kwargs):
        return self.call('log_error_reports_get', kwargs=kwargs)

    def log_error_reports_get_with_http_info(self, **kwargs):
        return self.call('log_error_reports_get_with_http_info', kwargs=kwargs)

    def log_error_reports_id_delete(self, **kwargs):
        return self.call('log_error_reports_id_delete', kwargs=kwargs)

    def log_error_reports_id_delete_with_http_info(self, **kwargs):
        return self.call('log_error_reports_id_delete_with_http_info', kwargs=kwargs)

    def log_error_reports_id_download_get(self, **kwargs):
        return self.call('log_error_reports_id_download_get', kwargs=kwargs)

    def log_error_reports_id_download_get_with_http_info(self, **kwargs):
        return self.call('log_error_reports_id_download_get_with_http_info', kwargs=kwargs)

    def log_error_reports_id_get(self, **kwargs):
        return self.call('log_error_reports_id_get', kwargs=kwargs)

    def log_error_reports_id_get_with_http_info(self, **kwargs):
        return self.call('log_error_reports_id_get_with_http_info', kwargs=kwargs)

    def log_error_reports_post(self, **kwargs):
        return self.call('log_error_reports_post', kwargs=kwargs)

    def log_error_reports_post_with_http_info(self, **kwargs):
        return self.call('log_error_reports_post_with_http_info', kwargs=kwargs)

    def maps_get(self, **kwargs):
        return self.call('maps_get', kwargs=kwargs)

    def maps_get_with_http_info(self, **kwargs):
        return self.call('maps_get_with_http_info', kwargs=kwargs)

    def maps_guid_delete(self, **kwargs):
        return self.call('maps_guid_delete', kwargs=kwargs)

    def maps_guid_delete_with_http_info(self, **kwargs):
        return self.call('maps_guid_delete_with_http_info', kwargs=kwargs)

    def maps_guid_get(self, **kwargs):
        return self.call('maps_guid_get', kwargs=kwargs)

    def maps_guid_get_with_http_info(self, **kwargs):
        return self.call('maps_guid_get_with_http_info', kwargs=kwargs)

    def maps_guid_put(self, **kwargs):
        return self.call('maps_guid_put', kwargs=kwargs)

    def maps_guid_put_with_http_info(self, **kwargs):
        return self.call('maps_guid_put_with_http_info', kwargs=kwargs)

    def maps_map_id_area_events_get(self, **kwargs):
        return self.call('maps_map_id_area_events_get', kwargs=kwargs)

    def maps_map_id_area_events_get_with_http_info(self, **kwargs):
        return self.call('maps_map_id_area_events_get_with_http_info', kwargs=kwargs)

    def maps_map_id_path_guides_get(self, **kwargs):
        return self.call('maps_map_id_path_guides_get', kwargs=kwargs)

    def maps_map_id_path_guides_get_with_http_info(self, **kwargs):
        return self.call('maps_map_id_path_guides_get_with_http_info', kwargs=kwargs)

    def maps_map_id_paths_get(self, **kwargs):
        return self.call('maps_map_id_paths_get', kwargs=kwargs)

    def maps_map_id_paths_get_with_http_info(self, **kwargs):
        return self.call('maps_map_id_paths_get_with_http_info', kwargs=kwargs)

    def maps_map_id_positions_get(self, **kwargs):
        return self.call('maps_map_id_positions_get', kwargs=kwargs)

    def maps_map_id_positions_get_with_http_info(self, **kwargs):
        return self.call('maps_map_id_positions_get_with_http_info', kwargs=kwargs)

    def maps_post(self, **kwargs):
        return self.call('maps_post', kwargs=kwargs)

    def maps_post_with_http_info(self, **kwargs):
        return self.call('maps_post_with_http_info', kwargs=kwargs)

    def mission_groups_get(self, **kwargs):
        return self.call('mission_groups_get', kwargs=kwargs)

    def mission_groups_get_with_http_info(self, **kwargs):
        return self.call('mission_groups_get_with_http_info', kwargs=kwargs)

    def mission_groups_group_id_missions_get(self, **kwargs):
        return self.call('mission_groups_group_id_missions_get', kwargs=kwargs)

    def mission_groups_group_id_missions_get_with_http_info(self, **kwargs):
        return self.call('mission_groups_group_id_missions_get_with_http_info', kwargs=kwargs)

    def mission_groups_guid_delete(self, **kwargs):
        return self.call('mission_groups_guid_delete', kwargs=kwargs)

    def mission_groups_guid_delete_with_http_info(self, **kwargs):
        return self.call('mission_groups_guid_delete_with_http_info', kwargs=kwargs)

    def mission_groups_guid_get(self, **kwargs):
        return self.call('mission_groups_guid_get', kwargs=kwargs)

    def mission_groups_guid_get_with_http_info(self, **kwargs):
        return self.call('mission_groups_guid_get_with_http_info', kwargs=kwargs)

    def mission_groups_guid_put(self, **kwargs):
        return self.call('mission_groups_guid_put', kwargs=kwargs)

    def mission_groups_guid_put_with_http_info(self, **kwargs):
        return self.call('mission_groups_guid_put_with_http_info', kwargs=kwargs)

    def mission_groups_mission_group_id_actions_get(self, **kwargs):
        return self.call('mission_groups_mission_group_id_actions_get', kwargs=kwargs)

    def mission_groups_mission_group_id_actions_get_with_http_info(self, **kwargs):
        return self.call('mission_groups_mission_group_id_actions_get_with_http_info', kwargs=kwargs)

    def mission_groups_post(self, **kwargs):
        return self.call('mission_groups_post', kwargs=kwargs)

    def mission_groups_post_with_http_info(self, **kwargs):
        return self.call('mission_groups_post_with_http_info', kwargs=kwargs)

    def mission_queue_delete(self, **kwargs):
        return self.call('mission_queue_delete', kwargs=kwargs)

    def mission_queue_delete_with_http_info(self, **kwargs):
        return self.call('mission_queue_delete_with_http_info', kwargs=kwargs)

    def mission_queue_get(self, **kwargs):
        return self.call('mission_queue_get', kwargs=kwargs)

    def mission_queue_get_with_http_info(self, **kwargs):
        return self.call('mission_queue_get_with_http_info', kwargs=kwargs)

    def mission_queue_id_delete(self, **kwargs):
        return self.call('mission_queue_id_delete', kwargs=kwargs)

    def mission_queue_id_delete_with_http_info(self, **kwargs):
        return self.call('mission_queue_id_delete_with_http_info', kwargs=kwargs)

    def mission_queue_id_get(self, **kwargs):
        return self.call('mission_queue_id_get', kwargs=kwargs)

    def mission_queue_id_get_with_http_info(self, **kwargs):
        return self.call('mission_queue_id_get_with_http_info', kwargs=kwargs)

    def mission_queue_id_put(self, **kwargs):
        return self.call('mission_queue_id_put', kwargs=kwargs)

    def mission_queue_id_put_with_http_info(self, **kwargs):
        return self.call('mission_queue_id_put_with_http_info', kwargs=kwargs)

    def mission_queue_mission_queue_id_actions_get(self, **kwargs):
        return self.call('mission_queue_mission_queue_id_actions_get', kwargs=kwargs)

    def mission_queue_mission_queue_id_actions_get_with_http_info(self, **kwargs):
        return self.call('mission_queue_mission_queue_id_actions_get_with_http_info', kwargs=kwargs)

    def mission_queue_mission_queue_id_actions_id_get(self, **kwargs):
        return self.call('mission_queue_mission_queue_id_actions_id_get', kwargs=kwargs)

    def mission_queue_mission_queue_id_actions_id_get_with_http_info(self, **kwargs):
        return self.call('mission_queue_mission_queue_id_actions_id_get_with_http_info', kwargs=kwargs)

    def mission_queue_post(self, **kwargs):
        return self.call('mission_queue_post', kwargs=kwargs)

    def mission_queue_post_with_http_info(self, **kwargs):
        return self.call('mission_queue_post_with_http_info', kwargs=kwargs)

    def missions_get(self, **kwargs):
        return self.call('missions_get', kwargs=kwargs)

    def missions_get_with_http_info(self, **kwargs):
        return self.call('missions_get_with_http_info', kwargs=kwargs)

    def missions_guid_definition_get(self, **kwargs):
        return self.call('missions_guid_definition_get', kwargs=kwargs)

    def missions_guid_definition_get_with_http_info(self, **kwargs):
        return self.call('missions_guid_definition_get_with_http_info', kwargs=kwargs)

    def missions_guid_delete(self, **kwargs):
        return self.call('missions_guid_delete', kwargs=kwargs)

    def missions_guid_delete_with_http_info(self, **kwargs):
        return self.call('missions_guid_delete_with_http_info', kwargs=kwargs)

    def missions_guid_get(self, **kwargs):
        return self.call('missions_guid_get', kwargs=kwargs)

    def missions_guid_get_with_http_info(self, **kwargs):
        return self.call('missions_guid_get_with_http_info', kwargs=kwargs)

    def missions_guid_put(self, **kwargs):
        return self.call('missions_guid_put', kwargs=kwargs)

    def missions_guid_put_with_http_info(self, **kwargs):
        return self.call('missions_guid_put_with_http_info', kwargs=kwargs)

    def missions_mission_id_actions_get(self, **kwargs):
        return self.call('missions_mission_id_actions_get', kwargs=kwargs)

    def missions_mission_id_actions_get_with_http_info(self, **kwargs):
        return self.call('missions_mission_id_actions_get_with_http_info', kwargs=kwargs)

    def missions_mission_id_actions_guid_delete(self, **kwargs):
        return self.call('missions_mission_id_actions_guid_delete', kwargs=kwargs)

    def missions_mission_id_actions_guid_delete_with_http_info(self, **kwargs):
        return self.call('missions_mission_id_actions_guid_delete_with_http_info', kwargs=kwargs)

    def missions_mission_id_actions_guid_get(self, **kwargs):
        return self.call('missions_mission_id_actions_guid_get', kwargs=kwargs)

    def missions_mission_id_actions_guid_get_with_http_info(self, **kwargs):
        return self.call('missions_mission_id_actions_guid_get_with_http_info', kwargs=kwargs)

    def missions_mission_id_actions_guid_put(self, **kwargs):
        return self.call('missions_mission_id_actions_guid_put', kwargs=kwargs)

    def missions_mission_id_actions_guid_put_with_http_info(self, **kwargs):
        return self.call('missions_mission_id_actions_guid_put_with_http_info', kwargs=kwargs)

    def missions_mission_id_actions_post(self, **kwargs):
        return self.call('missions_mission_id_actions_post', kwargs=kwargs)

    def missions_mission_id_actions_post_with_http_info(self, **kwargs):
        return self.call('missions_mission_id_actions_post_with_http_info', kwargs=kwargs)

    def missions_post(self, **kwargs):
        return self.call('missions_post', kwargs=kwargs)

    def missions_post_with_http_info(self, **kwargs):
        return self.call('missions_post_with_http_info', kwargs=kwargs)

    def modbus_get(self, **kwargs):
        return self.call('modbus_get', kwargs=kwargs)

    def modbus_get_with_http_info(self, **kwargs):
        return self.call('modbus_get_with_http_info', kwargs=kwargs)

    def modbus_id_get(self, **kwargs):
        return self.call('modbus_id_get', kwargs=kwargs)

    def modbus_id_get_with_http_info(self, **kwargs):
        return self.call('modbus_id_get_with_http_info', kwargs=kwargs)

    def modbus_missions_get(self, **kwargs):
        return self.call('modbus_missions_get', kwargs=kwargs)

    def modbus_missions_get_with_http_info(self, **kwargs):
        return self.call('modbus_missions_get_with_http_info', kwargs=kwargs)

    def modbus_missions_guid_delete(self, **kwargs):
        return self.call('modbus_missions_guid_delete', kwargs=kwargs)

    def modbus_missions_guid_delete_with_http_info(self, **kwargs):
        return self.call('modbus_missions_guid_delete_with_http_info', kwargs=kwargs)

    def modbus_missions_guid_get(self, **kwargs):
        return self.call('modbus_missions_guid_get', kwargs=kwargs)

    def modbus_missions_guid_get_with_http_info(self, **kwargs):
        return self.call('modbus_missions_guid_get_with_http_info', kwargs=kwargs)

    def modbus_missions_guid_put(self, **kwargs):
        return self.call('modbus_missions_guid_put', kwargs=kwargs)

    def modbus_missions_guid_put_with_http_info(self, **kwargs):
        return self.call('modbus_missions_guid_put_with_http_info', kwargs=kwargs)

    def modbus_missions_post(self, **kwargs):
        return self.call('modbus_missions_post', kwargs=kwargs)

    def modbus_missions_post_with_http_info(self, **kwargs):
        return self.call('modbus_missions_post_with_http_info', kwargs=kwargs)

    def path_guides_get(self, **kwargs):
        return self.call('path_guides_get', kwargs=kwargs)

    def path_guides_get_with_http_info(self, **kwargs):
        return self.call('path_guides_get_with_http_info', kwargs=kwargs)

    def path_guides_guid_delete(self, **kwargs):
        return self.call('path_guides_guid_delete', kwargs=kwargs)

    def path_guides_guid_delete_with_http_info(self, **kwargs):
        return self.call('path_guides_guid_delete_with_http_info', kwargs=kwargs)

    def path_guides_guid_get(self, **kwargs):
        return self.call('path_guides_guid_get', kwargs=kwargs)

    def path_guides_guid_get_with_http_info(self, **kwargs):
        return self.call('path_guides_guid_get_with_http_info', kwargs=kwargs)

    def path_guides_guid_put(self, **kwargs):
        return self.call('path_guides_guid_put', kwargs=kwargs)

    def path_guides_guid_put_with_http_info(self, **kwargs):
        return self.call('path_guides_guid_put_with_http_info', kwargs=kwargs)

    def path_guides_path_guide_guid_options_get(self, **kwargs):
        return self.call('path_guides_path_guide_guid_options_get', kwargs=kwargs)

    def path_guides_path_guide_guid_options_get_with_http_info(self, **kwargs):
        return self.call('path_guides_path_guide_guid_options_get_with_http_info', kwargs=kwargs)

    def path_guides_path_guide_guid_positions_get(self, **kwargs):
        return self.call('path_guides_path_guide_guid_positions_get', kwargs=kwargs)

    def path_guides_path_guide_guid_positions_get_with_http_info(self, **kwargs):
        return self.call('path_guides_path_guide_guid_positions_get_with_http_info', kwargs=kwargs)

    def path_guides_path_guide_guid_positions_guid_delete(self, **kwargs):
        return self.call('path_guides_path_guide_guid_positions_guid_delete', kwargs=kwargs)

    def path_guides_path_guide_guid_positions_guid_delete_with_http_info(self, **kwargs):
        return self.call('path_guides_path_guide_guid_positions_guid_delete_with_http_info', kwargs=kwargs)

    def path_guides_path_guide_guid_positions_guid_get(self, **kwargs):
        return self.call('path_guides_path_guide_guid_positions_guid_get', kwargs=kwargs)

    def path_guides_path_guide_guid_positions_guid_get_with_http_info(self, **kwargs):
        return self.call('path_guides_path_guide_guid_positions_guid_get_with_http_info', kwargs=kwargs)

    def path_guides_path_guide_guid_positions_guid_put(self, **kwargs):
        return self.call('path_guides_path_guide_guid_positions_guid_put', kwargs=kwargs)

    def path_guides_path_guide_guid_positions_guid_put_with_http_info(self, **kwargs):
        return self.call('path_guides_path_guide_guid_positions_guid_put_with_http_info', kwargs=kwargs)

    def path_guides_path_guide_guid_positions_post(self, **kwargs):
        return self.call('path_guides_path_guide_guid_positions_post', kwargs=kwargs)

    def path_guides_path_guide_guid_positions_post_with_http_info(self, **kwargs):
        return self.call('path_guides_path_guide_guid_positions_post_with_http_info', kwargs=kwargs)

    def path_guides_positions_get(self, **kwargs):
        return self.call('path_guides_positions_get', kwargs=kwargs)

    def path_guides_positions_get_with_http_info(self, **kwargs):
        return self.call('path_guides_positions_get_with_http_info', kwargs=kwargs)

    def path_guides_positions_guid_delete(self, **kwargs):
        return self.call('path_guides_positions_guid_delete', kwargs=kwargs)

    def path_guides_positions_guid_delete_with_http_info(self, **kwargs):
        return self.call('path_guides_positions_guid_delete_with_http_info', kwargs=kwargs)

    def path_guides_positions_guid_get(self, **kwargs):
        return self.call('path_guides_positions_guid_get', kwargs=kwargs)

    def path_guides_positions_guid_get_with_http_info(self, **kwargs):
        return self.call('path_guides_positions_guid_get_with_http_info', kwargs=kwargs)

    def path_guides_positions_guid_put(self, **kwargs):
        return self.call('path_guides_positions_guid_put', kwargs=kwargs)

    def path_guides_positions_guid_put_with_http_info(self, **kwargs):
        return self.call('path_guides_positions_guid_put_with_http_info', kwargs=kwargs)

    def path_guides_positions_post(self, **kwargs):
        return self.call('path_guides_positions_post', kwargs=kwargs)

    def path_guides_positions_post_with_http_info(self, **kwargs):
        return self.call('path_guides_positions_post_with_http_info', kwargs=kwargs)

    def path_guides_post(self, **kwargs):
        return self.call('path_guides_post', kwargs=kwargs)

    def path_guides_post_with_http_info(self, **kwargs):
        return self.call('path_guides_post_with_http_info', kwargs=kwargs)

    def path_guides_precalc_get(self, **kwargs):
        return self.call('path_guides_precalc_get', kwargs=kwargs)

    def path_guides_precalc_get_with_http_info(self, **kwargs):
        return self.call('path_guides_precalc_get_with_http_info', kwargs=kwargs)

    def path_guides_precalc_post(self, **kwargs):
        return self.call('path_guides_precalc_post', kwargs=kwargs)

    def path_guides_precalc_post_with_http_info(self, **kwargs):
        return self.call('path_guides_precalc_post_with_http_info', kwargs=kwargs)

    def paths_get(self, **kwargs):
        return self.call('paths_get', kwargs=kwargs)

    def paths_get_with_http_info(self, **kwargs):
        return self.call('paths_get_with_http_info', kwargs=kwargs)

    def paths_guid_delete(self, **kwargs):
        return self.call('paths_guid_delete', kwargs=kwargs)

    def paths_guid_delete_with_http_info(self, **kwargs):
        return self.call('paths_guid_delete_with_http_info', kwargs=kwargs)

    def paths_guid_get(self, **kwargs):
        return self.call('paths_guid_get', kwargs=kwargs)

    def paths_guid_get_with_http_info(self, **kwargs):
        return self.call('paths_guid_get_with_http_info', kwargs=kwargs)

    def paths_guid_put(self, **kwargs):
        return self.call('paths_guid_put', kwargs=kwargs)

    def paths_guid_put_with_http_info(self, **kwargs):
        return self.call('paths_guid_put_with_http_info', kwargs=kwargs)

    def paths_post(self, **kwargs):
        return self.call('paths_post', kwargs=kwargs)

    def paths_post_with_http_info(self, **kwargs):
        return self.call('paths_post_with_http_info', kwargs=kwargs)

    def permissions_guid_delete(self, **kwargs):
        return self.call('permissions_guid_delete', kwargs=kwargs)

    def permissions_guid_delete_with_http_info(self, **kwargs):
        return self.call('permissions_guid_delete_with_http_info', kwargs=kwargs)

    def permissions_guid_get(self, **kwargs):
        return self.call('permissions_guid_get', kwargs=kwargs)

    def permissions_guid_get_with_http_info(self, **kwargs):
        return self.call('permissions_guid_get_with_http_info', kwargs=kwargs)

    def permissions_guid_put(self, **kwargs):
        return self.call('permissions_guid_put', kwargs=kwargs)

    def permissions_guid_put_with_http_info(self, **kwargs):
        return self.call('permissions_guid_put_with_http_info', kwargs=kwargs)

    def position_transition_lists_get(self, **kwargs):
        return self.call('position_transition_lists_get', kwargs=kwargs)

    def position_transition_lists_get_with_http_info(self, **kwargs):
        return self.call('position_transition_lists_get_with_http_info', kwargs=kwargs)

    def position_transition_lists_guid_delete(self, **kwargs):
        return self.call('position_transition_lists_guid_delete', kwargs=kwargs)

    def position_transition_lists_guid_delete_with_http_info(self, **kwargs):
        return self.call('position_transition_lists_guid_delete_with_http_info', kwargs=kwargs)

    def position_transition_lists_guid_get(self, **kwargs):
        return self.call('position_transition_lists_guid_get', kwargs=kwargs)

    def position_transition_lists_guid_get_with_http_info(self, **kwargs):
        return self.call('position_transition_lists_guid_get_with_http_info', kwargs=kwargs)

    def position_transition_lists_guid_put(self, **kwargs):
        return self.call('position_transition_lists_guid_put', kwargs=kwargs)

    def position_transition_lists_guid_put_with_http_info(self, **kwargs):
        return self.call('position_transition_lists_guid_put_with_http_info', kwargs=kwargs)

    def position_transition_lists_post(self, **kwargs):
        return self.call('position_transition_lists_post', kwargs=kwargs)

    def position_transition_lists_post_with_http_info(self, **kwargs):
        return self.call('position_transition_lists_post_with_http_info', kwargs=kwargs)

    def position_types_get(self, **kwargs):
        return self.call('position_types_get', kwargs=kwargs)

    def position_types_get_with_http_info(self, **kwargs):
        return self.call('position_types_get_with_http_info', kwargs=kwargs)

    def position_types_id_get(self, **kwargs):
        return self.call('position_types_id_get', kwargs=kwargs)

    def position_types_id_get_with_http_info(self, **kwargs):
        return self.call('position_types_id_get_with_http_info', kwargs=kwargs)

    def positions_get(self, **kwargs):
        return self.call('positions_get', kwargs=kwargs)

    def positions_get_with_http_info(self, **kwargs):
        return self.call('positions_get_with_http_info', kwargs=kwargs)

    def positions_guid_delete(self, **kwargs):
        return self.call('positions_guid_delete', kwargs=kwargs)

    def positions_guid_delete_with_http_info(self, **kwargs):
        return self.call('positions_guid_delete_with_http_info', kwargs=kwargs)

    def positions_guid_get(self, **kwargs):
        return self.call('positions_guid_get', kwargs=kwargs)

    def positions_guid_get_with_http_info(self, **kwargs):
        return self.call('positions_guid_get_with_http_info', kwargs=kwargs)

    def positions_guid_put(self, **kwargs):
        return self.call('positions_guid_put', kwargs=kwargs)

    def positions_guid_put_with_http_info(self, **kwargs):
        return self.call('positions_guid_put_with_http_info', kwargs=kwargs)

    def positions_parent_guid_helper_positions_get(self, **kwargs):
        return self.call('positions_parent_guid_helper_positions_get', kwargs=kwargs)

    def positions_parent_guid_helper_positions_get_with_http_info(self, **kwargs):
        return self.call('positions_parent_guid_helper_positions_get_with_http_info', kwargs=kwargs)

    def positions_pos_id_docking_offsets_get(self, **kwargs):
        return self.call('positions_pos_id_docking_offsets_get', kwargs=kwargs)

    def positions_pos_id_docking_offsets_get_with_http_info(self, **kwargs):
        return self.call('positions_pos_id_docking_offsets_get_with_http_info', kwargs=kwargs)

    def positions_post(self, **kwargs):
        return self.call('positions_post', kwargs=kwargs)

    def positions_post_with_http_info(self, **kwargs):
        return self.call('positions_post_with_http_info', kwargs=kwargs)

    def registers_get(self, **kwargs):
        return self.call('registers_get', kwargs=kwargs)

    def registers_get_with_http_info(self, **kwargs):
        return self.call('registers_get_with_http_info', kwargs=kwargs)

    def registers_id_get(self, **kwargs):
        return self.call('registers_id_get', kwargs=kwargs)

    def registers_id_get_with_http_info(self, **kwargs):
        return self.call('registers_id_get_with_http_info', kwargs=kwargs)

    def registers_id_post(self, **kwargs):
        return self.call('registers_id_post', kwargs=kwargs)

    def registers_id_post_with_http_info(self, **kwargs):
        return self.call('registers_id_post_with_http_info', kwargs=kwargs)

    def registers_id_put(self, **kwargs):
        return self.call('registers_id_put', kwargs=kwargs)

    def registers_id_put_with_http_info(self, **kwargs):
        return self.call('registers_id_put_with_http_info', kwargs=kwargs)

    def remote_support_get(self, **kwargs):
        return self.call('remote_support_get', kwargs=kwargs)

    def remote_support_get_with_http_info(self, **kwargs):
        return self.call('remote_support_get_with_http_info', kwargs=kwargs)

    def remote_support_log_get(self, **kwargs):
        return self.call('remote_support_log_get', kwargs=kwargs)

    def remote_support_log_get_with_http_info(self, **kwargs):
        return self.call('remote_support_log_get_with_http_info', kwargs=kwargs)

    def remote_support_put(self, **kwargs):
        return self.call('remote_support_put', kwargs=kwargs)

    def remote_support_put_with_http_info(self, **kwargs):
        return self.call('remote_support_put_with_http_info', kwargs=kwargs)

    def robots_post(self, **kwargs):
        return self.call('robots_post', kwargs=kwargs)

    def robots_post_with_http_info(self, **kwargs):
        return self.call('robots_post_with_http_info', kwargs=kwargs)

    def service_book_get(self, **kwargs):
        return self.call('service_book_get', kwargs=kwargs)

    def service_book_get_with_http_info(self, **kwargs):
        return self.call('service_book_get_with_http_info', kwargs=kwargs)

    def service_book_guid_delete(self, **kwargs):
        return self.call('service_book_guid_delete', kwargs=kwargs)

    def service_book_guid_delete_with_http_info(self, **kwargs):
        return self.call('service_book_guid_delete_with_http_info', kwargs=kwargs)

    def service_book_guid_get(self, **kwargs):
        return self.call('service_book_guid_get', kwargs=kwargs)

    def service_book_guid_get_with_http_info(self, **kwargs):
        return self.call('service_book_guid_get_with_http_info', kwargs=kwargs)

    def service_book_post(self, **kwargs):
        return self.call('service_book_post', kwargs=kwargs)

    def service_book_post_with_http_info(self, **kwargs):
        return self.call('service_book_post_with_http_info', kwargs=kwargs)

    def sessions_get(self, **kwargs):
        return self.call('sessions_get', kwargs=kwargs)

    def sessions_get_with_http_info(self, **kwargs):
        return self.call('sessions_get_with_http_info', kwargs=kwargs)

    def sessions_guid_delete(self, **kwargs):
        return self.call('sessions_guid_delete', kwargs=kwargs)

    def sessions_guid_delete_with_http_info(self, **kwargs):
        return self.call('sessions_guid_delete_with_http_info', kwargs=kwargs)

    def sessions_guid_export_get(self, **kwargs):
        return self.call('sessions_guid_export_get', kwargs=kwargs)

    def sessions_guid_export_get_with_http_info(self, **kwargs):
        return self.call('sessions_guid_export_get_with_http_info', kwargs=kwargs)

    def sessions_guid_get(self, **kwargs):
        return self.call('sessions_guid_get', kwargs=kwargs)

    def sessions_guid_get_with_http_info(self, **kwargs):
        return self.call('sessions_guid_get_with_http_info', kwargs=kwargs)

    def sessions_guid_put(self, **kwargs):
        return self.call('sessions_guid_put', kwargs=kwargs)

    def sessions_guid_put_with_http_info(self, **kwargs):
        return self.call('sessions_guid_put_with_http_info', kwargs=kwargs)

    def sessions_import_delete(self, **kwargs):
        return self.call('sessions_import_delete', kwargs=kwargs)

    def sessions_import_delete_with_http_info(self, **kwargs):
        return self.call('sessions_import_delete_with_http_info', kwargs=kwargs)

    def sessions_import_get(self, **kwargs):
        return self.call('sessions_import_get', kwargs=kwargs)

    def sessions_import_get_with_http_info(self, **kwargs):
        return self.call('sessions_import_get_with_http_info', kwargs=kwargs)

    def sessions_import_post(self, **kwargs):
        return self.call('sessions_import_post', kwargs=kwargs)

    def sessions_import_post_with_http_info(self, **kwargs):
        return self.call('sessions_import_post_with_http_info', kwargs=kwargs)

    def sessions_post(self, **kwargs):
        return self.call('sessions_post', kwargs=kwargs)

    def sessions_post_with_http_info(self, **kwargs):
        return self.call('sessions_post_with_http_info', kwargs=kwargs)

    def sessions_session_id_maps_get(self, **kwargs):
        return self.call('sessions_session_id_maps_get', kwargs=kwargs)

    def sessions_session_id_maps_get_with_http_info(self, **kwargs):
        return self.call('sessions_session_id_maps_get_with_http_info', kwargs=kwargs)

    def sessions_session_id_missions_get(self, **kwargs):
        return self.call('sessions_session_id_missions_get', kwargs=kwargs)

    def sessions_session_id_missions_get_with_http_info(self, **kwargs):
        return self.call('sessions_session_id_missions_get_with_http_info', kwargs=kwargs)

    def sessions_session_id_position_transition_lists_get(self, **kwargs):
        return self.call('sessions_session_id_position_transition_lists_get', kwargs=kwargs)

    def sessions_session_id_position_transition_lists_get_with_http_info(self, **kwargs):
        return self.call('sessions_session_id_position_transition_lists_get_with_http_info', kwargs=kwargs)

    def setting_groups_get(self, **kwargs):
        return self.call('setting_groups_get', kwargs=kwargs)

    def setting_groups_get_with_http_info(self, **kwargs):
        return self.call('setting_groups_get_with_http_info', kwargs=kwargs)

    def setting_groups_id_get(self, **kwargs):
        return self.call('setting_groups_id_get', kwargs=kwargs)

    def setting_groups_id_get_with_http_info(self, **kwargs):
        return self.call('setting_groups_id_get_with_http_info', kwargs=kwargs)

    def setting_groups_settings_group_id_settings_advanced_get(self, **kwargs):
        return self.call('setting_groups_settings_group_id_settings_advanced_get', kwargs=kwargs)

    def setting_groups_settings_group_id_settings_advanced_get_with_http_info(self, **kwargs):
        return self.call('setting_groups_settings_group_id_settings_advanced_get_with_http_info', kwargs=kwargs)

    def setting_groups_settings_group_id_settings_get(self, **kwargs):
        return self.call('setting_groups_settings_group_id_settings_get', kwargs=kwargs)

    def setting_groups_settings_group_id_settings_get_with_http_info(self, **kwargs):
        return self.call('setting_groups_settings_group_id_settings_get_with_http_info', kwargs=kwargs)

    def settings_advanced_get(self, **kwargs):
        return self.call('settings_advanced_get', kwargs=kwargs)

    def settings_advanced_get_with_http_info(self, **kwargs):
        return self.call('settings_advanced_get_with_http_info', kwargs=kwargs)

    def settings_advanced_id_get(self, **kwargs):
        return self.call('settings_advanced_id_get', kwargs=kwargs)

    def settings_advanced_id_get_with_http_info(self, **kwargs):
        return self.call('settings_advanced_id_get_with_http_info', kwargs=kwargs)

    def settings_advanced_id_put(self, **kwargs):
        return self.call('settings_advanced_id_put', kwargs=kwargs)

    def settings_advanced_id_put_with_http_info(self, **kwargs):
        return self.call('settings_advanced_id_put_with_http_info', kwargs=kwargs)

    def settings_get(self, **kwargs):
        return self.call('settings_get', kwargs=kwargs)

    def settings_get_with_http_info(self, **kwargs):
        return self.call('settings_get_with_http_info', kwargs=kwargs)

    def settings_id_get(self, **kwargs):
        return self.call('settings_id_get', kwargs=kwargs)

    def settings_id_get_with_http_info(self, **kwargs):
        return self.call('settings_id_get_with_http_info', kwargs=kwargs)

    def settings_id_put(self, **kwargs):
        return self.call('settings_id_put', kwargs=kwargs)

    def settings_id_put_with_http_info(self, **kwargs):
        return self.call('settings_id_put_with_http_info', kwargs=kwargs)

    def shelf_types_get(self, **kwargs):
        return self.call('shelf_types_get', kwargs=kwargs)

    def shelf_types_get_with_http_info(self, **kwargs):
        return self.call('shelf_types_get_with_http_info', kwargs=kwargs)

    def shelf_types_guid_delete(self, **kwargs):
        return self.call('shelf_types_guid_delete', kwargs=kwargs)

    def shelf_types_guid_delete_with_http_info(self, **kwargs):
        return self.call('shelf_types_guid_delete_with_http_info', kwargs=kwargs)

    def shelf_types_guid_get(self, **kwargs):
        return self.call('shelf_types_guid_get', kwargs=kwargs)

    def shelf_types_guid_get_with_http_info(self, **kwargs):
        return self.call('shelf_types_guid_get_with_http_info', kwargs=kwargs)

    def shelf_types_guid_put(self, **kwargs):
        return self.call('shelf_types_guid_put', kwargs=kwargs)

    def shelf_types_guid_put_with_http_info(self, **kwargs):
        return self.call('shelf_types_guid_put_with_http_info', kwargs=kwargs)

    def shelf_types_post(self, **kwargs):
        return self.call('shelf_types_post', kwargs=kwargs)

    def shelf_types_post_with_http_info(self, **kwargs):
        return self.call('shelf_types_post_with_http_info', kwargs=kwargs)

    def software_backups_get(self, **kwargs):
        return self.call('software_backups_get', kwargs=kwargs)

    def software_backups_get_with_http_info(self, **kwargs):
        return self.call('software_backups_get_with_http_info', kwargs=kwargs)

    def software_backups_guid_delete(self, **kwargs):
        return self.call('software_backups_guid_delete', kwargs=kwargs)

    def software_backups_guid_delete_with_http_info(self, **kwargs):
        return self.call('software_backups_guid_delete_with_http_info', kwargs=kwargs)

    def software_backups_guid_get(self, **kwargs):
        return self.call('software_backups_guid_get', kwargs=kwargs)

    def software_backups_guid_get_with_http_info(self, **kwargs):
        return self.call('software_backups_guid_get_with_http_info', kwargs=kwargs)

    def software_backups_guid_post(self, **kwargs):
        return self.call('software_backups_guid_post', kwargs=kwargs)

    def software_backups_guid_post_with_http_info(self, **kwargs):
        return self.call('software_backups_guid_post_with_http_info', kwargs=kwargs)

    def software_backups_post(self, **kwargs):
        return self.call('software_backups_post', kwargs=kwargs)

    def software_backups_post_with_http_info(self, **kwargs):
        return self.call('software_backups_post_with_http_info', kwargs=kwargs)

    def software_lock_get(self, **kwargs):
        return self.call('software_lock_get', kwargs=kwargs)

    def software_lock_get_with_http_info(self, **kwargs):
        return self.call('software_lock_get_with_http_info', kwargs=kwargs)

    def software_lock_put(self, **kwargs):
        return self.call('software_lock_put', kwargs=kwargs)

    def software_lock_put_with_http_info(self, **kwargs):
        return self.call('software_lock_put_with_http_info', kwargs=kwargs)

    def software_logs_get(self, **kwargs):
        return self.call('software_logs_get', kwargs=kwargs)

    def software_logs_get_with_http_info(self, **kwargs):
        return self.call('software_logs_get_with_http_info', kwargs=kwargs)

    def software_logs_guid_get(self, **kwargs):
        return self.call('software_logs_guid_get', kwargs=kwargs)

    def software_logs_guid_get_with_http_info(self, **kwargs):
        return self.call('software_logs_guid_get_with_http_info', kwargs=kwargs)

    def software_upgrades_get(self, **kwargs):
        return self.call('software_upgrades_get', kwargs=kwargs)

    def software_upgrades_get_with_http_info(self, **kwargs):
        return self.call('software_upgrades_get_with_http_info', kwargs=kwargs)

    def software_upgrades_guid_delete(self, **kwargs):
        return self.call('software_upgrades_guid_delete', kwargs=kwargs)

    def software_upgrades_guid_delete_with_http_info(self, **kwargs):
        return self.call('software_upgrades_guid_delete_with_http_info', kwargs=kwargs)

    def software_upgrades_guid_get(self, **kwargs):
        return self.call('software_upgrades_guid_get', kwargs=kwargs)

    def software_upgrades_guid_get_with_http_info(self, **kwargs):
        return self.call('software_upgrades_guid_get_with_http_info', kwargs=kwargs)

    def software_upgrades_guid_post(self, **kwargs):
        return self.call('software_upgrades_guid_post', kwargs=kwargs)

    def software_upgrades_guid_post_with_http_info(self, **kwargs):
        return self.call('software_upgrades_guid_post_with_http_info', kwargs=kwargs)

    def software_upgrades_post(self, **kwargs):
        return self.call('software_upgrades_post', kwargs=kwargs)

    def software_upgrades_post_with_http_info(self, **kwargs):
        return self.call('software_upgrades_post_with_http_info', kwargs=kwargs)

    def sounds_get(self, **kwargs):
        return self.call('sounds_get', kwargs=kwargs)

    def sounds_get_with_http_info(self, **kwargs):
        return self.call('sounds_get_with_http_info', kwargs=kwargs)

    def sounds_guid_delete(self, **kwargs):
        return self.call('sounds_guid_delete', kwargs=kwargs)

    def sounds_guid_delete_with_http_info(self, **kwargs):
        return self.call('sounds_guid_delete_with_http_info', kwargs=kwargs)

    def sounds_guid_get(self, **kwargs):
        return self.call('sounds_guid_get', kwargs=kwargs)

    def sounds_guid_get_with_http_info(self, **kwargs):
        return self.call('sounds_guid_get_with_http_info', kwargs=kwargs)

    def sounds_guid_put(self, **kwargs):
        return self.call('sounds_guid_put', kwargs=kwargs)

    def sounds_guid_put_with_http_info(self, **kwargs):
        return self.call('sounds_guid_put_with_http_info', kwargs=kwargs)

    def sounds_guid_stream_get(self, **kwargs):
        return self.call('sounds_guid_stream_get', kwargs=kwargs)

    def sounds_guid_stream_get_with_http_info(self, **kwargs):
        return self.call('sounds_guid_stream_get_with_http_info', kwargs=kwargs)

    def sounds_post(self, **kwargs):
        return self.call('sounds_post', kwargs=kwargs)

    def sounds_post_with_http_info(self, **kwargs):
        return self.call('sounds_post_with_http_info', kwargs=kwargs)

    def statistics_distance_get(self, **kwargs):
        return self.call('statistics_distance_get', kwargs=kwargs)

    def statistics_distance_get_with_http_info(self, **kwargs):
        return self.call('statistics_distance_get_with_http_info', kwargs=kwargs)

    def status_get(self, **kwargs):
        return self.call('status_get', kwargs=kwargs)

    def status_get_with_http_info(self, **kwargs):
        return self.call('status_get_with_http_info', kwargs=kwargs)

    def status_put(self, **kwargs):
        return self.call('status_put', kwargs=kwargs)

    def status_put_with_http_info(self, **kwargs):
        return self.call('status_put_with_http_info', kwargs=kwargs)

    def system_info_get(self, **kwargs):
        return self.call('system_info_get', kwargs=kwargs)

    def system_info_get_with_http_info(self, **kwargs):
        return self.call('system_info_get_with_http_info', kwargs=kwargs)

    def user_groups_get(self, **kwargs):
        return self.call('user_groups_get', kwargs=kwargs)

    def user_groups_get_with_http_info(self, **kwargs):
        return self.call('user_groups_get_with_http_info', kwargs=kwargs)

    def user_groups_guid_delete(self, **kwargs):
        return self.call('user_groups_guid_delete', kwargs=kwargs)

    def user_groups_guid_delete_with_http_info(self, **kwargs):
        return self.call('user_groups_guid_delete_with_http_info', kwargs=kwargs)

    def user_groups_guid_get(self, **kwargs):
        return self.call('user_groups_guid_get', kwargs=kwargs)

    def user_groups_guid_get_with_http_info(self, **kwargs):
        return self.call('user_groups_guid_get_with_http_info', kwargs=kwargs)

    def user_groups_guid_put(self, **kwargs):
        return self.call('user_groups_guid_put', kwargs=kwargs)

    def user_groups_guid_put_with_http_info(self, **kwargs):
        return self.call('user_groups_guid_put_with_http_info', kwargs=kwargs)

    def user_groups_post(self, **kwargs):
        return self.call('user_groups_post', kwargs=kwargs)

    def user_groups_post_with_http_info(self, **kwargs):
        return self.call('user_groups_post_with_http_info', kwargs=kwargs)

    def user_groups_user_group_guid_permissions_get(self, **kwargs):
        return self.call('user_groups_user_group_guid_permissions_get', kwargs=kwargs)

    def user_groups_user_group_guid_permissions_get_with_http_info(self, **kwargs):
        return self.call('user_groups_user_group_guid_permissions_get_with_http_info', kwargs=kwargs)

    def user_groups_user_group_guid_permissions_post(self, **kwargs):
        return self.call('user_groups_user_group_guid_permissions_post', kwargs=kwargs)

    def user_groups_user_group_guid_permissions_post_with_http_info(self, **kwargs):
        return self.call('user_groups_user_group_guid_permissions_post_with_http_info', kwargs=kwargs)

    def users_auth_delete(self, **kwargs):
        return self.call('users_auth_delete', kwargs=kwargs)

    def users_auth_delete_with_http_info(self, **kwargs):
        return self.call('users_auth_delete_with_http_info', kwargs=kwargs)

    def users_auth_post(self, **kwargs):
        return self.call('users_auth_post', kwargs=kwargs)

    def users_auth_post_with_http_info(self, **kwargs):
        return self.call('users_auth_post_with_http_info', kwargs=kwargs)

    def users_get(self, **kwargs):
        return self.call('users_get', kwargs=kwargs)

    def users_get_with_http_info(self, **kwargs):
        return self.call('users_get_with_http_info', kwargs=kwargs)

    def users_guid_delete(self, **kwargs):
        return self.call('users_guid_delete', kwargs=kwargs)

    def users_guid_delete_with_http_info(self, **kwargs):
        return self.call('users_guid_delete_with_http_info', kwargs=kwargs)

    def users_guid_get(self, **kwargs):
        return self.call('users_guid_get', kwargs=kwargs)

    def users_guid_get_with_http_info(self, **kwargs):
        return self.call('users_guid_get_with_http_info', kwargs=kwargs)

    def users_guid_put(self, **kwargs):
        return self.call('users_guid_put', kwargs=kwargs)

    def users_guid_put_with_http_info(self, **kwargs):
        return self.call('users_guid_put_with_http_info', kwargs=kwargs)

    def users_me_get(self, **kwargs):
        return self.call('users_me_get', kwargs=kwargs)

    def users_me_get_with_http_info(self, **kwargs):
        return self.call('users_me_get_with_http_info', kwargs=kwargs)

    def users_me_permissions_get(self, **kwargs):
        return self.call('users_me_permissions_get', kwargs=kwargs)

    def users_me_permissions_get_with_http_info(self, **kwargs):
        return self.call('users_me_permissions_get_with_http_info', kwargs=kwargs)

    def users_me_put(self, **kwargs):
        return self.call('users_me_put', kwargs=kwargs)

    def users_me_put_with_http_info(self, **kwargs):
        return self.call('users_me_put_with_http_info', kwargs=kwargs)

    def users_post(self, **kwargs):
        return self.call('users_post', kwargs=kwargs)

    def users_post_with_http_info(self, **kwargs):
        return self.call('users_post_with_http_info', kwargs=kwargs)

    def wifi_connections_get(self, **kwargs):
        return self.call('wifi_connections_get', kwargs=kwargs)

    def wifi_connections_get_with_http_info(self, **kwargs):
        return self.call('wifi_connections_get_with_http_info', kwargs=kwargs)

    def wifi_connections_post(self, **kwargs):
        return self.call('wifi_connections_post', kwargs=kwargs)

    def wifi_connections_post_with_http_info(self, **kwargs):
        return self.call('wifi_connections_post_with_http_info', kwargs=kwargs)

    def wifi_connections_uuid_delete(self, **kwargs):
        return self.call('wifi_connections_uuid_delete', kwargs=kwargs)

    def wifi_connections_uuid_delete_with_http_info(self, **kwargs):
        return self.call('wifi_connections_uuid_delete_with_http_info', kwargs=kwargs)

    def wifi_connections_uuid_get(self, **kwargs):
        return self.call('wifi_connections_uuid_get', kwargs=kwargs)

    def wifi_connections_uuid_get_with_http_info(self, **kwargs):
        return self.call('wifi_connections_uuid_get_with_http_info', kwargs=kwargs)

    def wifi_connections_uuid_post(self, **kwargs):
        return self.call('wifi_connections_uuid_post', kwargs=kwargs)

    def wifi_connections_uuid_post_with_http_info(self, **kwargs):
        return self.call('wifi_connections_uuid_post_with_http_info', kwargs=kwargs)

    def wifi_get(self, **kwargs):
        return self.call('wifi_get', kwargs=kwargs)

    def wifi_get_with_http_info(self, **kwargs):
        return self.call('wifi_get_with_http_info', kwargs=kwargs)

    def wifi_networks_get(self, **kwargs):
        return self.call('wifi_networks_get', kwargs=kwargs)

    def wifi_networks_get_with_http_info(self, **kwargs):
        return self.call('wifi_networks_get_with_http_info', kwargs=kwargs)

    def wifi_networks_guid_get(self, **kwargs):
        return self.call('wifi_networks_guid_get', kwargs=kwargs)

    def wifi_networks_guid_get_with_http_info(self, **kwargs):
        return self.call('wifi_networks_guid_get_with_http_info', kwargs=kwargs)

    def world_model_get(self, **kwargs):
        return self.call('world_model_get', kwargs=kwargs)

    def world_model_get_with_http_info(self, **kwargs):
        return self.call('world_model_get_with_http_info', kwargs=kwargs)

    def world_model_post(self, **kwargs):
        return self.call('world_model_post', kwargs=kwargs)

    def world_model_post_with_http_info(self, **kwargs):
        return self.call('world_model_post_with_http_info', kwargs=kwargs)

