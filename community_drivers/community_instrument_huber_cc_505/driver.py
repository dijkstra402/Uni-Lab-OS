from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentHuberCc505(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/defranchis__Particulars', 'source_file': 'DAQ/AXIOM/devices/hp4980.py', 'class_name': 'hp4980', 'import_roots': [], 'candidate_methods': ['print_idn', 'get_idn', 'reset', 'restart', 'clear_status', 'self_test', 'set_voltage', 'set_frequency', 'set_mode', 'set_range_auto', 'set_imp_range', 'set_read_format', 'set_comparator', 'set_aperture_time', 'set_dc_isolation_auto', 'set_alc', 'check_voltage', 'check_frequency', 'check_mode', 'check_current', 'check_range', 'set_correction_cable_length', 'check_correction_cable_length', 'execute_closed_correction', 'execute_short_correction', 'execute_load_correction', 'set_open_correction', 'set_short_correction', 'set_load_correction', 'check_open_correction', 'check_short_correction', 'check_load_correction', 'set_load_correction_type', 'check_load_correction_type', 'set_trigger_continous', 'set_trigger_immediate', 'set_trigger_source', 'send_trigger', 'execute_measurement'], 'action_targets': {}, 'metadata': {'repo': 'defranchis/Particulars', 'repo_url': 'https://github.com/defranchis/Particulars', 'brand': 'Huber', 'model': 'CC-505', 'device_type_cn': '冷热水机', 'device_type_en': 'Chiller / Heater Unit', 'source_framework': '专用驱动', 'tag_id': '4369', 'tag_name': '冷热水机', 'tag_name_en': 'Chiller / Heater Unit', 'candidate_score': 342, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def print_idn(self, **kwargs):
        return self.call('print_idn', kwargs=kwargs)

    def get_idn(self, **kwargs):
        return self.call('get_idn', kwargs=kwargs)

    def reset(self, **kwargs):
        return self.call('reset', kwargs=kwargs)

    def restart(self, **kwargs):
        return self.call('restart', kwargs=kwargs)

    def clear_status(self, **kwargs):
        return self.call('clear_status', kwargs=kwargs)

    def self_test(self, **kwargs):
        return self.call('self_test', kwargs=kwargs)

    def set_voltage(self, **kwargs):
        return self.call('set_voltage', kwargs=kwargs)

    def set_frequency(self, **kwargs):
        return self.call('set_frequency', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def set_range_auto(self, **kwargs):
        return self.call('set_range_auto', kwargs=kwargs)

    def set_imp_range(self, **kwargs):
        return self.call('set_imp_range', kwargs=kwargs)

    def set_read_format(self, **kwargs):
        return self.call('set_read_format', kwargs=kwargs)

    def set_comparator(self, **kwargs):
        return self.call('set_comparator', kwargs=kwargs)

    def set_aperture_time(self, **kwargs):
        return self.call('set_aperture_time', kwargs=kwargs)

    def set_dc_isolation_auto(self, **kwargs):
        return self.call('set_dc_isolation_auto', kwargs=kwargs)

    def set_alc(self, **kwargs):
        return self.call('set_alc', kwargs=kwargs)

    def check_voltage(self, **kwargs):
        return self.call('check_voltage', kwargs=kwargs)

    def check_frequency(self, **kwargs):
        return self.call('check_frequency', kwargs=kwargs)

    def check_mode(self, **kwargs):
        return self.call('check_mode', kwargs=kwargs)

    def check_current(self, **kwargs):
        return self.call('check_current', kwargs=kwargs)

    def check_range(self, **kwargs):
        return self.call('check_range', kwargs=kwargs)

    def set_correction_cable_length(self, **kwargs):
        return self.call('set_correction_cable_length', kwargs=kwargs)

    def check_correction_cable_length(self, **kwargs):
        return self.call('check_correction_cable_length', kwargs=kwargs)

    def execute_closed_correction(self, **kwargs):
        return self.call('execute_closed_correction', kwargs=kwargs)

    def execute_short_correction(self, **kwargs):
        return self.call('execute_short_correction', kwargs=kwargs)

    def execute_load_correction(self, **kwargs):
        return self.call('execute_load_correction', kwargs=kwargs)

    def set_open_correction(self, **kwargs):
        return self.call('set_open_correction', kwargs=kwargs)

    def set_short_correction(self, **kwargs):
        return self.call('set_short_correction', kwargs=kwargs)

    def set_load_correction(self, **kwargs):
        return self.call('set_load_correction', kwargs=kwargs)

    def check_open_correction(self, **kwargs):
        return self.call('check_open_correction', kwargs=kwargs)

    def check_short_correction(self, **kwargs):
        return self.call('check_short_correction', kwargs=kwargs)

    def check_load_correction(self, **kwargs):
        return self.call('check_load_correction', kwargs=kwargs)

    def set_load_correction_type(self, **kwargs):
        return self.call('set_load_correction_type', kwargs=kwargs)

    def check_load_correction_type(self, **kwargs):
        return self.call('check_load_correction_type', kwargs=kwargs)

    def set_trigger_continous(self, **kwargs):
        return self.call('set_trigger_continous', kwargs=kwargs)

    def set_trigger_immediate(self, **kwargs):
        return self.call('set_trigger_immediate', kwargs=kwargs)

    def set_trigger_source(self, **kwargs):
        return self.call('set_trigger_source', kwargs=kwargs)

    def send_trigger(self, **kwargs):
        return self.call('send_trigger', kwargs=kwargs)

    def execute_measurement(self, **kwargs):
        return self.call('execute_measurement', kwargs=kwargs)

