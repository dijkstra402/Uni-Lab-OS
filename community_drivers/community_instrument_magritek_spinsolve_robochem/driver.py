from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMagritekSpinsolveRobochem(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/Noel-Research-Group__Robochem_v1.0', 'source_file': 'Platform_/Liquid_Handler/GX_241_Liquid_Handler.py', 'class_name': 'LiquidHandler', 'import_roots': [], 'candidate_methods': ['get_dll_version', 'immediate', 'buffered', 'request_module_identification', 'reset', 'home', 'Gilson_identification', 'get_error', 'clear_error', 'read_XYZ_coordinate', 'read_XY_coordinate', 'read_Z_coordinate', 'move_XY', 'move_XY_with_speed_and_drive', 'move_Z', 'move_Z_with_liquid_level_detection', 'read_syringe_info', 'read_motor_status', 'stop_syringe_pump', 'read_syringe_pump_status', 'switch_valve_position', 'read_valve_status', 'set_syringe_pump', 'get_sample_coordinate', 'take_single_sample', 'take_solvent', 'measure_cali', 'cleaning_test', 'clean_needle_tip', 'sample_mixing', 'clean_needle', 'prepare_reaction_sample_rack', 'prepare_reaction_sample'], 'action_targets': {}, 'metadata': {'repo': 'Noel-Research-Group/Robochem_v1.0', 'repo_url': 'https://github.com/Noel-Research-Group/Robochem_v1.0', 'brand': 'Magritek', 'model': 'Spinsolve (Robochem)', 'device_type_cn': '核磁共振波谱仪', 'device_type_en': 'Benchtop NMR', 'source_framework': 'Robochem', 'tag_id': '4404', 'tag_name': '核磁共振波谱仪', 'tag_name_en': 'NMR Spectrometer', 'candidate_score': 294, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def get_dll_version(self, **kwargs):
        return self.call('get_dll_version', kwargs=kwargs)

    def immediate(self, **kwargs):
        return self.call('immediate', kwargs=kwargs)

    def buffered(self, **kwargs):
        return self.call('buffered', kwargs=kwargs)

    def request_module_identification(self, **kwargs):
        return self.call('request_module_identification', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def home(self, **kwargs):
        return self.call('home', kwargs=kwargs)

    def Gilson_identification(self, **kwargs):
        return self.call('Gilson_identification', kwargs=kwargs)

    def get_error(self, **kwargs):
        return self.call('get_error', kwargs=kwargs)

    def clear_error(self, **kwargs):
        return self.call('clear_error', kwargs=kwargs)

    def read_XYZ_coordinate(self, **kwargs):
        return self.call('read_XYZ_coordinate', kwargs=kwargs)

    def read_XY_coordinate(self, **kwargs):
        return self.call('read_XY_coordinate', kwargs=kwargs)

    def read_Z_coordinate(self, **kwargs):
        return self.call('read_Z_coordinate', kwargs=kwargs)

    def move_XY(self, **kwargs):
        return self.call('move_XY', kwargs=kwargs)

    def move_XY_with_speed_and_drive(self, **kwargs):
        return self.call('move_XY_with_speed_and_drive', kwargs=kwargs)

    def move_Z(self, **kwargs):
        return self.call('move_Z', kwargs=kwargs)

    def move_Z_with_liquid_level_detection(self, **kwargs):
        return self.call('move_Z_with_liquid_level_detection', kwargs=kwargs)

    def read_syringe_info(self, **kwargs):
        return self.call('read_syringe_info', kwargs=kwargs)

    def read_motor_status(self, **kwargs):
        return self.call('read_motor_status', kwargs=kwargs)

    def stop_syringe_pump(self, **kwargs):
        return self.call('stop_syringe_pump', kwargs=kwargs)

    def read_syringe_pump_status(self, **kwargs):
        return self.call('read_syringe_pump_status', kwargs=kwargs)

    def switch_valve_position(self, **kwargs):
        return self.call('switch_valve_position', kwargs=kwargs)

    def read_valve_status(self, **kwargs):
        return self.call('read_valve_status', kwargs=kwargs)

    def set_syringe_pump(self, **kwargs):
        return self.call('set_syringe_pump', kwargs=kwargs)

    def get_sample_coordinate(self, **kwargs):
        return self.call('get_sample_coordinate', kwargs=kwargs)

    def take_single_sample(self, **kwargs):
        return self.call('take_single_sample', kwargs=kwargs)

    def take_solvent(self, **kwargs):
        return self.call('take_solvent', kwargs=kwargs)

    def measure_cali(self, **kwargs):
        return self.call('measure_cali', kwargs=kwargs)

    def cleaning_test(self, **kwargs):
        return self.call('cleaning_test', kwargs=kwargs)

    def clean_needle_tip(self, **kwargs):
        return self.call('clean_needle_tip', kwargs=kwargs)

    def sample_mixing(self, **kwargs):
        return self.call('sample_mixing', kwargs=kwargs)

    def clean_needle(self, **kwargs):
        return self.call('clean_needle', kwargs=kwargs)

    def prepare_reaction_sample_rack(self, **kwargs):
        return self.call('prepare_reaction_sample_rack', kwargs=kwargs)

    def prepare_reaction_sample(self, **kwargs):
        return self.call('prepare_reaction_sample', kwargs=kwargs)

