from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentIorodeoRodeostat(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/iorodeo__potentiostat', 'source_file': 'software/python/potentiostat/potentiostat/potentiostat.py', 'class_name': 'Potentiostat', 'import_roots': [], 'candidate_methods': ['get_hardware_variant', 'stop_test', 'get_volt', 'set_volt', 'get_curr', 'get_ref_volt', 'get_param', 'set_param', 'set_volt_range', 'get_volt_range', 'get_all_volt_range', 'set_curr_range', 'get_curr_range', 'get_all_curr_range', 'get_device_id', 'set_device_id', 'set_sample_period', 'get_sample_period', 'set_sample_rate', 'get_sample_rate', 'get_test_done_time', 'get_test_names', 'get_firmware_version', 'get_hardware_version', 'set_ref_elect_connected', 'get_ref_elect_connected', 'set_ctr_elect_connected', 'get_ctr_elect_connected', 'set_wrk_elect_connected', 'get_wrk_elect_connected', 'set_all_elect_connected', 'get_all_elect_connected', 'set_auto_connect', 'get_auto_connect', 'set_ref_elect_volt_range', 'get_ref_elect_volt_range', 'set_mux_enabled', 'get_mux_enabled', 'set_enabled_mux_channels', 'get_enabled_mux_channels', 'get_mux_test_names', 'set_mux_ref_elect_connected', 'get_mux_ref_elect_connected', 'set_mux_ctr_elect_connected', 'get_mux_ctr_elect_connected', 'set_mux_wrk_elect_connected', 'get_mux_wrk_elect_connected', 'disconnect_all_mux_elect', 'run_test', 'send_cmd', 'write', 'check_cmd_msg', 'check_for_success', 'check_cmd_match', 'check_test_match', 'check_hardware_version', 'atexit_cleanup'], 'action_targets': {}, 'metadata': {'repo': 'iorodeo/potentiostat', 'repo_url': 'https://github.com/iorodeo/potentiostat', 'brand': 'IoRodeo', 'model': 'Rodeostat', 'device_type_cn': '电化学反应器', 'device_type_en': 'Electrochemical Reactor', 'source_framework': '专用驱动', 'tag_id': '4424', 'tag_name': '电化学反应器', 'tag_name_en': 'Electrochemical Reactor', 'candidate_score': 506, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_hardware_variant(self, **kwargs):
        return self.call('get_hardware_variant', kwargs=kwargs)

    def stop_test(self, **kwargs):
        return self.call('stop_test', kwargs=kwargs)

    def get_volt(self, **kwargs):
        return self.call('get_volt', kwargs=kwargs)

    def set_volt(self, **kwargs):
        return self.call('set_volt', kwargs=kwargs)

    def get_curr(self, **kwargs):
        return self.call('get_curr', kwargs=kwargs)

    def get_ref_volt(self, **kwargs):
        return self.call('get_ref_volt', kwargs=kwargs)

    def get_param(self, **kwargs):
        return self.call('get_param', kwargs=kwargs)

    def set_param(self, **kwargs):
        return self.call('set_param', kwargs=kwargs)

    def set_volt_range(self, **kwargs):
        return self.call('set_volt_range', kwargs=kwargs)

    def get_volt_range(self, **kwargs):
        return self.call('get_volt_range', kwargs=kwargs)

    def get_all_volt_range(self, **kwargs):
        return self.call('get_all_volt_range', kwargs=kwargs)

    def set_curr_range(self, **kwargs):
        return self.call('set_curr_range', kwargs=kwargs)

    def get_curr_range(self, **kwargs):
        return self.call('get_curr_range', kwargs=kwargs)

    def get_all_curr_range(self, **kwargs):
        return self.call('get_all_curr_range', kwargs=kwargs)

    def get_device_id(self, **kwargs):
        return self.call('get_device_id', kwargs=kwargs)

    def set_device_id(self, **kwargs):
        return self.call('set_device_id', kwargs=kwargs)

    def set_sample_period(self, **kwargs):
        return self.call('set_sample_period', kwargs=kwargs)

    def get_sample_period(self, **kwargs):
        return self.call('get_sample_period', kwargs=kwargs)

    def set_sample_rate(self, **kwargs):
        return self.call('set_sample_rate', kwargs=kwargs)

    def get_sample_rate(self, **kwargs):
        return self.call('get_sample_rate', kwargs=kwargs)

    def get_test_done_time(self, **kwargs):
        return self.call('get_test_done_time', kwargs=kwargs)

    def get_test_names(self, **kwargs):
        return self.call('get_test_names', kwargs=kwargs)

    def get_firmware_version(self, **kwargs):
        return self.call('get_firmware_version', kwargs=kwargs)

    def get_hardware_version(self, **kwargs):
        return self.call('get_hardware_version', kwargs=kwargs)

    def set_ref_elect_connected(self, **kwargs):
        return self.call('set_ref_elect_connected', kwargs=kwargs)

    def get_ref_elect_connected(self, **kwargs):
        return self.call('get_ref_elect_connected', kwargs=kwargs)

    def set_ctr_elect_connected(self, **kwargs):
        return self.call('set_ctr_elect_connected', kwargs=kwargs)

    def get_ctr_elect_connected(self, **kwargs):
        return self.call('get_ctr_elect_connected', kwargs=kwargs)

    def set_wrk_elect_connected(self, **kwargs):
        return self.call('set_wrk_elect_connected', kwargs=kwargs)

    def get_wrk_elect_connected(self, **kwargs):
        return self.call('get_wrk_elect_connected', kwargs=kwargs)

    def set_all_elect_connected(self, **kwargs):
        return self.call('set_all_elect_connected', kwargs=kwargs)

    def get_all_elect_connected(self, **kwargs):
        return self.call('get_all_elect_connected', kwargs=kwargs)

    def set_auto_connect(self, **kwargs):
        return self.call('set_auto_connect', kwargs=kwargs)

    def get_auto_connect(self, **kwargs):
        return self.call('get_auto_connect', kwargs=kwargs)

    def set_ref_elect_volt_range(self, **kwargs):
        return self.call('set_ref_elect_volt_range', kwargs=kwargs)

    def get_ref_elect_volt_range(self, **kwargs):
        return self.call('get_ref_elect_volt_range', kwargs=kwargs)

    def set_mux_enabled(self, **kwargs):
        return self.call('set_mux_enabled', kwargs=kwargs)

    def get_mux_enabled(self, **kwargs):
        return self.call('get_mux_enabled', kwargs=kwargs)

    def set_enabled_mux_channels(self, **kwargs):
        return self.call('set_enabled_mux_channels', kwargs=kwargs)

    def get_enabled_mux_channels(self, **kwargs):
        return self.call('get_enabled_mux_channels', kwargs=kwargs)

    def get_mux_test_names(self, **kwargs):
        return self.call('get_mux_test_names', kwargs=kwargs)

    def set_mux_ref_elect_connected(self, **kwargs):
        return self.call('set_mux_ref_elect_connected', kwargs=kwargs)

    def get_mux_ref_elect_connected(self, **kwargs):
        return self.call('get_mux_ref_elect_connected', kwargs=kwargs)

    def set_mux_ctr_elect_connected(self, **kwargs):
        return self.call('set_mux_ctr_elect_connected', kwargs=kwargs)

    def get_mux_ctr_elect_connected(self, **kwargs):
        return self.call('get_mux_ctr_elect_connected', kwargs=kwargs)

    def set_mux_wrk_elect_connected(self, **kwargs):
        return self.call('set_mux_wrk_elect_connected', kwargs=kwargs)

    def get_mux_wrk_elect_connected(self, **kwargs):
        return self.call('get_mux_wrk_elect_connected', kwargs=kwargs)

    def disconnect_all_mux_elect(self, **kwargs):
        return self.call('disconnect_all_mux_elect', kwargs=kwargs)

    def run_test(self, **kwargs):
        return self.call('run_test', kwargs=kwargs)

    def send_cmd(self, **kwargs):
        return self.call('send_cmd', kwargs=kwargs)

    def write(self, **kwargs):
        return self.call('write', kwargs=kwargs)

    def check_cmd_msg(self, **kwargs):
        return self.call('check_cmd_msg', kwargs=kwargs)

    def check_for_success(self, **kwargs):
        return self.call('check_for_success', kwargs=kwargs)

    def check_cmd_match(self, **kwargs):
        return self.call('check_cmd_match', kwargs=kwargs)

    def check_test_match(self, **kwargs):
        return self.call('check_test_match', kwargs=kwargs)

    def check_hardware_version(self, **kwargs):
        return self.call('check_hardware_version', kwargs=kwargs)

    def atexit_cleanup(self, **kwargs):
        return self.call('atexit_cleanup', kwargs=kwargs)

