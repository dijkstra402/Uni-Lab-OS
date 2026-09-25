from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentEspecP300Scp220(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/EspecNorthAmerica__ChamberConnectLibrary', 'source_file': 'chamberconnectlibrary/watlowf4.py', 'class_name': 'WatlowF4', 'import_roots': [], 'candidate_methods': ['connect', 'close', 'raw', 'get_datetime', 'set_datetime', 'get_refrig', 'set_refrig', 'get_loop_sp', 'set_loop_sp', 'get_loop_pv', 'get_loop_range', 'set_loop_range', 'get_loop_en', 'set_loop_en', 'get_loop_units', 'get_loop_mode', 'get_loop_modes', 'set_loop_mode', 'get_loop_power', 'set_loop_power', 'get_cascade_sp', 'set_cascade_sp', 'get_cascade_pv', 'get_cascade_range', 'set_cascade_range', 'get_cascade_en', 'set_cascade_en', 'get_cascade_units', 'get_cascade_mode', 'get_cascade_modes', 'set_cascade_mode', 'get_cascade_ctl', 'set_cascade_ctl', 'get_cascade_deviation', 'set_cascade_deviation', 'get_cascade_power', 'set_cascade_power', 'get_event', 'set_event', 'get_status', 'get_alarm_status', 'const_start', 'stop', 'prgm_start', 'prgm_pause', 'prgm_resume', 'get_prgm_counter', 'prgm_next_step', 'get_prgm_cur', 'get_prgm_cstep', 'get_prgm_cstime', 'get_prgm_time', 'get_prgm_name', 'set_prgm_name', 'get_prgm_steps', 'get_prgms', 'get_prgm', 'set_prgm', 'prgm_delete', 'process_controller', 'get_network_settings', 'set_network_settings', 'get_operation_modes'], 'action_targets': {}, 'metadata': {'repo': 'EspecNorthAmerica/ChamberConnectLibrary', 'repo_url': 'https://github.com/EspecNorthAmerica/ChamberConnectLibrary', 'brand': 'Espec', 'model': 'P300/SCP-220控制器', 'device_type_cn': '环境试验箱', 'device_type_en': 'Environmental Test Chamber', 'source_framework': '环境控制/传感器', 'tag_id': '4387', 'tag_name': '微生物培养箱', 'tag_name_en': 'Microbial Incubator', 'candidate_score': 550, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def raw(self, **kwargs):
        return self.call('raw', kwargs=kwargs)

    def get_datetime(self, **kwargs):
        return self.call('get_datetime', kwargs=kwargs)

    def set_datetime(self, **kwargs):
        return self.call('set_datetime', kwargs=kwargs)

    def get_refrig(self, **kwargs):
        return self.call('get_refrig', kwargs=kwargs)

    def set_refrig(self, **kwargs):
        return self.call('set_refrig', kwargs=kwargs)

    def get_loop_sp(self, **kwargs):
        return self.call('get_loop_sp', kwargs=kwargs)

    def set_loop_sp(self, **kwargs):
        return self.call('set_loop_sp', kwargs=kwargs)

    def get_loop_pv(self, **kwargs):
        return self.call('get_loop_pv', kwargs=kwargs)

    def get_loop_range(self, **kwargs):
        return self.call('get_loop_range', kwargs=kwargs)

    def set_loop_range(self, **kwargs):
        return self.call('set_loop_range', kwargs=kwargs)

    def get_loop_en(self, **kwargs):
        return self.call('get_loop_en', kwargs=kwargs)

    def set_loop_en(self, **kwargs):
        return self.call('set_loop_en', kwargs=kwargs)

    def get_loop_units(self, **kwargs):
        return self.call('get_loop_units', kwargs=kwargs)

    def get_loop_mode(self, **kwargs):
        return self.call('get_loop_mode', kwargs=kwargs)

    def get_loop_modes(self, **kwargs):
        return self.call('get_loop_modes', kwargs=kwargs)

    def set_loop_mode(self, **kwargs):
        return self.call('set_loop_mode', kwargs=kwargs)

    def get_loop_power(self, **kwargs):
        return self.call('get_loop_power', kwargs=kwargs)

    def set_loop_power(self, **kwargs):
        return self.call('set_loop_power', kwargs=kwargs)

    def get_cascade_sp(self, **kwargs):
        return self.call('get_cascade_sp', kwargs=kwargs)

    def set_cascade_sp(self, **kwargs):
        return self.call('set_cascade_sp', kwargs=kwargs)

    def get_cascade_pv(self, **kwargs):
        return self.call('get_cascade_pv', kwargs=kwargs)

    def get_cascade_range(self, **kwargs):
        return self.call('get_cascade_range', kwargs=kwargs)

    def set_cascade_range(self, **kwargs):
        return self.call('set_cascade_range', kwargs=kwargs)

    def get_cascade_en(self, **kwargs):
        return self.call('get_cascade_en', kwargs=kwargs)

    def set_cascade_en(self, **kwargs):
        return self.call('set_cascade_en', kwargs=kwargs)

    def get_cascade_units(self, **kwargs):
        return self.call('get_cascade_units', kwargs=kwargs)

    def get_cascade_mode(self, **kwargs):
        return self.call('get_cascade_mode', kwargs=kwargs)

    def get_cascade_modes(self, **kwargs):
        return self.call('get_cascade_modes', kwargs=kwargs)

    def set_cascade_mode(self, **kwargs):
        return self.call('set_cascade_mode', kwargs=kwargs)

    def get_cascade_ctl(self, **kwargs):
        return self.call('get_cascade_ctl', kwargs=kwargs)

    def set_cascade_ctl(self, **kwargs):
        return self.call('set_cascade_ctl', kwargs=kwargs)

    def get_cascade_deviation(self, **kwargs):
        return self.call('get_cascade_deviation', kwargs=kwargs)

    def set_cascade_deviation(self, **kwargs):
        return self.call('set_cascade_deviation', kwargs=kwargs)

    def get_cascade_power(self, **kwargs):
        return self.call('get_cascade_power', kwargs=kwargs)

    def set_cascade_power(self, **kwargs):
        return self.call('set_cascade_power', kwargs=kwargs)

    def get_event(self, **kwargs):
        return self.call('get_event', kwargs=kwargs)

    def set_event(self, **kwargs):
        return self.call('set_event', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def get_alarm_status(self, **kwargs):
        return self.call('get_alarm_status', kwargs=kwargs)

    def const_start(self, **kwargs):
        return self.call('const_start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def prgm_start(self, **kwargs):
        return self.call('prgm_start', kwargs=kwargs)

    def prgm_pause(self, **kwargs):
        return self.call('prgm_pause', kwargs=kwargs)

    def prgm_resume(self, **kwargs):
        return self.call('prgm_resume', kwargs=kwargs)

    def get_prgm_counter(self, **kwargs):
        return self.call('get_prgm_counter', kwargs=kwargs)

    def prgm_next_step(self, **kwargs):
        return self.call('prgm_next_step', kwargs=kwargs)

    def get_prgm_cur(self, **kwargs):
        return self.call('get_prgm_cur', kwargs=kwargs)

    def get_prgm_cstep(self, **kwargs):
        return self.call('get_prgm_cstep', kwargs=kwargs)

    def get_prgm_cstime(self, **kwargs):
        return self.call('get_prgm_cstime', kwargs=kwargs)

    def get_prgm_time(self, **kwargs):
        return self.call('get_prgm_time', kwargs=kwargs)

    def get_prgm_name(self, **kwargs):
        return self.call('get_prgm_name', kwargs=kwargs)

    def set_prgm_name(self, **kwargs):
        return self.call('set_prgm_name', kwargs=kwargs)

    def get_prgm_steps(self, **kwargs):
        return self.call('get_prgm_steps', kwargs=kwargs)

    def get_prgms(self, **kwargs):
        return self.call('get_prgms', kwargs=kwargs)

    def get_prgm(self, **kwargs):
        return self.call('get_prgm', kwargs=kwargs)

    def set_prgm(self, **kwargs):
        return self.call('set_prgm', kwargs=kwargs)

    def prgm_delete(self, **kwargs):
        return self.call('prgm_delete', kwargs=kwargs)

    def process_controller(self, **kwargs):
        return self.call('process_controller', kwargs=kwargs)

    def get_network_settings(self, **kwargs):
        return self.call('get_network_settings', kwargs=kwargs)

    def set_network_settings(self, **kwargs):
        return self.call('set_network_settings', kwargs=kwargs)

    def get_operation_modes(self, **kwargs):
        return self.call('get_operation_modes', kwargs=kwargs)

