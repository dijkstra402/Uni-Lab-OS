from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentNovocontrolAlphaAnalyzer(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/JMoVS__JUMP', 'source_file': 'DataStorage.py', 'class_name': 'Database', 'import_roots': [], 'candidate_methods': ['change_to_passed_db', 'start_fresh', 'measurement_finished', 'pickle_database', 'new_pickle_path', 'start_post_processing', 'tasks', 'add_point', 'make_storage', 'calculate_all_values', 'merge_same_level_datapoints', 'merge_diff_level_datapoints', 'insert_sub_datapoints_into_parent_datapoint', 'get_transposed_parent_child_datapoints'], 'action_targets': {}, 'metadata': {'repo': 'JMoVS/JUMP', 'repo_url': 'https://github.com/JMoVS/JUMP', 'brand': 'Novocontrol', 'model': 'Alpha Analyzer', 'device_type_cn': '介电/阻抗分析仪', 'device_type_en': 'Dielectric/Impedance Analyzer', 'source_framework': '电化学/热分析/天平', 'tag_id': '4365', 'tag_name': '介电常数测定仪', 'tag_name_en': 'Dielectric Constant Meter', 'candidate_score': 117, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def change_to_passed_db(self, **kwargs):
        return self.call('change_to_passed_db', kwargs=kwargs)

    def start_fresh(self, **kwargs):
        return self.call('start_fresh', kwargs=kwargs)

    def measurement_finished(self, **kwargs):
        return self.call('measurement_finished', kwargs=kwargs)

    def pickle_database(self, **kwargs):
        return self.call('pickle_database', kwargs=kwargs)

    def new_pickle_path(self, **kwargs):
        return self.call('new_pickle_path', kwargs=kwargs)

    def start_post_processing(self, **kwargs):
        return self.call('start_post_processing', kwargs=kwargs)

    def tasks(self, **kwargs):
        return self.call('tasks', kwargs=kwargs)

    def add_point(self, **kwargs):
        return self.call('add_point', kwargs=kwargs)

    def make_storage(self, **kwargs):
        return self.call('make_storage', kwargs=kwargs)

    def calculate_all_values(self, **kwargs):
        return self.call('calculate_all_values', kwargs=kwargs)

    def merge_same_level_datapoints(self, **kwargs):
        return self.call('merge_same_level_datapoints', kwargs=kwargs)

    def merge_diff_level_datapoints(self, **kwargs):
        return self.call('merge_diff_level_datapoints', kwargs=kwargs)

    def insert_sub_datapoints_into_parent_datapoint(self, **kwargs):
        return self.call('insert_sub_datapoints_into_parent_datapoint', kwargs=kwargs)

    def get_transposed_parent_child_datapoints(self, **kwargs):
        return self.call('get_transposed_parent_child_datapoints', kwargs=kwargs)

