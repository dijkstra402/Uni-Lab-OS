from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentThermoProflex(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/thermocycling/thermo_fisher/proflex.py', 'class_name': 'ProflexBackend', 'import_roots': [], 'candidate_methods': ['abort_run', 'block_ramp_single_temp', 'buzzer_off', 'buzzer_on', 'check_run_exists', 'close_lid', 'continue_run', 'create_run', 'deactivate_block', 'deactivate_lid', 'get_block_current_temperature', 'get_block_id', 'get_block_presence', 'get_block_status', 'get_block_target_temperature', 'get_current_cycle_index', 'get_current_step_index', 'get_elapsed_run_time', 'get_elapsed_run_time_from_log', 'get_error', 'get_estimated_run_time', 'get_hold_time', 'get_lid_current_temperature', 'get_lid_open', 'get_lid_status', 'get_lid_target_temperature', 'get_log_by_runname', 'get_nickname', 'get_remaining_run_time', 'get_run_info', 'get_run_name', 'get_sample_temps', 'get_total_cycle_count', 'get_total_step_count', 'is_block_running', 'open_lid', 'power_off', 'power_on', 'run_protocol', 'send_morse_code', 'set_block_idle_temp', 'set_block_temperature', 'set_cover_idle_temp', 'set_lid_temperature', 'set_nickname', 'setup', 'stop'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Thermo Fisher', 'model': 'ProFlex', 'device_type_cn': '热循环仪', 'device_type_en': 'Thermocycler', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/thermocycling/thermo_fisher/proflex.py', 'class_name': 'ProflexBackend', 'candidate_methods': ['abort_run', 'block_ramp_single_temp', 'buzzer_off', 'buzzer_on', 'check_run_exists', 'close_lid', 'continue_run', 'create_run', 'deactivate_block', 'deactivate_lid', 'get_block_current_temperature', 'get_block_id', 'get_block_presence', 'get_block_status', 'get_block_target_temperature', 'get_current_cycle_index', 'get_current_step_index', 'get_elapsed_run_time', 'get_elapsed_run_time_from_log', 'get_error', 'get_estimated_run_time', 'get_hold_time', 'get_lid_current_temperature', 'get_lid_open', 'get_lid_status', 'get_lid_target_temperature', 'get_log_by_runname', 'get_nickname', 'get_remaining_run_time', 'get_run_info', 'get_run_name', 'get_sample_temps', 'get_total_cycle_count', 'get_total_step_count', 'is_block_running', 'open_lid', 'power_off', 'power_on', 'run_protocol', 'send_morse_code', 'set_block_idle_temp', 'set_block_temperature', 'set_cover_idle_temp', 'set_lid_temperature', 'set_nickname', 'setup', 'stop']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def abort_run(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('abort_run', kwargs={k: v for k, v in _kw.items() if v is not None})

    def block_ramp_single_temp(self, target_temp=None, block_id=None, rate=None, **kwargs):
        _kw = {'target_temp': target_temp, 'block_id': block_id, 'rate': rate}
        _kw.update(kwargs)
        return self.call('block_ramp_single_temp', kwargs={k: v for k, v in _kw.items() if v is not None})

    def buzzer_off(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('buzzer_off', kwargs={k: v for k, v in _kw.items() if v is not None})

    def buzzer_on(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('buzzer_on', kwargs={k: v for k, v in _kw.items() if v is not None})

    def check_run_exists(self, run_name=None, **kwargs):
        _kw = {'run_name': run_name}
        _kw.update(kwargs)
        return self.call('check_run_exists', kwargs={k: v for k, v in _kw.items() if v is not None})

    def close_lid(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('close_lid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def continue_run(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('continue_run', kwargs={k: v for k, v in _kw.items() if v is not None})

    def create_run(self, run_name=None, **kwargs):
        _kw = {'run_name': run_name}
        _kw.update(kwargs)
        return self.call('create_run', kwargs={k: v for k, v in _kw.items() if v is not None})

    def deactivate_block(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('deactivate_block', kwargs={k: v for k, v in _kw.items() if v is not None})

    def deactivate_lid(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('deactivate_lid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_block_current_temperature(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('get_block_current_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_block_id(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_block_id', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_block_presence(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_block_presence', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_block_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_block_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_block_target_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_block_target_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_current_cycle_index(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('get_current_cycle_index', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_current_step_index(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('get_current_step_index', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_elapsed_run_time(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('get_elapsed_run_time', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_elapsed_run_time_from_log(self, run_name=None, **kwargs):
        _kw = {'run_name': run_name}
        _kw.update(kwargs)
        return self.call('get_elapsed_run_time_from_log', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_error(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('get_error', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_estimated_run_time(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('get_estimated_run_time', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_hold_time(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_hold_time', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_current_temperature(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('get_lid_current_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_open(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_lid_open', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_status(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_lid_status', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_lid_target_temperature(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_lid_target_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_log_by_runname(self, run_name=None, **kwargs):
        _kw = {'run_name': run_name}
        _kw.update(kwargs)
        return self.call('get_log_by_runname', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_nickname(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_nickname', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_remaining_run_time(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('get_remaining_run_time', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_run_info(self, protocol=None, block_id=None, **kwargs):
        _kw = {'protocol': protocol, 'block_id': block_id}
        _kw.update(kwargs)
        return self.call('get_run_info', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_run_name(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('get_run_name', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_sample_temps(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('get_sample_temps', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_total_cycle_count(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_total_cycle_count', kwargs={k: v for k, v in _kw.items() if v is not None})

    def get_total_step_count(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('get_total_step_count', kwargs={k: v for k, v in _kw.items() if v is not None})

    def is_block_running(self, block_id=None, **kwargs):
        _kw = {'block_id': block_id}
        _kw.update(kwargs)
        return self.call('is_block_running', kwargs={k: v for k, v in _kw.items() if v is not None})

    def open_lid(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('open_lid', kwargs={k: v for k, v in _kw.items() if v is not None})

    def power_off(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('power_off', kwargs={k: v for k, v in _kw.items() if v is not None})

    def power_on(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('power_on', kwargs={k: v for k, v in _kw.items() if v is not None})

    def run_protocol(self, protocol=None, block_max_volume=None, block_id=None, run_name=None, user=None, run_mode=None, cover_temp=None, cover_enabled=None, protocol_name=None, stage_name_prefixes=None, **kwargs):
        _kw = {'protocol': protocol, 'block_max_volume': block_max_volume, 'block_id': block_id, 'run_name': run_name, 'user': user, 'run_mode': run_mode, 'cover_temp': cover_temp, 'cover_enabled': cover_enabled, 'protocol_name': protocol_name, 'stage_name_prefixes': stage_name_prefixes}
        _kw.update(kwargs)
        return self.call('run_protocol', kwargs={k: v for k, v in _kw.items() if v is not None})

    def send_morse_code(self, morse_code=None, **kwargs):
        _kw = {'morse_code': morse_code}
        _kw.update(kwargs)
        return self.call('send_morse_code', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_block_idle_temp(self, temp=None, block_id=None, control_enabled=None, **kwargs):
        _kw = {'temp': temp, 'block_id': block_id, 'control_enabled': control_enabled}
        _kw.update(kwargs)
        return self.call('set_block_idle_temp', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_block_temperature(self, temperature=None, block_id=None, rate=None, **kwargs):
        _kw = {'temperature': temperature, 'block_id': block_id, 'rate': rate}
        _kw.update(kwargs)
        return self.call('set_block_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_cover_idle_temp(self, temp=None, block_id=None, control_enabled=None, **kwargs):
        _kw = {'temp': temp, 'block_id': block_id, 'control_enabled': control_enabled}
        _kw.update(kwargs)
        return self.call('set_cover_idle_temp', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_lid_temperature(self, temperature=None, block_id=None, **kwargs):
        _kw = {'temperature': temperature, 'block_id': block_id}
        _kw.update(kwargs)
        return self.call('set_lid_temperature', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_nickname(self, nickname=None, **kwargs):
        _kw = {'nickname': nickname}
        _kw.update(kwargs)
        return self.call('set_nickname', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, block_idle_temp=None, cover_idle_temp=None, blocks_to_setup=None, **kwargs):
        _kw = {'block_idle_temp': block_idle_temp, 'cover_idle_temp': cover_idle_temp, 'blocks_to_setup': blocks_to_setup}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

