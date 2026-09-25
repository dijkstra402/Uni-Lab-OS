from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentGamryPc6(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/helgestein__helao-pub', 'source_file': 'driver/galil_driver.py', 'class_name': 'galil', 'import_roots': [], 'candidate_methods': ['motor_move', 'motor_move_live', 'motor_disconnect', 'query_all_axis_positions', 'query_axis', 'query_moving', 'motor_off', 'motor_on', 'motor_stop', 'read_analog_in', 'read_digital_in', 'read_digital_out', 'set_analog_out', 'digital_out_on', 'digital_out_off', 'infinite_digital_cycles', 'break_infinite_digital_cycles', 'shutdown_event'], 'action_targets': {}, 'metadata': {'repo': 'helgestein/helao-pub', 'repo_url': 'https://github.com/helgestein/helao-pub', 'brand': 'Gamry', 'model': 'PC6', 'device_type_cn': '电化学反应器', 'device_type_en': 'Electrochemical Reactor', 'source_framework': 'helao', 'tag_id': '4424', 'tag_name': '电化学反应器', 'tag_name_en': 'Electrochemical Reactor', 'candidate_score': 174, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def motor_move(self, **kwargs):
        return self.call('motor_move', kwargs=kwargs)

    def motor_move_live(self, **kwargs):
        return self.call('motor_move_live', kwargs=kwargs)

    def motor_disconnect(self, **kwargs):
        return self.call('motor_disconnect', kwargs=kwargs)

    def query_all_axis_positions(self, **kwargs):
        return self.call('query_all_axis_positions', kwargs=kwargs)

    def query_axis(self, **kwargs):
        return self.call('query_axis', kwargs=kwargs)

    def query_moving(self, **kwargs):
        return self.call('query_moving', kwargs=kwargs)

    def motor_off(self, **kwargs):
        return self.call('motor_off', kwargs=kwargs)

    def motor_on(self, **kwargs):
        return self.call('motor_on', kwargs=kwargs)

    def motor_stop(self, **kwargs):
        return self.call('motor_stop', kwargs=kwargs)

    def read_analog_in(self, **kwargs):
        return self.call('read_analog_in', kwargs=kwargs)

    def read_digital_in(self, **kwargs):
        return self.call('read_digital_in', kwargs=kwargs)

    def read_digital_out(self, **kwargs):
        return self.call('read_digital_out', kwargs=kwargs)

    def set_analog_out(self, **kwargs):
        return self.call('set_analog_out', kwargs=kwargs)

    def digital_out_on(self, **kwargs):
        return self.call('digital_out_on', kwargs=kwargs)

    def digital_out_off(self, **kwargs):
        return self.call('digital_out_off', kwargs=kwargs)

    def infinite_digital_cycles(self, **kwargs):
        return self.call('infinite_digital_cycles', kwargs=kwargs)

    def break_infinite_digital_cycles(self, **kwargs):
        return self.call('break_infinite_digital_cycles', kwargs=kwargs)

    def shutdown_event(self, **kwargs):
        return self.call('shutdown_event', kwargs=kwargs)

