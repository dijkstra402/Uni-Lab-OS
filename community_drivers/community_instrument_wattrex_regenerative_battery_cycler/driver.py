from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentWattrexRegenerativeBatteryCycler(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/WattRex__Battery-Cycler-Drivers', 'source_file': 'code/drv_epc/src/wattrex_driver_epc/drv_epc_device.py', 'class_name': 'DrvEpcDeviceC', 'import_roots': [], 'candidate_methods': ['read_can_buffer', 'set_cv_mode', 'set_cc_mode', 'set_cp_mode', 'set_wait_mode', 'disable', 'set_periodic', 'set_ls_volt_limit', 'set_ls_curr_limit', 'set_hs_volt_limit', 'set_ls_pwr_limit', 'set_temp_limit', 'get_data', 'get_properties', 'get_info', 'get_mode', 'get_status', 'get_elec_meas', 'get_temp_meas', 'get_ls_volt_limits', 'get_ls_curr_limits', 'get_hs_volt_limits', 'get_ls_pwr_limits', 'get_temp_limits', 'open', 'close'], 'action_targets': {}, 'metadata': {'repo': 'WattRex/Battery-Cycler-Drivers', 'repo_url': 'https://github.com/WattRex/Battery-Cycler-Drivers', 'brand': 'WattRex', 'model': 'Regenerative Battery Cycler', 'device_type_cn': '电池测试柜', 'device_type_en': 'Battery Test Cabinet', 'source_framework': '专用驱动', 'tag_id': '4427', 'tag_name': '电池测试柜', 'tag_name_en': 'Battery Test Cabinet', 'candidate_score': 254, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def read_can_buffer(self, **kwargs):
        return self.call('read_can_buffer', kwargs=kwargs)

    def set_cv_mode(self, **kwargs):
        return self.call('set_cv_mode', kwargs=kwargs)

    def set_cc_mode(self, **kwargs):
        return self.call('set_cc_mode', kwargs=kwargs)

    def set_cp_mode(self, **kwargs):
        return self.call('set_cp_mode', kwargs=kwargs)

    def set_wait_mode(self, **kwargs):
        return self.call('set_wait_mode', kwargs=kwargs)

    def disable(self, **kwargs):
        return self.call('disable', kwargs=kwargs)

    def set_periodic(self, **kwargs):
        return self.call('set_periodic', kwargs=kwargs)

    def set_ls_volt_limit(self, **kwargs):
        return self.call('set_ls_volt_limit', kwargs=kwargs)

    def set_ls_curr_limit(self, **kwargs):
        return self.call('set_ls_curr_limit', kwargs=kwargs)

    def set_hs_volt_limit(self, **kwargs):
        return self.call('set_hs_volt_limit', kwargs=kwargs)

    def set_ls_pwr_limit(self, **kwargs):
        return self.call('set_ls_pwr_limit', kwargs=kwargs)

    def set_temp_limit(self, **kwargs):
        return self.call('set_temp_limit', kwargs=kwargs)

    def get_data(self, **kwargs):
        return self.call('get_data', kwargs=kwargs)

    def get_properties(self, **kwargs):
        return self.call('get_properties', kwargs=kwargs)

    def get_info(self, **kwargs):
        return self.call('get_info', kwargs=kwargs)

    def get_mode(self, **kwargs):
        return self.call('get_mode', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def get_elec_meas(self, **kwargs):
        return self.call('get_elec_meas', kwargs=kwargs)

    def get_temp_meas(self, **kwargs):
        return self.call('get_temp_meas', kwargs=kwargs)

    def get_ls_volt_limits(self, **kwargs):
        return self.call('get_ls_volt_limits', kwargs=kwargs)

    def get_ls_curr_limits(self, **kwargs):
        return self.call('get_ls_curr_limits', kwargs=kwargs)

    def get_hs_volt_limits(self, **kwargs):
        return self.call('get_hs_volt_limits', kwargs=kwargs)

    def get_ls_pwr_limits(self, **kwargs):
        return self.call('get_ls_pwr_limits', kwargs=kwargs)

    def get_temp_limits(self, **kwargs):
        return self.call('get_temp_limits', kwargs=kwargs)

    def open(self, **kwargs):
        return self.call('open', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

