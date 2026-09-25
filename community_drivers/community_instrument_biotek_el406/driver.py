from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentBiotekEl406(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/PyLabRobot__pylabrobot', 'source_file': 'pylabrobot/plate_washing/biotek/el406/backend.py', 'class_name': 'ExperimentalBioTekEL406Backend', 'import_roots': [], 'candidate_methods': ['abort', 'batch', 'cleanup_after_protocol', 'home_motors', 'manifold_aspirate', 'manifold_auto_clean', 'manifold_dispense', 'manifold_prime', 'manifold_wash', 'pause', 'peristaltic_dispense', 'peristaltic_prime', 'peristaltic_purge', 'request_instrument_settings', 'request_peristaltic_installed', 'request_sensor_enabled', 'request_serial_number', 'request_syringe_box_info', 'request_syringe_manifold', 'request_washer_manifold', 'reset', 'resume', 'run_self_check', 'set_washer_manifold', 'setup', 'shake', 'start_batch', 'stop', 'syringe_dispense', 'syringe_prime'], 'action_targets': {}, 'metadata': {'repo': 'PyLabRobot/pylabrobot', 'repo_url': 'https://github.com/PyLabRobot/pylabrobot', 'brand': 'Agilent (BioTek)', 'model': 'EL406', 'device_type_cn': '板清洗机', 'device_type_en': 'Plate Washer', 'source_framework': 'PyLabRobot', 'source_file': 'pylabrobot/plate_washing/biotek/el406/backend.py', 'class_name': 'ExperimentalBioTekEL406Backend', 'candidate_methods': ['abort', 'batch', 'cleanup_after_protocol', 'home_motors', 'manifold_aspirate', 'manifold_auto_clean', 'manifold_dispense', 'manifold_prime', 'manifold_wash', 'pause', 'peristaltic_dispense', 'peristaltic_prime', 'peristaltic_purge', 'request_instrument_settings', 'request_peristaltic_installed', 'request_sensor_enabled', 'request_serial_number', 'request_syringe_box_info', 'request_syringe_manifold', 'request_washer_manifold', 'reset', 'resume', 'run_self_check', 'set_washer_manifold', 'setup', 'shake', 'start_batch', 'stop', 'syringe_dispense', 'syringe_prime']}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def abort(self, step_type=None, **kwargs):
        _kw = {'step_type': step_type}
        _kw.update(kwargs)
        return self.call('abort', kwargs={k: v for k, v in _kw.items() if v is not None})

    def batch(self, plate=None, **kwargs):
        _kw = {'plate': plate}
        _kw.update(kwargs)
        return self.call('batch', kwargs={k: v for k, v in _kw.items() if v is not None})

    def cleanup_after_protocol(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('cleanup_after_protocol', kwargs={k: v for k, v in _kw.items() if v is not None})

    def home_motors(self, home_type=None, motor=None, **kwargs):
        _kw = {'home_type': home_type, 'motor': motor}
        _kw.update(kwargs)
        return self.call('home_motors', kwargs={k: v for k, v in _kw.items() if v is not None})

    def manifold_aspirate(self, plate=None, vacuum_filtration=None, travel_rate=None, delay=None, vacuum_time=None, offset_x=None, offset_y=None, offset_z=None, secondary_aspirate=None, secondary_x=None, secondary_y=None, secondary_z=None, **kwargs):
        _kw = {'plate': plate, 'vacuum_filtration': vacuum_filtration, 'travel_rate': travel_rate, 'delay': delay, 'vacuum_time': vacuum_time, 'offset_x': offset_x, 'offset_y': offset_y, 'offset_z': offset_z, 'secondary_aspirate': secondary_aspirate, 'secondary_x': secondary_x, 'secondary_y': secondary_y, 'secondary_z': secondary_z}
        _kw.update(kwargs)
        return self.call('manifold_aspirate', kwargs={k: v for k, v in _kw.items() if v is not None})

    def manifold_auto_clean(self, plate=None, buffer=None, duration=None, **kwargs):
        _kw = {'plate': plate, 'buffer': buffer, 'duration': duration}
        _kw.update(kwargs)
        return self.call('manifold_auto_clean', kwargs={k: v for k, v in _kw.items() if v is not None})

    def manifold_dispense(self, plate=None, volume=None, buffer=None, flow_rate=None, offset_x=None, offset_y=None, offset_z=None, pre_dispense_volume=None, pre_dispense_flow_rate=None, vacuum_delay_volume=None, **kwargs):
        _kw = {'plate': plate, 'volume': volume, 'buffer': buffer, 'flow_rate': flow_rate, 'offset_x': offset_x, 'offset_y': offset_y, 'offset_z': offset_z, 'pre_dispense_volume': pre_dispense_volume, 'pre_dispense_flow_rate': pre_dispense_flow_rate, 'vacuum_delay_volume': vacuum_delay_volume}
        _kw.update(kwargs)
        return self.call('manifold_dispense', kwargs={k: v for k, v in _kw.items() if v is not None})

    def manifold_prime(self, plate=None, volume=None, buffer=None, flow_rate=None, low_flow_volume=None, submerge_duration=None, **kwargs):
        _kw = {'plate': plate, 'volume': volume, 'buffer': buffer, 'flow_rate': flow_rate, 'low_flow_volume': low_flow_volume, 'submerge_duration': submerge_duration}
        _kw.update(kwargs)
        return self.call('manifold_prime', kwargs={k: v for k, v in _kw.items() if v is not None})

    def manifold_wash(self, plate=None, cycles=None, buffer=None, dispense_volume=None, dispense_flow_rate=None, dispense_x=None, dispense_y=None, dispense_z=None, aspirate_travel_rate=None, aspirate_z=None, pre_dispense_flow_rate=None, aspirate_delay=None, aspirate_x=None, aspirate_y=None, final_aspirate=None, final_aspirate_z=None, final_aspirate_x=None, final_aspirate_y=None, final_aspirate_delay=None, pre_dispense_volume=None, vacuum_delay_volume=None, soak_duration=None, shake_duration=None, shake_intensity=None, secondary_aspirate=None, secondary_z=None, secondary_x=None, secondary_y=None, final_secondary_aspirate=None, final_secondary_z=None, final_secondary_x=None, final_secondary_y=None, bottom_wash=None, bottom_wash_volume=None, bottom_wash_flow_rate=None, pre_dispense_between_cycles_volume=None, pre_dispense_between_cycles_flow_rate=None, wash_format=None, sectors=None, move_home_first=None, **kwargs):
        _kw = {'plate': plate, 'cycles': cycles, 'buffer': buffer, 'dispense_volume': dispense_volume, 'dispense_flow_rate': dispense_flow_rate, 'dispense_x': dispense_x, 'dispense_y': dispense_y, 'dispense_z': dispense_z, 'aspirate_travel_rate': aspirate_travel_rate, 'aspirate_z': aspirate_z, 'pre_dispense_flow_rate': pre_dispense_flow_rate, 'aspirate_delay': aspirate_delay, 'aspirate_x': aspirate_x, 'aspirate_y': aspirate_y, 'final_aspirate': final_aspirate, 'final_aspirate_z': final_aspirate_z, 'final_aspirate_x': final_aspirate_x, 'final_aspirate_y': final_aspirate_y, 'final_aspirate_delay': final_aspirate_delay, 'pre_dispense_volume': pre_dispense_volume, 'vacuum_delay_volume': vacuum_delay_volume, 'soak_duration': soak_duration, 'shake_duration': shake_duration, 'shake_intensity': shake_intensity, 'secondary_aspirate': secondary_aspirate, 'secondary_z': secondary_z, 'secondary_x': secondary_x, 'secondary_y': secondary_y, 'final_secondary_aspirate': final_secondary_aspirate, 'final_secondary_z': final_secondary_z, 'final_secondary_x': final_secondary_x, 'final_secondary_y': final_secondary_y, 'bottom_wash': bottom_wash, 'bottom_wash_volume': bottom_wash_volume, 'bottom_wash_flow_rate': bottom_wash_flow_rate, 'pre_dispense_between_cycles_volume': pre_dispense_between_cycles_volume, 'pre_dispense_between_cycles_flow_rate': pre_dispense_between_cycles_flow_rate, 'wash_format': wash_format, 'sectors': sectors, 'move_home_first': move_home_first}
        _kw.update(kwargs)
        return self.call('manifold_wash', kwargs={k: v for k, v in _kw.items() if v is not None})

    def pause(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('pause', kwargs={k: v for k, v in _kw.items() if v is not None})

    def peristaltic_dispense(self, plate=None, volume=None, flow_rate=None, offset_x=None, offset_y=None, offset_z=None, pre_dispense_volume=None, num_pre_dispenses=None, cassette=None, columns=None, rows=None, **kwargs):
        _kw = {'plate': plate, 'volume': volume, 'flow_rate': flow_rate, 'offset_x': offset_x, 'offset_y': offset_y, 'offset_z': offset_z, 'pre_dispense_volume': pre_dispense_volume, 'num_pre_dispenses': num_pre_dispenses, 'cassette': cassette, 'columns': columns, 'rows': rows}
        _kw.update(kwargs)
        return self.call('peristaltic_dispense', kwargs={k: v for k, v in _kw.items() if v is not None})

    def peristaltic_prime(self, plate=None, volume=None, duration=None, flow_rate=None, cassette=None, **kwargs):
        _kw = {'plate': plate, 'volume': volume, 'duration': duration, 'flow_rate': flow_rate, 'cassette': cassette}
        _kw.update(kwargs)
        return self.call('peristaltic_prime', kwargs={k: v for k, v in _kw.items() if v is not None})

    def peristaltic_purge(self, plate=None, volume=None, duration=None, flow_rate=None, cassette=None, **kwargs):
        _kw = {'plate': plate, 'volume': volume, 'duration': duration, 'flow_rate': flow_rate, 'cassette': cassette}
        _kw.update(kwargs)
        return self.call('peristaltic_purge', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_instrument_settings(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_instrument_settings', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_peristaltic_installed(self, selector=None, **kwargs):
        _kw = {'selector': selector}
        _kw.update(kwargs)
        return self.call('request_peristaltic_installed', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_sensor_enabled(self, sensor=None, **kwargs):
        _kw = {'sensor': sensor}
        _kw.update(kwargs)
        return self.call('request_sensor_enabled', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_serial_number(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_serial_number', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_syringe_box_info(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_syringe_box_info', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_syringe_manifold(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_syringe_manifold', kwargs={k: v for k, v in _kw.items() if v is not None})

    def request_washer_manifold(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('request_washer_manifold', kwargs={k: v for k, v in _kw.items() if v is not None})

    def reset(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('reset', kwargs={k: v for k, v in _kw.items() if v is not None})

    def resume(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('resume', kwargs={k: v for k, v in _kw.items() if v is not None})

    def run_self_check(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('run_self_check', kwargs={k: v for k, v in _kw.items() if v is not None})

    def set_washer_manifold(self, manifold=None, **kwargs):
        _kw = {'manifold': manifold}
        _kw.update(kwargs)
        return self.call('set_washer_manifold', kwargs={k: v for k, v in _kw.items() if v is not None})

    def setup(self, skip_reset=None, **kwargs):
        _kw = {'skip_reset': skip_reset}
        _kw.update(kwargs)
        return self.call('setup', kwargs={k: v for k, v in _kw.items() if v is not None})

    def shake(self, plate=None, duration=None, intensity=None, soak_duration=None, move_home_first=None, **kwargs):
        _kw = {'plate': plate, 'duration': duration, 'intensity': intensity, 'soak_duration': soak_duration, 'move_home_first': move_home_first}
        _kw.update(kwargs)
        return self.call('shake', kwargs={k: v for k, v in _kw.items() if v is not None})

    def start_batch(self, wire_byte=None, **kwargs):
        _kw = {'wire_byte': wire_byte}
        _kw.update(kwargs)
        return self.call('start_batch', kwargs={k: v for k, v in _kw.items() if v is not None})

    def stop(self, **kwargs):
        _kw = {}
        _kw.update(kwargs)
        return self.call('stop', kwargs={k: v for k, v in _kw.items() if v is not None})

    def syringe_dispense(self, plate=None, volume=None, syringe=None, flow_rate=None, offset_x=None, offset_y=None, offset_z=None, pump_delay=None, pre_dispense=None, pre_dispense_volume=None, num_pre_dispenses=None, columns=None, **kwargs):
        _kw = {'plate': plate, 'volume': volume, 'syringe': syringe, 'flow_rate': flow_rate, 'offset_x': offset_x, 'offset_y': offset_y, 'offset_z': offset_z, 'pump_delay': pump_delay, 'pre_dispense': pre_dispense, 'pre_dispense_volume': pre_dispense_volume, 'num_pre_dispenses': num_pre_dispenses, 'columns': columns}
        _kw.update(kwargs)
        return self.call('syringe_dispense', kwargs={k: v for k, v in _kw.items() if v is not None})

    def syringe_prime(self, plate=None, syringe=None, volume=None, flow_rate=None, refills=None, pump_delay=None, submerge_tips=None, submerge_duration=None, **kwargs):
        _kw = {'plate': plate, 'syringe': syringe, 'volume': volume, 'flow_rate': flow_rate, 'refills': refills, 'pump_delay': pump_delay, 'submerge_tips': submerge_tips, 'submerge_duration': submerge_duration}
        _kw.update(kwargs)
        return self.call('syringe_prime', kwargs={k: v for k, v in _kw.items() if v is not None})

