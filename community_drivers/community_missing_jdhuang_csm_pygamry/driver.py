from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityMissingJdhuangCsmPygamry(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/jdhuang-csm__pygamry', 'source_file': 'pygamry/dtaq/readz.py', 'class_name': 'DtaqReadZ', 'import_roots': [], 'candidate_methods': ['__init__', 'set_mode', 'get_mode', 'set_ac_ierange', 'get_ac_ierange', 'cook', 'set_ie_range', '_IGamryReadZEvents_OnDataAvailable', '_IGamryReadZEvents_OnDataDone', 'initialize_pstat', 'set_cycle_lim', 'measure_point', 'run', 'initialize_figure', 'get_current_zdata', 'zdata_columns', 'z_dataframe', 'get_dataframe_to_write', 'kst_column_index', 'get_kst_dataframe', 'write_to_file'], 'metadata': {'repo': 'jdhuang-csm/pygamry', 'repo_url': 'https://github.com/jdhuang-csm/pygamry', 'review_status': 'pending_review', 'review_notes': ['尚未完成人工仪器级复核。']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def init(self, **kwargs):
        return self.call('__init__', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def get_mode(self, **kwargs):
        return self.call('get_mode', kwargs=kwargs)

    def set_ac_ierange(self, **kwargs):
        return self.call('set_ac_ierange', kwargs=kwargs)

    def get_ac_ierange(self, **kwargs):
        return self.call('get_ac_ierange', kwargs=kwargs)

    def cook(self, **kwargs):
        return self.call('cook', kwargs=kwargs)

    def set_ie_range(self, **kwargs):
        return self.call('set_ie_range', kwargs=kwargs)

    def IGamryReadZEvents_OnDataAvailable(self, **kwargs):
        return self.call('_IGamryReadZEvents_OnDataAvailable', kwargs=kwargs)

    def IGamryReadZEvents_OnDataDone(self, **kwargs):
        return self.call('_IGamryReadZEvents_OnDataDone', kwargs=kwargs)

    def initialize_pstat(self, **kwargs):
        return self.call('initialize_pstat', kwargs=kwargs)

    def set_cycle_lim(self, **kwargs):
        return self.call('set_cycle_lim', kwargs=kwargs)

    def measure_point(self, **kwargs):
        return self.call('measure_point', kwargs=kwargs)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

    def initialize_figure(self, **kwargs):
        return self.call('initialize_figure', kwargs=kwargs)

    def get_current_zdata(self, **kwargs):
        return self.call('get_current_zdata', kwargs=kwargs)

    def zdata_columns(self, **kwargs):
        return self.call('zdata_columns', kwargs=kwargs)

    def z_dataframe(self, **kwargs):
        return self.call('z_dataframe', kwargs=kwargs)

    def get_dataframe_to_write(self, **kwargs):
        return self.call('get_dataframe_to_write', kwargs=kwargs)

    def kst_column_index(self, **kwargs):
        return self.call('kst_column_index', kwargs=kwargs)

    def get_kst_dataframe(self, **kwargs):
        return self.call('get_kst_dataframe', kwargs=kwargs)

    def write_to_file(self, **kwargs):
        return self.call('write_to_file', kwargs=kwargs)

