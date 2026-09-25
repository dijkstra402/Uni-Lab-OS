from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThermoCytomat2c450Shake(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/storage/cytomat/heraeus_cytomat_backend.py', 'class_name': 'HeraeusCytomatBackend', 'import_roots': [], 'candidate_methods': ['close_door', 'fetch_plate_to_loading_tray', 'get_temperature', 'initialize', 'open_door', 'read_plate_detection_xfer', 'set_racks', 'set_temperature', 'setup', 'start_shaking', 'stop', 'stop_shaking', 'take_in_plate', 'wait_for_transfer_station'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Thermo Fisher', 'model': 'Cytomat 2 C450_SHAKE', 'device_type_cn': '存储孵育器', 'device_type_en': 'Storage Incubator', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/storage/cytomat/heraeus_cytomat_backend.py', 'class_name': 'HeraeusCytomatBackend', 'candidate_methods': ['close_door', 'fetch_plate_to_loading_tray', 'get_temperature', 'initialize', 'open_door', 'read_plate_detection_xfer', 'set_racks', 'set_temperature', 'setup', 'start_shaking', 'stop', 'stop_shaking', 'take_in_plate', 'wait_for_transfer_station']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('close_door', kwargs={k: v for k, v in _kw.items() if v is not None})

    def fetch_plate_to_loading_tray(self, plate=None, **kwargs):
        _kw = {'plate': plate}
        _kw.update(kwargs)
        return self.call('fetch_plate_to_loading_tray', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def initialize(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('initialize', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open_door', kwargs={k: v for k, v in _kw.items() if v is not None})

    def read_plate_detection_xfer(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('read_plate_detection_xfer', kwargs={k: v for k, v in _kw.items() if v is not None})

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

    def take_in_plate(self, plate=None, site=None, **kwargs):
        _kw = {'plate': plate, 'site': site}
        _kw.update(kwargs)
        return self.call('take_in_plate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def wait_for_transfer_station(self, occupied=None, **kwargs):
        _kw = {'occupied': occupied}
        _kw.update(kwargs)
        return self.call('wait_for_transfer_station', kwargs={k: v for k, v in _kw.items() if v is not None})

