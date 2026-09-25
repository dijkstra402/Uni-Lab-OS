from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLiconicStx44Icbt(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/storage/liconic/liconic_backend.py', 'class_name': 'ExperimentalLiconicBackend', 'import_roots': [], 'candidate_methods': ['check_second_transfer_sensor', 'check_shovel_sensor', 'check_transfer_sensor', 'close_door', 'fetch_plate_to_loading_tray', 'get_co2_level', 'get_humidity', 'get_n2_level', 'get_shaker_speed', 'get_target_co2_level', 'get_target_humidity', 'get_target_n2_level', 'get_target_temperature', 'get_temperature', 'initialize', 'move_position_to_position', 'open_door', 'read_barcode_inline', 'scan_barcode', 'set_co2_level', 'set_humidity', 'set_n2_level', 'set_racks', 'set_temperature', 'setup', 'shaker_status', 'start_shaking', 'stop', 'stop_shaking', 'take_in_plate', 'turn_swap_station'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Liconic', 'model': 'STX44-ICBT', 'device_type_cn': '自动化培养箱', 'device_type_en': 'Automated Incubator', 'source_framework': 'PyLabRobot', 'tag_id': '4442', 'tag_name': '组织培养试验箱', 'tag_name_en': 'Tissue Culture Chamber', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/storage/liconic/liconic_backend.py', 'class_name': 'ExperimentalLiconicBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def check_second_transfer_sensor(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('check_second_transfer_sensor', kwargs={k: v for k, v in _kw.items() if v is not None})

    def check_shovel_sensor(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('check_shovel_sensor', kwargs={k: v for k, v in _kw.items() if v is not None})

    def check_transfer_sensor(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('check_transfer_sensor', kwargs={k: v for k, v in _kw.items() if v is not None})

    def close_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('close_door', kwargs={k: v for k, v in _kw.items() if v is not None})

    def fetch_plate_to_loading_tray(self, plate=None, read_barcode=None, **kwargs):
        _kw = {'plate': plate, 'read_barcode': read_barcode}
        _kw.update(kwargs)
        return self.call('fetch_plate_to_loading_tray', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_co2_level(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_co2_level', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_humidity(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_humidity', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_n2_level(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_n2_level', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_shaker_speed(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_shaker_speed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_target_co2_level(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_target_co2_level', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_target_humidity(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_target_humidity', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_target_n2_level(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_target_n2_level', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_target_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_target_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def move_position_to_position(self, plate=None, dest_site=None, read_barcode=None, **kwargs):
        _kw = {'plate': plate, 'dest_site': dest_site, 'read_barcode': read_barcode}
        _kw.update(kwargs)
        return self.call('move_position_to_position', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open_door', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_barcode_inline(self, cassette=None, plt_position=None, **kwargs):
        _kw = {'cassette': cassette, 'plt_position': plt_position}
        _kw.update(kwargs)
        return self.call('read_barcode_inline', kwargs={k: v for k, v in _kw.items() if v is not None})

    def scan_barcode(self, site=None, **kwargs):
        _kw = {'site': site}
        _kw.update(kwargs)
        return self.call('scan_barcode', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_co2_level(self, co2_level=None, **kwargs):
        _kw = {'co2_level': co2_level}
        _kw.update(kwargs)
        return self.call('set_co2_level', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_humidity(self, humidity=None, **kwargs):
        _kw = {'humidity': humidity}
        _kw.update(kwargs)
        return self.call('set_humidity', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_n2_level(self, n2_level=None, **kwargs):
        _kw = {'n2_level': n2_level}
        _kw.update(kwargs)
        return self.call('set_n2_level', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_racks(self, racks=None, **kwargs):
        _kw = {'racks': racks}
        _kw.update(kwargs)
        return self.call('set_racks', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def shaker_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('shaker_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def start_shaking(self, frequency=None, **kwargs):
        _kw = {'frequency': frequency}
        _kw.update(kwargs)
        return self.call('start_shaking', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop_shaking(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop_shaking', kwargs={k: v for k, v in _kw.items() if v is not None})

    def take_in_plate(self, plate=None, site=None, read_barcode=None, **kwargs):
        _kw = {'plate': plate, 'site': site, 'read_barcode': read_barcode}
        _kw.update(kwargs)
        return self.call('take_in_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def turn_swap_station(self, home=None, **kwargs):
        _kw = {'home': home}
        _kw.update(kwargs)
        return self.call('turn_swap_station', kwargs={k: v for k, v in _kw.items() if v is not None})

