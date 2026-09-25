from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentLiconicStorexStx88(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/AD-SDL__BIO_workcell', 'source_file': 'applications/multi_growth_app/multi_growth_curve_app.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['sample_method_implementing_ai', 'process_experimental_results', 'read_globus_data', 'delete_experiment_excel_file', 'determine_payload_from_excel', 'setup_experiment_run_dataframes_from_stocks', 'return_stock_dictionary', 'run_experiment', 'dispose', 'setup', 'T0_Reading', 'T12_Reading', 'run_WEI', 'assign_barcode', 'return_barcode', 'main'], 'action_targets': {'sample_method_implementing_ai': 'sample_method_implementing_ai', 'process_experimental_results': 'process_experimental_results', 'read_globus_data': 'read_globus_data', 'delete_experiment_excel_file': 'delete_experiment_excel_file', 'determine_payload_from_excel': 'determine_payload_from_excel', 'setup_experiment_run_dataframes_from_stocks': 'setup_experiment_run_dataframes_from_stocks', 'return_stock_dictionary': 'return_stock_dictionary', 'run_experiment': 'run_experiment', 'dispose': 'dispose', 'setup': 'setup', 'T0_Reading': 'T0_Reading', 'T12_Reading': 'T12_Reading', 'run_WEI': 'run_WEI', 'assign_barcode': 'assign_barcode', 'return_barcode': 'return_barcode', 'main': 'main'}, 'metadata': {'repo': 'AD-SDL/BIO_workcell', 'repo_url': 'https://github.com/AD-SDL/BIO_workcell', 'brand': 'Liconic', 'model': 'StoreX STX88', 'device_type_cn': '自动化培养箱', 'device_type_en': 'Automated Incubator', 'source_framework': '生命科学', 'tag_id': '4387', 'tag_name': '微生物培养箱', 'tag_name_en': 'Microbial Incubator', 'candidate_score': 112, 'parse_status': 'module_reselected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'sample_method_implementing_ai': 'sample_method_implementing_ai', 'process_experimental_results': 'process_experimental_results', 'read_globus_data': 'read_globus_data', 'delete_experiment_excel_file': 'delete_experiment_excel_file', 'determine_payload_from_excel': 'determine_payload_from_excel', 'setup_experiment_run_dataframes_from_stocks': 'setup_experiment_run_dataframes_from_stocks', 'return_stock_dictionary': 'return_stock_dictionary', 'run_experiment': 'run_experiment', 'dispose': 'dispose', 'setup': 'setup', 'T0_Reading': 'T0_Reading', 'T12_Reading': 'T12_Reading', 'run_WEI': 'run_WEI', 'assign_barcode': 'assign_barcode', 'return_barcode': 'return_barcode', 'main': 'main'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def sample_method_implementing_ai(self, **kwargs):
        return self.call('sample_method_implementing_ai', kwargs=kwargs)

    def process_experimental_results(self, **kwargs):
        return self.call('process_experimental_results', kwargs=kwargs)

    def read_globus_data(self, **kwargs):
        return self.call('read_globus_data', kwargs=kwargs)

    def delete_experiment_excel_file(self, **kwargs):
        return self.call('delete_experiment_excel_file', kwargs=kwargs)

    def determine_payload_from_excel(self, **kwargs):
        return self.call('determine_payload_from_excel', kwargs=kwargs)

    def setup_experiment_run_dataframes_from_stocks(self, **kwargs):
        return self.call('setup_experiment_run_dataframes_from_stocks', kwargs=kwargs)

    def return_stock_dictionary(self, **kwargs):
        return self.call('return_stock_dictionary', kwargs=kwargs)

    def run_experiment(self, **kwargs):
        return self.call('run_experiment', kwargs=kwargs)

    def dispose(self, **kwargs):
        return self.call('dispose', kwargs=kwargs)

    def setup(self, **kwargs):
        return self.call('setup', kwargs=kwargs)

    def T0_Reading(self, **kwargs):
        return self.call('T0_Reading', kwargs=kwargs)

    def T12_Reading(self, **kwargs):
        return self.call('T12_Reading', kwargs=kwargs)

    def run_WEI(self, **kwargs):
        return self.call('run_WEI', kwargs=kwargs)

    def assign_barcode(self, **kwargs):
        return self.call('assign_barcode', kwargs=kwargs)

    def return_barcode(self, **kwargs):
        return self.call('return_barcode', kwargs=kwargs)

    def main(self, **kwargs):
        return self.call('main', kwargs=kwargs)

