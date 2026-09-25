from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentNewareBtsBeep(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/TRI-AMDD__beep', 'source_file': 'tests/structure/test_base.py', 'class_name': 'TestBEEPDatapath', 'import_roots': [], 'candidate_methods': ['setUpClass', 'setUp', 'run_dtypes_check', 'test_abc', 'test_unstructure', 'test_serialization', 'test_reloading_new', 'test_serialization_legacy', 'test_interpolate_step', 'test_interpolate_cycles', 'test_summarize_cycles', 'test_interpolate_diagnostic_cycles', 'test_summarize_diagnostic', 'test_paused_intervals', 'test_get_diagnostic', 'test_structure', 'test_structure_w_cycle_exclusion', 'test_get_cycle_life', 'test_data_types_old_processed', 'test_capacities_to_cycles', 'test_cycles_to_capacities', 'test_semiunique_id'], 'action_targets': {}, 'metadata': {'repo': 'TRI-AMDD/beep', 'repo_url': 'https://github.com/TRI-AMDD/beep', 'brand': 'Neware', 'model': 'BTS (BEEP)', 'device_type_cn': '电池测试柜', 'device_type_en': 'Battery Cycler', 'source_framework': 'BEEP', 'tag_id': '4427', 'tag_name': '电池测试柜', 'tag_name_en': 'Battery Test Cabinet', 'candidate_score': 238, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def setUpClass(self, **kwargs):
        return self.call('setUpClass', kwargs=kwargs)

    def setUp(self, **kwargs):
        return self.call('setUp', kwargs=kwargs)

    def run_dtypes_check(self, **kwargs):
        return self.call('run_dtypes_check', kwargs=kwargs)

    def test_abc(self, **kwargs):
        return self.call('test_abc', kwargs=kwargs)

    def test_unstructure(self, **kwargs):
        return self.call('test_unstructure', kwargs=kwargs)

    def test_serialization(self, **kwargs):
        return self.call('test_serialization', kwargs=kwargs)

    def test_reloading_new(self, **kwargs):
        return self.call('test_reloading_new', kwargs=kwargs)

    def test_serialization_legacy(self, **kwargs):
        return self.call('test_serialization_legacy', kwargs=kwargs)

    def test_interpolate_step(self, **kwargs):
        return self.call('test_interpolate_step', kwargs=kwargs)

    def test_interpolate_cycles(self, **kwargs):
        return self.call('test_interpolate_cycles', kwargs=kwargs)

    def test_summarize_cycles(self, **kwargs):
        return self.call('test_summarize_cycles', kwargs=kwargs)

    def test_interpolate_diagnostic_cycles(self, **kwargs):
        return self.call('test_interpolate_diagnostic_cycles', kwargs=kwargs)

    def test_summarize_diagnostic(self, **kwargs):
        return self.call('test_summarize_diagnostic', kwargs=kwargs)

    def test_paused_intervals(self, **kwargs):
        return self.call('test_paused_intervals', kwargs=kwargs)

    def test_get_diagnostic(self, **kwargs):
        return self.call('test_get_diagnostic', kwargs=kwargs)

    def test_structure(self, **kwargs):
        return self.call('test_structure', kwargs=kwargs)

    def test_structure_w_cycle_exclusion(self, **kwargs):
        return self.call('test_structure_w_cycle_exclusion', kwargs=kwargs)

    def test_get_cycle_life(self, **kwargs):
        return self.call('test_get_cycle_life', kwargs=kwargs)

    def test_data_types_old_processed(self, **kwargs):
        return self.call('test_data_types_old_processed', kwargs=kwargs)

    def test_capacities_to_cycles(self, **kwargs):
        return self.call('test_capacities_to_cycles', kwargs=kwargs)

    def test_cycles_to_capacities(self, **kwargs):
        return self.call('test_cycles_to_capacities', kwargs=kwargs)

    def test_semiunique_id(self, **kwargs):
        return self.call('test_semiunique_id', kwargs=kwargs)

