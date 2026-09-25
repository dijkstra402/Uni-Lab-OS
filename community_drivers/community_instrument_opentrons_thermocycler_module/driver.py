from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentOpentronsThermocyclerModule(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/mtoutai__ot_thermocycler_standalone', 'source_file': 'pcr_gui.py', 'class_name': '', 'import_roots': [], 'candidate_methods': ['connect', 'open_lid', 'close_lid', 'deactivate_all', 'prep_job_func', 'add_waiting', 'debug_print_job', 'prep_job', 'mean', 'is_block_stabilized', 'is_lid_stabilized', 'delay_schedule', 'load_job', 'save_job', 'run', 'update_graph', 'save_log', 'interrupt_callback'], 'action_targets': {'connect': 'connect', 'open_lid': 'open_lid', 'close_lid': 'close_lid', 'deactivate_all': 'deactivate_all', 'prep_job_func': 'prep_job_func', 'add_waiting': 'add_waiting', 'debug_print_job': 'debug_print_job', 'prep_job': 'prep_job', 'mean': 'mean', 'is_block_stabilized': 'is_block_stabilized', 'is_lid_stabilized': 'is_lid_stabilized', 'delay_schedule': 'delay_schedule', 'load_job': 'load_job', 'save_job': 'save_job', 'run': 'run', 'update_graph': 'update_graph', 'save_log': 'save_log', 'interrupt_callback': 'interrupt_callback'}, 'metadata': {'repo': 'mtoutai/ot_thermocycler_standalone', 'repo_url': 'https://github.com/mtoutai/ot_thermocycler_standalone', 'brand': 'Opentrons', 'model': 'Thermocycler Module (独立)', 'device_type_cn': '普通PCR仪', 'device_type_en': 'Thermal Cycler', 'source_framework': '专用驱动', 'tag_id': '4399', 'tag_name': '普通PCR仪', 'tag_name_en': 'Thermal Cycler', 'candidate_score': 146, 'parse_status': 'module_selected', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {'connect': 'connect', 'open_lid': 'open_lid', 'close_lid': 'close_lid', 'deactivate_all': 'deactivate_all', 'prep_job_func': 'prep_job_func', 'add_waiting': 'add_waiting', 'debug_print_job': 'debug_print_job', 'prep_job': 'prep_job', 'mean': 'mean', 'is_block_stabilized': 'is_block_stabilized', 'is_lid_stabilized': 'is_lid_stabilized', 'delay_schedule': 'delay_schedule', 'load_job': 'load_job', 'save_job': 'save_job', 'run': 'run', 'update_graph': 'update_graph', 'save_log': 'save_log', 'interrupt_callback': 'interrupt_callback'}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def open_lid(self, **kwargs):
        return self.call('open_lid', kwargs=kwargs)

    def close_lid(self, **kwargs):
        return self.call('close_lid', kwargs=kwargs)

    def deactivate_all(self, **kwargs):
        return self.call('deactivate_all', kwargs=kwargs)

    def prep_job_func(self, **kwargs):
        return self.call('prep_job_func', kwargs=kwargs)

    def add_waiting(self, **kwargs):
        return self.call('add_waiting', kwargs=kwargs)

    def debug_print_job(self, **kwargs):
        return self.call('debug_print_job', kwargs=kwargs)

    def prep_job(self, **kwargs):
        return self.call('prep_job', kwargs=kwargs)

    def mean(self, **kwargs):
        return self.call('mean', kwargs=kwargs)

    def is_block_stabilized(self, **kwargs):
        return self.call('is_block_stabilized', kwargs=kwargs)

    def is_lid_stabilized(self, **kwargs):
        return self.call('is_lid_stabilized', kwargs=kwargs)

    def delay_schedule(self, **kwargs):
        return self.call('delay_schedule', kwargs=kwargs)

    def load_job(self, **kwargs):
        return self.call('load_job', kwargs=kwargs)

    def save_job(self, **kwargs):
        return self.call('save_job', kwargs=kwargs)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

    def update_graph(self, **kwargs):
        return self.call('update_graph', kwargs=kwargs)

    def save_log(self, **kwargs):
        return self.call('save_log', kwargs=kwargs)

    def interrupt_callback(self, **kwargs):
        return self.call('interrupt_callback', kwargs=kwargs)

