from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOxfordNanoporePromethion(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/nanoporetech__minknow_api', 'source_file': 'python/minknow_api/manager_service.py', 'class_name': 'ManagerService', 'import_roots': ['python'], 'candidate_methods': ['describe_host', 'get_basecaller_features', 'flow_cell_positions', 'watch_flow_cell_positions', 'reset_position', 'basecaller_api', 'get_guppy_info', 'get_version_info', 'list_protocol_output_dir_files', 'create_directory', 'get_disk_space_info', 'get_default_output_directories', 'stream_disk_space_info', 'get_barcode_kit_info', 'get_lamp_kit_info', 'get_barcode_keys', 'get_flow_cell_types', 'get_sequencing_kits', 'add_simulated_device', 'remove_simulated_device', 'local_authentication_token_path', 'get_alignment_reference_information', 'association_device_code', 'apply_offline_association_unlock_code', 'find_protocols', 'list_settings_for_protocol', 'get_features', 'set_features', 'restart_device_admin_service', 'check_bed_file', 'find_basecall_configurations', 'check_path_info'], 'action_targets': {}, 'metadata': {'repo': 'nanoporetech/minknow_api', 'repo_url': 'https://github.com/nanoporetech/minknow_api', 'brand': 'Oxford Nanopore', 'model': 'PromethION', 'device_type_cn': 'DNA测序仪', 'device_type_en': 'DNA Sequencer', 'source_framework': '生命科学', 'tag_id': '4361', 'tag_name': 'DNA测序仪', 'tag_name_en': 'DNA Sequencer', 'candidate_score': 302, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def describe_host(self, **kwargs):
        return self.call('describe_host', kwargs=kwargs)

    def get_basecaller_features(self, **kwargs):
        return self.call('get_basecaller_features', kwargs=kwargs)

    def flow_cell_positions(self, **kwargs):
        return self.call('flow_cell_positions', kwargs=kwargs)

    def watch_flow_cell_positions(self, **kwargs):
        return self.call('watch_flow_cell_positions', kwargs=kwargs)

    def reset_position(self, **kwargs):
        return self.call('reset_position', kwargs=kwargs)

    def basecaller_api(self, **kwargs):
        return self.call('basecaller_api', kwargs=kwargs)

    def get_guppy_info(self, **kwargs):
        return self.call('get_guppy_info', kwargs=kwargs)

    def get_version_info(self, **kwargs):
        return self.call('get_version_info', kwargs=kwargs)

    def list_protocol_output_dir_files(self, **kwargs):
        return self.call('list_protocol_output_dir_files', kwargs=kwargs)

    def create_directory(self, **kwargs):
        return self.call('create_directory', kwargs=kwargs)

    def get_disk_space_info(self, **kwargs):
        return self.call('get_disk_space_info', kwargs=kwargs)

    def get_default_output_directories(self, **kwargs):
        return self.call('get_default_output_directories', kwargs=kwargs)

    def stream_disk_space_info(self, **kwargs):
        return self.call('stream_disk_space_info', kwargs=kwargs)

    def get_barcode_kit_info(self, **kwargs):
        return self.call('get_barcode_kit_info', kwargs=kwargs)

    def get_lamp_kit_info(self, **kwargs):
        return self.call('get_lamp_kit_info', kwargs=kwargs)

    def get_barcode_keys(self, **kwargs):
        return self.call('get_barcode_keys', kwargs=kwargs)

    def get_flow_cell_types(self, **kwargs):
        return self.call('get_flow_cell_types', kwargs=kwargs)

    def get_sequencing_kits(self, **kwargs):
        return self.call('get_sequencing_kits', kwargs=kwargs)

    def add_simulated_device(self, **kwargs):
        return self.call('add_simulated_device', kwargs=kwargs)

    def remove_simulated_device(self, **kwargs):
        return self.call('remove_simulated_device', kwargs=kwargs)

    def local_authentication_token_path(self, **kwargs):
        return self.call('local_authentication_token_path', kwargs=kwargs)

    def get_alignment_reference_information(self, **kwargs):
        return self.call('get_alignment_reference_information', kwargs=kwargs)

    def association_device_code(self, **kwargs):
        return self.call('association_device_code', kwargs=kwargs)

    def apply_offline_association_unlock_code(self, **kwargs):
        return self.call('apply_offline_association_unlock_code', kwargs=kwargs)

    def find_protocols(self, **kwargs):
        return self.call('find_protocols', kwargs=kwargs)

    def list_settings_for_protocol(self, **kwargs):
        return self.call('list_settings_for_protocol', kwargs=kwargs)

    def get_features(self, **kwargs):
        return self.call('get_features', kwargs=kwargs)

    def set_features(self, **kwargs):
        return self.call('set_features', kwargs=kwargs)

    def restart_device_admin_service(self, **kwargs):
        return self.call('restart_device_admin_service', kwargs=kwargs)

    def check_bed_file(self, **kwargs):
        return self.call('check_bed_file', kwargs=kwargs)

    def find_basecall_configurations(self, **kwargs):
        return self.call('find_basecall_configurations', kwargs=kwargs)

    def check_path_info(self, **kwargs):
        return self.call('check_path_info', kwargs=kwargs)

