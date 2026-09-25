from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentCetoniNemesys(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/psyfood__pyqmix', 'source_file': 'pyqmix/pump.py', 'class_name': 'QmixPump', 'import_roots': [], 'candidate_methods': ['name', 'is_enabled', 'enable', 'disable', 'is_in_fault_state', 'clear_fault_state', 'is_calibration_finished', 'calibrate', 'n_pumps', 'set_volume_unit', 'get_volume_unit', 'volume_unit', 'volume_max', 'set_flow_unit', 'get_flow_unit', 'flow_unit', 'set_syringe_params', 'set_syringe_params_by_type', 'get_syringe_params', 'syringe_params', 'max_flow_rate', 'aspirate', 'dispense', 'set_fill_level', 'generate_flow', 'fill', 'empty', 'stop', 'stop_all_pumps', 'dosed_volume', 'get_fill_level', 'fill_level', 'current_flow_rate', 'is_pumping', 'has_valve', 'valve_handle', 'add_external_valve', 'remove_external_valve', 'drive_pos_counter', 'save_drive_pos_counter'], 'action_targets': {}, 'metadata': {'repo': 'psyfood/pyqmix', 'repo_url': 'https://github.com/psyfood/pyqmix', 'brand': 'Cetoni', 'model': 'neMESYS', 'device_type_cn': '注射泵', 'device_type_en': 'Syringe Pump', 'source_framework': '泵阀/液体处理', 'tag_id': '4413', 'tag_name': '注射泵', 'tag_name_en': 'Syringe Pump', 'candidate_score': 386, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def name(self, **kwargs):
        return self.call('name', kwargs=kwargs)

    def is_enabled(self, **kwargs):
        return self.call('is_enabled', kwargs=kwargs)

    def enable(self, **kwargs):
        return self.call('enable', kwargs=kwargs)

    def disable(self, **kwargs):
        return self.call('disable', kwargs=kwargs)

    def is_in_fault_state(self, **kwargs):
        return self.call('is_in_fault_state', kwargs=kwargs)

    def clear_fault_state(self, **kwargs):
        return self.call('clear_fault_state', kwargs=kwargs)

    def is_calibration_finished(self, **kwargs):
        return self.call('is_calibration_finished', kwargs=kwargs)

    def calibrate(self, **kwargs):
        return self.call('calibrate', kwargs=kwargs)

    def n_pumps(self, **kwargs):
        return self.call('n_pumps', kwargs=kwargs)

    def set_volume_unit(self, **kwargs):
        return self.call('set_volume_unit', kwargs=kwargs)

    def get_volume_unit(self, **kwargs):
        return self.call('get_volume_unit', kwargs=kwargs)

    def volume_unit(self, **kwargs):
        return self.call('volume_unit', kwargs=kwargs)

    def volume_max(self, **kwargs):
        return self.call('volume_max', kwargs=kwargs)

    def set_flow_unit(self, **kwargs):
        return self.call('set_flow_unit', kwargs=kwargs)

    def get_flow_unit(self, **kwargs):
        return self.call('get_flow_unit', kwargs=kwargs)

    def flow_unit(self, **kwargs):
        return self.call('flow_unit', kwargs=kwargs)

    def set_syringe_params(self, **kwargs):
        return self.call('set_syringe_params', kwargs=kwargs)

    def set_syringe_params_by_type(self, **kwargs):
        return self.call('set_syringe_params_by_type', kwargs=kwargs)

    def get_syringe_params(self, **kwargs):
        return self.call('get_syringe_params', kwargs=kwargs)

    def syringe_params(self, **kwargs):
        return self.call('syringe_params', kwargs=kwargs)

    def max_flow_rate(self, **kwargs):
        return self.call('max_flow_rate', kwargs=kwargs)

    def aspirate(self, **kwargs):
        return self.call('aspirate', kwargs=kwargs)

    def dispense(self, **kwargs):
        return self.call('dispense', kwargs=kwargs)

    def set_fill_level(self, **kwargs):
        return self.call('set_fill_level', kwargs=kwargs)

    def generate_flow(self, **kwargs):
        return self.call('generate_flow', kwargs=kwargs)

    def fill(self, **kwargs):
        return self.call('fill', kwargs=kwargs)

    def empty(self, **kwargs):
        return self.call('empty', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def stop_all_pumps(self, **kwargs):
        return self.call('stop_all_pumps', kwargs=kwargs)

    def dosed_volume(self, **kwargs):
        return self.call('dosed_volume', kwargs=kwargs)

    def get_fill_level(self, **kwargs):
        return self.call('get_fill_level', kwargs=kwargs)

    def fill_level(self, **kwargs):
        return self.call('fill_level', kwargs=kwargs)

    def current_flow_rate(self, **kwargs):
        return self.call('current_flow_rate', kwargs=kwargs)

    def is_pumping(self, **kwargs):
        return self.call('is_pumping', kwargs=kwargs)

    def has_valve(self, **kwargs):
        return self.call('has_valve', kwargs=kwargs)

    def valve_handle(self, **kwargs):
        return self.call('valve_handle', kwargs=kwargs)

    def add_external_valve(self, **kwargs):
        return self.call('add_external_valve', kwargs=kwargs)

    def remove_external_valve(self, **kwargs):
        return self.call('remove_external_valve', kwargs=kwargs)

    def drive_pos_counter(self, **kwargs):
        return self.call('drive_pos_counter', kwargs=kwargs)

    def save_drive_pos_counter(self, **kwargs):
        return self.call('save_drive_pos_counter', kwargs=kwargs)

