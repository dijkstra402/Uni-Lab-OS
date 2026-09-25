from __future__ import annotations

from unilabos.devices.generic.community_repo_loader import CommunityRepoLoader


class CommunityInstrumentAmetekVersastat(CommunityRepoLoader):
    DEFAULT_CONFIG = {'repo_root': '/Users/sml/work/Uni-Lab-OS/new/instrument_driver_repos/usnistgov__autoSDC-JOM', 'source_file': 'autoSDC/asdc/sdc/potentiostat.py', 'class_name': 'Potentiostat', 'import_roots': [], 'candidate_methods': ['check_overload', 'read_buffers', 'run', 'connect', 'disconnect', 'set_cell', 'choose_cell', 'set_mode', 'set_current_range', 'set_dc_potential', 'set_dc_current', 'set_ac_frequency', 'set_ac_amplitude', 'set_ac_waveform', 'update_status', 'latest_potential', 'latest_current', 'overload_status', 'booster_enabled', 'cell_enabled', 'autorange_current', 'actions', 'clear', 'start', 'stop', 'skip', 'sequence_running', 'points_available', 'last_open_circuit', 'potential', 'current', 'elapsed_time', 'applied_potential', 'segment', 'current_range_history', 'frequency', 'impedance_real', 'impedance_imag', 'hardcoded_open_circuit', 'measure_open_circuit'], 'action_targets': {}, 'metadata': {'repo': 'usnistgov/autoSDC-JOM', 'repo_url': 'https://github.com/usnistgov/autoSDC-JOM', 'brand': 'Ametek', 'model': 'VersaSTAT', 'device_type_cn': '电化学工作站', 'device_type_en': 'Potentiostat', 'source_framework': '独立驱动', 'tag_id': '4425', 'tag_name': '电化学工作站', 'tag_name_en': 'Electrochemical Workstation', 'candidate_score': 378, 'parse_status': 'ok', 'quality_status': 'usable', 'quality_reasons': [], 'action_targets': {}}}

    def __init__(self, **kwargs):
        merged = dict(self.DEFAULT_CONFIG)
        merged.update(kwargs)
        super().__init__(**merged)

    def check_overload(self, **kwargs):
        return self.call('check_overload', kwargs=kwargs)

    def read_buffers(self, **kwargs):
        return self.call('read_buffers', kwargs=kwargs)

    def run(self, **kwargs):
        return self.call('run', kwargs=kwargs)

    def connect(self, **kwargs):
        return self.call('connect', kwargs=kwargs)

    def disconnect(self, **kwargs):
        return self.call('disconnect', kwargs=kwargs)

    def set_cell(self, **kwargs):
        return self.call('set_cell', kwargs=kwargs)

    def choose_cell(self, **kwargs):
        return self.call('choose_cell', kwargs=kwargs)

    def set_mode(self, **kwargs):
        return self.call('set_mode', kwargs=kwargs)

    def set_current_range(self, **kwargs):
        return self.call('set_current_range', kwargs=kwargs)

    def set_dc_potential(self, **kwargs):
        return self.call('set_dc_potential', kwargs=kwargs)

    def set_dc_current(self, **kwargs):
        return self.call('set_dc_current', kwargs=kwargs)

    def set_ac_frequency(self, **kwargs):
        return self.call('set_ac_frequency', kwargs=kwargs)

    def set_ac_amplitude(self, **kwargs):
        return self.call('set_ac_amplitude', kwargs=kwargs)

    def set_ac_waveform(self, **kwargs):
        return self.call('set_ac_waveform', kwargs=kwargs)

    def update_status(self, **kwargs):
        return self.call('update_status', kwargs=kwargs)

    def latest_potential(self, **kwargs):
        return self.call('latest_potential', kwargs=kwargs)

    def latest_current(self, **kwargs):
        return self.call('latest_current', kwargs=kwargs)

    def overload_status(self, **kwargs):
        return self.call('overload_status', kwargs=kwargs)

    def booster_enabled(self, **kwargs):
        return self.call('booster_enabled', kwargs=kwargs)

    def cell_enabled(self, **kwargs):
        return self.call('cell_enabled', kwargs=kwargs)

    def autorange_current(self, **kwargs):
        return self.call('autorange_current', kwargs=kwargs)

    def actions(self, **kwargs):
        return self.call('actions', kwargs=kwargs)

    def clear(self, **kwargs):
        return self.call('clear', kwargs=kwargs)

    def start(self, **kwargs):
        return self.call('start', kwargs=kwargs)

    def stop(self, **kwargs):
        return self.call('stop', kwargs=kwargs)

    def skip(self, **kwargs):
        return self.call('skip', kwargs=kwargs)

    def sequence_running(self, **kwargs):
        return self.call('sequence_running', kwargs=kwargs)

    def points_available(self, **kwargs):
        return self.call('points_available', kwargs=kwargs)

    def last_open_circuit(self, **kwargs):
        return self.call('last_open_circuit', kwargs=kwargs)

    def potential(self, **kwargs):
        return self.call('potential', kwargs=kwargs)

    def current(self, **kwargs):
        return self.call('current', kwargs=kwargs)

    def elapsed_time(self, **kwargs):
        return self.call('elapsed_time', kwargs=kwargs)

    def applied_potential(self, **kwargs):
        return self.call('applied_potential', kwargs=kwargs)

    def segment(self, **kwargs):
        return self.call('segment', kwargs=kwargs)

    def current_range_history(self, **kwargs):
        return self.call('current_range_history', kwargs=kwargs)

    def frequency(self, **kwargs):
        return self.call('frequency', kwargs=kwargs)

    def impedance_real(self, **kwargs):
        return self.call('impedance_real', kwargs=kwargs)

    def impedance_imag(self, **kwargs):
        return self.call('impedance_imag', kwargs=kwargs)

    def hardcoded_open_circuit(self, **kwargs):
        return self.call('hardcoded_open_circuit', kwargs=kwargs)

    def measure_open_circuit(self, **kwargs):
        return self.call('measure_open_circuit', kwargs=kwargs)

