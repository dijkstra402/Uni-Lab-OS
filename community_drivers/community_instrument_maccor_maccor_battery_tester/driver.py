from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentMaccorMaccorBatteryTester(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/OpenBattTools__maccor-utility', 'source_file': 'src/maccor_utility/read.py', 'class_name': '', 'import_roots': ['src'], 'candidate_methods': ['read_maccor_data_file', 'rename_columns', 'datetime_fromdelphi', 'get_bool_array_from_bit_field', 'get_top_lvl_procedure', 'get_procedure_and_subroutine', 'import_maccor_cycling_data', 'import_maccor_cycling_stats', 'process_exists'], 'action_targets': {'read_maccor_data_file': 'read_maccor_data_file', 'rename_columns': 'rename_columns', 'datetime_fromdelphi': 'datetime_fromdelphi', 'get_bool_array_from_bit_field': 'get_bool_array_from_bit_field', 'get_top_lvl_procedure': 'get_top_lvl_procedure', 'get_procedure_and_subroutine': 'get_procedure_and_subroutine', 'import_maccor_cycling_data': 'import_maccor_cycling_data', 'import_maccor_cycling_stats': 'import_maccor_cycling_stats', 'process_exists': 'process_exists'}, 'metadata': {'repo': 'OpenBattTools/maccor-utility', 'repo_url': 'https://github.com/OpenBattTools/maccor-utility', 'brand': 'Maccor', 'model': 'Maccor Battery Tester', 'device_type_cn': '电池测试柜', 'device_type_en': 'Battery Test Cabinet', 'source_framework': '专用驱动', 'tag_id': '4427', 'tag_name': '电池测试柜', 'tag_name_en': 'Battery Test Cabinet', 'candidate_score': 79, 'parse_status': 'module_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'read_maccor_data_file': 'read_maccor_data_file', 'rename_columns': 'rename_columns', 'datetime_fromdelphi': 'datetime_fromdelphi', 'get_bool_array_from_bit_field': 'get_bool_array_from_bit_field', 'get_top_lvl_procedure': 'get_top_lvl_procedure', 'get_procedure_and_subroutine': 'get_procedure_and_subroutine', 'import_maccor_cycling_data': 'import_maccor_cycling_data', 'import_maccor_cycling_stats': 'import_maccor_cycling_stats', 'process_exists': 'process_exists'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def read_maccor_data_file(self, **kwargs):
        return self.call('read_maccor_data_file', kwargs=kwargs)

    def rename_columns(self, **kwargs):
        return self.call('rename_columns', kwargs=kwargs)

    def datetime_fromdelphi(self, **kwargs):
        return self.call('datetime_fromdelphi', kwargs=kwargs)

    def get_bool_array_from_bit_field(self, **kwargs):
        return self.call('get_bool_array_from_bit_field', kwargs=kwargs)

    def get_top_lvl_procedure(self, **kwargs):
        return self.call('get_top_lvl_procedure', kwargs=kwargs)

    def get_procedure_and_subroutine(self, **kwargs):
        return self.call('get_procedure_and_subroutine', kwargs=kwargs)

    def import_maccor_cycling_data(self, **kwargs):
        return self.call('import_maccor_cycling_data', kwargs=kwargs)

    def import_maccor_cycling_stats(self, **kwargs):
        return self.call('import_maccor_cycling_stats', kwargs=kwargs)

    def process_exists(self, **kwargs):
        return self.call('process_exists', kwargs=kwargs)

