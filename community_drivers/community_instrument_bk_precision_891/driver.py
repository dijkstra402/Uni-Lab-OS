from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBkPrecision891(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/mcimech__bk891', 'source_file': 'bkp891/scpi891.py', 'class_name': 'ScpiConnection', 'import_roots': [], 'candidate_methods': ['close', 'sendcmd', 'calibrate', 'get_calibrate', 'set_displayfont', 'get_displayfont', 'set_displaymode', 'get_displaymode', 'set_displaypage', 'get_displaypage', 'fetch', 'set_format', 'get_format', 'set_frequency', 'get_frequency', 'set_aclevel', 'get_aclevel', 'set_function', 'get_function', 'set_speed', 'get_speed', 'set_measrange', 'get_measrange', 'set_brightness', 'get_brightness', 'set_beeper', 'get_beeper', 'set_date', 'get_date', 'set_time', 'get_time', 'get_error', 'get_instrument', 'clear_instrument', 'reset', 'save_configuration', 'recall_configuration'], 'action_targets': {}, 'metadata': {'repo': 'mcimech/bk891', 'repo_url': 'https://github.com/mcimech/bk891', 'brand': 'BK Precision', 'model': '891', 'device_type_cn': 'LCR表', 'device_type_en': 'LCR Meter', 'source_framework': '电化学/热分析/天平', 'tag_id': '4365', 'tag_name': '介电常数测定仪', 'tag_name_en': 'Dielectric Constant Meter', 'candidate_score': 334, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def sendcmd(self, **kwargs):
        return self.call('sendcmd', kwargs=kwargs)

    def calibrate(self, **kwargs):
        return self.call('calibrate', kwargs=kwargs)

    def get_calibrate(self, **kwargs):
        return self.call('get_calibrate', kwargs=kwargs)

    def set_displayfont(self, **kwargs):
        return self.call('set_displayfont', kwargs=kwargs)

    def get_displayfont(self, **kwargs):
        return self.call('get_displayfont', kwargs=kwargs)

    def set_displaymode(self, **kwargs):
        return self.call('set_displaymode', kwargs=kwargs)

    def get_displaymode(self, **kwargs):
        return self.call('get_displaymode', kwargs=kwargs)

    def set_displaypage(self, **kwargs):
        return self.call('set_displaypage', kwargs=kwargs)

    def get_displaypage(self, **kwargs):
        return self.call('get_displaypage', kwargs=kwargs)

    def fetch(self, **kwargs):
        return self.call('fetch', kwargs=kwargs)

    def set_format(self, **kwargs):
        return self.call('set_format', kwargs=kwargs)

    def get_format(self, **kwargs):
        return self.call('get_format', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def get_frequency(self, **kwargs):
        return self.call('get_frequency', kwargs=kwargs)

    def set_aclevel(self, **kwargs):
        return self.call('set_aclevel', kwargs=kwargs)

    def get_aclevel(self, **kwargs):
        return self.call('get_aclevel', kwargs=kwargs)

    def set_function(self, **kwargs):
        return self.call('set_function', kwargs=kwargs)

    def get_function(self, **kwargs):
        return self.call('get_function', kwargs=kwargs)

    def set_speed(self, **kwargs):
        return self.call('set_speed', kwargs=kwargs)

    def get_speed(self, **kwargs):
        return self.call('get_speed', kwargs=kwargs)

    def set_measrange(self, **kwargs):
        return self.call('set_measrange', kwargs=kwargs)

    def get_measrange(self, **kwargs):
        return self.call('get_measrange', kwargs=kwargs)

    def set_brightness(self, **kwargs):
        return self.call('set_brightness', kwargs=kwargs)

    def get_brightness(self, **kwargs):
        return self.call('get_brightness', kwargs=kwargs)

    def set_beeper(self, **kwargs):
        return self.call('set_beeper', kwargs=kwargs)

    def get_beeper(self, **kwargs):
        return self.call('get_beeper', kwargs=kwargs)

    def set_date(self, **kwargs):
        return self.call('set_date', kwargs=kwargs)

    def get_date(self, **kwargs):
        return self.call('get_date', kwargs=kwargs)

    def set_time(self, **kwargs):
        return self.call('set_time', kwargs=kwargs)

    def get_time(self, **kwargs):
        return self.call('get_time', kwargs=kwargs)

    def get_error(self, **kwargs):
        return self.call('get_error', kwargs=kwargs)

    def get_instrument(self, **kwargs):
        return self.call('get_instrument', kwargs=kwargs)

    def clear_instrument(self, **kwargs):
        return self.call('clear_instrument', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def save_configuration(self, **kwargs):
        return self.call('save_configuration', kwargs=kwargs)

    def recall_configuration(self, **kwargs):
        return self.call('recall_configuration', kwargs=kwargs)

