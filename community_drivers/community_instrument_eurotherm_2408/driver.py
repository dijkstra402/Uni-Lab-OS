from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentEurotherm2408(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/badarirao__Eurotemp', 'source_file': 'controller.py', 'class_name': 'MainWindow', 'import_roots': [], 'candidate_methods': ['connect_instrument', 'disable_editing', 'display_current_heating_program', 'feed_parameters', 'run_program', 'stop_program', 'save_heating_info', 'hold_program', 'continue_program', 'get_instrument_status', 'get_controller_data', 'display_status', 'clear_parameters', 'manual_heating', 'Rt_to_Rr', 'get_parameters', 'send_parameters', 'new_menu', 'open_new_parameter_file', 'open_menu', 'load_parameters_from_file', 'save_menu', 'save_parameters_to_file', 'savefile', 'exit_menu', 'manual_heatingRate', 'manual_heatingRate_dialogue', 'default_manualTemperature', 'manual_temperature_dialogue', 'com1_menu', 'com2_menu', 'com3_menu', 'com4_menu', 'Enter_Manually_menu', 'manual_entry_dialogue', 'set_instrument_address', 'load_settings', 'initialize_plot', 'plot', 'plot_realtime_data', 'update_plot_data', 'initialize_plot_data', 'isfloat', 'store_software_close_event', 'closeEvent', 'setupUi', 'retranslateUi'], 'action_targets': {}, 'metadata': {'repo': 'badarirao/Eurotemp', 'repo_url': 'https://github.com/badarirao/Eurotemp', 'brand': 'Eurotherm', 'model': '2408', 'device_type_cn': '箱式电阻炉', 'device_type_en': 'Box Resistance Furnace', 'source_framework': '专用驱动', 'tag_id': '4438', 'tag_name': '箱式电阻炉', 'tag_name_en': 'Box Resistance Furnace', 'candidate_score': 390, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect_instrument(self, **kwargs):
        return self.call('connect_instrument', kwargs=kwargs)

    def disable_editing(self, **kwargs):
        return self.call('disable_editing', kwargs=kwargs)

    def display_current_heating_program(self, **kwargs):
        return self.call('display_current_heating_program', kwargs=kwargs)

    def feed_parameters(self, **kwargs):
        return self.call('feed_parameters', kwargs=kwargs)

    def run_program(self, **kwargs):
        return self.call('run_program', kwargs=kwargs)

    def stop_program(self, **kwargs):
        return self.call('stop_program', kwargs=kwargs)

    def save_heating_info(self, **kwargs):
        return self.call('save_heating_info', kwargs=kwargs)

    def hold_program(self, **kwargs):
        return self.call('hold_program', kwargs=kwargs)

    def continue_program(self, **kwargs):
        return self.call('continue_program', kwargs=kwargs)

    def get_instrument_status(self, **kwargs):
        return self.call('get_instrument_status', kwargs=kwargs)

    def get_controller_data(self, **kwargs):
        return self.call('get_controller_data', kwargs=kwargs)

    def display_status(self, **kwargs):
        return self.call('display_status', kwargs=kwargs)

    def clear_parameters(self, **kwargs):
        return self.call('clear_parameters', kwargs=kwargs)

    def manual_heating(self, **kwargs):
        return self.call('manual_heating', kwargs=kwargs)

    def Rt_to_Rr(self, **kwargs):
        return self.call('Rt_to_Rr', kwargs=kwargs)

    def get_parameters(self, **kwargs):
        return self.call('get_parameters', kwargs=kwargs)

    def send_parameters(self, **kwargs):
        return self.call('send_parameters', kwargs=kwargs)

    def new_menu(self, **kwargs):
        return self.call('new_menu', kwargs=kwargs)

    def open_new_parameter_file(self, **kwargs):
        return self.call('open_new_parameter_file', kwargs=kwargs)

    def open_menu(self, **kwargs):
        return self.call('open_menu', kwargs=kwargs)

    def load_parameters_from_file(self, **kwargs):
        return self.call('load_parameters_from_file', kwargs=kwargs)

    def save_menu(self, **kwargs):
        return self.call('save_menu', kwargs=kwargs)

    def save_parameters_to_file(self, **kwargs):
        return self.call('save_parameters_to_file', kwargs=kwargs)

    def savefile(self, **kwargs):
        return self.call('savefile', kwargs=kwargs)

    def exit_menu(self, **kwargs):
        return self.call('exit_menu', kwargs=kwargs)

    def manual_heatingRate(self, **kwargs):
        return self.call('manual_heatingRate', kwargs=kwargs)

    def manual_heatingRate_dialogue(self, **kwargs):
        return self.call('manual_heatingRate_dialogue', kwargs=kwargs)

    def default_manualTemperature(self, **kwargs):
        return self.call('default_manualTemperature', kwargs=kwargs)

    def manual_temperature_dialogue(self, **kwargs):
        return self.call('manual_temperature_dialogue', kwargs=kwargs)

    def com1_menu(self, **kwargs):
        return self.call('com1_menu', kwargs=kwargs)

    def com2_menu(self, **kwargs):
        return self.call('com2_menu', kwargs=kwargs)

    def com3_menu(self, **kwargs):
        return self.call('com3_menu', kwargs=kwargs)

    def com4_menu(self, **kwargs):
        return self.call('com4_menu', kwargs=kwargs)

    def Enter_Manually_menu(self, **kwargs):
        return self.call('Enter_Manually_menu', kwargs=kwargs)

    def manual_entry_dialogue(self, **kwargs):
        return self.call('manual_entry_dialogue', kwargs=kwargs)

    def set_instrument_address(self, **kwargs):
        return self.call('set_instrument_address', kwargs=kwargs)

    def load_settings(self, **kwargs):
        return self.call('load_settings', kwargs=kwargs)

    def initialize_plot(self, **kwargs):
        return self.call('initialize_plot', kwargs=kwargs)

    def plot(self, **kwargs):
        return self.call('plot', kwargs=kwargs)

    def plot_realtime_data(self, **kwargs):
        return self.call('plot_realtime_data', kwargs=kwargs)

    def update_plot_data(self, **kwargs):
        return self.call('update_plot_data', kwargs=kwargs)

    def initialize_plot_data(self, **kwargs):
        return self.call('initialize_plot_data', kwargs=kwargs)

    def isfloat(self, **kwargs):
        return self.call('isfloat', kwargs=kwargs)

    def store_software_close_event(self, **kwargs):
        return self.call('store_software_close_event', kwargs=kwargs)

    def closeEvent(self, **kwargs):
        return self.call('closeEvent', kwargs=kwargs)

    def setupUi(self, **kwargs):
        return self.call('setupUi', kwargs=kwargs)

    def retranslateUi(self, **kwargs):
        return self.call('retranslateUi', kwargs=kwargs)

