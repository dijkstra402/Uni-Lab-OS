from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentKeysightE4980al(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/mitle__keysight_e4980al', 'source_file': 'keysight_e4980al.py', 'class_name': 'e4980al', 'import_roots': [], 'candidate_methods': ['select_instrument', 'init_instrument', 'meas_type', 'meas_type_valid', 'set_meas_freq', 'set_meas_voltage', 'set_bias_voltage', 'set_trig_mode', 'trigger', 'aperture', 'clear_display', 'enable_display', 'set_comment', 'disp_page', 'get_log_list', 'get_lin_list', 'fetch', 'beep_type', 'beep_enable', 'beep', 'meas_point', 'manual_list_measure'], 'action_targets': {}, 'metadata': {'repo': 'mitle/keysight_e4980al', 'repo_url': 'https://github.com/mitle/keysight_e4980al', 'brand': 'Keysight', 'model': 'E4980AL', 'device_type_cn': '介电常数测定仪', 'device_type_en': 'Dielectric Constant Meter', 'source_framework': '专用驱动', 'tag_id': '4365', 'tag_name': '介电常数测定仪', 'tag_name_en': 'Dielectric Constant Meter', 'candidate_score': 264, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def select_instrument(self, **kwargs):
        return self.call('select_instrument', kwargs=kwargs)

    def init_instrument(self, **kwargs):
        return self.call('init_instrument', kwargs=kwargs)

    def meas_type(self, **kwargs):
        return self.call('meas_type', kwargs=kwargs)

    def meas_type_valid(self, **kwargs):
        return self.call('meas_type_valid', kwargs=kwargs)

    def set_meas_freq(self, **kwargs):
        return self.call('set_meas_freq', kwargs=kwargs)

    def set_meas_voltage(self, **kwargs):
        return self.call('set_meas_voltage', kwargs=kwargs)

    def set_bias_voltage(self, **kwargs):
        return self.call('set_bias_voltage', kwargs=kwargs)

    def set_trig_mode(self, **kwargs):
        return self.call('set_trig_mode', kwargs=kwargs)

    def trigger(self, **kwargs):
        return self.call('trigger', kwargs=kwargs)

    def aperture(self, **kwargs):
        return self.call('aperture', kwargs=kwargs)

    def clear_display(self, **kwargs):
        return self.call('clear_display', kwargs=kwargs)

    def enable_display(self, **kwargs):
        return self.call('enable_display', kwargs=kwargs)

    def set_comment(self, **kwargs):
        return self.call('set_comment', kwargs=kwargs)

    def disp_page(self, **kwargs):
        return self.call('disp_page', kwargs=kwargs)

    def get_log_list(self, **kwargs):
        return self.call('get_log_list', kwargs=kwargs)

    def get_lin_list(self, **kwargs):
        return self.call('get_lin_list', kwargs=kwargs)

    def fetch(self, **kwargs):
        return self.call('fetch', kwargs=kwargs)

    def beep_type(self, **kwargs):
        return self.call('beep_type', kwargs=kwargs)

    def beep_enable(self, **kwargs):
        return self.call('beep_enable', kwargs=kwargs)

    def beep(self, **kwargs):
        return self.call('beep', kwargs=kwargs)

    def meas_point(self, **kwargs):
        return self.call('meas_point', kwargs=kwargs)

    def manual_list_measure(self, **kwargs):
        return self.call('manual_list_measure', kwargs=kwargs)

