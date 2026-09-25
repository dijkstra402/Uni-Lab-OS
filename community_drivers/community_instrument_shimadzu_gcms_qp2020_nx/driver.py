from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentShimadzuGcmsQp2020Nx(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/RBCanty__MIT_AMD_Platform', 'source_file': 'Shell_AH/Evoware_API/evoware_api_support.py', 'class_name': 'EVO', 'import_roots': [], 'candidate_methods': ['cancel_process', 'execute_script_command', 'get_device', 'get_device_count', 'get_lc_count', 'get_lc_info', 'get_number_of_racks', 'get_process_status', 'get_process_status_ex', 'get_process_variable', 'get_rack', 'get_script_status', 'get_script_status_ex', 'get_script_variable', 'get_status', 'get_sub_lc_count', 'get_sub_lc_info', 'get_system_info', 'get_window_handle', 'hide_gui', 'initialize', 'logoff', 'logon', 'pause', 'prepare_process', 'prepare_script', 'read_liquid_classes', 'reset_stored_adh_info', 'resume', 'set_door_locks', 'set_lamp', 'set_process_variable', 'set_rack', 'set_remote_mode', 'set_script_variable', 'shutdown', 'start_adh', 'start_adh_load_process', 'start_adh_unload_process', 'start_script', 'stop', 'write_to_trace_file', 'error_event'], 'action_targets': {}, 'metadata': {'repo': 'RBCanty/MIT_AMD_Platform', 'repo_url': 'https://github.com/RBCanty/MIT_AMD_Platform', 'brand': 'Shimadzu', 'model': 'GCMS-QP2020 NX', 'device_type_cn': '气质联用仪', 'device_type_en': 'GC-MS', 'source_framework': 'MIT-AMD', 'tag_id': '4411', 'tag_name': '气相色谱质谱联用仪', 'tag_name_en': 'GC-MS', 'candidate_score': 374, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def cancel_process(self, **kwargs):
        return self.call('cancel_process', kwargs=kwargs)

    def execute_script_command(self, **kwargs):
        return self.call('execute_script_command', kwargs=kwargs)

    def get_device(self, **kwargs):
        return self.call('get_device', kwargs=kwargs)

    def get_device_count(self, **kwargs):
        return self.call('get_device_count', kwargs=kwargs)

    def get_lc_count(self, **kwargs):
        return self.call('get_lc_count', kwargs=kwargs)

    def get_lc_info(self, **kwargs):
        return self.call('get_lc_info', kwargs=kwargs)

    def get_number_of_racks(self, **kwargs):
        return self.call('get_number_of_racks', kwargs=kwargs)

    def get_process_status(self, **kwargs):
        return self.call('get_process_status', kwargs=kwargs)

    def get_process_status_ex(self, **kwargs):
        return self.call('get_process_status_ex', kwargs=kwargs)

    def get_process_variable(self, **kwargs):
        return self.call('get_process_variable', kwargs=kwargs)

    def get_rack(self, **kwargs):
        return self.call('get_rack', kwargs=kwargs)

    def get_script_status(self, **kwargs):
        return self.call('get_script_status', kwargs=kwargs)

    def get_script_status_ex(self, **kwargs):
        return self.call('get_script_status_ex', kwargs=kwargs)

    def get_script_variable(self, **kwargs):
        return self.call('get_script_variable', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def get_sub_lc_count(self, **kwargs):
        return self.call('get_sub_lc_count', kwargs=kwargs)

    def get_sub_lc_info(self, **kwargs):
        return self.call('get_sub_lc_info', kwargs=kwargs)

    def get_system_info(self, **kwargs):
        return self.call('get_system_info', kwargs=kwargs)

    def get_window_handle(self, **kwargs):
        return self.call('get_window_handle', kwargs=kwargs)

    def hide_gui(self, **kwargs):
        return self.call('hide_gui', kwargs=kwargs)

    def initialize(self, **kwargs):
        return self.call('initialize', kwargs=kwargs)

    def logoff(self, **kwargs):
        return self.call('logoff', kwargs=kwargs)

    def logon(self, **kwargs):
        return self.call('logon', kwargs=kwargs)

    def pause(self, **kwargs):
        return self.call('pause', kwargs=kwargs)

    def prepare_process(self, **kwargs):
        return self.call('prepare_process', kwargs=kwargs)

    def prepare_script(self, **kwargs):
        return self.call('prepare_script', kwargs=kwargs)

    def read_liquid_classes(self, **kwargs):
        return self.call('read_liquid_classes', kwargs=kwargs)

    def reset_stored_adh_info(self, **kwargs):
        return self.call('reset_stored_adh_info', kwargs=kwargs)

    def resume(self, **kwargs):
        return self.call('resume', kwargs=kwargs)

    def set_door_locks(self, **kwargs):
        return self.call('set_door_locks', kwargs=kwargs)

    def set_lamp(self, **kwargs):
        return self.call('set_lamp', kwargs=kwargs)

    def set_process_variable(self, **kwargs):
        return self.call('set_process_variable', kwargs=kwargs)

    def set_rack(self, **kwargs):
        return self.call('set_rack', kwargs=kwargs)

    def set_remote_mode(self, **kwargs):
        return self.call('set_remote_mode', kwargs=kwargs)

    def set_script_variable(self, **kwargs):
        return self.call('set_script_variable', kwargs=kwargs)

    def shutdown(self, **kwargs):
        return self.call('shutdown', kwargs=kwargs)

    def start_adh(self, **kwargs):
        return self.call('start_adh', kwargs=kwargs)

    def start_adh_load_process(self, **kwargs):
        return self.call('start_adh_load_process', kwargs=kwargs)

    def start_adh_unload_process(self, **kwargs):
        return self.call('start_adh_unload_process', kwargs=kwargs)

    def start_script(self, **kwargs):
        return self.call('start_script', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def write_to_trace_file(self, **kwargs):
        return self.call('write_to_trace_file', kwargs=kwargs)

    def error_event(self, **kwargs):
        return self.call('error_event', kwargs=kwargs)

