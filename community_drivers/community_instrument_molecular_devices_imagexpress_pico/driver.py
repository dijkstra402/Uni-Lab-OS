from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMolecularDevicesImagexpressPico(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/microscopes/molecular_devices/pico/backend.py', 'class_name': 'ExperimentalPicoBackend', 'import_roots': [], 'candidate_methods': ['capture', 'change_filter_cube', 'change_objective', 'close_door', 'enter_objective_maintenance', 'exit_objective_maintenance', 'get_available_filter_cubes', 'get_available_objectives', 'get_configuration', 'open_door', 'setup', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Molecular Devices', 'model': 'ImageXpress Pico', 'device_type_cn': '高内涵细胞成像分析系统', 'device_type_en': 'High Content Cell Imaging Analysis System', 'source_framework': 'PyLabRobot', 'tag_id': '4460', 'tag_name': '高内涵细胞成像分析系统', 'tag_name_en': 'High Content Cell Imaging Analysis System', 'candidate_score': 2318, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}, 'source_file': 'pylabrobot/microscopes/molecular_devices/pico/backend.py', 'class_name': 'ExperimentalPicoBackend'}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def capture(self, row=None, column=None, mode=None, objective=None, exposure_time=None, focal_height=None, gain=None, plate=None, **kwargs):
        _kw = {'row': row, 'column': column, 'mode': mode, 'objective': objective, 'exposure_time': exposure_time, 'focal_height': focal_height, 'gain': gain, 'plate': plate}
        _kw.update(kwargs)
        return self.call('capture', kwargs={k: v for k, v in _kw.items() if v is not None})

    def change_filter_cube(self, position=None, filter_cube_id=None, **kwargs):
        _kw = {'position': position, 'filter_cube_id': filter_cube_id}
        _kw.update(kwargs)
        return self.call('change_filter_cube', kwargs={k: v for k, v in _kw.items() if v is not None})

    def change_objective(self, position=None, objective_id=None, **kwargs):
        _kw = {'position': position, 'objective_id': objective_id}
        _kw.update(kwargs)
        return self.call('change_objective', kwargs={k: v for k, v in _kw.items() if v is not None})

    def close_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('close_door', kwargs={k: v for k, v in _kw.items() if v is not None})

    def enter_objective_maintenance(self, position=None, **kwargs):
        _kw = {'position': position}
        _kw.update(kwargs)
        return self.call('enter_objective_maintenance', kwargs={k: v for k, v in _kw.items() if v is not None})

    def exit_objective_maintenance(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('exit_objective_maintenance', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_available_filter_cubes(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_available_filter_cubes', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_available_objectives(self, position=None, **kwargs):
        _kw = {'position': position}
        _kw.update(kwargs)
        return self.call('get_available_objectives', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_configuration(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_configuration', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open_door(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open_door', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

