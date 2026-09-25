from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentGamryGamryPotentiostat(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/jdhuang-csm__pygamry', 'source_file': 'pygamry/dtaq/eventsink.py', 'class_name': 'GamryDtaqEventSink', 'import_roots': [], 'candidate_methods': ['pstat_ctrlmode', 'cook', 'PumpEvents', 'close_handle', 'run_main', 'open_connection', 'close_connection', 'terminate', 'initialize_figure', 'run_plot_animation', 'plot_data', 'initialize_pstat', 'cook_columns', 'data_array', 'num_points', 'dataframe', 'get_dataframe_to_write', 'get_kst_dataframe', 'format_start_date_time', 'get_date_time_text', 'get_data_header', 'get_dtaq_header', 'get_notes_text', 'generate_header_text', 'generate_kst_header', 'generate_data_string', 'write_to_files', 'write_to_file', 'column_index_to_write', 'kst_columns', 'kst_column_index', 'get_file_offset_info', 'get_write_mode', 'set_write_mode'], 'action_targets': {}, 'metadata': {'repo': 'jdhuang-csm/pygamry', 'repo_url': 'https://github.com/jdhuang-csm/pygamry', 'brand': 'Gamry', 'model': 'Gamry Potentiostat', 'device_type_cn': '电化学工作站', 'device_type_en': 'Electrochemical Workstation', 'source_framework': 'pygamry', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 330, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def pstat_ctrlmode(self, **kwargs):
        return self.call('pstat_ctrlmode', kwargs=kwargs)

    def cook(self, **kwargs):
        return self.call('cook', kwargs=kwargs)

    def PumpEvents(self, **kwargs):
        return self.call('PumpEvents', kwargs=kwargs)

    def close_handle(self, **kwargs):
        return self.call('close_handle', kwargs=kwargs)

    def run_main(self, **kwargs):
        return self.call('run_main', kwargs=kwargs)

    def open_connection(self, **kwargs):
        return self.call('open_connection', kwargs=kwargs)

    def close_connection(self, **kwargs):
        return self.call('close_connection', kwargs=kwargs)

    def terminate(self, **kwargs):
        return self.call('terminate', kwargs=kwargs)

    def initialize_figure(self, **kwargs):
        return self.call('initialize_figure', kwargs=kwargs)

    def run_plot_animation(self, **kwargs):
        return self.call('run_plot_animation', kwargs=kwargs)

    def plot_data(self, **kwargs):
        return self.call('plot_data', kwargs=kwargs)

    def initialize_pstat(self, **kwargs):
        return self.call('initialize_pstat', kwargs=kwargs)

    def cook_columns(self, **kwargs):
        return self.call('cook_columns', kwargs=kwargs)

    def data_array(self, **kwargs):
        return self.call('data_array', kwargs=kwargs)

    def num_points(self, **kwargs):
        return self.call('num_points', kwargs=kwargs)

    def dataframe(self, **kwargs):
        return self.call('dataframe', kwargs=kwargs)

    def get_dataframe_to_write(self, **kwargs):
        return self.call('get_dataframe_to_write', kwargs=kwargs)

    def get_kst_dataframe(self, **kwargs):
        return self.call('get_kst_dataframe', kwargs=kwargs)

    def format_start_date_time(self, **kwargs):
        return self.call('format_start_date_time', kwargs=kwargs)

    def get_date_time_text(self, **kwargs):
        return self.call('get_date_time_text', kwargs=kwargs)

    def get_data_header(self, **kwargs):
        return self.call('get_data_header', kwargs=kwargs)

    def get_dtaq_header(self, **kwargs):
        return self.call('get_dtaq_header', kwargs=kwargs)

    def get_notes_text(self, **kwargs):
        return self.call('get_notes_text', kwargs=kwargs)

    def generate_header_text(self, **kwargs):
        return self.call('generate_header_text', kwargs=kwargs)

    def generate_kst_header(self, **kwargs):
        return self.call('generate_kst_header', kwargs=kwargs)

    def generate_data_string(self, **kwargs):
        return self.call('generate_data_string', kwargs=kwargs)

    def write_to_files(self, **kwargs):
        return self.call('write_to_files', kwargs=kwargs)

    def write_to_file(self, **kwargs):
        return self.call('write_to_file', kwargs=kwargs)

    def column_index_to_write(self, **kwargs):
        return self.call('column_index_to_write', kwargs=kwargs)

    def kst_columns(self, **kwargs):
        return self.call('kst_columns', kwargs=kwargs)

    def kst_column_index(self, **kwargs):
        return self.call('kst_column_index', kwargs=kwargs)

    def get_file_offset_info(self, **kwargs):
        return self.call('get_file_offset_info', kwargs=kwargs)

    def get_write_mode(self, **kwargs):
        return self.call('get_write_mode', kwargs=kwargs)

    def set_write_mode(self, **kwargs):
        return self.call('set_write_mode', kwargs=kwargs)

