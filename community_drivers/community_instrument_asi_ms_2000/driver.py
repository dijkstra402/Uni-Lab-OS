from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAsiMs2000(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/nvladimus__kekse', 'source_file': 'devices/etl_controller_Optotune.py', 'class_name': 'ETLController', 'import_roots': [], 'candidate_methods': ['set_port', 'connect', 'close', 'calc_crc', 'handshake', 'firmwaretype', 'firmwarebranch', 'partnumber', 'current_upper', 'current_lower', 'firmwareversion', 'deviceid', 'gain', 'serialnumber', 'get_current', 'set_current', 'siggen_upper', 'siggen_lower', 'siggen_freq', 'temp_limits', 'focalpower', 'current_max', 'temp_reading', 'get_status', 'eeprom_read', 'analog_input', 'eeprom_write', 'eeprom_contents', 'mode'], 'action_targets': {}, 'metadata': {'repo': 'nvladimus/kekse', 'repo_url': 'https://github.com/nvladimus/kekse', 'brand': 'ASI', 'model': 'MS-2000', 'device_type_cn': '普通光学显微镜', 'device_type_en': 'Optical Microscope', 'source_framework': '专用驱动', 'tag_id': '4400', 'tag_name': '普通光学显微镜', 'tag_name_en': 'Optical Microscope', 'candidate_score': 270, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def set_port(self, **kwargs):
        return self.call('set_port', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def close(self, **kwargs):
        return self.call('close', kwargs=kwargs)

    def calc_crc(self, **kwargs):
        return self.call('calc_crc', kwargs=kwargs)

    def handshake(self, **kwargs):
        return self.call('handshake', kwargs=kwargs)

    def firmwaretype(self, **kwargs):
        return self.call('firmwaretype', kwargs=kwargs)

    def firmwarebranch(self, **kwargs):
        return self.call('firmwarebranch', kwargs=kwargs)

    def partnumber(self, **kwargs):
        return self.call('partnumber', kwargs=kwargs)

    def current_upper(self, **kwargs):
        return self.call('current_upper', kwargs=kwargs)

    def current_lower(self, **kwargs):
        return self.call('current_lower', kwargs=kwargs)

    def firmwareversion(self, **kwargs):
        return self.call('firmwareversion', kwargs=kwargs)

    def deviceid(self, **kwargs):
        return self.call('deviceid', kwargs=kwargs)

    def gain(self, **kwargs):
        return self.call('gain', kwargs=kwargs)

    def serialnumber(self, **kwargs):
        return self.call('serialnumber', kwargs=kwargs)

    def get_current(self, **kwargs):
        return self.call('get_current', kwargs=kwargs)

    def set_current(self, **kwargs):
        return self.call('set_current', kwargs=kwargs)

    def siggen_upper(self, **kwargs):
        return self.call('siggen_upper', kwargs=kwargs)

    def siggen_lower(self, **kwargs):
        return self.call('siggen_lower', kwargs=kwargs)

    def siggen_freq(self, **kwargs):
        return self.call('siggen_freq', kwargs=kwargs)

    def temp_limits(self, **kwargs):
        return self.call('temp_limits', kwargs=kwargs)

    def focalpower(self, **kwargs):
        return self.call('focalpower', kwargs=kwargs)

    def current_max(self, **kwargs):
        return self.call('current_max', kwargs=kwargs)

    def temp_reading(self, **kwargs):
        return self.call('temp_reading', kwargs=kwargs)

    def get_status(self, **kwargs):
        return self.call('get_status', kwargs=kwargs)

    def eeprom_read(self, **kwargs):
        return self.call('eeprom_read', kwargs=kwargs)

    def analog_input(self, **kwargs):
        return self.call('analog_input', kwargs=kwargs)

    def eeprom_write(self, **kwargs):
        return self.call('eeprom_write', kwargs=kwargs)

    def eeprom_contents(self, **kwargs):
        return self.call('eeprom_contents', kwargs=kwargs)

    def mode(self, **kwargs):
        return self.call('mode', kwargs=kwargs)

