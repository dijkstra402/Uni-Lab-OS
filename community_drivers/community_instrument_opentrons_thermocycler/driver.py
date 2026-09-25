from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOpentronsThermocycler(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/thermocycling/opentrons_backend.py', 'class_name': 'OpentronsThermocyclerBackend', 'import_roots': [], 'candidate_methods': ['close_lid', 'deactivate_block', 'deactivate_lid', 'get_block_current_temperature', 'get_block_status', 'get_block_target_temperature', 'get_current_cycle_index', 'get_current_step_index', 'get_hold_time', 'get_lid_current_temperature', 'get_lid_open', 'get_lid_status', 'get_lid_target_temperature', 'get_total_cycle_count', 'get_total_step_count', 'open_lid', 'run_protocol', 'set_block_temperature', 'set_lid_temperature', 'setup', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Opentrons', 'model': 'Thermocycler', 'device_type_cn': '热循环仪', 'device_type_en': 'Thermocycler', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/thermocycling/opentrons_backend.py', 'class_name': 'OpentronsThermocyclerBackend', 'candidate_methods': ['close_lid', 'deactivate_block', 'deactivate_lid', 'get_block_current_temperature', 'get_block_status', 'get_block_target_temperature', 'get_current_cycle_index', 'get_current_step_index', 'get_hold_time', 'get_lid_current_temperature', 'get_lid_open', 'get_lid_status', 'get_lid_target_temperature', 'get_total_cycle_count', 'get_total_step_count', 'open_lid', 'run_protocol', 'set_block_temperature', 'set_lid_temperature', 'setup', 'stop']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def close_lid(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('close_lid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def deactivate_block(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('deactivate_block', kwargs={k: v for k, v in _kw.items() if v is not None})

    def deactivate_lid(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('deactivate_lid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_block_current_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_block_current_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_block_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_block_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_block_target_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_block_target_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_current_cycle_index(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_current_cycle_index', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_current_step_index(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_current_step_index', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_hold_time(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_hold_time', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_current_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_lid_current_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_open(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_lid_open', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_lid_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_target_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_lid_target_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_total_cycle_count(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_total_cycle_count', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_total_step_count(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_total_step_count', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open_lid(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open_lid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def run_protocol(self, protocol=None, block_max_volume=None, **kwargs):
        _kw = {'protocol': protocol, 'block_max_volume': block_max_volume}
        _kw.update(kwargs)
        return self.call('run_protocol', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_block_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_block_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_lid_temperature(self, temperature=None, **kwargs):
        _kw = {'temperature': temperature}
        _kw.update(kwargs)
        return self.call('set_lid_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

